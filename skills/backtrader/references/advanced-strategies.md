# Backtrader 进阶策略示例

## MACD + 布林带组合策略

```python
import backtrader as bt

class MACDBollStrategy(bt.Strategy):
    """MACD金叉 + 布林带下轨支撑组合买入策略"""
    params = (
        ('macd_fast', 12),
        ('macd_slow', 26),
        ('macd_signal', 9),
        ('boll_period', 20),
        ('boll_dev', 2.0),
        ('stake', 100),
    )

    def __init__(self):
        self.macd = bt.indicators.MACD(
            self.data.close,
            period_me1=self.p.macd_fast,
            period_me2=self.p.macd_slow,
            period_signal=self.p.macd_signal
        )
        self.boll = bt.indicators.BollingerBands(
            self.data.close, period=self.p.boll_period, devfactor=self.p.boll_dev
        )
        self.macd_cross = bt.indicators.CrossOver(self.macd.macd, self.macd.signal)

    def next(self):
        if not self.position:
            if self.macd_cross[0] > 0 and self.data.close[0] < self.boll.mid[0]:
                self.buy(size=self.p.stake)
        else:
            if self.data.close[0] > self.boll.top[0] or self.macd_cross[0] < 0:
                self.sell(size=self.p.stake)
```

## 海龟交易策略

```python
import backtrader as bt

class TurtleStrategy(bt.Strategy):
    """经典海龟交易策略 — 唐奇安通道突破 + ATR仓位管理"""
    params = (
        ('entry_period', 20),
        ('exit_period', 10),
        ('atr_period', 20),
        ('risk_pct', 0.01),
    )

    def __init__(self):
        self.entry_high = bt.indicators.Highest(self.data.high, period=self.p.entry_period)
        self.entry_low = bt.indicators.Lowest(self.data.low, period=self.p.entry_period)
        self.exit_high = bt.indicators.Highest(self.data.high, period=self.p.exit_period)
        self.exit_low = bt.indicators.Lowest(self.data.low, period=self.p.exit_period)
        self.atr = bt.indicators.ATR(self.data, period=self.p.atr_period)
        self.order = None

    def next(self):
        if self.order:
            return
        atr_val = self.atr[0]
        if atr_val <= 0:
            return
        unit_size = int(self.broker.getvalue() * self.p.risk_pct / atr_val)
        unit_size = max(unit_size, 1)

        if not self.position:
            if self.data.close[0] > self.entry_high[-1]:
                self.order = self.buy(size=unit_size)
        else:
            if self.data.close[0] < self.exit_low[-1]:
                self.order = self.close()

    def notify_order(self, order):
        if order.status in [order.Completed]:
            if order.isbuy():
                print(f'{self.data.datetime.date(0)} 买入 {order.executed.size} 股 @ {order.executed.price:.2f}')
            else:
                print(f'{self.data.datetime.date(0)} 卖出 @ {order.executed.price:.2f}')
        self.order = None
```

## 多股票轮动策略

```python
import backtrader as bt

class MomentumRotation(bt.Strategy):
    """动量轮动策略 — 每月持有动量最强的前N只股票"""
    params = (
        ('momentum_period', 20),
        ('hold_num', 3),
        ('rebalance_days', 20),
    )

    def __init__(self):
        self.counter = 0
        self.momentums = {}
        for d in self.datas:
            self.momentums[d._name] = bt.indicators.RateOfChange(
                d.close, period=self.p.momentum_period
            )

    def next(self):
        self.counter += 1
        if self.counter % self.p.rebalance_days != 0:
            return

        rankings = []
        for d in self.datas:
            mom = self.momentums[d._name][0]
            rankings.append((d._name, d, mom))
        rankings.sort(key=lambda x: x[2], reverse=True)

        selected = [r[1] for r in rankings[:self.p.hold_num]]
        for d in self.datas:
            if self.getposition(d).size > 0 and d not in selected:
                self.close(data=d)

        if selected:
            per_value = self.broker.getvalue() * 0.95 / len(selected)
            for d in selected:
                target_size = int(per_value / d.close[0])
                current_size = self.getposition(d).size
                if target_size > current_size:
                    self.buy(data=d, size=target_size - current_size)
                elif target_size < current_size:
                    self.sell(data=d, size=current_size - target_size)
```
