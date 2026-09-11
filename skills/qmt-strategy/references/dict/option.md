---
url: "https://dict.thinktrader.net/dictionary/option.html"
title: "期权数据 | 迅投知识库"
---

## 获取期权数据

### 获取指定期权标的对应的期权品种列表

为了获取与指定期权标的相关的期权品种列表，你需要使用此函数操作。根据你的需求，这个过程将需要输入期权标的（如某个公司的股票代码）作为参数，接下来，该函数将返回所有与此期权标的相关的期权品种信息。这样的功能使投资者能够对期权市场有更详尽、全面的掌握，从而做出更科学、合理的投资决策。

#### 方式1：内置python

**调用方法**

```py
#encoding:gbk
def init(ContextInfo):
  pass

def after_init(ContextInfo):
  data=ContextInfo.get_option_undl_data(undl_code_ref)
```

**参数**

| 字段 | 类型 | 说明 |
| --- | --- | --- |
| `undl_code_ref` | `string` | `期权标的代码` |

- undl_code_ref:期权标的代码,如'510300.SH'，传空字符串时获取全部标的数据

**返回**

提示

- 指定期权标的返回的是 列表类型
- 期权标的为空字符串返回的是 字典类型

示例与返回值

```py
#encoding:gbk

def init(ContextInfo):
	ContextInfo.etf_code = "510050.SH"

def after_init(ContextInfo):
	data=ContextInfo.get_option_undl_data('510300.SH')
	print(data)
```

```
 ['10005347.SHO', '10005348.SHO', '10005349.SHO', '10005350.SHO', '10005351.SHO', '10005352.SHO', '10005353.SHO', '10005354.SHO', '10005355.SHO', '10005356.SHO', '10005357.SHO', '10005358.SHO', '10005359.SHO', '10005360.SHO', '10005361.SHO', '10005362.SHO', '10005363.SHO', '10005364.SHO', '10005387.SHO', '10005388.SHO', '10005391.SHO', '10005392.SHO', '10005467.SHO', '10005468.SHO', '10005783.SHO', '10005784.SHO', '10005785.SHO', '10005786.SHO', '10005787.SHO', '10005788.SHO', '10005789.SHO', '10005790.SHO', '10005791.SHO', '10005792.SHO', '10005793.SHO', '10005794.SHO', '10005795.SHO', '10005796.SHO', '10005797.SHO', '10005798.SHO', '10005799.SHO', '10005800.SHO', '10005867.SHO', '10005868.SHO', '10005875.SHO', '10005876.SHO', '10005897.SHO', '10005898.SHO', '10005931.SHO', '10005932.SHO', '10005933.SHO', '10005934.SHO', '10005935.SHO', '10005936.SHO', '10005937.SHO', '10005938.SHO', '10005939.SHO', '10005940.SHO', '10005941.SHO', '10005942.SHO', '10005943.SHO', '10005944.SHO', '10005945.SHO', '10005946.SHO', '10005947.SHO', '10005948.SHO', '10006007.SHO', '10006008.SHO', '10006019.SHO', '10006020.SHO', '10006021.SHO', '10006022.SHO', '10006023.SHO', '10006024.SHO', '10006043.SHO', '10006044.SHO', '10006045.SHO', '10006046.SHO', '10006047.SHO', '10006048.SHO', '10006049.SHO', '10006050.SHO', '10006051.SHO', '10006052.SHO', '10006053.SHO', '10006054.SHO', '10006055.SHO', '10006056.SHO', '10006057.SHO', '10006058.SHO', '10006059.SHO', '10006060.SHO', '10006117.SHO', '10006118.SHO', '10006135.SHO', '10006136.SHO', '10006137.SHO', '10006138.SHO', '10006139.SHO', '10006140.SHO', '10006141.SHO', '10006142.SHO']
```

#### 方式2：原生python

**调用方法**

```py
from xtquant import xtdata
xtdata.get_option_undl_data(undl_code_ref)
```

**参数**

| 字段 | 类型 | 说明 |
| --- | --- | --- |
| `undl_code_ref` | `string` | `期权标的代码` |

- undl_code_ref:期权标的代码,如'510300.SH'，传空字符串时获取全部标的数据

**返回**

提示

