---
url: "https://dict.thinktrader.net/innerApi/data_function.html"
title: "行情函数 | 迅投知识库"
---

## 数据下载

### download_history_data - 下载指定合约代码指定周期对应时间范围的行情数据

提示

QMT提供的行情数据中，基础周期包含 tick、1m、5m、1d，这些是实际用于存储的周期。其他周期为合成周期，以基础周期合成得到

合成周期

- 3m， 由1m线合成
- 10m, 15m, 30m, 60m, 2h, 3h, 4h 由5分钟线合成
- 2d(2日线), 3d(3日线), 5d(5日线), 1w（周线）, 1mon（月线）, 1q(季线), 1hy(半年线), 1y（年线） 由日线数据合成

获取合成周期时

- 如果取历史，需要下载历史的基础周期（如取15m需要下载5m）
- 如果取实时，可以直接订阅原始周期（如直接订阅15m）

如果同时用到基础周期和合成周期，只需要下载基础周期,例如同时使用5m和15m，因为15m也是由5m合成，所以只需要下载一次5m的数据即可

**原型**

```py
download_history_data(stockcode,period,startTime,endTime)
```

**释义**

下载指定合约代码指定周期对应时间范围的行情数据

**参数**

| 字段名 | 数据类型 | 解释 |
| --- | --- | --- |
| `stockcode` | `string` | 股票代码，格式为'stkcode.market'，例如 '600000.SH' |
| `period` | `string` | K线周期类型，包括:<br>`'tick'`：分笔线<br>`'1d'`：日线<br>`'1m'`：分钟线<br>`'5m'`：5分钟线 |
| `startTime` | `string` | 起始时间，格式为 "20200101" 或 "20200101093000"，可以为空 |
| `endTime` | `string` | 结束时间，格式为 "20200101" 或 "20200101093000"，可以为空 |
| `incrementally` | `bool` | 默认为 `None` 是否从本地最后一条数据往后增量下载，部分版本客户端可能不支持此参数 |

**返回值**

`none`

**示例**

示例

```py
# coding:gbk
def init(C):
	download_history_data("000001.SZ","1d","20230101","") # 下载000001.SZ,从20230101至今的日线数据
    download_history_data("000001.SZ","1d","20230101","",incrementally=True) # 下载000001.SZ,从20230101至今的日线数据,增量下载

def handlebar(C):
    return
```

界面端进行数据下载可参考:

【攻略】K线/财务数据下载方式 https://www.xuntou.net/forum.php?mod=viewthread&tid=1354&user_code=7zqjlm

## 获取行情数据

该目录下的函数用于获取实时行情,历史行情

### ContextInfo.get_market_data_ex - 获取行情数据

注意

