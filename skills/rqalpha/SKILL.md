---
name: rqalpha
description: RQAlpha 米筐开源事件驱动回测框架。支持A股和期货，模块化架构，可自由扩展；当用户需要使用 rqalpha 进行策略回测、模拟交易或Mod插件开发时使用。
metadata: {"clawdbot":{"emoji":"📈","requires":{"bins":["python3"]}}}
---

# RQAlpha（米筐开源回测框架）

[RQAlpha](https://github.com/ricequant/rqalpha) 是 [米筐科技](https://www.ricequant.com) 开发的开源事件驱动回测框架。提供A股和期货市场的策略开发、回测和模拟交易完整解决方案。高度模块化，支持插件（Mod）系统扩展。

> 文档：https://rqalpha.readthedocs.io

## 安装

```bash
pip install rqalpha

# 下载内置数据包（A股日线数据）
rqalpha download-bundle

# 验证安装
python -c "import rqalpha; print(rqalpha.__version__)"
```

## 策略结构

```python
from rqalpha.api import *  # 导入所有 API 函数（含 logger）

def init(context):
    """策略启动时调用一次 — 设置订阅和参数"""
    context.stock = '000001.XSHE'
    context.fired = False

def handle_bar(context, bar_dict):
    """每根K线调用 — 主要交易逻辑"""
    if not context.fired:
        order_shares(context.stock, 1000)
        context.fired = True
        logger.info('买入完成')  # logger 通过 from rqalpha.api import * 自动可用

def before_trading(context):
    """每个交易日开盘前调用"""
    pass

def after_trading(context):
    """每个交易日收盘后调用"""
    pass
```

> **注意**：`from rqalpha.api import *` 会自动导入 `logger`，可直接使用 `logger.info()`、`logger.warn()`、`logger.error()` 输出日志。

## 运行回测

### 命令行

```bash
rqalpha run \
    -f strategy.py \
    -s 2024-01-01 \
    -e 2024-06-30 \
    --account stock 100000 \
    --benchmark 000300.XSHG \
    --plot
```

### Python API

```python
from rqalpha.api import *
from rqalpha import run_func

config = {
    "base": {
        "start_date": "2024-01-01",
        "end_date": "2024-06-30",
        "accounts": {"stock": 100000},
        "benchmark": "000300.XSHG",
        "frequency": "1d",
    },
    "extra": {
        "log_level": "warning",
    },
    "mod": {
        "sys_analyser": {"enabled": True, "plot": True},
    },
}

result = run_func(init=init, handle_bar=handle_bar, config=config)
print(result)
```

---

## 代码格式

| 市场 | 后缀 | 示例 |
|---|---|---|
| 上海A股 | `.XSHG` | `600000.XSHG`（浦发银行） |
| 深圳A股 | `.XSHE` | `000001.XSHE`（平安银行） |
| 指数 | `.XSHG/.XSHE` | `000300.XSHG`（沪深300） |
| 期货 | `.XSGE/.XDCE/.XZCE/.CCFX` | `IF2401.CCFX`（沪深300期货） |

---

## 下单函数

### 股票下单

```python
# 按股数买卖
order_shares('000001.XSHE', 1000)       # 买入1000股
order_shares('000001.XSHE', -500)       # 卖出500股

# 按手买入（1手=100股）
order_lots('000001.XSHE', 10)           # 买入10手（1000股）

# 按金额买入
order_value('000001.XSHE', 50000)       # 买入5万元

# 按组合比例买入
order_percent('000001.XSHE', 0.5)       # 买入组合值50%的仓位

# 目标仓位
order_target_value('000001.XSHE', 100000)   # 调整到10万元
order_target_percent('000001.XSHE', 0.3)    # 调整到组合的30%

# 撤单
cancel_order(order_id)
```

### 期货下单

```python
# 开仓
buy_open('IF2401.CCFX', 1)              # 买入开多1手
sell_open('IF2401.CCFX', 1)             # 卖出开空1手

# 平仓
sell_close('IF2401.CCFX', 1)            # 卖出平多1手
buy_close('IF2401.CCFX', 1)             # 买入平空1手
```

## 数据查询函数

```python
def handle_bar(context, bar_dict):
    # 当前K线数据
    bar = bar_dict['000001.XSHE']
    price = bar.close
    volume = bar.volume
    dt = bar.datetime

    # 历史数据（返回DataFrame）
    prices = history_bars('000001.XSHE', bar_count=20, frequency='1d',
                          fields=['close', 'volume', 'open', 'high', 'low'])

    # 检查股票是否可交易
    tradable = is_valid_price(bar.close)

    # 检查是否停牌
    suspended = is_suspended('000001.XSHE')
```

## 投资组合与持仓

```python
def handle_bar(context, bar_dict):
    # 组合信息
    cash = context.portfolio.cash                    # 可用资金
    total = context.portfolio.total_value            # 总资产
    market_value = context.portfolio.market_value    # 持仓市值
    pnl = context.portfolio.pnl                      # 总盈亏
    returns = context.portfolio.daily_returns        # 日收益率

    # 持仓信息
    positions = context.portfolio.positions
    for stock, pos in positions.items():
        print(f'{stock}: quantity={pos.quantity}, '
              f'sellable={pos.sellable}, '
              f'avg_price={pos.avg_price:.2f}, '
              f'market_value={pos.market_value:.2f}, '
              f'pnl={pos.pnl:.2f}')
```

## 定时调度

```python
from rqalpha.api import *

def init(context):
    # 每个交易日指定时间运行函数
    scheduler.run_daily(rebalance, time_rule=market_open(minute=5))
    # 每周运行（每周一）
    scheduler.run_weekly(weekly_task, tradingday=1, time_rule=market_open(minute=5))
    # 每月运行（首个交易日）
    scheduler.run_monthly(monthly_task, tradingday=1, time_rule=market_open(minute=5))

def rebalance(context, bar_dict):
    pass
```

---

## Mod系统（插件）

RQAlpha的模块化架构允许通过Mod扩展功能：

```python
config = {
    "mod": {
        "sys_analyser": {
            "enabled": True,
            "plot": True,
            "benchmark": "000300.XSHG",
        },
        "sys_simulation": {
            "enabled": True,
            "matching_type": "current_bar",    # 撮合方式：current_bar（当前Bar）或 next_bar（下一Bar）
            "slippage": 0.01,                  # 滑点（元）
        },
        "sys_transaction_cost": {
            "enabled": True,
            "commission_rate": 0.0003,         # 手续费率
            "tax_rate": 0.001,                 # 印花税（仅卖出）
            "min_commission": 5,               # 最低手续费
        },
    },
}
```

### 可用内置Mod

| Mod | 说明 |
|---|---|
| `sys_analyser` | 绩效分析和图表绘制 |
| `sys_simulation` | 撮合模拟 |
| `sys_transaction_cost` | 手续费和税费计算 |
| `sys_accounts` | 账户管理 |
| `sys_benchmark` | 基准追踪 |
| `sys_progress` | 进度条显示 |
| `sys_risk` | 风险管理检查 |

---

## 进阶示例

### 双均线交叉策略

```python
import numpy as np
from rqalpha.api import *

def init(context):
    context.stock = '600000.XSHG'
    context.fast = 5
    context.slow = 20
    scheduler.run_daily(trade_logic, time_rule=market_open(minute=5))

def trade_logic(context, bar_dict):
    prices = history_bars(context.stock, context.slow + 1, '1d', fields=['close'])
    if len(prices) < context.slow:
        return

    closes = prices['close']
    fast_ma = np.mean(closes[-context.fast:])
    slow_ma = np.mean(closes[-context.slow:])

    pos = context.portfolio.positions.get(context.stock)
    has_position = pos is not None and pos.quantity > 0

    if fast_ma > slow_ma and not has_position:
        order_target_percent(context.stock, 0.9)
        logger.info(f'买入: 快线={fast_ma:.2f} > 慢线={slow_ma:.2f}')
    elif fast_ma < slow_ma and has_position:
        order_target_percent(context.stock, 0)
        logger.info(f'卖出: 快线={fast_ma:.2f} < 慢线={slow_ma:.2f}')

def handle_bar(context, bar_dict):
    pass
```

### 多股等权重调仓

```python
from rqalpha.api import *

def init(context):
    context.stocks = ['600000.XSHG', '000001.XSHE', '601318.XSHG',
                       '600036.XSHG', '000858.XSHE']
    scheduler.run_monthly(rebalance, tradingday=1, time_rule=market_open(minute=30))

def rebalance(context, bar_dict):
    # 卖出不在目标列表中的股票
    for stock in list(context.portfolio.positions.keys()):
        if stock not in context.stocks:
            order_target_percent(stock, 0)

    # 等权分配
    weight = 0.95 / len(context.stocks)
    for stock in context.stocks:
        if not is_suspended(stock):
            order_target_percent(stock, weight)
            logger.info(f'调仓: {stock} -> {weight:.1%}')

def handle_bar(context, bar_dict):
    pass
```

### RSI均值回归策略

```python
import numpy as np
from rqalpha.api import *

def init(context):
    context.stock = '000001.XSHE'
    context.rsi_period = 14
    context.oversold = 30
    context.overbought = 70

def handle_bar(context, bar_dict):
    prices = history_bars(context.stock, context.rsi_period + 2, '1d', fields=['close'])
    if len(prices) < context.rsi_period + 1:
        return

    closes = prices['close']
    deltas = np.diff(closes)
    gains = np.where(deltas > 0, deltas, 0)
    losses = np.where(deltas < 0, -deltas, 0)
    avg_gain = np.mean(gains[-context.rsi_period:])
    avg_loss = np.mean(losses[-context.rsi_period:])

    if avg_loss == 0:
        rsi = 100
    else:
        rsi = 100 - 100 / (1 + avg_gain / avg_loss)

    pos = context.portfolio.positions.get(context.stock)
    has_pos = pos is not None and pos.quantity > 0

    if rsi < context.oversold and not has_pos:
        order_target_percent(context.stock, 0.9)
        logger.info(f'RSI={rsi:.1f} 超卖买入')
    elif rsi > context.overbought and has_pos:
        order_target_percent(context.stock, 0)
        logger.info(f'RSI={rsi:.1f} 超买卖出')
```

### 止损止盈策略

```python
from rqalpha.api import *
import numpy as np

def init(context):
    context.stock = '600519.XSHG'
    context.entry_price = 0
    context.stop_loss = 0.05
    context.take_profit = 0.15
    scheduler.run_daily(trade, time_rule=market_open(minute=5))

def trade(context, bar_dict):
    bar = bar_dict[context.stock]
    price = bar.close
    prices = history_bars(context.stock, 21, '1d', fields=['close'])
    ma20 = np.mean(prices['close'][-20:])

    pos = context.portfolio.positions.get(context.stock)
    has_pos = pos is not None and pos.quantity > 0

    if not has_pos:
        if price > ma20:
            order_target_percent(context.stock, 0.9)
            context.entry_price = price
            logger.info(f'买入: 价格={price:.2f}, 均线={ma20:.2f}')
    else:
        if context.entry_price > 0:
            pnl = (price - context.entry_price) / context.entry_price
            if pnl <= -context.stop_loss:
                order_target_percent(context.stock, 0)
                logger.info(f'止损: 收益率={pnl:.2%}')
                context.entry_price = 0
            elif pnl >= context.take_profit:
                order_target_percent(context.stock, 0)
                logger.info(f'止盈: 收益率={pnl:.2%}')
                context.entry_price = 0

def handle_bar(context, bar_dict):
    pass
```

### 期货双均线CTA策略

```python
import numpy as np
from rqalpha.api import *

def init(context):
    context.symbol = 'IF2401.CCFX'
    context.fast = 5
    context.slow = 20

def handle_bar(context, bar_dict):
    prices = history_bars(context.symbol, context.slow + 1, '1d', fields=['close'])
    if len(prices) < context.slow:
        return

    closes = prices['close']
    fast_ma = np.mean(closes[-context.fast:])
    slow_ma = np.mean(closes[-context.slow:])
    prev_fast = np.mean(closes[-context.fast-1:-1])
    prev_slow = np.mean(closes[-context.slow-1:-1])

    pos = context.portfolio.positions.get(context.symbol)
    long_qty = pos.buy_quantity if pos else 0

    if prev_fast <= prev_slow and fast_ma > slow_ma and long_qty == 0:
        buy_open(context.symbol, 1)
        logger.info(f'开多: 快线={fast_ma:.2f} > 慢线={slow_ma:.2f}')
    elif prev_fast >= prev_slow and fast_ma < slow_ma and long_qty > 0:
        sell_close(context.symbol, long_qty)
        logger.info(f'平多: 快线={fast_ma:.2f} < 慢线={slow_ma:.2f}')
```

---

## 绩效分析输出

运行回测后，`sys_analyser` Mod会输出以下指标：

| 指标 | 说明 |
|------|------|
| `total_returns` | 总收益率 |
| `annualized_returns` | 年化收益率 |
| `benchmark_total_returns` | 基准总收益率 |
| `alpha` | Alpha值 |
| `beta` | Beta值 |
| `sharpe` | 夏普比率 |
| `sortino` | Sortino比率 |
| `max_drawdown` | 最大回撤 |
| `tracking_error` | 跟踪误差 |
| `information_ratio` | 信息比率 |
| `volatility` | 波动率 |

## 常见错误处理

| 错误 | 原因 | 解决方法 |
|------|------|----------|
| `Bundle not found` | 未下载数据包 | 运行 `rqalpha download-bundle` |
| `Insufficient cash` | 可用资金不足 | 检查 `context.portfolio.cash` |
| `Order Creation Failed: suspended` | 股票停牌 | 用 `is_suspended()` 提前检查 |
| `No data for instrument` | 股票代码错误 | 检查代码格式（如 `.XSHG` / `.XSHE`） |
| `logger` 未定义 | 未导入 API | 确保 `from rqalpha.api import *` 在文件顶部 |

## 使用技巧

- RQAlpha 是纯本地框架，无云端依赖，适合离线研究。
- 使用 `rqalpha download-bundle` 获取免费内置A股日线数据。
- Mod 系统允许插入自定义数据源、券商接口和风控模块。
- 实盘交易可通过 `rqalpha-mod-vnpy` 连接 vn.py 的券商网关。
- 支持日线和分钟级回测。
- 文档：https://rqalpha.readthedocs.io/

## 规则

- 使用此 Skill 前，确认用户明确需要 rqalpha 框架进行策略回测。若用户仅需数据获取，引导使用 baostock/pywencai 等数据 Skill。
- 策略文件顶部必须包含 `from rqalpha.api import *`，以确保所有下单函数和 `logger` 可用。
- 期货策略必须使用 `buy_open`/`sell_open`/`buy_close`/`sell_close`，不能使用股票的 `order_shares` 等函数。
- 下单前应使用 `is_suspended()` 检查停牌状态，避免订单失败。
- 股票代码必须带后缀（`.XSHG`/`.XSHE`/`.CCFX` 等），不能使用纯数字代码。