- 指定期权标的返回的是 列表类型
- 期权标的为空字符串返回的是 字典类型

示例与返回值

```py
from xtquant import xtdata
print(xtdata.get_option_undl_data("510300.SH"))
```

```
 ['10005347.SHO', '10005348.SHO', '10005349.SHO', '10005350.SHO', '10005351.SHO', '10005352.SHO', '10005353.SHO', '10005354.SHO', '10005355.SHO', '10005356.SHO', '10005357.SHO', '10005358.SHO', '10005359.SHO', '10005360.SHO', '10005361.SHO', '10005362.SHO', '10005363.SHO', '10005364.SHO', '10005387.SHO', '10005388.SHO', '10005391.SHO', '10005392.SHO', '10005467.SHO', '10005468.SHO', '10005783.SHO', '10005784.SHO', '10005785.SHO', '10005786.SHO', '10005787.SHO', '10005788.SHO', '10005789.SHO', '10005790.SHO', '10005791.SHO', '10005792.SHO', '10005793.SHO', '10005794.SHO', '10005795.SHO', '10005796.SHO', '10005797.SHO', '10005798.SHO', '10005799.SHO', '10005800.SHO', '10005867.SHO', '10005868.SHO', '10005875.SHO', '10005876.SHO', '10005897.SHO', '10005898.SHO', '10005931.SHO', '10005932.SHO', '10005933.SHO', '10005934.SHO', '10005935.SHO', '10005936.SHO', '10005937.SHO', '10005938.SHO', '10005939.SHO', '10005940.SHO', '10005941.SHO', '10005942.SHO', '10005943.SHO', '10005944.SHO', '10005945.SHO', '10005946.SHO', '10005947.SHO', '10005948.SHO', '10006007.SHO', '10006008.SHO', '10006019.SHO', '10006020.SHO', '10006021.SHO', '10006022.SHO', '10006023.SHO', '10006024.SHO', '10006043.SHO', '10006044.SHO', '10006045.SHO', '10006046.SHO', '10006047.SHO', '10006048.SHO', '10006049.SHO', '10006050.SHO', '10006051.SHO', '10006052.SHO', '10006053.SHO', '10006054.SHO', '10006055.SHO', '10006056.SHO', '10006057.SHO', '10006058.SHO', '10006059.SHO', '10006060.SHO', '10006117.SHO', '10006118.SHO', '10006135.SHO', '10006136.SHO', '10006137.SHO', '10006138.SHO', '10006139.SHO', '10006140.SHO', '10006141.SHO', '10006142.SHO']
```

### 获取历史期权列表

函数能帮助用户获取历史期权列表, 包括某日历史在上交所上市的认购合约和认沽合约, 也包括已经退市的合约。通过这一函数, 投资者可以回溯和分析不同类型合约的历史行为, 对市场变化有更全面的理解, 从而制定出更为稳健和有效的投资策略。

#### 方式1：内置python

**调用方法**

```py
#encoding:gbk
def init(ContextInfo):
  pass

def after_init(ContextInfo):
  ContextInfo.get_option_list(undl_code,dedate,opttype,isavailable)
```

**参数**

| 字段 | 类型 | 说明 |
| --- | --- | --- |
| `undl_cod` | `str` | `期权标的代码` |
| `dedate` | `str` | `期权到期月或当前交易日期，"YYYYMM"格式为期权到期月，"YYYYMMDD"格式为获取当前日期交易的期权` |
| `opttype` | `str` | `期权类型，默认值为空，"CALL"，"PUT"，为空时认购认沽都取` |
| `isavailable` | `bool` | `是否可交易，当dedate的格式为"YYYYMMDD"格式为获取当前日期交易的期权时，isavailable为True时返回当前可用，为False时返回当前和历史可用` |

**返回**

- 期权合约列表list

提示

获取历史期权需要下载过期合约列表

示例与返回值

```py
#encoding:gbk

'''获取到期月份为202101的上交所510300ETF认购合约 '''

def init(ContextInfo):
  pass

def after_init(ContextInfo):
  # 获取到期月份为202101的上交所510300ETF认购合约
  data=ContextInfo.get_option_list('510300.SH','202101',"CALL")

  # 获取20210104当天上交所510300ETF可交易的认购合约
  #data=ContextInfo.get_option_list('510300.SH','20210104',"CALL",True)

  #获取20210104当天上交所510300ETF已经上市的认购合约(包括退市)
  #data=ContextInfo.get_option_list('510300.SH','20210104',"CALL",False)

  print(data)
```

