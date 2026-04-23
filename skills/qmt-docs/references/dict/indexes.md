---
url: "https://dict.thinktrader.net/dictionary/indexes.html"
title: "指数数据 | 迅投知识库"
---

## 关于迅投指数计算规则的说明

指数数据计算规则说明

迅投指数的计算规则为

1. 普通代码上市超过20个交易日后加入计算，债券为5个交易日。
2. 涨停打开超过3个交易日后加入计算。
3. 复牌股涨跌幅超25%不加入计算。
4. 指数成分等权进行计算。

## 获取沪深指数数据

### 获取指数代码列表

提示

为了获取指数合约列表,首先需要使用函数`get_sector_list`来获取需要查询的指数索引。具体的索引信息可以通过键入您感兴趣的索引名（例如："沪深指数"或"上证指数"）等获得。接下来，通过调用函数`get_stock_list_in_sector`并输入指定的索引名称，你就可以返回相应的指数合约列表。这部分合约列表包含了所有与特定指数相关的现有合约，这对于投资者在进行投资策略分析和决策时具有重要参考价值。

**调用方法**

python

```
# coding=utf-8
from xtquant import xtdata
# 获取板块列表
xtdata.get_sector_list()
# 根据板块列表找查询指数索引名称
xtdata.get_stock_list_in_sector(sector_name)
```

**参数**

| 字段 | 类型 | 说明 |
| --- | --- | --- |
| `sector_name` | `string` | `板块名称` |

**返回**

- 列表，包含指定板块成分代码。

示例返回值(板块列表)返回值(板块数据)

```
# coding=utf-8
from xtquant import xtdata
# 获取板块列表
ret_sector_list = xtdata.get_sector_list()
print(f'获取板块目录: {ret_sector_list}')
# 根据板块列表找查询指数索引名称
ret_sector_data = xtdata.get_stock_list_in_sector('沪深指数')
print(f'获取板块合约: {ret_sector_data}')
```

```
# 板块目录以列表形式,截取部分展示!
['上证指数', '上证新兴', '上证材料', '上证民企', '上证沪企', '上证流通', '上证海外', '上证消费', '上证环保', '上证电信', '上证能源', '上证资源', '上证转债', '上证金融', '上证银行', '上证高新', '上证龙头', '专利领先', '两融标的', '中关村50', '中关村60', '中关村A', '中创100', '中创100R', '中创400', '中创500', ...]
```

```
# 指数合约以列表形式返回,截取部分展示!
['000001.SH', '000002.SH', '000003.SH', '000004.SH', '000005.SH', '000006.SH', '000007.SH', '000008.SH', '000009.SH', '000010.SH', '000011.SH', '000012.SH', '000013.SH', '000015.SH', '000016.SH', '000017.SH', '000018.SH', '000019.SH', '000020.SH', '000021.SH', '000022.SH', '000025.SH', '000026.SH', '000027.SH', '000028.SH', '000029.SH', '000030.SH',...]
```

### 获取指数成份股权重

如果你的本地环境中缺少合约权重数据，那么可以先通过函数`download_index_weight`进行数据下载。下载后,再使用`get_index_weight`函数来取得相关指数下各个合约的权重信息。这两步操作能帮助你获得详尽而全面的权重数据，进一步增强你对投资环境的理解和掌握，帮助做出更明智的投资决策。

**调用方法**

python

```
# coding=utf-8
from xtquant import xtdata
# 下载权重相关信息
xtdata.download_index_weight()
# 获取权重相关信息
xtdata.get_index_weight(index_code)
```

**参数**

| 字段 | 类型 | 说明 |
| --- | --- | --- |
| `index_code` | `string` | `指数代码` |

- index\_code:字符串格式,指数代码,例如 000300.SH

**返回**

- 字典, key为成分代码, value为权重

示例返回值

```
# coding=utf-8
from xtquant import xtdata
# 下载权重相关信息
xtdata.download_index_weight()
# 获取权重相关信息
ret_weight_data = xtdata.get_index_weight('000300.SH')
print(ret_weight_data)
```

