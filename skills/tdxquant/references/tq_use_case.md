# tqcenter 使用示例与故障排除

## 使用示例

### 示例1：获取K线数据

```python
import sys
sys.path.insert(0, 'E:/App/new_tdx_test64/PYPlugins/user')
from tqcenter import tq

tq.initialize(__file__)

# 获取最近100条日线数据（前复权）
data = tq.get_market_data(
    field_list=['Open', 'Close', 'High', 'Low', 'Volume', 'Amount'],
    stock_list=['600000.SH', '000001.SZ'],
    period='1d',
    count=100,
    dividend_type='front'
)

close_df = data['Close']  # DataFrame，行=时间，列=股票代码
print(close_df.tail())

tq.close()
```

---

### 示例2：获取实时行情快照

```python
from tqcenter import tq
tq.initialize(__file__)

snapshot = tq.get_market_snapshot(stock_code='300505.SZ')
print(snapshot.get('Now'))      # 当前价
print(snapshot.get('Volume'))   # 成交量
print(snapshot.get('Buyp'))     # 五档买价

tq.close()
```

---

### 示例3：MACD全市场批量选股（推荐方式）

```python
from tqcenter import tq
tq.initialize(__file__)

# 获取所有A股
all_stocks = tq.get_stock_list(market='5')

# 批量调用MACD公式，返回最新2条数据
mul_zb_result = tq.formula_process_mul_zb(
    formula_name='MACD',
    formula_arg='12,26,9',
    xsflag=6,
    return_count=2,
    return_date=False,
    stock_list=all_stocks,
    stock_period='1d',
    count=100,
    dividend_type=1
)

# 筛选金叉股票
macd_stocks = []
if mul_zb_result:
    for key in mul_zb_result:
        if key != "ErrorId":
            dif = mul_zb_result[key].get('DIF', [])
            dea = mul_zb_result[key].get('DEA', [])
            if len(dif) >= 2 and len(dea) >= 2:
                if float(dif[-2]) < float(dea[-2]) and float(dif[-1]) >= float(dea[-1]):
                    macd_stocks.append(key)

print(f"MACD金叉股票：{len(macd_stocks)}只")
# 发送到临时条件股
tq.send_user_block(block_code='', stocks=macd_stocks)
tq.close()
```

---

### 示例4：连续N日上涨选股并加入自定义板块

```python
import pandas as pd
import numpy as np
from datetime import datetime
from tqcenter import tq

tq.initialize(__file__)

batch_codes = tq.get_stock_list_in_sector('通达信88')
N = 3           # 连续上涨天数
block_code = 'LZXG'
block_name = '连涨选股'

df_real = tq.get_market_data(
    field_list=['Close'],
    stock_list=batch_codes,
    start_time="20251025",
    end_time=datetime.now().strftime("%Y%m%d"),
    dividend_type='front',
    period='1d',
    fill_data=True
)
close_df = tq.price_df(df_real, 'Close', column_names=batch_codes)

# 计算连续上涨天数
is_up = close_df > close_df.shift(1)
up_mask = np.where(is_up, 1, np.nan)
up_mask_df = pd.DataFrame(up_mask, index=close_df.index, columns=close_df.columns)
filled_df = up_mask_df.ffill()
consec_up_days = filled_df.notna().cumsum()
reset_counts = consec_up_days.where(~is_up).ffill().fillna(0)
consec_up_days = (consec_up_days - reset_counts).astype(int)

# 筛选最新交易日连续上涨≥N天的股票
latest_date = consec_up_days.index[-1]
latest_consec_up = consec_up_days.loc[latest_date]
target_stocks_list = latest_consec_up[latest_consec_up >= N].sort_values(ascending=False).index.tolist()

# 创建板块并推送
tq.create_sector(block_code=block_code, block_name=block_name)
tq.send_user_block(block_code=block_code, stocks=target_stocks_list, show=True)
tq.send_message(f"MSG,连涨≥{N}天股票：{len(target_stocks_list)}只")
tq.close()
```

---

### 示例5：订阅行情实时预警（分批订阅+防抖）