```

['10002931.SHO', '10002932.SHO', '10002933.SHO', '10002934.SHO', '10002935.SHO', '10002936.SHO', '10002937.SHO', '10002938.SHO', '10002939.SHO', '10003031.SHO', '10003093.SHO', '10003117.SHO', '10003125.SHO', '10003126.SHO', '10003127.SHO', '10003128.SHO', '10003129.SHO', '10003130.SHO', '10003131.SHO', '10003132.SHO', '10003133.SHO', '10003197.SHO']
```

#### 方式2：原生python

**调用方法**

```py
from xtquant import xtdata
xtdata.get_option_list(undl_code,dedate,opttype,isavailable)
```

**参数**

| 字段 | 类型 | 说明 |
| --- | --- | --- |
| `undl_cod` | `str` | `期权标的代码` |
| `dedate` | `str` | `期权到期月或当前交易日期，"YYYYMM"格式为期权到期月，"YYYYMMDD"格式为获取当前日期交易的期权` |
| `opttype` | `str` | `期权类型，默认值为空，"CALL"，"PUT"，为空时认购认沽都取` |
| `isavailable` | `bool` | `是否可交易，当dedate的格式为"YYYYMMDD"格式为获取当前日期交易的期权时，isavailable为True时返回当前可用，为False时返回当前和历史可用` |

**返回**

- 期权合约列表list

提示

获取历史期权需要下载过期合约列表

示例与返回值

```py
from xtquant import xtdata

# 获取到期月份为202101的上交所510300ETF认购合约
data = xtdata.get_option_list('510300.SH','202101',"CALL")

# 获取20210104当天上交所510300ETF可交易的认购合约
#data=xtdata.get_option_list('510300.SH','20210104',"CALL",True)

#获取20210104当天上交所510300ETF已经上市的认购合约(包括退市)
#data=xtdata.get_option_list('510300.SH','20210104',"CALL",False)

print(data)
```

```

['10002931.SHO', '10002932.SHO', '10002933.SHO', '10002934.SHO', '10002935.SHO', '10002936.SHO', '10002937.SHO', '10002938.SHO', '10002939.SHO', '10003031.SHO', '10003093.SHO', '10003117.SHO', '10003125.SHO', '10003126.SHO', '10003127.SHO', '10003128.SHO', '10003129.SHO', '10003130.SHO', '10003131.SHO', '10003132.SHO', '10003133.SHO', '10003197.SHO']
```

### 获取指定期权品种的详细信息

该函数能帮助用户获取指定期权品种的详细信息，如期权代码、市场、涨跌停价、期权行权价以及期权行权终止日等关键数据。通过使用此功能，投资者可以快速获取与特定期权品种有关的各项重要信息，更加清楚地理解该期权的具体状况，从而为投资决策提供准确的参考依据。

#### 方法1：内置python

**调用方法**

```py
#encoding:gbk
def init(ContextInfo):
  pass

def after_init(ContextInfo):
  ContextInfo.get_option_detail_data(optioncode)
```

**参数**

| 字段 | 类型 | 说明 |
| --- | --- | --- |
| `optioncode` | `str` | `期权代码` |

提示

当填写空字符串时候默认为当前主图的期权品种

**返回**

字典类型

| 字段 | 类型 | 说明 |
| --- | --- | --- |
| ExchangeID | str | 期权市场代码 |
| InstrumentID | str | 期权代码 |
| ProductID | str | 期权标的的产品ID |
| OpenDate | - | 发行日期 |
| ExpireDate | - | 到期日 |
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
| EndDelivDate | - | 期权行权终止日 |
| optType | str | 期权类型 |

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

#### 方法2：原生python

**调用方法**

```py
from xtquant import xtdata
xtdata.get_option_detail_data(optioncode)
```

**参数**

| 字段 | 类型 | 说明 |
| --- | --- | --- |
| `optioncode` | `str` | `期权代码` |

**返回**

字典类型

