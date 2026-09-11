# QMT Python 常用 API 速查

> 本文档是 QMT 开发中最常用的函数快速参考。完整的 API 文档请查阅 `python-innerApi/` 目录。

## 🔑 编码规范

```python
#coding:gbk  # 必须在文件第一行，不可省略
```

- 缩进使用 4 个空格（不可混用）
- 股票最小交易单位：**100 股**
- 账户金额单位：**分**（需要 `/100` 转换为元）
- 回测模式使用 `subscribe=False`，实盘使用 `subscribe=True`

## 📊 核心概念速查

| 概念 | 说明 | 回测 | 实盘 |
|------|------|:----:|:----:|
| `handlebar` | 逐K线驱动 | ✅ | ✅ |
| `subscribe` | 事件驱动（分笔推送） | ❌ | ✅ |
| `run_time` | 定时任务 | ❌ | ✅ |
| `quicktrade=0` | 等待K线完成再下单 | ✅ | ✅ |
| `quicktrade=2` | 立即下单 | ❌ | ✅ |

## 📈 行情数据 API

### get_market_data_ex — 获取K线历史数据

```python
# ⚠️ 前两个参数必须用位置参数，不能用 fields= / stocks=
data = C.get_market_data_ex(
    ['close'],              # 位置参数：字段列表
    ['600000.SH'],          # 位置参数：股票列表
    end_time='20250101',    # 数据截止时间
    period='1d',            # K线周期
    count=100,              # 数据条数
    subscribe=False         # 回测False，实盘True
)

# 提取数据
close_list = list(data['600000.SH'].iloc[:, 0])
```

**常用字段：** `open` `close` `high` `low` `volume` `amount`

**常用周期：** `1d`(日线) `1w`(周线) `1m`/`5m`/`15m`(分钟线)

### get_full_tick — 获取实时全推行情

```python
tick = C.get_full_tick(['600000.SH', '000001.SZ'])
price = tick['600000.SH']['lastPrice']       # 最新价
pre_close = tick['600000.SH']['lastClose']   # 前收盘
volume = tick['600000.SH']['volume']         # 成交量
```

> ⚠️ 仅实盘可用，回测不支持

### subscribe_quote — 订阅行情推送

```python
def init(C):
    def on_quote(data):
        for stock in data:
            price = data[stock]['close']
            # 交易逻辑...
    C.subscribe_quote('600000.SH', period='1d', callback=on_quote)
```

## 💰 交易 API

### passorder — 下单

```python
passorder(
    23,              # opType: 23=买入, 24=卖出
    1101,            # orderType: 1101=按股数
    account,         # 资金账号，回测填任意字符串
    '600000.SH',     # 股票代码
    5,               # prType: 5=最新价, 11=限价
    -1,              # price: -1=不设止价（最新价模式）
    100,             # volume: 股数（须为100的倍数）
    '策略名称',      # strategyName
    0,               # quicktrade: 0=逐K线, 2=立即下单
    '投资备注',      # userOrderId
    C                # ContextInfo 对象
)
```

**关键 opType 值：**
| 值 | 含义 | 值 | 含义 |
|:--:|------|:--:|------|
| 23 | 股票买入 | 24 | 股票卖出 |
| 33 | 担保品买入 | 34 | 担保品卖出 |
| 27 | 融资买入 | 28 | 融券卖出 |

**关键 orderType 值：**
| 值 | 含义 |
|:--:|------|
| 1101 | 按股数下单 |
| 1102 | 按金额下单 |
| 1123 | 按市值比例(1=全仓) |

### get_trade_detail_data — 查询交易数据

```python
# 查询账户
acc = get_trade_detail_data(account, 'stock', 'account')[0]
cash = acc.m_dAvailable          # 可用资金（分）
total_asset = acc.m_dTotalAsset  # 总资产

# 查询持仓（返回列表，每个元素为一个持仓对象）
positions = get_trade_detail_data(account, 'stock', 'position')
holds = {f'{p.m_strInstrumentID}.{p.m_strExchangeID}': p.m_nVolume
         for p in positions}

# 查询委托
orders = get_trade_detail_data(account, 'stock', 'order')

# 查询成交
deals = get_trade_detail_data(account, 'stock', 'deal')
```

**数据查询类型：** `'account'` `'position'` `'order'` `'deal'`

**account_type：** `'stock'`(股票) `'credit'`(两融) `'FUTURE'`(期货)

### 委托状态码

| 码 | 状态 | 码 | 状态 |
|:--:|------|:--:|------|
| 0 | 未报 | 4 | 部成 |
| 1 | 待报 | 5 | 已成 |
| 2 | 已报 | 6 | 废单 |
| 3 | 已撤 | 7 | 待撤 |

## 🛠️ 常用辅助函数

```python
# 获取板块股票列表
stocks = C.get_stock_list_in_sector('沪深A股')

# 获取股票名称
name = C.get_stock_name('600000.SH')

# K线时间戳转日期字符串
bar_date = timetag_to_datetime(C.get_bar_timetag(C.barpos), '%Y%m%d%H%M%S')

# 判断是否为最后一根K线（实盘中区分历史/实时）
if C.is_last_bar():
    # 只处理实时数据...

# 获取品种详情
info = C.get_instrument_detail('600000.SH')
```

## 📋 常用策略代码骨架

```python
#coding:gbk
import pandas as pd
import numpy as np

def init(C):
    C.stock = C.stockcode + '.' + C.market
    C.accountid = 'test'
    C.period = '1d'

def handlebar(C):
    # 获取K线时间
    bar_date = timetag_to_datetime(C.get_bar_timetag(C.barpos), '%Y%m%d%H%M%S')

    # 获取行情数据
    data = C.get_market_data_ex(
        ['close'], [C.stock],
        end_time=bar_date, period=C.period,
        count=100, subscribe=False
    )
    close_list = list(data[C.stock].iloc[:, 0])

    if len(close_list) < 20:
        return

    # 获取账户信息
    acc = get_trade_detail_data(C.accountid, 'stock', 'account')[0]
    cash = int(acc.m_dAvailable)

    # 获取持仓
    positions = get_trade_detail_data(C.accountid, 'stock', 'position')
    holds = {f'{p.m_strInstrumentID}.{p.m_strExchangeID}': p.m_nVolume
             for p in positions}
    vol = holds.get(C.stock, 0)

    # 交易逻辑
    price = close_list[-1]
    if vol == 0 and buy_signal:
        qty = int(cash / price / 100) * 100
        passorder(23, 1101, C.accountid, C.stock, 5, -1, qty, C)
    elif vol > 0 and sell_signal:
        passorder(24, 1101, C.accountid, C.stock, 5, -1, vol, C)
```

## 📖 完整文档导航

- **详细 API 参数** → `python-innerApi/data_function.md` / `trading_function.md` / `system_function.md`
- **数据结构定义** → `python-innerApi/data_structure.md`
- **枚举常量** → `python-innerApi/enum_constants.md`
- **代码示例** → `python-innerApi/code_examples.md` / `examples/`
- **常见问题** → `python-innerApi/question_answer.md`
