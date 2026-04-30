---
url: "https://dict.thinktrader.net/dictionary/stock.html"
title: "股票数据 | 迅投知识库"
---

## 获取股票概况

包含股票的上市时间、退市时间、代码、名称、是否是ST等。

### 获取合约基础信息数据

该信息每交易日9点更新

#### 内置Python

提示

旧版本客户端中，函数名为ContextInfo.get_instrumentdetail

**调用方法**

```py

ContextInfo.get_instrument_detail(stockcode)
```

**释义**

根据代码获取合约详细信息

**参数**

| 字段名 | 数据类型 | 解释 |
| --- | --- | --- |
| `stockcode` | `string` | 标的名称，必须是 'stock.market' 形式 |

**返回值**

根据stockcode返回一个dict。该字典数据key值有：

| 名称 | 类型 | 描述 |
| --- | --- | --- |
| ExchangeID | string | 合约市场代码 |
| InstrumentID | string | 合约代码 |
| InstrumentName | string | 合约名称 |
| ProductID | string | 合约的品种ID(期货) |
| ProductName | string | 合约的品种名称(期货) |
| ProductType | int | 合约的类型, 默认-1,枚举值可参考下方说明 |
| ExchangeCode | string | 交易所代码 |
| UniCode | string | 统一规则代码 |
| CreateDate | str | 创建日期 |
| OpenDate | str | 上市日期（特殊值情况见表末） |
| ExpireDate | int | 退市日或者到期日（特殊值情况见表末） |
| PreClose | float | 前收盘价格 |
| SettlementPrice | float | 前结算价格 |
| UpStopPrice | float | 当日涨停价 |
| DownStopPrice | float | 当日跌停价 |
| FloatVolume | float | 流通股本（注意，部分低等级客户端中此字段为FloatVolumn） |
| TotalVolume | float | 总股本（注意，部分低等级客户端中此字段为FloatVolumn） |
| LongMarginRatio | float | 多头保证金率 |
| ShortMarginRatio | float | 空头保证金率 |
| PriceTick | float | 最小价格变动单位 |
| VolumeMultiple | int | 合约乘数(对期货以外的品种，默认是1) |
| MainContract | int | 主力合约标记，1、2、3分别表示第一主力合约，第二主力合约，第三主力合约 |
| LastVolume | int | 昨日持仓量 |
| InstrumentStatus | int | 合约停牌状态(<=0:正常交易（-1:复牌）;>=1停牌天数;) |
| IsTrading | bool | 合约是否可交易 |
| IsRecent | bool | 是否是近月合约 |

提示

字段`OpenDate`有以下几种特殊值： 19700101=新股, 19700102=老股东增发, 19700103=新债, 19700104=可转债, 19700105=配股， 19700106=配号 字段`ExpireDate`为0 或 99999999 时，表示该标的暂无退市日或到期日

字段`ProductType` 对于股票以外的品种，有以下几种值

国内期货市场：1-期货 2-期权(DF SF ZF INE GF) 3-组合套利 4-即期 5-期转现 6-期权(IF) 7-结算价交易(tas) 沪深股票期权市场：0-认购 1-认沽 外盘： 1-100：期货， 101-200：现货, 201-300:股票相关 1：股指期货 2：能源期货 3：农业期货 4：金属期货 5：利率期货 6：汇率期货 7：数字货币期货 99：自定义合约期货 107：数字货币现货 201：股票 202：GDR 203：ETF 204：ETN 300：其他

**示例**

示例返回值

 ```py
# coding:gbk
def init(C):
	pass

def handlebar(C):
	data = C.get_instrumentdetail("000001.SZ")
	print(data)
```

```
{'ExchangeID': 'SZ', 'InstrumentID': '000001', 'InstrumentName': '平安银行', 'ProductID': None, 'ProductName': None, 'CreateDate': 0, 'OpenDate': 19910403, 'ExpireDate': 99999999, 'PreClose': 10.69, 'SettlementPrice': 10.69, 'UpStopPrice': 11.76, 'DownStopPrice': 9.62, 'FloatVolumn': 19405546950.0, 'TotalVolumn': 19405918198.0, 'LongMarginRatio': None, 'ShortMarginRatio': None, 'PriceTick': 0.01, 'VolumeMultiple': 1, 'MainContract': None, 'LastVolume': None, 'InstrumentStatus': 0, 'IsTrading': None, 'IsRecent': None}
```

#### 原生Python

**调用方法**

python

```
from xtquant import xtdata
xtdata.get_instrument_detail(stock_code)
```

**参数**

| 名称 | 类型 | 描述 |
| --- | --- | --- |
| `stock_code` | `string` | `合约代码` |

**返回值**

- 一个字典, 有如下键值，找不到指定合约时返回`None`:

| 名称 | 类型 | 描述 |
| --- | --- | --- |
| ExchangeID | string | 合约市场代码 |
| InstrumentID | string | 合约代码 |
| InstrumentName | string | 合约名称 |
| ProductID | string | 合约的品种ID(期货) |
| ProductName | string | 合约的品种名称(期货) |
| ProductType | int | 合约的类型, 默认-1,枚举值可参考下方说明 |
| ExchangeCode | string | 交易所代码 |
| UniCode | string | 统一规则代码 |
| CreateDate | str | 创建日期 |
| OpenDate | str | 上市日期（特殊值情况见表末） |
| ExpireDate | int | 退市日或者到期日（特殊值情况见表末） |
| PreClose | float | 前收盘价格 |
| SettlementPrice | float | 前结算价格 |
| UpStopPrice | float | 当日涨停价 |
| DownStopPrice | float | 当日跌停价 |
| FloatVolume | float | 流通股本（注意，部分低等级客户端中此字段为FloatVolumn） |
| TotalVolume | float | 总股本（注意，部分低等级客户端中此字段为FloatVolumn） |
| LongMarginRatio | float | 多头保证金率 |
| ShortMarginRatio | float | 空头保证金率 |
| PriceTick | float | 最小价格变动单位 |
| VolumeMultiple | int | 合约乘数(对期货以外的品种，默认是1) |
| MainContract | int | 主力合约标记，1、2、3分别表示第一主力合约，第二主力合约，第三主力合约 |
| LastVolume | int | 昨日持仓量 |
| InstrumentStatus | int | 合约停牌状态(<=0:正常交易（-1:复牌）;>=1停牌天数;) |
| IsTrading | bool | 合约是否可交易 |
| IsRecent | bool | 是否是近月合约 |

提示

字段`OpenDate`有以下几种特殊值： 19700101=新股, 19700102=老股东增发, 19700103=新债, 19700104=可转债, 19700105=配股， 19700106=配号 字段`ExpireDate`为0 或 99999999 时，表示该标的暂无退市日或到期日

字段`ProductType` 对于股票以外的品种，有以下几种值

国内期货市场：1-期货 2-期权(DF SF ZF INE GF) 3-组合套利 4-即期 5-期转现 6-期权(IF) 7-结算价交易(tas) 沪深股票期权市场：0-认购 1-认沽 外盘： 1-100：期货， 101-200：现货, 201-300:股票相关 1：股指期货 2：能源期货 3：农业期货 4：金属期货 5：利率期货 6：汇率期货 7：数字货币期货 99：自定义合约期货 107：数字货币现货 201：股票 202：GDR 203：ETF 204：ETN 300：其他

**示例**

示例返回值

```
from xtquant import xtdata

# 输出平安银行信息的中文名称
xtdata.get_instrument_detail("000001.SZ")
```

```
{"ExchangeID": "SZ",
 "InstrumentID": "000001",
 "InstrumentName": "平安银行",
 "ProductID": "",
 "ProductName": "",
 "ExchangeCode": "000001",
 "UniCode": "000001",
 "CreateDate": "0",
 "OpenDate": "19910403",
 "ExpireDate": 99999999,
 "PreClose": 11.02,
 "SettlementPrice": 11.02,
 "UpStopPrice": 12.12,
 "DownStopPrice": 9.92,
 "FloatVolume": 19405546950.0,
 "TotalVolume": 19405918198.0,
 "LongMarginRatio": 1.7976931348623157e+308,
 "ShortMarginRatio": 1.7976931348623157e+308,
 "PriceTick": 0.01,
 "VolumeMultiple": 1,
 "MainContract": 2147483647,
 "LastVolume": 2147483647,
 "InstrumentStatus": 0,
 "IsTrading": False,
 "IsRecent": False,
 "ProductTradeQuota": 6488165,
 "ContractTradeQuota": 7209071,
 "ProductOpenInterestQuota": 7536740,
 "ContractOpenInterestQuota": 2097193}
```

### 获取板块成分股列表

**调用方法**

python

```
from xtquant import xtdata
xtdata.get_stock_list_in_sector(sector_name)
```

**参数**

| 名称 | 类型 | 描述 |
| --- | --- | --- |
| `sector_name` | `string` | `版块名称` |

**返回**

- `list`

**示例**

示例返回值

```
from xtquant import xtdata
# 获取沪深A股全部股票的代码
xtdata.get_stock_list_in_sector("沪深A股")
```

```
['000001.SZ',
 '000002.SZ',
 '000004.SZ',
 '000005.SZ',
 '000006.SZ',
 '000007.SZ',
 '000008.SZ',
 '000009.SZ',
 '000010.SZ',
 '000011.SZ',
 '000012.SZ',
 '000014.SZ',
 '000016.SZ',
 '000017.SZ',
 '000019.SZ',
 '000020.SZ',
 '000021.SZ',
 '000023.SZ',
 '000025.SZ',
 '000026.SZ',
 '000027.SZ',
 '000028.SZ',
 '000029.SZ',
 '000030.SZ',
 '000031.SZ',
 ...]
```

### 获取某只股票ST的历史

#### 内置python

提示