```python
import json, time, signal, sys
from datetime import datetime
from collections import defaultdict
from tqcenter import tq

PRICE_RISE_THRESHOLD = 5.0   # 涨幅阈值
ANTI_SHAKE_SECONDS = 10       # 防抖间隔（秒）
BATCH_SIZE = 50               # 每批订阅数量

tq.initialize(__file__)

all_stocks = tq.get_stock_list_in_sector('通达信88')
last_warn_time = defaultdict(int)
TRIGGERED = set()
EXIT_FLAG = False

def signal_handler(signum, frame):
    global EXIT_FLAG
    EXIT_FLAG = True
    tq.unsubscribe_hq(stock_list=all_stocks)
    sys.exit(0)

signal.signal(signal.SIGINT, signal_handler)

def price_rise_callback(data_str):
    code_json = json.loads(data_str)
    code = code_json.get('Code')
    if code_json.get('ErrorId') != "0" or not code or code in TRIGGERED:
        return

    snapshot = tq.get_market_snapshot(code)
    if not snapshot:
        return
    now_price = float(snapshot.get('Now', 0))
    last_close = float(snapshot.get('LastClose', 0))
    if now_price <= 0 or last_close <= 0:
        return

    rise_rate = (now_price - last_close) / last_close * 100
    current_time = int(time.time())
    if rise_rate > PRICE_RISE_THRESHOLD and (current_time - last_warn_time[code]) >= ANTI_SHAKE_SECONDS:
        TRIGGERED.add(code)
        last_warn_time[code] = current_time
        tq.unsubscribe_hq(stock_list=[code])
        tq.send_warn(
            stock_list=[code],
            time_list=[datetime.now().strftime("%Y%m%d%H%M%S")],
            price_list=[str(now_price)],
            close_list=[str(last_close)],
            volum_list=[snapshot.get('Volume', '0')],
            bs_flag_list=['0'],
            warn_type_list=['3'],
            reason_list=[f'涨幅突破{PRICE_RISE_THRESHOLD}%'],
            count=1
        )

# 分批订阅
for i in range(0, len(all_stocks), BATCH_SIZE):
    tq.subscribe_hq(stock_list=all_stocks[i:i+BATCH_SIZE], callback=price_rise_callback)

print(f"监控启动，共{len(all_stocks)}只，按Ctrl+C退出...")
while not EXIT_FLAG:
    time.sleep(0.1)
```

---

### 示例6：MA均线调仓信号+发送预警（可双击闪电买卖）

```python
import vectorbt as vbt
import pandas as pd
from datetime import datetime, timedelta
from tqcenter import tq

tq.initialize(__file__)

N = 5  # 均线周期
batch_codes = tq.get_stock_list_in_sector('通达信88')
end_date = datetime.now().strftime("%Y%m%d")
start_date = (datetime.now() - timedelta(days=2 * N + 20)).strftime("%Y%m%d")

df_real = tq.get_market_data(
    field_list=['Close'],
    stock_list=batch_codes,
    start_time=start_date,
    end_time=end_date,
    dividend_type='front',
    period='1d',
    fill_data=True
)
close_df = tq.price_df(df_real, 'Close', column_names=batch_codes)

ma = vbt.MA.run(close_df, window=N).ma
ma.columns = close_df.columns
entries = close_df.vbt.crossed_above(ma)
exits = close_df.vbt.crossed_below(ma)
latest_date = close_df.index[-1]
prev_date = close_df.index[-2] if len(close_df.index) >= 2 else latest_date

# 收集买卖信号
buy_signals, sell_signals = {}, {}
for code in batch_codes:
    if code not in close_df.columns:
        continue
    today_close = round(close_df.loc[latest_date, code], 2)
    prev_close = round(close_df.loc[prev_date, code], 2)
    if entries.loc[latest_date, code]:
        buy_signals[code] = {'today_close': today_close, 'prev_close': prev_close}
    if exits.loc[latest_date, code]:
        sell_signals[code] = {'today_close': today_close, 'prev_close': prev_close}

# 发送预警（warn_type='1' 支持双击闪电买卖）
all_signals = [(c, i, '买入') for c, i in buy_signals.items()] + \
              [(c, i, '卖出') for c, i in sell_signals.items()]
if all_signals:
    warn_time = datetime.now().strftime("%Y%m%d%H%M%S")
    tq.send_warn(
        stock_list=[s[0] for s in all_signals],
        time_list=[warn_time] * len(all_signals),
        price_list=[str(s[1]['today_close']) for s in all_signals],
        close_list=[str(s[1]['prev_close']) for s in all_signals],
        volum_list=['0'] * len(all_signals),
        bs_flag_list=['0' if s[2] == '买入' else '1' for s in all_signals],
        warn_type_list=['1'] * len(all_signals),    # 支持双击闪电买卖
        reason_list=[f"{s[2]}信号" for s in all_signals],
        count=len(all_signals)
    )
tq.close()
```

---

### 示例7：vectorbt 简单回测