```
{'000001.SZ': 0.583, '000002.SZ': 0.501, '000063.SZ': 0.61, '000069.SZ': 0.096, ...}
```

### 获取指数行情数据

获取行情数据，最新行情需要数据订阅`subscribe_quote`。如果您需要获取历史数据，可以使用`download_history_data`函数下载相关数据，然后使用`get_market_data_ex`函数提取所需的信息。这样，使用者就能获得最新和详细的合约最新数据，有助于做出更精准的投资决策。

**调用方法**

python

```
# coding=utf-8
from xtquant import xtdata
# 订阅指定合约最新行情
xtdata.subscribe_quote(stock_code, period='', start_time='', end_time='', count=0, callback=None)
# 下载指定合约历史行情
xtdata.download_history_data(stock_code, period, start_time='', end_time='')
# 获取指定合约历史行情
xtdata.get_market_data_ex(field_list = [], stock_list = [], period = '', start_time = '', end_time = '', count = -1, dividend_type = 'none', fill_data = True)
```

**参数**

- xtdata.subscribe\_quote

| 字段 | 类型 | 说明 |
| --- | --- | --- |
| `stock_code` | `str` | `股票代码` |
| `start_time` | `str` | `开始时间格式YYYYMMDD/YYYYMMDDhhmmss` |
| `end_time` | `str` | `结束时间` |
| `count` | `int` | `数量 -1全部/n: 从结束时间向前数n个` |
| `period` | `str` | `周期 分笔"tick" 分钟线"1m"/"5m" 日线"1d"` |

- xtdata.get\_market\_data\_ex

| 参数名称 | 类型 | 描述 |
| --- | --- | --- |
| `field_list` | `list` | 表示所有字段。不同的数据周期，取值范围有所不同。 |
| `stock_list` | `list` | 合约代码列表 |
| `period` | `str` | 数据周期，默认是当前主图周期。可选值如下： 'tick' (分笔线)， '1d' (日线)， '1m' (1分钟线)， '5m' (5分钟线)， '15m' (15分钟线)， 'l2quote' (Level2行情快照)， 'l2quoteaux' (Level2行情快照补充)， 'l2order' (Level2逐笔委托)， 'l2transaction' (Level2逐笔成交)，'l2transactioncount' (Level2大单统计)， 'l2orderqueue' (Level2委买委卖队列) |
| `start_time` | `str` | 开始时间。为空时默认为最早时间。时间格式为'20201231'或'20201231093000' |
| `end_time` | `str` | 结束时间。为空时默认为最新时间。时间格式为'20201231'或'20201231235959' |
| `count` | `int` | 数据最大个数。-1表示不做个数限制 |
| `dividend_type` | `str` | 复权方式，默认是当前主图复权方式。可选值包括： 'none' (不复权)， 'front'(前复权)， 'back' (后复权)， 'front\_ratio' (等比前复权)， 'back\_ratio' (等比后复权) |
| `fill_data` | `bool` | 停牌填充方式 |

**返回值**

- period为`1m``5m``1d`K线周期时
  - 返回dict { field1 : value1, field2 : value2, ... }
  - value1, value2, ... ：pd.DataFrame 数据集，index为stock\_list，columns为time\_list
  - 各字段对应的DataFrame维度相同、索引相同
- period为`tick`分笔周期时
  - 返回dict { stock1 : value1, stock2 : value2, ... }
  - stock1, stock2, ... ：合约代码
  - value1, value2, ... ：np.ndarray 数据集，按数据时间戳`time`增序排列

示例返回值

```
# coding=utf-8
from xtquant import xtdata
# 获取迅投板块指数代码列表
xt_sector_index_list = xtdata.get_stock_list_in_sector("迅投一级行业板块加权指数")
# 获取迅投板块指数合约信息
xt_sector_index_info = xtdata.get_instrument_detail(xt_sector_index_list[0])
xt_sector_index = xt_sector_index_list[0]
print(xt_sector_index_info)
# 订阅合约数据
xtdata.subscribe_quote(xt_sector_index, period='1d', start_time='', end_time='20231026', count=1, callback=None)
# 下载指定合约历史行情
xtdata.download_history_data(xt_sector_index, '1d', '20231020', '20231026')
# 获取指定合约历史行情
day_data = xtdata.get_market_data_ex(field_list=[], stock_list=[xt_sector_index], period='1d', start_time='',end_time='20231026',  count=5, dividend_type='none', fill_data=True)
print(day_data)
```