1. **该函数不建议在`init`中运行,在`init`中运行时仅能取到本地数据**
2. 关于获取行情函数之间的区别与注意事项可在 - [常见问题-行情相关](question_answer.md#%E8%A1%8C%E6%83%85%E7%9B%B8%E5%85%B3) 查看
3. 除实时行情外，该函数还可用于获取特色数据，如`资金流向数据`,`订单流数据`等，获取方式见 [数据字典](https://dict.thinktrader.net/dictionary/)

**原型**

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
| `period` | `str` | `数据周期，可选字段为:`<br>`"tick"`<br>`"1m"：1分钟线`<br>`"5m"：5分钟线；"15m"：15分钟线；"30m"：30分钟线`<br>`"1h"小时线`<br>`"1d"：日线`<br>`"1w"：周线`<br>`"1mon"：月线`<br>`"1q"：季线`<br>`"1hy"：半年线`<br>`"1y"：年线`<br>`'l2quote'：Level2行情快照`<br>`'l2quoteaux'：Level2行情快照补充`<br>`'l2order'：Level2逐笔委托`<br>`'l2transaction'：Level2逐笔成交`<br>`'l2transactioncount'：Level2大单统计`<br>`'l2orderqueue'：Level2委买委卖队列` |
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

| field | 数据类型 | 含义 |
| --- | --- | --- |
| `time` | `int` | `时间` |
| `lastPrice` | `float` | `最新价` |
| `lastClose` | `float` | `前收盘价` |
| `open` | `float` | `开盘价` |
| `high` | `float` | `最高价` |
| `low` | `float` | `最低价` |
| `close` | `float` | `收盘价` |
| `volume` | `float` | `成交量` |
| `amount` | `float` | `成交额` |
| `settle` | `float` | `今结算` |
| `openInterest` | `float` | `持仓量` |
| `stockStatus` | `int` | `停牌` 1停牌，0 不停牌 |

- `period`周期为Level2数据时，字段参考 [数据结构](data_structure.md#l2quote-level2%E8%A1%8C%E6%83%85%E5%BF%AB%E7%85%A7)

**返回值**

- 返回dict { stock_code1 : value1, stock_code2 : value2, ... }
- value1, value2, ... ：pd.DataFrame 数据集，index为 time_list，columns为fields,可参考 [Bar字段](data_structure.md#bar-bar%E5%AF%B9%E8%B1%A1)
- 各标的对应的DataFrame维度相同、索引相同

**示例**

```py
# coding:gbk
import pandas as pd
import numpy as np

def init(C):
	C.stock_list = ["000001.SZ","600519.SH", "510050.SH"]# 指定获取的标的
	C.start_time = "20230901"# 指定获取数据的开始时间
	C.end_time = "20231101"# 指定获取数据的结束时间

def handlebar(C):
	# 获取多只股票，多个字段，一条数据
	data1 = C.get_market_data_ex([],C.stock_list, period = "1d",count = 1)
	# 获取多只股票，多个字段，指定时间数据
	data2 = C.get_market_data_ex([],C.stock_list, period = "1d", start_time = C.start_time, end_time = C.end_time)
	# 获取多只股票，多个字段，指定时间15m数据
	data3 = C.get_market_data_ex([],C.stock_list, period = "15m", start_time = C.start_time, end_time = C.end_time)
	# 获取多只股票，指定字段，指定时间15m数据
	data4 = C.get_market_data_ex(["close","open"],C.stock_list, period = "15m", start_time = C.start_time, end_time = C.end_time)
	# 获取多只股票，历史tick
	tick = C.get_market_data_ex([],C.stock_list, period = "tick", start_time = C.start_time, end_time = C.end_time)
	# 获取期货5档盘口tick
	future_lv2_quote = C.get_market_data_ex([],["rb2405.SF","ec2404.INE"], period = "l2quote", count = 1)
	print(data1)
	print(data2["000001.SZ"].tail())
	print(data3)
	print(data4["000001.SZ"])
	print(data4["000001.SZ"].to_csv("your_path")) # 导出文件为csv格式，路径填本机路径
	print(tick["000001.SZ"])
	print(future_lv2_quote)
```

### ContextInfo.get_full_tick - 获取全推数据

提示

不能用于回测 只能取最新的分笔，不能取历史分笔

**原型**

```py
ContextInfo.get_full_tick(stock_code=[])
```

**释义**

获取最新分笔数据

**参数**

| 名称 | 类型 | 描述 |
| --- | --- | --- |
| `stock_code` | `list[str]` | `合约代码列表，如['600000.SH','600036.SH']，不指定时为当前主图合约。` |

**返回值** 根据stock_code返回一个dict，该字典的key值是股票代码，其值仍然是一个dict，在该dict中存放股票代码对应的最新的数据。该字典数据key值参考 [tick字段](data_structure.md#tick-tick-%E5%AF%B9%E8%B1%A1)

**示例**

```py
# coding:gbk
import pandas as pd
import numpy as np

def init(C):
	C.stock_list = ["000001.SZ","600519.SH", "510050.SH"]

def handlebar(C):
	tick = C.get_full_tick(C.stock_list)
	print(tick["510050.SH"])
```

```
{'timetag': '20231106 15:00:04', 'lastPrice': 2.533, 'open': 2.528, 'high': 2.5380000000000003, 'low': 2.521, 'lastClose': 2.513, 'amount': 1442588037.0, 'volume': 5701929, 'pvolume': 5701929, 'stockStatus': 5, 'openInt': 15, 'settlementPrice': 0.0, 'lastSettlementPrice': 0.0, 'askPrice': [2.533, 2.5340000000000003, 2.535, 2.536, 2.537], 'bidPrice': [2.532, 2.531, 2.5300000000000002, 2.529, 2.528], 'askVol': [2615, 19753, 24334, 16932, 35835], 'bidVol': [5662, 24808, 11876, 11472, 14966]}
```

### ContextInfo.subscribe_quote - 订阅行情数据

提示

1. 该函数属于订阅函数，非VIP用户限制订阅数量
2. VIP用户支持全推市场指定周期K线
3. VIP用户权限请参考 [vip-行情用户优势对比](https://dict.thinktrader.net/dictionary/#vip-%E8%A1%8C%E6%83%85%E7%94%A8%E6%88%B7%E4%BC%98%E5%8A%BF%E5%AF%B9%E6%AF%94)

**原型**

```py
ContextInfo.subscribe_quote(
    stock_code,
    period='follow',
    dividend_type='follow',
    result_type='',
    callback=None)
```

**释义**

订阅行情数据,关于订阅机制请参考 [运行机制对比](start_now.md#%E4%B8%89%E3%80%81%E8%BF%90%E8%A1%8C%E6%9C%BA%E5%88%B6%E5%AF%B9%E6%AF%94)

**参数**

| 字段名 | 数据类型 | 解释 |
| --- | --- | --- |
| `stockcode` | `string` | `股票代码，'stkcode.market'，如'600000.SH'` |
| `period` | `string` | `K线周期类型` |
| `dividend_type` | `string` | `除权方式,可选值为`<br>`'none'：不复权`<br>`'front':前复权`<br>`'back':后复权`<br>`'front_ratio': 等比前复权`<br>`'back_ratio': 等比后复权`<br>`注意：分笔周期返回数据均为不复权` |
| `result_type` | `string` | `返回数据格式,可选范围：<br>'DataFrame'或''（默认）：返回{code:data}，data为pd.DataFrame数据集，index为字符串格式的时间序列，columns为数据字段<br>'dict'：返回{code:{k1:v1,k2:v2,...}}，k为数据字段名，v为字段值<br>'list'：返回{code:{k1:[v1],k2:[v2],...}}，k为数据字段名，v为字段值` |
| `callback` | `function` | `指定推送行情的回调函数` |

**返回值**

`int`：订阅号，用于反订阅

**示例**

```py
# coding:gbk
def call_back(data):
	print(data)

def init(C):
	C.subID = C.subscribe_quote("000001.SZ","1d", callback = call_back)
def handlebar(C):
	print("============================")
	print("C.subID: ",C.subID)
```
返回值
```
{'000001.SZ':                amount  close   high    low   open  openInterest  preClose
stime
20231107  254505920.0   10.6  10.66  10.58  10.66            13     10.69

          settelementPrice     stime  suspendFlag           time
stime
20231107               0.0  20231107            0  1699286400000

                 timeEx  volume
stime
20231107  1699286400000  239704  }
============================
C.subID:  11
```

### ContextInfo.subscribe_whole_quote - 订阅全推数据


```py
ContextInfo.subscribe_whole_quote(code_list,callback=None)
```

**释义**

订阅全推数据，全推数据只有分笔周期，每次增量推送数据有变化的品种

**参数**

| 字段名 | 数据类型 | 解释 |
| --- | --- | --- |
| `code_list` | `list[str,...]` | `市场代码列表/品种代码列表,如 ['SH','SZ'] 或 ['600000.SH', '000001.SZ']` |
| `callback` | `function` | `数据推送回调` |

**返回值**`int`，订阅号，可用`ContextInfo.unsubscribe_quote`做反订阅

示例：

```py
# coding:gbk
def call_back(data):
	print(data)

def init(C):
	C.stock_list = ["000001.SZ","600519.SH", "510050.SH"]
	C.subID = C.subscribe_whole_quote(C.stock_list,callback=call_back)
def handlebar(C):
	print("============================")
	print("C.subID: ",C.subID)
```
返回值：
```
C.subID:  2
{'000001.SZ': {'time': 1699326201000, 'stime': '20231107110321.000', 'lastPrice': 10.620000000000001, 'amount': 310826160.0, 'volume': 292680, 'pvolume': 292680, 'openInt': 13, 'stockStatus': 3, 'lastSettlementPrice': 0.0, 'open': 10.66, 'high': 10.66, 'low': 10.58, 'settlementPrice': 0.0, 'lastClose': 10.69, 'transactionNum': 0, 'askPrice': [10.63, 10.64, 10.65, 10.66, 10.67], 'bidPrice': [10.620000000000001, 10.61, 10.6, 10.59, 10.58], 'askVol': [3284, 4654, 6762, 8346, 1431], 'bidVol': [574, 5275, 13643, 8898, 14521]}}
{'510050.SH': {'time': 1699326202000, 'stime': '20231107110322.000', 'lastPrice': 2.519, 'amount': 578313036.0, 'volume': 2294893, 'pvolume': 2294893, 'openInt': 13, 'stockStatus': 3, 'lastSettlementPrice': 0.0, 'open': 2.528, 'high': 2.528, 'low': 2.515, 'settlementPrice': 0.0, 'lastClose': 2.533, 'transactionNum': 0, 'askPrice': [2.519, 2.52, 2.521, 2.5220000000000002, 2.523], 'bidPrice': [2.5180000000000002, 2.517, 2.516, 2.515, 2.5140000000000002], 'askVol': [15233, 71470, 59978, 30042, 17226], 'bidVol': [34168, 57565, 82326, 59915, 23790]}}
{'600519.SH': {'time': 1699326203000, 'stime': '20231107110323.000', 'lastPrice': 1790.9, 'amount': 1714097021.0, 'volume': 9547, 'pvolume': 9547, 'openInt': 13, 'stockStatus': 3, 'lastSettlementPrice': 0.0, 'open': 1805.0, 'high': 1810.0, 'low': 1789.0, 'settlementPrice': 0.0, 'lastClose': 1812.0, 'transactionNum': 0, 'askPrice': [1790.9, 1791.0, 1791.4, 1791.5, 1791.58], 'bidPrice': [1790.3400000000001, 1790.33, 1790.23, 1790.18, 1790.17], 'askVol': [1, 11, 1, 3, 2], 'bidVol': [3, 1, 1, 1, 1]}}
============================
C.subID:  2
{'000001.SZ': {'time': 1699326204000, 'stime': '20231107110324.000', 'lastPrice': 10.63, 'amount': 310842090.0, 'volume': 292695, 'pvolume': 292695, 'openInt': 13, 'stockStatus': 3, 'lastSettlementPrice': 0.0, 'open': 10.66, 'high': 10.66, 'low': 10.58, 'settlementPrice': 0.0, 'lastClose': 10.69, 'transactionNum': 0, 'askPrice': [10.63, 10.64, 10.65, 10.66, 10.67], 'bidPrice': [10.620000000000001, 10.61, 10.6, 10.59, 10.58], 'askVol': [3279, 4654, 6762, 8346, 1431], 'bidVol': [579, 5275, 13628, 8898, 14521]}}
{'510050.SH': {'time': 1699326205000, 'stime': '20231107110325.000', 'lastPrice': 2.519, 'amount': 578313036.0, 'volume': 2294893, 'pvolume': 2294893, 'openInt': 13, 'stockStatus': 3, 'lastSettlementPrice': 0.0, 'open': 2.528, 'high': 2.528, 'low': 2.515, 'settlementPrice': 0.0, 'lastClose': 2.533, 'transactionNum': 0, 'askPrice': [2.519, 2.52, 2.521, 2.5220000000000002, 2.523], 'bidPrice': [2.5180000000000002, 2.517, 2.516, 2.515, 2.5140000000000002], 'askVol': [15243, 71470, 59778, 29042, 20670], 'bidVol': [34668, 62360, 81475, 59866, 24894]}}
{'600519.SH': {'time': 1699326206000, 'stime': '20231107110326.000', 'lastPrice': 1790.3400000000001, 'amount': 1714276564.0, 'volume': 9548, 'pvolume': 9548, 'openInt': 13, 'stockStatus': 3, 'lastSettlementPrice': 0.0, 'open': 1805.0, 'high': 1810.0, 'low': 1789.0, 'settlementPrice': 0.0, 'lastClose': 1812.0, 'transactionNum': 0, 'askPrice': [1790.89, 1790.9, 1791.0, 1791.4, 1791.5], 'bidPrice': [1790.3400000000001, 1790.33, 1790.23, 1790.18, 1790.17], 'askVol': [1, 1, 11, 1, 3], 'bidVol': [2, 1, 1, 1, 1]}}
```

### ContextInfo.unsubscribe_quote - 反订阅行情数据

**原型**

```py
ContextInfo.unsubscribe_quote(subId)
```

**释义**

反订阅行情数据，配合`ContextInfo.subscribe_quote()`或`ContextInfo.subscribe_whole_quote()`使用

**参数**

| 字段名 | 数据类型 | 解释 |
| --- | --- | --- |
| `subId` | `int` | `行情订阅返回的订阅号` |

**示例**

示例

```py
# coding:gbk
def call_back(data):
	print(data)
def init(C):
	C.stock_list = ["000001.SZ","600519.SH", "510050.SH"]
	C.subID = C.subscribe_whole_quote(C.stock_list,callback=call_back)

def handlebar(C):
	print("============================")
	print("C.subID: ",C.subID)
	if C.subID > 0:
		C.unsubscribe_quote(C.subID) # 取消行情订阅
```

### subscribe_formula - 订阅模型

**原型**

```py
subscribe_formula(
   formula_name,stock_code,period
   ,start_time="",end_time="",count=-1
   ,dividend_type="none"
   ,extend_param={}
   ,callback=None)
```

**释义** 订阅vba模型运行结果，使用前要注意补充本地K线数据或分笔数据

**参数**

| 字段名 | 类型 | 描述 |
| --- | --- | --- |
| formula_name | str | 模型名称名 |
| stock_code | str | 模型主图代码形式如'stkcode.market'，如'000300.SH' |
| period | str | K线周期类型，可选范围：'tick':分笔线，'1d':日线，'1m':分钟线，'3m':三分钟线，'5m':5分钟线，'15m':15分钟线，'30m':30分钟线，'1h':小时线，'1w':周线，'1mon':月线，'1q':季线，'1hy':半年线，'1y':年线 |
| start_time | str | 模型运行起始时间，形如:'20200101'，默认为空视为最早 |
| end_time | str | 模型运行截止时间，形如:'20200101'，默认为空视为最新 |
| count | int | 模型运行范围为向前 count 根 bar，默认为 -1 运行所有 bar |
| dividend_type | str | 复权方式，默认为主图除权方式，可选范围：'none':不复权，'front':向前复权，'back':向后复权，'front_ratio':等比向前复权，'back_ratio':等比向后复权 |
| extend_param | dict | 模型的入参，形如 {'a': 1, '__basket': {}} |
| __basket | dict | 可选参数，组合模型的股票池权重，形如 {'600000.SH': 0.06, '000001.SZ': 0.01} |

**返回值** 分两块，

- subscribe_formula返回模型的订阅号,可用于后续反订阅，失败返回 -1

- callback:

  - timelist： 数据时间戳
  - outputs：模型的输出值，结构为{变量名:值}

**示例**

```py
#encoding=gbk
def callback(data):
    print(data)

def init(ContextInfo):
    basket={
       '600000.SH':0.06,
       '000001.SZ':0.01
      }
    argsDict={'a':100,'__basket':basket}
    subID=subscribe_formula(
      '单股模型示范','000300.SH','1d',
      '20240101','20240201',-1,
      "none",
      argsDict,
      callback
   )
```

### unsubscribe_formula - 反订阅模型

**原型**

```py
unsubscribe_formula(subID)
```

**释义** 反订阅模型

**参数**

| 字段名 | 类型 | 描述 |
| --- | --- | --- |
| subID | int | 模型订阅号 |

**返回值**

- bool:反订阅成功为True，失败为False

**示例**

```py
#encoding=gbk
def callback(data):
    print(data)

def init(ContextInfo):
    basket={
       '600000.SH':0.06,
       '000001.SZ':0.01
      }
    argsDict={'a':100,'__basket':basket}
    subID=subscribe_formula(
      '单股模型示范','000300.SH','1d',
      '20240101','20240201',-1,
      "none",
      argsDict,
      callback
   )

	unsubscribe_formula(subID)
```

### call_formula - 调用模型

**原型**

```py
call_formula(formula_name,stock_code,period,start_time="",end_time="",count=-1,dividend_type="none",extend_param={})
```

**释义** 获取vba模型运行结果，使用前要注意补充本地K线数据或分笔数据

**参数**

| 字段名 | 类型 | 描述 |
| --- | --- | --- |
| formula_name | str | 模型名称名 |
| stock_code | str | 模型主图代码形式如'stkcode.market'，如'000300.SH' |
| period | str | K线周期类型，可选范围：'tick':分笔线，'1d':日线，'1m':分钟线，'3m':三分钟线，'5m':5分钟线，'15m':15分钟线，'30m':30分钟线，'1h':小时线，'1w':周线，'1mon':月线，'1q':季线，'1hy':半年线，'1y':年线 |
| start_time | str | 模型运行起始时间，形如:'20200101'，默认为空视为最早 |
| end_time | str | 模型运行截止时间，形如:'20200101'，默认为空视为最新 |
| count | int | 模型运行范围为向前 count 根 bar，默认为 -1 运行所有 bar |
| dividend_type | str | 复权方式，默认为主图除权方式，可选范围：'none':不复权，'front':向前复权，'back':向后复权，'front_ratio':等比向前复权，'back_ratio':等比向后复权 |
| extend_param | dict | 模型的入参,{"模型名:参数名":参数值},例如在跑模型MA时，{'MA:n1':1};入参可以添加__basket:dict,组合模型的股票池权重,形如{'__basket':{'600000.SH':0.06,'000001.SZ':0.01}}，如果在跑一个模型1的时候，模型1调用了模型2，如果只想修改模型2的参数可以传{'模型2:参数':参数值} |

**返回值** 返回：dict{ 'dbt':0,#返回数据类型，0:全部历史数据 'timelist':[...],#返回数据时间范围list, 'outputs':{'var1':[...],'var2':[...]}#输出变量名：变量值list }

**示例**

示例

```
def handlebar(ContextInfo):
    basket={'600000.SH':0.06,'000001.SZ':0.01}
    argsDict={'a':100,'__basket':basket}
    modelRet=call_formula('单股模型示范','000300.SH','1d','20240101','20240201',-1,"none",argsDict)
    print(modelRet)
```

### call_formula_batch - 批量调用模型

**原型**

```py
call_formula_batch(formula_names,stock_codes,period,start_time="",end_time="",count=-1,dividend_type="none",extend_params=[])
```

**释义** 批量获取vba模型运行结果，使用前要注意补充本地K线数据或分笔数据

**参数**

| 字段名 | 类型 | 描述 |
| --- | --- | --- |
| formula_names | list | 包含要批量运行的模型名 |
| stock_codes | list | 包含要批量运行的模型主图代码形式'stkcode.market'，如'000300.SH' |
| period | str | K线周期类型，可选范围：'tick':分笔线，'1d':日线，'1m':分钟线，'3m':三分钟线，'5m':5分钟线，'15m':15分钟线，'30m':30分钟线，'1h':小时线，'1w':周线，'1mon':月线，'1q':季线，'1hy':半年线，'1y':年线 |
| start_time | str | 模型运行起始时间，形如:'20200101'，默认为空视为最早 |
| end_time | str | 模型运行截止时间，形如:'20200101'，默认为空视为最新 |
| count | int | 模型运行范围为向前 count 根 bar，默认为 -1 运行所有 bar |
| dividend_type | str | 复权方式，默认为主图除权方式，可选范围：'none':不复权，'front':向前复权，'back':向后复权，'front_ratio':等比向前复权，'back_ratio':等比向后复权 |
| extend_params | list | 包含每个模型的入参,[{"模型名:参数名":参数值}],例如在跑模型MA时，{'MA:n1':1};入参可以添加__basket:dict,组合模型的股票池权重,形如{'__basket':{'600000.SH':0.06,'000001.SZ':0.01}}，如果在跑一个模型1的时候，模型1调用了模型2，如果只想修改模型2的参数可以传{'模型2:参数':参数值} |

**返回值**

- list[dict]
  - dict说明:
    - formula:模型名
    - stock:品种代码
    - argument:参数
    - result:dict参考call_formula返回结果

**示例**

示例

```

def handlebar(ContextInfo):
    formulas=['testModel1','testModel2']
    codes=['600000.SH','000001.SZ']
    basket={'600000.SH':0.06,'000001.SZ':0.01}
    args=[{'a':100,'__basket':basket},{'a':200,'__basket':basket}]
    modelRet=call_formula_batch(formulas,codes,'1d',extend_params=args);
    print(modelRet)
```

### ContextInfo.get_svol - 根据代码获取对应股票的内盘成交量

**原型**

```py
ContextInfo.get_svol(stockcode)
```

**释义**

根据代码获取对应股票的内盘成交量

**参数**

| 字段名 | 数据类型 | 解释 |
| --- | --- | --- |
| `stockcode` | `string` | 股票代码，如 '000001.SZ'，缺省值''，默认为当前图代码 |

**返回值**`int`:内盘成交量

**示例**

示例与返回值

```py
# coding:gbk
def init(C):
	pass

def handlebar(C):
	data = C.get_svol('000001.SZ')
	print(data)
```

```
339072
```

### ContextInfo.get_bvol - 根据代码获取对应股票的外盘成交量

**原型**

```py
ContextInfo.get_bvol(stockcode)
```

**释义**

根据代码获取对应股票的外盘成交量

**参数**

| 字段名 | 数据类型 | 解释 |
| --- | --- | --- |
| `stockcode` | `string` | 股票代码，如 '000001.SZ'，缺省值''，默认为当前图代码 |

**返回值**

`int`:外盘成交量

**示例**

示例与返回值

```py
# coding:gbk
def init(C):
	pass

def handlebar(C):
	data = C.get_bvol('000001.SZ')
	print(data)
```

```
301794
```

### ContextInfo.get_turnover_rate - 获取换手率

提示

使用之前需要下载财务数据(在财务数据下载中)以及日线数据

如果不补充股本数据,将使用最新流通股本计算历史换手率,可能会造成历史换手率不正确

**原型**

```py
ContextInfo.get_turnover_rate(stock_list,startTime,endTime)
```

**释义**

获取换手率

**参数**

| 字段名 | 数据类型 | 解释 |
| --- | --- | --- |
| `stock_list` | `list` | 股票列表，如['600000.SH','000001.SZ'] |
| `startTime` | `string` | 起始时间，如'20170101' |
| `endTime` | `string` | 结束时间，如'20180101' |

**返回值**

`pandas.Dataframe`

**示例**

示例与返回值

```py
# coding:gbk
def init(C):
	pass

def handlebar(C):
	data = C.get_turnover_rate(['000002.SZ'],'20170101','20170301')
	print(data)
```

```
          000002.SZ
20170103   0.002235
20170104   0.003415
20170105   0.003194
20170106   0.002430
20170109   0.001555
20170110   0.001639
20170111   0.001737
20170113   0.010962
20170116   0.005698
20170117   0.003307
20170118   0.003345
20170119   0.002234
20170120   0.002215
20170123   0.001611
20170124   0.001641
20170125   0.001593
20170126   0.001455
20170203   0.001122
20170206   0.001453
20170207   0.001793
20170208   0.001855
20170209   0.006996
20170210   0.003450
20170213   0.002937
20170214   0.003808
20170215   0.002959
20170216   0.001762
20170217   0.002041
20170220   0.002549
20170221   0.005529
20170222   0.002321
20170223   0.001974
20170224   0.002241
20170227   0.003022
20170228   0.001645
20170301   0.002581
```

### ContextInfo.get_longhubang - 获取龙虎榜数据

**原型**

```py
ContextInfo.get_longhubang(stock_list, startTime, endTime)
```

**释义**

获取龙虎榜数据

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

示例与返回值

```py
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

### ContextInfo.get_north_finance_change - 获取对应周期的北向数据

**原型**

```py
ContextInfo.get_north_finance_change(period)
```

**释义**

获取对应周期的北向数据

**参数**

| 字段名 | 数据类型 | 描述 |
| --- | --- | --- |
| `period` | `str` | 数据周期 |

**返回值**

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

**示例：**

示例与返回值

```py
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

### ContextInfo.get_hkt_details - 获取指定品种的持股明细

**原型**

```py
ContextInfo.get_hkt_details(stockcode)
```

**释义**

获取指定品种的持股明细

**参数**

| 参数名称 | 数据类型 | 描述 |
| --- | --- | --- |
| `stockcode` | `string` | 必须是'stock.market'形式 |

**返回值**

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

示例与返回值

```py
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

### ContextInfo.get_hkt_statistics - 获取指定品种的持股统计

**原型**

```py
ContextInfo.get_hkt_statistics(stockcode)
```

**释义**

获取指定品种的持股统计

**参数**

| 字段名 | 数据类型 | 解释 |
| --- | --- | --- |
| `stockcode` | `string` | 必须是'stock.market'形式 |

**返回值**

根据stockcode返回一个dict，该字典的key值是北向持股统计数据的时间戳，其值仍然是一个dict，其值的key值是北向持股统计数据的字段类型，其值是对应字段的值，该字典数据key值有：

| 字段名 | 数据类型 | 解释 |
| --- | --- | --- |
| `stockCode` | `string` | 股票代码 |
| `ownSharesAmount` | `float` | 持股数量，单位：股 |
| `ownSharesMarketValue` | `float` | 持股市值，单位：元 |
| `ownSharesRatio` | `float` | 持股数量占比，单位：% |
| `ownSharesNetBuy` | `float` | 净买入，单位：元，浮点数（当日持股-前一日持股） |

**示例**

示例与返回值

```py
# coding:gbk
def init(C):
	pass

def handlebar(C):

	print(C.get_hkt_statistics('600000.SH'))
```

```
{1699200000000: {'stockCode': '600000.SH', 'ownSharesAmount': 607853523, 'ownSharesMarketValue': 4218503449.6200004, 'ownSharesRatio': 2.07, 'ownSharesNetBuy': -5461620.530932084}}
```

### get_etf_info - 根据ETF基金代码获取ETF申赎清单及对应成分股数据

**原型**

```py
get_etf_info(stockcode)
```

**释义**

根据ETF基金代码获取ETF申赎清单及对应成分股数据,每日盘前更新

**参数**

| 字段名 | 数据类型 | 解释 |
| --- | --- | --- |
| `stockcode` | `string` | ETF基金代码如"510050.SH" |

**返回值**

一个多层嵌套的`dict`

**示例**

示例与返回值

```py
# coding:gbk
def init(C):
    pass

def handlebar(C):
    d = get_etf_info("510050.SH")
    print(d)
```

```
{'etfCode': '510050', 'etfExchID': 'SH', 'prCode': '510050', 'cashBalance': 17838.95, 'maxCashRatio': 0.5, 'reportUnit': 900000, 'navPerCU': 2234087.74, 'nav': 2.4823, 'ecc': 13245.23, 'needPublish': 1, 'enableCreation': 1, 'enableRedemption': 1, 'creationLimit': 0, 'redemptionLimit': 0, 'type': 0, 'tradingDay': '', 'preTradingDay': '', 'stocks': {'600028.SH': {'componentExchID': 'SH', 'componentCode': '600028', 'componentVolume': 6300, 'ReplaceFlag': 49, 'ReplaceRatio': 0.1, 'ReplaceBalance': 0.0}, '600030.SH': {'componentExchID': 'SH', 'componentCode': '600030', 'componentVolume': 3200, 'ReplaceFlag': 49, 'ReplaceRatio': 0.1, 'ReplaceBalance': 0.0}, '600031.SH': {'componentExchID': 'SH', 'componentCode': '600031', 'componentVolume': 2000, 'ReplaceFlag': 49, 'ReplaceRatio': 0.1, 'ReplaceBalance': 0.0}, '600036.SH': {'componentExchID': 'SH', 'componentCode': '600036', 'componentVolume': 4100, 'ReplaceFlag': 49, 'ReplaceRatio': 0.1, 'ReplaceBalance': 0.0}, '600048.SH': {'componentExchID': 'SH', 'componentCode': '600048', 'componentVolume': 2400, 'ReplaceFlag': 49, 'ReplaceRatio': 0.1, 'ReplaceBalance': 0.0}, '600050.SH': {'componentExchID': 'SH', 'componentCode': '600050', 'componentVolume': 6300, 'ReplaceFlag': 49, 'ReplaceRatio': 0.1, 'ReplaceBalance': 0.0}, '600089.SH': {'componentExchID': 'SH', 'componentCode': '600089', 'componentVolume': 1700, 'ReplaceFlag': 49, 'ReplaceRatio': 0.1, 'ReplaceBalance': 0.0}, '600104.SH': {'componentExchID': 'SH', 'componentCode': '600104', 'componentVolume': 1500, 'ReplaceFlag': 49, 'ReplaceRatio': 0.1, 'ReplaceBalance': 0.0}, '600111.SH': {'componentExchID': 'SH', 'componentCode': '600111', 'componentVolume': 800, 'ReplaceFlag': 49, 'ReplaceRatio': 0.1, 'ReplaceBalance': 0.0}, '600150.SH': {'componentExchID': 'SH', 'componentCode': '600150', 'componentVolume': 700, 'ReplaceFlag': 49, 'ReplaceRatio': 0.1, 'ReplaceBalance': 0.0}, '600276.SH': {'componentExchID': 'SH', 'componentCode': '600276', 'componentVolume': 1500, 'ReplaceFlag': 49, 'ReplaceRatio': 0.1, 'ReplaceBalance': 0.0}, '600309.SH': {'componentExchID': 'SH', 'componentCode': '600309', 'componentVolume': 600, 'ReplaceFlag': 49, 'ReplaceRatio': 0.1, 'ReplaceBalance': 0.0}, '600406.SH': {'componentExchID': 'SH', 'componentCode': '600406', 'componentVolume': 1300, 'ReplaceFlag': 49, 'ReplaceRatio': 0.1, 'ReplaceBalance': 0.0}, '600436.SH': {'componentExchID': 'SH', 'componentCode': '600436', 'componentVolume': 100, 'ReplaceFlag': 49, 'ReplaceRatio': 0.1, 'ReplaceBalance': 0.0}, '600438.SH': {'componentExchID': 'SH', 'componentCode': '600438', 'componentVolume': 900, 'ReplaceFlag': 49, 'ReplaceRatio': 0.1, 'ReplaceBalance': 0.0}, '600519.SH': {'componentExchID': 'SH', 'componentCode': '600519', 'componentVolume': 200, 'ReplaceFlag': 49, 'ReplaceRatio': 0.1, 'ReplaceBalance': 0.0}, '600690.SH': {'componentExchID': 'SH', 'componentCode': '600690', 'componentVolume': 1300, 'ReplaceFlag': 49, 'ReplaceRatio': 0.1, 'ReplaceBalance': 0.0}, '600809.SH': {'componentExchID': 'SH', 'componentCode': '600809', 'componentVolume': 200, 'ReplaceFlag': 49, 'ReplaceRatio': 0.1, 'ReplaceBalance': 0.0}, '600887.SH': {'componentExchID': 'SH', 'componentCode': '600887', 'componentVolume': 2100, 'ReplaceFlag': 49, 'ReplaceRatio': 0.1, 'ReplaceBalance': 0.0}, '600893.SH': {'componentExchID': 'SH', 'componentCode': '600893', 'componentVolume': 400, 'ReplaceFlag': 49, 'ReplaceRatio': 0.1, 'ReplaceBalance': 0.0}, '600900.SH': {'componentExchID': 'SH', 'componentCode': '600900', 'componentVolume': 3200, 'ReplaceFlag': 49, 'ReplaceRatio': 0.1, 'ReplaceBalance': 0.0}, '600905.SH': {'componentExchID': 'SH', 'componentCode': '600905', 'componentVolume': 4800, 'ReplaceFlag': 49, 'ReplaceRatio': 0.1, 'ReplaceBalance': 0.0}, '601012.SH': {'componentExchID': 'SH', 'componentCode': '601012', 'componentVolume': 2000, 'ReplaceFlag': 49, 'ReplaceRatio': 0.1, 'ReplaceBalance': 0.0}, '601088.SH': {'componentExchID': 'SH', 'componentCode': '601088', 'componentVolume': 1100, 'ReplaceFlag': 49, 'ReplaceRatio': 0.1, 'ReplaceBalance': 0.0}, '601166.SH': {'componentExchID': 'SH', 'componentCode': '601166', 'componentVolume': 4800, 'ReplaceFlag': 49, 'ReplaceRatio': 0.1, 'ReplaceBalance': 0.0}, '601225.SH': {'componentExchID': 'SH', 'componentCode': '601225', 'componentVolume': 1300, 'ReplaceFlag': 49, 'ReplaceRatio': 0.1, 'ReplaceBalance': 0.0}, '601288.SH': {'componentExchID': 'SH', 'componentCode': '601288', 'componentVolume': 10600, 'ReplaceFlag': 49, 'ReplaceRatio': 0.1, 'ReplaceBalance': 0.0}, '601318.SH': {'componentExchID': 'SH', 'componentCode': '601318', 'componentVolume': 3600, 'ReplaceFlag': 49, 'ReplaceRatio': 0.1, 'ReplaceBalance': 0.0}, '601390.SH': {'componentExchID': 'SH', 'componentCode': '601390', 'componentVolume': 3400, 'ReplaceFlag': 49, 'ReplaceRatio': 0.1, 'ReplaceBalance': 0.0}, '601398.SH': {'componentExchID': 'SH', 'componentCode': '601398', 'componentVolume': 11600, 'ReplaceFlag': 49, 'ReplaceRatio': 0.1, 'ReplaceBalance': 0.0}, '601601.SH': {'componentExchID': 'SH', 'componentCode': '601601', 'componentVolume': 1100, 'ReplaceFlag': 49, 'ReplaceRatio': 0.1, 'ReplaceBalance': 0.0}, '601628.SH': {'componentExchID': 'SH', 'componentCode': '601628', 'componentVolume': 600, 'ReplaceFlag': 49, 'ReplaceRatio': 0.1, 'ReplaceBalance': 0.0}, '601633.SH': {'componentExchID': 'SH', 'componentCode': '601633', 'componentVolume': 400, 'ReplaceFlag': 49, 'ReplaceRatio': 0.1, 'ReplaceBalance': 0.0}, '601668.SH': {'componentExchID': 'SH', 'componentCode': '601668', 'componentVolume': 6900, 'ReplaceFlag': 49, 'ReplaceRatio': 0.1, 'ReplaceBalance': 0.0}, '601669.SH': {'componentExchID': 'SH', 'componentCode': '601669', 'componentVolume': 2900, 'ReplaceFlag': 49, 'ReplaceRatio': 0.1, 'ReplaceBalance': 0.0}, '601728.SH': {'componentExchID': 'SH', 'componentCode': '601728', 'componentVolume': 5200, 'ReplaceFlag': 49, 'ReplaceRatio': 0.1, 'ReplaceBalance': 0.0}, '601857.SH': {'componentExchID': 'SH', 'componentCode': '601857', 'componentVolume': 3800, 'ReplaceFlag': 49, 'ReplaceRatio': 0.1, 'ReplaceBalance': 0.0}, '601888.SH': {'componentExchID': 'SH', 'componentCode': '601888', 'componentVolume': 300, 'ReplaceFlag': 49, 'ReplaceRatio': 0.1, 'ReplaceBalance': 0.0}, '601899.SH': {'componentExchID': 'SH', 'componentCode': '601899', 'componentVolume': 5500, 'ReplaceFlag': 49, 'ReplaceRatio': 0.1, 'ReplaceBalance': 0.0}, '601919.SH': {'componentExchID': 'SH', 'componentCode': '601919', 'componentVolume': 2100, 'ReplaceFlag': 49, 'ReplaceRatio': 0.1, 'ReplaceBalance': 0.0}, '601988.SH': {'componentExchID': 'SH', 'componentCode': '601988', 'componentVolume': 6900, 'ReplaceFlag': 49, 'ReplaceRatio': 0.1, 'ReplaceBalance': 0.0}, '603259.SH': {'componentExchID': 'SH', 'componentCode': '603259', 'componentVolume': 700, 'ReplaceFlag': 49, 'ReplaceRatio': 0.1, 'ReplaceBalance': 0.0}, '603288.SH': {'componentExchID': 'SH', 'componentCode': '603288', 'componentVolume': 600, 'ReplaceFlag': 49, 'ReplaceRatio': 0.1, 'ReplaceBalance': 0.0}, '603501.SH': {'componentExchID': 'SH', 'componentCode': '603501', 'componentVolume': 200, 'ReplaceFlag': 49, 'ReplaceRatio': 0.1, 'ReplaceBalance': 0.0}, '603799.SH': {'componentExchID': 'SH', 'componentCode': '603799', 'componentVolume': 500, 'ReplaceFlag': 49, 'ReplaceRatio': 0.1, 'ReplaceBalance': 0.0}, '603986.SH': {'componentExchID': 'SH', 'componentCode': '603986', 'componentVolume': 200, 'ReplaceFlag': 49, 'ReplaceRatio': 0.1, 'ReplaceBalance': 0.0}, '688041.SH': {'componentExchID': 'SH', 'componentCode': '688041', 'componentVolume': 308, 'ReplaceFlag': 49, 'ReplaceRatio': 0.1, 'ReplaceBalance': 0.0}, '688111.SH': {'componentExchID': 'SH', 'componentCode': '688111', 'componentVolume': 77, 'ReplaceFlag': 50, 'ReplaceRatio': 0.0, 'ReplaceBalance': 23582.79}, '688599.SH': {'componentExchID': 'SH', 'componentCode': '688599', 'componentVolume': 363, 'ReplaceFlag': 49, 'ReplaceRatio': 0.1, 'ReplaceBalance': 0.0}, '688981.SH': {'componentExchID': 'SH', 'componentCode': '688981', 'componentVolume': 656, 'ReplaceFlag': 49, 'ReplaceRatio': 0.1, 'ReplaceBalance': 0.0}}}
```

### get_etf_iopv - 根据ETF基金代码获取ETF的基金份额参考净值

**原型**

```py
get_etf_iopv(stockcode)
```

**释义**

根据ETF基金代码获取ETF的基金份额参考净值

**参数**

| 字段名 | 数据类型 | 解释 |
| --- | --- | --- |
| `stockcode` | `string` | ETF基金代码如"510050.SH" |

**返回值**

`float`类型值,IOPV，基金份额参考净值

**示例**

示例与返回值

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

### ContextInfo.get_local_data - 获取本地行情数据【不推荐】

注意

本函数用于仅用于获取本地历史行情数据，使用前请确保已通过 [download_history_data](data_function.md#download-history-data-%E4%B8%8B%E8%BD%BD%E6%8C%87%E5%AE%9A%E5%90%88%E7%BA%A6%E4%BB%A3%E7%A0%81%E6%8C%87%E5%AE%9A%E5%91%A8%E6%9C%9F%E5%AF%B9%E5%BA%94%E6%97%B6%E9%97%B4%E8%8C%83%E5%9B%B4%E7%9A%84%E8%A1%8C%E6%83%85%E6%95%B0%E6%8D%AE) 下载过历史行情数据

**原型**

```py
ContextInfo.get_local_data(
    stock_code,
    start_time='',
    end_time='',
    period='1d',
    divid_type='none',
    count=-1)
```

**释义**

获取本地行情数据

**参数**

| 字段名 | 数据类型 | 解释 |
| --- | --- | --- |
| `stock_code` | `string` | 默认参数，合约代码格式为 `code.market`，不指定时为当前图合约 |
| `start_time` | `string` | 默认参数，开始时间，格式为 '20171209' 或 '20171209010101' |
| `end_time` | `string` | 默认参数，结束时间，格式同 `start_time` |
| `period` | `string` | 默认参数，K线类型，可选值包括：<br>`'tick'`：分笔线（只用于获取'quoter'字段数据）、`'realtime'`: 实时线、`'1d'`：日线<br>`'md'`：多日线、`'1m'`：1分钟线、`'3m'`：3分钟线<br>`'5m'`：5分钟线、`'15m'`：15分钟线、`'30m'`：30分钟线<br>`'mm'`：多分钟线、`'1h'`：小时线、`'mh'`：多小时线<br>`'1w'`：周线、`'1mon'`：月线、`'1q'`：季线<br>`'1hy'`：半年线、`'1y'`：年线 |
| `dividend_type` | `string` | 除复权种类，可选值：<br>`'none'`：不复权<br>`'front'`：向前复权<br>`'back'`：向后复权<br>`'front_ratio'`：等比向前复权<br>`'back_ratio'`：等比向后复权 |
| `count` | `int` | 当 `count` 大于等于0时：<br> 如果指定了 `start_time` 和 `end_time`，则以 `end_time` 为基准向前取 `count` 条数据；<br> 如果 `start_time` 和 `end_time` 缺省，则默认取本地数据最新的 `count` 条数据；<br> 如果 `start_time`、`end_time` 和 `count` 都缺省时，则默认取本地全部数据。 |

**返回值**

返回一个`dict`，键值为timetag，value为另一个dict(valuedict)

- period='tick'时函数获取分笔数据，valuedict字典数据key值有：

| 字段 | 数据类型 | 含义 |
| --- | --- | --- |
| `lastPrice` | `float` | `最新价` |
| `open` | `float` | `开盘价` |
| `high` | `float` | `最高价` |
| `low` | `float` | `最低价` |
| `lastClose` | `float` | `前收盘价` |
| `amount` | `float` | `成交额` |
| `volume` | `float` | `成交量` |
| `pvolume` | `float` | `原始成交量` |
| `stockStatus` | `int` | `作废 参考openInt` |
| `openInt` | `float` | `若是股票，则openInt含义为股票状态，非股票则是持仓量` [openInt字段说明](data_structure.md#openint-%E8%AF%81%E5%88%B8%E7%8A%B6%E6%80%81) |
| `lastSettlementPrice` | `float` | `昨结算价` |
| `askPrice` | `list` | `委卖价` |
| `bidPrice` | `list` | `委买价` |
| `askVol` | `list` | `委卖量` |
| `bidVol` | `list` | `委买量` |
| `settlementPrice` | `float` | `今结算价` |

- period为其他值时，valuedict字典数据key值有：

| 字段名 | 数据类型 | 解释 |
| --- | --- | --- |
| `amount` | `float` | 成交额 |
| `volume` | `float` | 成交量 |
| `open` | `float` | 开盘价 |
| `high` | `float` | 最高价 |
| `low` | `float` | 最低价 |
| `close` | `float` | 收盘价 |

**示例**

示例与返回值

```py
# coding:gbk
def init(C):
	pass

def handlebar(C):
	data = C.get_local_data(stock_code='600000.SH',start_time='20220101',end_time='20220131',period='1d',divid_type='none')
	print(data)
```

```
{1641225600000: {'open': 8.54, 'high': 8.58, 'low': 8.52, 'close': 8.57, 'volume': 377076, 'amount': 322145532.0}, 1641312000000: {'open': 8.57, 'high': 8.68, 'low': 8.56, 'close': 8.64, 'volume': 554591, 'amount': 478834470.0}, 1641398400000: {'open': 8.66, 'high': 8.66, 'low': 8.56, 'close': 8.57, 'volume': 410311, 'amount': 352720656.0}, 1641484800000: {'open': 8.57, 'high': 8.73, 'low': 8.57, 'close': 8.71, 'volume': 630183, 'amount': 546456194.0}, 1641744000000: {'open': 8.72, 'high': 8.78, 'low': 8.66, 'close': 8.72, 'volume': 340553, 'amount': 296601230.0}, 1641830400000: {'open': 8.74, 'high': 8.78, 'low': 8.69, 'close': 8.73, 'volume': 426461, 'amount': 373093384.0}, 1641916800000: {'open': 8.75, 'high': 8.75, 'low': 8.63, 'close': 8.69, 'volume': 412407, 'amount': 358535694.0}, 1642003200000: {'open': 8.73, 'high': 8.85, 'low': 8.69, 'close': 8.72, 'volume': 489237, 'amount': 429003208.0}, 1642089600000: {'open': 8.72, 'high': 8.72, 'low': 8.57, 'close': 8.59, 'volume': 510607, 'amount': 440215953.0}, 1642348800000: {'open': 8.57, 'high': 8.63, 'low': 8.57, 'close': 8.57, 'volume': 221780, 'amount': 190459847.0}, 1642435200000: {'open': 8.58, 'high': 8.66, 'low': 8.55, 'close': 8.63, 'volume': 399952, 'amount': 344181260.0}, 1642521600000: {'open': 8.63, 'high': 8.66, 'low': 8.61, 'close': 8.64, 'volume': 262577, 'amount': 226931297.0}, 1642608000000: {'open': 8.66, 'high': 8.82, 'low': 8.64, 'close': 8.8, 'volume': 828420, 'amount': 724160483.0}, 1642694400000: {'open': 8.78, 'high': 8.8, 'low': 8.72, 'close': 8.76, 'volume': 475725, 'amount': 416684184.0}, 1642953600000: {'open': 8.79, 'high': 8.79, 'low': 8.66, 'close': 8.69, 'volume': 324897, 'amount': 282465419.0}, 1643040000000: {'open': 8.68, 'high': 8.68, 'low': 8.56, 'close': 8.56, 'volume': 433124, 'amount': 372488759.0}, 1643126400000: {'open': 8.57, 'high': 8.59, 'low': 8.54, 'close': 8.57, 'volume': 234820, 'amount': 201130974.0}, 1643212800000: {'open': 8.55, 'high': 8.56, 'low': 8.45, 'close': 8.45, 'volume': 562810, 'amount': 477716811.0}, 1643299200000: {'open': 8.48, 'high': 8.51, 'low': 8.41, 'close': 8.41, 'volume': 439938, 'amount': 372256637.0}}
```

### ContextInfo.get_history_data - 获取历史行情数据【不推荐】

警告

1. 此函数已不推荐使用，推荐使用 [ContextInfo.get_market_data_ex()](data_function.md#contextinfo-get-market-data-ex-%E8%8E%B7%E5%8F%96%E8%A1%8C%E6%83%85%E6%95%B0%E6%8D%AE)
2. 此函数使用前需要先通过 [ContextInfo.set_universe()](data_function.md) 设定股票池

**原型**

```py
ContextInfo.get_history_data(
    len,
    period,
    field,
    dividend_type = 0,
    skip_paused = True)
```

**释义**

获取历史行情数据

**参数**

| 名称 | 类型 | 描述 |
| --- | --- | --- |
| `len` | `int` | `需获取的历史数据长度` |
| `period` | `string` | 需获取的历史数据周期，可选值包括：<br>`'tick'`：分笔线、 `'1d'`：日线、 `'1m'`：1分钟线<br>`'3m'`：3分钟线、 `'5m'`：5分钟线、 `'15m'`：15分钟线<br>`'30m'`：30分钟线、 `'1h'`：小时线、 `'1w'`：周线<br>`'1mon'`：月线、 `'1q'`：季线、 `'1hy'`：半年线<br>`'1y'`：年线 |
| `field` | `string` | 需获取的历史数据的类型，可选值包括：<br>`'open'`：开盘价<br>`'high'`：最高价<br>`'low'`：最低价<br>`'close'`：收盘价<br>`'quoter'`：详细报价（结构见 `get_market_data` 方法） |
| `dividend_type` | `int` | 默认参数，除复权，默认不复权，可选值包括：<br>`0`：不复权<br>`1`：向前复权<br>`2`：向后复权<br>`3`：等比向前复权<br>`4`：等比向后复权 |
| `skip_paused` | `bool` | 默认参数，是否停牌填充，默认填充 |

**返回值** 一个字典`dict`结构，key 为 stockcode.market, value 为行情数据 list，list 中第 0 位为最早的价格，第 1 位为次早价格，依次下去。

**示例**

示例与返回值

```py
# coding = gbk
def init(C):
	C.stock_list = ["000001.SZ","600519.SH", "510050.SH"]
	C.set_universe(C.stock_list)

def handlebar(C):
	data = C.get_history_data(2, '1d', 'close')
	print(data)
```

```
{'000001.SZ': [10.41, 10.41], '510050.SH': [2.492, 2.492], '600519.SH': [1683.02, 1683.02]}
{'000001.SZ': [10.41, 10.41], '510050.SH': [2.492, 2.492], '600519.SH': [1683.02, 1790.6000000000001]}
{'000001.SZ': [10.41, 10.61], '510050.SH': [2.492, 2.521], '600519.SH': [1683.02, 1790.94]}
{'000001.SZ': [10.41, 10.620000000000001], '510050.SH': [2.492, 2.52], '600519.SH': [1683.02, 1790.94]}
{'000001.SZ': [10.41, 10.620000000000001], '510050.SH': [2.492, 2.521], '600519.SH': [1683.02, 1790.99]}
{'000001.SZ': [10.41, 10.620000000000001], '510050.SH': [2.492, 2.521], '600519.SH': [1683.02, 1791.1000000000001]}
{'000001.SZ': [10.41, 10.620000000000001], '510050.SH': [2.492, 2.521], '600519.SH': [1683.02, 1791.1000000000001]}
{'000001.SZ': [10.41, 10.620000000000001], '510050.SH': [2.492, 2.521], '600519.SH': [1683.02, 1791.0]}
```

### - 获取行情数据【不推荐】

提示

推荐使用 [ContextInfo.get_market_data_ex()](data_function.md#contextinfo-get-market-data-ex-%E8%8E%B7%E5%8F%96%E8%A1%8C%E6%83%85%E6%95%B0%E6%8D%AE)

**原型**

```py
ContextInfo.get_market_data(
    fields,
    stock_code = [],
    start_time = '',
    end_time = '',
    skip_paused = True,
    period = 'follow',
    dividend_type = 'follow',
    count = -1)
```

**释义**

获取行情数据

**参数**

| 字段名 | 数据类型 | 解释 |
| --- | --- | --- |
| `fields` | 字段列表 | 可选值包括：<br>`'open'`: 开<br>`'high'`: 高<br>`'low'`: 低<br>`'close'`: 收<br>`'volume'`: 成交量<br>`'amount'`: 成交额<br>`'settle'`: 结算价<br>`'quoter'`: 分笔数据（包括历史） |
| `stock_code` | 默认参数，合约代码列表 | 合约格式为 `code.market`，例如 '600000.SH'，不指定时为当前图合约 |
| `start_time` | 默认参数，时间戳 | 开始时间，格式为 '20171209' 或 '20171209010101' |
| `end_time` | 默认参数，时间戳 | 结束时间，格式为 '20171209' 或 '20171209010101' |
| `skip_paused` | 默认参数，布尔值 | 如何处理停牌数据：<br>`true`：如果是停牌股，会自动填充未停牌前的价格作为停牌日的价格<br>`false`：停牌数据为 NaN |
| `period` | `string` | 需获取的历史数据周期，可选值包括：<br>`'tick'`：分笔线、 `'1d'`：日线、 `'1m'`：1分钟线<br>`'3m'`：3分钟线、 `'5m'`：5分钟线、 `'15m'`：15分钟线<br>`'30m'`：30分钟线、 `'1h'`：小时线、 `'1w'`：周线<br>`'1mon'`：月线、 `'1q'`：季线、 `'1hy'`：半年线<br>`'1y'`：年线 |
| `dividend_type` | 默认参数，字符串 | 缺省值为 'none'，除复权，可选值包括：<br>`'none'`：不复权<br>`'front'`：向前复权<br>`'back'`：向后复权<br>`'front_ratio'`：等比向前复权<br>`'back_ratio'`：等比向后复权 |
| `count` | 默认参数，整数 | 缺省值为 -1。当大于等于 0 时，效果与 `get_history_data` 保持一致 |

- count参数设置的几种情况

| count 取值 | 时间设置是否生效 | 开始时间和结束时间设置效果 |
| --- | --- | --- |
| count >= 0 | **生效** | 返回数量取决于开始时间与结束时间和count与结束时间的交集 |
| count = -1 | **生效** | 同时设置开始时间和结束时间，在所设置的时间段内取值 |
| count = -1 | **生效** | 开始时间结束时间都不设置，取当前最新bar的值 |
| count = -1 | **生效** | 只设置开始时间，取所设开始时间到当前时间的值 |
| count = -1 | **生效** | 只设置结束时间，取股票上市第一根 bar 到所设结束时间的值 |

**返回值**

- 返回值根据传入的参数情况，会返回不同类型的结果

| count | 字段数量 | 股票数量 | 时间点 | 返回类型 |
| --- | --- | --- | --- | --- |
| =-1 | =1 | =1 | =1 | float |
| =-1 | >1 | =1 | 默认值 | pandas.Series |
| >=-1 | >=1 | =1 | >=1 | pandas.DataFrame(字段数量和时间点不同时为1) |
| =-1 | >=1 | >1 | 默认值 | pandas.DataFrame |
| >1 | =1 | =1 | =1 | pandas.DataFrame |
| >=-1 | >=1 | >1 | >=1 | pandas.Panel |

**示例**

示例data1返回值data2返回值data3返回值data4返回值

```
# coding = gbk
def init(C):
    C.stock_list = ["000001.SZ","600519.SH", "510050.SH"]

def handlebar(C):
    data1 = C.get_market_data(["close"],["000001.SZ"],start_time = "20231106",end_time = "20231106", count = -1) # 返回float值
    data2 = C.get_market_data(["close","open"],["000001.SZ"], count = -1) # 返回pandas.Series
    data3 = C.get_market_data(["close","open"],C.stock_list, count = -1) # 返回pandas.DataFrame
    data4 = C.get_market_data(["open","high", "low", "close"],C.stock_list,count = 20) # 返回pandas.Panel

    print(data1)
    print(data2)
    print(data3)
    print(data4)
```

```
10.69
```

```
close    10.60
open     10.66
dtype: float64
```

```
              close      open
000001.SZ    10.590    10.660
600519.SH  1794.000  1805.000
510050.SH     2.522     2.528
```

```
Dimensions: 3 (items) x 20 (major_axis) x 4 (minor_axis)
Items axis: 000001.SZ to 600519.SH
Major_axis axis: 20231011 to 20231107
Minor_axis axis: open to close
<class 'pandas.core.panel.Panel'>
```

## 获取财务数据

获取财务数据前，请先通过`界面端数据管理 - 财务数据`下载

![财务数据下载](https://dict.thinktrader.net/assets/%E5%86%85%E7%BD%AEAPI_%E4%B8%8B%E8%BD%BD%E8%B4%A2%E5%8A%A1%E6%95%B0%E6%8D%AE-61e927b9.png)

提示

财务数据接口通过读取下载本地的数据取数，使用前需要补充本地数据。除公告日期和报表截止日期为时间戳毫秒格式其他单位为元或 %，数据主要包括资产负债表(ASHAREBALANCESHEET)、利润表（ASHAREINCOME）、现金流量表（ASHARECASHFLOW）、股本表（CAPITALSTRUCTURE）的主要字段数据以及经过计算的主要财务指标数据（PERSHAREINDEX）。建议使用本文档对照表中的英文表名和迅投英文字段，表名不区分大小写。

### ContextInfo.get_financial_data - 获取财务数据

财务数据接口有两种用法，入参和返回值不同，具体如下

#### 用法1

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

报告日期是指财务报告所覆盖的会计时间段，而公告日期是指公司向外界公布该报告的具体时间点

若指定report_type为`report_time`，则不会考虑财报的公告日期， **可能会取到未来数据**

若指定report_type为`announce_time`，则会按财报实际发布日期返回数据， **不会取到未来数据**

例：

**返回值**

函数根据stockList代码列表,startDate,endDate时间范围，返回不同的的数据类型。如下：

| 代码数量 | 时间范围 | 返回类型 |
| --- | --- | --- |
| =1 | =1 | pandas.Series (index = 字段) |
| =1 | >1 | pandas.DataFrame (index = 时间, columns = 字段) |
| >1 | =1 | pandas.DataFrame (index = 代码, columns = 字段) |
| >1 | >1 | pandas.Panel (items = 代码, major_axis = 时间, minor_axis = 字段) |

**示例**

示例与返回值

```py
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

#### 用法2

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

示例与返回值

```py
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

### ContextInfo.get_raw_financial_data - 获取原始财务数据

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

示例与返回值

```py
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

### ContextInfo.get_last_volume - 获取最新流通股本

**原型**

```py
ContextInfo.get_last_volume(stockcode)
```

**释义**

获取最新流通股本

**参数**

| 字段名 | 数据类型 | 解释 |
| --- | --- | --- |
| `stockcode` | `string` | 标的名称，必须是 'stock.market' 形式 |

**返回值**

`int`类型值,代表流通股本数量

**示例**

示例与返回值

```py
# coding:gbk
def init(C):
	pass

def handlebar(C):
	data = C.get_last_volume("000001.SZ")
	print(data)
```

```
19405546950
```

### ContextInfo.get_total_share - 获取总股数

**原型**

```py
ContextInfo.get_total_share(stockcode)
```

**释义**

获取总股数

**参数**

| 字段名 | 数据类型 | 解释 |
| --- | --- | --- |
| `stockcode` | `string` | 股票代码，缺省值 ''，默认为当前图代码, 如：'600000.SH' |

**返回值**

`int`:总股数

**示例**

示例与返回值

```py
# coding:gbk
def init(C):
	pass

def handlebar(C):
	data = C.get_total_share('600000.SH')
	print(data)
```

```
29352176396
```

### 财务数据字段表

#### 资产负债表 (ASHAREBALANCESHEET)

| **中文字段** | **迅投字段** |
| --- | --- |
| `应收利息` | `int_rcv` |
| `可供出售金融资产` | `fin_assets_avail_for_sale` |
| `持有至到期投资` | `held_to_mty_invest` |
| `长期股权投资` | `long_term_eqy_invest` |
| `固定资产` | `fix_assets` |
| `无形资产` | `intang_assets` |
| `递延所得税资产` | `deferred_tax_assets` |
| `资产总计` | `tot_assets` |
| `交易性金融负债` | `tradable_fin_liab` |
| `应付职工薪酬` | `empl_ben_payable` |
| `应交税费` | `taxes_surcharges_payable` |
| `应付利息` | `int_payable` |
| `应付债券` | `bonds_payable` |
| `递延所得税负债` | `deferred_tax_liab` |
| `负债合计` | `tot_liab` |
| `实收资本(或股本)` | `cap_stk` |
| `资本公积金` | `cap_rsrv` |
| `盈余公积金` | `surplus_rsrv` |
| `未分配利润` | `undistributed_profit` |
| `归属于母公司股东权益合计` | `tot_shrhldr_eqy_excl_min_int` |
| `少数股东权益` | `minority_int` |
| `负债和股东权益总计` | `tot_liab_shrhldr_eqy` |
| `所有者权益合计` | `total_equity` |
| `货币资金` | `cash_equivalents` |
| `应收票据` | `bill_receivable` |
| `应收账款` | `account_receivable` |
| `预付账款` | `advance_payment` |
| `其他应收款` | `other_receivable` |
| `其他流动资产` | `other_current_assets` |
| `流动资产合计` | `total_current_assets` |
| `存货` | `inventories` |
| `在建工程` | `constru_in_process` |
| `工程物资` | `construction_materials` |
| `长期待摊费用` | `long_deferred_expense` |
| `非流动资产合计` | `total_non_current_assets` |
| `短期借款` | `shortterm_loan` |
| `应付股利` | `dividend_payable` |
| `其他应付款` | `other_payable` |
| `一年内到期的非流动负债` | `non_current_liability_in_one_year` |
| `其他流动负债` | `other_current_liability` |
| `长期应付款` | `longterm_account_payable` |
| `应付账款` | `accounts_payable` |
| `预收账款` | `advance_peceipts` |
| `流动负债合计` | `total_current_liability` |
| `应付票据` | `notes_payable` |
| `长期借款` | `long_term_loans` |
| `专项应付款` | `grants_received` |
| `其他非流动负债` | `other_non_current_liabilities` |
| `非流动负债合计` | `non_current_liabilities` |
| `专项储备` | `specific_reserves` |
| `商誉` | `goodwill` |
| `报告截止日` | `m_timetag` |
| `公告日` | `m_anntime` |

#### 利润表 (ASHAREINCOME)

| **中文字段** | **迅投字段** |
| --- | --- |
| `投资收益` | `plus_net_invest_inc` |
| `联营企业和合营企业的投资收益` | `incl_inc_invest_assoc_jv_entp` |
| `营业税金及附加` | `less_taxes_surcharges_ops` |
| `营业总收入` | `revenue` |
| `营业总成本` | `total_operating_cost` |
| `营业收入` | `revenue_inc` |
| `营业成本` | `total_expense` |
| `资产减值损失` | `less_impair_loss_assets` |
| `营业利润` | `oper_profit` |
| `营业外收入` | `plus_non_oper_rev` |
| `营业外支出` | `less_non_oper_exp` |
| `利润总额` | `tot_profit` |
| `所得税` | `inc_tax` |
| `净利润` | `net_profit_incl_min_int_inc` |
| `归母净利润` | `net_profit_excl_min_int_inc` |
| `管理费用` | `less_gerl_admin_exp` |
| `销售费用` | `sale_expense` |
| `财务费用` | `financial_expense` |
| `综合收益总额` | `total_income` |
| `归属于少数股东的综合收益总额` | `total_income_minority` |
| `公允价值变动收益` | `change_income_fair_value` |
| `已赚保费` | `earned_premium` |
| `报告截止日` | `m_timetag` |
| `公告日` | `m_anntime` |

#### 现金流量表 (ASHARECASHFLOW)

| **中文字段** | **迅投字段** |
| --- | --- |
| `收到其他与经营活动有关的现金` | `other_cash_recp_ral_oper_act` |
| `经营活动现金流入小计` | `stot_cash_inflows_oper_act` |
| `支付给职工以及为职工支付的现金` | `cash_pay_beh_empl` |
| `支付的各项税费` | `pay_all_typ_tax` |
| `支付其他与经营活动有关的现金` | `other_cash_pay_ral_oper_act` |
| `经营活动现金流出小计` | `stot_cash_outflows_oper_act` |
| `经营活动产生的现金流量净额` | `net_cash_flows_oper_act` |
| `取得投资收益所收到的现金` | `cash_recp_return_invest` |
| `处置固定资产、无形资产和其他长期投资收到的现金` | `net_cash_recp_disp_fiolta` |
| `投资活动现金流入小计` | `stot_cash_inflows_inv_act` |
| `投资支付的现金` | `cash_paid_invest` |
| `购建固定资产、无形资产和其他长期投资支付的现金` | `cash_pay_acq_const_fiolta` |
| `支付其他与投资的现金` | `other_cash_pay_ral_inv_act` |
| `投资活动产生的现金流出小计` | `stot_cash_outflows_inv_act` |
| `投资活动产生的现金流量净额` | `net_cash_flows_inv_act` |
| `吸收投资收到的现金` | `cash_recp_cap_contrib` |
| `取得借款收到的现金` | `cash_recp_borrow` |
| `收到其他与筹资活动有关的现金` | `other_cash_recp_ral_fnc_act` |
| `筹资活动现金流入小计` | `stot_cash_inflows_fnc_act` |
| `偿还债务支付现金` | `cash_prepay_amt_borr` |
| `分配股利、利润或偿付利息支付的现金` | `cash_pay_dist_dpcp_int_exp` |
| `支付其他与筹资的现金` | `other_cash_pay_ral_fnc_act` |
| `筹资活动现金流出小计` | `stot_cash_outflows_fnc_act` |
| `筹资活动产生的现金流量净额` | `net_cash_flows_fnc_act` |
| `汇率变动对现金的影响` | `eff_fx_flu_cash` |
| `现金及现金等价物净增加额` | `net_incr_cash_cash_equ` |
| `销售商品、提供劳务收到的现金` | `goods_sale_and_service_render_cash` |
| `收到的税费与返还` | `tax_levy_refund` |
| `购买商品、接受劳务支付的现金` | `goods_and_services_cash_paid` |
| `处置子公司及其他收到的现金` | `net_cash_deal_subcompany` |
| `其中子公司吸收现金` | `cash_from_mino_s_invest_sub` |
| `处置固定资产、无形资产和其他长期资产支付的现金净额` | `fix_intan_other_asset_dispo_cash_payment` |
| `报告截止日` | `m_timetag` |
| `公告日` | `m_anntime` |

#### 股本表 (CAPITALSTRUCTURE)

| **中文字段** | **迅投字段** |
| --- | --- |
| `总股本` | `total_capital` |
| `已上市流通A股` | `circulating_capital` |
| `自由流通股本` | `free_float_capital`（旧版本为`freeFloatCapital`） |
| `限售流通股份` | `restrict_circulating_capital` |
| `变动日期` | `m_timetag` |
| `公告日` | `m_anntime` |

#### 主要指标 (PERSHAREINDEX)

| **中文字段** | **迅投字段** |
| --- | --- |
| `每股经营活动现金流量` | `s_fa_ocfps` |
| `每股净资产` | `s_fa_bps` |
| `基本每股收益` | `s_fa_eps_basic` |
| `稀释每股收益` | `s_fa_eps_diluted` |
| `每股未分配利润` | `s_fa_undistributedps` |
| `每股资本公积金` | `s_fa_surpluscapitalps` |
| `扣非每股收益` | `adjusted_earnings_per_share` |
| `净资产收益率` | `du_return_on_equity` |
| `销售毛利率` | `sales_gross_profit` |
| `主营收入同比增长` | `inc_revenue_rate` |
| `净利润同比增长` | `du_profit_rate` |
| `归属于母公司所有者的净利润同比增长` | `inc_net_profit_rate` |
| `扣非净利润同比增长` | `adjusted_net_profit_rate` |
| `营业总收入滚动环比增长` | `inc_total_revenue_annual` |
| `归属净利润滚动环比增长` | `inc_net_profit_to_shareholders_annual` |
| `扣非净利润滚动环比增长` | `adjusted_profit_to_profit_annual` |
| `加权净资产收益率` | `equity_roe` |
| `摊薄净资产收益率` | `net_roe` |
| `摊薄总资产收益率` | `total_roe` |
| `毛利率` | `gross_profit` |
| `净利率` | `net_profit` |
| `实际税率` | `actual_tax_rate` |
| `预收款营业收入` | `pre_pay_operate_income` |
| `销售现金流营业收入` | `sales_cash_flow` |
| `资产负债比率` | `gear_ratio` |
| `存货周转率` | `inventory_turnover` |

#### 十大股东/十大流通股东 (TOP10HOLDER/TOP10FLOWHOLDER)

提示

对于公告内披露的十大股东数量大于10条的，我们会保留原始数据，以保持和公司公告信息一致

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

#### 股东数 (SHAREHOLDER)

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

## 获取合约信息

### ContextInfo.get_instrument_detail - 根据代码获取合约详细信息

提示：在旧版本客户端中，函数名为`ContextInfo.get_instrumentdetail`，且不支持 `iscomplete` 参数

**原型**

```py
ContextInfo.get_instrument_detail(stockcode,iscomplete = Fasle)
```

**释义**

根据代码获取合约详细信息

**参数**

| 字段名 | 数据类型 | 解释 |
| --- | --- | --- |
| `stockcode` | `string` | 标的名称，必须是 'stock.market' 形式 |
| `iscomplete` | `bool` | 是否获取全部字段，默认为False |

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
| ChargeType | int | 期货和期权手续费方式 |
| ChargeOpen | float | 开仓手续费(率) |
| ChargeClose | float | 平仓手续费(率) |
| ChargeTodayOpen | float | 开今仓(日内开仓)手续费(率) |
| ChargeTodayClose | float | 平今仓(日内平仓)手续费(率) |
| OptionType | int | 期权类型 |
| OpenInterestMultiple | int | 交割月持仓倍数 |

提示

字段`OpenDate`有以下几种特殊值： 19700101=新股, 19700102=老股东增发, 19700103=新债, 19700104=可转债, 19700105=配股， 19700106=配号 字段`ExpireDate`为0 或 99999999 时，表示该标的暂无退市日或到期日

字段`ProductType` 对于 **股票以外** 的品种，有以下几种值

**国内期货市场：** 1-期货 2-期权(DF SF ZF INE GF) 3-组合套利 4-即期 5-期转现 6-期权(IF) 7-结算价交易(tas)

**沪深股票期权市场：**0-认购 1-认沽

**外盘：** 1-100：期货， 101-200：现货, 201-300:股票相关 1：股指期货 2：能源期货 3：农业期货 4：金属期货 5：利率期货 6：汇率期货 7：数字货币期货 99：自定义合约期货 107：数字货币现货 201：股票 202：GDR 203：ETF 204：ETN 300：其他

**示例**

示例与返回值

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

### get_st_status - 获取历史st状态

提示

本函数需要下载历史ST数据(过期合约K线),可通过`界面端数据管理 - 过期合约数据`下载

**原型**

```py
get_st_status(stockcode)
```

**释义**

获取历史st状态

**参数**

| 字段名 | 数据类型 | 解释 |
| --- | --- | --- |
| `stockcode` | `string` | 股票代码，如000004.SZ（可为空，为空时取主图代码） |

**返回值**

st范围字典 格式 {'ST': [['20210520', '20380119']], '*ST': [['20070427', '20080618'], ['20200611', '20210520']]}

示例：

**示例**

示例与返回值

```py
# coding:gbk
def init(C):
	pass

def handlebar(C):
	print(get_st_status('600599.SH'))
```

```
{'ST': [['20210520', '20380119']], '*ST': [['20070427', '20080618'], ['20200611', '20210520']]}
```

### ContextInfo.get_his_st_data - 获取某只股票ST的历史

提示

本函数需要下载历史ST数据(过期合约K线),可通过`界面端数据管理 - 过期合约数据`下载

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

示例与返回值

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

### ContextInfo.get_main_contract - 获取期货主力合约

提示

1. 该函数支持实盘/回测两种模式
2. 若要使用该函数获取历史主力合约，必须要先下载`历史主力合约`数据
3. `历史主力合约`数据目前通过`界面端数据管理 - 过期合约数据 - 历史主力合约`下载

**原型**

```py
ContextInfo.get_main_contract(codemarket)
ContextInfo.get_main_contract(codemarket,date="")
ContextInfo.get_main_contract(codemarket,startDate="",endDate="")
```

**释义**

获取当前期货主力合约

**参数**

| 字段名 | 数据类型 | 解释 |
| --- | --- | --- |
| `codemarket` | `string` | 合约和市场，合约格式为品种名加00，如IF00.IF，zn00.SF |
| `startDate` | `string` | 开始日期(可以不写),如20180608 |
| `endDate` | `string` | 结束日期(可以不写),如20190608 |

**返回值**

`str`，合约代码

**示例**

示例与返回值

```py
# coding:gbk
def init(C):
	pass

def handlebar(C):
	symbol1 = C.get_main_contract('IF00.IF')# 获取当前主力合约

	symbol2 = C.get_main_contract('IF00.IF',"20190101")# 获取指定日期主力合约

	symbol3 = C.get_main_contract('IF00.IF',"20181101","20190101") # 获取时间段内全部主力合约

	print(symbol1, symbol2)
	print("="*10)
	print(symbol3)
```

```
IF2312
==========
IF1901
==========
1540137600000    IF1811
1545321600000    IF1901
dtype: object
```

### ContextInfo.get_contract_multiplier - 获取合约乘数

**原型**

```py
ContextInfo.get_contract_multiplier(contractcode)
```

**释义**

获取合约乘数

**参数**

| 字段名 | 数据类型 | 解释 |
| --- | --- | --- |
| `contractcode` | `string` | 合约代码，格式为 'code.market'，例如 'IF1707.IF' |

**返回值**`int`,表示合约乘数

**示例**

示例与返回值

```py
# coding:gbk
def init(C):
	pass

def handlebar(C):
	multiplier = C.get_contract_multiplier("rb2401.SF")
	print(multiplier)
```

```
10
```

### ContextInfo.get_contract_expire_date - 获取期货合约到期日

**原型**

```py
ContextInfo.get_contract_expire_date(codemarket)
```

**释义**

获取期货合约到期日

**参数**

| 字段名 | 数据类型 | 解释 |
| --- | --- | --- |
| `Codemarket` | `string` | 合约和市场,如IF00.IF,zn00.SF |

**返回值**`str`，合约到期日

**示例**

示例与返回值

```py
# coding:gbk
def init(C):
	pass

def handlebar(C):
	data = C.get_contract_expire_date("IF2311.IF")
	# print(type(data))
	print(data)
```

```
"20231117"
```

### ContextInfo.get_his_contract_list - 获取市场已退市合约

**原型**

```py
ContextInfo.get_his_contract_list(market)
```

**释义**

获取市场已退市合约，需要手动补充过期合约列表

**参数**

| 字段名 | 数据类型 | 解释 |
| --- | --- | --- |
| `market` | `string` | 市场,SH,SZ,SHO,SZO,IF等 |

**返回值**

`list`,合约代码列表

**示例**

示例与返回值

```py
# coding:gbk
def init(C):
	pass

def handlebar(C):

	print(C.get_his_contract_list('SHO')[:30])
```

```
['10000001.SHO', '10000002.SHO', '10000003.SHO', '10000004.SHO', '10000005.SHO', '10000006.SHO', '10000007.SHO', '10000008.SHO', '10000009.SHO', '10000010.SHO', '10000011.SHO', '10000012.SHO', '10000013.SHO', '10000014.SHO', '10000015.SHO', '10000016.SHO', '10000017.SHO', '10000018.SHO', '10000019.SHO', '10000020.SHO', '10000021.SHO', '10000022.SHO', '10000023.SHO', '10000024.SHO', '10000025.SHO', '10000026.SHO', '10000027.SHO', '10000028.SHO', '10000029.SHO', '10000030.SHO']
```

## 获取期权信息

### ContextInfo.get_option_detail_data - 获取指定期权品种的详细信息

**原型**

```py
ContextInfo.get_option_detail_data(optioncode)
```

**释义**

获取指定期权品种的详细信息

**参数**

| 字段名 | 数据类型 | 解释 |
| --- | --- | --- |
| `optioncode` | `string` | 期权代码,如'10001506.SHO',当填写空字符串时候默认为当前主图的期权品种 |

**返回值**`dict`,字段如下：

| 字段 | 类型 | 说明 |
| --- | --- | --- |
| ExchangeID | str | 期权市场代码 |
| InstrumentID | str | 期权代码 |
| ProductID | str | 期权标的的产品ID |
| OpenDate | int | 发行日期 |
| ExpireDate | int | 到期日 |
| PreClose | float | 前收价格 |
| SettlementPrice | float | 前结算价格 |
| UpStopPrice | float | 当日涨停价 |
| DownStopPrice | float | 当日跌停价 |
| LongMarginRatio | float | 多头保证金率 |
| ShortMarginRatio | float | 空头保证金率 |
| PriceTick | float | 最小变价单位 |
| VolumeMultiple | int | 合约乘数 |
| MaxMarketOrderVolume | int | 涨跌停价最大下单量 |
| MinMarketOrderVolume | int | 涨跌停价最小下单量 |
| MaxLimitOrderVolume | int | 限价单最大下单量 |
| MinLimitOrderVolume | int | 限价单最小下单量 |
| OptUnit | int | 期权合约单位 |
| MarginUnit | float | 期权单位保证金 |
| OptUndlCode | str | 期权标的证券代码 |
| OptUndlMarket | str | 期权标的证券市场 |
| OptExercisePrice | float | 期权行权价 |
| NeeqExeType | str | 全国股转转让类型 |
| OptUndlRiskFreeRate | float | 期权标的无风险利率 |
| OptUndlHistoryRate | float | 期权标的历史波动率 |
| EndDelivDate | int | 期权行权终止日 |
| optType | str | 期权类型 |

**示例**

示例与返回值

```py
#encoding:gbk
def init(ContextInfo):
  pass

def after_init(ContextInfo):
  print(ContextInfo.get_option_detail_data('10002235.SHO'))
```

```
{'ExchangeID': 'SHO', 'InstrumentID': '10002235', 'ProductID': '50ETF(510050)', 'OpenDate': 20200123, 'ExpireDate': 20200923, 'PreClose': 0.3199, 'SettlementPrice': 0.322, 'UpStopPrice': 0.6542, 'DownStopPrice': 0.0001, 'LongMarginRatio': 12.0, 'ShortMarginRatio': 7.0, 'PriceTick': 0.0001, 'VolumeMultiple': 10000, 'MaxMarketOrderVolume': 10, 'MinMarketOrderVolume': 1, 'MaxLimitOrderVolume': 50, 'MinLimitOrderVolume': 1, 'OptUnit': 1.7976931348623157e+308, 'MarginUnit': 7206.4, 'OptUndlCode': '510050', 'OptUndlMarket': 'SH', 'OptExercisePrice': 3.0, 'NeeqExeType': 0, 'OptUndlRiskFreeRate': 0.03234, 'OptUndlHistoryRate': 0.283734422522, 'EndDelivDate': 20200923, 'optType': 'CALL'}
```

### ContextInfo.get_option_list - 获取指定期权列表

**原型**

```py
ContextInfo.get_option_list(undl_code,dedate,opttype,isavailable)
```

**释义**

获取指定期权列表。如获取历史期权，需先下载过期合约列表

**参数**

| 字段名 | 数据类型 | 解释 |
| --- | --- | --- |
| `undl_code` | `string` | 期权标的代码,如'510300.SH' |
| `dedate` | `string` | 期权到期月或当前交易日期，"YYYYMM"格式为期权到期月，"YYYYMMDD"格式为获取当前日期交易的期权 |
| `opttype` | `string` | 期权类型，默认值为空，"CALL"，"PUT"，为空时认购认沽都取 |
| `isavailable` | `bool` | 是否可交易，当`dedate`的格式为"YYYYMMDD"格式为获取当前日期交易的期权时，`isavailable`为True时返回当前可用，为False时返回当前和历史可用 |

**返回值**

`list`，期权合约列表

**示例**

示例data1返回值data2返回值data3返回值

```py
# coding:gbk
def init(C):
	pass

def handlebar(C):
	# 获取到期月份为202101的上交所510300ETF认购合约
	data1=C.get_option_list('510300.SH','202101',"CALL")

	# 获取20210104当天上交所510300ETF可交易的认购合约
	data2=C.get_option_list('510300.SH','20210104',"CALL",True)

	# 获取20210104当天上交所510300ETF已经上市的认购合约(包括退市)
	data3=C.get_option_list('510300.SH','20210104',"CALL",False)
```

```
['10002931.SHO', '10002932.SHO', '10002933.SHO', '10002934.SHO', '10002935.SHO', '10002936.SHO', '10002937.SHO', '10002938.SHO', '10002939.SHO', '10003031.SHO', '10003093.SHO', '10003117.SHO', '10003125.SHO', '10003126.SHO', '10003127.SHO', '10003128.SHO', '10003129.SHO', '10003130.SHO', '10003131.SHO', '10003132.SHO', '10003133.SHO', '10003197.SHO']
```

```
['10002743.SHO', '10002744.SHO', '10002745.SHO', '10002746.SHO', '10002747.SHO', '10002748.SHO', '10002749.SHO', '10002750.SHO', '10002751.SHO', '10002763.SHO', '10002764.SHO', '10002769.SHO', '10002877.SHO', '10002878.SHO', '10002879.SHO', '10002880.SHO', '10002881.SHO', '10002882.SHO', '10002883.SHO', '10002884.SHO', '10002885.SHO', '10002897.SHO', '10002903.SHO', '10002905.SHO', '10002931.SHO', '10002932.SHO', '10002933.SHO', '10002934.SHO', '10002935.SHO', '10002936.SHO', '10002937.SHO', '10002938.SHO', '10002939.SHO', '10003031.SHO', '10003033.SHO', '10003035.SHO', '10003063.SHO', '10003064.SHO', '10003065.SHO', '10003066.SHO', '10003067.SHO', '10003068.SHO', '10003069.SHO', '10003070.SHO', '10003071.SHO', '10003081.SHO']
```

```
['10002117.SHO', '10002118.SHO', '10002119.SHO', '10002120.SHO', '10002121.SHO', '10002122.SHO', '10002123.SHO', '10002124.SHO', '10002125.SHO', '10002135.SHO', '10002136.SHO', '10002137.SHO', '10002138.SHO', '10002139.SHO', '10002140.SHO', '10002141.SHO', '10002142.SHO', '10002143.SHO', '10002153.SHO', '10002154.SHO', '10002155.SHO', '10002156.SHO', '10002157.SHO', '10002158.SHO', '10002159.SHO', '10002160.SHO', '10002161.SHO', '10002171.SHO', '10002172.SHO', '10002173.SHO', '10002174.SHO', '10002175.SHO', '10002176.SHO', '10002177.SHO', '10002178.SHO', '10002179.SHO', '10002215.SHO', '10002217.SHO', '10002219.SHO', '10002221.SHO', '10002223.SHO', '10002225.SHO', '10002227.SHO', '10002229.SHO', '10002249.SHO', '10002250.SHO', '10002251.SHO', '10002252.SHO', '10002253.SHO', '10002254.SHO', '10002255.SHO', '10002256.SHO', '10002257.SHO', '10002271.SHO', '10002309.SHO', '10002310.SHO', '10002311.SHO', '10002315.SHO', '10002316.SHO', '10002317.SHO', '10002321.SHO', '10002322.SHO', '10002323.SHO', '10002327.SHO', '10002328.SHO', '10002329.SHO', '10002351.SHO', '10002352.SHO', '10002353.SHO', '10002354.SHO', '10002355.SHO', '10002356.SHO', '10002357.SHO', '10002358.SHO', '10002359.SHO', '10002373.SHO', '10002374.SHO', '10002381.SHO', '10002383.SHO', '10002389.SHO', '10002390.SHO', '10002409.SHO', '10002411.SHO', '10002413.SHO', '10002415.SHO', '10002425.SHO', '10002427.SHO', '10002429.SHO', '10002431.SHO', '10002451.SHO', '10002452.SHO', '10002453.SHO', '10002454.SHO', '10002455.SHO', '10002456.SHO', '10002457.SHO', '10002458.SHO', '10002459.SHO', '10002473.SHO', '10002495.SHO', '10002496.SHO', '10002497.SHO', '10002498.SHO', '10002499.SHO', '10002500.SHO', '10002501.SHO', '10002502.SHO', '10002503.SHO', '10002519.SHO', '10002521.SHO', '10002523.SHO', '10002525.SHO', '10002545.SHO', '10002546.SHO', '10002547.SHO', '10002548.SHO', '10002549.SHO', '10002550.SHO', '10002551.SHO', '10002552.SHO', '10002553.SHO', '10002563.SHO', '10002567.SHO', '10002573.SHO', '10002575.SHO', '10002581.SHO', '10002583.SHO', '10002603.SHO', '10002604.SHO', '10002605.SHO', '10002606.SHO', '10002607.SHO', '10002608.SHO', '10002609.SHO', '10002610.SHO', '10002611.SHO', '10002621.SHO', '10002629.SHO', '10002631.SHO', '10002633.SHO', '10002635.SHO', '10002645.SHO', '10002647.SHO', '10002649.SHO', '10002651.SHO', '10002661.SHO', '10002663.SHO', '10002665.SHO', '10002667.SHO', '10002693.SHO', '10002694.SHO', '10002695.SHO', '10002699.SHO', '10002700.SHO', '10002701.SHO', '10002705.SHO', '10002706.SHO', '10002707.SHO', '10002711.SHO', '10002712.SHO', '10002713.SHO', '10002717.SHO', '10002719.SHO', '10002721.SHO', '10002723.SHO', '10002743.SHO', '10002744.SHO', '10002745.SHO', '10002746.SHO', '10002747.SHO', '10002748.SHO', '10002749.SHO', '10002750.SHO', '10002751.SHO', '10002763.SHO', '10002764.SHO', '10002769.SHO', '10002789.SHO', '10002790.SHO', '10002791.SHO', '10002792.SHO', '10002793.SHO', '10002794.SHO', '10002795.SHO', '10002796.SHO', '10002797.SHO', '10002809.SHO', '10002811.SHO', '10002813.SHO', '10002833.SHO', '10002834.SHO', '10002835.SHO', '10002836.SHO', '10002837.SHO', '10002838.SHO', '10002839.SHO', '10002840.SHO', '10002841.SHO', '10002851.SHO', '10002855.SHO', '10002856.SHO', '10002877.SHO', '10002878.SHO', '10002879.SHO', '10002880.SHO', '10002881.SHO', '10002882.SHO', '10002883.SHO', '10002884.SHO', '10002885.SHO', '10002897.SHO', '10002899.SHO', '10002901.SHO', '10002903.SHO', '10002905.SHO', '10002931.SHO', '10002932.SHO', '10002933.SHO', '10002934.SHO', '10002935.SHO', '10002936.SHO', '10002937.SHO', '10002938.SHO', '10002939.SHO', '10003029.SHO', '10003031.SHO', '10003033.SHO', '10003035.SHO', '10003063.SHO', '10003064.SHO', '10003065.SHO', '10003066.SHO', '10003067.SHO', '10003068.SHO', '10003069.SHO', '10003070.SHO', '10003071.SHO', '10003081.SHO']
```

### ContextInfo.get_option_undl_data - 获取指定期权标的对应的期权品种列表

**原型**

```py
ContextInfo.get_option_undl_data(undl_code_ref)
```

**释义**

获取指定期权标的对应的期权品种列表

**参数**

| 字段名 | 数据类型 | 解释 |
| --- | --- | --- |
| `undl_code_ref` | `string` | 期权标的代码,如'510300.SH'，传空字符串时获取全部标的数据 |

**返回值**

指定期权标的代码时返回对应该标的的期权合约列表`list`

期权标的代码为空字符串时返回全部标的对应的品种列表的字典`dict`

**示例**

示例与返回值

```py
# coding:gbk
def init(C):
	pass

def handlebar(C):

	print(C.get_option_undl_data('510300.SH')[:30])
```

```
['10005347.SHO', '10005348.SHO', '10005349.SHO', '10005350.SHO', '10005351.SHO', '10005352.SHO', '10005353.SHO', '10005354.SHO', '10005355.SHO', '10005356.SHO', '10005357.SHO', '10005358.SHO', '10005359.SHO', '10005360.SHO', '10005361.SHO', '10005362.SHO', '10005363.SHO', '10005364.SHO', '10005387.SHO', '10005388.SHO', '10005391.SHO', '10005392.SHO', '10005467.SHO', '10005468.SHO', '10005783.SHO', '10005784.SHO', '10005785.SHO', '10005786.SHO', '10005787.SHO', '10005788.SHO']
```

### ContextInfo.bsm_price - 基于BS模型计算欧式期权理论价格

**原型**

```py
ContextInfo.bsm_price(optionType,objectPrices,strikePrice,riskFree,sigma,days,dividend)
```

**释义**

基于Black-Scholes-Merton模型，输入期权标的价格、期权行权价、无风险利率、期权标的年化波动率、剩余天数、标的分红率、计算期权的理论价格

**参数**

| 字段 | 类型 | 说明 |
| --- | --- | --- |
| `optionType` | `str` | `期权类型，认购：'C'，认沽：'P'` |
| `objectPrices` | `float` | `期权标的价格，可以是价格列表或者单个价格` |
| `strikePrice` | `float` | `期权行权价` |
| `riskFree` | `float` | `无风险收益率` |
| `sigma` | `float` | `标的波动率` |
| `days` | `int` | `剩余天数` |
| `dividend` | `float` | `分红率` |

**返回**

提示

- objectPrices为float时，返回float
- objectPrices为list时，返回list
- 计算结果最小值0.0001，结果保留4位小数,输入非法参数返回nan

示例与返回值

```py
#encoding:gbk
import numpy as np

def init(ContextInfo):
  pass

def after_init(ContextInfo):
  object_prices=list(np.arange(3,4,0.01));
  #计算剩余15天的行权价3.5的认购期权,在无风险利率3%,分红率为0,标的年化波动率为23%时标的价格从3元到4元变动过程中期权理论价格序列
  prices=ContextInfo.bsm_price('C',object_prices,3.5,0.03,0.23,15,0)
  print(prices)
  #计算剩余15天的行权价3.5的认购期权,在无风险利率3%,分红率为0,标的年化波动率为23%时标的价格为3.51元的平值期权的理论价格
  price=ContextInfo.bsm_price('C',3.51,3.5,0.03,0.23,15,0)
  print(price)
```

```
# 计算剩余15天的行权价3.5的认购期权,在无风险利率3%,分红率为0,标的年化波动率为23%时标的价格从3元到4元变动过程中期权理论价格序列
[0.0001, 0.0001, 0.0001, 0.0001, 0.0001, 0.0001, 0.0001, 0.0001, 0.0002, 0.0002, 0.0002, 0.0003, 0.0004, 0.0005, 0.0006, 0.0007, 0.0008, 0.001, 0.0012, 0.0015, 0.0017, 0.0021, 0.0025, 0.0029, 0.0034, 0.004, 0.0046, 0.0054, 0.0062, 0.0072, 0.0082, 0.0094, 0.0108, 0.0122, 0.0138, 0.0156, 0.0176, 0.0197, 0.022, 0.0246, 0.0273, 0.0302, 0.0334, 0.0368, 0.0404, 0.0443, 0.0484, 0.0527, 0.0573, 0.0621, 0.0672, 0.0725, 0.0781, 0.0839, 0.0899, 0.0962, 0.1027, 0.1094, 0.1163, 0.1235, 0.1308, 0.1383, 0.146, 0.1539, 0.162, 0.1702, 0.1785, 0.1871, 0.1957, 0.2044, 0.2133, 0.2223, 0.2314, 0.2405, 0.2498, 0.2591, 0.2685, 0.278, 0.2875, 0.2971, 0.3067, 0.3164, 0.3261, 0.3359, 0.3456, 0.3554, 0.3653, 0.3751, 0.385, 0.3949, 0.4048, 0.4147, 0.4246, 0.4346, 0.4445, 0.4545, 0.4644, 0.4744, 0.4844, 0.4944]
# 计算剩余15天的行权价3.5的认购期权,在无风险利率3%,分红率为0,标的年化波动率为23%时标的价格为3.51元的平值期权的理论价格
0.0725
```

### ContextInfo.bsm_iv - 基于BS模型计算欧式期权隐含波动率

**原型**

```py
ContextInfo.bsm_iv(optionType,objectPrices,strikePrice,optionPrice,riskFree,days,dividend)
```

**释义** 基于Black-Scholes-Merton模型,输入期权标的价格、期权行权价、期权现价、无风险利率、剩余天数、标的分红率,计算期权的隐含波动率

**参数**

| 字段 | 类型 | 说明 |
| --- | --- | --- |
| `optionType` | `str` | `期权类型，认购：'C'，认沽：'P'` |
| `objectPrices` | `float` | `期权标的价格，可以是价格列表或者单个价格` |
| `strikePrice` | `float` | `期权行权价` |
| `riskFree` | `float` | `无风险收益率` |
| `sigma` | `float` | `标的波动率` |
| `days` | `int` | `剩余天数` |
| `dividend` | `float` | `分红率` |

**返回**

`double`

示例与返回值

```py
#encoding:gbk
import numpy as np

def init(ContextInfo):
    pass

def after_init(ContextInfo):
    # 计算剩余15天的行权价3.5的认购期权,在无风险利率3%,分红率为0时,标的现价3.51元,期权价格0.0725元时的隐含波动率
    iv=ContextInfo.bsm_iv('C',3.51,3.5,0.0725,0.03,15)
    print(iv)
```

```
0.2299
```

## 获取除复权信息

### ContextInfo.get_divid_factors - 获取除权除息日和复权因子

**原型**

```py
ContextInfo.get_divid_factors(stock.market)
```

**释义**

获取除权除息日和复权因子

**参数**

| 字段名 | 数据类型 | 解释 |
| --- | --- | --- |
| `stock.market` | `string` | 股票代码.市场代码，如 '600000.SH' |

**返回值**

`dict`

key:时间戳，

value:list[每股红利,每股送转,每股转赠,配股,配股价,是否股改,复权系数]

输入除权除息日非法时候返回空dict，合法时返回输入日期的对应的dict，不输入时返回查询股票的所有除权除息日及对应dict

**示例**

示例与返回值

```py
# coding:gbk
def init(C):
	pass

def handlebar(C):
	Result = C.get_divid_factors('600000.SH')
	print(Result)
```

```
{962812800000: [0.15, 0.0, 0.0, 0.0, 0.0, 0, 1.006501], 1029945600000: [0.2, 0.0, 0.5, 0.0, 0.0, 0, 1.5169], 1056297600000: [0.1, 0.0, 0.0, 0.0, 0.0, 0, 1.008361], 1084982400000: [0.11, 0.0, 0.0, 0.0, 0.0, 0, 1.011853], 1115827200000: [0.12, 0.0, 0.0, 0.0, 0.0, 0, 1.017291], 1147363200000: [0.0, 0.3, 0.0, 0.0, 0.0, 1, 1.3], 1148486400000: [0.13, 0.0, 0.0, 0.0, 0.0, 0, 1.013171], 1184688000000: [0.15, 0.0, 0.0, 0.0, 0.0, 0, 1.004145], 1208966400000: [0.16, 0.3, 0.0, 0.0, 0.0, 0, 1.306069], 1244476800000: [0.23, 0.4, 0.0, 0.0, 0.0, 0, 1.4103269999999999], 1276099200000: [0.15, 0.3, 0.0, 0.0, 0.0, 0, 1.310198], 1307030400000: [0.16, 0.3, 0.0, 0.0, 0.0, 0, 1.315737], 1340640000000: [0.3, 0.0, 0.0, 0.0, 0.0, 0, 1.037267], 1370188800000: [0.55, 0.0, 0.0, 0.0, 0.0, 0, 1.055443], 1403539200000: [0.66, 0.0, 0.0, 0.0, 0.0, 0, 1.0733329999999999], 1434988800000: [0.757, 0.0, 0.0, 0.0, 0.0, 0, 1.046597], 1466611200000: [0.515, 0.0, 0.1, 0.0, 0.0, 0, 1.132278], 1495641600000: [0.2, 0.0, 0.3, 0.0, 0.0, 0, 1.316595], 1531411200000: [0.1, 0.0, 0.0, 0.0, 0.0, 0, 1.010559], 1560182400000: [0.35, 0.0, 0.0, 0.0, 0.0, 0, 1.031083], 1595433600000: [0.6, 0.0, 0.0, 0.0, 0.0, 0, 1.054446], 1626796800000: [0.48, 0.0, 0.0, 0.0, 0.0, 0, 1.050473], 1658332800000: [0.41, 0.0, 0.0, 0.0, 0.0, 0, 1.055555], 1689868800000: [0.32, 0.0, 0.0, 0.0, 0.0, 0, 1.04507]}
```

## 获取指数权重

### ContextInfo.get_weight_in_index - 获取某只股票在某指数中的绝对权重

**原型**

```py
ContextInfo.get_weight_in_index(indexcode, stockcode)
```

**释义**

获取某只股票在某指数中的绝对权重

**参数**

| 字段名 | 数据类型 | 解释 |
| --- | --- | --- |
| `indexcode` | `string` | 指数代码，格式为 'stockcode.market'，例如 '000300.SH' |
| `stockcode` | `string` | 股票代码，格式为 'stockcode.market'，例如 '600004.SH' |

**返回值**

`float`：返回的数值单位是 %，如 1.6134 表示权重是 1.6134%

**示例**

示例与返回值

```py
# coding:gbk
def init(C):
	pass

def handlebar(C):
	data = C.get_weight_in_index('000300.SH', '000002.SZ')
	print(data)
```

```
0.438
```

## 获取成分股信息

### ContextInfo.get_stock_list_in_sector - 获取板块成份股

**原型**

```py
ContextInfo.get_stock_list_in_sector(sectorname, realtime)
```

**释义**

获取板块成份股，支持客户端左侧板块列表中任意的板块，包括自定义板块

**参数**

| 字段名 | 数据类型 | 解释 |
| --- | --- | --- |
| `sectorname` | `string` | 板块名，如 '沪深300'，'中证500'，'上证50'，'我的自选'等 |
| `realtime` | 毫秒级时间戳 | 实时数据的毫秒级时间戳 |

**返回值**

list：内含成份股代码，代码形式为 'stockcode.market'，如 '000002.SZ'

**示例**

示例与返回值

```py
# coding:gbk
def init(C):
	pass
def handlebar(C):
	print(C.get_stock_list_in_sector('上证50'))
```

```
['600010.SH', '600028.SH', '600030.SH', '600031.SH', '600036.SH', '600048.SH', '600050.SH', '600089.SH', '600104.SH', '600111.SH', '600196.SH', '600276.SH', '600309.SH', '600406.SH', '600436.SH', '600438.SH', '600519.SH', '600690.SH', '600745.SH', '600809.SH', '600887.SH', '600893.SH', '600900.SH', '600905.SH', '601012.SH', '601066.SH', '601088.SH', '601166.SH', '601225.SH', '601288.SH', '601318.SH', '601390.SH', '601398.SH', '601628.SH', '601633.SH', '601668.SH', '601669.SH', '601728.SH', '601857.SH', '601888.SH', '601899.SH', '601919.SH', '603259.SH', '603260.SH', '603288.SH', '603501.SH', '603799.SH', '603986.SH', '688111.SH', '688599.SH']
```

## 获取交易日信息

注意

1. 该函数只能在`after_init`;`handlebar`运行

### ContextInfo.get_trading_dates - 获取交易日信息

**原型**

```py
ContextInfo.get_trading_dates(stockcode,start_date,end_date,count,period='1d')
```

**参数**

| 字段名 | 数据类型 | 解释 |
| --- | --- | --- |
| `stockcode` | `string` | 股票代码,缺省值''默认为当前图代码，如:'600000.SH' |
| `start_date` | `string` | 开始时间，缺省值''为空时不使用，如:'20170101','20170101000000' |
| `end_date` | `string` | 结束时间，缺省值''默认为当前bar的时间，如:'20170102','20170102000000' |
| `count` | `int` | K线个数，必须大于0，取包括end_date往前的count个K线，start_date不为空时此值无效，写为1即可 |
| `period` | `string` | k线类型,'1d':日线,'1m':分钟线,'3m':三分钟线,'5m':5分钟线,'15m':15分钟线,'30m':30分钟线,'1h':小时线,'1w':周线,'1mon':月线,'1q':季线,'1hy':半年线,'1y':年线 |

**返回值**

list:K线周期（交易日）列表 period为日线时返回如['20170101','20170102',...]样式 其它返回如['20170101010000','20170102020000',...]样式

**示例**

示例与返回值

```py
# coding:gbk
def init(C):
	pass
def after_init(C):
    print(C.get_trading_dates('600000.SH','','',30,'1d'))
def handlebar(C):
	pass
```

```
['20231101', '20231102', '20231103', '20231106', '20231107', '20231108', '20231109', '20231110', '20231113', '20231114', '20231115', '20231116', '20231117', '20231120', '20231121', '20231122', '20231123', '20231124', '20231127', '20231128', '20231129', '20231130', '20231201', '20231204', '20231205', '20231206', '20231207', '20231208', '20231211', '20231212']
```