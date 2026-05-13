---
url: "https://dict.thinktrader.net/innerApi/enum_constants.html"
title: "枚举常量 | 迅投知识库"
---

## opType - 操作类型

### 期货/股指期权/商品期权 \- 六键

| 数值 | 描述 |
| --- | --- |
| 0 | 开多 |
| 1 | 平昨多 |
| 2 | 平今多 |
| 3 | 开空 |
| 4 | 平昨空 |
| 5 | 平今空 |

### 期货/股指期权/商品期权 \- 四键

| 数值 | 描述 |
| --- | --- |
| 6 | 平多, 优先平今 |
| 7 | 平多, 优先平昨 |
| 8 | 平空, 优先平今 |
| 9 | 平空, 优先平昨 |

### 期货/股指期权/商品期权 \- 两键

| 数值 | 描述 |
| --- | --- |
| 10 | 卖出, 如有多仓, 优先平仓, 优先平今, 如有余量, 再开空 |
| 11 | 卖出, 如有多仓, 优先平仓, 优先平昨, 如有余量, 再开空 |
| 12 | 买入, 如有空仓, 优先平仓, 优先平今, 如有余量, 再开多 |
| 13 | 买入, 如有空仓, 优先平仓, 优先平昨, 如有余量, 再开多 |
| 14 | 买入, 不优先平仓 |
| 15 | 卖出, 不优先平仓 |

### 股票/ETF/可转债买卖

| 数值 | 描述 |
| --- | --- |
| 23 | 股票/ETF/可转债买入，或沪港通、深港通股票买入 |
| 24 | 股票/ETF/可转债卖出，或沪港通、深港通股票卖出 |

### 融资融券

| 数值 | 描述 |
| --- | --- |
| 27 | 融资买入 |
| 28 | 融券卖出 |
| 29 | 买券还券 |
| 30 | 直接还券 |
| 31 | 卖券还款 |
| 32 | 直接还款 |
| 33 | 担保品买入 |
| 34 | 担保品卖出 |

### 组合交易

| 数值 | 描述 |
| --- | --- |
| 25 | 组合买入，或沪港通、深港通的组合买入 |
| 26 | 组合卖出，或沪港通、深港通的组合卖出 |
| 27 | 融资买入 |
| 28 | 融券卖出 |
| 29 | 买券还券 |
| 31 | 卖券还款 |
| 33 | 担保品买入 |
| 34 | 担保品卖出 |
| 35 | 普通账号一键买卖 |
| 36 | 信用账号一键买卖 |
| 40 | 期货组合开多 |
| 43 | 期货组合开空 |
| 46 | 期货组合平多, 优先平今 |
| 47 | 期货组合平多, 优先平昨 |
| 48 | 期货组合平空, 优先平今 |
| 49 | 期货组合平空, 优先平昨 |

### ETF期权交易

| 数值 | 描述 |
| --- | --- |
| 50 | 买入开仓 |
| 51 | 卖出平仓 |
| 52 | 卖出开仓 |
| 53 | 买入平仓 |
| 54 | 备兑开仓 |
| 55 | 备兑平仓 |
| 56 | 认购行权 |
| 57 | 认沽行权 |
| 58 | 证券锁定 |
| 59 | 证券解锁 |

### ETF申赎交易

| 数值 | 描述 |
| --- | --- |
| 60 | 申购 |
| 61 | 赎回 |

### 专项两融

| 数值 | 描述 |
| --- | --- |
| 70 | 专项融资买入 |
| 71 | 专项融券卖出 |
| 72 | 专项买券还券 |
| 73 | 专项直接还券 |
| 74 | 专项卖券还款 |
| 75 | 专项直接还款 |

### 可转债转股/回售

| 数值 | 描述 |
| --- | --- |
| 80 | 普通账户转股 |
| 81 | 普通账户回售 |
| 82 | 信用账户转股 |
| 83 | 信用账户回售 |

## orderType - 下单方式

提示

注意

一、期货不支持 1102 和 1202

二、对所有账号组的操作相当于对账号组里的每个账号做一样的操作，如：

1. `passorder(23, 1202, 'testS', '000001.SZ', 5, -1, 50000, ContextInfo)`，意思就是对账号组`testS` 里的所有账号都以最新价开仓买入 `50000` 元市值的 `000001.SZ`平安银行；
2. `passorder (60,1101,"test",'510050. SH', 5,-1,1, ContextInfo)`意思就是账号`test`申购`1`个单位 (`900000股`)的`华夏上证50ETF` (只申购不买入成分股)。

### 单股交易

| 数值 | 描述 |
| --- | --- |
| 1101 | 单股、单账号、普通、股/手方式下单 |
| 1102 | 单股、单账号、普通、金额（元）方式下单（只支持股票） |
| 1113 | 单股、单账号、总资产、比例 \[0 ~ 1\] 方式下单 |
| 1123 | 单股、单账号、可用、比例\[0 ~ 1\]方式下单 |

### 单股交易（账号组）

| 数值 | 描述 |
| --- | --- |
| 1201 | 单股、账号组（无权重）、普通、股/手方式下单 |
| 1202 | 单股、账号组（无权重）、普通、金额（元）方式下单（只支持股票） |
| 1213 | 单股、账号组（无权重）、总资产、比例 \[0 ~ 1\] 方式下单 |
| 1223 | 单股、账号组（无权重）、可用、比例 \[0 ~ 1\] 方式下单 |

### 组合交易（单账号）

| 数值 | 描述 |
| --- | --- |
| 2101 | 组合、单账号、普通、按组合股票数量（篮子中股票设定的数量）方式下单 \> 对应 volume 的单位为篮子的份 |
| 2102 | 组合、单账号、普通、按组合股票权重（篮子中股票设定的权重）方式下单 \> 对应 volume 的单位为元 |
| 2103 | 组合、单账号、普通、按账号可用方式下单 \> （底层篮子股票怎么分配？答：按可用资金比例后按篮子中股票权重分配，如用户没填权重则按相等权重分配）只对股票篮子支持 |

### 组合交易（账号组）

| 数值 | 描述 |
| --- | --- |
| 2201 | 组合、账号组（无权重）、普通、按组合股票数量方式下单 |
| 2202 | 组合、账号组（无权重）、普通、按组合股票权重方式下单 |
| 2203 | 组合、账号组（无权重）、普通、按账号可用方式下单只对股票篮子支持 |

## prType - 下单选价类型

关于使用市价指令的说明

1. 对于上交所（42,43,44,45）

1. 当`prType`选择 **市价类型** 时时，`price`为保护限价，范围为（0 - 9999）表示投资者能够接受的最高买入价或最低卖出价，即买入申报的成交价格和转限价的价格不高于保护限价，卖出申报的成交价格和转限价的价格不低于保护限价，当`price`指定为 `0` 时，保护限价为对应的涨跌停价
2. 融券卖出不允许使用市价指令
3. 集合竞价阶段不允许使用市价指令
2. 对于深交所（44,45,46,47,48）

1. 市价申报只适用于有价格涨跌幅限制证券。
2. 集合竞价阶段不允许使用市价指令
3. 对于北交所(42,43,44,45)

1. 当`prType`选择 **市价类型** 时时，`price`为保护限价，范围为（0 - 9999）表示投资者能够接受的最高买入价或最低卖出价，即买入申报的成交价格和转限价的价格不高于保护限价，卖出申报的成交价格和转限价的价格不低于保护限价，当`price`指定为 `0` 时，保护限价为对应的涨跌停价
2. 融券卖出不允许使用市价指令
3. 集合竞价阶段不允许使用市价指令