```
{'ExchangeID': 'BKZS', 'InstrumentID': '260992', 'InstrumentName': 'SW1农林牧渔加权', 'ProductID': '', 'ProductName': '', 'ExchangeCode': '260992', 'UniCode': '260992', 'CreateDate': '0', 'OpenDate': '0', 'ExpireDate': 0, 'PreClose': 26232.32, 'SettlementPrice': 1.7976931348623157e+308, 'UpStopPrice': 1.7976931348623157e+308, 'DownStopPrice': 1.7976931348623157e+308, 'FloatVolume': 1.7976931348623157e+308, 'TotalVolume': 1.7976931348623157e+308, 'LongMarginRatio': 1.7976931348623157e+308, 'ShortMarginRatio': 1.7976931348623157e+308, 'PriceTick': 0.01, 'VolumeMultiple': 1, 'MainContract': 2147483647, 'LastVolume': 2147483647, 'InstrumentStatus': 2147483647, 'IsTrading': False, 'IsRecent': False, 'ProductTradeQuota': None, 'ContractTradeQuota': None, 'ProductOpenInterestQuota': None, 'ContractOpenInterestQuota': None}
{'260992.BKZS':                    time      open      high       low     close    volume  \
20231020  1697731200000  24602.81  24703.36  24401.10  24472.14  11904789
20231023  1697990400000  24403.87  24668.01  24071.37  24185.03  12184223
20231024  1698076800000  24197.98  24566.55  24095.19  24539.91  11494663
20231025  1698163200000  24717.87  25125.34  24717.87  24973.70  12586106
20231026  1698249600000  24887.32  25203.12  24809.58  25138.33  12035455

                amount  settelementPrice  openInterest  preClose  suspendFlag
20231020  1.012435e+10               0.0            15  24683.79            0
20231023  9.617285e+09               0.0            15  24472.14            0
20231024  9.028663e+09               0.0            15  24185.03            0
20231025  1.105085e+10               0.0            15  24539.91            0
20231026  1.008865e+10               0.0            15  24973.70            0  }
```

### 获取指数tick数据

获取全推tick数据的函数是用户主动调用的工具。所谓"全推tick数据"，指的是以tick（最小报价单位）为单位的实时市场数据，包括每一笔交易的信息，如成交金额、成交量、收盘价等。通过主动调用这个函数，用户能实时获得最新的市场动态，从而做出及时和准确的投资决策。

**调用方法**

python

```
# coding=utf-8
from xtquant import xtdata
xtdata.get_full_tick(code_list)
```

**参数**

| 字段 | 类型 | 说明 |
| --- | --- | --- |
| `code_list` | `list` | `合约列表` |

- code\_list:字符串格式, 例如 \['000001.SH', '000300.SH'\]

**返回值**

- dict 数据集 { stock1 : tick1, stock2 : tick2, ... }, tick字段如下

| 字段 | 类型 | 说明 |
| --- | --- | --- |
| timetag | str | 时间 |
| lastPrice | float | 最新价 |
| open | float | 开盘价 |
| low | float | 最低价 |
| amount | float | 成交额 |
| volume | int | 成交总量 |
| pvolume | int | 原始成交总量 |
| openInt | int | 持仓量 |
| stockStatus | str | 证券状态 |
| lastClose | float | 前收盘价 |
| lastSettlementPrice | float | 前结算价 |
| settlementPrice | float | 今结算价 |
| askPrice | list | 多档委卖价 |
| bidPrice | list | 多档委买价 |
| askVol | list | 多档委卖量 |
| bidVol | list | 多档委买量 |

示例返回值