| 字段 | 类型 | 说明 |
| --- | --- | --- |
| ExchangeID | str | 期权市场代码 |
| InstrumentID | str | 期权代码 |
| ProductID | str | 期权标的的产品ID |
| OpenDate | - | 发行日期 |
| ExpireDate | - | 到期日 |
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
| EndDelivDate | - | 期权行权终止日 |
| optType | str | 期权类型 |

示例与返回值

```py
from xtquant import xtdata
print(xtdata.get_option_detail_data('10002235.SHO'))
```

```
{'ExchangeID': 'SHO', 'InstrumentID': '10002235', 'ProductID': '50ETF(510050)', 'OpenDate': 20200123, 'ExpireDate': 20200923, 'PreClose': 0.3199, 'SettlementPrice': 0.322, 'UpStopPrice': 0.6542, 'DownStopPrice': 0.0001, 'LongMarginRatio': 12.0, 'ShortMarginRatio': 7.0, 'PriceTick': 0.0001, 'VolumeMultiple': 10000, 'MaxMarketOrderVolume': 10, 'MinMarketOrderVolume': 1, 'MaxLimitOrderVolume': 50, 'MinLimitOrderVolume': 1, 'OptUnit': 1.7976931348623157e+308, 'MarginUnit': 7206.4, 'OptUndlCode': '510050', 'OptUndlMarket': 'SH', 'OptExercisePrice': 3.0, 'NeeqExeType': 0, 'OptUndlRiskFreeRate': 0.03234, 'OptUndlHistoryRate': 0.283734422522, 'EndDelivDate': 20200923, 'optType': 'CALL'}
```

### 基于BS模型计算欧式期权理论价格

基于Black-Scholes-Merton模型，输入期权标的价格、期权行权价、无风险利率、期权标的年化波动率、剩余天数、标的分红率、计算期权的理论价格

#### 方法1：内置python

**调用方法**

```py
#encoding:gbk
def init(ContextInfo):
  pass

def after_init(ContextInfo):
  ContextInfo.bsm_price(optionType,objectPrices,strikePrice,riskFree,sigma,days,dividend)
```

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

### 基于BS模型计算欧式期权隐含波动率

基于Black-Scholes-Merton模型,输入期权标的价格、期权行权价、期权现价、无风险利率、剩余天数、标的分红率,计算期权的隐含波动率

#### 方法1：内置python

**调用方法**

```py
#encoding:gbk
def init(ContextInfo):
    pass

def after_init(ContextInfo):
    ContextInfo.bsm_iv(optionType,objectPrices,strikePrice,optionPrice,riskFree,days,dividend)
```

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

## 期权行情数据

### 获取期权行情数据

获取期权最新数据，首先需要进行数据订阅。完成合约订阅后，用`get_market_data_ex`函数即可提取相关信息。这个过程包含两大步骤：第一，通过订阅操作确保能接收到你感兴趣的期权合约的更新；第二，调用`get_market_data_ex`函数来实际获取并处理这些订阅到的数据,如果需要用到历史数据或过期合约数据，需要使用`download_history_data`进行下载。这样，使用者就能获得最新和详细的期权数据，有助于做出更精准的投资决策。

**调用方法**

```py
# coding=utf-8
from xtquant import xtdata
# 下载指定合约历史行情
xtdata.download_history_data(stock_code, period, start_time='', end_time='')
# 订阅指定合约行情
xtdata.subscribe_quote(stock_code, period='', start_time='', end_time='', count=0, callback=None)
# 等待订阅完成
time.sleep(1)
# 获取指定合约行情
xtdata.get_market_data_ex(field_list = [], stock_list = [], period = '', start_time = '', end_time = '', count = -1, dividend_type = 'none', fill_data = True)
```

**参数**

- xtdata.subscribe_quote

| 字段 | 类型 | 说明 |
| --- | --- | --- |
| `stock_code` | `str` | `股票代码` |
| `start_time` | `str` | `开始时间格式YYYYMMDD/YYYYMMDDhhmmss` |
| `end_time` | `str` | `结束时间` |
| `count` | `int` | `数量 -1全部/n: 从结束时间向前数n个` |
| `period` | `str` | `周期 分笔"tick" 分钟线"1m"/"5m" 日线"1d"` |

- xtdata.get_market_data_ex

