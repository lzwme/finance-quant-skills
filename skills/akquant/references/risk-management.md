# 风控配置指南

本文档详细说明 akquant 框架的风险管理机制，包括预交易风控、账户级风控与策略级风控。

## 目录

- [风控概述](#风控概述)
- [RiskConfig 配置](#riskconfig-配置)
- [Engine 层风控](#engine-层风控)
- [账户级风控](#账户级风控)
- [策略级风控](#策略级风控)
- [最佳实践](#最佳实践)

---

## 风控概述

akquant 内置了强大的预交易风控模块，支持在 Engine 层面拦截不合规的订单。风控系统采用"检查链"模式，每个规则独立判断，任一规则拒绝则订单被拦截。

### 风控层级

```
订单提交 → 单笔检查 → 持仓检查 → 账户检查 → 策略检查 → 提交成功
           ↓           ↓           ↓           ↓
         拒绝         拒绝        拒绝        拒绝
```

---

## RiskConfig 配置

### 基本配置

```python
from akquant.config import RiskConfig

risk_config = RiskConfig(
    active=True,                    # 是否启用风控
    safety_margin=0.0001,           # 安全垫
    max_order_size=10000,           # 单笔最大委托数量
    max_order_value=100_000.0,      # 单笔最大委托金额
    max_position_size=50000,        # 单标的最大持仓数量
    max_position_pct=0.10,          # 单标的持仓上限（占总权益）
    sector_concentration=0.20,      # 行业集中度限制
    restricted_list=["ST001", "ST002"],  # 禁止交易标的
    max_account_drawdown=0.20,      # 账户最大回撤
    max_daily_loss=0.05,            # 单日最大亏损
    stop_loss_threshold=0.80,       # 账户净值止损阈值
)
```

### 通过 run_backtest 配置

```python
from akquant import run_backtest
from akquant.config import RiskConfig

result = run_backtest(
    strategy=MyStrategy,
    data=df,
    risk_config=RiskConfig(
        max_position_pct=0.10,
        max_account_drawdown=0.20,
    ),
)
```

### 通过 BacktestConfig 配置

```python
from akquant import BacktestConfig, StrategyConfig, run_backtest
from akquant.config import RiskConfig

config = BacktestConfig(
    strategy_config=StrategyConfig(
        initial_cash=500_000.0,
        risk=RiskConfig(
            max_position_pct=0.10,
            max_account_drawdown=0.20,
        ),
    ),
)

result = run_backtest(strategy=MyStrategy, data=df, config=config)
```

---

## Engine 层风控

### 获取 RiskManager

```python
from akquant import Engine

engine = Engine()
# ... 添加数据 ...

rm = engine.risk_manager
```

### 单标的持仓上限

```python
# 某标的持仓市值不超过总权益的 10%
rm.add_max_position_percent_rule(0.10)
```

### 行业集中度限制

```python
# 单行业持仓不超过总权益的 20%
sector_map = {
    "AAPL": "Tech",
    "MSFT": "Tech",
    "XOM": "Energy",
    "JPM": "Finance",
}
rm.add_sector_concentration_rule(0.20, sector_map)
```

### 杠杆率熔断

```python
# 总敞口 / 总权益 > 1.5 时拒绝开仓
rm.config.check_cash = False  # 关闭现金检查（高杠杆策略）
rm.add_max_leverage_rule(1.5)
```

### 应用配置

```python
# 修改后必须赋值回去
engine.risk_manager = rm
```

---

## 账户级风控

账户级风控在订单提交前检查账户状态，触发后拒绝新的下单请求。

### 最大回撤限制

```python
risk_config = RiskConfig(
    max_account_drawdown=0.20,  # 最大回撤 20%
)
```

**规则说明**：
- 以历史权益峰值为基准
- 当前权益回撤超过阈值后，新的下单请求被拒绝
- 已有持仓不受影响，仅阻止新开仓

### 单日亏损限制

```python
risk_config = RiskConfig(
    max_daily_loss=0.05,  # 单日亏损 5%
)
```

**规则说明**：
- 以当日首次风控检查时的权益为基准
- 当日亏损超过阈值后，新的下单请求被拒绝
- 次日重置基准

### 账户净值止损

```python
risk_config = RiskConfig(
    stop_loss_threshold=0.80,  # 跌至初始权益 80% 时触发
)
```

**规则说明**：
- 当前权益 < 规则首次生效时权益 × 阈值时触发
- 触发后新的下单请求被拒绝
- 永久生效，不会重置

### 参数建议

| 风格 | `max_account_drawdown` | `max_daily_loss` | `stop_loss_threshold` |
|------|------------------------|------------------|------------------------|
| 保守 | 0.10 | 0.02 | 0.90 |
| 中性 | 0.20 | 0.05 | 0.80 |
| 激进 | 0.30 | 0.08 | 0.70 |

---

## 策略级风控

多策略场景下，支持为每个策略设置独立的风控规则。

### 配置策略级风控

```python
from akquant import BacktestConfig, StrategyConfig, run_backtest

config = BacktestConfig(
    strategy_config=StrategyConfig(
        strategy_id="alpha",
        strategies_by_slot={"beta": BetaStrategy},
        
        # 策略级持仓限制
        strategy_max_order_size={"alpha": 10, "beta": 20},
        strategy_max_position_size={"alpha": 100, "beta": 200},
        strategy_max_order_value={"alpha": 5000, "beta": 10000},
        
        # 策略级亏损限制
        strategy_max_daily_loss={"alpha": 0.03, "beta": 0.05},
        strategy_max_drawdown={"alpha": 0.15, "beta": 0.20},
        
        # 风控后动作
        strategy_reduce_only_after_risk={"alpha": True, "beta": False},
        strategy_risk_cooldown_bars={"alpha": 2, "beta": 0},
        
        # 优先级
        strategy_priority={"alpha": 1, "beta": 2},
    ),
)

result = run_backtest(strategy=AlphaStrategy, data=df, config=config)
```

### 风控后动作

**仅平仓模式**：

```python
strategy_reduce_only_after_risk={"alpha": True}
```

- 风控触发后，该策略只能提交平仓订单
- 开仓订单会被拒绝

**冷却期**：

```python
strategy_risk_cooldown_bars={"alpha": 2}
```

- 风控触发后，该策略在 N 个 Bar 内无法下单
- 冷却期结束后恢复正常

---

## 最佳实践

### 1. 分层配置

```python
# 账户级：全局底线
risk_config = RiskConfig(
    max_account_drawdown=0.20,  # 账户最大回撤 20%
    max_daily_loss=0.05,        # 单日最大亏损 5%
)

# 策略级：策略约束
strategy_config = StrategyConfig(
    strategy_max_position_size={"alpha": 100},
    strategy_max_daily_loss={"alpha": 0.03},
)
```

### 2. 监控拒单原因

```python
result = run_backtest(...)

# 查看所有被拒订单
rejected = result.orders_df[result.orders_df["status"] == "Rejected"]
print(rejected[["symbol", "side", "quantity", "reject_reason"]])
```

**常见拒单原因**：
- `Insufficient cash`：资金不足
- `Exceeds max position percent`：超过持仓上限
- `Exceeds sector concentration`：超过行业集中度
- `Account drawdown exceeded`：触发账户回撤限制
- `Daily loss limit exceeded`：触发单日亏损限制
- `Insufficient available position`：可用持仓不足（T+1）

### 3. 风控触发日志

```python
class MyStrategy(Strategy):
    def on_reject(self, order):
        self.log(f"订单被拒: {order.symbol} {order.side} 原因: {order.reject_reason}")
```

### 4. 动态调整风控

```python
class AdaptiveRiskStrategy(Strategy):
    def on_bar(self, bar):
        # 根据市场波动动态调整风控
        volatility = self.calculate_volatility()
        
        if volatility > 0.03:
            # 高波动：收紧风控
            self.ctx.risk_manager.config.max_position_pct = 0.05
        else:
            # 低波动：放宽风控
            self.ctx.risk_manager.config.max_position_pct = 0.10
```

### 5. 回测前验证

```python
# 在策略类中定义参数模型
from akquant import ParamModel, IntParam, FloatParam

class StrategyParams(ParamModel):
    max_position_pct: float = FloatParam(0.10, ge=0.01, le=1.0)
    max_drawdown: float = FloatParam(0.20, ge=0.05, le=0.50)

class MyStrategy(Strategy):
    PARAM_MODEL = StrategyParams
    
    def __init__(self, max_position_pct=0.10, max_drawdown=0.20):
        self.max_position_pct = max_position_pct
        self.max_drawdown = max_drawdown
```

---

## 完整示例

```python
from akquant import Strategy, Bar, run_backtest, BacktestConfig, StrategyConfig
from akquant.config import RiskConfig
import numpy as np

class RiskManagedStrategy(Strategy):
    warmup_period = 30
    
    def __init__(self, ma_window=20, stop_loss=0.05):
        self.ma_window = ma_window
        self.stop_loss = stop_loss
        self.entry_prices = {}
    
    def on_start(self):
        self.subscribe("600000")
    
    def on_bar(self, bar):
        closes = self.get_history(self.ma_window, bar.symbol, "close")
        if len(closes) < self.ma_window:
            return
        
        ma = np.mean(closes)
        pos = self.get_position(bar.symbol)
        
        # 开仓
        if bar.close > ma * 1.02 and pos == 0:
            self.buy(bar.symbol, 100)
            self.entry_prices[bar.symbol] = bar.close
            self.log(f"开仓: {bar.symbol} @ {bar.close}")
        
        # 止损
        elif bar.symbol in self.entry_prices:
            entry = self.entry_prices[bar.symbol]
            pnl_pct = (bar.close - entry) / entry
            
            if pnl_pct < -self.stop_loss:
                self.sell(bar.symbol, pos)
                del self.entry_prices[bar.symbol]
                self.log(f"止损: {bar.symbol} @ {bar.close}, PnL: {pnl_pct:.2%}")
    
    def on_reject(self, order):
        self.log(f"订单被拒: {order.reject_reason}", level=40)

# 运行回测
config = BacktestConfig(
    strategy_config=StrategyConfig(
        initial_cash=500_000.0,
        commission_rate=0.0003,
        t_plus_one=True,
        risk=RiskConfig(
            max_position_pct=0.20,       # 单标的不超过 20%
            max_account_drawdown=0.15,   # 最大回撤 15%
            max_daily_loss=0.03,         # 单日亏损 3%
        ),
    ),
)

result = run_backtest(
    strategy=RiskManagedStrategy,
    data=df,
    symbol="600000",
    config=config,
)

# 检查拒单
rejected = result.orders_df[result.orders_df["status"] == "Rejected"]
if len(rejected) > 0:
    print("被拒订单:")
    print(rejected[["timestamp", "symbol", "side", "reject_reason"]])
```