```
# coding=utf-8
from xtquant import xtdata

# 获取迅投板块指数代码列表
xt_sector_index_list = xtdata.get_stock_list_in_sector("迅投一级行业板块加权指数")
# 获取迅投板块指数信息
xt_sector_index_info = xtdata.get_instrument_detail(xt_sector_index_list[0])
# 获取迅投板块指数tick数据
ret_full_tick = xtdata.get_full_tick([xt_sector_index])
print(ret_full_tick)
```

```
{'260992.BKZS': {'timetag': '20231114 15:00:09',
  'lastPrice': 26327.94,
  'open': 26190.7,
  'high': 26430.76,
  'low': 26186.34,
  'lastClose': 26232.32,
  'amount': 7523740134,
  'volume': 9392934,
  'pvolume': 9392934,
  'stockStatus': 5,
  'openInt': 15,
  'settlementPrice': 0,
  'lastSettlementPrice': 0,
  'askPrice': [0, 0, 0, 0, 0],
  'bidPrice': [0, 0, 0, 0, 0],
  'askVol': [0, 0, 0, 0, 0],
  'bidVol': [0, 0, 0, 0, 0]}}
```

## 获取迅投商品市场指数行情数据

提示

1.获取迅投商品市场指数行情数据，如要获取历史数据需要进行下载`download_history_data`,再根据函数`get_market_data_ex`获取

2. [VIP 权限数据](https://xuntou.net/#/productvip)

**调用方法**

python

```
# coding=utf-8
from xtquant import xtdata
# 下载合约
xtdata.download_history_data(stock_code,period = "1d")
# 获取迅投商品市场指数行情数据
xtdata.get_market_data_ex([],[stock_code],period='1d')
```

**参数**

| 字段 | 类型 | 说明 |
| --- | --- | --- |
| `stock_code` | `str` | `合约列表` |

**返回值**

- period为`1m``5m``1d`K线周期时
  - 返回dict { field1 : value1, field2 : value2, ... }
  - value1, value2, ... ：pd.DataFrame 数据集，index为stock\_list，columns为time\_list
  - 各字段对应的DataFrame维度相同、索引相同
- period为`tick`分笔周期时
  - 返回dict { stock1 : value1, stock2 : value2, ... }
  - stock1, stock2, ... ：合约代码
  - value1, value2, ... ：np.ndarray 数据集，按数据时间戳`time`增序排列

示例返回值

```
# coding=utf-8
from xtquant import xtdata
xtdata.download_history_data('290000.BKZS',period = "1d")
# 获取迅投商品市场指数行情数据
xtdata.get_market_data_ex([],['290000.BKZS'],period='1d')
```

```
{'290000.BKZS':                    time    open    high     low   close    volume  \
 19960102   820512000000  138.55  138.55  138.55  138.55         0
 19960103   820598400000  137.86  137.86  137.86  137.86         0
 19960104   820684800000  137.86  137.86  137.86  137.86         0
 19960105   820771200000  137.90  137.90  137.90  137.90         0
 19960108   821030400000  137.82  137.82  137.82  137.82         0
 ...                 ...     ...     ...     ...     ...       ...
 20231017  1697472000000  240.20  240.23  238.14  238.40  23597871
 20231018  1697558400000  238.39  239.81  237.67  237.89  24646472
 20231019  1697644800000  238.02  239.21  237.31  238.64  24785048
 20231020  1697731200000  238.60  239.34  236.77  237.10  25381186
 20231023  1697990400000  237.18  237.45  234.96  235.61  27538299

                 amount  settelementPrice  openInterest  preClose  suspendFlag
 19960102  0.000000e+00               0.0             0    138.69            0
 19960103  0.000000e+00               0.0             0    138.55            0
 19960104  0.000000e+00               0.0             0    137.86            0
 19960105  0.000000e+00               0.0             0    137.86            0
 19960108  0.000000e+00               0.0             0    137.90            0
 ...                ...               ...           ...       ...          ...
 20231017  1.400718e+12               0.0            13    239.99            0
 20231018  1.499089e+12               0.0            13    238.40            0
 20231019  1.449394e+12               0.0            13    237.89            0
 20231020  1.513323e+12               0.0            13    238.64            0
 20231023  1.549690e+12               0.0            13    237.10            0

 [6742 rows x 11 columns]}
```