| 参数名称 | 类型 | 描述 |
| --- | --- | --- |
| `field_list` | `list` | 表示所有字段。不同的数据周期，取值范围有所不同。 |
| `stock_list` | `list` | 合约代码列表 |
| `period` | `str` | 数据周期，默认是当前主图周期。可选值如下： 'tick' (分笔线)， '1d' (日线)， '1m' (1分钟线)， '5m' (5分钟线)， '15m' (15分钟线)， 'l2quote' (Level2行情快照)， 'l2quoteaux' (Level2行情快照补充)， 'l2order' (Level2逐笔委托)， 'l2transaction' (Level2逐笔成交)，'l2transactioncount' (Level2大单统计)， 'l2orderqueue' (Level2委买委卖队列) |
| `start_time` | `str` | 开始时间。为空时默认为最早时间。时间格式为'20201231'或'20201231093000' |
| `end_time` | `str` | 结束时间。为空时默认为最新时间。时间格式为'20201231'或'20201231235959' |
| `count` | `int` | 数据最大个数。-1表示不做个数限制 |
| `dividend_type` | `str` | 复权方式，默认是当前主图复权方式。可选值包括： 'none' (不复权)， 'front'(前复权)， 'back' (后复权)， 'front_ratio' (等比前复权)， 'back_ratio' (等比后复权) |
| `fill_data` | `bool` | 停牌填充方式 |

**返回值**

- period为`1m``5m``1d`K线周期时
  - 返回dict { field1 : value1, field2 : value2, ... }
  - value1, value2, ... ：pd.DataFrame 数据集，index为stock_list，columns为time_list
  - 各字段对应的DataFrame维度相同、索引相同
- period为`tick`分笔周期时
  - 返回dict { stock1 : value1, stock2 : value2, ... }
  - stock1, stock2, ... ：合约代码
  - value1, value2, ... ：np.ndarray 数据集，按数据时间戳`time`增序排列

示例与返回值

```py
# coding=utf-8
from xtquant import xtdata
# 订阅指定合约最新行情
xtdata.subscribe_quote('10005329.SHO', period='1d', start_time='', end_time='20231026150000', count=1, callback=None)
# 下载指定合约历史行情
xtdata.download_history_data('10005329.SHO',period = "1d") # ETF期权
xtdata.download_history_data('a2407-C-5200.DF',period = "1d") # 商品期货期权
xtdata.download_history_data('IO2312-C-3550.IF',period = "1d") # 股指期货期权
# 获取指定合约历史行情
day_data = xtdata.get_market_data_ex([], ['10005329.SHO'], period='1d', start_time='20230101', end_time='20231026', count=-1, dividend_type='front', fill_data=True)
print(day_data)
```

```
{'10005329.SHO':                    time   open   high    low  close  volume     amount
 20231010  1696867200000  2.216  2.248  1.969  1.980     141   290131.0
 20231011  1696953600000  2.065  2.152  2.000  2.005     389   801904.0
 20231012  1697040000000  2.255  2.309  2.150  2.210     141   311402.0
 20231013  1697126400000  2.053  2.075  1.980  2.012     275   560743.0
 20231016  1697385600000  1.990  1.990  1.753  1.797     539   976868.0
 20231017  1697472000000  1.818  1.900  1.766  1.866     519   946258.0
 20231018  1697558400000  1.813  1.881  1.744  1.770     173   309998.0
 20231019  1697644800000  1.632  1.632  1.244  1.244    1398  1967442.0
 20231020  1697731200000  1.158  1.264  1.126  1.185    1580  1888661.0
 20231023  1697990400000  1.230  1.241  0.980  1.057    2397  2597350.0

           settelementPrice  openInterest  preClose  suspendFlag
 20231010             1.980          3276     2.140            0
 20231011             2.030          3122     1.980            0
 20231012             2.210          3083     2.005            0
 20231013             2.003          2994     2.210            0
 20231016             1.797          3064     2.012            0
 20231017             1.859          2969     1.797            0
 20231018             1.757          2939     1.866            0
 20231019             1.250          3065     1.770            0
 20231020             1.185          3582     1.244            0
 20231023             1.057          4191     1.185            0  }
```

### 获取过期期权合约代码

注意

获取过期期权合约代码本质上是通过`get_stock_list_in_sector()`获取到`过期板块`内容，所以在使用前， **请务必确保已经下载过历史合约信息**

