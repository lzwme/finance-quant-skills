# 策略编写范式

本文档提供 akquant 框架的策略编写范式，涵盖策略结构设计、生命周期管理、指标计算与常见陷阱。

## 目录

- [策略风格选择](#策略风格选择)
- [策略生命周期](#策略生命周期)
- [数据预热机制](#数据预热机制)
- [历史数据访问](#历史数据访问)
- [指标计算](#指标计算)
- [常见策略范式](#常见策略范式)
- [常见陷阱](#常见陷阱)

---

## 策略风格选择

akquant 提供两种策略编写风格：

| 特性 | 类风格（推荐） | 函数风格 |
|------|----------------|----------|
| **定义方式** | 继承 `Strategy` | `initialize` + `on_bar` |
| **适用场景** | 复杂策略、生产环境 | 快速原型、迁移旧代码 |
| **代码结构** | 面向对象、封装性好 | 脚本化、简单直观 |
| **API 调用** | `self.buy()` | `ctx.buy()` |

**推荐**：优先使用类风格，便于维护和扩展。

### 类风格示例

```python
from akquant import Strategy, Bar
import numpy as np

class MyStrategy(Strategy):
    warmup_period = 20
    
    def __init__(self, ma_window=20):
        self.ma_window = ma_window
        self.warmup_period = ma_window + 1
    
    def on_start(self):
        self.subscribe("600000")
    
    def on_bar(self, bar: Bar):
        history = self.get_history(self.ma_window, bar.symbol, "close")
        if len(history) < self.ma_window:
            return
        
        ma = np.mean(history)
        pos = self.get_position(bar.symbol)
        
        if bar.close > ma and pos == 0:
            self.buy(bar.symbol, 100)
        elif bar.close < ma and pos > 0:
            self.sell(bar.symbol, pos)
```

### 函数风格示例

```python
from akquant import run_backtest

def initialize(ctx):
    ctx.ma_window = 20

def on_bar(ctx, bar):
    history = ctx.get_history(ctx.ma_window, bar.symbol, "close")
    if len(history) < ctx.ma_window:
        return
    
    import numpy as np
    ma = np.mean(history)
    pos = ctx.get_position(bar.symbol)
    
    if bar.close > ma and pos == 0:
        ctx.buy(bar.symbol, 100)
    elif bar.close < ma and pos > 0:
        ctx.sell(bar.symbol, pos)

run_backtest(strategy=on_bar, initialize=initialize, data=df)
```

---

## 策略生命周期

### 完整生命周期流程

```
__init__ → on_start → [on_resume] → [on_bar / on_tick / on_timer] → on_stop
                           ↑
                     （仅热启动时）
```

### 各阶段职责

| 阶段 | 职责 | 注意事项 |
|------|------|----------|
| `__init__` | 定义参数、初始化变量 | 不要调用交易 API |
| `on_start` | 订阅数据、注册指标 | **必须**调用 `self.subscribe()` |
| `on_resume` | 处理快照恢复逻辑 | 仅热启动时调用，在 `on_start` 之前 |
| `on_bar` | 核心交易逻辑 | 检查数据长度再计算 |
| `on_order` | 监控订单状态 | 先于 `on_bar` 触发 |
| `on_trade` | 处理成交回报 | 与 `on_order` 配合使用 |
| `on_timer` | 定时调仓 | 横截面策略推荐使用 |
| `on_stop` | 资源清理、结果统计 | 无需手动平仓 |

### 热启动适配

```python
class WarmStartStrategy(Strategy):
    def __init__(self):
        self.sma = None
    
    def on_start(self):
        if not self.is_restored:
            # 冷启动：初始化指标
            self.sma = SMA(30)
        else:
            # 热启动：指标已从快照恢复
            self.log("Resumed from snapshot")
        
        # 必须执行：注册指标
        self.register_indicator("sma", self.sma)
        self.subscribe("AAPL")
```

---

## 数据预热机制

### 为什么需要预热？

计算技术指标（如 MA、RSI）需要一定长度的历史数据。预热机制确保策略在正式开始交易前，已经加载了足够的历史数据。

### 设置预热期

**静态设置（推荐）**：

```python
class MyStrategy(Strategy):
    warmup_period = 20  # 类属性
```

**动态设置**：

```python
class MyStrategy(Strategy):
    def __init__(self, ma_window=20):
        self.ma_window = ma_window
        self.warmup_period = ma_window + 5  # 动态计算
```

**预热期计算规则**：
- 单均线策略：`warmup_period = ma_window`
- 双均线策略：`warmup_period = max(fast, slow)`
- 带波动率策略：`warmup_period = max(ma_window, volatility_window)`

### 预热期内的行为

- 预热期内：`on_bar` 正常触发，但历史数据长度可能不足
- 建议：在 `on_bar` 开头检查 `len(history) >= required_length`

```python
def on_bar(self, bar):
    history = self.get_history(20, bar.symbol, "close")
    if len(history) < 20:
        return  # 数据不足，跳过
    # ... 正常逻辑
```

---

## 历史数据访问

### get_history

返回 `numpy.ndarray`，性能最高。

```python
# 获取最近 20 根 Bar 的收盘价
closes = self.get_history(count=20, symbol="AAPL", field="close")
# 返回: array([close_t-19, ..., close_t-1, close_t])

# 可用字段
closes = self.get_history(20, symbol, "close")
opens = self.get_history(20, symbol, "open")
highs = self.get_history(20, symbol, "high")
lows = self.get_history(20, symbol, "low")
volumes = self.get_history(20, symbol, "volume")
```

### get_history_df

返回 `pandas.DataFrame`，适合复杂分析。

```python
df = self.get_history_df(count=20, symbol="AAPL")
# 列: timestamp, open, high, low, close, volume, symbol

# 示例：计算波动率
import numpy as np
df = self.get_history_df(20, bar.symbol)
volatility = df["close"].pct_change().std()
```

### 访问当前 Bar 数据

```python
def on_bar(self, bar):
    # 方式 1：通过 Bar 对象
    close = bar.close
    volume = bar.volume
    
    # 方式 2：通过快捷属性
    close = self.close
    open_price = self.open
    high = self.high
    low = self.low
    volume = self.volume
    symbol = self.symbol
```

### 访问自定义因子

```python
# 在 DataFrame 中添加因子
df["momentum"] = df["close"] / df["open"]
df["sentiment"] = sentiment_scores

# 在策略中访问
def on_bar(self, bar):
    mom = bar.extra.get("momentum", 0.0)
    sentiment = bar.extra.get("sentiment", 0.5)
```

---

## 指标计算

### 使用 numpy 手动计算

```python
import numpy as np

def on_bar(self, bar):
    closes = self.get_history(20, bar.symbol, "close")
    if len(closes) < 20:
        return
    
    # 简单移动平均
    ma = np.mean(closes)
    
    # 标准差
    std = np.std(closes)
    
    # 布林带
    upper = ma + 2 * std
    lower = ma - 2 * std
    
    # RSI
    returns = np.diff(closes)
    gains = np.where(returns > 0, returns, 0)
    losses = np.where(returns < 0, -returns, 0)
    avg_gain = np.mean(gains[-14:])
    avg_loss = np.mean(losses[-14:])
    rs = avg_gain / (avg_loss + 1e-10)
    rsi = 100 - (100 / (1 + rs))
```

### 使用内置指标

```python
from akquant import SMA, EMA, RSI

class IndicatorStrategy(Strategy):
    def __init__(self):
        self.indicator_mode = "precompute"
        self.sma20 = SMA(20)
        self.rsi14 = RSI(14)
        self.register_precomputed_indicator("sma20", self.sma20)
        self.register_precomputed_indicator("rsi14", self.rsi14)
    
    def on_bar(self, bar):
        sma_val = self.sma20.get_value(bar.symbol, bar.timestamp)
        rsi_val = self.rsi14.get_value(bar.symbol, bar.timestamp)
```

---

## 常见策略范式

### 趋势跟踪策略

```python
class TrendFollowing(Strategy):
    warmup_period = 30
    
    def __init__(self, fast=10, slow=20):
        self.fast = fast
        self.slow = slow
        self.warmup_period = slow + 1
    
    def on_bar(self, bar):
        fast_ma = np.mean(self.get_history(self.fast, bar.symbol, "close"))
        slow_ma = np.mean(self.get_history(self.slow, bar.symbol, "close"))
        
        pos = self.get_position(bar.symbol)
        if fast_ma > slow_ma and pos == 0:
            self.buy(bar.symbol, 100)
        elif fast_ma < slow_ma and pos > 0:
            self.sell(bar.symbol, pos)
```

### 均值回归策略

```python
class MeanReversion(Strategy):
    warmup_period = 20
    
    def __init__(self, window=20, z_threshold=2.0):
        self.window = window
        self.z_threshold = z_threshold
    
    def on_bar(self, bar):
        closes = self.get_history(self.window, bar.symbol, "close")
        if len(closes) < self.window:
            return
        
        mean = np.mean(closes)
        std = np.std(closes)
        z_score = (bar.close - mean) / std
        
        pos = self.get_position(bar.symbol)
        if z_score < -self.z_threshold and pos == 0:
            self.buy(bar.symbol, 100)
        elif z_score > self.z_threshold and pos > 0:
            self.sell(bar.symbol, pos)
```

### 带止损止盈的策略

```python
class StrategyWithStopLoss(Strategy):
    warmup_period = 20
    
    def __init__(self, stop_loss=0.05, take_profit=0.10):
        self.stop_loss = stop_loss
        self.take_profit = take_profit
        self.entry_price = {}
    
    def on_bar(self, bar):
        # ... 开仓逻辑
        if buy_signal and pos == 0:
            self.buy(bar.symbol, 100)
            self.entry_price[bar.symbol] = bar.close
        
        # 止损止盈
        if bar.symbol in self.entry_price:
            entry = self.entry_price[bar.symbol]
            pnl_pct = (bar.close - entry) / entry
            
            if pnl_pct <= -self.stop_loss or pnl_pct >= self.take_profit:
                self.sell(bar.symbol, pos)
                del self.entry_price[bar.symbol]
```

---

## 常见陷阱

### 1. 预热期不足

```python
# ❌ 错误：warmup_period 小于指标窗口
class BadStrategy(Strategy):
    warmup_period = 10
    
    def on_bar(self, bar):
        history = self.get_history(20, bar.symbol, "close")  # 需要 20 根
        ma = np.mean(history)  # 实际可能只有 10 根，导致错误

# ✅ 正确：warmup_period >= 最大窗口
class GoodStrategy(Strategy):
    warmup_period = 25  # 留出缓冲
    
    def on_bar(self, bar):
        history = self.get_history(20, bar.symbol, "close")
        if len(history) < 20:
            return
        ma = np.mean(history)
```

### 2. T+1 规则未区分

```python
# ❌ 错误：T+1 模式下用总持仓判断
def on_bar(self, bar):
    pos = self.get_position(bar.symbol)  # 总持仓
    if sell_signal and pos > 0:
        self.sell(bar.symbol, pos)  # 可能卖出今日买入的部分

# ✅ 正确：T+1 模式下用可用持仓
def on_bar(self, bar):
    available = self.get_available_position(bar.symbol)  # 可卖数量
    if sell_signal and available > 0:
        self.sell(bar.symbol, available)
```

### 3. 未检查数据长度

```python
# ❌ 错误：直接计算，可能因数据不足报错
def on_bar(self, bar):
    history = self.get_history(20, bar.symbol, "close")
    ma = np.mean(history)  # 如果 history 长度 < 20 会怎样？

# ✅ 正确：防御性检查
def on_bar(self, bar):
    history = self.get_history(20, bar.symbol, "close")
    if len(history) < 20:
        return
    ma = np.mean(history)
```

### 4. 订单未成交就重复下单

```python
# ❌ 错误：每个 Bar 都下单，导致重复
def on_bar(self, bar):
    if buy_signal:
        self.buy(bar.symbol, 100)  # 每个 Bar 都会买

# ✅ 正确：检查持仓或挂单
def on_bar(self, bar):
    pos = self.get_position(bar.symbol)
    open_orders = self.get_open_orders(bar.symbol)
    
    if buy_signal and pos == 0 and len(open_orders) == 0:
        self.buy(bar.symbol, 100)
```

### 5. on_start 未订阅数据

```python
# ❌ 错误：忘记订阅
class BadStrategy(Strategy):
    def on_start(self):
        pass  # 未订阅
    
    def on_bar(self, bar):
        # 永远不会触发

# ✅ 正确：显式订阅
class GoodStrategy(Strategy):
    def on_start(self):
        self.subscribe("600000")
    
    def on_bar(self, bar):
        # 正常触发
```

---

## 最佳实践清单

1. **预热期**：设置为最大指标窗口 + 缓冲（如 +5）
2. **数据检查**：`on_bar` 开头检查 `len(history) >= required`
3. **T+1 规则**：A股策略设置 `t_plus_one=True`，用 `available_position`
4. **订单管理**：开仓前检查持仓和挂单，避免重复下单
5. **日志记录**：关键决策点使用 `self.log()` 记录
6. **参数命名**：使用 `PARAM_MODEL` 定义参数，支持页面化配置
7. **风控配置**：生产策略必须配置风控规则
8. **异常处理**：重写 `on_error` 处理回调异常