1. 本函数需要下载历史ST数据(过期合约K线),可通过`界面端数据管理 - 过期合约数据`下载
2. 该数据是 [VIP权限数据](https://xuntou.net/#/productvip)

**原型**

```py
ContextInfo.get_his_st_data(stockcode)
```

**释义**

获取某只股票ST的历史

**参数**

| 字段名 | 数据类型 | 解释 |
| --- | --- | --- |
| `stockcode` | `string` | 股票代码，'stkcode.market'，如'000004.SZ' |

**返回值**

`dict`,st历史，key为ST,*ST,PT,历史未ST会返回{}

**示例**

示例返回值

 ```py
# coding:gbk
def init(C):
	pass

def handlebar(C):
	print(C.get_his_st_data('000004.SZ'))
```

```
{'ST': [['19990427', '20010306'], ['20070525', '20090421'], ['20100531', '20110608'], ['20220506', '20230628']], '*ST': [['20060421', '20070525'], ['20090421', '20100531']]}
```

#### 原生python

提示

1. 获取该数据前需要先调用xtdata.download_his_st_data()进行数据下载
2. 该数据是 [VIP权限数据](https://xuntou.net/#/productvip)

**调用方法**

python

```
from xtquant import xtdata
xtdata.get_his_st_data(stock_code)
```

**参数**

| 名称 | 类型 | 描述 |
| --- | --- | --- |
| `stock_code` | `string` | `股票代码` |

**返回值**

- `dict`类型的st历史，key为ST,*ST,PT,历史未ST会返回{}

| 名称 | 类型 | 描述 |
| --- | --- | --- |
| ST | list | ST时间段 |
| *ST | list | *ST时间段 |
| PT | list | PT时间段 |

**示例**

示例返回值

```
from xtquant import xtdata
import time
# 下载市场历史ST情况
xtdata.download_his_st_data()

# 由于download_his_st_data是异步函数，需要确保下载完成

time.sleep(3)

# 获取000004.SZ历史ST情况
xtdata.get_his_st_data('000004.SZ')
```

```
{"ST": [["19990427", "20010306"],
  ["20070525", "20090421"],
  ["20100531", "20110608"],
  ["20220506", "20230628"]],
 "*ST": [["20060421", "20070525"], ["20090421", "20100531"]]}
```

## 获取行情数据

交易类数据提供股票的交易行情数据，通过API接口调用即可获取相应的数据。

| 名称 | 描述 |
| --- | --- |
| get_market_data | 获取历史数据与实时行情(包含tick数据)，可查询多个标的多个数据字段，返回数据格式为 {field：DataFrame} |
| get_market_data_ex | 获取历史数据与实时行情(包含tick数据)，可查询多个标的多个数据字段，返回数据格式为 {stock_code：DataFrame} |
| get_local_data | 获取历史数据(包含tick数据)，可查询单个或多个标的多个数据字段，返回数据格式为 {stock_code：DataFrame} |
| get_full_tick | 获取最新的 tick 数据 |
| subscribe_whole_quote | 订阅多个标的实时tick数据 |

### 获取历史行情与实时行情

提示：

1. 在gmd系列函数中，历史行情需要从本地读取，所以若想取历史行情，需要先将历史行情下载到本地，而实时行情是从服务器返回的
2. 所以，若需要历史行情，请先使用`界面端`或者`download_history_data`函数进行下载；若需要最新行情，请向服务器进行`订阅`
3. 特别的，对于`xtdata.get_market_data_ex`来说，由于没有subscribe参数，需要在参数外先进行订阅(`subscribe_quote`)才能获取最新行情
4. 对于 **同时获取历史和实时行情** 的情况，gmd系列函数会 **自动进行拼接**


#### 内置Python

**调用方法**

```py
ContextInfo.get_market_data_ex(
    fields=[],
    stock_code=[],
    period='follow',
    start_time='',
    end_time='',
    count=-1,
    dividend_type='follow',
    fill_data=True,
    subscribe=True)
```

**释义**

获取实时行情与历史行情数据

**参数**

| 名称 | 类型 | 描述 |
| --- | --- | --- |
| `field` | `list` | `数据字段，详情见下方field字段表` |
| `stock_list` | `list` | `合约代码列表` |
| `period` | `str` | `数据周期，可选字段为:`<br>`"tick"`<br>`"1m"的整数倍周期`<br>`"5m"的整数倍周期`<br>`"1d"的整数倍周期` |
| `start_time` | `str` | `数据起始时间，格式为 %Y%m%d 或 %Y%m%d%H%M%S，填""为获取历史最早一天` |
| `end_time` | `str` | `数据结束时间，格式为 %Y%m%d 或 %Y%m%d%H%M%S ，填""为截止到最新一天` |
| `count` | `int` | `数据个数` |
| `dividend_type` | `str` | `除权方式,可选值为`<br>`'none'：不复权`<br>`'front':前复权`<br>`'back':后复权`<br>`'front_ratio': 等比前复权`<br>`'back_ratio': 等比后复权` |
| `fill_data` | `bool` | `是否填充数据` |
| `subscribe` | `bool` | `订阅数据开关，默认为True，设置为False时不做数据订阅，只读取本地已有数据。` |

- `field`字段可选：

| field | 数据类型 | 含义 |
| --- | --- | --- |
| `time` | `int` | `时间` |
| `open` | `float` | `开盘价` |
| `high` | `float` | `最高价` |
| `low` | `float` | `最低价` |
| `close` | `float` | `收盘价` |
| `volume` | `float` | `成交量` |
| `amount` | `float` | `成交额` |
| `settle` | `float` | `今结算` |
| `openInterest` | `float` | `持仓量` |
| `preClose` | `float` | `前收盘价` |
| `suspendFlag` | `int` | `停牌` 1停牌，0 不停牌 |

- `period`周期为tick时，`field`字段可选:

| 字段名 | 数据类型 | 含义 |
| --- | --- | --- |
| `time` | `int` | `时间戳` |
| `stime` | `string` | `时间戳字符串形式` |
| `lastPrice` | `float` | `最新价` |
| `open` | `float` | `开盘价` |
| `high` | `float` | `最高价` |
| `low` | `float` | `最低价` |
| `lastClose` | `float` | `前收盘价` |
| `amount` | `float` | `成交总额` |
| `volume` | `int` | `成交总量（手）` |
| `pvolume` | `int` | `原始成交总量(未经过股手转换的成交总量)【不推荐使用】` |
| `stockStatus` | `int` | `证券状态` |
| `openInterest` | `int` | `若是股票，则openInt含义为股票状态，非股票则是持仓量` [openInt字段说明](data_structure.md#openint-%E8%AF%81%E5%88%B8%E7%8A%B6%E6%80%81) |
| `transactionNum` | `float` | `成交笔数(期货没有，单独计算)` |
| `lastSettlementPrice` | `float` | `前结算(股票为0)` |
| `settlementPrice` | `float` | `今结算(股票为0)` |
| `askPrice` | `list[float]` | `多档委卖价` |
| `askVol` | `list[int]` | `多档委卖量` |
| `bidPrice` | `list[float]` | `多档委买价` |
| `bidVol` | `list[int]` | `多档委买量` |

**返回值**

- 返回dict { stock_code1 : value1, stock_code2 : value2, ... }
- value1, value2, ... ：pd.DataFrame 数据集，index为time_list，columns为fields,可参考 [Bar字段](data_structure.md#bar-bar%E5%AF%B9%E8%B1%A1)
- 各标的对应的DataFrame维度相同、索引相同

**示例**

获取行情示例仅获取历史行情仅获取最新行情获取历史行情+最新行情

 ```py
# coding:gbk

def init(C):
  start_date = '20231001'# 格式"YYYYMMDD"，开始下载的日期，date = ""时全量下载
  end_date = ""
  period = "1d"

  need_download = 1  # 取数据是空值时，将need_download赋值为1，确保正确下载了历史数据

  code_list = ["000001.SZ", "600519.SH"] # 股票列表

  if need_download: # 判断要不要下载数据, gmd系列函数都是从本地读取历史数据,从服务器订阅获取最新数据
    my_download(code_list, period, start_date, end_date)

  ############ 仅获取历史行情 #####################
  subscribe = False # 设置订阅参数，使gmd_ex仅返回本地数据
  count = -1 # 设置count参数，使gmd_ex返回全部数据
  data1 = C.get_market_data_ex([],code_list,period = period, start_time = start_date, end_time = end_date,subscribe = subscribe)

  ############ 仅获取最新行情 #####################
  subscribe = True # 设置订阅参数，使gmd_ex仅返回最新行情
  count = 1 # 设置count参数，使gmd_ex仅返回最新行情数据
  data2 = C.get_market_data_ex([],code_list,period = period, start_time = start_date, end_time = end_date,subscribe = subscribe, count = 1) # count 设置为1，使返回值只包含最新行情

  ############ 获取历史行情+最新行情 #####################
  subscribe = True # 设置订阅参数，使gmd_ex仅返回最新行情
  count = -1 # 设置count参数，使gmd_ex返回全部数据
  data3 = C.get_market_data_ex([],code_list,period = period, start_time = start_date, end_time = end_date,subscribe = subscribe, count = -1) # count 设置为-1，使返回值包含最新行情和历史行情

  print(data1[code_list[0]].tail())# 行情数据查看
  print(data2[code_list[0]].tail())
  print(data3[code_list[0]].tail())

def handlebar(C):
  return

def my_download(stock_list,period,start_date = '', end_date = ''):
  '''
  用于显示下载进度
  '''
  if "d" in period:
    period = "1d"
  elif "m" in period:
    if int(period[0]) < 5:
      period = "1m"
    else:
      period = "5m"
  elif "tick" == period:
    pass
  else:
    raise KeyboardInterrupt("周期传入错误")

  n = 1
  num = len(stock_list)
  for i in stock_list:
    print(f"当前正在下载{n}/{num}")

    download_history_data(i,period,start_date, end_date)
    n += 1
  print("下载任务结束")
```

```
当前正在下载1/2
当前正在下载2/2
下载任务结束
start simulation mode
                amount  close   high    low   open  openInterest  preClose
stime
20231124  6.914234e+08  10.10  10.13  10.08  10.11            15     10.15
20231127  8.362684e+08  10.01  10.09   9.97  10.09            15     10.10
20231128  7.844058e+08   9.95  10.02   9.95   9.99            15     10.01
20231129  1.438320e+09   9.72   9.97   9.70   9.95            15      9.95
20231130  8.714817e+08   9.68   9.73   9.62   9.69            15      9.72

          settelementPrice     stime  suspendFlag           time   volume
stime
20231124               0.0  20231124            0  1700755200000   684695
20231127               0.0  20231127            0  1701014400000   836188
20231128               0.0  20231128            0  1701100800000   786175
20231129               0.0  20231129            0  1701187200000  1467597
20231130               0.0  20231130            0  1701273600000   901765
```

```
start simulation mode
                amount  close  high   low  open  openInterest  preClose
stime
20231130  8.714817e+08   9.68  9.73  9.62  9.69            15      9.72

          settelementPrice     stime  suspendFlag           time  volume
stime
20231130               0.0  20231130            0  1701273600000  901765
```

```

start simulation mode
                amount  close   high    low   open  openInterest  preClose
stime
20231124  6.914234e+08  10.10  10.13  10.08  10.11            15     10.15
20231127  8.362684e+08  10.01  10.09   9.97  10.09            15     10.10
20231128  7.844058e+08   9.95  10.02   9.95   9.99            15     10.01
20231129  1.438320e+09   9.72   9.97   9.70   9.95            15      9.95
20231130  8.714817e+08   9.68   9.73   9.62   9.69            15      9.72

          settelementPrice     stime  suspendFlag           time   volume
stime
20231124               0.0  20231124            0  1700755200000   684695
20231127               0.0  20231127            0  1701014400000   836188
20231128               0.0  20231128            0  1701100800000   786175
20231129               0.0  20231129            0  1701187200000  1467597
20231130               0.0  20231130            0  1701273600000   901765
```

#### 原生Python

**调用方法**

python

```
from xtquant import xtdata
xtdata.get_market_data_ex(
    field_list=[],# 字段
    stock_list=[],# 合约代码列表
    period='1d',# 数据周期——1m、5m、1d、tick
    start_time='',# 数据起始时间%Y%m%d或%Y%m%d%H%M%S
    end_time='',# 数据结束时间%Y%m%d或%Y%m%d%H%M%S
    count=-1, # 数据个数
    dividend_type='none', # 除权方式
    fill_data=True, # 是否填充数据
)
```

**参数**

| 名称 | 类型 | 描述 |
| --- | --- | --- |
| `field` | `list` | `数据字段，详情见下方field字段表` |
| `stock_list` | `list` | `合约代码列表` |
| `period` | `str` | `数据周期——1m、5m、1d、tick` |
| `start_time` | `str` | `数据起始时间，格式为 %Y%m%d 或 %Y%m%d%H%M%S，填""为获取历史最早一天` |
| `end_time` | `str` | `数据结束时间，格式为 %Y%m%d 或 %Y%m%d%H%M%S ，填""为截止到最新一天` |
| `count` | `int` | `数据个数` |
| `dividend_type` | `str` | `除权方式` |
| `fill_data` | `bool` | `是否填充数据` |

- `field`字段可选：

| field | 数据类型 | 含义 |
| --- | --- | --- |
| `time` | `int` | `时间` |
| `open` | `float` | `开盘价` |
| `high` | `float` | `最高价` |
| `low` | `float` | `最低价` |
| `close` | `float` | `收盘价` |
| `volume` | `float` | `成交量` |
| `amount` | `float` | `成交额` |
| `settle` | `float` | `今结算` |
| `openInterest` | `float` | `持仓量` |
| `preClose` | `float` | `前收盘价` |
| `suspendFlag` | `int` | `停牌` 1停牌，0 不停牌 |

- `period`周期为tick时，`field`字段可选:

| 字段名 | 数据类型 | 含义 |
| --- | --- | --- |
| `time` | `int` | `时间戳` |
| `stime` | `string` | `时间戳字符串形式` |
| `lastPrice` | `float` | `最新价` |
| `open` | `float` | `开盘价` |
| `high` | `float` | `最高价` |
| `low` | `float` | `最低价` |
| `lastClose` | `float` | `前收盘价` |
| `amount` | `float` | `成交总额` |
| `volume` | `int` | `成交总量（手）` |
| `pvolume` | `int` | `原始成交总量(未经过股手转换的成交总量)【不推荐使用】` |
| `stockStatus` | `int` | `证券状态` |
| `openInterest` | `int` | `若是股票，则openInt含义为股票状态，非股票则是持仓量` [openInt字段说明](data_structure.md#openint-%E8%AF%81%E5%88%B8%E7%8A%B6%E6%80%81) |
| `transactionNum` | `float` | `成交笔数(期货没有，单独计算)` |
| `lastSettlementPrice` | `float` | `前结算(股票为0)` |
| `settlementPrice` | `float` | `今结算(股票为0)` |
| `askPrice` | `list[float]` | `多档委卖价` |
| `askVol` | `list[int]` | `多档委卖量` |
| `bidPrice` | `list[float]` | `多档委买价` |
| `bidVol` | `list[int]` | `多档委买量` |

**返回值**

- period为`1m``5m``1d`K线周期时
  - 返回dict { field1 : value1, field2 : value2, ... }
  - value1, value2, ... ：pd.DataFrame 数据集，index为stock_list，columns为time_list
  - 各字段对应的DataFrame维度相同、索引相同

**示例**

示例仅获取历史行情仅获取最新行情获取历史行情+最新行情

```

from xtquant import xtdata
import time

def my_download(stock_list:list,period:str,start_date = '', end_date = ''):
    '''
    用于显示下载进度
    '''
    import string

    if [i for i in ["d","w","mon","q","y",] if i in period]:
        period = "1d"
    elif "m" in period:
        numb = period.translate(str.maketrans("", "", string.ascii_letters))
        if int(numb) < 5:
            period = "1m"
        else:
            period = "5m"
    elif "tick" == period:
        pass
    else:
        raise KeyboardInterrupt("周期传入错误")

    n = 1
    num = len(stock_list)
    for i in stock_list:
        print(f"当前正在下载 {period} {n}/{num}")

        xtdata.download_history_data(i,period,start_date, end_date)
        n += 1
    print("下载任务结束")

def do_subscribe_quote(stock_list:list, period:str):
  for i in stock_list:
    xtdata.subscribe_quote(i,period = period)
  time.sleep(1) # 等待订阅完成

if __name__ == "__main__":

  start_date = '20231001'# 格式"YYYYMMDD"，开始下载的日期，date = ""时全量下载
  end_date = ""
  period = "1d"

  need_download = 1  # 取数据是空值时，将need_download赋值为1，确保正确下载了历史数据

  code_list = ["000001.SZ", "600519.SH"] # 股票列表

  if need_download: # 判断要不要下载数据, gmd系列函数都是从本地读取历史数据,从服务器订阅获取最新数据
    my_download(code_list, period, start_date, end_date)

  ############ 仅获取历史行情 #####################
  count = -1 # 设置count参数，使gmd_ex返回全部数据
  data1 = xtdata.get_market_data_ex([],code_list,period = period, start_time = start_date, end_time = end_date)

  ############ 仅获取最新行情 #####################
  do_subscribe_quote(code_list,period)# 设置订阅参数，使gmd_ex取到最新行情
  count = 1 # 设置count参数，使gmd_ex仅返回最新行情数据
  data2 = xtdata.get_market_data_ex([],code_list,period = period, start_time = start_date, end_time = end_date, count = 1) # count 设置为1，使返回值只包含最新行情

  ############ 获取历史行情+最新行情 #####################
  do_subscribe_quote(code_list,period) # 设置订阅参数，使gmd_ex取到最新行情
  count = -1 # 设置count参数，使gmd_ex返回全部数据
  data3 = xtdata.get_market_data_ex([],code_list,period = period, start_time = start_date, end_time = end_date, count = -1) # count 设置为1，使返回值只包含最新行情

  print(data1[code_list[0]].tail())# 行情数据查看
  print(data2[code_list[0]].tail())
  print(data3[code_list[0]].tail())
```

```
当前正在下载1/2
当前正在下载2/2
下载任务结束

                amount  close   high    low   open  openInterest  preClose
stime
20231124  6.914234e+08  10.10  10.13  10.08  10.11            15     10.15
20231127  8.362684e+08  10.01  10.09   9.97  10.09            15     10.10
20231128  7.844058e+08   9.95  10.02   9.95   9.99            15     10.01
20231129  1.438320e+09   9.72   9.97   9.70   9.95            15      9.95
20231130  8.714817e+08   9.68   9.73   9.62   9.69            15      9.72

          settelementPrice     stime  suspendFlag           time   volume
stime
20231124               0.0  20231124            0  1700755200000   684695
20231127               0.0  20231127            0  1701014400000   836188
20231128               0.0  20231128            0  1701100800000   786175
20231129               0.0  20231129            0  1701187200000  1467597
20231130               0.0  20231130            0  1701273600000   901765
```

```

                amount  close  high   low  open  openInterest  preClose
stime
20231130  8.714817e+08   9.68  9.73  9.62  9.69            15      9.72

          settelementPrice     stime  suspendFlag           time  volume
stime
20231130               0.0  20231130            0  1701273600000  901765
```

```

                amount  close   high    low   open  openInterest  preClose
stime
20231124  6.914234e+08  10.10  10.13  10.08  10.11            15     10.15
20231127  8.362684e+08  10.01  10.09   9.97  10.09            15     10.10
20231128  7.844058e+08   9.95  10.02   9.95   9.99            15     10.01
20231129  1.438320e+09   9.72   9.97   9.70   9.95            15      9.95
20231130  8.714817e+08   9.68   9.73   9.62   9.69            15      9.72

          settelementPrice     stime  suspendFlag           time   volume
stime
20231124               0.0  20231124            0  1700755200000   684695
20231127               0.0  20231127            0  1701014400000   836188
20231128               0.0  20231128            0  1701100800000   786175
20231129               0.0  20231129            0  1701187200000  1467597
20231130               0.0  20231130            0  1701273600000   901765
```

### 获取股票历史涨跌停价格

#### 原生Python

提示

1. 获取该数据前需要先调用`xtdata.download_history_data`进行下载，period参数选择`"stoppricedata"`

2. 该数据通过`get_market_data_ex`接口获取，period参数选择`"stoppricedata"`

3. 若是只需要最新一天的涨跌停价格，可通过 [get_instrument_detail](stock.md#%E8%8E%B7%E5%8F%96%E8%82%A1%E7%A5%A8%E6%A6%82%E5%86%B5) 的`UpStopPrice`和`DownStopPrice`字段获取

4. 该数据是 [VIP权限数据](https://xuntou.net/#/productvip)


**调用方法**

```
get_market_data_ex([],stock_list,period="stoppricedata",start_time = "", end_time = "")
```

**参数**

| 参数名称 | 类型 | 描述 |
| --- | --- | --- |
| `field_list` | `list` | 数据字段列表，传空则为全部字段 |
| `stock_list` | `list` | 合约代码列表 |
| `period` | `string` | 周期 |
| `start_time` | `string` | 起始时间 |
| `end_time` | `string` | 结束时间 |
| `count` | `int` | 数据个数。默认参数，大于等于0时，若指定了 `start_time`，`end_time`，此时以 `end_time` 为基准向前取 `count` 条；若 `start_time`，`end_time` 缺省，默认取本地数据最新的 `count` 条数据；若 `start_time`，`end_time`，`count` 都缺省时，默认取本地全部数据 |

**返回值**

返回一个 {`stock_code`:`pd.DataFrame`} 结构的`dict`对象，默认的列索引为取得的全部字段. 如果给定了 `fields` 参数, 则列索引与给定的 `fields` 对应.

**示例**

python返回值

```

from xtquant import xtdata

stock_list = xtdata.get_stock_list_in_sector("沪深A股")[:5]

# 下载涨跌停价格数据
for i in stock_list:
  xtdata.download_history_data(i, 'stoppricedata', '', '')

# 获取涨跌停价格数据
data = xtdata.get_market_data_ex([], stock_list, 'stoppricedata', '', '')

print(data)
```

```

{'000001.SZ':                time    涨停价   跌停价
 0      663004800000   0.00  0.00
 1      663609600000   0.00  0.00
 2      664214400000   0.00  0.00
 3      664819200000   0.00  0.00
 4      665424000000   0.00  0.00
 ...             ...    ...   ...
 7824  1701360000000  10.65  8.71
 7825  1701619200000  10.63  8.69
 7826  1701705600000  10.59  8.67
 7827  1701792000000  10.43  8.53
 7828  1701878400000  10.45  8.55

 [7829 rows x 3 columns],
 '000002.SZ':                time    涨停价    跌停价
 0      663004800000   0.00   0.00
 1      664214400000   0.00   0.00
 2      665078400000   0.00   0.00
 3      665164800000   0.00   0.00
 4      665424000000   0.00   0.00
 ...             ...    ...    ...
 7816  1701360000000  12.58  10.30
 7817  1701619200000  12.54  10.26
 7818  1701705600000  12.30  10.06
 7819  1701792000000  11.87   9.71
 7820  1701878400000  11.94   9.77

 [7821 rows x 3 columns],
 '000004.SZ':                time    涨停价    跌停价
 0      663004800000   0.00   0.00
 1      663609600000   0.00   0.00
 2      663782400000   0.00   0.00
 3      663868800000   0.00   0.00
 4      663955200000   0.00   0.00
 ...             ...    ...    ...
 7687  1701360000000  19.09  15.62
 7688  1701619200000  19.71  16.13
 7689  1701705600000  19.94  16.32
 7690  1701792000000  19.00  15.54
 7691  1701878400000  18.72  15.32

 [7692 rows x 3 columns],
 '000005.SZ':                time   涨停价   跌停价
 0      661536000000  0.00  0.00
 1      661622400000  0.00  0.00
 2      661708800000  0.00  0.00
 3      661968000000  0.00  0.00
 4      662054400000  0.00  0.00
 ...             ...   ...   ...
 7303  1701360000000  1.47  1.33
 7304  1701619200000  1.47  1.33
 7305  1701705600000  1.48  1.34
 7306  1701792000000  1.48  1.34
 7307  1701878400000  1.47  1.33

 [7308 rows x 3 columns],
 '000006.SZ':                time   涨停价   跌停价
 0      704304000000  0.00  0.00
 1      704390400000  0.00  0.00
 2      704476800000  0.00  0.00
 3      704563200000  0.00  0.00
 4      704822400000  0.00  0.00
 ...             ...   ...   ...
 7491  1701360000000  5.09  4.17
 7492  1701619200000  5.14  4.20
 7493  1701705600000  5.12  4.19
 7494  1701792000000  5.07  4.15
 7495  1701878400000  5.27  4.31

 [7496 rows x 3 columns]}
```

### 股票快照指标

提供标的的量比，涨速，换手率等数据

提示

1. 通过指定period为`snapshotindex`获取该数据
2. 该数据为 [VIP 权限数据](https://xuntou.net/#/productvip)
3. 获取时需要先通过 [subscribe_quote](http://dict.thinktrader.net/innerApi/data_function.html#contextinfo-subscribe-quote-%E8%AE%A2%E9%98%85%E8%A1%8C%E6%83%85%E6%95%B0%E6%8D%AE) 进行订阅

#### 原生python

**调用方法**

```
xtdata.get_market_data_ex([],stock_list,period="snapshotindex",start_time = "", end_time = "")
```

**返回值**

分两种，当使用gmd_ex函数获取时:

- 一个`{stock_code:pd.DataFrame}`结构的dict对象，其中pd.DataFrame的结构为：
  - `index`: 时间序列,`str`类型值
  - `columns`: ['time', '量比', '1分钟涨速', '5分钟涨速', '3日涨幅', '5日涨幅', '10日涨幅', '3日换手', '5日换手', '10日换手']

当使用callback函数时：

- 一个`{stock_code:[{field1:values1,field2:values2,...}]}`的dict嵌套对象

**示例**

python返回值

```
from xtquant import xtdata

def f(data):
    print(data)

# 获取前需要先订阅，该数据通过指定period = 'snapshotindex'获取
xtdata.subscribe_quote("000001.SZ",period = 'snapshotindex', count = -1,callback = f)

data = xtdata.get_market_data_ex([],["000001.SZ"],period="snapshotindex",start_time = "", end_time = "",count = 10)
print(data)
```

```
{'000001.SZ':                          time     量比  1分钟涨速  5分钟涨速      3日涨幅      5日涨幅
 20230724093000  1690162200000   0.00   0.00   0.00  0.001768  0.001768
 20230724093100  1690162260000  10.53  -0.09  -0.09  0.000000  0.000000
 20230724093200  1690162320000   6.84  -0.35  -0.44 -0.003537 -0.003537
 20230724093300  1690162380000   6.42   0.09  -0.35 -0.002653 -0.002653
 20230724093400  1690162440000   6.04  -0.09  -0.44 -0.003537 -0.003537
 ...                       ...    ...    ...    ...       ...       ...
 20240229143000  1709188200000   0.51   0.00   0.10 -0.003799 -0.037615
 20240229143100  1709188260000   0.51   0.00   0.00 -0.003799 -0.037615
 20240229143200  1709188320000   0.51   0.00   0.00 -0.003799 -0.037615
 20240229143300  1709188380000   0.51   0.00   0.10 -0.003799 -0.037615
 20240229143400  1709188440000   0.51   0.10   0.19 -0.002849 -0.036697

                    10日涨幅      3日换手      5日换手     10日换手
 20230724093000  0.011607  0.004827  0.009229  0.028597
 20230724093100  0.009821  0.004901  0.009303  0.028672
 20230724093200  0.006250  0.004936  0.009337  0.028706
 20230724093300  0.007143  0.004993  0.009395  0.028763
 20230724093400  0.006250  0.005044  0.009445  0.028814
 ...                  ...       ...       ...       ...
 20240229143000  0.091571  0.033694  0.066829  0.140845
 20240229143100  0.091571  0.033734  0.066870  0.140886
 20240229143200  0.091571  0.033758  0.066894  0.140910
 20240229143300  0.091571  0.033826  0.066961  0.140977
 20240229143400  0.092612  0.033828  0.066963  0.140979

 [35134 rows x 10 columns]}

{'000001.SZ': [{'time': 1709188440000, '量比': 0.51, '1分钟涨速': 0.0, '5分钟涨速': 0.1, '3日涨幅': -0.0037, '5日涨幅': -0.0376, '10日涨幅': 0.0915, '3日换手': 0.0338, '5日换手': 0.0669, '10日换手': 0.1409}]}
{'000001.SZ': [{'time': 1709188440000, '量比': 0.51, '1分钟涨速': 0.19, '5分钟涨速': 0.1, '3日涨幅': -0.0028, '5日涨幅': -0.0366, '10日涨幅': 0.0926, '3日换手': 0.0338, '5日换手': 0.0669, '10日换手': 0.1409}]}
```

### 涨跌停/集合竞价表现

#### 原生python

提供开盘集合竞价成交量，收盘集合竞价成交量，炸板次数，涨停金额等数据

提示

1. 通过指定period为`limitupperformance`获取该数据
2. 该数据为 [VIP 权限数据](https://xuntou.net/#/productvip)
3. 获取历史数据时需要先通过[download_history_data]进行下载，实时数据通过 [subscribe_quote](http://dict.thinktrader.net/innerApi/data_function.html#contextinfo-subscribe-quote-%E8%AE%A2%E9%98%85%E8%A1%8C%E6%83%85%E6%95%B0%E6%8D%AE) 进行订阅

**调用方法**

```
xtdata.get_market_data_ex([],stock_list,period="limitupperformance",start_time = "", end_time = "")
```

**返回值**

| 字段名 | 数据类型 | 含义 |
| --- | --- | --- |
| time | int | 时间戳 |
| openVol | int | 开盘集合竞价的成交量 |
| closeVol | int | 收盘集合竞价的成交量 |
| finalVol | int | 盘后定价的成交量 |
| startUp | int | 涨停开始时间 |
| endUp | int | 涨停结束时间 |
| breakUp | int | 炸板次数 |
| upAmount | float | 涨停金额 |
| startDn | int | 跌停开始时间 |
| endDn | int | 跌停结束时间 |
| breakDn | int | 开板次数 |
| dnAmount | float | 跌停金额 |
| direct | int | 涨跌方向 0-无 1-涨停 2-跌停 |
| sealVolRatio | float | 封成比 |
| sealFreeRatio | float | 封流比 |
| bidPreRatio | float | 竞昨比 |
| sealCount | int | 几板 |
| sealDays | int | 几天 |
| sealBreak | int | 封板中断天数 |

**示例**

python返回值

```
from xtquant import xtdata

def f(data):
    print(data)

period = "limitupperformance"
stock = "000001.SZ"
ls = [stock]
xtdata.download_history_data2(ls,period = period) # 下载历史数据

# 获取前需要先订阅，该数据通过指定period = 'limitupperformance'获取
xtdata.subscribe_quote(stock,period = 'limitupperformance', count = -1,callback = f)

data = xtdata.get_market_data_ex([],[stock],period="limitupperformance",start_time = "", end_time = "",count = 10)
print(data)
```

```
{'000001.SZ':                          time  openVol  closeVol  finalVol  startUp  endUp
 20190531000000  1559232000000     6334     15124         0        0      0
 20190603000000  1559491200000     6873     10702         0        0      0
 20190604000000  1559577600000     4707      5957         0        0      0
 20190605000000  1559664000000     9472      3344         0        0      0
 20190606000000  1559750400000     4165      6051         0        0      0
 ...                       ...      ...       ...       ...      ...    ...
 20240513000000  1715529600000    19142     13848         0        0      0
 20240514000000  1715616000000    15960     15193         0        0      0
 20240515000000  1715702400000     4481     11689         0        0      0
 20240516000000  1715788800000     3377     25695         0        0      0
 20240517000000  1715875200000    31414     51721         0        0      0

                 breakUp  upAmount  startDn  endDn  breakDn  dnAmount  direct
 20190531000000        0       0.0        0      0        0       0.0       0
 20190603000000        0       0.0        0      0        0       0.0       0
 20190604000000        0       0.0        0      0        0       0.0       0
 20190605000000        0       0.0        0      0        0       0.0       0
 20190606000000        0       0.0        0      0        0       0.0       0
 ...                 ...       ...      ...    ...      ...       ...     ...
 20240513000000        0       0.0        0      0        0       0.0       0
 20240514000000        0       0.0        0      0        0       0.0       0
 20240515000000        0       0.0        0      0        0       0.0       0
 20240516000000        0       0.0        0      0        0       0.0       0
 20240517000000        0       0.0        0      0        0       0.0       0

                 sealVolRatio  sealFreeRatio  bidPreRatio  sealCount  sealDays
 20190531000000           0.0            0.0     0.980064          0         0
 20190603000000           0.0            0.0     1.000737          0         0
 20190604000000           0.0            0.0     0.311162          0         0
 20190605000000           0.0            0.0     0.971831          0         0
 20190606000000           0.0            0.0     0.556155          0         0
 ...                      ...            ...          ...        ...       ...
 20240513000000           0.0            0.0     1.082793          0         0
 20240514000000           0.0            0.0     1.137969          0         0
 20240515000000           0.0            0.0     0.416533          0         0
 20240516000000           0.0            0.0     0.388922          0         0
 20240517000000           0.0            0.0     1.021164          0         0

                 sealBreak
 20190531000000          0
 20190603000000          0
 20190604000000          0
 20190605000000          0
 20190606000000          0
 ...                   ...
 20240513000000          0
 20240514000000          0
 20240515000000          0
 20240516000000          0
 20240517000000          0

 [1204 rows x 19 columns]}
```

## 获取股票资金流向数据

获取一只或者多只股票在一个时间段内的资金流向数据

提示

1.该数据通过`get_market_data`和`get_market_data_ex`接口获取，period参数选择`transactioncount1d` 或者 `transactioncount1m`

2.获取历史数据前需要先用`download_history_data`下载历史数据

3. [VIP 权限数据](https://xuntou.net/#/productvip)

### 内置python

**原型**

```py
# 逐笔成交统计日级
C.get_market_data_ex([],stock_list,period="transactioncount1d",start_time = "", end_time = "")
# 逐步成交统计1分钟级
C.get_market_data_ex([],stock_list,period="transactioncount1m",start_time = "", end_time = "")
```

**参数**

除period参数需指定为`transactioncount1d` 或者 `transactioncount1m`外，其余参数与 [ContextInfo.get_market_data_ex](data_function.md#contextinfo-get-market-data-ex-%E8%8E%B7%E5%8F%96%E8%A1%8C%E6%83%85%E6%95%B0%E6%8D%AE) 一致

**返回值**

- 返回dict { stock_code1 : value1, stock_code2 : value2, ... }
- value1, value2, ... ：pd.DataFrame 数据集，index为time_list，columns为fields

提示

特大单：成交金额大于或等于100万元或成交量大于或等于5000手

大单：成交金额大于或等于20万元或成交量大于或等于1000手

中单：成交金额大于或等于4万元或成交量大于或等于200手

小单：其它为小单

| 字段名 | 数据类型 | 解释 |
| --- | --- | --- |
| time | int | 时间戳 |
| bidNumber | int | 主买单总单数 |
| offNumber | int | 主卖单总单数 |
| ddx | float | 大单动向 |
| ddy | float | 涨跌动因 |
| ddz | float | 大单差分 |
| netOrder | int | 净挂单量 |
| netWithdraw | int | 净撤单量 |
| withdrawBid | int | 总撤买量 |
| withdrawOff | int | 总撤卖量 |
| bidNumberDx | int | 主买单总单数增量 |
| offNumberDx | int | 主卖单总单数增量 |
| transactionNumber | int | 成交笔数增量 |
| bidMostAmount | float | 主买特大单成交额 |
| bidBigAmount | float | 主买大单成交额 |
| bidMediumAmount | float | 主买中单成交额 |
| bidSmallAmount | float | 主买小单成交额 |
| bidTotalAmount | float | 主买累计成交额 |
| offMostAmount | float | 主卖特大单成交额 |
| offBigAmount | float | 主卖大单成交额 |
| offMediumAmount | float | 主卖中单成交额 |
| offSmallAmount | float | 主卖小单成交额 |
| offTotalAmount | float | 主卖累计成交额 |
| unactiveBidMostAmount | float | 被动买特大单成交额 |
| unactiveBidBigAmount | float | 被动买大单成交额 |
| unactiveBidMediumAmount | float | 被动买中单成交额 |
| unactiveBidSmallAmount | float | 被动买小单成交额 |
| unactiveBidTotalAmount | float | 被动买累计成交额 |
| unactiveOffMostAmount | float | 被动卖特大单成交额 |
| unactiveOffBigAmount | float | 被动卖大单成交额 |
| unactiveOffMediumAmount | float | 被动卖中单成交额 |
| unactiveOffSmallAmount | float | 被动卖小单成交额 |
| unactiveOffTotalAmount | float | 被动卖累计成交额 |
| netInflowMostAmount | float | 净流入超大单成交额 |
| netInflowBigAmount | float | 净流入大单成交额 |
| netInflowMediumAmount | float | 净流入中单成交额 |
| netInflowSmallAmount | float | 净流入小单成交额 |
| bidMostVolume | int | 主买特大单成交量 |
| bidBigVolume | int | 主买大单成交量 |
| bidMediumVolume | int | 主买中单成交量 |
| bidSmallVolume | int | 主买小单成交量 |
| bidTotalVolume | int | 主买累计成交量 |
| offMostVolume | int | 主卖特大单成交量 |
| offBigVolume | int | 主卖大单成交量 |
| offMediumVolume | int | 主卖中单成交量 |
| offSmallVolume | int | 主卖小单成交量 |
| offTotalVolume | int | 主卖累计成交量 |
| unactiveBidMostVolume | int | 被动买特大单成交量 |
| unactiveBidBigVolume | int | 被动买大单成交量 |
| unactiveBidMediumVolume | int | 被动买中单成交量 |
| unactiveBidSmallVolume | int | 被动买小单成交量 |
| unactiveBidTotalVolume | int | 被动买累计成交量 |
| unactiveOffMostVolume | int | 被动卖特大单成交量 |
| unactiveOffBigVolume | int | 被动卖大单成交量 |
| unactiveOffMediumVolume | int | 被动卖中单成交量 |
| unactiveOffSmallVolume | int | 被动卖小单成交量 |
| unactiveOffTotalVolume | int | 被动卖累计成交量 |
| netInflowMostVolume | int | 净流入超大单成交量 |
| netInflowBigVolume | int | 净流入大单成交量 |
| netInflowMediumVolume | int | 净流入中单成交量 |
| netInflowSmallVolume | int | 净流入小单成交量 |
| bidMostAmountDx | float | 主买特大单成交额增量 |
| bidBigAmountDx | float | 主买大单成交额增量 |
| bidMediumAmountDx | float | 主买中单成交额增量 |
| bidSmallAmountDx | float | 主买小单成交额增量 |
| bidTotalAmountDx | float | 主买累计成交额增量 |
| offMostAmountDx | float | 主卖特大单成交额增量 |
| offBigAmountDx | float | 主卖大单成交额增量 |
| offMediumAmountDx | float | 主卖中单成交额增量 |
| offSmallAmountDx | float | 主卖小单成交额增量 |
| offTotalAmountDx | float | 主卖累计成交额增量 |
| unactiveBidMostAmountDx | float | 被动买特大单成交额增量 |
| unactiveBidBigAmountDx | float | 被动买大单成交额增量 |
| unactiveBidMediumAmountDx | float | 被动买中单成交额增量 |
| unactiveBidSmallAmountDx | float | 被动买小单成交额增量 |
| unactiveBidTotalAmountDx | float | 被动买累计成交额增量 |
| unactiveOffMostAmountDx | float | 被动卖特大单成交额增量 |
| unactiveOffBigAmountDx | float | 被动卖大单成交额增量 |
| unactiveOffMediumAmountDx | float | 被动卖中单成交额增量 |
| unactiveOffSmallAmountDx | float | 被动卖小单成交额增量 |
| unactiveOffTotalAmountDx | float | 被动卖累计成交额增量 |
| netInflowMostAmountDx | float | 净流入超大单成交额增量 |
| netInflowBigAmountDx | float | 净流入大单成交额增量 |
| netInflowMediumAmountDx | float | 净流入中单成交额增量 |
| netInflowSmallAmountDx | float | 净流入小单成交额增量 |
| bidMostVolumeDx | int | 主买特大单成交量增量 |
| bidBigVolumeDx | int | 主买大单成交量增量 |
| bidMediumVolumeDx | int | 主买中单成交量增量 |
| bidSmallVolumeDx | int | 主买小单成交量增量 |
| bidTotalVolumeDx | int | 主买累计成交量增量 |
| offMostVolumeDx | int | 主卖特大单成交量增量 |
| offBigVolumeDx | int | 主卖大单成交量增量 |
| offMediumVolumeDx | int | 主卖中单成交量增量 |
| offSmallVolumeDx | int | 主卖小单成交量增量 |
| offTotalVolumeDx | int | 主卖累计成交量增量 |
| unactiveBidMostVolumeDx | int | 被动买特大单成交量增量 |
| unactiveBidBigVolumeDx | int | 被动买大单成交量增量 |
| unactiveBidMediumVolumeDx | int | 被动买中单成交量增量 |
| unactiveBidSmallVolumeDx | int | 被动买小单成交量增量 |
| unactiveBidTotalVolumeDx | int | 被动买累计成交量增量 |
| unactiveOffMostVolumeDx | int | 被动卖特大单成交量增量 |
| unactiveOffBigVolumeDx | int | 被动卖大单成交量增量 |
| unactiveOffMediumVolumeDx | int | 被动卖中单成交量增量 |
| unactiveOffSmallVolumeDx | int | 被动卖小单成交量增量 |
| unactiveOffTotalVolumeDx | int | 被动卖累计成交量增量 |
| netInflowMostVolumeDx | int | 净流入超大单成交量增量 |
| netInflowBigVolumeDx | int | 净流入大单成交量增量 |
| netInflowMediumVolumeDx | int | 净流入中单成交量增量 |
| netInflowSmallVolumeDx | int | 净流入小单成交量增量 |

**示例**

python返回值

 ```py
# coding:gbk

def init(C):
    return


def f(data):
    print(data)

def after_init(C):
    stock_list = ["000001.SZ"]
    if 1:
        download_history_data("000001.SZ","transactioncount1d",'','')


    C.subscribe_quote("000001.SZ","transactioncount1d",callback = f)
    # C.subscribe_quote("000001.SZ","transactioncount1d")
    print(C.get_market_data_ex([],stock_list,period="transactioncount1d",start_time = "", end_time = ""))
    pass
```

```

start simulation mode
{'000001.SZ':                    time     stime  bidNumber  offNumber   ddx  ...
stime                                                          ...
20250516  1747324800000  20250516       1550       1507 -2.51  ...
          unactiveOffTotalVolumeDx  netInflowMostVolumeDx
stime
20250516                    328617                      0
          netInflowBigVolumeDx  netInflowMediumVolumeDx
stime
20250516                     0                        0
          netInflowSmallVolumeDx
stime
20250516                       0  [1 rows x 110 columns]}

{'000001.SZ':                    time     stime  bidNumber  offNumber          ddx  ...
stime                                                                 ...
20230801  1690819200000  20230801       2191          0  12327955.00  ...
20230802  1690905600000  20230802       2464          0  11194205.00  ...
20230803  1690992000000  20230803       2230          0  10885057.00  ...
20230804  1691078400000  20230804       2298          0  11119479.00  ...
20230807  1691337600000  20230807       1995          0  16092011.00  ...
...                 ...       ...        ...        ...          ...  ...
20250512  1746979200000  20250512       2245          0  15021368.00  ...
20250513  1747065600000  20250513       2020          0  15908930.00  ...
20250514  1747152000000  20250514       2378          0  11124173.00  ...
20250515  1747238400000  20250515       2177          0  13139036.00  ...
20250516  1747324800000  20250516       1534       1492        -2.52  ...

          unactiveOffTotalVolumeDx  netInflowMostVolumeDx
stime
20230801                         0                    716
20230802                         0                  -1933
20230803                         0                  -1383
20230804                         0                   -798
20230807                         0                   2425
...                            ...                    ...
20250512        455631063339761664      -5434394755989187
20250513        459072581333417984      -7135253671964321
20250514        463965350866714624      -6642651424095361
20250515        454601440107692032      -2439668058552763
20250516                    327626                      0

          netInflowBigVolumeDx  netInflowMediumVolumeDx
stime
20230801                 75879                   171779
20230802                 -5034                   276211
20230803               -169004                   398601
20230804                 68341                   326952
20230807                  8207                   125727
...                        ...                      ...
20250512     -4763444846873791       -10501628226169660
20250513     -3495947015496893       -10581682322706995
20250514     -8658337684285924       -13378567106110239
20250515     -3747962710555290       -12682859378414047
20250516                     0                        0

          netInflowSmallVolumeDx
stime
20230801                  179228
20230802                  184852
20230803                  199623
20230804                  206804
20230807                  114136
...                          ...
20250512       22232073758714901
20250513       26151815523499053
20250514       28225223249912353
20250515       26390287081427330
20250516                       0

[432 rows x 110 columns]}
```

### 原生python

**原型**

原生python

```
# 逐笔成交统计日级
get_market_data_ex([],stock_list,period="transactioncount1d",start_time = "", end_time = "")
# 逐步成交统计1分钟级
get_market_data_ex([],stock_list,period="transactioncount1m",start_time = "", end_time = "")
```

**参数**

| 参数名称 | 类型 | 描述 |
| --- | --- | --- |
| `field_list` | `list` | 数据字段列表，传空则为全部字段 |
| `stock_list` | `list` | 合约代码列表 |
| `period` | `string` | 周期 |
| `start_time` | `string` | 起始时间 |
| `end_time` | `string` | 结束时间 |
| `count` | `int` | 数据个数。默认参数，大于等于0时，若指定了 `start_time`，`end_time`，此时以 `end_time` 为基准向前取 `count` 条；若 `start_time`，`end_time` 缺省，默认取本地数据最新的 `count` 条数据；若 `start_time`，`end_time`，`count` 都缺省时，默认取本地全部数据 |
| `dividend_type` | `string` | 除权方式 |
| `fill_data` | `bool` | 是否向后填充空缺数据 |

- `field_list`字段可选:

提示

特大单：成交金额大于或等于100万元或成交量大于或等于5000手

大单：成交金额大于或等于20万元或成交量大于或等于1000手

中单：成交金额大于或等于4万元或成交量大于或等于200手

小单：其它为小单

| 字段名 | 数据类型 | 解释 |
| --- | --- | --- |
| time | int | 时间戳 |
| bidNumber | int | 主买单总单数 |
| offNumber | int | 主卖单总单数 |
| ddx | float | 大单动向 |
| ddy | float | 涨跌动因 |
| ddz | float | 大单差分 |
| netOrder | int | 净挂单量 |
| netWithdraw | int | 净撤单量 |
| withdrawBid | int | 总撤买量 |
| withdrawOff | int | 总撤卖量 |
| bidNumberDx | int | 主买单总单数增量 |
| offNumberDx | int | 主卖单总单数增量 |
| transactionNumber | int | 成交笔数增量 |
| bidMostAmount | float | 主买特大单成交额 |
| bidBigAmount | float | 主买大单成交额 |
| bidMediumAmount | float | 主买中单成交额 |
| bidSmallAmount | float | 主买小单成交额 |
| bidTotalAmount | float | 主买累计成交额 |
| offMostAmount | float | 主卖特大单成交额 |
| offBigAmount | float | 主卖大单成交额 |
| offMediumAmount | float | 主卖中单成交额 |
| offSmallAmount | float | 主卖小单成交额 |
| offTotalAmount | float | 主卖累计成交额 |
| unactiveBidMostAmount | float | 被动买特大单成交额 |
| unactiveBidBigAmount | float | 被动买大单成交额 |
| unactiveBidMediumAmount | float | 被动买中单成交额 |
| unactiveBidSmallAmount | float | 被动买小单成交额 |
| unactiveBidTotalAmount | float | 被动买累计成交额 |
| unactiveOffMostAmount | float | 被动卖特大单成交额 |
| unactiveOffBigAmount | float | 被动卖大单成交额 |
| unactiveOffMediumAmount | float | 被动卖中单成交额 |
| unactiveOffSmallAmount | float | 被动卖小单成交额 |
| unactiveOffTotalAmount | float | 被动卖累计成交额 |
| netInflowMostAmount | float | 净流入超大单成交额 |
| netInflowBigAmount | float | 净流入大单成交额 |
| netInflowMediumAmount | float | 净流入中单成交额 |
| netInflowSmallAmount | float | 净流入小单成交额 |
| bidMostVolume | int | 主买特大单成交量 |
| bidBigVolume | int | 主买大单成交量 |
| bidMediumVolume | int | 主买中单成交量 |
| bidSmallVolume | int | 主买小单成交量 |
| bidTotalVolume | int | 主买累计成交量 |
| offMostVolume | int | 主卖特大单成交量 |
| offBigVolume | int | 主卖大单成交量 |
| offMediumVolume | int | 主卖中单成交量 |
| offSmallVolume | int | 主卖小单成交量 |
| offTotalVolume | int | 主卖累计成交量 |
| unactiveBidMostVolume | int | 被动买特大单成交量 |
| unactiveBidBigVolume | int | 被动买大单成交量 |
| unactiveBidMediumVolume | int | 被动买中单成交量 |
| unactiveBidSmallVolume | int | 被动买小单成交量 |
| unactiveBidTotalVolume | int | 被动买累计成交量 |
| unactiveOffMostVolume | int | 被动卖特大单成交量 |
| unactiveOffBigVolume | int | 被动卖大单成交量 |
| unactiveOffMediumVolume | int | 被动卖中单成交量 |
| unactiveOffSmallVolume | int | 被动卖小单成交量 |
| unactiveOffTotalVolume | int | 被动卖累计成交量 |
| netInflowMostVolume | int | 净流入超大单成交量 |
| netInflowBigVolume | int | 净流入大单成交量 |
| netInflowMediumVolume | int | 净流入中单成交量 |
| netInflowSmallVolume | int | 净流入小单成交量 |
| bidMostAmountDx | float | 主买特大单成交额增量 |
| bidBigAmountDx | float | 主买大单成交额增量 |
| bidMediumAmountDx | float | 主买中单成交额增量 |
| bidSmallAmountDx | float | 主买小单成交额增量 |
| bidTotalAmountDx | float | 主买累计成交额增量 |
| offMostAmountDx | float | 主卖特大单成交额增量 |
| offBigAmountDx | float | 主卖大单成交额增量 |
| offMediumAmountDx | float | 主卖中单成交额增量 |
| offSmallAmountDx | float | 主卖小单成交额增量 |
| offTotalAmountDx | float | 主卖累计成交额增量 |
| unactiveBidMostAmountDx | float | 被动买特大单成交额增量 |
| unactiveBidBigAmountDx | float | 被动买大单成交额增量 |
| unactiveBidMediumAmountDx | float | 被动买中单成交额增量 |
| unactiveBidSmallAmountDx | float | 被动买小单成交额增量 |
| unactiveBidTotalAmountDx | float | 被动买累计成交额增量 |
| unactiveOffMostAmountDx | float | 被动卖特大单成交额增量 |
| unactiveOffBigAmountDx | float | 被动卖大单成交额增量 |
| unactiveOffMediumAmountDx | float | 被动卖中单成交额增量 |
| unactiveOffSmallAmountDx | float | 被动卖小单成交额增量 |
| unactiveOffTotalAmountDx | float | 被动卖累计成交额增量 |
| netInflowMostAmountDx | float | 净流入超大单成交额增量 |
| netInflowBigAmountDx | float | 净流入大单成交额增量 |
| netInflowMediumAmountDx | float | 净流入中单成交额增量 |
| netInflowSmallAmountDx | float | 净流入小单成交额增量 |
| bidMostVolumeDx | int | 主买特大单成交量增量 |
| bidBigVolumeDx | int | 主买大单成交量增量 |
| bidMediumVolumeDx | int | 主买中单成交量增量 |
| bidSmallVolumeDx | int | 主买小单成交量增量 |
| bidTotalVolumeDx | int | 主买累计成交量增量 |
| offMostVolumeDx | int | 主卖特大单成交量增量 |
| offBigVolumeDx | int | 主卖大单成交量增量 |
| offMediumVolumeDx | int | 主卖中单成交量增量 |
| offSmallVolumeDx | int | 主卖小单成交量增量 |
| offTotalVolumeDx | int | 主卖累计成交量增量 |
| unactiveBidMostVolumeDx | int | 被动买特大单成交量增量 |
| unactiveBidBigVolumeDx | int | 被动买大单成交量增量 |
| unactiveBidMediumVolumeDx | int | 被动买中单成交量增量 |
| unactiveBidSmallVolumeDx | int | 被动买小单成交量增量 |
| unactiveBidTotalVolumeDx | int | 被动买累计成交量增量 |
| unactiveOffMostVolumeDx | int | 被动卖特大单成交量增量 |
| unactiveOffBigVolumeDx | int | 被动卖大单成交量增量 |
| unactiveOffMediumVolumeDx | int | 被动卖中单成交量增量 |
| unactiveOffSmallVolumeDx | int | 被动卖小单成交量增量 |
| unactiveOffTotalVolumeDx | int | 被动卖累计成交量增量 |
| netInflowMostVolumeDx | int | 净流入超大单成交量增量 |
| netInflowBigVolumeDx | int | 净流入大单成交量增量 |
| netInflowMediumVolumeDx | int | 净流入中单成交量增量 |
| netInflowSmallVolumeDx | int | 净流入小单成交量增量 |

**返回**

返回一个 {`stock_code`:`pd.DataFrame`} 结构的`dict`对象，默认的列索引为取得的全部字段. 如果给定了 `fields` 参数, 则列索引与给定的 `fields` 对应.

**示例**

示例data1返回值data2返回值data3返回值

```
from xtquant import xtdata

# 获取历史数据前，请确保已经下载历史数据
xtdata.download_history_data("000001.SZ",period="transactioncount1d")
xtdata.download_history_data("000582.SZ",period="transactioncount1d")

# 获取一只股票在一个时间段内的资金流量数据
data1 = xtdata.get_market_data_ex([],["000001.SZ"],period="transactioncount1d",start_time = "20230101", end_time = "20230109")

# 获取多只股票在一个时间段内的资金流向数据
data2 = xtdata.get_market_data_ex([],["000001.SZ","000582.SZ"],period="transactioncount1d",start_time = "20230101", end_time = "20231009")
# 获取多只股票在某一天的资金流向数据
data3 = xtdata.get_market_data_ex([],["000001.SZ","000582.SZ"],period="transactioncount1d",start_time = "20231009", end_time = "20231009")
```

```
{'000001.SZ':                          time  bidNumber  bidMostVolume  bidBigVolume
 20230919000000  1695052800000        984          69117         44872
 20230921000000  1695225600000        895         108902         83679
 20230925000000  1695571200000       1623         231467         74114
 20230926000000  1695657600000       2062          67169         55677
 20230927000000  1695744000000       2009          58878         62465

                 bidMediumVolume  bidSmallVolume  offNumber  offMostVolume
 20230919000000            26438            6501       1967          85488
 20230921000000            35465            3924        983         229549
 20230925000000            43191           10924       2505         187342
 20230926000000            51364           17352       2249         116657
 20230927000000            56459           14777       1309          81739

                 offBigVolume  offMediumVolume  ...  unactiveOffMediumVolume
 20230919000000         59203            59738  ...                    26438
 20230921000000         86736            32368  ...                    35465
 20230925000000        122762            72830  ...                    43191
 20230926000000         60107            56529  ...                    51364
 20230927000000         45153            35564  ...                    56459

                 unactiveOffSmallVolume  unactiveBidMostAmount
 20230919000000                    6501             95675555.0
 20230921000000                    3924            254330642.0
 20230925000000                   10924            210680989.0
 20230926000000                   17352            130480050.0
 20230927000000                   14777             91271341.0

                 unactiveBidBigAmount  unactiveBidMediumAmount
 20230919000000            66298552.0               66894672.0
 20230921000000            96037439.0               35829510.0
 20230925000000           138055328.0               81832159.0
 20230926000000            67243196.0               63224375.0
 20230927000000            50446231.0               39734344.0

                 unactiveBidSmallAmount  unactiveOffMostAmount
 20230919000000              15027131.0             77417455.0
 20230921000000               6162863.0            120659362.0
 20230925000000              20874412.0            260444433.0
 20230926000000              22504832.0             75270646.0
 20230927000000               9942591.0             65804316.0

                 unactiveOffBigAmount  unactiveOffMediumAmount
 20230919000000            50235300.0               29606244.0
 20230921000000            92703643.0               39276977.0
 20230925000000            83333817.0               48529084.0
 20230926000000            62328071.0               57432804.0
 20230927000000            69814571.0               63092343.0

                 unactiveOffSmallAmount
 20230919000000               7278898.0
 20230921000000               4345184.0
 20230925000000              12272276.0
 20230926000000              19401833.0
 20230927000000              16510431.0

 [5 rows x 47 columns]}
```

```
{'000001.SZ':                          time  bidNumber  bidMostVolume  bidBigVolume
 20230919000000  1695052800000        984          69117         44872
 20230921000000  1695225600000        895         108902         83679
 20230925000000  1695571200000       1623         231467         74114
 20230926000000  1695657600000       2062          67169         55677
 20230927000000  1695744000000       2009          58878         62465

                 bidMediumVolume  bidSmallVolume  offNumber  offMostVolume
 20230919000000            26438            6501       1967          85488
 20230921000000            35465            3924        983         229549
 20230925000000            43191           10924       2505         187342
 20230926000000            51364           17352       2249         116657
 20230927000000            56459           14777       1309          81739

                 offBigVolume  offMediumVolume  ...  unactiveOffMediumVolume
 20230919000000         59203            59738  ...                    26438
 20230921000000         86736            32368  ...                    35465
 20230925000000        122762            72830  ...                    43191
 20230926000000         60107            56529  ...                    51364
 20230927000000         45153            35564  ...                    56459

                 unactiveOffSmallVolume  unactiveBidMostAmount
 20230919000000                    6501             95675555.0
 20230921000000                    3924            254330642.0
 20230925000000                   10924            210680989.0
 20230926000000                   17352            130480050.0
 20230927000000                   14777             91271341.0

                 unactiveBidBigAmount  unactiveBidMediumAmount
 20230919000000            66298552.0               66894672.0
 20230921000000            96037439.0               35829510.0
 20230925000000           138055328.0               81832159.0
 20230926000000            67243196.0               63224375.0
 20230927000000            50446231.0               39734344.0

                 unactiveBidSmallAmount  unactiveOffMostAmount
 20230919000000              15027131.0             77417455.0
 20230921000000               6162863.0            120659362.0
 20230925000000              20874412.0            260444433.0
 20230926000000              22504832.0             75270646.0
 20230927000000               9942591.0             65804316.0

                 unactiveOffBigAmount  unactiveOffMediumAmount
 20230919000000            50235300.0               29606244.0
 20230921000000            92703643.0               39276977.0
 20230925000000            83333817.0               48529084.0
 20230926000000            62328071.0               57432804.0
 20230927000000            69814571.0               63092343.0

                 unactiveOffSmallAmount
 20230919000000               7278898.0
 20230921000000               4345184.0
 20230925000000              12272276.0
 20230926000000              19401833.0
 20230927000000              16510431.0

 [5 rows x 47 columns],
 '000582.SZ':                          time  bidNumber  bidMostVolume  bidBigVolume
 20231009000000  1696780800000       1235           1822          7834

                 bidMediumVolume  bidSmallVolume  offNumber  offMostVolume
 20231009000000            13594           11220       1158              0

                 offBigVolume  offMediumVolume  ...  unactiveOffMediumVolume
 20231009000000         13378            19074  ...                    13594

                 unactiveOffSmallVolume  unactiveBidMostAmount
 20231009000000                   11220                    0.0

                 unactiveBidBigAmount  unactiveBidMediumAmount
 20231009000000            10446929.0               14883956.0

                 unactiveBidSmallAmount  unactiveOffMostAmount
 20231009000000               9972652.0              1419544.0

                 unactiveOffBigAmount  unactiveOffMediumAmount
 20231009000000             6119272.0               10617787.0

                 unactiveOffSmallAmount
 20231009000000               8753931.0

 [1 rows x 47 columns]}
```

```
{'000582.SZ':                          time  bidNumber  bidMostVolume  bidBigVolume
 20231009000000  1696780800000       1235           1822          7834

                 bidMediumVolume  bidSmallVolume  offNumber  offMostVolume
 20231009000000            13594           11220       1158              0

                 offBigVolume  offMediumVolume  ...  unactiveOffMediumVolume
 20231009000000         13378            19074  ...                    13594

                 unactiveOffSmallVolume  unactiveBidMostAmount
 20231009000000                   11220                    0.0

                 unactiveBidBigAmount  unactiveBidMediumAmount
 20231009000000            10446929.0               14883956.0

                 unactiveBidSmallAmount  unactiveOffMostAmount
 20231009000000               9972652.0              1419544.0

                 unactiveOffBigAmount  unactiveOffMediumAmount
 20231009000000             6119272.0               10617787.0

                 unactiveOffSmallAmount
 20231009000000               8753931.0

 [1 rows x 47 columns],
 '000001.SZ':                          time  bidNumber  bidMostVolume  bidBigVolume
 20231009000000  1696780800000       1720         124493         91717

                 bidMediumVolume  bidSmallVolume  offNumber  offMostVolume
 20231009000000            52939           12295       2691         193122

                 offBigVolume  offMediumVolume  ...  unactiveOffMediumVolume
 20231009000000        120549            79591  ...                    52939

                 unactiveOffSmallVolume  unactiveBidMostAmount
 20231009000000                   12295            214620203.0

                 unactiveBidBigAmount  unactiveBidMediumAmount
 20231009000000           133821821.0               88366888.0

                 unactiveBidSmallAmount  unactiveOffMostAmount
 20231009000000              23450520.0            138450770.0

                 unactiveOffBigAmount  unactiveOffMediumAmount
 20231009000000           101823002.0               58774037.0

                 unactiveOffSmallAmount
 20231009000000              13652109.0

 [1 rows x 47 columns]}
```

## 获取股票订单流数据

获取股票在某个价位的订单数量

提示

1.该数据通过`get_market_data`和`get_market_data_ex`接口获取，period参数选择`orderflow1m` 或者 `orderflow1d`

2.获取历史数据前需要先用`download_history_data`下载历史数据，订单流数据仅提供`orderflow1m`周期数据下载，其他周期的订单流数据都是通过1m周期合成的

3. [订单流版 权限数据](https://xuntou.net/#/productvip)

### 内置python

**原型**

python

```

# 一分钟订单流
C.get_market_data_ex([],stock_list,period="orderflow1m",start_time = "", end_time = "")
# 1d订单流
C.get_market_data_ex([],stock_list,period="orderflow1d",start_time = "", end_time = "")
```

**参数** 除period参数需指定为`orderflow1m` 或者 `orderflow1d`外，其余参数与 [ContextInfo.get_market_data_ex](data_function.md#contextinfo-get-market-data-ex-%E8%8E%B7%E5%8F%96%E8%A1%8C%E6%83%85%E6%95%B0%E6%8D%AE) 一致

**返回值**

- 返回dict { stock_code1 : value1, stock_code2 : value2, ... }
- value1, value2, ... ：pd.DataFrame 数据集，index为time_list，columns为fields

**示例**

python返回值

```

# coding:gbk
def init(C):
    return

def f(data):
    print(data)

def after_init(C):
    stock_list = ["000001.SZ"]
    if 1:
        download_history_data("000001.SZ","orderflow1m",'','')


    C.subscribe_quote("000001.SZ","orderflow1m",callback = f)
    # C.subscribe_quote("000001.SZ","transactioncount1d")
    print(C.get_market_data_ex([],stock_list,period="orderflow1m",start_time = "", end_time = "",count = 1))
```

```

start simulation mode
{'000001.SZ':                     buyNum          price sellNum           stime
stime
20240315150000  [0, 82724]  [10.58, 10.6]  [0, 0]  20240315150000

                         time
stime
20240315150000  1710486000000  }
buyNum         [0, 82724]
price       [10.58, 10.6]
sellNum            [0, 0]
stime      20240315150000
time        1710486000000
Name: 20240315150000, dtype: object
```

### 原生pytrhon

python

```
from xtquant import xtdata
# 订单流数据仅提供1m周期数据下载，其他周期的订单流数据都是通过1m周期合成的
period = "orderflow1m"
# 下载000001.SZ的1m订单流数据
xtdata.download_history_data("000001.SZ",period=period)
# 获取000001.SZ的1m订单流数据
xtdata.get_market_data_ex([],["000001.SZ"],period=period)["000001.SZ"]
```

**参数**

| 名称 | 类型 | 描述 |
| --- | --- | --- |
| `field` | `list` | `数据字段，详情见下方field字段表` |
| `stock_list` | `list` | `合约代码列表` |
| `period` | `str` | `订单流数据周期——orderflow1m, orderflow5m, orderflow15m, orderflow30m, orderflow1h, orderflow1d` |
| `start_time` | `str` | `数据起始时间，格式为 %Y%m%d 或 %Y%m%d%H%M%S，填""为获取历史最早一天` |
| `end_time` | `str` | `数据结束时间，格式为 %Y%m%d 或 %Y%m%d%H%M%S ，填""为截止到最新一天` |
| `count` | `int` | `数据个数` |
| `dividend_type` | `str` | `除权方式` |
| `fill_data` | `bool` | `是否填充数据` |

- `field`字段可选：

| field | 数据类型 | 含义 |
| --- | --- | --- |
| `time` | `str` | `时间` |
| `price` | `str` | `价格段` |
| `buyNum` | `str` | `各价格对应的买方订单量` |
| `sellNum` | `str` | `各价格对应的卖方订单量` |

- `period`字段可选:

| period | 数据类型 | 含义 |
| --- | --- | --- |
| `orderflow1m` | `str` | `1m周期订单流数据` |
| `orderflow5m` | `str` | `5m周期订单流数据` |
| `orderflow15m` | `str` | `15m周期订单流数据` |
| `orderflow30m` | `str` | `30m周期订单流数据` |
| `orderflow1h` | `str` | `1h周期订单流数据` |
| `orderflow1d` | `str` | `1d周期订单流数据` |

**返回值** 返回一个 {`stock_code`:`pd.DataFrame`} 结构的`dict`对象，默认的列索引为取得的全部字段. 如果给定了 `fields` 参数, 则列索引与给定的 `fields` 对应.

**示例**

示例data1返回值data2返回值data3返回值data4返回值

```
# 下载000001.SZ的orderflow1m，以获取历史数据
# orderflow仅提供1m周期进行下载，其他周期皆在系统底层通过1m订单流数据进行合成给出
xtdata.download_history_data("000001.SZ",period="orderflow1m")

# 获取000001.SZ，1m订单流数据
period = "orderflow1m"
data1 = xtdata.get_market_data_ex([],["000001.SZ"],period=period)["000001.SZ"]

# 获取000001.SZ, 5m订单流数据
period = "orderflow5m"
data2 = xtdata.get_market_data_ex([],["000001.SZ"],period=period)["000001.SZ"]

# 获取000001.SZ 1d订单流数据
period = "orderflow1d"
data3 = xtdata.get_market_data_ex([],["000001.SZ"],period=period)["000001.SZ"]

# 订阅实时000001.SZ 1m订单流数据
period = "orderflow1m"

# 进行数据订阅
xtdata.subscribe_quote("000001.SZ", period = period)
# 获取订阅后的实时数据
data4 = xtdata.get_market_data_ex([],["000001.SZ"],period=period)["000001.SZ"]

print(data1)
print(data2)
print(data3)

print(data4)
```

```
	time	price	buyNum	sellNum
20230324093000	1679621400000	[12.85]	[4230]	[0]
20230324093100	1679621460000	[12.790000000000001, 12.8, 12.81, 12.82, 12.83...	[888, 453, 769, 2536, 0, 1854, 1722]	[837, 3372, 1525, 6121, 575, 3324, 0]
20230324093200	1679621520000	[12.77, 12.780000000000001, 12.790000000000001...	[0, 3267, 5211, 318]	[1843, 1505, 3051, 197]
20230324093300	1679621580000	[12.780000000000001, 12.790000000000001, 12.8]	[0, 5552, 107]	[3990, 1539, 0]
20230324093400	1679621640000	[12.8, 12.81]	[889, 1728]	[852, 1611]
...	...	...	...	...
20231026134900	1698299340000	[10.36, 10.370000000000001, 10.38]	[0, 255, 353]	[15, 140, 0]
20231026135000	1698299400000	[10.370000000000001, 10.38]	[0, 596]	[3106, 0]
20231026135100	1698299460000	[10.370000000000001, 10.38]	[0, 608]	[175, 0]
20231026135200	1698299520000	[10.370000000000001, 10.38]	[0, 944]	[667, 0]
20231026135300	1698299580000	[10.370000000000001, 10.38]	[0, 160]	[106, 0]
34396 rows × 4 columns
```

```
	time	price	buyNum	sellNum
20230324093500	1679621700000	[12.77, 12.780000000000001, 12.790000000000001...	[0, 3267, 11651, 1767, 4135, 3092, 0, 1854, 5952]	[1843, 5495, 5427, 4580, 4744, 6121, 575, 3324...
20230324094000	1679622000000	[12.81, 12.82, 12.83, 12.84, 12.85, 12.86]	[3515, 603, 4610, 5587, 3346, 158]	[3358, 2884, 4953, 1099, 61, 0]
20230324094500	1679622300000	[12.790000000000001, 12.8, 12.81, 12.82, 12.83...	[0, 322, 3573, 526, 604, 935, 1270]	[964, 11150, 2242, 4940, 1407, 517, 0]
20230324095000	1679622600000	[12.77, 12.780000000000001, 12.790000000000001...	[935, 11904, 119, 754, 2892]	[6065, 6067, 4771, 5898, 0]
20230324095500	1679622900000	[12.780000000000001, 12.790000000000001, 12.8,...	[300, 1229, 6217, 197]	[739, 4098, 858, 0]
...	...	...	...	...
20231026110500	1698289500000	[10.32, 10.33, 10.34]	[0, 1318, 264]	[3, 9260, 0]
20231026111000	1698289800000	[10.33, 10.34]	[0, 1880]	[4062, 0]
20231026111500	1698290100000	[10.33, 10.34]	[0, 1965]	[1729, 0]
20231026112000	1698290400000	[10.33, 10.34, 10.35, 10.36]	[0, 1414, 5373, 257]	[1309, 2367, 775, 0]
20231026112500	1698290700000	[10.33, 10.34, 10.35]	[0, 1077, 258]	[487, 499, 0]
6839 rows × 4 columns
```

```
	time	price	buyNum	sellNum
20230324000000	1679587200000	[12.77, 12.780000000000001, 12.790000000000001...	[935, 17170, 22882, 27895, 62600, 53273, 39324...	[8938, 27896, 31737, 80764, 68784, 68695, 2731...
20230327000000	1679846400000	[12.47, 12.48, 12.49, 12.5, 12.51, 12.52, 12.5...	[0, 8792, 4885, 4997, 50228, 57248, 31828, 348...	[915, 24135, 25945, 30326, 82575, 40025, 32308...
20230328000000	1679932800000	[12.55, 12.56, 12.57, 12.58, 12.59, 12.6, 12.6...	[0, 2411, 2096, 8403, 17269, 13652, 30554, 201...	[2002, 5320, 11049, 10937, 16325, 26177, 26658...
20230329000000	1680019200000	[12.52, 12.530000000000001, 12.540000000000001...	[0, 5689, 49134, 29969, 16598, 15290, 23969, 1...	[16122, 54360, 33434, 13624, 30877, 22648, 264...
20230330000000	1680105600000	[12.41, 12.42, 12.43, 12.44, 12.45000000000000...	[0, 19093, 24669, 16814, 9488, 7165, 9891, 109...	[7093, 37216, 34430, 13969, 12035, 11947, 1369...
...	...	...	...	...
20231020000000	1697731200000	[10.52, 10.53, 10.540000000000001, 10.55, 10.5...	[419, 13251, 17713, 12059, 6547, 14152, 17650,...	[5527, 2180, 5684, 4222, 8746, 20424, 22532, 4...
20231023000000	1697990400000	[10.43, 10.44, 10.450000000000001, 10.46, 10.4...	[0, 11496, 18358, 23063, 24492, 14307, 7609, 2...	[11067, 15592, 21853, 16322, 26661, 14717, 256...
20231024000000	1698076800000	[10.44, 10.450000000000001, 10.46, 10.47, 10.4...	[0, 7838, 11767, 11598, 10783, 8160, 7532, 223...	[6030, 15551, 17457, 7944, 12948, 3154, 17360,...
20231025000000	1698163200000	[10.36, 10.370000000000001, 10.38, 10.39, 10.4...	[0, 30043, 48101, 93420, 77355, 58783, 34336, ...	[15876, 59255, 135796, 82676, 96175, 51600, 32...
20231026000000	1698249600000	[10.31, 10.32, 10.33, 10.34, 10.35, 10.36, 10....	[2314, 3430, 13070, 30194, 45518, 29091, 40124...	[16564, 3579, 42438, 42624, 26508, 26492, 1297...
143 rows × 4 columns
```

```
	time	price	buyNum	sellNum
20230324093000	1679621400000	[12.85]	[4230]	[0]
20230324093100	1679621460000	[12.790000000000001, 12.8, 12.81, 12.82, 12.83...	[888, 453, 769, 2536, 0, 1854, 1722]	[837, 3372, 1525, 6121, 575, 3324, 0]
20230324093200	1679621520000	[12.77, 12.780000000000001, 12.790000000000001...	[0, 3267, 5211, 318]	[1843, 1505, 3051, 197]
20230324093300	1679621580000	[12.780000000000001, 12.790000000000001, 12.8]	[0, 5552, 107]	[3990, 1539, 0]
20230324093400	1679621640000	[12.8, 12.81]	[889, 1728]	[852, 1611]
...	...	...	...	...
20231026134100	1698298860000	[10.36, 10.370000000000001]	[0, 11]	[44, 0]
20231026134200	1698298920000	[10.36, 10.370000000000001]	[0, 206]	[86, 0]
20231026134300	1698298980000	[10.36, 10.370000000000001]	[0, 0]	[78, 0]
20231026134400	1698299040000	[10.36, 10.370000000000001]	[0, 33]	[291, 0]
20231026134500	1698299100000	[10.36]	[0]	[14]
```

## 获取问董秘数据

提示

1.该数据通过`get_market_data_ex`接口获取,周期需填写为 **`interactiveqa`**

2.获取数据前需要先用`download_history_data`下载历史数据

3. [VIP 权限数据](https://xuntou.net/#/productvip)

### 原生python

python

```
from xtquant import xtdata
xtdata.get_market_data_ex(field_list,stock_list,period='interactiveqa')
```

**参数**

除period 需填写为`interactiveqa`外，其余参数参考`get_market_data_ex`

**返回值**

返回一个 {`stock_code`:`pd.DataFrame`} 结构的`dict`对象

**示例**

示例返回值

```

from xtquant import xtdata
xtdata.download_history_data("000001.SZ",period="interactiveqa")
data = xtdata.get_market_data_ex([],["000001.SZ"],period="interactiveqa")
print(data)
```

```
{'000001.SZ':              time                 问答编号           问题时间
 0   1688572800000  1477967097550430208  1686794016000
 1   1688572800001  1481018439885479936  1687149238000
 2   1688572800002  1486238955455750144  1687756986000
 3   1688572800003  1492863495831379968  1688528184000
 4   1688572800004  1480984724391051264  1687145313000
 ..            ...                  ...            ...
 87  1700150400004  1587992657604898816  1699602677000
 88  1700150400005  1588473238651199488  1699658624000
 89  1700150400006  1589974656269893632  1699833412000
 90  1700150400007  1591562814916870144  1700018297000
 91  1700150400008  1592406612781776897  1700116529000

                                                  问题内容           回答时间
 0                                   公司认为经营银行的长期主义是什么？  1688605558000
 1                                        请问现在的股东人数是多少  1688605821000
 2                             贵公司分红率为什么这么低，是否可以加大分红比率  1688606076000
 3                  建议平安私有化平安银行，这样的估值没有必要留在资本市场，平安也受益。  1688606100000
 4                            公司手续费佣金收入年年下降，有没有什么办法改善？  1688606510000
 ..                                                ...            ...
 87  贵公司的营业收入增速已经开始负增长，行业进入增长停滞的状态，行业逐步趋向成熟。为什么分红率相...  1700187933000
 88  前两年买了一点公司股票，后来看董秘说要珍惜十四元的平安银行，现重仓贵司亏损重大！公司的分红率...  1700187940000
 89  你好:公司股价长期低于每股未分配利润11.2463元（2023三季报）,作为公司老股东小股东...  1700187948000
 90                               请问公司最近三年在外地的投资项目有哪些？  1700188768000
 91            董秘好！请问：银行资本新规，对平安银行资本充足率，会产生正面影响还是负面影响？  1700188844000

                                                  回答内容
 0   本行以“中国最卓越、全球领先的智能化零售银行”为战略目标，坚持“科技引领、零售突破、对公做精...
 1          您好，截至2023年一季度末，本行股东总户数为506,867户。感谢您对我行的关注。
 2   您好！本行于2021年4月8日召开的2020年年度股东大会审议通过了《平安银行股份有限公司2...
 3                                       感谢您对我行的关注和建议。
 4   2022年，本集团手续费及佣金净收入302.08亿元，主要受宏观环境等因素影响，未来，本行将...
 ..                                                ...
 87                                      您好，感谢您的建议与关注。
 88                                      您好，感谢您的建议与关注。
 89                                      您好，感谢您的建议与关注。
 90  您好，本行是一家全国性股份制商业银行。截至2023年9月末，本行共有109家分行（含香港分行...
 91  您好，截至2023年9月末，得益于净利润增长、资本精细化管理等因素，本行核心一级资本充足率、...

 [92 rows x 6 columns]}
```

## 获取交易日历

获取历史和未来日历数据

### 内置python

**调用方法**

```py
get_trading_calendar(market,start_time='',end_time='')
```

**参数**

| 参数名称 | 类型 | 描述 |
| --- | --- | --- |
| `market` | `str` | 市场，如 'SH' |
| `start_time` | `str` | 起始时间，如 '20170101' |
| `end_time` | `str` | 结束时间，如 '20180101' |

**返回值**

- list类型

**示例**

示例返回值

```
# coding:gbk
def init(C):
    return
def after_init(C):
    print(get_trading_calendar('SZ','20230103','20240103'))
```

```
['20230103', '20230104', '20230105', '20230106', '20230109', '20230110', '20230111', '20230112', '20230113', '20230116', '20230117', '20230118', '20230119', '20230120', '20230130', '20230131', '20230201', '20230202', '20230203', '20230206', '20230207', '20230208', '20230209', '20230210', '20230213', '20230214', '20230215', '20230216', '20230217', '20230220', '20230221', '20230222', '20230223', '20230224', '20230227', '20230228', '20230301', '20230302', '20230303', '20230306', '20230307', '20230308', '20230309', '20230310', '20230313', '20230314', '20230315', '20230316', '20230317', '20230320', '20230321', '20230322', '20230323', '20230324', '20230327', '20230328', '20230329', '20230330', '20230331', '20230403', '20230404', '20230406', '20230407', '20230410', '20230411', '20230412', '20230413', '20230414', '20230417', '20230418', '20230419', '20230420', '20230421', '20230424', '20230425', '20230426', '20230427', '20230428', '20230504', '20230505', '20230508', '20230509', '20230510', '20230511', '20230512', '20230515', '20230516', '20230517', '20230518', '20230519', '20230522', '20230523', '20230524', '20230525', '20230526', '20230529', '20230530', '20230531', '20230601', '20230602', '20230605', '20230606', '20230607', '20230608', '20230609', '20230612', '20230613', '20230614', '20230615', '20230616', '20230619', '20230620', '20230621', '20230626', '20230627', '20230628', '20230629', '20230630', '20230703', '20230704', '20230705', '20230706', '20230707', '20230710', '20230711', '20230712', '20230713', '20230714', '20230717', '20230718', '20230719', '20230720', '20230721', '20230724', '20230725', '20230726', '20230727', '20230728', '20230731', '20230801', '20230802', '20230803', '20230804', '20230807', '20230808', '20230809', '20230810', '20230811', '20230814', '20230815', '20230816', '20230817', '20230818', '20230821', '20230822', '20230823', '20230824', '20230825', '20230828', '20230829', '20230830', '20230831', '20230901', '20230904', '20230905', '20230906', '20230907', '20230908', '20230911', '20230912', '20230913', '20230914', '20230915', '20230918', '20230919', '20230920', '20230921', '20230922', '20230925', '20230926', '20230927', '20230928', '20231009', '20231010', '20231011', '20231012', '20231013', '20231016', '20231017', '20231018', '20231019', '20231020', '20231023', '20231024', '20231025', '20231026', '20231027', '20231030', '20231031', '20231101', '20231102', '20231103', '20231106', '20231107', '20231108', '20231109', '20231110', '20231113', '20231114', '20231115', '20231116', '20231117', '20231120', '20231121', '20231122', '20231123', '20231124', '20231127', '20231128', '20231129', '20231130', '20231201', '20231204', '20231205', '20231206', '20231207', '20231208', '20231211', '20231212', '20231213', '20231214', '20231215', '20231218', '20231219', '20231220', '20231221', '20231222', '20231225', '20231226', '20231227', '20231228', '20231229', '20240102', '20240103']
```

### 原生python

**调用方法**

原生python

```
# 下载交易日历数据
xtdata.download_holiday_data()
# 返回获取的交易日历
result = xtdata.get_trading_calendar(market, start_time , end_time )
```

**参数**

| 参数名称 | 类型 | 描述 |
| --- | --- | --- |
| `market` | `str` | 市场，如 'SH' |
| `start_time` | `str` | 起始时间，如 '20170101' |
| `end_time` | `str` | 结束时间，如 '20180101' |

**返回值**

- list类型

**示例**

示例返回值

```py
# coding:utf-8
from xtquant import xtdata
import time

# 下载交易日历数据
xtdata.download_holiday_data()
# 获取交易日
start_time =  time.strftime("%Y%m%d") # 起始日期
end_time = time.strftime("%Y") + '1231' #结束日期,这里我用time函数自动计算年,格式生成'20241231'
# 返回获取的交易日历
result = xtdata.get_trading_calendar('SH', start_time , end_time )
print(result)
```

```
['20240109', '20240110', '20240111', '20240112', '20240115', '20240116', '20240117', '20240118', '20240119', '20240122', '20240123', '20240124', '20240125', '20240126', '20240129', '20240130', '20240131', '20240201', '20240202', '20240205', '20240206', '20240207', '20240208', '20240219', '20240220', '20240221', '20240222', '20240223', '20240226', '20240227', '20240228', '20240229', '20240301', '20240304', '20240305', '20240306', '20240307', '20240308', '20240311', '20240312', '20240313', '20240314', '20240315', '20240318', '20240319', '20240320', '20240321', '20240322', '20240325', '20240326', '20240327', '20240328', '20240329', '20240401', '20240402', '20240403', '20240408', '20240409', '20240410', '20240411', '20240412', '20240415', '20240416', '20240417', '20240418', '20240419', '20240422', '20240423', '20240424', '20240425', '20240426', '20240429', '20240430', '20240506', '20240507', '20240508', '20240509', '20240510', '20240513', '20240514', '20240515', '20240516', '20240517', '20240520', '20240521', '20240522', '20240523', '20240524', '20240527', '20240528', '20240529', '20240530', '20240531', '20240603', '20240604', '20240605', '20240606', '20240607', '20240611', '20240612', '20240613', '20240614', '20240617', '20240618', '20240619', '20240620', '20240621', '20240624', '20240625', '20240626', '20240627', '20240628', '20240701', '20240702', '20240703', '20240704', '20240705', '20240708', '20240709', '20240710', '20240711', '20240712', '20240715', '20240716', '20240717', '20240718', '20240719', '20240722', '20240723', '20240724', '20240725', '20240726', '20240729', '20240730', '20240731', '20240801', '20240802', '20240805', '20240806', '20240807', '20240808', '20240809', '20240812', '20240813', '20240814', '20240815', '20240816', '20240819', '20240820', '20240821', '20240822', '20240823', '20240826', '20240827', '20240828', '20240829', '20240830', '20240902', '20240903', '20240904', '20240905', '20240906', '20240909', '20240910', '20240911', '20240912', '20240913', '20240918', '20240919', '20240920', '20240923', '20240924', '20240925', '20240926', '20240927', '20240930', '20241008', '20241009', '20241010', '20241011', '20241014', '20241015', '20241016', '20241017', '20241018', '20241021', '20241022', '20241023', '20241024', '20241025', '20241028', '20241029', '20241030', '20241031', '20241101', '20241104', '20241105', '20241106', '20241107', '20241108', '20241111', '20241112', '20241113', '20241114', '20241115', '20241118', '20241119', '20241120', '20241121', '20241122', '20241125', '20241126', '20241127', '20241128', '20241129', '20241202', '20241203', '20241204', '20241205', '20241206', '20241209', '20241210', '20241211', '20241212', '20241213', '20241216', '20241217', '20241218', '20241219', '20241220', '20241223', '20241224', '20241225', '20241226', '20241227', '20241230', '20241231']
```

## 获取龙虎榜数据

获取指定日期区间内的龙虎榜数据

```py
C.get_longhubang(stock_list, startTime, endTime)
```

**参数**

| 参数名称 | 类型 | 描述 |
| --- | --- | --- |
| `stock_list` | `list` | 股票列表，如 ['600000.SH', '600036.SH'] |
| `startTime` | `str` | 起始时间，如 '20170101' |
| `endTime` | `str` | 结束时间，如 '20180101' |

**返回值**

- 格式为`pandas.DataFrame`:

| 参数名称 | 数据类型 | 描述 |
| --- | --- | --- |
| `reason` | `str` | 上榜原因 |
| `close` | `float` | 收盘价 |
| `spreadRate` | `float` | 涨跌幅 |
| `TurnoverVolune` | `float` | 成交量 |
| `Turnover_Amount` | `float` | 成交金额 |
| `buyTraderBooth` | `pandas.DataFrame` | 买方席位 |
| `sellTraderBooth` | `pandas.DataFrame` | 卖方席位 |

- `buyTraderBooth` 或 `sellTraderBooth` 包含字段：

| 参数名称 | 数据类型 | 描述 |
| --- | --- | --- |
| `traderName` | `str` | 交易营业部名称 |
| `buyAmount` | `float` | 买入金额 |
| `buyPercent` | `float` | 买入金额占总成交占比 |
| `sellAmount` | `float` | 卖出金额 |
| `sellPercent` | `float` | 卖出金额占总成交占比 |
| `totalAmount` | `float` | 该席位总成交金额 |
| `rank` | `int` | 席位排行 |
| `direction` | `int` | 买卖方向 |

**示例**

示例返回值

```
# coding:gbk

def init(C):
    return

def handlebar(C):
    print(C.get_longhubang(['000002.SZ'],'20100101','20180101'))
```

```
 stockCode stockName                 date                  reason
0   000002.SZ       万科Ａ  2010-12-21 00:00:00        日价格涨幅偏离值达7%以上的证券
1   000002.SZ       万科Ａ  2013-01-21 00:00:00        日价格涨幅偏离值达7%以上的证券
2   000002.SZ       万科Ａ  2013-06-28 00:00:00        日价格涨幅偏离值达7%以上的证券
3   000002.SZ       万科Ａ  2014-12-31 00:00:00        日价格涨幅偏离值达7%以上的证券
4   000002.SZ       万科Ａ  2015-12-01 00:00:00        日价格涨幅偏离值达7%以上的证券
5   000002.SZ       万科Ａ  2015-12-02 00:00:00  连续三个交易日内涨幅偏离值累计达20%的证券
6   000002.SZ       万科Ａ  2015-12-02 00:00:00        日价格涨幅偏离值达7%以上的证券
7   000002.SZ       万科Ａ  2015-12-09 00:00:00        日价格涨幅偏离值达7%以上的证券
8   000002.SZ       万科Ａ  2015-12-17 00:00:00        日价格涨幅偏离值达7%以上的证券
9   000002.SZ       万科Ａ  2015-12-18 00:00:00        日价格涨幅偏离值达7%以上的证券
10  000002.SZ       万科Ａ  2016-07-04 00:00:00        日价格跌幅偏离值达7%以上的证券
11  000002.SZ       万科Ａ  2016-07-05 00:00:00        日价格跌幅偏离值达7%以上的证券
12  000002.SZ       万科Ａ  2016-07-05 00:00:00  连续三个交易日内跌幅偏离值累计达20%的证券
13  000002.SZ       万科Ａ  2016-08-04 00:00:00        日价格涨幅偏离值达7%以上的证券
14  000002.SZ       万科Ａ  2016-08-12 00:00:00        日价格涨幅偏离值达7%以上的证券
15  000002.SZ       万科Ａ  2016-08-15 00:00:00        日价格涨幅偏离值达7%以上的证券
16  000002.SZ       万科Ａ  2016-08-16 00:00:00  连续三个交易日内涨幅偏离值累计达20%的证券
17  000002.SZ       万科Ａ  2016-08-16 00:00:00        日价格涨幅偏离值达7%以上的证券
18  000002.SZ       万科Ａ  2016-08-31 00:00:00        日价格涨幅偏离值达7%以上的证券
19  000002.SZ       万科Ａ  2016-11-09 00:00:00        日价格涨幅偏离值达7%以上的证券
20  000002.SZ       万科Ａ  2017-01-13 00:00:00        日价格涨幅偏离值达7%以上的证券
21  000002.SZ       万科Ａ  2017-06-23 00:00:00        日价格涨幅偏离值达7%以上的证券
22  000002.SZ       万科Ａ  2017-06-26 00:00:00  连续三个交易日内涨幅偏离值累计达20%的证券
23  000002.SZ       万科Ａ  2017-06-26 00:00:00        日价格涨幅偏离值达7%以上的证券
24  000002.SZ       万科Ａ  2017-09-07 00:00:00        日价格涨幅偏离值达7%以上的证券
25  000002.SZ       万科Ａ  2017-11-21 00:00:00        日价格涨幅偏离值达7%以上的证券
26  000002.SZ       万科Ａ  2021-02-25 00:00:00           日涨幅偏离值达到7%的证券
27  000002.SZ       万科Ａ  2022-11-11 00:00:00           日涨幅偏离值达到7%的证券
28  000002.SZ       万科Ａ  2022-11-29 00:00:00           日涨幅偏离值达到7%的证券

                 close           SpreadRate      TurnoverVolume
0   9.1300000000000008                   10  29708.793799999999
1   11.130000000000001   9.9800000000000004  2343.0893000000001
2   9.8499999999999996   8.3599999999999994  23490.928500000002
3                 13.9   9.9700000000000006  48995.445899999999
4   16.579999999999998                10.02  37501.637000000002
5   18.239999999999998                10.01  121600.59819999999
6   18.239999999999998                10.01  121600.59819999999
7   19.550000000000001                10.02          35985.1973
8   22.210000000000001                   10  25833.926500000001
9                24.43                   10  22389.840199999999
10  21.989999999999998  -9.9900000000000002              426.63
11  19.789999999999999                  -10  19905.759999999998
12  19.789999999999999                  -10  19905.759999999998
13  19.670000000000002                10.01  37134.658199999998
14  22.780000000000001                   10  37487.086199999998
15  25.059999999999999                10.01  32311.062999999998
16               27.57                10.02  33347.805800000002
17               27.57                10.02  33347.805800000002
18               24.93                10.02  23831.257399999999
19  26.300000000000001   8.5899999999999999  40171.613899999997
20  21.809999999999999   6.9100000000000001          10642.6641
21               24.07                10.01  12511.867700000001
22               26.48                10.01          17111.8298
23               26.48                10.01          17111.8298
24  25.969999999999999   9.1199999999999992          12745.6991
25  31.789999999999999                   10  10817.886200000001
26  32.990000000000002                   10  25954.038499999999
27               15.76   9.9800000000000004  29116.540400000002
28  18.829999999999998   9.9900000000000002  25456.029699999999
...
```

## 北向南向资金（沪港通，深港通和港股通）

### 北向南向资金交易日历

获取交易日列表

python

```
from xtquant import xtdata
xtdata.get_trading_dates(market, start_time='', end_time='', count=-1)
```

**参数：**

| 参数名称 | 类型 | 描述 |
| --- | --- | --- |
| `market` | `string` | 市场代码 |
| `start_time` | `string` | 起始时间 |
| `end_time` | `string` | 结束时间 |
| `count` | `int` | 数据个数 |

**返回**

- `list` 时间戳列表，[ date1, date2, ... ]

**示例**

示例返回值

```
from xtquant import xtdata

# 获取沪港通最近十五天交易日历
data1 = xtdata.get_trading_dates(market = "HGT", start_time='', end_time='', count=-1)[-15:]
```

```
[1695312000000,
 1695571200000,
 1695657600000,
 1695744000000,
 1695830400000,
 1696780800000,
 1696867200000,
 1696953600000,
 1697040000000,
 1697126400000,
 1697385600000,
 1697472000000,
 1697558400000,
 1697644800000,
 1697731200000]
```

### 获取对应周期的北向南向数据

提示

1. 该数据通过`get_market_data_ex`接口获取
2. 获取历史数据前需要先用`download_history_data`下载历史数据,可选字段为`"northfinancechange1m"`：一分钟周期北向数据,`"northfinancechange1d"`：日线周期北向数据
3. [VIP 权限数据](https://xuntou.net/#/productvip)

#### 方式1：内置python

获取对应周期的北向数据

```py
C.get_north_finance_change(period)
```

**参数：**

| 字段名 | 数据类型 | 描述 |
| --- | --- | --- |
| `period` | `str` | 数据周期 |

**返回结果：**

- 根据`period`返回一个`dict`，该字典的`key`值是北向数据的时间戳，其值仍然是一个`dict`，其值的`key`值是北向数据的字段类型，其值是对应字段的值。该字典数据`key`值有：

| 字段名 | 数据类型 | 描述 |
| --- | --- | --- |
| hgtNorthBuyMoney | int | HGT北向买入资金 |
| hgtNorthSellMoney | int | HGT北向卖出资金 |
| hgtSouthBuyMoney | int | HGT南向买入资金 |
| hgtSouthSellMoney | int | HGT南向卖出资金 |
| sgtNorthBuyMoney | int | SGT北向买入资金 |
| sgtNorthSellMoney | int | SGT北向卖出资金 |
| sgtSouthBuyMoney | int | SGT南向买入资金 |
| sgtSouthSellMoney | int | SGT南向卖出资金 |
| hgtNorthNetInFlow | int | HGT北向资金净流入 |
| hgtNorthBalanceByDay | int | HGT北向当日资金余额 |
| hgtSouthNetInFlow | int | HGT南向资金净流入 |
| hgtSouthBalanceByDay | int | HGT南向当日资金余额 |
| sgtNorthNetInFlow | int | SGT北向资金净流入 |
| sgtNorthBalanceByDay | int | SGT北向当日资金余额 |
| sgtSouthNetInFlow | int | SGT南向资金净流入 |
| sgtSouthBalanceByDay | int | SGT南向当日资金余额 |

**示例1 通过内置python获取：**

示例返回值

```
# coding = gbk
def init(C):
    return
# 获取市场北向数据
def handlebar(C):
    print(C.get_north_finance_change('1d'))
```

```
{1416153600000: {"hgtNorthBuyMoney": 120820000, "hgtNorthSellMoney": 0,
"hgtSouthBuyMoney": 1772000000, "hgtSouthSellMoney": 84000000,
"sgtNorthBuyMoney": 0, "sgtNorthSellMoney": 0, "sgtSouthBuyMoney": 0,
"sgtSouthSellMoney": 0, "hgtNorthNetInFlow": 13000000000, "hgtNorthBalanceByDay": 0,
"hgtSouthNetInFlow": 1768000000, "hgtSouthBalanceByDay": 8732000000,
"sgtNorthNetInFlow": 0, "sgtNorthBalanceByDay": 0, "sgtSouthNetInFlow": 0, "sgtSouthBalanceByDay": 0}}
```

#### 方式2：原生python

原生python

```
xtdata.get_market_data_ex(
    fields=[],
    stock_code=[],
    period='follow',
    start_time='',
    end_time='',
    count=-1,
    dividend_type='follow',
    fill_data=True,
    subscribe=True
    )
```

**参数**

| 名称 | 类型 | 描述 |
| --- | --- | --- |
| `field` | `list` | 取北向数据时填写为`[]`空列表即可 |
| `stock_list` | `list` | 合约代码列表 |
| `period` | `str` | `数据周期，可选字段为:`<br>`"northfinancechange1m"`：一分钟周期北向数据<br>`"northfinancechange1d"`：日线周期北向数据 |
| `start_time` | `str` | 数据起始时间，格式为 `%Y%m%d` 或 `%Y%m%d%H%M%S`，填`""`为获取历史最早一天 |
| `end_time` | `str` | 数据结束时间，格式为 `%Y%m%d` 或 `%Y%m%d%H%M%S` ，填`""`为截止到最新一天 |
| `count` | `int` | 数据个数 |
| `dividend_type` | `str` | 除权方式,可选值为<br>`'none'`：不复权<br>`'front'`:前复权<br>`'back'`:后复权 <br>`'front_ratio'`: 等比前复权<br>`'back_ratio'`: 等比后复权<br>取此数据时不生效 |
| `fill_data` | `bool` | 是否填充数据 |
| `subscribe` | `bool` | 订阅数据开关，默认为True，设置为False时不做数据订阅，只读取本地已有数据。 |

**返回值**

返回一个 `{stock_code:pd.DataFrame}` 结构的`dict`对象，

**示例2 通过原生python获取：**

示例返回值

```
# 该示例演示token获取数据方式
from xtquant import xtdatacenter as xtdc

import xtquant.xtdata as xtdata

xtdc.set_token('这里输入token')
xtdc.init()

s = 'FFFFFF.SGT' # 北向资金代码
period = 'northfinancechange1m' # 数据周期
if 1:
    print('download')
    xtdata.download_history_data(s, period, '20231101', '')
    print('done')

data = xtdata.get_market_data_ex([], [s], period, '', '')[s]
print(data)
```

```
	time	HGT北向买入资金	HGT北向卖出资金	HGT南向买入资金	HGT南向卖出资金	SGT北向买入资金	SGT北向卖出资金	SGT南向买入资金	SGT南向卖出资金	HGT北向资金净流入	HGT北向当日资金余额	HGT南向资金净流入	HGT南向当日资金余额	SGT北向资金净流入	SGT北向当日资金余额	SGT南向资金净流入	SGT南向当日资金余额
0	1679619600000	0	0	0	0	0	0	0	0	0	52000000000	56482000	41943518000	0	52000000000	38749800	41961250199
1	1679619660000	0	0	0	0	0	0	0	0	0	52000000000	79933000	41920067000	0	52000000000	47571600	41952428400
2	1679619720000	0	0	0	0	0	0	0	0	0	52000000000	104898100	41895101900	0	52000000000	66697000	41933303000
3	1679619780000	0	0	0	0	0	0	0	0	0	52000000000	112106000	41887894000	0	52000000000	80038500	41919961500
4	1679619840000	0	0	0	0	0	0	0	0	0	52000000000	120973900	41879026200	0	52000000000	110223100	41889776900
...	...	...	...	...	...	...	...	...	...	...	...	...	...	...	...	...	...
52802	1699517160000	25931289200	23761060600	7192241300	4497273400	31224095900	33457685500	6649753700	4381821900	3487650300	48512349700	3561839099	38438160900	-956425200	52956425199	2952439099	39047560900
52803	1699517220000	25931289200	23761060600	7192241300	4497273400	31224095900	33457685500	6649753700	4381821900	3487650300	48512349700	3573462800	38426537200	-956425200	52956425199	2953814300	39046185700
52804	1699517280000	25931289200	23761060600	7192241300	4497273400	31224095900	33457685500	6649753700	4381821900	3487650300	48512349700	3550669400	38449330600	-956425200	52956425199	2934226100	39065773900
52805	1699517340000	25931289200	23761060600	7257519800	4531832900	31224095900	33457685500	6717744000	4402893900	3487650300	48512349700	3550669400	38449330600	-956425200	52956425199	2934226100	39065773900
52806	1699517400000	25931289200	23761060600	7257519800	4531832900	31224095900	33457685500	6717744000	4402893900	3487650300	48512349700	3550669400	38449330600	-956425200	52956425199	2934226100	39065773900
52807 rows × 17 columns
```

### 沪深港通持股数据

提示

1. 该数据是VIP权限数据
2. [VIP 权限数据](https://xuntou.net/#/productvip)

获取指定品种的持股明细

```py
C.get_hkt_details(stockcode)
```

**参数：**

| 参数名称 | 数据类型 | 描述 |
| --- | --- | --- |
| `stockcode` | `string` | 必须是'stock.market'形式 |

**返回结果：**

- 根据`stockcode`返回一个`dict`，该字典的key值是北向持股明细数据的时间戳，其值仍然是一个`dict`，其值的`key`值是北向持股明细数据的字段类型，其值是对应字段的值，该字典数据`key`值有：

| 参数名称 | 数据类型/单位 | 描述 |
| --- | --- | --- |
| `stockCode` | `str` | 股票代码 |
| `ownSharesCompany` | `str` | 机构名称 |
| `ownSharesAmount` | `int` | 持股数量 |
| `ownSharesMarketValue` | `float` | 持股市值 |
| `ownSharesRatio` | `float` | 持股数量占比 |
| `ownSharesNetBuy` | `float` | 净买入金额（当日持股-前一日持股） |

**示例：**

示例返回值

```
# coding = gbk
def init(C):
    return
def handlebar(C):
    data = C.get_hkt_details('600000.SH')
    print(data)
```

```
{1696694400053: {"stockCode": "600000.SH", "ownSharesCompany": "香港中央结算有限公司",
"ownSharesAmount": 15, "ownSharesMarketValue": 106.50000000000001,
"ownSharesRatio": 0.0, "ownSharesNetBuy": 0.0}}
```

## 交易所公告数据

### 原生Python

提示

1. 获取该数据前需要先调用`xtdata.download_history_data`进行下载，period参数选择`"announcement"`

2. 该数据通过`get_market_data_ex`接口获取，period参数选择`"announcement"`

3. 该数据是 [VIP权限数据](https://xuntou.net/#/productvip)


**调用方法**

```
get_market_data_ex([],stock_list,period="announcement",start_time = "", end_time = "")
```

**参数**

| 参数名称 | 类型 | 描述 |
| --- | --- | --- |
| `field_list` | `list` | 数据字段列表，传空则为全部字段 |
| `stock_list` | `list` | 合约代码列表 |
| `period` | `string` | 周期 |
| `start_time` | `string` | 起始时间 |
| `end_time` | `string` | 结束时间 |
| `count` | `int` | 数据个数。默认参数，大于等于0时，若指定了 `start_time`，`end_time`，此时以 `end_time` 为基准向前取 `count` 条；若 `start_time`，`end_time` 缺省，默认取本地数据最新的 `count` 条数据；若 `start_time`，`end_time`，`count` 都缺省时，默认取本地全部数据 |

**返回值**

返回一个 {`stock_code`:`pd.DataFrame`} 结构的`dict`对象，默认的列索引为取得的全部字段. 如果给定了 `fields` 参数, 则列索引与给定的 `fields` 对应.

**示例**

原生python返回值

```
from xtquant import xtdata
xtdata.download_history_data('600050.SH','announcement')

data = xtdata.get_market_data_ex([], ['600050.SH'], 'announcement', '', '')

d=data['600050.SH']

print(d.tail())
```

```
time 证券                                       主题 摘要   格式
535  1720195215674               中国联合网络通信股份有限公司第八届董事会第二次会议决议公告     TXT
536  1720195215850                中国联合网络通信股份有限公司关于聘任公司高级副总裁的公告     TXT
537  1720713609694     北京市通商律师事务所关于中国联合网络通信股份有限公司差异化分红事宜之法律意见书     TXT
538  1720713609868             中国联合网络通信股份有限公司2023年年度末期现金红利实施公告     TXT
539  1721664010707                中国联合网络通信股份有限公司2024年6月份运营数据公告     TXT

                                                    内容  级别  类型 0-其他 1-财报类
535  http://static.sse.com.cn/disclosure/listedinfo...   0              0
536  http://static.sse.com.cn/disclosure/listedinfo...   0              0
537  http://static.sse.com.cn/disclosure/listedinfo...   0              0
538  http://static.sse.com.cn/disclosure/listedinfo...   0              0
539  http://static.sse.com.cn/disclosure/listedinfo...   0              0
```

## 获取单季度/年度财务数据

查询股票的 **市值数据、资产负债数据、现金流数据、利润数据、财务指标数据**. 详情通过 [财务数据列表](http://docs.thinktrader.net/vip/pages/36f5df/#%E8%8E%B7%E5%8F%96%E8%B4%A2%E5%8A%A1%E6%95%B0%E6%8D%AE) 查看! 可通过以下api进行查询 :

### 内置python

获取财务数据前，请先通过`界面端数据管理 - 财务数据`下载

![财务数据下载](https://dict.thinktrader.net/assets/%E5%86%85%E7%BD%AEAPI_%E4%B8%8B%E8%BD%BD%E8%B4%A2%E5%8A%A1%E6%95%B0%E6%8D%AE-61e927b9.png)

提示

财务数据接口通过读取下载本地的数据取数，使用前需要补充本地数据。除公告日期和报表截止日期为时间戳毫秒格式其他单位为元或 %，数据主要包括资产负债表(ASHAREBALANCESHEET)、利润表（ASHAREINCOME）、现金流量表（ASHARECASHFLOW）、股本表（CAPITALSTRUCTURE）的主要字段数据以及经过计算的主要财务指标数据（PERSHAREINDEX）。建议使用本文档对照表中的英文表名和迅投英文字段，表名不区分大小写。

#### ContextInfo.get_financial_data - 获取财务数据

财务数据接口有两种用法，入参和返回值不同，具体如下

##### 用法1，返回目标数据对象

**原型**

```py
ContextInfo.get_financial_data(fieldList, stockList, startDate, enDate, report_type = 'announce_time')
```

**释义**

获取财务数据，方法1

**参数**

| 字段名 | 类型 | 释义与用例 |
| --- | --- | --- |
| `fieldList` | `List（必须）` | `财报字段列表：['ASHAREBALANCESHEET.fix_assets', '利润表.净利润']` |
| `stockList` | `List（必须）` | `股票列表：['600000.SH', '000001.SZ']` |
| `startDate` | `Str（必须）` | `开始时间：'20171209'` |
| `endDate` | `Str（必须）` | `结束时间：'20171212'` |
| `report_type` | `Str（可选）` | `报表时间类型，可缺省，默认是按照数据的公告期为区分取数据，设置为 'report_time' 为按照报告期取数据，' announce_time' 为按照公告日期取数据` |

提示

选择按照公告期取数和按照报告期取数的区别：

若某公司当年 4 月 26 日发布上年度年报，如果选择按照公告期取数，则当年 4 月 26 日之后至下个财报发布日期之间的数据都是上年度年报的财务数据。

若选择按照报告期取数，则上年度第 4 季度（上年度 10 月 1 日 - 12 月 31 日）的数据就是上年度报告期的数据。

**返回值**

函数根据stockList代码列表,startDate,endDate时间范围，返回不同的的数据类型。如下：

| 代码数量 | 时间范围 | 返回类型 |
| --- | --- | --- |
| =1 | =1 | pandas.Series (index = 字段) |
| =1 | >1 | pandas.DataFrame (index = 时间, columns = 字段) |
| >1 | =1 | pandas.DataFrame (index = 代码, columns = 字段) |
| >1 | >1 | pandas.Panel (items = 代码, major_axis = 时间, minor_axis = 字段) |

**示例**

示例返回值

```
# coding:gbk
def init(C):
  pass

def handlebar(C):

  #取总股本和净利润
  fieldList = ['CAPITALSTRUCTURE.total_capital', '利润表.净利润']
  stockList = ["000001.SZ","000002.SZ","430017.BJ"]
  startDate = '20171209'
  endDate = '20231204'
  data = C.get_financial_data(fieldList, stockList, startDate, endDate, report_type = 'report_time')
  print(data)
```

```
<class 'pandas.core.panel.Panel'>
Dimensions: 3 (items) x 1453 (major_axis) x 2 (minor_axis)
Items axis: 000001.SZ to 430017.BJ
Major_axis axis: 20171211 to 20231204
Minor_axis axis: total_capital to 净利润
```

##### 用法2，返回目标数据单个值

**原型**

```py
ContextInfo.get_financial_data(tabname, colname, market, code, report_type = 'report_time', barpos)
```

与用法 1 可同时使用

**释义**

获取财务数据，方法2

**参数**

| 字段名 | 类型 | 释义与用例 |
| --- | --- | --- |
| `tabname` | `Str（必须）` | `表名：'ASHAREBALANCESHEET'` |
| `colname` | `Str（必须）` | `字段名：'fix_assets'` |
| `market` | `Str（必须）` | `市场：'SH'` |
| `code` | `Str（必须）` | `代码：'600000'` |
| `report_type` | `Str（可选）` | `报表时间类型，可缺省，默认是按照数据的公告期为区分取数据，设置为 'report_time' 为按照报告期取数据，' announce_time ' 为按照公告日期取数据` |
| `barpos` | `number` | `当前 bar 的索引` |

**返回值**

`float` ：所取字段的数值

**示例**

示例返回值

```
# coding:gbk
def init(C):
  pass

def handlebar(C):
  index = C.barpos
  data = C.get_financial_data('ASHAREBALANCESHEET', 'fix_assets', 'SH', '600000', index)
  print(data)
```

```
42758000000.0
```

#### ContextInfo.get_raw_financial_data - 获取原始财务数据

提示

取原始财务数据,与get_financial_data相比不填充每个交易日的数据

**原型**

```py
ContextInfo.get_raw_financial_data(fieldList,stockList,startDate,endDate,report_type='announce_time')
```

**释义**

取原始财务数据,与get_financial_data相比不填充每个交易日的数据

**参数**

| 字段名 | 类型 | 释义与用例 |
| --- | --- | --- |
| `fieldList` | `List（必须）` | 字段列表：例如 ['资产负债表.固定资产','利润表.净利润'] |
| `stockList` | `List（必须）` | 股票列表：例如['600000.SH','000001.SZ'] |
| `startDate` | `Str（必须）` | 开始时间：例如 '20171209' |
| `endDate` | `Str（必须）` | 结束时间：例如 '20171212' |
| `report_type` | `Str（可选）` | 时间类型，可缺省，默认是按照数据的公告期为区分取数据，设置为 'report_time' 为按照报告期取数据，可选值:'announce_time','report_time' |

**返回值**

函数根据stockList代码列表,startDate,endDate时间范围，返回不同的的数据类型。如下：

| 代码数量 | 时间范围 | 返回类型 |
| --- | --- | --- |
| =1 | =1 | pandas.Series (index = 字段) |
| =1 | >1 | pandas.DataFrame (index = 时间, columns = 字段) |
| >1 | =1 | pandas.DataFrame (index = 代码, columns = 字段) |
| >1 | >1 | pandas.Panel (items = 代码, major_axis = 时间, minor_axis = 字段) |

**示例**

示例返回值

```
#encoding:gbk
'''
获取财务数据
'''
import pandas as pd
import numpy as np
import talib

def to_zw(a):
	'''0.中文价格字符串'''
	import numpy as np
	try:
		header = '' if a > 0 else '-'
		if np.isnan(a):
			return '问题数据'
		if abs(a) < 1000:
			return header + str(int(a)) + "元"
		if abs(a) < 10000:
			return header + str(int(a))[0] + "千"
		if abs(a) < 100000000:
			return header + str(int(a))[:-4] + "万" + str(int(a))[-4] + '千'
		else:
			return header + str(int(a))[:-8] + "亿" + str(int(a))[-8:-4] + '万'
	except:
		print(f"问题数据{a}")
		return '问题数据'

def after_init(C):
	fieldList = ['ASHAREINCOME.net_profit_excl_min_int_inc','ASHAREINCOME.revenue'] # 字段表
	stockList = ['000001.SZ'] # 标的
	a=C.get_raw_financial_data(fieldList,stockList,'20150101','20300101',report_type = 'report_time') # 获取原始财务数据
	# print(a)
	for stock in a:
		for key in a[stock]:
			for t in a[stock][key]:
				print(key, timetag_to_datetime(int(t),'%Y%m%d'), to_zw(a[stock][key][t]))
			print('-' *22)
		print('-' *22)
```

```

ASHAREINCOME.net_profit_excl_min_int_inc 20150331 56亿2900万
ASHAREINCOME.net_profit_excl_min_int_inc 20150630 115亿8500万
ASHAREINCOME.net_profit_excl_min_int_inc 20150930 177亿4000万
ASHAREINCOME.net_profit_excl_min_int_inc 20151231 218亿6500万
ASHAREINCOME.net_profit_excl_min_int_inc 20160331 60亿8600万
ASHAREINCOME.net_profit_excl_min_int_inc 20160630 122亿9200万
ASHAREINCOME.net_profit_excl_min_int_inc 20160930 187亿1900万
ASHAREINCOME.net_profit_excl_min_int_inc 20161231 225亿9900万
ASHAREINCOME.net_profit_excl_min_int_inc 20170331 62亿1400万
ASHAREINCOME.net_profit_excl_min_int_inc 20170630 125亿5400万
ASHAREINCOME.net_profit_excl_min_int_inc 20170930 191亿5300万
ASHAREINCOME.net_profit_excl_min_int_inc 20171231 231亿8900万
ASHAREINCOME.net_profit_excl_min_int_inc 20180331 65亿9500万
ASHAREINCOME.net_profit_excl_min_int_inc 20180630 133亿7200万
ASHAREINCOME.net_profit_excl_min_int_inc 20180930 204亿5600万
ASHAREINCOME.net_profit_excl_min_int_inc 20181231 248亿1800万
ASHAREINCOME.net_profit_excl_min_int_inc 20190331 74亿4600万
ASHAREINCOME.net_profit_excl_min_int_inc 20190630 154亿0300万
ASHAREINCOME.net_profit_excl_min_int_inc 20190930 236亿2100万
ASHAREINCOME.net_profit_excl_min_int_inc 20191231 281亿9500万
ASHAREINCOME.net_profit_excl_min_int_inc 20200331 85亿4800万
ASHAREINCOME.net_profit_excl_min_int_inc 20200630 136亿7800万
ASHAREINCOME.net_profit_excl_min_int_inc 20200930 223亿9800万
ASHAREINCOME.net_profit_excl_min_int_inc 20201231 289亿2800万
ASHAREINCOME.net_profit_excl_min_int_inc 20210331 101亿3200万
ASHAREINCOME.net_profit_excl_min_int_inc 20210630 175亿8300万
ASHAREINCOME.net_profit_excl_min_int_inc 20210930 291亿3500万
ASHAREINCOME.net_profit_excl_min_int_inc 20211231 363亿3600万
ASHAREINCOME.net_profit_excl_min_int_inc 20220331 128亿5000万
ASHAREINCOME.net_profit_excl_min_int_inc 20220630 220亿8800万
ASHAREINCOME.net_profit_excl_min_int_inc 20220930 366亿5900万
ASHAREINCOME.net_profit_excl_min_int_inc 20221231 455亿1600万
ASHAREINCOME.net_profit_excl_min_int_inc 20230331 146亿0200万
ASHAREINCOME.net_profit_excl_min_int_inc 20230630 253亿8700万
ASHAREINCOME.net_profit_excl_min_int_inc 20230930 396亿3500万
----------------------
ASHAREINCOME.revenue 20150331 206亿7100万
ASHAREINCOME.revenue 20150630 465亿7500万
ASHAREINCOME.revenue 20150930 711亿5200万
ASHAREINCOME.revenue 20151231 961亿6300万
ASHAREINCOME.revenue 20160331 275亿3200万
ASHAREINCOME.revenue 20160630 547亿6900万
ASHAREINCOME.revenue 20160930 819亿6800万
ASHAREINCOME.revenue 20161231 1077亿1500万
ASHAREINCOME.revenue 20170331 277亿2600万
ASHAREINCOME.revenue 20170630 540亿6900万
ASHAREINCOME.revenue 20170930 798亿3200万
ASHAREINCOME.revenue 20171231 1057亿8600万
ASHAREINCOME.revenue 20180331 280亿2600万
ASHAREINCOME.revenue 20180630 572亿4100万
ASHAREINCOME.revenue 20180930 866亿6400万
ASHAREINCOME.revenue 20181231 1167亿1600万
ASHAREINCOME.revenue 20190331 324亿7600万
ASHAREINCOME.revenue 20190630 678亿2900万
ASHAREINCOME.revenue 20190930 1029亿5800万
ASHAREINCOME.revenue 20191231 1379亿5800万
ASHAREINCOME.revenue 20200331 379亿2600万
ASHAREINCOME.revenue 20200630 783亿2800万
ASHAREINCOME.revenue 20200930 1165亿6400万
ASHAREINCOME.revenue 20201231 1535亿4200万
ASHAREINCOME.revenue 20210331 417亿8800万
ASHAREINCOME.revenue 20210630 846亿8000万
ASHAREINCOME.revenue 20210930 1271亿9000万
ASHAREINCOME.revenue 20211231 1693亿8300万
ASHAREINCOME.revenue 20220331 462亿0700万
ASHAREINCOME.revenue 20220630 920亿2200万
ASHAREINCOME.revenue 20220930 1382亿6500万
ASHAREINCOME.revenue 20221231 1798亿9500万
ASHAREINCOME.revenue 20230331 450亿9800万
ASHAREINCOME.revenue 20230630 886亿1000万
ASHAREINCOME.revenue 20230930 1276亿3400万
----------------------
----------------------
```

### 原生python

python

```
from xtquant import xtdata
xtdata.get_financial_data(stock_list, table_list=[], start_time='', end_time='', report_type='report_time')
```

提示

选择按照公告期取数和按照报告期取数的区别：

若某公司当年 4 月 26 日发布上年度年报，如果选择按照公告期取数，则当年 4 月 26 日之后至下个财报发布日期之间的数据都是上年度年报的财务数据。

若选择按照报告期取数，则上年度第 4 季度（上年度 10 月 1 日 - 12 月 31 日）的数据就是上年度报告期的数据。

**参数**

| 参数名称 | 数据类型 | 描述 |
| --- | --- | --- |
| `stock_list` | `list` | 合约代码列表 |
| `table_list` | `list` | 财务数据表名称列表,可选：`Balance` #资产负债表；`Income` #利润表；`CashFlow` #现金流量表 |
| `start_time` | `string` | 起始时间 |
| `end_time` | `string` | 结束时间 |
| `report_type` | `string` | 报表筛选方式,可选：`report_time` #截止日期；`announce_time` #披露日期 |

**返回**

- `dict` 数据集 { stock1 : datas1, stock2 : data2, ... }
  - stock1, stock2, ... # 合约代码
  - datas1, datas2, ... # dict 数据集 { table1 : table_data1, table2 : table_data2, ... }

**示例**

示例返回值

```
from xtquant import xtdata
# 取数据前请确保已下载所需要的财务数据
xtdata.download_financial_data(["000001.SZ","600519.SH","430017.BJ"], table_list=["Balance","Income"])
xtdata.get_financial_data(["000001.SZ","600519.SH","430017.BJ"],["Balance","Income"])
```

```
{'000001.SZ': {'Balance':     m_timetag m_anntime  internal_shoule_recv  fixed_capital_clearance
  0    19901231  19910430                   NaN                      NaN
  1    19911231  19920430                   NaN                      NaN
  2    19921231  19930226                   NaN                      NaN
  3    19931231  19940329                   NaN                      NaN
  4    19940630  19940630                   NaN                -241835.0
  ..        ...       ...                   ...                      ...
  101  20220630  20220818                   NaN                      NaN
  102  20220930  20221025                   NaN                      NaN
  103  20221231  20230309                   NaN                      NaN
  104  20230331  20230425                   NaN                      NaN
  105  20230630  20230824                   NaN                      NaN
  ...
```

### 财务数据列表

#### 资产负债表

- 内置表名：ASHAREBALANCESHEET
- 原生表名：Balance

| 字段名 | 定义 |
| --- | --- |
| m_anntime | 披露日期 |
| m_timetag | 截止日期 |
| internal_shoule_recv | 内部应收款 |
| fixed_capital_clearance | 固定资产清理 |
| should_pay_money | 应付分保账款 |
| settlement_payment | 结算备付金 |
| receivable_premium | 应收保费 |
| accounts_receivable_reinsurance | 应收分保账款 |
| reinsurance_contract_reserve | 应收分保合同准备金 |
| dividends_payable | 应收股利 |
| tax_rebate_for_export | 应收出口退税 |
| subsidies_receivable | 应收补贴款 |
| deposit_receivable | 应收保证金 |
| apportioned_cost | 待摊费用 |
| profit_and_current_assets_with_deal | 待处理流动资产损益 |
| current_assets_one_year | 一年内到期的非流动资产 |
| long_term_receivables | 长期应收款 |
| other_long_term_investments | 其他长期投资 |
| original_value_of_fixed_assets | 固定资产原值 |
| net_value_of_fixed_assets | 固定资产净值 |
| depreciation_reserves_of_fixed_assets | 固定资产减值准备 |
| productive_biological_assets | 生产性生物资产 |
| public_welfare_biological_assets | 公益性生物资产 |
| oil_and_gas_assets | 油气资产 |
| development_expenditure | 开发支出 |
| right_of_split_share_distribution | 股权分置流通权 |
| other_non_mobile_assets | 其他非流动资产 |
| handling_fee_and_commission | 应付手续费及佣金 |
| other_payables | 其他应交款 |
| margin_payable | 应付保证金 |
| internal_accounts_payable | 内部应付款 |
| advance_cost | 预提费用 |
| insurance_contract_reserve | 保险合同准备金 |
| broker_buying_and_selling_securities | 代理买卖证券款 |
| acting_underwriting_securities | 代理承销证券款 |
| international_ticket_settlement | 国际票证结算 |
| domestic_ticket_settlement | 国内票证结算 |
| deferred_income | 递延收益 |
| short_term_bonds_payable | 应付短期债券 |
| long_term_deferred_income | 长期递延收益 |
| undetermined_investment_losses | 未确定的投资损失 |
| quasi_distribution_of_cash_dividends | 拟分配现金股利 |
| provisions_not | 预计负债 |
| cust_bank_dep | 吸收存款及同业存放 |
| provisions | 预计流动负债 |
| less_tsy_stk | 减:库存股 |
| cash_equivalents | 货币资金 |
| loans_to_oth_banks | 拆出资金 |
| tradable_fin_assets | 交易性金融资产 |
| derivative_fin_assets | 衍生金融资产 |
| bill_receivable | 应收票据 |
| account_receivable | 应收账款 |
| advance_payment | 预付款项 |
| int_rcv | 应收利息 |
| other_receivable | 其他应收款 |
| red_monetary_cap_for_sale | 买入返售金融资产款 |
| agency_bus_assets | 以公允价值计量且其变动计入当期损益的金融资产 |
| inventories | 存货 |
| other_current_assets | 其他流动资产 |
| total_current_assets | 流动资产合计 |
| loans_and_adv_granted | 发放贷款及垫款 |
| fin_assets_avail_for_sale | 可供出售金融资产 |
| held_to_mty_invest | 持有至到期投资 |
| long_term_eqy_invest | 长期股权投资 |
| invest_real_estate | 投资性房地产 |
| accumulated_depreciation | 累计折旧 |
| fix_assets | 固定资产 |
| constru_in_process | 在建工程 |
| construction_materials | 工程物资 |
| long_term_liabilities | 长期负债 |
| intang_assets | 无形资产 |
| goodwill | 商誉 |
| long_deferred_expense | 长期待摊费用 |
| deferred_tax_assets | 递延所得税资产 |
| total_non_current_assets | 非流动资产合计 |
| tot_assets | 资产总计 |
| shortterm_loan | 短期借款 |
| borrow_central_bank | 向中央银行借款 |
| loans_oth_banks | 拆入资金 |
| tradable_fin_liab | 交易性金融负债 |
| derivative_fin_liab | 衍生金融负债 |
| notes_payable | 应付票据 |
| accounts_payable | 应付账款 |
| advance_peceipts | 预收账款 |
| fund_sales_fin_assets_rp | 卖出回购金融资产款 |
| empl_ben_payable | 应付职工薪酬 |
| taxes_surcharges_payable | 应交税费 |
| int_payable | 应付利息 |
| dividend_payable | 应付股利 |
| other_payable | 其他应付款 |
| non_current_liability_in_one_year | 一年内到期的非流动负债 |
| other_current_liability | 其他流动负债 |
| total_current_liability | 流动负债合计 |
| long_term_loans | 长期借款 |
| bonds_payable | 应付债券 |
| longterm_account_payable | 长期应付款 |
| grants_received | 专项应付款 |
| deferred_tax_liab | 递延所得税负债 |
| other_non_current_liabilities | 其他非流动负债 |
| non_current_liabilities | 非流动负债合计 |
| tot_liab | 负债合计 |
| cap_stk | 实收资本(或股本) |
| cap_rsrv | 资本公积 |
| specific_reserves | 专项储备 |
| surplus_rsrv | 盈余公积 |
| prov_nom_risks | 一般风险准备 |
| undistributed_profit | 未分配利润 |
| cnvd_diff_foreign_curr_stat | 外币报表折算差额 |
| tot_shrhldr_eqy_excl_min_int | 归属于母公司股东权益合计 |
| minority_int | 少数股东权益 |
| total_equity | 所有者权益合计 |
| tot_liab_shrhldr_eqy | 负债和股东权益总计 |

#### 利润表

- 内置表名：ASHAREINCOME
- 原生表名：Income

| 字段名 | 定义 |
| --- | --- |
| m_anntime | 披露日期 |
| m_timetag | 截止日期 |
| revenue_inc | 营业收入 |
| earned_premium | 已赚保费 |
| real_estate_sales_income | 房地产销售收入 |
| total_operating_cost | 营业总成本 |
| real_estate_sales_cost | 房地产销售成本 |
| research_expenses | 研发费用 |
| surrender_value | 退保金 |
| net_payments | 赔付支出净额 |
| net_withdrawal_ins_con_res | 提取保险合同准备金净额 |
| policy_dividend_expenses | 保单红利支出 |
| reinsurance_cost | 分保费用 |
| change_income_fair_value | 公允价值变动收益 |
| futures_loss | 期货损益 |
| trust_income | 托管收益 |
| subsidize_revenue | 补贴收入 |
| other_business_profits | 其他业务利润 |
| net_profit_excl_merged_int_inc | 被合并方在合并前实现净利润 |
| int_inc | 利息收入 |
| handling_chrg_comm_inc | 手续费及佣金收入 |
| less_handling_chrg_comm_exp | 手续费及佣金支出 |
| other_bus_cost | 其他业务成本 |
| plus_net_gain_fx_trans | 汇兑收益 |
| il_net_loss_disp_noncur_asset | 非流动资产处置收益 |
| inc_tax | 所得税费用 |
| unconfirmed_invest_loss | 未确认投资损失 |
| net_profit_excl_min_int_inc | 归属于母公司所有者的净利润 |
| less_int_exp | 利息支出 |
| other_bus_inc | 其他业务收入 |
| revenue | 营业总收入 |
| total_expense | 营业成本 |
| less_taxes_surcharges_ops | 营业税金及附加 |
| sale_expense | 销售费用 |
| less_gerl_admin_exp | 管理费用 |
| financial_expense | 财务费用 |
| less_impair_loss_assets | 资产减值损失 |
| plus_net_invest_inc | 投资收益 |
| incl_inc_invest_assoc_jv_entp | 联营企业和合营企业的投资收益 |
| oper_profit | 营业利润 |
| plus_non_oper_rev | 营业外收入 |
| less_non_oper_exp | 营业外支出 |
| tot_profit | 利润总额 |
| net_profit_incl_min_int_inc | 净利润 |
| net_profit_incl_min_int_inc_after | 净利润(扣除非经常性损益后) |
| minority_int_inc | 少数股东损益 |
| s_fa_eps_basic | 基本每股收益 |
| s_fa_eps_diluted | 稀释每股收益 |
| total_income | 综合收益总额 |
| total_income_minority | 归属于少数股东的综合收益总额 |
| other_compreh_inc | 其他收益 |

#### 现金流表

- 内置表名：ASHARECASHFLOW
- 原生表名: CashFlow

| 字段名 | 定义 |
| --- | --- |
| m_anntime | 披露日期 |
| m_timetag | 截止日期 |
| cash_received_ori_ins_contract_pre | 收到原保险合同保费取得的现金 |
| net_cash_received_rei_ope | 收到再保险业务现金净额 |
| net_increase_insured_funds | 保户储金及投资款净增加额 |
| net_increase_in_disposal | 处置交易性金融资产净增加额 |
| cash_for_interest | 收取利息、手续费及佣金的现金 |
| net_increase_in_repurchase_funds | 回购业务资金净增加额 |
| cash_for_payment_original_insurance | 支付原保险合同赔付款项的现金 |
| cash_payment_policy_dividends | 支付保单红利的现金 |
| disposal_other_business_units | 处置子公司及其他收到的现金 |
| cash_received_from_pledges | 减少质押和定期存款所收到的现金 |
| cash_paid_for_investments | 投资所支付的现金 |
| net_increase_in_pledged_loans | 质押贷款净增加额 |
| cash_paid_by_subsidiaries | 取得子公司及其他营业单位支付的现金净额 |
| increase_in_cash_paid | 增加质押和定期存款所支付的现金 |
| cass_received_sub_abs | 其中子公司吸收现金 |
| cass_received_sub_investments | 其中:子公司支付给少数股东的股利、利润 |
| minority_shareholder_profit_loss | 少数股东损益 |
| unrecognized_investment_losses | 未确认的投资损失 |
| ncrease_deferred_income | 递延收益增加(减:减少) |
| projected_liability | 预计负债 |
| increase_operational_payables | 经营性应付项目的增加 |
| reduction_outstanding_amounts_less | 已完工尚未结算款的减少(减:增加) |
| reduction_outstanding_amounts_more | 已结算尚未完工款的增加(减:减少) |
| goods_sale_and_service_render_cash | 销售商品、提供劳务收到的现金 |
| net_incr_dep_cob | 客户存款和同业存放款项净增加额 |
| net_incr_loans_central_bank | 向中央银行借款净增加额(万元) |
| net_incr_fund_borr_ofi | 向其他金融机构拆入资金净增加额 |
| net_incr_fund_borr_ofi | 拆入资金净增加额 |
| tax_levy_refund | 收到的税费与返还 |
| cash_paid_invest | 投资支付的现金 |
| other_cash_recp_ral_oper_act | 收到的其他与经营活动有关的现金 |
| stot_cash_inflows_oper_act | 经营活动现金流入小计 |
| goods_and_services_cash_paid | 购买商品、接受劳务支付的现金 |
| net_incr_clients_loan_adv | 客户贷款及垫款净增加额 |
| net_incr_dep_cbob | 存放中央银行和同业款项净增加额 |
| handling_chrg_paid | 支付利息、手续费及佣金的现金 |
| cash_pay_beh_empl | 支付给职工以及为职工支付的现金 |
| pay_all_typ_tax | 支付的各项税费 |
| other_cash_pay_ral_oper_act | 支付其他与经营活动有关的现金 |
| stot_cash_outflows_oper_act | 经营活动现金流出小计 |
| net_cash_flows_oper_act | 经营活动产生的现金流量净额 |
| cash_recp_disp_withdrwl_invest | 收回投资所收到的现金 |
| cash_recp_return_invest | 取得投资收益所收到的现金 |
| net_cash_recp_disp_fiolta | 处置固定资产、无形资产和其他长期投资收到的现金 |
| other_cash_recp_ral_inv_act | 收到的其他与投资活动有关的现金 |
| stot_cash_inflows_inv_act | 投资活动现金流入小计 |
| cash_pay_acq_const_fiolta | 购建固定资产、无形资产和其他长期投资支付的现金 |
| other_cash_pay_ral_oper_act | 支付其他与投资的现金 |
| stot_cash_outflows_inv_act | 投资活动现金流出小计 |
| net_cash_flows_inv_act | 投资活动产生的现金流量净额 |
| cash_recp_cap_contrib | 吸收投资收到的现金 |
| cash_recp_borrow | 取得借款收到的现金 |
| proc_issue_bonds | 发行债券收到的现金 |
| other_cash_recp_ral_fnc_act | 收到其他与筹资活动有关的现金 |
| stot_cash_inflows_fnc_act | 筹资活动现金流入小计 |
| cash_prepay_amt_borr | 偿还债务支付现金 |
| cash_pay_dist_dpcp_int_exp | 分配股利、利润或偿付利息支付的现金 |
| other_cash_pay_ral_fnc_act | 支付其他与筹资的现金 |
| stot_cash_outflows_fnc_act | 筹资活动现金流出小计 |
| net_cash_flows_fnc_act | 筹资活动产生的现金流量净额 |
| eff_fx_flu_cash | 汇率变动对现金的影响 |
| net_incr_cash_cash_equ | 现金及现金等价物净增加额 |
| cash_cash_equ_beg_period | 期初现金及现金等价物余额 |
| cash_cash_equ_end_period | 期末现金及现金等价物余额 |
| net_profit | 净利润 |
| plus_prov_depr_assets | 资产减值准备 |
| depr_fa_coga_dpba | 固定资产折旧、油气资产折耗、生产性物资折旧 |
| amort_intang_assets | 无形资产摊销 |
| amort_lt_deferred_exp | 长期待摊费用摊销 |
| decr_deferred_exp | 待摊费用的减少 |
| incr_acc_exp | 预提费用的增加 |
| loss_disp_fiolta | 处置固定资产、无形资产和其他长期资产的损失 |
| loss_scr_fa | 固定资产报废损失 |
| loss_fv_chg | 公允价值变动损失 |
| fin_exp | 财务费用 |
| invest_loss | 投资损失 |
| decr_deferred_inc_tax_assets | 递延所得税资产减少 |
| incr_deferred_inc_tax_liab | 递延所得税负债增加 |
| decr_inventories | 存货的减少 |
| decr_oper_payable | 经营性应收项目的减少 |
| others | 其他 |
| im_net_cash_flows_oper_act | 经营活动产生现金流量净额 |
| conv_debt_into_cap | 债务转为资本 |
| conv_corp_bonds_due_within_1y | 一年内到期的可转换公司债券 |
| fa_fnc_leases | 融资租入固定资产 |
| end_bal_cash | 现金的期末余额 |
| less_beg_bal_cash | 现金的期初余额 |
| plus_end_bal_cash_equ | 现金等价物的期末余额 |
| less_beg_bal_cash_equ | 现金等价物的期初余额 |
| im_net_incr_cash_cash_equ | 现金及现金等价物的净增加额 |
| tax_levy_refund | 收到的税费返还 |

#### 股本表

- 内置表名：CAPITALSTRUCTURE
- 原生表名：Capital

| **中文字段** | **迅投字段** |
| --- | --- |
| 总股本 | total_capital |
| 已上市流通A股 | circulating_capital |
| 限售流通股份 | restrict_circulating_capital |
| 变动日期 | m_timetag |
| 公告日 | m_anntime |

#### 主要指标

- 内置表名：PERSHAREINDEX
- 原生表名：PershareIndex

| **中文字段** | **迅投字段** |
| --- | --- |
| 每股经营活动现金流量 | s_fa_ocfps |
| 每股净资产 | s_fa_bps |
| 基本每股收益 | s_fa_eps_basic |
| 稀释每股收益 | s_fa_eps_diluted |
| 每股未分配利润 | s_fa_undistributedps |
| 每股资本公积金 | s_fa_surpluscapitalps |
| 扣非每股收益 | adjusted_earnings_per_share |
| 净资产收益率 | du_return_on_equity |
| 销售毛利率 | sales_gross_profit |
| 主营收入同比增长 | inc_revenue_rate |
| 净利润同比增长 | du_profit_rate |
| 归属于母公司所有者的净利润同比增长 | inc_net_profit_rate |
| 扣非净利润同比增长 | adjusted_net_profit_rate |
| 营业总收入滚动环比增长 | inc_total_revenue_annual |
| 归属净利润滚动环比增长 | inc_net_profit_to_shareholders_annual |
| 扣非净利润滚动环比增长 | adjusted_profit_to_profit_annual |
| 加权净资产收益率 | equity_roe |
| 摊薄净资产收益率 | net_roe |
| 摊薄总资产收益率 | total_roe |
| 毛利率 | gross_profit |
| 净利率 | net_profit |
| 实际税率 | actual_tax_rate |
| 预收款营业收入 | pre_pay_operate_income |
| 销售现金流营业收入 | sales_cash_flow |
| 资产负债比率 | gear_ratio |
| 存货周转率 | inventory_turnover |

#### 十大股东/十大流通股东

- 内置表名：TOP10HOLDER/TOP10FLOWHOLDER
- 原生表名：Top10holder/Top10flowholder

| **中文字段** | **迅投字段** |
| --- | --- |
| `公告日期` | `declareDate` |
| `截止日期` | `endDate` |
| `股东名称` | `name` |
| `股东类型` | `type` |
| `持股数量` | `quantity` |
| `变动原因` | `reason` |
| `持股比例` | `ratio` |
| `股份性质` | `nature` |
| `持股排名` | `rank` |

#### 股东数

- 内置表名：SHAREHOLDER
- 原生表名：Holdernum

| **中文字段** | **迅投字段** |
| --- | --- |
| `公告日期` | `declareDate` |
| `截止日期` | `endDate` |
| `股东总数` | `shareholder` |
| `A股东户数` | `shareholderA` |
| `B股东户数` | `shareholderB` |
| `H股东户数` | `shareholderH` |
| `已流通股东户数` | `shareholderFloat` |
| `未流通股东户数` | `shareholderOther` |