| 数值 | 描述 |
| --- | --- |
| -1 | 无效(只对于algo_passorder起作用) |
| 0 | 卖5价 |
| 1 | 卖4价 |
| 2 | 卖3价 |
| 3 | 卖2价 |
| 4 | 卖1价 |
| 5 | 最新价 |
| 6 | 买1价 |
| 7 | 买2价(组合不支持) |
| 8 | 买3价(组合不支持) |
| 9 | 买4价(组合不支持) |
| 10 | 买5价(组合不支持) |
| 11 | 指定价（只对单股情况支持,对组合交易不支持） |
| 12 | 涨跌停价(对手方最远端价格) |
| 13 | 挂单价(本方一档价格) |
| 14 | 对手价(对方一档价格) |
| 18 | 市价最优价\[郑商所\]\[期货\] (不支持模拟交易中使用) |
| 19 | 市价即成剩撤\[大商所\]\[期货\] (不支持模拟交易中使用) |
| 20 | 市价全额成交或撤\[大商所\]\[期货\] (不支持模拟交易中使用) |
| 21 | 市价最优一档即成剩撤\[中金所\]\[期货\] (不支持模拟交易中使用) |
| 22 | 市价最优五档即成剩撤\[中金所\]\[期货\] (不支持模拟交易中使用) |
| 23 | 市价最优一档即成剩转\[中金所\]\[期货\] (不支持模拟交易中使用) |
| 24 | 市价最优五档即成剩转\[中金所\]\[期货\] (不支持模拟交易中使用) |
| 26 | 限价即时全部成交否则撤单\[上交所\[期权\]\] \[深交所\[期权\]\] (不支持模拟交易中使用) |
| 27 | 市价即成剩撤\[上交所\]\[期权\] (不支持模拟交易中使用) |
| 28 | 市价即全成否则撤\[上交所\]\[期权\] (不支持模拟交易中使用) |
| 29 | 市价剩转限价\[上交所\]\[期权\] (不支持模拟交易中使用) |
| 42 | 最优五档即时成交剩余撤销申报\[上交所\[股票\]\]\[北交所\[股票\]\] (不支持模拟交易中使用) |
| 43 | 最优五档即时成交剩转限价申报\[上交所\[股票\]\]\[北交所\[股票\]\] (不支持模拟交易中使用) |
| 44 | 对手方最优价格委托\[上交所\[股票\]\]\[深交所\[股票\]\[北交所\[股票\]\]\[期权\]\] (不支持模拟交易中使用) |
| 45 | 本方最优价格委托\[上交所\[股票\]\]\[深交所\[股票\]\[北交所\[股票\]\]\[期权\]\] (不支持模拟交易中使用) |
| 46 | 即时成交剩余撤销委托\[深交所\]\[股票\]\[期权\] (不支持模拟交易中使用) |
| 47 | 最优五档即时成交剩余撤销委托\[深交所\]\[股票\]\[期权\] (不支持模拟交易中使用) |
| 48 | 全额成交或撤销委托\[深交所\]\[股票\]\[期权\] (不支持模拟交易中使用) |
| 49 | 盘后定价 |

## volume - 下单数量

提示

根据 orderType 值最后一位确定 volume 的单位

### 单股下单时

| 数值 | 描述 |
| --- | --- |
| 1 | 股 / 手 （股票: 股，股票期权: 张，期货: 手，可转债: 张，基金：份） |
| 2 | 金额（元） |
| 3 | 比例（%） |

### 组合下单时

| 数值 | 描述 |
| --- | --- |
| 1 | 按组合股票数量（份） |
| 2 | 按组合股票权重（元） |
| 3 | 按账号可用（%） |

## quicktrade - 快速下单

| 数值 | 描述 |
| --- | --- |
| 0 | 否 |
| 1 | 是 |
| 2 | 是 |

提示

`passorder`是对最后一根K线完全走完后生成的模型信号在下一根K线的第一个 tick 数据来时触发下单交易；

采用`quickTrade`参数设置为`1`时，非历史 bar 上执行时（`ContextInfo.is_last_bar()`为`True`），只要策略模型中调用到就触发下单交易。

`quickTrade`参数设置为`2`时，不判断 bar 状态，只要策略模型中调用到就触发下单交易，历史 bar 上也能触发下单，请谨慎使用。

## enum_ - 对象属性状态字段释义

### enum_EEntrustBS - 买卖方向

| 变量 | 数值 | 描述 |
| --- | --- | --- |
| `ENTRUST_BUY` | 48 | 买入，多 |
| `ENTRUST_SELL` | 49 | 卖出，空 |
| `ENTRUST_PLEDGE_IN` | 81 | 质押入库 |
| `ENTRUST_PLEDGE_OUT` | 66 | 质押出库 |

### EEntrustSubmitStatus - 报单状态

| 数值 | 描述 |
| --- | --- |
| 48 | 已经提交 |
| 49 | 撤单已经提交 |
| 50 | 修改已经提交 |
| 51 | 已经接受 |
| 52 | 报单已经被拒绝 |
| 53 | 撤单已经被拒绝 |
| 54 | 改单已经被拒绝 |

### enum_EEntrustTypes - 委托类型

| 变量名称 | 数值 | 描述 |
| --- | --- | --- |
| ENTRUST_BUY_SELL | 48 | 买卖 |
| ENTRUST_QUERY | 49 | 查询 |
| ENTRUST_CANCE | 50 | 撤单 |
| ENTRUST_APPEND | 51 | 补单 |
| ENTRUST_COMFIRM | 52 | 确认 |
| ENTRUST_BIG | 53 | 大宗 |
| ENTRUST_FIN | 54 | 融资委托 |
| ENTRUST_SLO | 55 | 融券委托 |
| ENTRUST_CLOSE | 56 | 信用平仓 |
| ENTRUST_CREDIT_NORMAL | 57 | 信用普通委托 |
| ENTRUST_CANCEL_OPEN | 58 | 撤单补单 |
| ENTRUST_TYPE_OPTION_EXERCISE | 59 | 行权 |
| ENTRUST_TYPE_OPTION_SECU_LOCK | 60 | 锁定 |
| ENTRUST_TYPE_OPTION_SECU_UNLOCK | 61 | 解锁 |
| ENTRUST_QUOTATION_REPURCHASE | 62 | 报价回购 |
| ENTRUST_TYPE_OPTION_ABANDON | 63 | 放弃行权 |
| ENTRUST_AGREEMENT_REPURCHASE | 64 | 协议回购 |
| ENTRUST_TYPE_OPTION_COMB_EXERCISE | 65 | 组合行权 |
| ENTRUST_TYPE_OPTION_BUILD_COMB_STRATEGY | 66 | 构建组合策略持仓 |
| ENTRUST_TYPE_OPTION_RELEASE_COMB_STRATEGY | 67 | 解除组合策略持仓 |
| ENTRUST_TYPE_LMT_LOAN | 68 | 转融通出借 |
| ENTRUST_TYPE_LMT_LOAN_DEFER | 69 | 转融通出借展期 |
| ENTRUST_TYPE_LMT_LOAN_FINISH_AHEAD | 70 | 转融通出借提前了结 |
| ENTRUST_CROSS_MARKET_IN | 71 | 跨市场场内 |
| ENTRUST_CROSS_MARKET_OUT | 72 | 跨市场场外 |

### enum_EEntrustStatus - 委托状态

