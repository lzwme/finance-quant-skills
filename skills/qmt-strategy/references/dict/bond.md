---
url: "https://dict.thinktrader.net/dictionary/bond.html"
title: "债券数据 | 迅投知识库"
---

## 可转债数据

### 获取可转债信息

可转债信息函数中，我们能够提供一系列重要的可转债详情。这些信息包括最新的转股价格，相关正股的代码，发行时的价格，总共发行的金额，强制赎回的价格，以及到期时的赎回价等关键参数。这些详细且全面的数据帮助投资者更好地理解和评估可转债的潜在值和风险，从而进行更明智的投资决策。

提示

1. 该函数为 [vip权限函数](https://xuntou.net/#/productvip)
2. 获取前需要先用`download_cb_data`下载可转债信息

**调用方法**

```py
# coding=utf-8
from xtquant import xtdata
# 下载转债信息
xtdata.download_cb_data()
# 获取转债信息
xtdata.get_cb_info(bond_code)
```

**参数**

| 字段 | 类型 | 说明 |
| --- | --- | --- |
| `bond_code` | `string` | `合约代码` |

**返回**

- 字典类型

| 字段 | 类型 | 说明 |
| --- | --- | --- |
| bondCode | str | 可转债代码 |
| bondName | str | 可转债简称 |
| stockCode | str | 正股代码 |
| stockName | str | 正股简称 |
| bondMaturity | float | 发行年限 |
| bondParvalue | float | 面值 |
| bondIssuePrice | float | 发行价格 |
| bondIssueSize | float | 发行总额（元） |
| bondReMainSize | float | 债券余额（元） |
| bondValueDate | int | 起息日期 |
| bondMaturityDate | int | 到期日期 |
| bondRateType | str | 利率类型 |
| bondCouponRate | float | 票面利率 |
| bondAddRate | float | 补偿利率 |
| bondPayPerYear | int | 年付息次数 |
| bondListDate | int | 上市日期 |
| delistDate | int | 摘牌日 |
| bondExchange | str | 上市地点 |
| convStartDate | int | 转股起始日，转股日 |
| convEndDate | int | 转股截止日 |
| firstConvPrice | float | 初始转股价 |
| bondConvPrice | float | 最新转股价 |
| rateClause | str | 利率说明 |
| forceRedeemTradeDate | int | 强赎最后交易日 |
| forceRedeemConvDate | int | 强赎最后转股日 |
| forceRedeemPrice | float | 强赎价格 |
| triggerForceRedeemPrice | float | 强赎触发价 |
| triggerRepurchasePrice | float | 回售触发价 |
| expireRedeemPrice | float | 到期赎回价 |
| analYTM | float | 纯债YTM(%) |
| analPTM | float | 剩余期限 |
| analAccruedinterst | float | 应计利息 |
| analStrbvalue | float | 纯债价值 |
| analStrbpremium | float | 纯债溢价率(%) |
| analConvvalue | float | 转股价值 |
| analConvpremiumratio | float | 转股溢价率(%) |
| analDuration | float | 久期 |
| analConvexity | float | 凸性 |
| infoProvisiontype | str | 条款类型，多种类型时使用 "," 分隔 |
| termYear | float | 债券期限（年） |
| interestType | int | 付息利率品种,1-浮动利率，2-固定利率，3-累进利率 |
| level | str | 债券评级 |
| forceRedeemPriceRatio | float | 强赎触发比(%) |
| redeemTerms | str | 强赎条款 |
| nextPutDate | int | 回售起始日 |
| putPrice | float | 回售价 |
| putConvertPriceRatio | float | 回售触发比(%) |
| putTerms | str | 回售条款 |
| triggerAdjustPrice | float | 下修触发价 |
| adjustPriceRatio | float | 下修触发比(%) |
| adjustTerms | str | 下修条款 |
| ytm | float | 到期收益率(%) |
| redeemStatus | str | 强赎状态 |
| adjustStatus | str | 下修状态 |
| readjustDate | int | 下修重算起始日 |
| regProvince | str | 所属省份 |

**示例：**

示例与返回值

```py
# coding=utf-8
from xtquant import xtdata
# 下载转债信息
xtdata.download_cb_data()
# 获取转债信息
cb_info = xtdata.get_cb_info("123219.SZ")
print(cb_info)
```

```
{'bondCode': '123219.SZ',
 'bondName': '宇瞳转债',
 'stockCode': '300790.SZ',
 'stockName': '宇瞳光学',
 'bondMaturity': 6.0,
 'bondParvalue': 100.0,
 'bondIssuePrice': 100.0,
 'bondIssueSize': 600000000.0,
 'bondReMainSize': 600000000.0,
 'bondValueDate': 20230811,
 'bondMaturityDate': 20290811,
 'bondRateType': '',
 'bondCouponRate': 0.3,
 'bondAddRate': 0.0,
 'bondPayPerYear': 0,
 'bondListDate': 20230829,
 'delistDate': 20290810,
 'bondExchange': '',
 'convStartDate': 20240219,
 'convEndDate': 20290810,
 'firstConvPrice': 15.29,
 'bondConvPrice': 15.32,
 'rateClause': '',
 'forceRedeemTradeDate': 0,
 'forceRedeemConvDate': 0,
 'forceRedeemPrice': 0.0,
 'triggerForceRedeemPrice': 19.916,
 'triggerRepurchasePrice': 10.724000000000002,
 'expireRedeemPrice': 0.0,
 'analYTM': 0.0,
 'analPTM': 5.737,
 'analAccruedinterst': 0.0,
 'analStrbvalue': 0.0,
 'analStrbpremium': 0.0,
 'analConvvalue': 0.0,
 'analConvpremiumratio': 0.0,
 'analDuration': 0.0,
 'analConvexity': 0.0,
 'infoProvisiontype': '',
 'termYear': 6.0,
 'interestType': 0,
 'level': 'A+',
 'forceRedeemPriceRatio': 130.0,
 'redeemTerms': '在本次发行可转换公司债券的转股期内，当下述两种情形的任意一种出现时，公司有权决定按照债券面值加当期应计利息的价格赎回全部或部分未转股的可转换公司债券：①在转股期内，如果公司股票在任何连续30个交易日中至少有15个交易日的收盘价格不低于当期转股价格的130%（含130%）；②当本次发行的可转换公司债券未转股的票面总金额不足3,000万元时。当期应计利息的计算公式为：IA=B×i×t/365其中：IA为当期应计利息；B为本次发行的可转换公司债券持有人持有的将赎回的可转换公司债券票面总金额；i为可转换公司债券当年票面利率；t为计息天数，即从上一个付息日起至本计息年度赎回日止的实际日历天数（算头不算尾）。若在前述30个交易日内发生过因除权、除息等引起公司转股价格调整的情形，则在调整前的交易日按调整前的转股价格和收盘价格计算，在调整后的交易日按调整后的转股价格和收盘价格计算。',
 'nextPutDate': 20270811,
 'putPrice': 100.0,
 'putConvertPriceRatio': 70.0,
 'putTerms': '（1）有条件回售条款在本次发行的可转换公司债券最后两个计息年度，如果公司股票在任何连续30个交易日的收盘价格低于当期转股价的70%时，可转换公司债券持有人有权将其持有的可转换公司债券全部或部分按面值加上当期应计利息的价格回售给公司。若在上述交易日内发生过转股价格因发生送红股、转增股本、增发新股、配股以及派发现金股利等情况（不包括因本次发行的可转换公司债券转股而增加的股本）而调整的情形，则在调整前的交易日按调整前的转股价格和收盘价格计算，在调整后的交易日按调整后的转股价格和收盘价格计算。如果出现转股价格向下修正的情况，则上述“连续30个交易日”须从转股价格调整之后的第一个交易日起重新计算。本次发行的可转换公司债券最后两个计息年度，可转换公司债券持有人在每年回售条件首次满足后可按上述约定条件行使回售权一次，若在首次满足回售条件而可转换公司债券持有人未在公司届时公告的回售申报期内申报并实施回售的，该计息年度不能再行使回售权，可转换公司债券持有人不能多次行使部分回售权。（2）附加回售条款若公司本次发行的可转换公司债券募集资金投资项目的实施情况与公司在募集说明书中的承诺情况相比出现重大变化，根据中国证监会的相关规定被视作改变募集资金用途或被中国证监会认定为改变募集资金用途的，可转换公司债券持有人享有一次回售的权利。可转换公司债券持有人有权将其持有的可转换公司债券全部或部分按债券面值加上当期应计利息价格回售给公司。可转换公司债券持有人在附加回售条件满足后，可以在公司公告后的附加回售申报期内进行回售，该次附加回售申报期内不实施回售的，自动丧失该回售权，不应再行使附加回售权。',
 'triggerAdjustPrice': 13.022,
 'adjustPriceRatio': 85.0,
 'adjustTerms': '在本次发行的可转换公司债券存续期间，当公司股票在任意连续30个交易日中至少有15个交易日的收盘价低于当期转股价格的85%时，公司董事会有权提出转股价格向下修正方案并提交公司股东大会审议表决。上述方案须经出席会议的股东所持表决权的三分之二以上通过方可实施。股东大会进行表决时，持有本次发行的可转换公司债券的股东应当回避。修正后的转股价格应不低于本次股东大会召开日前20个交易日公司股票交易均价和前1个交易日公司股票交易均价之间的较高者。同时，修正后的转股价格不得低于最近一期经审计的每股净资产值和股票面值。若在前述30个交易日内发生过因除权、除息等引起公司转股价格调整的情形，则转股价格调整日前的交易日按调整前的转股价格和收盘价计算，在转股价格调整日及之后的交易日按调整后的转股价格和收盘价计算。（2）修正程序如公司决定向下修正转股价格时，公司须在中国证监会指定的信息披露报刊及互联网网站上刊登股东大会决议公告，公告修正幅度和股权登记日及暂停转股期间（如需）等有关信息。从股权登记日后的第一个交易日（即转股价格修正日），开始恢复转股申请并执行修正后的转股价格。若转股价格修正日为转股申请日或之后，转换股份登记日之前，该类转股申请应按修正后的转股价格执行。',
 'ytm': 0.0,
 'redeemStatus': '0/15 | 30',
 'adjustStatus': '0/15 | 30',
 'readjustDate': 0,
 'regProvince': '广东省'}
```

### 获取可转债合约信息

此函数被设计为专门用于单一转债的查询，能够提供详尽的转债信息。通过使用这个函数，您可以获取到深度的特定转债数据，包括其涨跌停价格、上市日期、退市日期和期权到期日等关键信息。这种全面的信息将成为您理解和分析转债历史趋势以及当前状态的有力工具。

**调用方法**

```py
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
| InstrumentStatus | int | 合约已停牌日期（停牌第一天值为0，第二天为1，以此类推。注意，正常交易的股票该值也是0）获取股票停牌状态参考 [get_full_tick](http://docs.thinktrader.net/vip/pages/36f5df/#%E8%8E%B7%E5%8F%96%E5%85%A8%E6%8E%A8%E6%95%B0%E6%8D%AE) [openInt字段](http://docs.thinktrader.net/vip/pages/41b7c5/#tick-%E5%88%86%E7%AC%94%E6%95%B0%E6%8D%AE) |
| IsTrading | bool | 合约是否可交易 |
| IsRecent | bool | 是否是近月合约 |

**示例：**

示例与返回值

```py
# coding=utf-8
from xtquant import xtdata
code_detail = xtdata.get_instrument_detail('123219.SZ')
print(code_detail)
```

```
{'ExchangeID': 'SZ',
 'InstrumentID': '123219',
 'InstrumentName': '宇瞳转债',
 'ProductID': '',
 'ProductName': '',
 'ExchangeCode': '123219',
 'UniCode': '123219',
 'CreateDate': '0',
 'OpenDate': '20230829',
 'ExpireDate': 99999999,
 'PreClose': 122.828,
 'SettlementPrice': 122.828,
 'UpStopPrice': 147.394,
 'DownStopPrice': 98.262,
 'FloatVolume': 6000000.0,
 'TotalVolume': 6000000.0,
 'LongMarginRatio': 1.7976931348623157e+308,
 'ShortMarginRatio': 1.7976931348623157e+308,
 'PriceTick': 0.001,
 'VolumeMultiple': 1,
 'MainContract': 2147483647,
 'LastVolume': 2147483647,
 'InstrumentStatus': 0,
 'IsTrading': False,
 'IsRecent': False,
 'ProductTradeQuota': 1,
 'ContractTradeQuota': 0,
 'ProductOpenInterestQuota': 14592,
 'ContractOpenInterestQuota': 0}
```

### 获取可转债行情

为了获取转债的日线/1m/1d的k数据，以通过数据订阅形式获取最新行情`subscribe_quote`。如果您需要获取历史数据，可以使用`download_history_data`函数下载相关数据，然后使用`get_market_data_ex`函数提取所需的信息。这样，使用者就能获得最新和详细的转债最新数据，有助于做出更精准的投资决策。

**调用方法**

```py
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
xtdata.subscribe_quote('123219.SZ', period='1m', start_time='', end_time='20231026150000', count=1, callback=None)
# 下载指定合约历史行情
xtdata.download_history_data('123219.SZ', '1m', '20231026093000', '20231026150000')
# 获取指定合约历史行情
min_data = xtdata.get_market_data_ex(field_list=[], stock_list=['123219.SZ'], period='1m', start_time='', end_time='20231026150000', count=10, dividend_type='none', fill_data=True)
print(min_data)
```

```
{'123219.SZ':                          time     open  ...  preClose  suspendFlag
20231026111800  1698290280000  121.398  ...   121.380            0
20231026111900  1698290340000  121.269  ...   121.229            0
20231026112000  1698290400000  121.269  ...   121.269            0
20231026112100  1698290460000  121.269  ...   121.269            0
20231026112200  1698290520000  121.269  ...   121.269            0
20231026112300  1698290580000  121.269  ...   121.269            0
20231026112400  1698290640000  121.265  ...   121.269            0
20231026112500  1698290700000  121.465  ...   121.468            0
20231026112600  1698290760000  121.461  ...   121.356            0
20231026112700  1698290820000  121.352  ...   121.461            0

[10 rows x 11 columns]}
```