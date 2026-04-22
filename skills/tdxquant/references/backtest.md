# 策略开发与回测

## 快速开始

策略开发需要先初始化 `tqcenter`，参考 [tdx_quant.md](tdx_quant.md) 中的「重要：Python 文件路径配置」章节。

```python
import sys, os, winreg

# 自动获取通达信安装目录
key_path = r"SOFTWARE\Microsoft\Windows\CurrentVersion\Uninstall\通达信金融终端64"
with winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, key_path) as key:
    tdx_root, _ = winreg.QueryValueEx(key, "InstallLocation")

sys.path.insert(0, os.path.join(tdx_root, 'PYPlugins', 'user'))

from tqcenter import tq
tq.initialize(__file__)
```

## 策略代码结构模板

```python
import pandas as pd
import vectorbt as vbt
from tqcenter import tq

tq.initialize(__file__)
pd.set_option('future.no_silent_downcasting', True)

# 1. 配置参数
CONFIG = {
    'start_time': '20240101',
    'end_time': '20241231',
    'stock_list': ['600519.SH'],
    'window': 5,
    'init_cash': 100000,
    'fees': 0.0003
}

# 2. 获取数据
df = tq.get_market_data(
    field_list=['Close', 'Open'],
    stock_list=CONFIG['stock_list'],
    start_time=CONFIG['start_time'],
    end_time=CONFIG['end_time'],
    dividend_type='front',
    period='1d'
)
close_df = tq.price_df(df, 'Close', column_names=CONFIG['stock_list'])
open_df = tq.price_df(df, 'Open', column_names=CONFIG['stock_list'])

# 3. 生成信号
ma = vbt.MA.run(close_df, window=CONFIG['window'])
entries = close_df.vbt.crossed_above(ma.ma)
exits = close_df.vbt.crossed_below(ma.ma)
entries = entries.shift(1).fillna(False)
exits = exits.shift(1).fillna(False)

# 4. 执行回测
portfolio = vbt.Portfolio.from_signals(
    close=close_df,
    entries=entries,
    exits=exits,
    price=open_df,
    init_cash=CONFIG['init_cash'],
    fees=CONFIG['fees'],
    freq='D',
    size_granularity=100
)

# 5. 结果分析
print(portfolio.stats())
print(portfolio.trades.records_readable)

tq.close()
```

## 关键统计指标

```python
# 总收益率
total_return = (final_value - init_cash) / init_cash

# 年化收益率
annual_return = (1 + total_return) ** (252 / trading_days) - 1

# 夏普比率
import numpy as np
sharpe_ratio = np.sqrt(252) * (daily_returns.mean() / daily_returns.std())

# 最大回撤
cum_returns = (1 + daily_returns).cumprod()
peak = cum_returns.cummax()
drawdown = (cum_returns - peak) / peak
max_drawdown = drawdown.min()
```

## 常用信号生成

```python
# 金叉信号
entries = close_df.vbt.crossed_above(ma_line)

# 死叉信号
exits = close_df.vbt.crossed_below(ma_line)

# 信号移位（次日开盘成交）
entries = entries.shift(1).fillna(False)

# 去除重复信号
entries = entries & ~entries.shift(1).fillna(False)
```

## 更多示例

完整的策略开发与回测示例，包括：
- MACD全市场批量选股
- 连涨N日选股
- 实时行情订阅预警
- MA均线调仓信号
- 发送回测数据到通达信客户端

请参考 [tq_use_case.md](tq_use_case.md) 的使用示例章节。