```python
import pandas as pd
import vectorbt as vbt
from tqcenter import tq

tq.initialize(__file__)

pd.set_option('future.no_silent_downcasting', True)

stock_code_list = ['688318.SH']
window = 5
target_start = '20250701'
target_end = '20251231'
start_time = (pd.to_datetime(target_start) - pd.Timedelta(days=window + 10)).strftime('%Y%m%d')

df_real = tq.get_market_data(
    field_list=['Close', 'Open'],
    stock_list=stock_code_list,
    start_time=start_time,
    end_time=target_end,
    dividend_type='front',
    period='1d',
    fill_data=True
)
close_df = tq.price_df(df_real, 'Close', column_names=stock_code_list)
open_df = tq.price_df(df_real, 'Open', column_names=stock_code_list)

ma = vbt.MA.run(close_df, window=window).ma.ffill()
ma.columns = close_df.columns

entries_df = close_df.vbt.crossed_above(ma).shift(1).fillna(False).astype(bool)
exits_df = close_df.vbt.crossed_below(ma).shift(1).fillna(False).astype(bool)

portfolio = vbt.Portfolio.from_signals(
    close=close_df,
    entries=entries_df,
    exits=exits_df,
    price=open_df,
    init_cash=100000,
    fees=0.0003,
    freq='D',
    size_granularity=100    # A股最小交易单位100股
)

# 输出结果并绘图
print(portfolio.stats())
portfolio[stock_code_list[0]].plot().show()

tq.close()
# 注意：vectorbt 不支持分红送股等权益变动
```

---

### 示例8：发送回测数据+通达信公式展示

```python
from tqcenter import tq
import pandas as pd

tq.initialize(__file__)

stock_code = '688318.SH'
data = tq.get_market_data(
    field_list=['Close'],
    stock_list=[stock_code],
    period='1d',
    count=60,
    dividend_type='front'
)
close_series = data['Close'][stock_code]
ma5 = close_series.rolling(5).mean()
ma10 = close_series.rolling(10).mean()
buy_signal = ((ma5.shift(1) <= ma10.shift(1)) & (ma5 > ma10)).astype(int)
sell_signal = ((ma5.shift(1) >= ma10.shift(1)) & (ma5 < ma10)).astype(int)

time_list = close_series.index.strftime('%Y%m%d').tolist()
data_list = []
for i in range(len(close_series)):
    data_list.append([
        f"{ma5.iloc[i]:.2f}" if not pd.isna(ma5.iloc[i]) else "0",
        f"{ma10.iloc[i]:.2f}" if not pd.isna(ma10.iloc[i]) else "0",
        str(int(buy_signal.iloc[i])),
        str(int(sell_signal.iloc[i]))
    ])

tq.send_bt_data(
    stock_code=stock_code,
    time_list=time_list,
    data_list=data_list,
    count=len(time_list)
)
# 在通达信公式管理器中用 SIGNALS_TQ(1,0)~SIGNALS_TQ(4,0) 引用上述数据
tq.close()
```

---

### 示例9：交易接口完整流程

```python
from tqcenter import tq, tqconst
tq.initialize(__file__)

# 获取账户句柄（须先在客户端登录）
account_id = tq.stock_account(account="1190008847", account_type="STOCK")
print(f"账户句柄: {account_id}")  # ≥0 有效

# 查询持仓
positions = tq.query_stock_positions(account_id=account_id)
for pos in positions:
    print(f"{pos['Code']}: 成本价={pos['Cbj']}, 总持仓={pos['TotalVol']}")

# 查询委托
orders = tq.query_stock_orders(account_id=account_id, stock_code="")
print(f"当日委托: {orders}")

# 下单（自填价买入）
result = tq.order_stock(
    account_id=account_id,
    stock_code="688318.SH",
    order_type=tqconst.STOCK_BUY,
    order_volume=100,
    price_type=tqconst.PRICE_MY,
    price=130.0
)
print(result)  # {'ErrorId': '0', 'Msg': '已发送信号至客户端，待用户确认！', 'Value': 1}

tq.close()
```

---

## 故障排除

### "TQ数据接口初始化失败或已有同名策略运行"
1. 确保通达信客户端已运行并登录
2. 使用 `sys.path.insert(0, ...)` 而非 `sys.path.append()`
3. 确认 `PYPlugins/` 目录下存在 `TPyth.dll` 和 `TPythClient.dll`
4. 检查是否已有相同 `__file__` 路径的策略在运行（ErrorId='12'）

### 菜单一直显示"正在开启TQ策略..."
检查是否有防火墙弹窗，若有请允许访问。

### 获取数据时指标值前面是 None
`count` 参数设置的K线数量不足以覆盖公式计算中的最大参数值。例如 `MA(C,20)` 需要至少20根K线，若 `count=10` 则前10根K线的MA值为 None。

### `send_warn` 报 ValueError
- 确认 `count > 0`
- 确认 `stock_list`、`price_list`、`close_list`、`volum_list` 的长度均 ≥ `count`
- 确认 `price_list`、`close_list`、`volum_list` 中的元素均为纯数字字符串

### 批量公式选股结果比客户端少
`count` 参数设置太小，不够覆盖公式计算所需的最大回溯K线数，适当增大 `count` 值。

### Module Not Found 错误
- 确认 `PYPlugins/user` 路径正确
- 使用绝对路径而非相对路径
- 使用 `sys.path.insert(0, ...)` 保证优先加载