1. 原生python：调用`xtdata.download_history_contracts()`进行下载

2. 内置python：在界面端`数据管理 - 过期合约数据 - 过期合约列表`勾选下载，下载后需要重启客户端生效


#### 内置python

**调用方法**

```py
C.get_stock_list_in_sector(sector_name)
```

**参数**

| 字段 | 类型 | 说明 |
| --- | --- | --- |
| `sector_name` | `string` | `板块名称` |

**返回值**

- `list`：内含成份股代码，代码形式为 'stockcode.market'，如 '000002.SZ'

**示例**

示例与返回值

```py
#encoding:gbk

import re

def init(C):

  option_code_list1 = get_option_code(C,"IF",data_type = 0) # 获取中金所当前可交易期权合约

  option_code_list2 = get_option_code(C,"SHO",data_type = 1) # 获取上交所已退市可交易期权合约
  option_code_list3 = get_option_code(C,"IF",data_type = 2) # 获取 中金所 所有期权（包含历史）合约

  print(option_code_list1[:5])
  print("="*20)
  print(option_code_list2[:5])
  print("="*20)
  print(option_code_list3[:5])

  # 可通过C.get_option_detail_data()查看合约具体信息

def hanldbar(C):
  return

def get_option_code(C,market,data_type = 0):

    '''

    ToDo:取出指定market的期权合约

    Args:
        market: 目标市场，比如中金所填 IF

    data_type: 返回数据范围，可返回已退市合约，默认仅返回当前

        0: 仅当前
        1: 仅历史
        2: 历史 + 当前

    '''
    _history_sector_dict = {
        "IF":"过期中金所",
        "SF":"过期上期所",
        "DF":"过期大商所",
        "ZF":"过期郑商所",
        "INE":"过期能源中心",
        "SHO":"过期上证期权",
        "SZO":"过期深证期权",
    }

    # _now_secotr_dict = {
    #     "IF":"中金所",
    #     "SF":"上期所",
    #     "DF":"大商所",
    #     "ZF":"郑商所",
    #     "INE":"能源中心",
    #     "SHO":"上证期权",
    #     "SZO":"深证期权",
    # }

    _sector = _history_sector_dict.get(market)
    # _now_sector = _now_secotr_dict.get(market)
    if _sector == None:
        raise KeyError(f"不存在该市场:{market}")
    _now_sector = _sector[2:]


    # 过期上证和过期深证有专门的板块，不需要处理
    if market == "SHO" or market == "SZO":
        if data_type == 0:
            _list = C.get_stock_list_in_sector(_now_sector)
        elif data_type == 1:
            _list = C.get_stock_list_in_sector(_sector)
        elif data_type == 2:
            _list = C.get_stock_list_in_sector(_sector) + C.get_stock_list_in_sector(_now_sector)
        else:
            raise KeyError(f"data_type参数错误:{data_type}")
        return _list

    # 期货期权需要额外处理
    if data_type == 0:
        all_list = C.get_stock_list_in_sector(_now_sector)
    elif data_type == 1:
        all_list = C.get_stock_list_in_sector(_sector)
    elif data_type == 2:
        all_list = C.get_stock_list_in_sector(_sector) + C.get_stock_list_in_sector(_now_sector)
    else:
        raise KeyError(f"data_type参数错误:{data_type}")

    _list = []
    pattern1 = r'^[A-Z]{2}\d{4}-[A-Z]-\d{4}\.[A-Z]+$'
    pattern2 = r'^[a-zA-Z]+\d+[a-zA-Z]\d+\.[A-Z]+$'
    pattern3 = r'^[a-zA-Z]+\d+-[a-zA-Z]-\d+\.[A-Z]+$'
    for i in all_list:
        if re.match(pattern1,i):
            _list.append(i)
        elif re.match(pattern2,i):
            _list.append(i)
        elif re.match(pattern3,i):
            _list.append(i)
    # _list =[i for i in all_list if re.match(pattern, i)]
    return _list
```