| 变量名称 | 数值 | 描述 |
| --- | --- | --- |
| `ENTRUST_STATUS_WAIT_REPORTING` | 49 | 待报 |
| `ENTRUST_STATUS_REPORTED` | 50 | 已报（已报出到柜台，待成交） |
| `ENTRUST_STATUS_REPORTED_CANCEL` | 51 | 已报待撤（对已报状态的委托撤单吗，等待柜台处理撤单请求） |
| `ENTRUST_STATUS_PARTSUCC_CANCEL` | 52 | 部成待撤（已报到柜台，已有部分成交，已发出对剩余部分的撤单，待柜台处理撤单请求） |
| `ENTRUST_STATUS_PART_CANCEL` | 53 | 部撤（已报到柜台，已有部分成交，剩余部分已撤） |
| `ENTRUST_STATUS_CANCELED` | 54 | 已撤 |
| `ENTRUST_STATUS_PART_SUCC` | 55 | 部成（已报到柜台，已有部分成交） |
| `ENTRUST_STATUS_SUCCEEDED` | 56 | 已成 |
| `ENTRUST_STATUS_JUNK` | 57 | 废单（不符合报单条件，委托被打回，相关信息再委托的废单原因字段查看） |

![委托状态流程](https://dict.thinktrader.net/assets/%E5%A7%94%E6%89%98%E7%8A%B6%E6%80%81%E5%8F%98%E5%8A%A8-c15208aa.png)

### enum_EHedge_Flag_Type - 投保类型

| 变量名称 | 数值 | 描述 |
| --- | --- | --- |
| `HEDGE_FLAG_SPECULATION` | 49 | 投机 |
| `HEDGE_FLAG_ARBITRAGE` | 50 | 套利 |
| `HEDGE_FLAG_HEDGE` | 51 | 套保 |

### enum_EFutureTradeType - 成交类型

| 变量名称 | 数值 | 描述 |
| --- | --- | --- |
| `FUTRUE_TRADE_TYPE_COMMON` | 48 | 普通成交 |
| `FUTURE_TRADE_TYPE_OPTIONSEXECUTION` | 49 | 期权成交 |
| `FUTURE_TRADE_TYPE_OTC` | 50 | OTC 成交 |
| `FUTURE_TRADE_TYPE_EFPDIRVED` | 51 | 期转现衍生成交 |
| `FUTURE_TRADE_TYPE_COMBINATION_DERIVED` | 52 | 组合衍生成交 |

### enum_EBrokerPriceType - 价格类型

| 变量名称 | 数值 | 描述 |
| --- | --- | --- |
| `BROKER_PRICE_ANY` | 49 | 市价 |
| `BROKER_PRICE_LIMIT` | 50 | 限价 |
| `BROKER_PRICE_BEST` | 51 | 最优价 |
| `BROKER_PRICE_PROP_ALLOTMENT` | 52 | 配股 |
| `BROKER_PRICE_PROP_REFER` | 53 | 转托 |
| `BROKER_PRICE_PROP_SUBSCRIBE` | 54 | 申购 |
| `BROKER_PRICE_PROP_BUYBACK` | 55 | 回购 |
| `BROKER_PRICE_PROP_PLACING` | 56 | 配售 |
| `BROKER_PRICE_PROP_DECIDE` | 57 | 指定 |
| `BROKER_PRICE_PROP_EQUITY` | 58 | 转股 |
| `BROKER_PRICE_PROP_SELLBACK` | 59 | 回售 |
| `BROKER_PRICE_PROP_DIVIDEND` | 60 | 股息 |
| `BROKER_PRICE_PROP_SHENZHEN_PLACING` | 68 | 深圳配售确认 |
| `BROKER_PRICE_PROP_CANCEL_PLACING` | 69 | 配售放弃 |
| `BROKER_PRICE_PROP_WDZY` | 70 | 无冻质押 |
| `BROKER_PRICE_PROP_DJZY` | 71 | 冻结质押 |
| `BROKER_PRICE_PROP_WDJY` | 72 | 无冻解押 |
| `BROKER_PRICE_PROP_JDJY` | 73 | 解冻解押 |
| `BROKER_PRICE_PROP_ETF` | 81 | ETF申购 |
| `BROKER_PRICE_PROP_VOTE` | 75 | 投票 |
| `BROKER_PRICE_PROP_YYSGYS` | 92 | 要约收购预售 |
| `BROKER_PRICE_PROP_YSYYJC` | 77 | 预售要约解除 |
| `BROKER_PRICE_PROP_FUND_DEVIDEND` | 78 | 基金设红 |
| `BROKER_PRICE_PROP_FUND_ENTRUST` | 79 | 基金申赎 |
| `BROKER_PRICE_PROP_CROSS_MARKET` | 80 | 跨市转托 |
| `BROKER_PRICE_PROP_EXERCIS` | 83 | 权证行权 |
| `BROKER_PRICE_PROP_PEER_PRICE_FIRST` | 84 | 对手方最优价格 |
| `BROKER_PRICE_PROP_L5_FIRST_LIMITPX` | 85 | 最优五档即时成交剩余转限价 |
| `BROKER_PRICE_PROP_MIME_PRICE_FIRST` | 86 | 本方最优价格 |
| `BROKER_PRICE_PROP_INSTBUSI_RESTCANCEL` | 87 | 即时成交剩余撤销 |
| `BROKER_PRICE_PROP_L5_FIRST_CANCEL` | 88 | 最优五档即时成交剩余撤销 |
| `BROKER_PRICE_PROP_FULL_REAL_CANCEL` | 89 | 全额成交并撤单 |
| `BROKER_PRICE_PROP_DIRECT_SECU_REPAY` | 101 | 直接还券 |
| `BROKER_PRICE_PROP_FUND_CHAIHE` | 90 | 基金拆合 |
| `BROKER_PRICE_PROP_DEBT_CONVERSION` | 91 | 债转股 |
| `BROKER_PRICE_BID_LIMIT` | 92 | 港股通竞价限价 |
| `BROKER_PRICE_ENHANCED_LIMIT` | 93 | 港股通增强限价 |
| `BROKER_PRICE_RETAIL_LIMIT` | 94 | 港股通零股限价 |
| `BROKER_PRICE_PROP_INCREASE_SHARE` | 'j' | 增发 |
| `BROKER_PRICE_PROP_COLLATERAL_TRANSFER` | 107 | 担保品划转 |
| `BROKER_PRICE_PROP_NEEQ_PRICING` | 'w' | 定价（全国股转 \- 挂牌公司交易 \- 协议转让） |
| `BROKER_PRICE_PROP_NEEQ_MATCH_CONFIRM` | 'x' | 成交确认（全国股转 \- 挂牌公司交易 \- 协议转让） |
| `BROKER_PRICE_PROP_NEEQ_MUTUAL_MATCH_CONFIRM` | 'y' | 互报成交确认（全国股转 \- 挂牌公司交易 \- 协议转让） |
| `BROKER_PRICE_PROP_NEEQ_LIMIT` | 'z' | 限价（用于挂牌公司交易 \- 做市转让 \- 限价买卖和两网及退市交易-限价买卖） |

### enum_EOffset_Flag_Type - 操作类型

| 变量名称 | 数值 | 描述 |
| --- | --- | --- |
| `EOFF_THOST_FTDC_OF_INVALID` | -1 | 无效操作 |
| `EOFF_THOST_FTDC_OF_Open` | 48 | 买入，开仓 |
| `EOFF_THOST_FTDC_OF_Close` | 49 | 卖出，平仓 |
| `EOFF_THOST_FTDC_OF_ForceClose` | 50 | 强平 |
| `EOFF_THOST_FTDC_OF_CloseToday` | 51 | 平今 |
| `EOFF_THOST_FTDC_OF_CloseYesterday` | 52 | 平昨 |
| `EOFF_THOST_FTDC_OF_ForceOff` | 53 | 强减 |
| `EOFF_THOST_FTDC_OF_LocalForceClose` | 54 | 本地强平 |
| `EOFF_THOST_FTDC_OF_PLEDGE_IN` | 81 | 质押入库 |
| `EOFF_THOST_FTDC_OF_PLEDGE_OUT` | 66 | 质押出库 |
| `EOFF_THOST_FTDC_OF_ALLOTMENT` | 67 | 股票配股 |

### enum_EXTSubjectsStatus - 融资融券状态

| 变量名称 | 数值 | 描述 |
| --- | --- | --- |
| `SUBJECTS_STATUS_NORMAL` | 48 | 正常 |
| `SUBJECTS_STATUS_PAUSE` | 49 | 暂停 |
| `SUBJECTS_STATUS_NOT` | 50 | 作废 |

### enum_EXTCreditFundCtl - 融资交易控制

| 变量名称 | 数值 | 描述 |
| --- | --- | --- |
| `FUND_CTL_ONLY_FIN_BUY` | 48 | 只允许融资买入 |
| `FUND_CTL_ONLY_SELL_CASH_REPAY` | 49 | 只允许卖券还款 |
| `FUND_CTL_ALL` | 50 | 既允许融资买入又允许卖券还款 |
| `FUND_CTL_NONE` | 51 | 既不允许融资买入又不允许卖券还款 |

### enum_EXTCreditStkCtl - 融券交易控制

| 变量名称 | 数值 | 描述 |
| --- | --- | --- |
| `STK_CTL_ONLY_SLO_SELL` | 48 | 只允许融券卖出 |
| `STK_CTL_ONLY_BUY_SECU_REPAY` | 49 | 只允许买券还券 |
| `STK_CTL_ALL` | 50 | 既允许融券卖出又允许买券还券 |
| `STK_CTL_NONE` | 51 | 既不允许融券卖出又不允许买券还券 |

### enum_EXTSloTypeQueryMode - 查询类型

| 变量名称 | 数值 | 描述 |
| --- | --- | --- |
| `XT_SLOTYPE_QUERYMODE_NOMARL` | 48 | 普通 |
| `XT_SLOTYPE_QUERYMODE_SPECIAL` | 49 | 专项 |

### enum_EXTCompactType - 合约类型

| 变量名称 | 数值 | 描述 |
| --- | --- | --- |
| `COMPACT_TYPE_ALL` | 32 | 不限制 |
| `COMPACT_TYPE_FIN` | 48 | 融资 |
| `COMPACT_TYPE_SLO` | 49 | 融券 |

### enum_EXTCompactStatus - 合约状态

| 变量名称 | 数值 | 描述 |
| --- | --- | --- |
| `COMPACT_STATUS_ALL` | 32 | 不限制 |
| `COMPACT_STATUS_UNDONE` | 48 | 未归还 |
| `COMPACT_STATUS_PART_DONE` | 49 | 部分归还 |
| `COMPACT_STATUS_DONE` | 50 | 已归还 |
| `COMPACT_STATUS_DONE_BY_SELF` | 51 | 自行了结 |
| `COMPACT_STATUS_DONE_BY_HAND` | 52 | 手工了结 |
| `COMPACT_STATUS_NOT_DEBT` | 53 | 未形成负债 |
| `COMPACT_STATUS_EXPIRY` | 54 | 合约已过期 |

### enum_EXTCompactBrushSource - 头寸来源

| 变量名称 | 数值 | 描述 |
| --- | --- | --- |
| `XT_COMPACT_BRUSH_SOURCE_ALL` | 32 | 不限制 |
| `XT_COMPACT_BRUSH_SOURCE_NORMAL` | 48 | 普通头寸 |
| `XT_COMPACT_BRUSH_SOURCE_SPECIAL` | 49 | 专项头寸 |

### enum_EXTSpecialAssure - 是否可以用融券资金买入

| 变量名称 | 数值 | 描述 |
| --- | --- | --- |
| `ASSURE_USE_SLO_CASH_DISABLE` | 48 | 担保品买入不允许使用融券资金 |
| `ASSURE_USE_SLO_CASH_ENABLE` | 49 | 担保品买入允许使用融券资金 |

### enum_EOperationType - 下单操作类型/主要交易类型

| 变量名称 | 数值 | 描述 |
| --- | --- | --- |
| `OPT_OPEN_LONG` | 0 | 开多 |
| `OPT_CLOSE_LONG_HISTORY` | 1 | 平昨多 |
| `OPT_CLOSE_LONG_TODAY` | 2 | 平今多 |
| `OPT_OPEN_SHORT` | 3 | 开空 |
| `OPT_CLOSE_SHORT_HISTORY` | 4 | 平昨空 |
| `OPT_CLOSE_SHORT_TODAY` | 5 | 平今空 |
| `OPT_CLOSE_LONG_TODAY_FIRST` | 6 | 优先平今多 |
| `OPT_CLOSE_LONG_HISTORY_FIRST` | 7 | 优先平昨多 |
| `OPT_CLOSE_SHORT_TODAY_FIRST` | 8 | 平空优先平今 |
| `OPT_CLOSE_SHORT_HISTORY_FIRST` | 9 | 平空优先平昨 |
| `OPT_CLOSE_LONG_TODAY_HISTORY_THEN_OPEN_SHORT` | 10 | 卖出优先平今 |
| `OPT_CLOSE_LONG_HISTORY_TODAY_THEN_OPEN_SHORT` | 11 | 卖出优先平昨 |
| `OPT_CLOSE_SHORT_TODAY_HISTORY_THEN_OPEN_LONG` | 12 | 买入优先平今 |
| `OPT_CLOSE_SHORT_HISTORY_TODAY_THEN_OPEN_LONG` | 13 | 买入优先平昨 |
| `OPT_CLOSE_LONG` | 14 | 平多 |
| `OPT_CLOSE_SHORT` | 15 | 平空 |
| `OPT_OPEN` | 16 | 开仓 |
| `OPT_CLOSE` | 17 | 平仓 |
| `OPT_BUY` | 18 | 买入 |
| `OPT_SELL` | 19 | 卖出 |
| `OPT_FIN_BUY` | 20 | 融资买入 |
| `OPT_SLO_SELL` | 21 | 融券卖出 |
| `OPT_BUY_SECU_REPAY` | 22 | 买券还券 |
| `OPT_DIRECT_SECU_REPAY` | 23 | 直接还券 |
| `OPT_SELL_CASH_REPAY` | 24 | 卖券还款 |
| `OPT_DIRECT_CASH_REPAY` | 25 | 直接还款 |
| `OPT_FUND_SUBSCRIBE` | 26 | 基金申购 |
| `OPT_FUND_REDEMPTION` | 27 | 基金赎回 |
| `OPT_FUND_MERGE` | 28 | 基金合并 |
| `OPT_FUND_SPLIT` | 29 | 基金分拆 |
| `OPT_PLEDGE_IN` | 30 | 质押入库 |
| `OPT_PLEDGE_OUT` | 31 | 质押出库 |
| `OPT_OPTION_BUY_OPEN` | 32 | 买入开仓（个股期权交易） |
| `OPT_OPTION_SELL_CLOSE` | 33 | 卖出平仓（个股期权交易） |
| `OPT_OPTION_SELL_OPEN` | 34 | 卖出开仓（个股期权交易） |
| `OPT_OPTION_BUY_CLOSE` | 35 | 买入平仓（个股期权交易） |
| `OPT_OPTION_COVERED_OPEN` | 36 | 备兑开仓（个股期权交易） |
| `OPT_OPTION_COVERED_CLOSE` | 37 | 备兑平仓（个股期权交易） |
| `OPT_OPTION_CALL_EXERCISE` | 38 | 认购行权（个股期权交易） |
| `OPT_OPTION_PUT_EXERCISE` | 39 | 认沽行权（个股期权交易） |
| `OPT_OPTION_SECU_LOCK` | 40 | 证券锁定（个股期权交易） |
| `OPT_OPTION_SECU_UNLOCK` | 41 | 证券解锁（个股期权交易） |
| `OPT_N3B_PRICE_BUY` | 42 | 协议转让-定价买入 |
| `OPT_N3B_PRICE_SELL` | 43 | 协议转让-定价卖出 |
| `OPT_N3B_CONFIRM_BUY` | 44 | 协议转让-成交确认买入 |
| `OPT_N3B_CONFIRM_SELL` | 45 | 协议转让-成交确认卖出 |
| `OPT_N3B_REPORT_CONFIRM_BUY` | 46 | 协议转让-互报成交确认买入 |
| `OPT_N3B_REPORT_CONFIRM_SELL` | 47 | 协议转让-互报成交确认卖出 |
| `OPT_N3B_LIMIT_PRICE_BUY` | 48 | 全国股转-限价买入 |
| `OPT_N3B_LIMIT_PRICE_SELL` | 49 | 全国股转-限价卖出 |
| `OPT_FUTURE_OPTION_EXERCISE` | 50 | 期货期权行权 |
| `OPT_CONVERT_BONDS` | 51 | 可转债转股 |
| `OPT_SELL_BACK_BONDS` | 52 | 可转债回售 |
| `OPT_STK_ALLOTMENT` | 53 | 股票配股 |
| `OPT_STK_INCREASE_SHARE` | 54 | 股票增发 |
| `OPT_COLLATERAL_TRANSFER_IN` | 55 | 担保品划入 |
| `OPT_COLLATERAL_TRANSFER_OUT` | 56 | 担保品划出 |
| `OPT_BLOCK_INTENTION_BUY` | 57 | 意向申报买入 |
| `OPT_BLOCK_INTENTION_SELL` | 58 | 意向申报卖出 |
| `OPT_BLOCK_PRICE_BUY` | 59 | 定价申报买入 |
| `OPT_BLOCK_PRICE_SELL` | 60 | 定价申报卖出 |
| `OPT_BLOCK_CONFIRM_BUY` | 61 | 成交申报买入 |
| `OPT_BLOCK_CONFIRM_SELL` | 62 | 成交申报卖出 |
| `OPT_BLOCK_CLOSE_PRICE_BUY` | 63 | 盘后定价买入 |
| `OPT_BLOCK_CLOSE_PRICE_SELL` | 64 | 盘后定价卖出 |
| `OPT_GOLD_PRICE_DELIVERY_BUY` | 65 | 黄金交割买 |
| `OPT_GOLD_PRICE_DELIVERY_SELL` | 66 | 黄金交割卖 |
| `OPT_GOLD_PRICE_MIDDLE_BUY` | 67 | 黄金中立仓买 |
| `OPT_GOLD_PRICE_MIDDLE_SELL` | 68 | 黄金中立仓卖 |
| `OPT_COMPOSE_ONEKEY_BUYSELL` | 69 | 组合交易一键买卖 |
| `OPT_COMPOSE_GGT_BUY` | 70 | 组合交易港股通买入 |
| `OPT_COMPOSE_GGT_SELL` | 71 | 组合交易港股通卖出 |
| `OPT_ODD_SELL` | 72 | 零股卖出 |
| `OPT_ETF_STOCK_BUY` | 73 | 成份股买入 |
| `OPT_ETF_STOCK_SELL` | 74 | 成份股卖出 |
| `OPT_OTC_FUND_SUBSCRIBE` | 200 | 场外基金认购 |
| `OPT_OTC_FUND_PURCHASE` | 201 | 场外基金申购 |
| `OPT_OTC_FUND_REDEMPTION` | 202 | 场外基金赎回 |
| `OPT_OTC_FUND_CONVERT` | 203 | 场外基金转换 |
| `OPT_OTC_FUND_BONUS_TYPE_UPDATE` | 204 | 场外基金分红方式变更 |
| `OPT_OTC_CONTRACTUAL_DEPOSIT` | 205 | 场外协议存款 |
| `OPT_OTC_NON_CONTRACTUAL_DEPOSIT` | 206 | 场外非协议存款 |
| `OPT_OTC_CONTRACTUAL_DEPOSIT_ASK` | 207 | 场外协议存款询价 |
| `OPT_OTC_NON_CONTRACTUAL_DEPOSIT_ASK` | 208 | 场外非协议存款询价 |
| `OPT_OTC_NON_CONTRACTUAL_DEPOSIT_CUR` | 209 | 场外非协议活期存款 |
| `OPT_OTC_DRAW_DEPOSIT` | 210 | 场外存单支取 |
| `OPT_OTC_STOCK_INQUIRY` | 230 | 网下询价 |
| `OPT_OTC_STOCK_PURCHASE` | 231 | 网下申购 |
| `OPT_OPTION_NS_DEPOSIT` | 1001 | 场外转账入金 |
| `OPT_OPTION_NS_WITHDRAW` | 1002 | 场外转账出金 |
| `OPT_OPTION_NS_INOUT` | 1003 | 场外互转 |
| `OPT_ETF_PURCHASE` | 1004 | ETF申购 |
| `OPT_ETF_REDEMPTION` | 1005 | ETF赎回 |
| `OPT_OUTER_BUY` | 1006 | 外盘买入 |
| `OPT_OUTER_SELL` | 1007 | 外盘卖出 |
| `OPT_OUTER_CAN_CLOSE_BUY` | 1008 | 外盘可平买仓 |
| `OPT_OUTER_CAN_CLOSE_SELL` | 1009 | 外盘可平卖仓 |
| `OPT_SLO_SELL_SPECIAL` | 1010 | 专项融券卖出 |
| `OPT_BUY_SECU_REPAY_SPECIAL` | 1011 | 专项买券还券 |
| `OPT_DIRECT_SECU_REPAY_SPECIAL` | 1012 | 专项直接还券 |
| `OPT_NEEQ_O3B_LIMIT_PRICE_BUY` | 1013 | 全国股转-两网及退市交易-限价买入 |
| `OPT_NEEQ_O3B_LIMIT_PRICE_SELL` | 1014 | 全国股转-两网及退市交易-限价卖出 |
| `OPT_IBANK_BOND_BUY` | 1015 | 投行债券买入 |
| `OPT_IBANK_BOND_SELL` | 1016 | 投行债券卖出 |
| `OPT_IBANK_FUND_REPURCHASE` | 1017 | 质押式融资回购 |
| `OPT_IBANK_BOND_REPURCHASE` | 1018 | 质押式融券回购 |
| `OPT_IBANK_BOND_REPAY` | 1019 | 质押式融资购回 |
| `OPT_IBANK_FUND_RETRIEVE` | 1020 | 质押式融券购回 |
| `OPT_INTEREST_FEE` | 1021 | 融券息费 |
| `OPT_FIN_BUY_SPECIAL` | 1022 | 专项融资买入 |
| `OPT_SELL_CASH_REPAY_SPECIAL` | 1023 | 专项卖券还款 |
| `OPT_DIRECT_CASH_REPAY_SPECIAL` | 1024 | 专项直接还款 |
| `OPT_FUND_PRICE_BUY` | 1025 | 货币基金申购 |
| `OPT_FUND_PRICE_SELL` | 1026 | 货币基金赎回 |
| `OPT_N3B_CALL_AUCTION_BUY` | 1027 | 协议转让-集合竞价买入 |
| `OPT_N3B_CALL_AUCTION_SELL` | 1028 | 协议转让-集合竞价卖出 |
| `OPT_N3B_AFTER_HOURS_BUY` | 1029 | 全国股转-盘后协议买入 |
| `OPT_N3B_AFTER_HOURS_SELL` | 1030 | 全国股转-盘后协议卖出 |
| `OPT_ETF_HEDGE` | 1031 | ETF套利 |
| `OPT_QUOTATION_REPURCHASE_BUY` | 1032 | 报价回购买入 |
| `OPT_QUOTATION_REPURCHASE_STOP` | 1033 | 报价回购终止续做 |
| `OPT_QUOTATION_REPURCHASE_BEFORE` | 1034 | 报价回购提前购回 |
| `OPT_QUOTATION_REPURCHASE_RESERVATION` | 1035 | 报价回购购回预约 |
| `OPT_QUOTATION_REPURCHASE_CANCEL` | 1036 | 报价回购取消预约 |
| `OPT_BLOCK_CONFIRM_MATCH_BUY` | 1037 | 成交申报配对买入 |
| `OPT_BLOCK_CONFIRM_MATCH_SELL` | 1038 | 成交申报配对卖出 |
| `OPT_FUTURE_OPTION_ABANDON` | 1039 | 期货期权放弃行权 |
| `OPT_ONEKEY_TRANSFER` | 1040 | 一键划转 |
| `OPT_ONEKEY_TRANSFER_IN` | 1041 | 一键划入 |
| `OPT_ONEKEY_TRANSFER_OUT` | 1042 | 一键划出 |
| `OPT_AFTER_FIX_BUY` | 1043 | 盘后定价买入 |
| `OPT_AFTER_FIX_SELL` | 1044 | 盘后定价卖 |
| `OPT_AGREEMENT_REPURCHASE_TRANSACTION_DEC_FORWARD` | 1045 | 成交申报正回购 |
| `OPT_AGREEMENT_REPURCHASE_TRANSACTION_DEC_REVERSE` | 1046 | 成交申报逆回购 |
| `OPT_AGREEMENT_REPURCHASE_EXPIRE_CONFIRM` | 1047 | 到期确认 |
| `OPT_AGREEMENT_REPURCHASE_ADVANCE_REPURCHASE` | 1048 | 提前购回正回购 |
| `OPT_AGREEMENT_REPURCHASE_ADVANCE_REVERSE` | 1049 | 提前购回逆回购 |
| `OPT_AGREEMENT_REPURCHASE_EXPIRE_RENEW` | 1050 | 到期续做正回购 |
| `OPT_AGREEMENT_REPURCHASE_EXPIRE_REVERSE` | 1051 | 到期续做逆回购 |
| `OPT_TRANSACTION_IN_CASH_BUY` | 1052 | 现券买入 |
| `OPT_TRANSACTION_IN_CASH_SELL` | 1053 | 现券卖出 |
| `OPT_OUTRIGHT_REPO_FUND_REPURCHASE` | 1054 | 买断式融资回购 |
| `OPT_OUTRIGHT_REPO_BOND_REPURCHASE` | 1055 | 买断式融券回购 |
| `OPT_OUTRIGHT_REPO_BOND_REPAY` | 1056 | 买断式融资购回 |
| `OPT_OUTRIGHT_REPO_FUND_RETRIEVE` | 1057 | 买断式融券购回 |
| `OPT_DISTRIBUTION_BUYING` | 1058 | 分销买入 |
| `OPT_FIXRATE_TO_FLOATINGRATE` | 1059 | 固定利率换浮动利率 |
| `OPT_FLOATINGRATE_TO_FIXRATE` | 1060 | 浮动利率换固定利率 |
| `OPT_IBANK_TRANSFER_OUT` | 1061 | 银行间转出托管 |
| `OPT_IBANK_TRANSFER_IN` | 1062 | 银行间转入托管 |
| `OPT_AGREEMENT_REPURCHASE_INTENTION_BUY` | 1063 | 意向申报正回购买入 |
| `OPT_AGREEMENT_REPURCHASE_INTENTION_SELL` | 1064 | 意向申报正回购卖出 |
| `OPT_AGREEMENT_REPURCHASE_BIZ_APPLY_CONFIRM` | 1065 | 协议回购成交申报确认 |
| `OPT_AGREEMENT_REPURCHASE_BIZ_APPLY_REJECT` | 1066 | 协议回购成交申报拒绝 |
| `OPT_AGREEMENT_REPURCHASE_CONTINUE_CONFIRM` | 1067 | 协议回购到期续做申报确认 |
| `OPT_AGREEMENT_REPURCHASE_CONTINUE_REJECT` | 1068 | 协议回购到期续做申报拒绝 |
| `OPT_AGREEMENT_REPURCHASE_INTENTION_CHANGE_BONDS` | 1069 | 协议回购换券申报 |
| `OPT_AGREEMENT_REPURCHASE_INTENTION_CHANGE_BONDS_CONFIRM` | 1070 | 协议回购换券申报确认 |
| `OPT_AGREEMENT_REPURCHASE_INTENTION_CHANGE_BONDS_REJECT` | 1071 | 协议回购换券申报拒绝 |
| `OPT_AGREEMENT_REPURCHASE_STOP_AHEAD_CONFIRM` | 1072 | 协议回购正回购提前终止申报确认 |
| `OPT_AGREEMENT_REPURCHASE_STOP_AHEAD_REJECT` | 1073 | 协议回购正回购提前终止申报拒绝 |
| `OPT_AGREEMENT_REPURCHASE_RELEASE_PLEDGE` | 1074 | 协议回购正回购方解除质押申报 |
| `OPT_AGREEMENT_REPURCHASE_RELEASE_PLEDGE_CONFIRM` | 1075 | 协议回购正回购解除质押申报确认 |
| `OPT_AGREEMENT_REPURCHASE_RELEASE_PLEDGE_REJECT` | 1076 | 协议回购正回购解除质押申报拒绝 |
| `OPT_AGREEMENT_REPURCHASE_EXPIRE_CONFIRM_SELL` | 1077 | 深圳到期确认卖出 |
| `OPT_LOAN_DISTRIBUTION_BUY` | 1078 | 债券分销 |
| `OPT_PREFERENCE_SHARES_BIDDING_BUY` | 1079 | 优先股竞价买入 |
| `OPT_PREFERENCE_SHARES_BIDDING_SELL` | 1080 | 优先股竞价卖出 |
| `OPT_TOC_BOND` | 1081 | 债券转托管 |
| `OPT_TOC_FUND` | 1082 | 基金转托管 |
| `OPT_IBANK_BORROW` | 1083 | 同业拆入 |
| `OPT_IBANK_LOAN` | 1084 | 同业拆出 |
| `OPT_IBANK_BORROW_REPAY` | 1085 | 拆入还款 |
| `OPT_IBANK_LOAN_REPAY` | 1086 | 拆出还款 |
| `OPT_FINANCIAL_PRODUCT_BUY` | 1087 | 理财产品申购 |
| `OPT_FINANCIAL_PRODUCT_SELL` | 1088 | 理财产品赎回 |
| `OPT_OPTION_COMB_EXERCISE` | 1089 | 组合行权 |
| `OPT_OPTION_BUILD_COMB_STRATEGY` | 1090 | 构建组合策略 |
| `OPT_OPTION_RELEASE_COMB_STRATEGY` | 1091 | 解除组合策略 |
| `OPT_AGREEMENT_REPURCHASE_REVERSE_STOP_AHEAD_CONFIRM` | 1092 | 协议回购逆回购提前终止申报确认 |
| `OPT_AGREEMENT_REPURCHASE_REVERSE_STOP_AHEAD_REJECT` | 1093 | 协议回购逆回购提前终止申报拒绝 |
| `OPT_AGREEMENT_REPURCHASE_REVERSE_RELEASE_PLEDGE` | 1094 | 协议回购逆回购方解除质押申报 |
| `OPT_AGREEMENT_REPURCHASE_REVERSE_RELEASE_PLEDGE_CONFIRM` | 1095 | 协议回购逆回购解除质押申报确认 |
| `OPT_AGREEMENT_REPURCHASE_REVERSE_RELEASE_PLEDGE_REJECT` | 1096 | 协议回购逆回购解除质押申报拒绝 |
| `OPT_BOND_TENDER` | 1097 | 债券投标 |
| `OPT_FINANCIAL_PRODUCT_CALL` | 1098 | 理财产品认购 |
| `OPT_NEEQ_O3B_CONTINUOUS_AUCTION_BUY` | 1099 | 全国股转-北交所买入 |
| `OPT_NEEQ_O3B_CONTINUOUS_AUCTION_SELL` | 1100 | 全国股转-北交所卖出 |
| `OPT_NEEQ_O3B_ASK_PRICE` | 1101 | 全国股转-申购-询价申报 |
| `OPT_NEEQ_O3B_PRICE_CONFIRM` | 1102 | 全国股转-申购-申购申报 |
| `OPT_NEEQ_O3B_BLOCKTRADING_BUY` | 1103 | 全国股转-大宗交易买入 |
| `OPT_NEEQ_O3B_BLOCKTRADING_SELL` | 1104 | 全国股转-大宗交易卖出 |
| `OPT_LMT_LOAN_SET` | 1105 | 转融通非约定出借申报 |
| `OPT_LMT_LOAN_CONVENTION` | 1106 | 转融通约定出借申报 |
| `OPT_LMT_LOAN_RENEWAL` | 1107 | 转融通出借展期 |
| `OPT_LMT_LOAN_SETTLE_EARLY` | 1108 | 转融通出借提前了结 |
| `OPT_CROSS_MARKET_IN_ETF_PURCHASE` | 1109 | 跨市场ETF场内申购 |
| `OPT_CROSS_MARKET_IN_ETF_REDEMPTION` | 1110 | 跨市场ETF场内赎回 |
| `OPT_CROSS_MARKET_OUT_ETF_PURCHASE` | 1111 | 跨市场ETF场外申购 |
| `OPT_CROSS_MARKET_OUT_ETF_REDEMPTION` | 1112 | 跨市场ETF场外赎回 |
| `OPT_CREDIT_APPOINTMENT` | 1113 | 券源预约 |
| `OPT_OFF_IPO_PUB_PRICE` | 1114 | 网下申购-公开发行询价 |
| `OPT_OFF_IPO_PUB_PURCHASE` | 1115 | 网下申购-公开发行申购 |
| `OPT_OFF_IPO_NON_PUB_PRICE` | 1116 | 网下申购-非公开发行询价 |
| `OPT_OFF_IPO_NON_PUB_PURCHASE` | 1117 | 网下申购-非公开发行申购 |
| `OPT_IBANK_PUT` | 1118 | 债券回售 |
| `OPT_IBANK_BOND_BORROW` | 1119 | 债券借贷融入 |
| `OPT_IBANK_BOND_LEND` | 1120 | 债券借贷融出 |
| `OPT_IBANK_BOND_BORROW_REPAY` | 1121 | 债券借贷融入购回 |
| `OPT_IBANK_BOND_LEND_RETRIEVE` | 1122 | 债券借贷融出购回 |
| `OPT_IBANK_BOND_DISPLACE` | 1123 | 债券借贷-质押券置换 |
| `OPT_LENDING_INTEGRATE_INTO` | 1124 | 融券通-预约融券融入 |
| `OPT_LENDING_MELT_OUT` | 1125 | 融券通-预约融券融出 |
| `OPT_FICC_MANUAL_DECLARE_BUY` | 1126 | 固收业务-点击成交-报价申报买入 |
| `OPT_FICC_MANUAL_DECLARE_SELL` | 1127 | 固收业务-点击成交-报价申报卖出 |
| `OPT_FICC_MANUAL_CONFIRM_BUY_CONFIRM` | 1128 | 固收业务-点击成交-报价确认-买入-确认 |
| `OPT_FICC_MANUAL_CONFIRM_BUY_REJECT` | 1129 | 固收业务-点击成交-报价确认-买入-拒绝 |
| `OPT_FICC_MANUAL_CONFIRM_SELL_CONFIRM` | 1130 | 固收业务-点击成交-报价确认-卖出-确认 |
| `OPT_FICC_MANUAL_CONFIRM_SELL_REJECT` | 1131 | 固收业务-点击成交-报价确认-卖出-拒绝 |
| `OPT_FICC_CONSULT_DECLARE_BUY` | 1132 | 固收业务-协商成交-协商申报买入 |
| `OPT_FICC_CONSULT_DECLARE_SELL` | 1133 | 固收业务-协商成交-协商申报卖出 |
| `OPT_FICC_CONSULT_CONFIRM_BUY_CONFIRM` | 1134 | 固收业务-协商成交-协商确认-买入-确认 |
| `OPT_FICC_CONSULT_CONFIRM_BUY_REJECT` | 1135 | 固收业务-协商成交-协商确认-买入-拒绝 |
| `OPT_FICC_CONSULT_CONFIRM_SELL_CONFIRM` | 1136 | 固收业务-协商成交-协商确认-卖出-确认 |
| `OPT_FICC_CONSULT_CONFIRM_SELL_REJECT` | 1137 | 固收业务-协商成交-协商确认-卖出-拒绝 |
| `OPT_FICC_ENQUIRY_DECLARE_BUY` | 1138 | 固收业务-询价成交-询价申报买入 |
| `OPT_FICC_ENQUIRY_DECLARE_SELL` | 1139 | 固收业务-询价成交-询价申报卖出 |
| `OPT_FICC_ENQUIRY_REPLAY_BUY_CONFIRM` | 1140 | 固收业务-询价成交-报价回复-买入-确认 |
| `OPT_FICC_ENQUIRY_REPLAY_BUY_REJECT` | 1141 | 固收业务-询价成交-报价回复-买入-拒绝--预留字段 |
| `OPT_FICC_ENQUIRY_REPLAY_SELL_CONFIRM` | 1142 | 固收业务-询价成交-报价回复-卖出-确认 |
| `OPT_FICC_ENQUIRY_REPLAY_SELL_REJECT` | 1143 | 固收业务-询价成交-报价回复-卖出-拒绝--预留字段 |
| `OPT_FICC_ENQUIRY_INQUIRY_BUY_CONFIRM` | 1144 | 固收业务-询价成交-询价成交-买入-确认 |
| `OPT_FICC_ENQUIRY_INQUIRY_BUY_REJECT` | 1145 | 固收业务-询价成交-询价成交-买入-拒绝--预留字段 |
| `OPT_FICC_ENQUIRY_INQUIRY_SELL_CONFIRM` | 1146 | 固收业务-竞买成交-询价成交-卖出-确认 |
| `OPT_FICC_ENQUIRY_INQUIRY_SELL_REJECT` | 1147 | 固收业务-竞买成交-询价成交-卖出-拒绝--预留字段 |
| `OPT_FICC_BINDDING_RESERVE_BUY` | 1148 | 固收业务-竞买成交-竞买预约买入 |
| `OPT_FICC_BINDDING_RESERVE_SELL` | 1149 | 固收业务-竞买成交-竞买预约卖出 |
| `OPT_FICC_BINDDING_DECLARE_BUY` | 1150 | 固收业务-竞买成交-竞买申报买入 |
| `OPT_FICC_BINDDING_DECLARE_SELL` | 1151 | 固收业务-竞买成交-竞买申报卖出 |
| `OPT_FICC_BINDDING_PRICE_DECLARE_BUY` | 1152 | 固收业务-竞买成交-应价申报买入 |
| `OPT_FICC_BINDDING_PRICE_DECLARE_SELL` | 1153 | 固收业务-竞买成交-应价申报卖出 |
| `OPT_OPTION_BUY_CLOSE_THEN_OPEN` | 1154 | 买入优先平仓，个股期权交易业务补充类型 |
| `OPT_OPTION_SELL_CLOSE_THEN_OPEN` | 1155 | 卖出优先平仓 |
| `OPT_FUND_TRANSFER_IN` | 1156 | 资金划入 |
| `OPT_FUND_TRANSFER_OUT` | 1157 | 资金划出 |

### enum_EOrderType - 算法交易、普通交易类型

| 变量名称 | 数值 | 描述 |
| --- | --- | --- |
| `OTP_ORDINARY` | 0 | 常规 |
| `OTP_ALGORITHM` | 1 | 算法交易 |
| `OTP_RANDVOLUME` | 2 | 随机量交易 |
| `OTP_ALGORITHM3` | 3 | 算法交易3 |
| `OTP_ZXJT` | 4 | 中信建投算法 |
| `OTP_ZSGS` | 5 | 隔时交易 |
| `OTP_ORDINARY_BASKET_TRIGGER_SINGLE_ORDER` | 6 | 普通交易的触价单笔委托方式 |
| `OTP_ALGORITHM_BASKET_TRIGGER_SINGLE_ORDER` | 7 | 算法交易的触价单笔委托方式 |
| `OTP_ZXZQ` | 8 | 中信证券算法 |
| `OTP_GENUS` | 9 | 金纳算法 |
| `OTP_JAZZ` | 10 | 爵士算法 |
| `OTP_VWAP` | 11 | 智能VWAP |
| `OTP_TWAP` | 12 | 智能TWAP |
| `OTP_XTALGO` | 13 | 智能算法 |
| `OTP_HUACHUANG` | 14 | 华创算法 |
| `OTP_HUARUN` | 15 | 华润算法 |
| `OTP_CUSTOM` | 16 | 回转算法 |
| `OPT_EXTERN` | 17 | 主动算法 |
| `OTP_GUANGFA` | 18 | 广发算法 |

### enum_EPriceType - 价格类型

| 变量名称 | 数值 | 描述 |
| --- | --- | --- |
| `PRTP_SALE5` | 0 | 卖5 |
| `PRTP_SALE4` | 1 | 卖4 |
| `PRTP_SALE3` | 2 | 卖3 |
| `PRTP_SALE2` | 3 | 卖2 |
| `PRTP_SALE1` | 4 | 卖1 |
| `PRTP_LATEST` | 5 | 最新价 |
| `PRTP_BUY1` | 6 | 买1 |
| `PRTP_BUY2` | 7 | 买2 |
| `PRTP_BUY3` | 8 | 买3 |
| `PRTP_BUY4` | 9 | 买4 |
| `PRTP_BUY5` | 10 | 买5 |
| `PRTP_FIX` | 11 | 指定价 |
| `PRTP_MARKET` | 12 | 市价_涨跌停价 |
| `PRTP_HANG` | 13 | 挂单价 |
| `PRTP_COMPETE` | 14 | 对手价 |
| `PRTP_AUTO` | 15 | 自动盘口 |
| `PRTP_CLOSE` | 16 | 昨收价 |
| `PRTP_AVERAGE` | 17 | 大宗加权平均价 |
| `PRTP_MARKET_BEST` | 18 | 市价_最优价 |
| `PRTP_MARKET_CANCEL` | 19 | 市价_即成剩撤 |
| `PRTP_MARKET_CANCEL_ALL` | 20 | 市价_全额成交或撤 |
| `PRTP_MARKET_CANCEL_1` | 21 | 市价_最优1档即成剩撤 |
| `PRTP_MARKET_CANCEL_5` | 22 | 市价_最优5档即成剩撤 |
| `PRTP_MARKET_CONVERT_1` | 23 | 市价_最优1档即成剩转 |
| `PRTP_MARKET_CONVERT_5` | 24 | 市价_最优5档即成剩转 |
| `PRTP_STK_OPTION_ASK` | 25 | 询价 |
| `PRTP_STK_OPTION_FIX_CANCEL_ALL` | 26 | 限价即时全部成交否则撤单 |
| `PRTP_STK_OPTION_MARKET_CACEL_LEFT` | 27 | 市价即时成交剩余撤单 |
| `PRTP_STK_OPTION_MARKET_CANCEL_ALL` | 28 | 市价即时全部成交否则撤单 |
| `PRTP_STK_OPTION_MARKET_CONVERT_FIX` | 29 | 市价剩余转限价 |
| `PRTP_SALE6` | 30 | 卖6 |
| `PRTP_SALE7` | 31 | 卖7 |
| `PRTP_SALE8` | 32 | 卖8 |
| `PRTP_SALE9` | 33 | 卖9 |
| `PRTP_SALE10` | 34 | 卖10 |
| `PRTP_BUY6` | 35 | 买6 |
| `PRTP_BUY7` | 36 | 买7 |
| `PRTP_BUY8` | 37 | 买8 |
| `PRTP_BUY9` | 38 | 买9 |
| `PRTP_BUY10` | 39 | 买10 |
| `PRTP_UPPER_LIMIT_PRICE` | 40 | 涨停价 |
| `PRTP_LOWER_LIMIT_PRICE` | 41 | 跌停价 |
| `PRTP_MARKET_SH_CONVERT_5_CANCEL` | 42 | 最优五档即时成交剩余撤销 |
| `PRTP_MARKET_SH_CONVERT_5_LIMIT` | 43 | 最优五档即时成交剩转限价 |
| `PRTP_MARKET_PEER_PRICE_FIRST` | 44 | 对手方最优价格委托 |
| `PRTP_MARKET_MINE_PRICE_FIRST` | 45 | 本方最优价格委托 |
| `PRTP_MARKET_SZ_INSTBUSI_RESTCANCEL` | 46 | 即时成交剩余撤销委托 |
| `PRTP_MARKET_SZ_CONVERT_5_CANCEL` | 47 | 最优五档即时成交剩余撤销委托 |
| `PRTP_MARKET_SZ_FULL_REAL_CANCEL` | 48 | 全额成交或撤销委托 |
| `PRTP_AFTER_FIX_PRICE` | 49 | 盘后定价申报 |

### enum_ETaskStatus - 任务状态

| 变量名称 | 数值 | 描述 |
| --- | --- | --- |
| `TASK_STATUS_UNKNOWN` | 0 | 未知 |
| `TASK_STATUS_WAITING` | 1 | 等待 |
| `TASK_STATUS_COMMITING` | 2 | 提交中 |
| `TASK_STATUS_RUNNING` | 3 | 执行中 |
| `TASK_STATUS_PAUSE` | 4 | 暂停 |
| `TASK_STATUS_CANCELING_DEPRECATED` | 5 | 撤销中（已弃用） |
| `TASK_STATUS_EXCEPTION_CANCELING_DEPRECATED` | 6 | 异常撤销中（已弃用） |
| `TASK_STATUS_COMPLETED` | 7 | 完成 |
| `TASK_STATUS_CANCELED` | 8 | 已撤 |
| `TASK_STATUS_REJECTED` | 9 | 打回 |
| `TASK_STATUS_EXCEPTION_CANCELED` | 10 | 异常终止 |
| `TASK_STATUS_DROPPED` | 11 | 放弃（用于组合交易中，放弃补单） |
| `TASK_STATUS_FORCE_CANCELED_DEPRECATED` | 12 | 强制终止（已弃用） |