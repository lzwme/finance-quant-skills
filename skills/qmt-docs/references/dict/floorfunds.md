---
url: "https://dict.thinktrader.net/dictionary/floorfunds.html"
title: "场内基金 | 迅投知识库"
---

## 获取基金数据

此函数被设计为只支持单一基金查询，用于获取详细的股票信息。该函数可以让您接收关于特定基金的深度信息，包括但不限于其涨跌停价格、上市日期、退市日期以及期权到期日等重要数据。这将为您提供详尽的信息，以便更好地理解并分析股票的历史和现状。

**调用方法**

python

```
# coding=utf-8
from xtquant import xtdata
xtdata.get_instrument_detail(stock_code)
```

**参数**

| 字段 | 类型 | 说明 |
| --- | --- | --- |
| `stock_code` | `string` | `合约代码` |

**返回值**

- 字典，{ field1 : value1, field2 : value2, ... }，找不到指定合约时返回`None`

| 字段 | 类型 | 说明 |
| --- | --- | --- |
| ExchangeID | str | 合约市场代码 |
| InstrumentID | str | 合约代码 |
| ProductID | str | 合约的品种ID(期货) |
| ProductName | str | 合约的品种名称(期货) |
| CreateDate | str | 上市日期(期货) |
| OpenDate | str | IPO日期(股票) |
| ExpireDate | int | 退市日或者到期日 |
| PreClose | float | 前收盘价格 |
| SettlementPrice | float | 前结算价格 |
| UpStopPrice | float | 当日涨停价 |
| DownStopPrice | float | 当日跌停价 |
| FloatVolume | float | 流通股本 |
| TotalVolume | float | 总股本 |
| LongMarginRatio | float | 多头保证金率 |
| ShortMarginRatio | float | 空头保证金率 |
| PriceTick | float | 最小价格变动单位 |
| VolumeMultiple | int | 合约乘数(对期货以外的品种，默认是1) |
| MainContract | int | 主力合约标记，1、2、3分别表示第一主力合约，第二主力合约，第三主力合约 |
| LastVolume | int | 昨日持仓量 |
| InstrumentStatus | int | 合约已停牌日期（停牌第一天值为0，第二天为1，以此类推。注意，正常交易的股票该值也是0）获取股票停牌状态参考 [get\_full\_tick](http://docs.thinktrader.net/vip/pages/36f5df/#%E8%8E%B7%E5%8F%96%E5%85%A8%E6%8E%A8%E6%95%B0%E6%8D%AE) [openInt字段](http://docs.thinktrader.net/vip/pages/41b7c5/#tick-%E5%88%86%E7%AC%94%E6%95%B0%E6%8D%AE) |
| IsTrading | bool | 合约是否可交易 |
| IsRecent | bool | 是否是近月合约 |

示例返回值

```
# coding=utf-8
from xtquant import xtdata
code_detail = xtdata.get_instrument_detail('159733.SZ')
print(code_detail)
```

```
{'ExchangeID': 'SZ',
 'InstrumentID': '159733',
 'InstrumentName': '消费电子50ETF',
 'ProductID': '',
 'ProductName': '',
 'CreateDate': '0',
 'OpenDate': '20210929',
 'ExpireDate': 99999999,
 'PreClose': 0.6950000000000001,
 'SettlementPrice': 0.6941,
 'UpStopPrice': 0.765,
 'DownStopPrice': 0.626,
 'FloatVolume': 41156925.0,
 'TotalVolume': 41156925.0,
 'LongMarginRatio': 1.7976931348623157e+308,
 'ShortMarginRatio': 1.7976931348623157e+308,
 'PriceTick': 0.001,
 'VolumeMultiple': 1,
 'MainContract': 2147483647,
 'LastVolume': 2147483647,
 'InstrumentStatus': 0,
 'IsTrading': False,
 'IsRecent': False,
 'ProductTradeQuota': 0,
 'ContractTradeQuota': 0,
 'ProductOpenInterestQuota': 0,
 'ContractOpenInterestQuota': 0}
```

## ETF申赎清单

提示

1. 使用前需要调用`xtdata.download_etf_info()`下载数据
2. [VIP 权限数据](https://xuntou.net/#/productvip)

**调用方法**

python

```

from xtquant import xtdata

xtdata.get_etf_info()
```

**参数**

None

**返回值**

一个多层嵌套的dict

现金替代标志：

- 深市ETF的成分股现金替代标记取值范围

  - 0 = 禁止现金替代（必须有证券）
  - 1 = 可以进行现金替代（先用证券，证券不足时差额部分用现金替代）
  - 2 = 必须用现金替代
- 沪市ETF的成分股现金替代标记取值范围

  - 0 = 沪市不可被替代
  - 1 = 沪市可以被替代
  - 2 = 沪市必须被替代
  - 3 = 深市退补现金替代
  - 4 = 深市必须现金替代
  - 5 = 成份证券退补现金替代
  - 6 = 成份证券必须现金替代
  - 7 = 港市退补现金替代
  - 8 = 港市必须现金替代

是否需要公布IOPV:

- 0: 否
- 1: 是

申购的允许情况:

- 0: 否
- 1: 是

赎回的允许情况:

- 0: 否
- 1: 是

示例返回值

```
from xtquant import xtdata

xtdata.download_etf_info()

all_etf_info = xtdata.get_etf_info()

print(list(all_etf_info.keys())[:20]) # 打印第一层key

target_etf_info = all_etf_info["510050.SH"]

print(target_etf_info.keys()) # 打印第二层key

data = target_etf_info["成份股信息"]

print(data[:10]) # 打印成份股信息
```

```
['515110.SH', '515020.SH', '515330.SH', '513750.SH', '513220.SH', '512800.SH', '513190.SH', '513660.SH', '513860.SH', '513200.SH', '513360.SH', '513310.SH', '513560.SH', '515310.SH', '513550.SH', '513590.SH', '513330.SH', '513700.SH', '513880.SH', '513530.SH']

dict_keys(['market', 'stock', '基金代码', '基金名称', '现金差额', '最小申购、赎回单位净值', '基金份额净值', '预估现金差额', '现金替代比例上限', '是否需要公布IOPV', '最小申购、赎回单位', '申购的允许情况', '赎回的允许情况', '申购上限', '赎回上限', '成份股信息'])

[{'成份股代码': '600010.SH', '成份股名称': '包钢股份', '成份股数量': 7900, '现金替代标志': 1, '申购现金替代溢价比率': 0.1, '申购替代金额': 0.0, '赎回现金替代折价比率': 0.0, '赎回替代金额': 0.0, '成份股所属市场': 'SH', '映射代码': '', '是否实物对价申赎': 0, '占净值比例': 0.0, '持股数': 0, '持仓市值': 0.0}, {'成份股代码': '600028.SH', '成份股名称': '中国石化', '成份股数量': 6600, '现金替代标志': 1, '申购现金替代溢价比率': 0.1, '申购替代金额': 0.0, '赎回现金替代折价比率': 0.0, '赎回替代金额': 0.0, '成份股所属市场': 'SH', '映射代码': '', '是否实物对价申赎': 0, '占净值比例': 0.0, '持股数': 0, '持仓市值': 0.0}, {'成份股代码': '600030.SH', '成份股名称': '中信证券', '成份股数量': 3400, '现金替代标志': 1, '申购现金替代溢价比率': 0.1, '申购替代金额': 0.0, '赎回现金替代折价比率': 0.0, '赎回替代金额': 0.0, '成份股所属市场': 'SH', '映射代码': '', '是否实物对价申赎': 0, '占净值比例': 0.0, '持股数': 0, '持仓市值': 0.0}, {'成份股代码': '600031.SH', '成份股名称': '三一重工', '成份股数量': 2100, '现金替代标志': 1, '申购现金替代溢价比率': 0.1, '申购替代金额': 0.0, '赎回现金替代折价比率': 0.0, '赎回替代金额': 0.0, '成份股所属市场': 'SH', '映射代码': '', '是否实物对价申赎': 0, '占净值比例': 0.0, '持股数': 0, '持仓市值': 0.0}, {'成份股代码': '600036.SH', '成份股名称': '招商银行', '成份股数量': 4300, '现金替代标志': 1, '申购现金替代溢价比率': 0.1, '申购替代金额': 0.0, '赎回现金替代折价比率': 0.0, '赎回替代金额': 0.0, '成份股所属市场': 'SH', '映射代码': '', '是否实物对价申赎': 0, '占净值比例': 0.0, '持股数': 0, '持仓市值': 0.0}, {'成份股代码': '600048.SH', '成份股名称': '保利发展', '成份股数量': 2500, '现金替代标志': 1, '申购现金替代溢价比率': 0.1, '申购替代金额': 0.0, '赎回现金替代折价比率': 0.0, '赎回替代金额': 0.0, '成份股所属市场': 'SH', '映射代码': '', '是否实物对价申赎': 0, '占净值比例': 0.0, '持股数': 0, '持仓市值': 0.0}, {'成份股代码': '600050.SH', '成份股名称': '中国联通', '成份股数量': 6600, '现金替代标志': 1, '申购现金替代溢价比率': 0.1, '申购替代金额': 0.0, '赎回现金替代折价比率': 0.0, '赎回替代金额': 0.0, '成份股所属市场': 'SH', '映射代码': '', '是否实物对价申赎': 0, '占净值比例': 0.0, '持股数': 0, '持仓市值': 0.0}, {'成份股代码': '600089.SH', '成份股名称': '特变电工', '成份股数量': 1700, '现金替代标志': 1, '申购现金替代溢价比率': 0.1, '申购替代金额': 0.0, '赎回现金替代折价比率': 0.0, '赎回替代金额': 0.0, '成份股所属市场': 'SH', '映射代码': '', '是否实物对价申赎': 0, '占净值比例': 0.0, '持股数': 0, '持仓市值': 0.0}, {'成份股代码': '600104.SH', '成份股名称': '上汽集团', '成份股数量': 1600, '现金替代标志': 1, '申购现金替代溢价比率': 0.1, '申购替代金额': 0.0, '赎回现金替代折价比率': 0.0, '赎回替代金额': 0.0, '成份股所属市场': 'SH', '映射代码': '', '是否实物对价申赎': 0, '占净值比例': 0.0, '持股数': 0, '持仓市值': 0.0}, {'成份股代码': '600111.SH', '成份股名称': '北方稀土', '成份股数量': 900, '现金替代标志': 1, '申购现金替代溢价比率': 0.1, '申购替代金额': 0.0, '赎回现金替代折价比率': 0.0, '赎回替代金额': 0.0, '成份股所属市场': 'SH', '映射代码': '', '是否实物对价申赎': 0, '占净值比例': 0.0, '持股数': 0, '持仓市值': 0.0}]
```

## 基金份额参考净值

函数是一个特定于Python的内部函数，它旨在获得基金的份额参考净值（IOPV - Indicative Optimized Portfolio Value）。使用此函数，可以轻松获取ETF（交易型开放式指数基金）当前的估算净值，帮助投资者了解基金及其底层资产的实时价值，从而进行更准确的投资决策。

**调用方法**

```py
get_etf_iopv(stock_code)
```

**参数**

| 字段 | 类型 | 说明 |
| --- | --- | --- |
| `stock_code` | `string` | `合约代码` |

**返回值**

- IOPV, 基金份额参考净值

示例返回值

 ```py
# coding:gbk
def init(C):
	pass

def handlebar(C):
	print(get_etf_iopv("510050.SH"))
```

```
2.3079
```

## 基金实时申赎数据

提示

1. 通过指定period为`etfstatistics`获取该数据
2. 该数据为 [VIP 权限数据](https://xuntou.net/#/productvip)
3. 获取时需要先通过 [subscribe\_quote](http://dict.thinktrader.net/innerApi/data_function.html#contextinfo-subscribe-quote-%E8%AE%A2%E9%98%85%E8%A1%8C%E6%83%85%E6%95%B0%E6%8D%AE) 进行订阅

### 原生python

**调用方法**

原生python

```
from xtquant import xtdata
xtdata.download_history_data(stock, 'etfstatistics', start_time, end_time, incrementally = True)
data = xtdata.get_market_data_ex([], stock_list, period = 'etfstatistics', start_time = "", end_time = "")
```

**参数** 除`period`参数需指定为 `etfstatistics` 外，其余参数于 get\_market\_data\_ex 函数一致

**返回值**

分两种，当使用gmd\_ex函数获取时:

- 一个`{stock_code:pd.DataFrame}`结构的dict对象，其中pd.DataFrame的结构为：
  - `index`: 自增序列,`int`类型值
  - `columns`: \['time', '申购笔数', '申购数量', '申购金额', '赎回笔数', '赎回数量', '赎回金额'\]

当使用callback函数时：

- 一个`{stock_code:[{field1:values1,field2:values2,...}]}`的dict嵌套对象

**示例**

示例gmd返回值callback返回值

```
import datetime
from xtquant import xtdata
from datetime import datetime

start_time = datetime.now().strftime("%Y%m%d")
end_time = ''
print('start_time:', start_time, ' end_time:', end_time)
stock_list = ['159001.SZ', '159003.SZ', '159005.SZ', '159150.SZ', '159306.SZ', '159309.SZ', '159502.SZ']
for stock in stock_list:
    '''下载etf实时申赎信息'''
    xtdata.download_history_data(stock, 'etfstatistics', start_time, end_time, incrementally = True)
    print('download finished ' + stock)

data = xtdata.get_market_data_ex([], stock_list, 'etfstatistics', start_time, end_time, -1)
# 打印"159001.SZ"最后5条数据
print(data["159001.SZ"].iloc[-5:])

def f(data):
  print(data)

for i in stock_list:
    xtdata.subscribe_quote(i,period="etfstatistics",callback=f)
```

```
# 打印"159001.SZ"最后5条数据
time	申购笔数	申购数量	申购金额	赎回笔数	赎回数量	赎回金额
17628	1721629992000	417	647341.0	0.0	84	890490.0	0.0
17629	1721629995000	417	647341.0	0.0	84	890490.0	0.0
17630	1721630001000	417	647341.0	0.0	84	890490.0	0.0
17631	1721630007000	417	647341.0	0.0	84	890490.0	0.0
17632	1721630019000	417	647341.0	0.0	84	890490.0	0.0
```

```

{'159150.SZ': [{'time': 1721630379000, 'buyNumber': 0, 'buyAmount': 0.0, 'buyMoney ': 0.0, 'sellNumber': 2, 'sellAmount': 2000000.0, 'sellMoney': 0.0}]}
{'159502.SZ': [{'time': 1721630379000, 'buyNumber': 1, 'buyAmount': 1000000.0, 'buyMoney ': 0.0, 'sellNumber': 0, 'sellAmount': 0.0, 'sellMoney': 0.0}]}
{'159003.SZ': [{'time': 1721630382000, 'buyNumber': 9, 'buyAmount': 10022.0, 'buyMoney ': 0.0, 'sellNumber': 21, 'sellAmount': 33857.0, 'sellMoney': 0.0}]}
{'159502.SZ': [{'time': 1721630382000, 'buyNumber': 1, 'buyAmount': 1000000.0, 'buyMoney ': 0.0, 'sellNumber': 0, 'sellAmount': 0.0, 'sellMoney': 0.0}]}
{'159309.SZ': [{'time': 1721630382000, 'buyNumber': 0, 'buyAmount': 0.0, 'buyMoney ': 0.0, 'sellNumber': 1, 'sellAmount': 1000000.0, 'sellMoney': 0.0}]}
{'159005.SZ': [{'time': 1721630382000, 'buyNumber': 37, 'buyAmount': 2670.0, 'buyMoney ': 0.0, 'sellNumber': 39, 'sellAmount': 30663.0, 'sellMoney': 0.0}]}
```

## 获取场内基金tick数据

要获取场内基金的tick数据，您需要先进行数据订阅`subscribe_quote`以获取最新的tick数据。如果您需要获取历史数据，可以使用`download_history_data`函数下载相关数据，然后使用`get_market_data_ex`函数提取所需的信息。这两个函数的组合可以帮助您获取即时和历史的场内基金数据，使您能够对市场情况有更全面、准确的了解，并帮助您做出更明智的投资决策。

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
# 订阅指定合约最新行情
xtdata.subscribe_quote('513330.SH', period='tick', start_time='', end_time='20231026150000', count=1, callback=None)
# 下载指定合约历史行情
xtdata.download_history_data('513330.SH', 'tick', '20231026093000', '20231026150000')
# 获取指定合约历史行情
tick_data = xtdata.get_market_data_ex(field_list=[], stock_list=['513330.SH'], period='tick', start_time='', end_time='20231026150000', count=10, dividend_type='none', fill_data=True)
print(tick_data)
```

```
{'513330.SH':                          time  lastPrice  ...  settlementPrice  transactionNum
20231026111832  1698290312000      0.372  ...              0.0           28429
20231026111835  1698290315000      0.372  ...              0.0           28430
20231026111838  1698290318000      0.372  ...              0.0           28432
20231026111841  1698290321000      0.372  ...              0.0           28433
20231026111844  1698290324000      0.371  ...              0.0           28434
20231026111847  1698290327000      0.372  ...              0.0           28436
20231026111850  1698290330000      0.372  ...              0.0           28439
20231026111853  1698290333000      0.372  ...              0.0           28439
20231026111856  1698290336000      0.371  ...              0.0           28442
20231026111859  1698290339000      0.372  ...              0.0           28445

[10 rows x 18 columns]}
```

## 基金列表

函数可以实时获取上市的场内基金、ETF（交易所交易基金）以及LOF（Listed Open-end Fund，列出的开放式基金）的列表。这个功能能帮助投资者了解当前上市并且可交易的基金合约，提供最新的数据支持，从而进行更精准的投资决策。

**调用方法**

python

```
# coding=utf-8
from xtquant import xtdata
xtdata.get_stock_list_in_sector(sector_name)
```

**参数**

| 字段 | 类型 | 说明 |
| --- | --- | --- |
| `sector_name` | `str` | `板块名` |

**返回值**

- list：内含成份股代码，代码形式为 'stockcode.market'，如 \['159659.SZ', '513330.SH'\]

示例返回值

```
# coding=utf-8
from xtquant import xtdata
ret_sector_data = get_stock_list_in_sector('沪深基金') [:10]
print(ret_sector_data)
```

```
['588400.SH', '518890.SH', '501208.SH', '516330.SH', '515020.SH',\
'513600.SH', '515860.SH', '510510.SH', '516900.SH', '510760.SH']
```