```
['HO2312-C-2100.IF', 'HO2312-C-2100.IF', 'HO2312-C-2125.IF', 'HO2312-C-2125.IF', 'HO2312-C-2150.IF']
====================
['10000001.SHO', '10000002.SHO', '10000003.SHO', '10000004.SHO', '10000005.SHO']
====================
['HO2301-C-2325.IF', 'HO2301-C-2325.IF', 'HO2301-C-2350.IF', 'HO2301-C-2350.IF', 'HO2301-C-2375.IF']
```

#### 原生Python

**调用方法**

```py
# coding=utf-8
from xtquant import xtdata
xtdata.get_stock_list_in_sector(sector_name)
```

**参数**

| 字段 | 类型 | 说明 |
| --- | --- | --- |
| `sector_name` | `string` | `板块名称` |

**返回值**

- `list`：内含成份股代码，代码形式为 'stockcode.market'，如 '000002.SZ'

**示例**

示例与返回值

```py
from xtquant import xtdata
import re

def get_option_code(market,data_type = 0):

    '''

    ToDo:取出指定market的期权合约

    Args:
        market: 目标市场，比如中金所填 IF

    data_type: 返回数据范围，可返回已退市合约，默认仅返回当前

        0: 仅当前
        1: 仅历史
        2: 历史 + 当前

    '''
    _history_sector_dict = {
        "IF":"过期中金所",
        "SF":"过期上期所",
        "DF":"过期大商所",
        "ZF":"过期郑商所",
        "INE":"过期能源中心",
        "SHO":"过期上证期权",
        "SZO":"过期深证期权",
    }

    # _now_secotr_dict = {
    #     "IF":"中金所",
    #     "SF":"上期所",
    #     "DF":"大商所",
    #     "ZF":"郑商所",
    #     "INE":"能源中心",
    #     "SHO":"上证期权",
    #     "SZO":"深证期权",
    # }

    _sector = _history_sector_dict.get(market)
    # _now_sector = _now_secotr_dict.get(market)
    if _sector == None:
        raise KeyError(f"不存在该市场:{market}")
    _now_sector = _sector[2:]


    # 过期上证和过期深证有专门的板块，不需要处理
    if market == "SHO" or market == "SZO":
        if data_type == 0:
            _list = xtdata.get_stock_list_in_sector(_now_sector)
        elif data_type == 1:
            _list = xtdata.get_stock_list_in_sector(_sector)
        elif data_type == 2:
            _list = xtdata.get_stock_list_in_sector(_sector) + xtdata.get_stock_list_in_sector(_now_sector)
        else:
            raise KeyError(f"data_type参数错误:{data_type}")
        return _list

    # 期货期权需要额外处理
    if data_type == 0:
        all_list = xtdata.get_stock_list_in_sector(_now_sector)
    elif data_type == 1:
        all_list = xtdata.get_stock_list_in_sector(_sector)
    elif data_type == 2:
        all_list = xtdata.get_stock_list_in_sector(_sector) + xtdata.get_stock_list_in_sector(_now_sector)
    else:
        raise KeyError(f"data_type参数错误:{data_type}")

    _list = []
    pattern1 = r'^[A-Z]{2}\d{4}-[A-Z]-\d{4}\.[A-Z]+$'
    pattern2 = r'^[a-zA-Z]+\d+[a-zA-Z]\d+\.[A-Z]+$'
    pattern3 = r'^[a-zA-Z]+\d+-[a-zA-Z]-\d+\.[A-Z]+$'
    for i in all_list:
        if re.match(pattern1,i):
            _list.append(i)
        elif re.match(pattern2,i):
            _list.append(i)
        elif re.match(pattern3,i):
            _list.append(i)
    # _list =[i for i in all_list if re.match(pattern, i)]
    return _list

if __name__ == "__main__":
  xtdata.download_history_contracts() # 下载历史合约信息

  option_code_list1 = get_option_code("IF",data_type = 0) # 获取中金所当前可交易期权合约

  option_code_list2 = get_option_code("SHO",data_type = 1) # 获取上交所已退市可交易期权合约
  option_code_list3 = get_option_code("IF",data_type = 2) # 获取 中金所 所有期权（包含历史）合约

  print(option_code_list1[:5])
  print("="*20)
  print(option_code_list2[:5])
  print("="*20)
  print(option_code_list3[:5])

  # 可通过xtdata.get_option_detail_data()查看合约具体信息
```

