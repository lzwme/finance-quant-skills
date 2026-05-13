---
url: "https://dict.thinktrader.net/innerApi/code_examples.html"
title: "完整示例 | 迅投知识库"
---

## 获取行情示例

### 按品种划分

#### 两融

##### 获取融资融券账户可融资买入标的

```py
#coding:gbk
def init(C):

	r = get_assure_contract('123456789')
	if len(r) == 0:
		print('未取到担保明细')
	else:
		finable = [o.m_strInstrumentID+'.'+o.m_strExchangeID for o in r if o.m_eFinStatus==48]
		print('可融资买入标的:', finable)
```

### 按功能划分

#### 订阅K线全推

提示

1. K线全推需要 [VIP权限](http://dict.thinktrader.net/dictionary/?id=null#vip-%E8%A1%8C%E6%83%85%E7%94%A8%E6%88%B7%E4%BC%98%E5%8A%BF%E5%AF%B9%E6%AF%94)，非VIP用户请勿使用此功能

订阅全市场1m周期K线

```py
#coding:gbk

import pandas as pd
import numpy as np

def init(C):
	stock_list = C.get_stock_list_in_sector("沪深A股")
	sub_num_dict = {i:C.subscribe_quote(
		stock_code = i,
		period = '1m',
		dividend_type = 'none',
		result_type = 'dict',  # 回调函数的行情数据格式
		callback = call_back  # 指定一个自定义的函数接收行情，自定义的函数只能有一个位置参数
		) for i in stock_list}

def call_back(data):
	print(data)
```

#### 获取N分钟周期K线数据

提示

1. 获取历史N分钟数据前，需要先下载历史数据
2. 1m以上，5m以下的数据，是通过1m数据合成的
3. 5m以上，1d以下的数据，是通过5m数据合成的
4. 1d以上的数据，是通过1d的数据合成的

```py
#coding:gbk

import pandas as pd
import numpy as np

def init(C):

	# start_date = '20231001'# 格式"YYYYMMDD"，开始下载的日期，date = ""时全量下载
	start_date = '20231001'# 格式"YYYYMMDD"，开始下载的日期，date = ""时增量下载
	end_date = "" # 格式同上，下载结束时间
	period = "3m" # 数据周期
	need_download = 1 # 取数据是空值时，将need_download赋值为1，确保正确下载了历史数据
	# code_list = ["110052.SH"] # 可转债
	# code_list = ["rb2401.SF", "FG403.ZF"] # 期货列表
	# code_list = ["HO2310-P-2500.IF"] # 期权列表
	code_list = ["000001.SZ", "600519.SH"] # 股票列表

	# 判断要不要下载数据
	if need_download:
		my_download(code_list, period, start_date, end_date)
	# 取数据
	data = C.get_market_data_ex([],code_list,period = period, start_time = start_date, end_time = end_date,dividend_type = "back_ratio")

	print(data)# 行情数据查看
	print(C.get_instrument_detail(code_list[0])) # 合约信息查看

def hanldebar(C):
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

#### 获取 Lv1 行情数据

本示例用于说明如何通过函数获取行情数据。

```py
#coding:gbk
# get_market_data_ex(subscribe=True)有订阅股票数量限制
# 即stock_list参数的数量不能超过500

# get_market_data_ex(subscribe=False) 该模式下（非订阅模式），接口会从本地行情文件里获取数据，不会获取动态行情数，且不受订阅数限制，但需要提前下载数据
# 下载数据在 操作/数据管理/补充数据选项卡里，按照页面提示下载数据

# get_market_data_ex(subscribe=True) 该模式下（订阅模式），受订阅数量上限限制，可以取到动态行情

# 建议每天盘后增量补充对应周期的行情

import time

def init(C):
	C.stock = C.stockcode + '.' + C.market
	# 获取指定时间的k线
	price = C.get_market_data_ex(['open','high','low','close'], [C.stock], start_time='', end_time='',period='1d', subscribe=False)
	print(price[C.stock].head())

def handlebar(C):

	bar_timetag = C.get_bar_timetag(C.barpos)
	bar_date = timetag_to_datetime(bar_timetag, '%Y%m%d%H%M%S')
	print('获取截至到%s为止前5根k线的开高低收等字段:'%(bar_date))
	# 获取截至今天为止前30根k线
	price = C.get_market_data_ex(
					[], [C.stock],
					end_time=bar_date,
					period=C.period,
					subscribe=True,
					count=5,
					)
	print(price[C.stock].to_dict('dict'))
```

#### 获取 Lv2 数据（需要数据源支持）

##### 方法1 - 查询LV2数据

使用该函数后，会定期查询最新数据，并进行数据返回。

使用示例：

```py
#coding:gbk
def init(C):
	C.sub_nums  = []

	C.stock = C.stockcode+'.'+C.market
	for field in ['l2transaction', 'l2order', 'l2transactioncount', 'l2quote']:
		num = C.subscribe_quote(C.stock, period=field,
							dividend_type='follow',
							)

		C.sub_nums.append(num)

def handlebar(C):
	if not C.is_last_bar():
		return
	price = C.get_market_data_ex([],[C.stock],period='l2transaction',count=10)[C.stock]
	price_dict = price.to_dict('index')
	print(price_dict)
	for pos, t in enumerate(price_dict):
		print(f" 逐笔成交:{pos+1} 时间:{price_dict[t]['stime']}, 时间戳:{price_dict[t]['time']}, 成交价:{price_dict[t]['price']},
成交量:{price_dict[t]['volume']}, 成交额:{price_dict[t]['amount']}
成交记录号:{price_dict[t]['tradeIndex']}, 买方委托号:{price_dict[t]['buyNo']},
卖方委托号:{price_dict[t]['sellNo']}, 成交类型:{price_dict[t]['tradeType']},
成交标志:{price_dict[t]['tradeFlag']}, ")

	price = C.get_market_data_ex([],[C.stock],period='l2quote',count=10)[C.stock]
	price_dict = price.to_dict('index')
	print(price_dict)
	for pos, t in enumerate(price_dict):
		print(f" 十档快照:{pos+1} 时间:{price_dict[t]['stime']}, 时间戳:{price_dict[t]['time']}, 最新价:{price_dict[t]['lastPrice']},
开盘价:{price_dict[t]['open']}, 最高价:{price_dict[t]['high']} 最低价:{price_dict[t]['low']}, 成交额:{price_dict[t]['amount']},
成交总量:{price_dict[t]['volume']}, 原始成交总量:{price_dict[t]['pvolume']}, 证券状态:{price_dict[t]['stockStatus']}, 持仓量:{price_dict[t]['openInt']},
成交笔数:{price_dict[t]['transactionNum']},前收盘价:{price_dict[t]['lastClose']},多档委卖价:{price_dict[t]['askPrice']},多档委卖量:{price_dict[t]['askVol']},
多档委买价:{price_dict[t]['bidPrice']},多档委买量:{price_dict[t]['bidVol']}")

	price = C.get_market_data_ex([],[C.stock],period='l2order',count=10)[C.stock]
	price_dict = price.to_dict('index')
	for pos, t in enumerate(price_dict):
		print(f" 逐笔委托:{pos+1} 时间:{price_dict[t]['stime']}, 时间戳:{price_dict[t]['time']}, 委托价:{price_dict[t]['price']},
委托量:{price_dict[t]['volume']}, 委托号:{price_dict[t]['entrustNo']}
委托类型:{price_dict[t]['entrustType']}, 委托方向:{price_dict[t]['entrustDirection']},
")
# 委托类型: 0：未知 1: 买入,2: 卖出,3: 撤单

	price = C.get_market_data_ex([],[C.stock],period='l2transactioncount',count=10)[C.stock]
	price_dict = price.to_dict('index')
	for pos, t in enumerate(price_dict):
		print('大单统计:', price_dict[t])

def stop(C):
	for num in C.sub_nums:
		C.unsubscribe_quote(num)
```
结果示例：
```
{'20240220150000.000': {'amount': 2946.0, 'buyNo': 33949158, 'price': 9.82, 'sellNo': 33860170, 'seq': 33952658, 'stime': '20240220150000.000', 'time': 1708412400000, 'tradeFlag': 1, 'tradeIndex': 33952658, 'tradeType': 0, 'volume': 300}}
 逐笔成交:1 时间:20240220150000.000, 时间戳:1708412400000, 成交价:9.82, 成交量:300, 成交额:2946.0 成交记录号:33952658, 买方委托号:33949158,卖方委托号:33860170, 成交类型:0, 成交标志:1,
{'20240220145839.000': {'amount': 1080809029.2600002, 'askPrice': [9.82, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], 'askVol': [12462, 666, 0, 0, 0, 0, 0, 0, 0, 0], 'bidPrice': [9.82, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], 'bidVol': [12462, 0, 0, 0, 0, 0, 0, 0, 0, 0], 'high': 9.84, 'lastClose': 9.81, 'lastPrice': 9.82, 'lastSettlementPrice': 0.0, 'low': 9.73, 'open': 9.790000000000001, 'openInt': 18, 'pvolume': 110505198, 'settlementPrice': 0.0, 'stime': '20240220145839.000', 'stockStatus': 8, 'time': 1708412319000, 'transactionNum': 52246, 'volume': 1105052}, '20240220145848.000': {'amount': 1080809029.2600002, 'askPrice': [9.82, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], 'askVol': [12587, 586, 0, 0, 0, 0, 0, 0, 0, 0], 'bidPrice': [9.82, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], 'bidVol': [12587, 0, 0, 0, 0, 0, 0, 0, 0, 0], 'high': 9.84, 'lastClose': 9.81, 'lastPrice': 9.82, 'lastSettlementPrice': 0.0, 'low': 9.73, 'open': 9.790000000000001, 'openInt': 18, 'pvolume': 110505198, 'settlementPrice': 0.0, 'stime': '20240220145848.000', 'stockStatus': 8, 'time': 1708412328000, 'transactionNum': 52246, 'volume': 1105052}, '20240220145857.000': {'amount': 1080809029.2600002, 'askPrice': [9.82, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], 'askVol': [13735, 2880, 0, 0, 0, 0, 0, 0, 0, 0], 'bidPrice': [9.82, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], 'bidVol': [13735, 0, 0, 0, 0, 0, 0, 0, 0, 0], 'high': 9.84, 'lastClose': 9.81, 'lastPrice': 9.82, 'lastSettlementPrice': 0.0, 'low': 9.73, 'open': 9.790000000000001, 'openInt': 18, 'pvolume': 110505198, 'settlementPrice': 0.0, 'stime': '20240220145857.000', 'stockStatus': 8, 'time': 1708412337000, 'transactionNum': 52246, 'volume': 1105052}, '20240220145906.000': {'amount': 1080809029.2600002, 'askPrice': [9.82, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], 'askVol': [14206, 2650, 0, 0, 0, 0, 0, 0, 0, 0], 'bidPrice': [9.82, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], 'bidVol': [14206, 0, 0, 0, 0, 0, 0, 0, 0, 0], 'high': 9.84, 'lastClose': 9.81, 'lastPrice': 9.82, 'lastSettlementPrice': 0.0, 'low': 9.73, 'open': 9.790000000000001, 'openInt': 18, 'pvolume': 110505198, 'settlementPrice': 0.0, 'stime': '20240220145906.000', 'stockStatus': 8, 'time': 1708412346000, 'transactionNum': 52246, 'volume': 1105052}, '20240220145915.000': {'amount': 1080809029.2600002, 'askPrice': [9.82, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], 'askVol': [14410, 2671, 0, 0, 0, 0, 0, 0, 0, 0], 'bidPrice': [9.82, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], 'bidVol': [14410, 0, 0, 0, 0, 0, 0, 0, 0, 0], 'high': 9.84, 'lastClose': 9.81, 'lastPrice': 9.82, 'lastSettlementPrice': 0.0, 'low': 9.73, 'open': 9.790000000000001, 'openInt': 18, 'pvolume': 110505198, 'settlementPrice': 0.0, 'stime': '20240220145915.000', 'stockStatus': 8, 'time': 1708412355000, 'transactionNum': 52246, 'volume': 1105052}, '20240220145924.000': {'amount': 1080809029.2600002, 'askPrice': [9.82, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], 'askVol': [15925, 1564, 0, 0, 0, 0, 0, 0, 0, 0], 'bidPrice': [9.82, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], 'bidVol': [15925, 0, 0, 0, 0, 0, 0, 0, 0, 0], 'high': 9.84, 'lastClose': 9.81, 'lastPrice': 9.82, 'lastSettlementPrice': 0.0, 'low': 9.73, 'open': 9.790000000000001, 'openInt': 18, 'pvolume': 110505198, 'settlementPrice': 0.0, 'stime': '20240220145924.000', 'stockStatus': 8, 'time': 1708412364000, 'transactionNum': 52246, 'volume': 1105052}, '20240220145933.000': {'amount': 1080809029.2600002, 'askPrice': [9.82, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], 'askVol': [16241, 1873, 0, 0, 0, 0, 0, 0, 0, 0], 'bidPrice': [9.82, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], 'bidVol': [16241, 0, 0, 0, 0, 0, 0, 0, 0, 0], 'high': 9.84, 'lastClose': 9.81, 'lastPrice': 9.82, 'lastSettlementPrice': 0.0, 'low': 9.73, 'open': 9.790000000000001, 'openInt': 18, 'pvolume': 110505198, 'settlementPrice': 0.0, 'stime': '20240220145933.000', 'stockStatus': 8, 'time': 1708412373000, 'transactionNum': 52246, 'volume': 1105052}, '20240220145942.000': {'amount': 1080809029.2600002, 'askPrice': [9.82, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], 'askVol': [17643, 529, 0, 0, 0, 0, 0, 0, 0, 0], 'bidPrice': [9.82, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], 'bidVol': [17643, 0, 0, 0, 0, 0, 0, 0, 0, 0], 'high': 9.84, 'lastClose': 9.81, 'lastPrice': 9.82, 'lastSettlementPrice': 0.0, 'low': 9.73, 'open': 9.790000000000001, 'openInt': 18, 'pvolume': 110505198, 'settlementPrice': 0.0, 'stime': '20240220145942.000', 'stockStatus': 8, 'time': 1708412382000, 'transactionNum': 52246, 'volume': 1105052}, '20240220145951.000': {'amount': 1080809029.2600002, 'askPrice': [9.82, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], 'askVol': [18262, 620, 0, 0, 0, 0, 0, 0, 0, 0], 'bidPrice': [9.82, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], 'bidVol': [18262, 0, 0, 0, 0, 0, 0, 0, 0, 0], 'high': 9.84, 'lastClose': 9.81, 'lastPrice': 9.82, 'lastSettlementPrice': 0.0, 'low': 9.73, 'open': 9.790000000000001, 'openInt': 18, 'pvolume': 110505198, 'settlementPrice': 0.0, 'stime': '20240220145951.000', 'stockStatus': 8, 'time': 1708412391000, 'transactionNum': 52246, 'volume': 1105052}, '20240220150000.000': {'amount': 1098987813.26, 'askPrice': [9.82, 9.83, 9.84, 9.85, 9.86, 9.87, 9.879999999999999, 9.889999999999999, 9.899999999999999, 9.909999999999998], 'askVol': [5810, 13718, 16260, 14328, 5391, 7251, 11538, 5153, 5390, 1508], 'bidPrice': [9.81, 9.8, 9.790000000000001, 9.780000000000001, 9.770000000000001, 9.760000000000002, 9.750000000000002, 9.740000000000002, 9.730000000000002, 9.720000000000002], 'bidVol': [2123, 6962, 8252, 3011, 3118, 2448, 5289, 3242, 9223, 6510], 'high': 9.84, 'lastClose': 9.81, 'lastPrice': 9.82, 'lastSettlementPrice': 0.0, 'low': 9.73, 'open': 9.790000000000001, 'openInt': 15, 'pvolume': 112356398, 'settlementPrice': 0.0, 'stime': '20240220150000.000', 'stockStatus': 5, 'time': 1708412400000, 'transactionNum': 52729, 'volume': 1123564}}
 十档快照:1 时间:20240220145839.000, 时间戳:1708412319000, 最新价:9.82, 开盘价:9.790000000000001, 最高价:9.84 最低价:9.73, 成交额:1080809029.2600002,成交总量:1105052, 原始成交总量:110505198, 证券状态:8, 持仓量:18,成交笔数:52246,前收盘价:9.81,多档委卖价:[9.82, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0],多档委卖量:[12462, 666, 0, 0, 0, 0, 0, 0, 0, 0],多档委买价:[9.82, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0],多档委买量:[12462, 0, 0, 0, 0, 0, 0, 0, 0, 0]
 十档快照:2 时间:20240220145848.000, 时间戳:1708412328000, 最新价:9.82, 开盘价:9.790000000000001, 最高价:9.84 最低价:9.73, 成交额:1080809029.2600002,成交总量:1105052, 原始成交总量:110505198, 证券状态:8, 持仓量:18,成交笔数:52246,前收盘价:9.81,多档委卖价:[9.82, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0],多档委卖量:[12587, 586, 0, 0, 0, 0, 0, 0, 0, 0],多档委买价:[9.82, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0],多档委买量:[12587, 0, 0, 0, 0, 0, 0, 0, 0, 0]
 十档快照:3 时间:20240220145857.000, 时间戳:1708412337000, 最新价:9.82, 开盘价:9.790000000000001, 最高价:9.84 最低价:9.73, 成交额:1080809029.2600002,成交总量:1105052, 原始成交总量:110505198, 证券状态:8, 持仓量:18,成交笔数:52246,前收盘价:9.81,多档委卖价:[9.82, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0],多档委卖量:[13735, 2880, 0, 0, 0, 0, 0, 0, 0, 0],多档委买价:[9.82, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0],多档委买量:[13735, 0, 0, 0, 0, 0, 0, 0, 0, 0]
 十档快照:4 时间:20240220145906.000, 时间戳:1708412346000, 最新价:9.82, 开盘价:9.790000000000001, 最高价:9.84 最低价:9.73, 成交额:1080809029.2600002,成交总量:1105052, 原始成交总量:110505198, 证券状态:8, 持仓量:18,成交笔数:52246,前收盘价:9.81,多档委卖价:[9.82, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0],多档委卖量:[14206, 2650, 0, 0, 0, 0, 0, 0, 0, 0],多档委买价:[9.82, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0],多档委买量:[14206, 0, 0, 0, 0, 0, 0, 0, 0, 0]
 十档快照:5 时间:20240220145915.000, 时间戳:1708412355000, 最新价:9.82, 开盘价:9.790000000000001, 最高价:9.84 最低价:9.73, 成交额:1080809029.2600002,成交总量:1105052, 原始成交总量:110505198, 证券状态:8, 持仓量:18,成交笔数:52246,前收盘价:9.81,多档委卖价:[9.82, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0],多档委卖量:[14410, 2671, 0, 0, 0, 0, 0, 0, 0, 0],多档委买价:[9.82, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0],多档委买量:[14410, 0, 0, 0, 0, 0, 0, 0, 0, 0]
 十档快照:6 时间:20240220145924.000, 时间戳:1708412364000, 最新价:9.82, 开盘价:9.790000000000001, 最高价:9.84 最低价:9.73, 成交额:1080809029.2600002,成交总量:1105052, 原始成交总量:110505198, 证券状态:8, 持仓量:18,成交笔数:52246,前收盘价:9.81,多档委卖价:[9.82, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0],多档委卖量:[15925, 1564, 0, 0, 0, 0, 0, 0, 0, 0],多档委买价:[9.82, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0],多档委买量:[15925, 0, 0, 0, 0, 0, 0, 0, 0, 0]
 十档快照:7 时间:20240220145933.000, 时间戳:1708412373000, 最新价:9.82, 开盘价:9.790000000000001, 最高价:9.84 最低价:9.73, 成交额:1080809029.2600002,成交总量:1105052, 原始成交总量:110505198, 证券状态:8, 持仓量:18,成交笔数:52246,前收盘价:9.81,多档委卖价:[9.82, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0],多档委卖量:[16241, 1873, 0, 0, 0, 0, 0, 0, 0, 0],多档委买价:[9.82, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0],多档委买量:[16241, 0, 0, 0, 0, 0, 0, 0, 0, 0]
 十档快照:8 时间:20240220145942.000, 时间戳:1708412382000, 最新价:9.82, 开盘价:9.790000000000001, 最高价:9.84 最低价:9.73, 成交额:1080809029.2600002,成交总量:1105052, 原始成交总量:110505198, 证券状态:8, 持仓量:18,成交笔数:52246,前收盘价:9.81,多档委卖价:[9.82, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0],多档委卖量:[17643, 529, 0, 0, 0, 0, 0, 0, 0, 0],多档委买价:[9.82, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0],多档委买量:[17643, 0, 0, 0, 0, 0, 0, 0, 0, 0]
 十档快照:9 时间:20240220145951.000, 时间戳:1708412391000, 最新价:9.82, 开盘价:9.790000000000001, 最高价:9.84 最低价:9.73, 成交额:1080809029.2600002,成交总量:1105052, 原始成交总量:110505198, 证券状态:8, 持仓量:18,成交笔数:52246,前收盘价:9.81,多档委卖价:[9.82, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0],多档委卖量:[18262, 620, 0, 0, 0, 0, 0, 0, 0, 0],多档委买价:[9.82, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0],多档委买量:[18262, 0, 0, 0, 0, 0, 0, 0, 0, 0]
 十档快照:10 时间:20240220150000.000, 时间戳:1708412400000, 最新价:9.82, 开盘价:9.790000000000001, 最高价:9.84 最低价:9.73, 成交额:1098987813.26,成交总量:1123564, 原始成交总量:112356398, 证券状态:5, 持仓量:15,成交笔数:52729,前收盘价:9.81,多档委卖价:[9.82, 9.83, 9.84, 9.85, 9.86, 9.87, 9.879999999999999, 9.889999999999999, 9.899999999999999, 9.909999999999998],多档委卖量:[5810, 13718, 16260, 14328, 5391, 7251, 11538, 5153, 5390, 1508],多档委买价:[9.81, 9.8, 9.790000000000001, 9.780000000000001, 9.770000000000001, 9.760000000000002, 9.750000000000002, 9.740000000000002, 9.730000000000002, 9.720000000000002],多档委买量:[2123, 6962, 8252, 3011, 3118, 2448, 5289, 3242, 9223, 6510]
 逐笔委托:1 时间:20240220145956.680, 时间戳:1708412396680, 委托价:9.83, 委托量:1500, 委托号:33949047 委托类型:1, 委托方向:1,
 逐笔委托:2 时间:20240220145956.730, 时间戳:1708412396730, 委托价:9.82, 委托量:500, 委托号:33949086 委托类型:1, 委托方向:1,
 逐笔委托:3 时间:20240220145956.770, 时间戳:1708412396770, 委托价:9.8, 委托量:300000, 委托号:33949126 委托类型:1, 委托方向:2,
 逐笔委托:4 时间:20240220145956.810, 时间戳:1708412396810, 委托价:9.82, 委托量:300, 委托号:33949158 委托类型:1, 委托方向:1,
 逐笔委托:5 时间:20240220145957.180, 时间戳:1708412397180, 委托价:9.8, 委托量:18600, 委托号:33949592 委托类型:1, 委托方向:2,
 逐笔委托:6 时间:20240220145957.580, 时间戳:1708412397580, 委托价:9.82, 委托量:100, 委托号:33949982 委托类型:1, 委托方向:2,
 逐笔委托:7 时间:20240220145958.300, 时间戳:1708412398300, 委托价:9.8, 委托量:84700, 委托号:33950549 委托类型:1, 委托方向:2,
 逐笔委托:8 时间:20240220145958.320, 时间戳:1708412398320, 委托价:9.83, 委托量:1200, 委托号:33950573 委托类型:1, 委托方向:1,
 逐笔委托:9 时间:20240220145958.450, 时间戳:1708412398450, 委托价:9.81, 委托量:83800, 委托号:33950686 委托类型:1, 委托方向:2,
 逐笔委托:10 时间:20240220145959.100, 时间戳:1708412399100, 委托价:9.83, 委托量:1300, 委托号:33951170 委托类型:1, 委托方向:2,
大单统计: {'bidBigAmount': 152925991.0, 'bidBigVolmue': 156226, 'bidMediumAmount': 124399721.0, 'bidMediumVolmue': 127143, 'bidMostAmount': 177571807.0, 'bidMostVolmue': 181294, 'bidNumber': 12867, 'bidSmallAmount': 81248200.0, 'bidSmallVolmue': 83072, 'ddx': 0.0, 'ddy': 4.03, 'ddz': -0.02, 'netOrder': -374, 'netWithdraw': 16, 'offBigAmount': 145053456.0, 'offBigVolmue': 148447, 'offMediumAmount': 120132514.0, 'offMediumVolmue': 122938, 'offMostAmount': 179460717.0, 'offMostVolmue': 183675, 'offNumber': 13948, 'offSmallAmount': 97078349.0, 'offSmallVolmue': 99424, 'stime': '20240220145636.000', 'time': 1708412196000, 'unactiveBidBigAmount': 181050089.0, 'unactiveBidBigVolmue': 185301, 'unactiveBidMediumAmount': 166479412.0, 'unactiveBidMediumVolmue': 170418, 'unactiveBidMostAmount': 104229355.0, 'unactiveBidMostVolmue': 106597, 'unactiveBidSmallAmount': 89966179.0, 'unactiveBidSmallVolmue': 92168, 'unactiveOffBigAmount': 177098765.0, 'unactiveOffBigVolmue': 180907, 'unactiveOffMediumAmount': 170938705.0, 'unactiveOffMediumVolmue': 174590, 'unactiveOffMostAmount': 78116964.0, 'unactiveOffMostVolmue': 79881, 'unactiveOffSmallAmount': 109991285.0, 'unactiveOffSmallVolmue': 112357, 'withdrawBid': 13979, 'withdrawOff': 9278, 'zjbyBig': 7872534, 'zjbyMedium': 4267206, 'zjbyMost': -1888909, 'zjbyNetInflow': -5579317, 'zjbySmall': -15830148}
大单统计: {'bidBigAmount': 152925991.0, 'bidBigVolmue': 156226, 'bidMediumAmount': 124399721.0, 'bidMediumVolmue': 127143, 'bidMostAmount': 177571807.0, 'bidMostVolmue': 181294, 'bidNumber': 12867, 'bidSmallAmount': 81248200.0, 'bidSmallVolmue': 83072, 'ddx': 0.0, 'ddy': 4.03, 'ddz': -0.02, 'netOrder': -374, 'netWithdraw': 12, 'offBigAmount': 145053456.0, 'offBigVolmue': 148447, 'offMediumAmount': 120132514.0, 'offMediumVolmue': 122938, 'offMostAmount': 179460717.0, 'offMostVolmue': 183675, 'offNumber': 13950, 'offSmallAmount': 97112684.0, 'offSmallVolmue': 99459, 'stime': '20240220145638.000', 'time': 1708412198000, 'unactiveBidBigAmount': 181084424.0, 'unactiveBidBigVolmue': 185336, 'unactiveBidMediumAmount': 166479412.0, 'unactiveBidMediumVolmue': 170418, 'unactiveBidMostAmount': 104229355.0, 'unactiveBidMostVolmue': 106597, 'unactiveBidSmallAmount': 89966179.0, 'unactiveBidSmallVolmue': 92168, 'unactiveOffBigAmount': 177098765.0, 'unactiveOffBigVolmue': 180907, 'unactiveOffMediumAmount': 170938705.0, 'unactiveOffMediumVolmue': 174590, 'unactiveOffMostAmount': 78116964.0, 'unactiveOffMostVolmue': 79881, 'unactiveOffSmallAmount': 109991285.0, 'unactiveOffSmallVolmue': 112357, 'withdrawBid': 13981, 'withdrawOff': 9280, 'zjbyBig': 7872534, 'zjbyMedium': 4267206, 'zjbyMost': -1888909, 'zjbyNetInflow': -5613652, 'zjbySmall': -15864483}
大单统计: {'bidBigAmount': 152925991.0, 'bidBigVolmue': 156226, 'bidMediumAmount': 124499885.0, 'bidMediumVolmue': 127245, 'bidMostAmount': 177571807.0, 'bidMostVolmue': 181294, 'bidNumber': 12872, 'bidSmallAmount': 81264894.0, 'bidSmallVolmue': 83089, 'ddx': 0.0, 'ddy': 4.06, 'ddz': -0.02, 'netOrder': -5, 'netWithdraw': 13, 'offBigAmount': 145053456.0, 'offBigVolmue': 148447, 'offMediumAmount': 120318904.0, 'offMediumVolmue': 123128, 'offMostAmount': 179460717.0, 'offMostVolmue': 183675, 'offNumber': 13962, 'offSmallAmount': 97206860.0, 'offSmallVolmue': 99555, 'stime': '20240220145642.000', 'time': 1708412202000, 'unactiveBidBigAmount': 181363028.0, 'unactiveBidBigVolmue': 185620, 'unactiveBidMediumAmount': 166479412.0, 'unactiveBidMediumVolmue': 170418, 'unactiveBidMostAmount': 104229355.0, 'unactiveBidMostVolmue': 106597, 'unactiveBidSmallAmount': 89968141.0, 'unactiveBidSmallVolmue': 92170, 'unactiveOffBigAmount': 177369797.0, 'unactiveOffBigVolmue': 181183, 'unactiveOffMediumAmount': 170784531.0, 'unactiveOffMediumVolmue': 174433, 'unactiveOffMostAmount': 78116964.0, 'unactiveOffMostVolmue': 79881, 'unactiveOffSmallAmount': 109991285.0, 'unactiveOffSmallVolmue': 112357, 'withdrawBid': 13987, 'withdrawOff': 9283, 'zjbyBig': 7872534, 'zjbyMedium': 4180980, 'zjbyMost': -1888909, 'zjbyNetInflow': -5777360, 'zjbySmall': -15941965}
大单统计: {'bidBigAmount': 152925991.0, 'bidBigVolmue': 156226, 'bidMediumAmount': 124499885.0, 'bidMediumVolmue': 127245, 'bidMostAmount': 177571807.0, 'bidMostVolmue': 181294, 'bidNumber': 12872, 'bidSmallAmount': 81264894.0, 'bidSmallVolmue': 83089, 'ddx': 0.0, 'ddy': 4.06, 'ddz': -0.02, 'netOrder': -5, 'netWithdraw': 11, 'offBigAmount': 145053456.0, 'offBigVolmue': 148447, 'offMediumAmount': 120503332.0, 'offMediumVolmue': 123316, 'offMostAmount': 179460717.0, 'offMostVolmue': 183675, 'offNumber': 13963, 'offSmallAmount': 97206860.0, 'offSmallVolmue': 99555, 'stime': '20240220145643.000', 'time': 1708412203000, 'unactiveBidBigAmount': 181363028.0, 'unactiveBidBigVolmue': 185620, 'unactiveBidMediumAmount': 166562797.0, 'unactiveBidMediumVolmue': 170503, 'unactiveBidMostAmount': 104229355.0, 'unactiveBidMostVolmue': 106597, 'unactiveBidSmallAmount': 90069184.0, 'unactiveBidSmallVolmue': 92273, 'unactiveOffBigAmount': 177369797.0, 'unactiveOffBigVolmue': 181183, 'unactiveOffMediumAmount': 170784531.0, 'unactiveOffMediumVolmue': 174433, 'unactiveOffMostAmount': 78116964.0, 'unactiveOffMostVolmue': 79881, 'unactiveOffSmallAmount': 109991285.0, 'unactiveOffSmallVolmue': 112357, 'withdrawBid': 13989, 'withdrawOff': 9283, 'zjbyBig': 7872534, 'zjbyMedium': 3996552, 'zjbyMost': -1888909, 'zjbyNetInflow': -5961788, 'zjbySmall': -15941965}
大单统计: {'bidBigAmount': 152925991.0, 'bidBigVolmue': 156226, 'bidMediumAmount': 124499885.0, 'bidMediumVolmue': 127245, 'bidMostAmount': 177571807.0, 'bidMostVolmue': 181294, 'bidNumber': 12873, 'bidSmallAmount': 81274714.0, 'bidSmallVolmue': 83099, 'ddx': 0.0, 'ddy': 4.07, 'ddz': -0.02, 'netOrder': 248, 'netWithdraw': 12, 'offBigAmount': 145053456.0, 'offBigVolmue': 148447, 'offMediumAmount': 120503332.0, 'offMediumVolmue': 123316, 'offMostAmount': 179460717.0, 'offMostVolmue': 183675, 'offNumber': 13967, 'offSmallAmount': 97279454.0, 'offSmallVolmue': 99629, 'stime': '20240220145648.000', 'time': 1708412208000, 'unactiveBidBigAmount': 181363028.0, 'unactiveBidBigVolmue': 185620, 'unactiveBidMediumAmount': 166635391.0, 'unactiveBidMediumVolmue': 170577, 'unactiveBidMostAmount': 104229355.0, 'unactiveBidMostVolmue': 106597, 'unactiveBidSmallAmount': 90069184.0, 'unactiveBidSmallVolmue': 92273, 'unactiveOffBigAmount': 177379617.0, 'unactiveOffBigVolmue': 181193, 'unactiveOffMediumAmount': 170784531.0, 'unactiveOffMediumVolmue': 174433, 'unactiveOffMostAmount': 78116964.0, 'unactiveOffMostVolmue': 79881, 'unactiveOffSmallAmount': 109991285.0, 'unactiveOffSmallVolmue': 112357, 'withdrawBid': 13992, 'withdrawOff': 9290, 'zjbyBig': 7872534, 'zjbyMedium': 3996552, 'zjbyMost': -1888909, 'zjbyNetInflow': -6024562, 'zjbySmall': -16004739}
大单统计: {'bidBigAmount': 152925991.0, 'bidBigVolmue': 156226, 'bidMediumAmount': 124499885.0, 'bidMediumVolmue': 127245, 'bidMostAmount': 177571807.0, 'bidMostVolmue': 181294, 'bidNumber': 12875, 'bidSmallAmount': 81313012.0, 'bidSmallVolmue': 83138, 'ddx': 0.0, 'ddy': 4.07, 'ddz': -0.02, 'netOrder': 248, 'netWithdraw': 17, 'offBigAmount': 145053456.0, 'offBigVolmue': 148447, 'offMediumAmount': 120556306.0, 'offMediumVolmue': 123370, 'offMostAmount': 179460717.0, 'offMostVolmue': 183675, 'offNumber': 13968, 'offSmallAmount': 97279454.0, 'offSmallVolmue': 99629, 'stime': '20240220145650.000', 'time': 1708412210000, 'unactiveBidBigAmount': 181565114.0, 'unactiveBidBigVolmue': 185826, 'unactiveBidMediumAmount': 166479412.0, 'unactiveBidMediumVolmue': 170418, 'unactiveBidMostAmount': 104229355.0, 'unactiveBidMostVolmue': 106597, 'unactiveBidSmallAmount': 90076051.0, 'unactiveBidSmallVolmue': 92280, 'unactiveOffBigAmount': 177417915.0, 'unactiveOffBigVolmue': 181232, 'unactiveOffMediumAmount': 170784531.0, 'unactiveOffMediumVolmue': 174433, 'unactiveOffMostAmount': 78116964.0, 'unactiveOffMostVolmue': 79881, 'unactiveOffSmallAmount': 109991285.0, 'unactiveOffSmallVolmue': 112357, 'withdrawBid': 13997, 'withdrawOff': 9292, 'zjbyBig': 7872534, 'zjbyMedium': 3943578, 'zjbyMost': -1888909, 'zjbyNetInflow': -6039238, 'zjbySmall': -15966441}
大单统计: {'bidBigAmount': 152925991.0, 'bidBigVolmue': 156226, 'bidMediumAmount': 124499885.0, 'bidMediumVolmue': 127245, 'bidMostAmount': 177571807.0, 'bidMostVolmue': 181294, 'bidNumber': 12877, 'bidSmallAmount': 81323814.0, 'bidSmallVolmue': 83149, 'ddx': 0.0, 'ddy': 4.07, 'ddz': -0.02, 'netOrder': -6373, 'netWithdraw': 16, 'offBigAmount': 145053456.0, 'offBigVolmue': 148447, 'offMediumAmount': 120611242.0, 'offMediumVolmue': 123426, 'offMostAmount': 179460717.0, 'offMostVolmue': 183675, 'offNumber': 13971, 'offSmallAmount': 97326542.0, 'offSmallVolmue': 99677, 'stime': '20240220145654.000', 'time': 1708412214000, 'unactiveBidBigAmount': 181565114.0, 'unactiveBidBigVolmue': 185826, 'unactiveBidMediumAmount': 166528462.0, 'unactiveBidMediumVolmue': 170468, 'unactiveBidMostAmount': 104229355.0, 'unactiveBidMostVolmue': 106597, 'unactiveBidSmallAmount': 90129025.0, 'unactiveBidSmallVolmue': 92334, 'unactiveOffBigAmount': 177428717.0, 'unactiveOffBigVolmue': 181243, 'unactiveOffMediumAmount': 170784531.0, 'unactiveOffMediumVolmue': 174433, 'unactiveOffMostAmount': 78116964.0, 'unactiveOffMostVolmue': 79881, 'unactiveOffSmallAmount': 109991285.0, 'unactiveOffSmallVolmue': 112357, 'withdrawBid': 13999, 'withdrawOff': 9299, 'zjbyBig': 7872534, 'zjbyMedium': 3888642, 'zjbyMost': -1888909, 'zjbyNetInflow': -6130460, 'zjbySmall': -16002727}
大单统计: {'bidBigAmount': 152925991.0, 'bidBigVolmue': 156226, 'bidMediumAmount': 124499885.0, 'bidMediumVolmue': 127245, 'bidMostAmount': 177571807.0, 'bidMostVolmue': 181294, 'bidNumber': 12877, 'bidSmallAmount': 81323814.0, 'bidSmallVolmue': 83149, 'ddx': 0.0, 'ddy': 4.09, 'ddz': -0.02, 'netOrder': -6373, 'netWithdraw': 15, 'offBigAmount': 145053456.0, 'offBigVolmue': 148447, 'offMediumAmount': 120611242.0, 'offMediumVolmue': 123426, 'offMostAmount': 179460717.0, 'offMostVolmue': 183675, 'offNumber': 13976, 'offSmallAmount': 97372649.0, 'offSmallVolmue': 99724, 'stime': '20240220145656.000', 'time': 1708412216000, 'unactiveBidBigAmount': 181565114.0, 'unactiveBidBigVolmue': 185826, 'unactiveBidMediumAmount': 166577512.0, 'unactiveBidMediumVolmue': 170518, 'unactiveBidMostAmount': 104229355.0, 'unactiveBidMostVolmue': 106597, 'unactiveBidSmallAmount': 90126082.0, 'unactiveBidSmallVolmue': 92331, 'unactiveOffBigAmount': 177428717.0, 'unactiveOffBigVolmue': 181243, 'unactiveOffMediumAmount': 170784531.0, 'unactiveOffMediumVolmue': 174433, 'unactiveOffMostAmount': 78116964.0, 'unactiveOffMostVolmue': 79881, 'unactiveOffSmallAmount': 109991285.0, 'unactiveOffSmallVolmue': 112357, 'withdrawBid': 14002, 'withdrawOff': 9302, 'zjbyBig': 7872534, 'zjbyMedium': 3888642, 'zjbyMost': -1888909, 'zjbyNetInflow': -6176567, 'zjbySmall': -16048834}
大单统计: {'bidBigAmount': 153907941.0, 'bidBigVolmue': 157226, 'bidMediumAmount': 124499885.0, 'bidMediumVolmue': 127245, 'bidMostAmount': 177571807.0, 'bidMostVolmue': 181294, 'bidNumber': 12881, 'bidSmallAmount': 81386627.0, 'bidSmallVolmue': 83213, 'ddx': 0.0, 'ddy': 4.09, 'ddz': -0.02, 'netOrder': -324, 'netWithdraw': 9, 'offBigAmount': 145951071.0, 'offBigVolmue': 149362, 'offMediumAmount': 120611242.0, 'offMediumVolmue': 123426, 'offMostAmount': 179460717.0, 'offMostVolmue': 183675, 'offNumber': 13980, 'offSmallAmount': 97419737.0, 'offSmallVolmue': 99772, 'stime': '20240220145659.000', 'time': 1708412219000, 'unactiveBidBigAmount': 181946723.0, 'unactiveBidBigVolmue': 186215, 'unactiveBidMediumAmount': 167049373.0, 'unactiveBidMediumVolmue': 170999, 'unactiveBidMostAmount': 104229355.0, 'unactiveBidMostVolmue': 106597, 'unactiveBidSmallAmount': 90217315.0, 'unactiveBidSmallVolmue': 92424, 'unactiveOffBigAmount': 178280111.0, 'unactiveOffBigVolmue': 182110, 'unactiveOffMediumAmount': 170956296.0, 'unactiveOffMediumVolmue': 174608, 'unactiveOffMostAmount': 78116964.0, 'unactiveOffMostVolmue': 79881, 'unactiveOffSmallAmount': 110012889.0, 'unactiveOffSmallVolmue': 112379, 'withdrawBid': 14003, 'withdrawOff': 9304, 'zjbyBig': 7956869, 'zjbyMedium': 3888642, 'zjbyMost': -1888909, 'zjbyNetInflow': -6076507, 'zjbySmall': -16033109}
大单统计: {'bidBigAmount': 156870635.0, 'bidBigVolmue': 160243, 'bidMediumAmount': 126389253.0, 'bidMediumVolmue': 129169, 'bidMostAmount': 180761343.0, 'bidMostVolmue': 184542, 'bidNumber': 12970, 'bidSmallAmount': 81947349.0, 'bidSmallVolmue': 83784, 'ddx': 0.0, 'ddy': 4.21, 'ddz': -0.02, 'netOrder': 7661, 'netWithdraw': 9, 'offBigAmount': 148570065.0, 'offBigVolmue': 152029, 'offMediumAmount': 123102576.0, 'offMediumVolmue': 125963, 'offMostAmount': 182394933.0, 'offMostVolmue': 186663, 'offNumber': 14111, 'offSmallAmount': 98951657.0, 'offSmallVolmue': 101332, 'stime': '20240220150000.000', 'time': 1708412400000, 'unactiveBidBigAmount': 184733639.0, 'unactiveBidBigVolmue': 189053, 'unactiveBidMediumAmount': 168611735.0, 'unactiveBidMediumVolmue': 172590, 'unactiveBidMostAmount': 108729861.0, 'unactiveBidMostVolmue': 111180, 'unactiveBidSmallAmount': 90943995.0, 'unactiveBidSmallVolmue': 93164, 'unactiveOffBigAmount': 180480773.0, 'unactiveOffBigVolmue': 184351, 'unactiveOffMediumAmount': 174386422.0, 'unactiveOffMediumVolmue': 178101, 'unactiveOffMostAmount': 79344464.0, 'unactiveOffMostVolmue': 81131, 'unactiveOffSmallAmount': 111756921.0, 'unactiveOffSmallVolmue': 114155, 'withdrawBid': 14003, 'withdrawOff': 9304, 'zjbyBig': 8300569, 'zjbyMedium': 3286676, 'zjbyMost': -1633589, 'zjbyNetInflow': -7050651, 'zjbySmall': -17004307}
```

##### 方法2 - 订阅LV2数据

此方法在发起订阅后，会自动收到所订阅数据，订阅方需要记录订阅函数返回的订阅号，并在不需要订阅时调用unsubscribe_quote反订阅数据，释放资源。

使用示例：

```py
#coding:gbk

def l2_quote_callback(data):
	for s in data:
		print('lv2快照:',s, data[s])

def l2transaction_callback(data):
	for s in data:
		print('逐笔成交',s, data[s])

def l2order_callback(data):
	for s in data:
		print('逐笔委托',s, data[s])

def l2quoteaux_callback(data):
	for s in data:
		print('行情快照补充',s, data[s])

def l2transactioncount_callback(data):
	for s in data:
		print('大单统计',s, data[s])

def l2orderqueue_callback(data):
	for s in data:
		print('委买委卖队列',s, data[s])

def init(C):
	C.stock = C.stockcode + '.' + C.market

	# Level2 逐笔快照
	C.subscribe_quote(C.stock, 'l2quote', result_type='dict', callback=l2_quote_callback)
	# Level2 行情快照补充
	C.subscribe_quote(C.stock, 'l2quoteaux', result_type='dict', callback=l2quoteaux_callback)
	# Level2 逐笔成交
	C.subscribe_quote(C.stock, 'l2transaction', result_type='dict', callback=l2transaction_callback)
	# Level2 逐笔委托
	C.subscribe_quote(C.stock, 'l2order', result_type='dict', callback=l2order_callback)
	# Level2大单统计
	C.subscribe_quote(C.stock, 'l2transactioncount', result_type='dict', callback=l2transactioncount_callback)
	# Level2委买委卖队列
	C.subscribe_quote(C.stock, 'l2orderqueue', result_type='dict', callback=l2orderqueue_callback)

def handlebar(C):
	return
```
结果示例：
```
行情快照补充 000001.SZ {'time': 1708412400000, 'stime': '20240220150000.000', 'avgBidPrice': 9.59, 'totalBidQuantity': 109458, 'avgOffPrice': 10.22, 'totalOffQuantity': 246790, 'withdrawBidQuantity': 0, 'withdrawBidAmount': 0.0, 'withdrawOffQuantity': 0, 'withdrawOffAmount': 0.0}
lv2快照: 000001.SZ {'time': 1708412400000, 'stime': '20240220150000.000', 'lastPrice': 9.82, 'amount': 1098987813.26, 'volume': 1123564, 'pvolume': 112356398, 'openInt': 15, 'stockStatus': 5, 'lastSettlementPrice': 0.0, 'open': 9.790000000000001, 'high': 9.84, 'low': 9.73, 'settlementPrice': 0.0, 'lastClose': 9.81, 'transactionNum': 52729, 'askPrice': [9.82, 9.83, 9.84, 9.85, 9.86, 9.87, 9.879999999999999, 9.889999999999999, 9.899999999999999, 9.909999999999998], 'bidPrice': [9.81, 9.8, 9.790000000000001, 9.780000000000001, 9.770000000000001, 9.760000000000002, 9.750000000000002, 9.740000000000002, 9.730000000000002, 9.720000000000002], 'askVol': [5810, 13718, 16260, 14328, 5391, 7251, 11538, 5153, 5390, 1508], 'bidVol': [2123, 6962, 8252, 3011, 3118, 2448, 5289, 3242, 9223, 6510]}
委买委卖队列 000001.SZ {'time': 1708412400000, 'stime': '20240220150000.000', 'bidLevelPrice': 9.81, 'bidLevelVolume': [604, 5, 115, 10, 9, 5, 10, 1, 2, 12, 8, 5, 4, 50, 40, 100, 10, 5, 100, 52, 26, 29, 20, 2, 20, 5, 10, 10, 10, 115, 5, 239, 388, 6, 68, 23], 'offerLevelPrice': 9.82, 'offerLevelVolume': [58, 5, 10, 10, 5, 10, 30, 10, 8, 4, 65, 2, 10, 1, 1, 15, 20, 5, 20, 19, 39, 29, 20, 7, 20, 126, 4, 2, 30, 20, 30, 2, 50, 3, 1, 10, 90, 10, 1, 4, 10, 10, 20, 5, 5, 2, 104, 2, 4, 65]}
大单统计 000001.SZ {'time': 1708412400000, 'stime': '20240220150000.000', 'bidNumber': 12970, 'bidMostVolmue': 184542, 'bidBigVolmue': 160243, 'bidMediumVolmue': 129169, 'bidSmallVolmue': 83784, 'offNumber': 14111, 'offMostVolmue': 186663, 'offBigVolmue': 152029, 'offMediumVolmue': 125963, 'offSmallVolmue': 101332, 'bidMostAmount': 180761343.0, 'bidBigAmount': 156870635.0, 'bidMediumAmount': 126389253.0, 'bidSmallAmount': 81947349.0, 'offMostAmount': 182394933.0, 'offBigAmount': 148570065.0, 'offMediumAmount': 123102576.0, 'offSmallAmount': 98951657.0, 'ddx': 0.0, 'ddy': 4.21, 'ddz': -0.02, 'zjbyNetInflow': -7050651, 'zjbyMost': -1633589, 'zjbyBig': 8300569, 'zjbyMedium': 3286676, 'zjbySmall': -17004307, 'netOrder': 7661, 'netWithdraw': 9, 'withdrawBid': 14003, 'withdrawOff': 9304, 'unactiveBidMostVolmue': 111180, 'unactiveBidBigVolmue': 189053, 'unactiveBidMediumVolmue': 172590, 'unactiveBidSmallVolmue': 93164, 'unactiveOffMostVolmue': 81131, 'unactiveOffBigVolmue': 184351, 'unactiveOffMediumVolmue': 178101, 'unactiveOffSmallVolmue': 114155, 'unactiveBidMostAmount': 108729861.0, 'unactiveBidBigAmount': 184733639.0, 'unactiveBidMediumAmount': 168611735.0, 'unactiveBidSmallAmount': 90943995.0, 'unactiveOffMostAmount': 79344464.0, 'unactiveOffBigAmount': 180480773.0, 'unactiveOffMediumAmount': 174386422.0, 'unactiveOffSmallAmount': 111756921.0}
```

#### 使用 Lv1 全推数据计算全市场涨幅

```py
#coding:gbk

import time

class a():pass

A = a()

def init(C):
	A.hsa = C.get_stock_list_in_sector('沪深A股') + C.get_stock_list_in_sector('京市A股')
	print('股票池大小', len(A.hsa))
	A.vol_dict = {}
	for stock in A.hsa:
			A.vol_dict[stock] = C.get_last_volume(stock)
	C.run_time("f","3nSecond","2019-10-14 13:20:00")

def to_zw(a):
	'''0.中文价格字符串'''
	import numpy as np
	if np.isnan(a):
			return '问题数据'
	if abs(a) < 1000:
			print(a, str(round(int(a) / 1000.0, 2)) + "千")
			return str(round(int(a) / 1000.0, 2)) + "千"
	if abs(a) < 10000:
			return str(int(a))[0] + "千"
	if abs(a) < 100000000:
			return str(int(a))[:-4] + "万" + str(int(a))[-4]
	return f"{int(a / 100000000)}亿"

def f(C):
	t0 = time.time()
	full_tick = C.get_full_tick(A.hsa)
	total_market_value = 0
	total_ratio = 0
	count = 0
	total_amount = 0
	ratio_list = []
	for stock in A.hsa:
			ratio = full_tick[stock]['lastPrice'] / full_tick[stock]['lastClose'] - 1
			amount = full_tick[stock]['amount']
			total_amount += amount
			rise_price = round(full_tick[stock]['lastClose'] *1.2,2) if stock[0] == '3' or stock[:3] == '688' else round(full_tick[stock]['lastClose'] *1.1,2)
			#如果要打印涨停品种
			#if abs(full_tick[stock]['lastPrice'] - rise_price) <0.01:
			#        print(f"涨停品种 {stock} {C.get_stock_name(stock)}")
			market_value = full_tick[stock]['lastPrice'] * A.vol_dict[stock]
			total_ratio += ratio * market_value
			total_market_value += market_value
			count += 1
			ratio_list.append(ratio)
	#print(count)
	total_ratio /= total_market_value
	total_ratio *= 100
	middle  = int(len(ratio_list) / 2)
	middle_ratio = ratio_list[middle]
	rise_num = len([i for i in ratio_list if i > 0])
	down_num = len([i for i in ratio_list if i < 0])
	print(f'A股加权涨幅 {round(total_ratio,2)}% 涨幅中位数 {round(middle_ratio,2)}% {rise_num}个上涨 {down_num}个下跌 成交金额 {to_zw(total_amount)} 耗时{round(time.time()- t0,5)}秒')
```

#### 在行情回调函数里处理动态行情

[ContextInfo.subscribe_quote - 订阅行情函数说明](data_function.md#contextinfosubscribe_quote---%E8%AE%A2%E9%98%85%E8%A1%8C%E6%83%85%E6%95%B0%E6%8D%AE)

[行情回调函数字段说明](data_structure.md#%E4%BA%A4%E6%98%93%E7%B1%BB)

```py
#coding:gbk

sub_nums = []

def init(C):
	global sub_nums

	# def on_quote(data1， data2): # 错误写法
	def on_quote(data):
		for s in data:
			q = data[s]
			print(type(q), q)

	stocks = [C.stockcode + '.' + C.market]  # 获取到当前主图股票代码
	for s in stocks:
		num = C.subscribe_quote(s, period='1d',
						  dividend_type='none',
						  result_type='dict',  # 回调函数的行情数据格式
						  callback=on_quote  # 指定一个自定义的函数接收行情，自定义的函数只能有一个位置参数
						)
		sub_nums.append(num)

def stop(C):
	# 反订阅
	for num in sub_nums:
		C.unsubscribe_quote(num)
```

#### python写入扩展数据

```py
# coding:gbk
'''
python写扩展数据，投研接口
'''

def init(C):
    # 创建扩展数据
    extencd_name  = 'test' # 创建名为test的扩展数据
    create_extend_data# (父节点, 扩展数据名称, 是否覆盖)
    C.extencd_name = create_extend_data('扩展数据', extencd_name, True)


def handlebar(C):
    if C.is_last_bar():
        data = {'SH600177': 0.43, 'SZ000767': 0.18, 'SH600362': 0.27, 'SH600171': 0.25, 'SH600170': 0.18, 'SH600073': 0.13, 'SZ000768': 0.17, 'SH600282': 0.19, 'SH600601': 0.42, 'SH600569': 0.26, 'SZ000401': 0.21, 'SH600602': 0.17, 'SZ000806': 0.13, 'SZ000807': 0.15, 'SH600608': 0.08, 'SH600874': 0.09, 'SZ000825': 0.44, 'SZ000652': 0.19, 'SH600078': 0.11, 'SH600871': 0.1, 'SZ000573': 0.1, 'SZ000520': 0.14, 'SH600879': 0.43, 'SZ000960': 0.2, 'SH600597': 0.21, 'SZ000550': 0.1, 'SH600591': 0.14, 'SZ000059': 0.13, 'SH600215': 0.12, 'SZ000968': 0.11, 'SZ000969': 0.14, 'SZ000568': 0.22, 'SH600598': 0.22, 'SH600028': 1.85, 'SH600270': 0.27, 'SH600060': 0.22, 'SH600062': 0.15, 'SH600779': 0.14, 'SH600997': 0.2, 'SZ000707': 0.12, 'SH600068': 0.16, 'SH600770': 0.14, 'SZ000680': 0.14, 'SH600674': 0.1, 'SH600675': 0.25, 'SZ000488': 0.28, 'SZ000012': 0.11, 'SH600863': 0.17, 'SZ000429': 0.17, 'SH600027': 0.32, 'SH600866': 0.13, 'SH600001': 0.43, 'SZ000636': 0.11, 'SH600900': 2.73, 'SH600600': 0.31, 'SH600895': 0.26, 'SH600029': 0.43, 'SH600020': 0.24, 'SH600205': 0.39, 'SH600688': 0.76, 'SH600207': 0.1, 'SZ000970': 0.3, 'SZ000601': 0.19, 'SH600200': 0.35, 'SZ000975': 0.08, 'SZ000538': 0.39, 'SZ000422': 0.14, 'SZ000858': 0.88, 'SZ000651': 0.44, 'SH600780': 0.21, 'SH600007': 0.11, 'SH600016': 2.36, 'SZ000866': 0.84, 'SH600267': 0.12, 'SH600266': 0.16, 'SH600786': 0.27, 'SZ000406': 0.39, 'SH600269': 0.47, 'SZ000528': 0.19, 'SH600694': 0.51, 'SZ000786': 0.14, 'SH600004': 0.4, 'SH600663': 0.25, 'SH600662': 0.21, 'SH600548': 0.11, 'SH600383': 0.42, 'SH600357': 0.12, 'SH600705': 0.13, 'SH600812': 0.18, 'SH600707': 0.06, 'SZ000895': 0.49, 'SZ000898': 0.68, 'SZ000400': 0.17, 'SZ000607': 0.1, 'SH600894': 0.1, 'SH600418': 0.4, 'SZ000061': 0.15, 'SH600653': 0.31, 'SZ000682': 0.17, 'SZ000543': 0.07, 'SZ000541': 0.25, 'SH600377': 0.12, 'SZ000949': 0.06, 'SH600256': 0.17, 'SH600006': 0.23, 'SH600005': 1.13, 'SH600790': 0.1, 'SH600797': 0.2, 'SH600002': 0.51, 'SH600795': 0.49, 'SH600000': 1.64, 'SH600652': 0.17, 'SH600121': 0.13, 'SH600123': 0.3, 'SH600125': 0.27, 'SH600126': 0.12, 'SH600008': 0.51, 'SZ000016': 0.14, 'SH600550': 0.24, 'SH600718': 0.16, 'SH600654': 0.2, 'SZ000157': 0.2, 'SH600808': 0.42, 'SZ000666': 0.1, 'SH600805': 0.11, 'SZ000527': 0.39, 'SH600717': 0.5, 'SH600399': 0.07, 'SZ000828': 0.14, 'SZ000959': 0.17, 'SZ000729': 0.29, 'SH600098': 0.43, 'SZ000886': 0.09, 'SZ000099': 0.13, 'SZ000800': 0.29, 'SH600096': 0.29, 'SZ001872': 0.17, 'SH600091': 0.12, 'SZ000956': 0.41, 'SH600887': 0.63, 'SH600886': 0.2, 'SH600884': 0.12, 'SH600308': 0.32, 'SH600309': 0.64, 'SH600881': 0.21, 'SH600307': 0.14, 'SZ000069': 0.8, 'SZ000068': 0.1, 'SH600153': 0.19, 'SZ000792': 0.55, 'SZ000060': 0.38, 'SZ000002': 2.25, 'SZ000001': 1.25, 'SH600138': 0.1, 'SH600649': 0.44, 'SH600015': 0.99, 'SZ000533': 0.07, 'SZ000009': 0.24, 'SH600408': 0.09, 'SZ000778': 0.23, 'SH600643': 0.17, 'SH600642': 0.71, 'SH600832': 0.71, 'SZ000089': 0.36, 'SZ000088': 0.44, 'SZ000539': 0.3, 'SH600835': 0.19, 'SH600726': 0.09, 'SH600010': 0.42, 'SH600724': 0.16, 'SH600839': 0.61, 'SH600011': 0.38, 'SH600012': 0.27, 'SH600089': 0.23, 'SH600088': 0.12, 'SH600087': 0.12, 'SH600085': 0.38, 'SZ000927': 0.2, 'SZ000920': 0.11, 'SZ000962': 0.13, 'SZ000559': 0.16, 'SH600050': 2.98, 'SZ000708': 0.09, 'SZ000503': 0.36, 'SZ000839': 0.44, 'SZ000717': 0.28, 'SZ000100': 0.31, 'SZ000036': 0.18, 'SZ000878': 0.24, 'SZ000511': 0.09, 'SZ000410': 0.19, 'SH600033': 0.24, 'SH600108': 0.13, 'SZ000031': 0.21, 'SZ000507': 0.09, 'SH600104': 0.78, 'SZ002024': 0.45, 'SH600102': 0.18, 'SH600103': 0.14, 'SH600100': 0.41, 'SH600019': 2.84, 'SH600009': 1.5, 'SH600639': 0.19, 'SZ000709': 0.34, 'SH600820': 0.14, 'SZ000571': 0.1, 'SH600739': 0.13, 'SH600631': 0.25, 'SH600021': 0.24, 'SH600635': 0.22, 'SH600637': 0.15, 'SZ000733': 0.09, 'SZ000780': 0.09, 'SH600210': 0.25, 'SZ000939': 0.12, 'SZ000937': 0.26, 'SZ000875': 0.15, 'SZ000933': 0.22, 'SZ000932': 0.51, 'SZ000659': 0.15, 'SZ000930': 0.38, 'SH600320': 0.8, 'SZ000822': 0.17, 'SZ000726': 0.14, 'SZ000727': 0.1, 'SZ000725': 0.13, 'SH600380': 0.14, 'SH600030': 0.63, 'SH600031': 0.16, 'SH600036': 3.93, 'SH600037': 0.62, 'SH600035': 0.16, 'SH600058': 0.2, 'SH600110': 0.13, 'SH600508': 0.19, 'SZ000402': 0.62, 'SH600115': 0.1, 'SH600117': 0.13, 'SZ000423': 0.22, 'SH600348': 0.34, 'SZ000518': 0.14, 'SH600500': 0.26, 'SH600660': 0.37, 'SH600057': 0.09, 'SH600744': 0.12, 'SH600747': 0.11, 'SH600740': 0.09, 'SH600741': 0.17, 'SH600621': 0.11, 'SZ000698': 0.14, 'SH600851': 0.19, 'SZ000900': 0.28, 'SH600854': 0.1, 'SH600868': 0.25, 'SH600428': 0.3, 'SZ000630': 0.36, 'SH600811': 0.3, 'SZ000735': 0.1, 'SZ000737': 0.09, 'SZ000066': 0.19, 'SH600331': 0.25, 'SH600183': 0.27, 'SH600333': 0.1, 'SZ000581': 0.25, 'SZ000425': 0.11, 'SZ000983': 0.49, 'SH600236': 0.25, 'SH600026': 0.45, 'SH600339': 0.08, 'SH600231': 0.16, 'SH600188': 0.27, 'SH600022': 0.2, 'SH600166': 0.08, 'SH600350': 0.37, 'SH600519': 1.14, 'SZ000063': 1.49, 'SH600690': 0.44, 'SZ000758': 0.24, 'SH600296': 0.26, 'SH601607': 0.17, 'SHT00018': 0.8, 'SZ000039': 0.78, 'SZ000599': 0.1, 'SH600198': 0.21, 'SZ000917': 0.15, 'SZ000916': 0.22, 'SZ000912': 0.21, 'SH600190': 0.11, 'SH600196': 0.25, 'SH600583': 0.54, 'SH600581': 0.12, 'SZ000027': 0.6, 'SZ000629': 0.52, 'SH600585': 0.32, 'SZ000021': 0.26, 'SZ000625': 0.25, 'SZ000623': 0.18, 'SZ000024': 0.42, 'SH600221': 0.13, 'SH600220': 0.17}
        timetag = C.get_bar_timetag(C.barpos)
        stock_list = list(data.keys())
        print(stock_list)

        #设置需要写入的扩展数据股票列表
        #reset_extend_data_stock_list(扩展数据名称, 股票列表)
        reset_extend_data_stock_list(C.extencd_name, stock_list)
        # 执行写入扩展数据
        # set_extend_data_value（扩展数据名称，时间戳(毫秒)，数据）
        set_extend_data_value(C.extencd_name, timetag, data)
        print('写入完成')
```

### 扩展数据展示

![扩展数据](https://dict.thinktrader.net/assets/%E5%86%85%E7%BD%AEAPI_%E6%89%A9%E5%B1%95%E6%95%B0%E6%8D%AE-58079b49.png)

#### 每1分钟统计一次市场涨跌情况

示例

```py
# coding:gbk
import datetime as dt
def on_timer(ContextInfo):
    ls = globals().get("stock_list")
    now_time = dt.datetime.now().strftime("%Y%m%d %H:%M:%S")
    # 取tick数据
    ticks = ContextInfo.get_full_tick(ls)

    # 涨跌统计,并去除停牌股
    profit_ls = [i for i in ticks if ticks[i]["lastPrice"] > ticks[i]["lastClose"] and ticks[i]["openInt"] != 1]
    loss_ls = [i for i in ticks if ticks[i]["lastPrice"] < ticks[i]["lastClose"] and ticks[i]["openInt"] != 1]
    print(f"{now_time}: 涨家数{len(profit_ls)}; 跌家数{len(loss_ls)}")

def init(ContextInfo):
    globals()["stock_list"] = get_stock_list_in_sector("沪深京A股")
    # 自2023-12-31 23:59:59后每60s运行一次on_timer
    tid=ContextInfo.schedule_run(on_timer,'20231231235959',3,dt.timedelta(seconds=60),'my_timer')
    # 取消任务组为"my_timer"的任务
    # # ContextInfo.cancel_schedule_run('my_timer')

    # 关于schedule_run函数的用法请阅读文档http://dict.thinktrader.net/innerApi/system_function.html?id=7zqjlm#contextinfo-schedule-run-%E8%AE%BE%E7%BD%AE%E5%AE%9A%E6%97%B6%E5%99%A8

```

## 交易下单示例

### 按品种划分

#### 股票

```py
#coding:gbk
def handlebar(ContextInfo):
    if not ContextInfo.is_last_bar():
        return
    # 单股单账号股票最新价买入 100 股（1 手）
    passorder(23, 1101, 'test', '600000.SH', 5, 0, 100, '',1,'',ContextInfo)
    # 单股单账号股票最新价卖出 100 股（1 手）
    passorder(24, 1101, 'test', '600000.SH', 5, 0, 100, '',1,'',ContextInfo)
    # 单股单账号沪市股票市价买入 100 股（1 手），沪市市价存在保护限价，Price参数为保护限价，买入为投资者能够接受的最高买价，填0会自动填为涨停价
    passorder(23, 1101, 'test', '600000.SH', 42, 0, 100, '',1,'',ContextInfo)
    # 单股单账号沪市股票市价卖出 100 股（1 手），沪市市价存在保护限价，Price参数为保护限价，卖出为投资者能够接受的最低卖价，填0会自动填为跌停价
    passorder(24, 1101, 'test', '600000.SH', 42, 0, 100, '',1,'',ContextInfo)
    # 单股单账号京市股票最新价买入 101 股（1 手零 1 股）
    passorder(23, 1101, 'test', '430047.BJ', 5, 0, 101, '',1,'',ContextInfo)
    # 单股单账号京市股票最新价卖出 101 股（1 手零 1 股）
    passorder(24, 1101, 'test', '430047.BJ', 5, 0, 101, '',1,'',ContextInfo)
```

#### 基金

```py
def handlebar(ContextInfo):
    if not ContextInfo.is_last_bar():
        return

    # 申购 中证500指数ETF
    passorder(60, 1101, 'test', '510030.SH', 5, 0, 1, 2, ContextInfo)

    # 赎回 中证500指数ETF
    passorder(61, 1101, 'test', '510030.SH', 5, 0, 1, 2, ContextInfo)
```

#### 两融

```py
#coding:gbk
def handlebar(ContextInfo):
    if not ContextInfo.is_last_bar():
        return
    target = '000001.SZ'
    # 单股单账号股票指定价担保品买入 100 股（1 手）
    passorder(33, 1101, 'test', target, 11, 7, 100, ContextInfo)
    # 单股单账号股票指定价融资买入 100 股（1 手）
    passorder(27, 1101, 'test', target, 11, 7, 100, ContextInfo)
```

#### 期货

```py
#coding:gbk
def handlebar(ContextInfo):
    if not ContextInfo.is_last_bar():
        return

    # 单股单账号期货最新价开多螺纹钢2401 10 手
	target = 'rb2401.SF'
    passorder(0, 1101, 'test', target, 5, -1, 10, 1, ContextInfo)


    # 单股单账号期货指定价开空甲醇2401 10 手
	target = 'MA401.ZF'
    passorder(3, 1101, 'test', target, 11, 3000, 10, 1, ContextInfo)

    #期货四键平多300股指2311,优先平今 2手
	target = 'IF2311.IF'
	passorder(6, 1101, 'test', target, 5, -1, 2, 1, ContextInfo)

```

#### 期权

```py
#coding:gbk
def handlebar(ContextInfo):
    if not ContextInfo.is_last_bar():
        return
	target = '10005330.SHO' # 50ETF购12月2450合约

    # 单股单账号用最新价买入开仓期权合约target 2张
    passorder(50, 1101, 'test', target, 5, -1, 2, 1, ContextInfo)

    # 单股单账号用最新价卖出平仓期权合约target 2张
    passorder(51, 1101, 'test', target, 5, -1, 2, 1, ContextInfo)
```

#### 新股申购

```py
#coding:gbk
def init(C):
	ipoStock=get_ipo_data("STOCK")#返回新股信息
	print(ipoStock)
	accont = '123456789'
	for stock in ipoStock:
		ipo_price = ipoStock[stock]['issuePrice'] # 发行价
		maxPurchaseNum = ipoStock[stock]['maxPurchaseNum'] # 可申购额度
		passorder(23,1101, accont, stock,11,ipo_price, maxPurchaseNum,'新股申购',2,stock,C)
```

#### 债券

```py
#coding:gbk
def handlebar(ContextInfo):
    if not ContextInfo.is_last_bar():
        return
    # 单股单账号最新价可转债买入 20张
    passorder(23, 1101, 'test', '128123.SZ', 5, -1, 10, 1, ContextInfo)

```

#### ETF

```py
#coding:gbk
def handlebar(ContextInfo):
    if not ContextInfo.is_last_bar():
        return
    # 单股单账号 最新价买入上证etf 2000份
    passorder(23, 1101, 'test', '510050.SH', 5, -1, 2000, ContextInfo)

```

#### 组合交易

一键买卖（一篮子下单）

**功能描述：** 该示例演示如何用python进行一揽子股票买卖的交易操作

**代码示例：**

```py
#coding:gbk

def init(C):

	table=[
			{'stock':'600000.SH','weight':0.11,'quantity':100,'optType':23},
			{'stock':'600028.SH','weight':0.11,'quantity':200,'optType':24},
		]
	basket={'name':'basket1','stocks':table}
	set_basket(basket)
	# 按篮子数量下单， 下2份 # 即下两倍篮子
	pice = 2
	passorder(35,  #一键买卖
			2101,  # 表示按股票数量下单
			account,
			'basket1',  # 篮子名称
			5, # 最新价下单
			1,  # 价格，最新价时 该参数无效，需要填任意数占位
			pice, # 篮子份数
			'',2,'strReMark',C)

	# 按篮子权重下单
	table=[
			{'stock':'600000.SH','weight':0.4,'quantity':0,'optType':23}, # 40%
			{'stock':'600028.SH','weight':0.6,'quantity':0,'optType':24}, # 60%
		]
	basket={'name':'basket2','stocks':table}
	set_basket(basket)
	# 按组合权重 总额10000元
	money = 10000
	passorder(35,2102,account,'basket2',5,1,money,'',2,'strReMark',C)
```

#### 组合套利交易

提示

（`accountID`、`orderType` 特殊设置）

**用法**

**释义**：

**参数**

| 参数名称 | 描述 |
| --- | --- |
| accountID | 'stockAccountID, futureAccountID' |
| orderCode | 'basketName, futureName' |
| hedgeRatio | 套利比例（0 ~ 2 之间值，相当于 %0 至 200% 套利） |
| volume | 份数 \ 资金 \ 比例 |
| orderType | 参考下方 **orderType-下单方式（特殊设置）** |

**orderType - 下单方式（特殊设置）**

| 编号 | 项目 |
| --- | --- |
| 2331 | 组合、套利、合约价值自动套利、按组合股票数量方式下单 |
| 2332 | 组合、套利、按合约价值自动套利、按组合股票权重方式下单 |
| 2333 | 组合、套利、按合约价值自动套利、按账号可用方式下单 |

**示例**

```py

```

```

```

### 按功能划分

#### passorder 下单函数

本示例用于演示K线走完下单及立即下单的参数写法差异，旨在帮助您了解如何快速实现下单操作。

```py
#coding:gbk
c = 0
s = '000001.SZ'
def init(ContextInfo):
	# 立即下单 用最新价买入股票s 100股，且指定投资备注
	passorder(23,1101,account,s,5,0,100,'1',2,'tzbz',ContextInfo)
	pass

def handlebar(ContextInfo):
	if not ContextInfo.is_last_bar():
		#历史k线不应该发出实盘信号 跳过
		return

	if ContextInfo.is_last_bar():
		global c
		c +=1
		if c ==1:
			# 用14.00元限价买入股票s 100股
			passorder(23,1101,account,s,11,14.00,100,1,ContextInfo)  # 当前k线为最新k线 则立即下单
			# 用最新价限价买入股票s 100股
			passorder(23,1101,account,s,5,-1,100,0,ContextInfo)  # K线走完下单
			# 用最新价限价买入股票s 1000元
			passorder(23, 1102, account, s, 5, 0,1000, 2, ContextInfo)  # 不管是不是最新K线，立即下单
```

#### 集合竞价下单

本示例演示了利用定时器函数和passorder下单函数在集合竞价期间以指定价买入平安银行100股。

```py
#coding:gbk

import time
c = 0
s = '000001.SZ'
def init(ContextInfo):
	# 设置定时器，历史时间表示会在一次间隔时间后开始调用回调函数 比如本例中 5秒后会后第一次触发myHandlebar调用 之后五秒触发一次
	ContextInfo.run_time("myHandlebar","5nSecond","2019-10-14 13:20:00")

def myHandlebar(ContextInfo):
	global c
	now = time.strftime('%H%M%S')
	if c ==0 and '092500' >= now >= '091500':
		c += 1
		passorder(23,1101,account,s,11,14.00,100,2,ContextInfo) # 立即下单

def handlebar(ContextInfo):
	return
```

#### 止盈止损示例

```py

#coding:gbk

"""
1.账户内所有股票，当股价低于买入价10%止损卖出。
2.账户内所有股票，当股价高于前一天的收盘价10%时，开始监控一旦股价炸板（开板），以买三价卖出
"""

def init(C):
	C.ratio = 1
	if accountType == 'STOCK':
		C.sell_code = 24
	if accountType == 'CREDIT':
		C.sell_code = 34
	C.spare_list = C.get_stock_list_in_sector('不卖品种')

def handlebar(C):
	if not C.is_last_bar():
		return
	holdings = get_trade_detail_data(account, accountType, 'position')
	stock_list = [holding.m_strInstrumentID + '.' + holding.m_strExchangeID for holding in holdings]
	if stock_list:
		full_tick = C.get_full_tick(stock_list)
		for holding in holdings:
			stock = holding.m_strInstrumentID + '.' + holding.m_strExchangeID
			rate = holding.m_dProfitRate
			volume = holding.m_nCanUseVolume
			if not volume >= 100:
				continue
			if stock in C.spare_list:
				continue
			if rate < -0.1:
				msg = f'{stock} 盈亏比例 {rate} 小于-10% 卖出 {volume}股'
				print(msg)
				passorder(C.sell_code, 1101, account, stock, 14, -1, volume, '减仓模型', 2, msg, C)
				continue
			if stock in full_tick:
				current_price = full_tick[stock]['lastPrice']
				pre_price = full_tick[stock]['lastClose']
				high_price = full_tick[stock]['high']
				stop_price = pre_price * 1.2 if stock[:2] in ['30', '68'] else pre_price * 1.1
				stop_price = round(stop_price, 2)
				ask_price_3 = full_tick[stock]['bidPrice'][2]
				if not ask_price_3:
					print(f"{stock} {full_tick[stock]} 未取到三档盘口价 请检查客户端右下角 行情界面 是否选择了五档行情 本次跳过卖出")
					continue
				if high_price == stop_price and current_price < stop_price:
					msg = f"{stock} 涨停后 开板 卖出 {volume}股"
					print(msg)
					passorder(C.sell_code, 1101, account, stock, 14, -1, volume, '减仓模型', 2, msg, C)
					continue
```

#### passorder 下算法单函数

本示例由于演示如何下达算法单，具体算法参数请参考迅投投研平台客户端参数说明。

```py
#coding:gbk
import time

def init(C):
	userparam={
	'OrderType':1,  #表示要下算法
	'PriceType':0, # 卖5价下单
	'MaxOrderCount':12, # 最大委托次数
	'SuperPriceType':0,  # 超价类型，0表示按比例
	'SuperPriceRate':0.02,  # 超价2%下单
	'VolumeRate':0.1,  # 单笔下单比率 每次拆10%
	'VolumeType': 10,  # 单笔基准量类型
	'SingleNumMax':1000000,  # 单笔拆单最大值
	'PriceRangeType':0,  # 波动区间类型
	'PriceRangeRate':1,  # 波动区间值
	'ValidTimeType':1,  # 有效时间类型 1 表示按执行时间
	'ValidTimeStart':int(time.time()),  # 算法开始时间
	'ValidTimeEnd':int(time.time()+60*60),  # 算法结束时间
	'PlaceOrderInterval':10, # 报撤间隔
	'UndealtEntrustRule':0, # 未成委托处理数值 用卖5加挂单
	}
	target_vol = 2000000  # 股， 算法目标总量
	algo_passorder(23, 1101, account, '600000.SH', -1, -1, target_vol, '', 2, '普通算法', userparam, C)
	print('finish')
def handlebar(C):
	pass
```

#### 如何使用投资备注

投资备注功能是模型下单时指定的任意字符串(长度小于24)，即passorder的userOrderId参数，可以用于匹配委托或成交。有且只有passorder， algo_passorder, smart_algo_passorder下单函数支持投资备注功能。

```py
# encoding:gbk

note = 0

def get_new_note():
	global note
	note += 1
	return str(note)

def init(ContextInfo):
	ContextInfo.set_account(account)
	passorder(23, 1101, account, '000001.SZ', 5 ,0, 100, '', 2, get_new_note(), ContextInfo)

	orders = get_trade_detail_data(account, accountType, 'order')
	remark = [o.m_strRemark for o in orders]
	sysid_list = [o.m_strOrderSysID for o in orders]
	print(remark)

def handlebar(C):
	pass

def order_callback(C, O):
	print(O.m_strRemark, O.m_strOrderSysID)


def deal_callback(C, D):
	print(D.m_strRemark, D.m_strOrderSysID)
```

#### 如何获取委托持仓及资金数据

本示例用于演示如何通过函数获取指定账户的委托、持仓、资金数据。

```py
#coding:gbk

def to_dict(obj):
	attr_dict = {}
	for attr in dir(obj):
		try:
			if attr[:2] == 'm_':
				attr_dict[attr] = getattr(obj, attr)
		except:
			pass
	return attr_dict

def init(C):
	pass
	#orders, deals, positions, accounts = query_info(C)

def handlebar(C):
	if not C.is_last_bar():
		return
	orders, deals, positions, accounts = query_info(C)

def query_info(C):
	orders = get_trade_detail_data('8000000213', 'stock', 'order')
	for o in orders:
		print(f'股票代码: {o.m_strInstrumentID}, 市场类型: {o.m_strExchangeID}, 证券名称: {o.m_strInstrumentName}, 买卖方向: {o.m_nOffsetFlag}',
		f'委托数量: {o.m_nVolumeTotalOriginal}, 成交均价: {o.m_dTradedPrice}, 成交数量: {o.m_nVolumeTraded}, 成交金额:{o.m_dTradeAmount}')

	deals = get_trade_detail_data('8000000213', 'stock', 'deal')
	for dt in deals:
		print(f'股票代码: {dt.m_strInstrumentID}, 市场类型: {dt.m_strExchangeID}, 证券名称: {dt.m_strInstrumentName}, 买卖方向: {dt.m_nOffsetFlag}',
		f'成交价格: {dt.m_dPrice}, 成交数量: {dt.m_nVolume}, 成交金额: {dt.m_dTradeAmount}')

	positions = get_trade_detail_data('8000000213', 'stock', 'position')
	for dt in positions:
		print(f'股票代码: {dt.m_strInstrumentID}, 市场类型: {dt.m_strExchangeID}, 证券名称: {dt.m_strInstrumentName}, 持仓量: {dt.m_nVolume}, 可用数量: {dt.m_nCanUseVolume}',
		f'成本价: {dt.m_dOpenPrice:.2f}, 市值: {dt.m_dInstrumentValue:.2f}, 持仓成本: {dt.m_dPositionCost:.2f}, 盈亏: {dt.m_dPositionProfit:.2f}')

	accounts = get_trade_detail_data('8000000213', 'stock', 'account')
	for dt in accounts:
		print(f'总资产: {dt.m_dBalance:.2f}, 净资产: {dt.m_dAssureAsset:.2f}, 总市值: {dt.m_dInstrumentValue:.2f}',
		f'总负债: {dt.m_dTotalDebit:.2f}, 可用金额: {dt.m_dAvailable:.2f}, 盈亏: {dt.m_dPositionProfit:.2f}')

	return orders, deals, positions, accounts
```

#### 使用快速交易参数委托

本例展示如何使用快速交易参数(quickTrade)立刻进行委托。

```py
#coding:gbk

def after_init(C):
	#account变量是模型交易界面 添加策略时选择的资金账号 不需要手动填写
	#快速交易参数(quickTrade )填2 passorder函数执行后立刻下单 不会等待k线走完再委托。 可以在after_init函数 run_time函数注册的回调函数里进行委托
	msg = f"投资备注字符串 用来区分不同委托"
	passorder(23, 1101, account, '600000.SH', 5, -1, 200, '测试下单', 2, msg, C)
```

#### 调整至目标持仓

本示例由于演示如何调仓。

```py
#encoding:gbk

'''
调仓到指定篮子
'''

import pandas as pd
import numpy as np
import time
from datetime import timedelta,datetime

#自定义类 用来保存状态
class a():pass
A=a()
A.waiting_dict =  {}
A.all_order_ref_dict = {}
#撤单间隔 单位秒 超过间隔未成交的委托撤回重报
A.withdraw_secs = 30
#定义策略开始结束时间 在两者间时进行下单判断 其他时间跳过
A.start_time = '093000'
A.end_time = '150000'

def init(C):
	'''读取目标仓位 字典格式 品种代码:持仓股数, 可以读本地文件/数据库，当前在代码里写死'''
	A.final_dict = {"600000.SH" :10000, '000001.SZ' : 20000}
	'''设置交易账号 acount accountType是界面上选的账号 账号类型'''
	A.acct = account
	A.acct_type = accountType
	#定时器 定时触发指定函数
	C.run_time("f","1nSecond","2019-10-14 13:20:00","SH")

def f(C):
	'''定义定时触发的函数 入参是ContextInfo对象'''
	#记录本次调用时间戳
	t0 = time.time()
	final_dict=A.final_dict
	#本次运行时间字符串
	now = datetime.now()
	now_timestr = now.strftime("%H%M%S")
	#跳过非交易时间
	if now_timestr < A.start_time or now_timestr > A.end_time:
		return
	#获取账号信息
	acct = get_trade_detail_data(A.acct, A.acct_type, 'account')
	if len(acct) == 0:
		print(A.acct, '账号未登录 停止委托')
		return
	acct = acct[0]
	#获取可用资金
	available_cash = acct.m_dAvailable
	print(now, '可用资金', available_cash)
	#获取持仓信息
	position_list = get_trade_detail_data(A.acct, A.acct_type, 'position')
	#持仓数据 组合为字典
	position_dict = {i.m_strInstrumentID + '.' + i.m_strExchangeID : int(i.m_nVolume) for i in position_list}
	position_dict_available = {i.m_strInstrumentID + '.' + i.m_strExchangeID : int(i.m_nCanUseVolume) for i in position_list}
	#未持有的品种填充持股数0
	not_in_position_stock_dict = {i : 0 for i in final_dict if i not in position_dict}
	position_dict.update(not_in_position_stock_dict)
	#print(position_dict)
	stock_list = list(position_dict.keys())
	# print(stock_list)
	#获取全推行情
	full_tick = C.get_full_tick(stock_list)
	#print('fulltick', full_tick)
	#更新持仓状态记录
	refresh_waiting_dict(C)
	#撤超时委托
	order_list = get_trade_detail_data(A.acct, 'stock', 'order')
	if '091500'<= now_timestr <= '093000':#指定的范围內不撤单
		pass
	else:
		for order in order_list:
			#非本策略 本次运行记录的委托 不撤
			if order.m_strRemark not in A.all_order_ref_dict:
				continue
			#委托后 时间不到撤单等待时间的 不撤
			if time.time() - A.all_order_ref_dict[order.m_strRemark] < A.withdraw_secs:
				continue
			#对所有可撤状态的委托 撤单
			if order.m_nOrderStatus in [48,49,50,51,52,55,86,255]:
				print(f"超时撤单 停止等待 {order.m_strRemark}")
				cancel(order.m_strOrderSysID,A.acct,'stock',C)
	#下单判断
	for stock in position_dict:
		#有未查到的委托的品种 跳过下单 防止超单
		if stock in A.waiting_dict:
			print(f"{stock} 未查到或存在未撤回委托 {A.waiting_dict[stock]} 暂停后续报单")
			continue
		if stock in position_dict.keys():
			#print(position_dict[stock],target_vol,'1111')
			#到达目标数量的品种 停止委托
			target_vol = final_dict[stock] if stock in final_dict else 0
			if int(abs(position_dict[stock] - target_vol)) == 0:
				print(stock, C.get_stock_name(stock), '与目标一致')
				continue
			#与目标数量差值小于100股的品种 停止委托
			if abs(position_dict[stock] - target_vol) < 100:
				print(f"{stock} {C.get_stock_name(stock)} 目标持仓{target_vol} 当前持仓{position_dict[stock]} 差额小于100 停止委托")
				continue
			#持仓大于目标持仓 卖出
			if position_dict[stock]>target_vol:
				vol = int((position_dict[stock] - target_vol)/100)*100
				if stock not in position_dict_available:
					continue
				vol = min(vol, position_dict_available[stock])
				#获取买一价
				print(stock,'应该卖出')
				buy_one_price = full_tick[stock]['bidPrice'][0]
				#买一价无效时 跳过委托
				if not buy_one_price > 0:
					print(f"{stock} {C.get_stock_name(stock)} 取到的价格{buy_one_price}无效，跳过此次推送")
					continue
				print(f"{stock} {C.get_stock_name(stock)} 目标股数{target_vol} 当前股数{position_dict[stock]}")
				msg = f"{now.strftime('%Y%m%d%H%M%S')}_{stock}_sell_{vol}股"
				print(msg)
				#对手价卖出
				passorder(24,1101,A.acct,stock,14,-1,vol,'调仓策略',2,msg,C)
				A.waiting_dict[stock] = msg
				A.all_order_ref_dict[msg] = time.time()
			#持仓小于目标持仓 买入
			if position_dict[stock]<target_vol:
				vol = int((target_vol-position_dict[stock])/100)*100
				#获取卖一价
				sell_one_price = full_tick[stock]['askPrice'][0]
				#卖一价无效时 跳过委托
				if not sell_one_price > 0:
					print(f"{stock} {C.get_stock_name(stock)} 取到的价格{sell_one_price}无效，跳过此次推送")
					continue
				target_value = sell_one_price * vol
				if target_value > available_cash:
					print(f"{stock} 目标市值{target_value} 大于 可用资金{available_cash} 跳过委托")
					continue
				print(f"{stock} {C.get_stock_name(stock)} 目标股数{target_vol} 当前股数{position_dict[stock]}")
				msg = f"{now.strftime('%Y%m%d%H%M%S')}_{stock}_buy_{vol}股"
				print(msg)
				#对手价买入
				passorder(23,1101,A.acct,stock,14,-1,vol,'调仓策略',2,msg,C)
				A.waiting_dict[stock] = msg
				A.all_order_ref_dict[msg] = time.time()
				available_cash -= target_value
	#打印函数运行耗时 定时器间隔应大于该值
	print(f"下单判断函数运行完成 耗时{time.time() - t0}秒")

def refresh_waiting_dict(C):
	"""更新委托状态 入参为ContextInfo对象"""
	#获取委托信息
	order_list = get_trade_detail_data(A.acct,A.acct_type,'order')
	#取出委托对象的 投资备注 : 委托状态
	ref_dict = {i.m_strRemark : int(i.m_nOrderStatus) for i in order_list}
	del_list = []
	for stock in A.waiting_dict:
		if A.waiting_dict[stock] in ref_dict and ref_dict[A.waiting_dict[stock]] in [56, 53, 54]:
			#查到对应投资备注 且状态为成交 / 已撤 / 部撤， 从等待字典中删除
			print(f'查到投资备注 {A.waiting_dict[stock]}，的委托 状态{ref_dict[A.waiting_dict[stock]]} (56已成 53部撤 54已撤)从等待等待字典中删除')
			del_list.append(stock)
		if A.waiting_dict[stock] in ref_dict and ref_dict[A.waiting_dict[stock]] == 57:
			#委托状态是废单的 也停止等待 从等待字典中删除
			print(f"投资备注为{A.waiting_dict[stock]}的委托状态为废单 停止等待")
			del_list.append(stock)
	for stock in del_list:
		del A.waiting_dict[stock]
```

#### 获取融资融券账户可融资买入标的

```py
#coding:gbk
def init(C):

	r = get_assure_contract('123456789')
	if len(r) == 0:
		print('未取到担保明细')
	else:
		finable = [o.m_strInstrumentID+'.'+o.m_strExchangeID for o in r if o.m_eFinStatus==48]
		print('可融资买入标的:', finable)
```

#### 获取两融账号信息示例

```py
#coding:gbk

def init(C):
	account_str = '11800028'
	credit_account = query_credit_account(account_str, 1234, C)

def credit_account_callback(C,seq,result):
	print('可买担保品资金', result.m_dAssureEnbuyBalance)
```

#### 直接还款示例

该示例演示使用python进行融资融券账户的还款操作。

```py
#coding:gbk

def init(ContextInfo):
	# 用passorder函数进行融资融券账号的直接还款操作

	money = 10000  #还款金额
	#account='123456'
	s = '000001.SZ'  # 代码填任意股票，占位用
	passorder(32, 1101, account, s, 5, 0, money, 2, ContextInfo)
	# passorder(75, 1101, account, s, 5, 0, money, 2, ContextInfo) 专项直接还款
```

### 交易数据查询示例

```py
#coding:gbk

def to_dict(obj):
	attr_dict = {}
	for attr in dir(obj):
		try:
			if attr[:2] == 'm_':
				attr_dict[attr] = getattr(obj, attr)
		except:
			pass
	return attr_dict

def init(C):
	pass
	#orders, deals, positions, accounts = query_info(C)

def handlebar(C):
	if not C.is_last_bar():
		return
	orders, deals, positions, accounts = query_info(C)

def query_info(C):
	orders = get_trade_detail_data('8000000213', 'stock', 'order')
	for o in orders:
		print(f'股票代码: {o.m_strInstrumentID}, 市场类型: {o.m_strExchangeID}, 证券名称: {o.m_strInstrumentName}, 买卖方向: {o.m_nOffsetFlag}',
		f'委托数量: {o.m_nVolumeTotalOriginal}, 成交均价: {o.m_dTradedPrice}, 成交数量: {o.m_nVolumeTraded}, 成交金额:{o.m_dTradeAmount}')

	deals = get_trade_detail_data('8000000213', 'stock', 'deal')
	for dt in deals:
		print(f'股票代码: {dt.m_strInstrumentID}, 市场类型: {dt.m_strExchangeID}, 证券名称: {dt.m_strInstrumentName}, 买卖方向: {dt.m_nOffsetFlag}',
		f'成交价格: {dt.m_dPrice}, 成交数量: {dt.m_nVolume}, 成交金额: {dt.m_dTradeAmount}')

	positions = get_trade_detail_data('8000000213', 'stock', 'position')
	for dt in positions:
		print(f'股票代码: {dt.m_strInstrumentID}, 市场类型: {dt.m_strExchangeID}, 证券名称: {dt.m_strInstrumentName}, 持仓量: {dt.m_nVolume}, 可用数量: {dt.m_nCanUseVolume}',
		f'成本价: {dt.m_dOpenPrice:.2f}, 市值: {dt.m_dInstrumentValue:.2f}, 持仓成本: {dt.m_dPositionCost:.2f}, 盈亏: {dt.m_dPositionProfit:.2f}')

	accounts = get_trade_detail_data('8000000213', 'stock', 'account')
	for dt in accounts:
		print(f'总资产: {dt.m_dBalance:.2f}, 净资产: {dt.m_dAssureAsset:.2f}, 总市值: {dt.m_dInstrumentValue:.2f}',
		f'总负债: {dt.m_dTotalDebit:.2f}, 可用金额: {dt.m_dAvailable:.2f}, 盈亏: {dt.m_dPositionProfit:.2f}')

	return orders, deals, positions, accounts
```