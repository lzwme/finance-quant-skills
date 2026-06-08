# RQAlpha 进阶策略示例

## 双均线交叉策略

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
    elif fast_ma < slow_ma and has_position:
        order_target_percent(context.stock, 0)

def handle_bar(context, bar_dict):
    pass
```

## 多股等权重调仓

```python
from rqalpha.api import *

def init(context):
    context.stocks = ['600000.XSHG', '000001.XSHE', '601318.XSHG',
                       '600036.XSHG', '000858.XSHE']
    scheduler.run_monthly(rebalance, tradingday=1, time_rule=market_open(minute=30))

def rebalance(context, bar_dict):
    for stock in list(context.portfolio.positions.keys()):
        if stock not in context.stocks:
            order_target_percent(stock, 0)

    weight = 0.95 / len(context.stocks)
    for stock in context.stocks:
        if not is_suspended(stock):
            order_target_percent(stock, weight)

def handle_bar(context, bar_dict):
    pass
```

## RSI均值回归策略

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
    elif rsi > context.overbought and has_pos:
        order_target_percent(context.stock, 0)
```

## 止损止盈策略

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
    else:
        if context.entry_price > 0:
            pnl = (price - context.entry_price) / context.entry_price
            if pnl <= -context.stop_loss or pnl >= context.take_profit:
                order_target_percent(context.stock, 0)
                context.entry_price = 0

def handle_bar(context, bar_dict):
    pass
```

## 期货双均线CTA策略

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
    elif prev_fast >= prev_slow and fast_ma < slow_ma and long_qty > 0:
        sell_close(context.symbol, long_qty)
```