```
['HO2312-C-2100.IF', 'HO2312-C-2100.IF', 'HO2312-C-2125.IF', 'HO2312-C-2125.IF', 'HO2312-C-2150.IF']
====================
['10000001.SHO', '10000002.SHO', '10000003.SHO', '10000004.SHO', '10000005.SHO']
====================
['HO2301-C-2325.IF', 'HO2301-C-2325.IF', 'HO2301-C-2350.IF', 'HO2301-C-2350.IF', 'HO2301-C-2375.IF']
```

### 获取期权全推数据

获取全推tick数据的函数是用户主动调用的工具。所谓"全推tick数据"，指的是以tick（最小报价单位）为单位的实时市场数据，包括每一笔交易的信息，如成交金额、成交量、收盘价等。通过主动调用这个函数，用户能实时获得最新的市场动态，从而做出及时和准确的投资决策。

**调用方法**

```py
# coding=utf-8
from xtquant import xtdata
xtdata.get_full_tick(code_list)
```

**参数**

| 字段 | 类型 | 说明 |
| --- | --- | --- |
| `code_list` | `list` | `合约列表` |

- code_list:合约字符串格式, 例如 \['10005331.SHO', '10005332.SHO'\]

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

示例与返回值

```py
# coding=utf-8
from xtquant import xtdata
ret_full_tick = xtdata.get_full_tick(['10005331.SHO'])
print(ret_full_tick)
```

```
{'10005331.SHO': {'timetag': '20231026 10:32:56.950', 'lastPrice': 0.05470000000000001, 'open': 0.0551, 'high': 0.06100000000000001, 'low': 0.0532, 'lastClose': 0.0568, 'amount': 2018934.84, 'volume': 3524, 'pvolume': 3524, 'stockStatus': 3, 'openInt': 16495, 'settlementPrice': 0, 'lastSettlementPrice': 0, 'askPrice': [0.0548, 0.0549, 0.055, 0.0551, 0.05520000000000001], 'bidPrice': [0.05470000000000001, 0.0546, 0.0545, 0.0544, 0.0543], 'askVol': [25, 20, 65, 33, 30], 'bidVol': [43, 20, 20, 23, 40]}}
```

### 期权VIX指数

**VIX指数编制规则**

![](https://dict.thinktrader.net/assets/%E8%BF%85%E6%8A%95%E6%95%B0%E6%8D%AE%E6%9C%8D%E5%8A%A1_VIX%E6%8C%87%E6%95%B0%E7%BC%96%E5%88%B6%E8%A7%84%E5%88%99-5439c00c.png)

其中：

σ：VIX/100即VIX=σ\*100

T：到期时间

F：指数期权价格对应的远期指数水平

K0：低于F的第一个行权价

Ki：第i个虚值期权的行权价格；如果Ki > K0为看涨期权；如果Ki < K0为看跌期权；如果Ki=K0都选

∆Ki：行权价价格————Ki附近行权价差的一半(注：Ki为最低行权价时∆Ki是最低行权价和下一根行权价的差，类似的，∆Ki为最高行权价时，∆Ki是最好行权价和上一个行权价的差)

![](https://dict.thinktrader.net/assets/%E8%BF%85%E6%8A%95%E6%95%B0%E6%8D%AE%E6%9C%8D%E5%8A%A1_%E2%96%B2Ki%E8%AE%A1%E7%AE%97%E8%AF%B4%E6%98%8E-1cebe8c9.png)

R：至到期日的无风险利率

Q(Ki)：行权价为Ki的每个期权的bid-ask价差的中点

**VIX指数合约代码规则**

#### 沪深VIX指数

| 名称 | VIX指数合约代码 |
| --- | --- |
| 深圳100ETFVIX | 159901VIX.SZO.VIX |
| 创业板ETFVIX | 159915VIX.SZO.VIX |
| 沪深300ETFVIX | 159919VIX.SZO.VIX |
| 中证500ETFVIX | 159922VIX.SZO.VIX |
| 50ETFVIX | 510050VIX.SHO.VIX |
| 300ETFVIX | 510300VIX.SHO.VIX |
| 500ETFVIX | 510500VIX.SHO.VIX |
| 科创50VIX | 588000VIX.SHO.VIX |
| 科创板50VIX | 588080VIX.SHO.VIX |

**获取VIX指数行情**