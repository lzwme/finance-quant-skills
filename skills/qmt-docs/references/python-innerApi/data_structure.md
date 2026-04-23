---
url: "https://dict.thinktrader.net/innerApi/data_structure.html"
title: "数据结构 | 迅投知识库"
---

## 数据类

### Tick - Tick 对象

行情快照数据

#### get\_market\_data\_ex/get\_full\_tick返回对象：

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
| `openInt` | `int` | `若是股票，则openInt含义为股票状态，非股票则是持仓量` [openInt字段说明](data_structure.md#openint-%E8%AF%81%E5%88%B8%E7%8A%B6%E6%80%81) |
| `transactionNum` | `float` | `成交笔数(期货没有，单独计算)` |
| `lastSettlementPrice` | `float` | `前结算(股票为0)` |
| `settlementPrice` | `float` | `今结算(股票为0)` |
| `askPrice` | `list[float]` | `多档委卖价` |
| `askVol` | `list[int]` | `多档委卖量` |
| `bidPrice` | `list[float]` | `多档委买价` |
| `bidVol` | `list[int]` | `多档委买量` |

#### get\_market\_data返回对象：

| 字段 | 数据类型 | 含义 |
| --- | --- | --- |
| `timetag` | `string` | `时间戳，格式为: %Y%m%d %H:%M:%S` |
| `lastPrice` | `float` | `最新价` |
| `open` | `float` | `开盘价` |
| `high` | `float` | `最高价` |
| `low` | `float` | `最低价` |
| `lastClose` | `float` | `前收盘价` |
| `amount` | `float` | `成交额` |
| `volume` | `float` | `成交量（手）` |
| `pvolume` | `float` | `原始成交量（股）【不推荐使用】` |
| `stockStatus` | `int` | `作废 参考openInt` |
| `openInt` | `float` | `若是股票，则openInt含义为股票状态，非股票则是持仓量` [openInt字段说明](data_structure.md#openint-%E8%AF%81%E5%88%B8%E7%8A%B6%E6%80%81) |
| `lastSettlementPrice` | `float` | `昨结算价` |
| `pe` | `float` | `对于股票是市盈率,对于ETF是iopv值` |
| `askPrice` | `list` | `委卖价` |
| `bidPrice` | `list` | `委买价` |
| `askVol` | `list` | `委卖量` |
| `bidVol` | `list` | `委买量` |
| `settlementPrice` | `float` | `今结算价` |

#### subscribe\_quote/subscribe\_whole\_quote回调对象：

同 `get_full_tick` 返回结构

### Bar - Bar对象

bar数据是指各种频率的行情数据

| 字段 | 数据类型 | 含义 |
| --- | --- | --- |
| `time` | `int` | `时间` |
| `open` | `float` | `开盘价` |
| `high` | `float` | `最高价` |
| `low` | `float` | `最低价` |
| `close` | `float` | `收盘价` |
| `volume` | `float` | `成交量` |
| `amount` | `float` | `成交额` |
| `settelementPrice` | `float` | `今结算` |
| `openInterest` | `float` | `持仓量` |
| `preClose` | `float` | `前收盘价` |
| `suspendFlag` | `int` | `停牌` 1停牌，0 不停牌 |

### l2quote - Level2行情快照

| 字段名 | 数据类型 | 解释 |
| --- | --- | --- |
| time | int | 时间戳 |
| stime | string | 时间戳字符串形式 |
| lastPrice | float | 最新价 |
| open | float | 开盘价 |
| high | float | 最高价 |
| low | float | 最低价 |
| amount | float | 成交额 |
| volume | int | 成交总量 |
| pvolume | int | 原始成交总量(未经过股手转换的成交总量) |
| stockStatus | int | 证券状态 |
| openInt | int | 持仓量 |
| transactionNum | int | 成交笔数(期货没有，单独计算) |
| lastClose | float | 前收盘价 |
| lastSettlementPrice | float | 前结算(股票为0) |
| settlementPrice | float | 今结算(股票为0) |
| askPrice | list\[float\] | 多档委卖价 |
| askVol | list\[int\] | 多档委卖量 |
| bidPrice | list\[float\] | 多档委买价 |
| bidVol | list\[int\] | 多档委买量 |

### l2quoteaux - Level2行情快照补充

| 字段名 | 数据类型 | 解释 |
| --- | --- | --- |
| time | int | 时间戳 |
| stime | string | 时间戳字符串形式 |
| avgBidPrice | float | 委买均价 |
| totalBidQuantity | int | 委买总量 |
| avgOffPrice | float | 委卖均价 |
| totalOffQuantity | int | 委卖总量 |
| withdrawBidQuantity | int | 买入撤单总量 |
| withdrawBidAmount | float | 买入撤单总额 |
| withdrawOffQuantity | int | 卖出撤单总量 |
| withdrawOffAmount | float | 卖出撤单总额 |

### l2order - Level2逐笔委托

| 字段名 | 数据类型 | 解释 |
| --- | --- | --- |
| time | int | 时间戳 |
| stime | float | 时间戳浮点数形式 |
| price | float | 委托价 |
| volume | int | 委托量 |
| entrustNo | int | 委托号 |
| entrustType | int | [委托类型](data_structure.md#entrusttype-%E5%A7%94%E6%89%98%E7%B1%BB%E5%9E%8B) |
| entrustDirection | int | 委托方向 |

提示

注：上交所的撤单信息在逐笔委托的委托方向，区分撤买撤卖

- 0 - 未知
- 1 - 买入
- 2 - 卖出
- 3 - 撤买（上交所）
- 4 - 撤卖（上交所）

### l2transaction - Level2逐笔成交

| 字段名 | 数据类型 | 解释 |
| --- | --- | --- |
| time | int | 时间戳 |
| stime | string | 时间戳字符串形式 |
| price | float | 成交价 |
| volume | int | 成交量 |
| amount | float | 成交额 |
| tradeIndex | int | 成交记录号 |
| buyNo | int | 买方委托号 |
| sellNo | int | 卖方委托号 |
| tradeType | int | 成交类型 |
| tradeFlag | int | 成交标志 |

提示

深交所逐笔成交的撤单标志，没有方向

- 0 - 未知
- 1 - 外盘，主买
- 2 - 内盘，主卖
- 3 - 撤单

### l2transactioncount - Level2逐笔成交统计

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

### l2orderqueue - Level2委买委卖队列

## 交易类

### Account - 账户对象

| 字段名 | 数据类型 | 解释 |
| --- | --- | --- |
| m\_strAccountID | str | 资金账号，用于识别不同的资金账户 |
| m\_nBrokerType | int | 账号类型，表示账号的具体种类 |
| m\_dMaxMarginRate | float | 保证金比率，通常用于期货账号 |
| m\_dFrozenMargin | float | 冻结保证金，指投资者在交易中被冻结的保证金金额 |
| m\_dFrozenCash | float | 冻结金额，指投资者在交易中被冻结的资金金额 |
| m\_dFrozenCommission | float | 冻结手续费，指投资者在交易中被冻结的手续费金额 |
| m\_dRisk | float | 风险度，指投资者账户的风险程度 |
| m\_dNav | float | 单位净值，用于表示基金的净值 |
| m\_dPreBalance | float | 期初权益，指期初时账户的资金金额 |
| m\_dBalance | float | 总资产，表示账户的总资金金额 |
| m\_dAvailable | float | 可用金额，指账户中可用于交易和提取的资金金额 |
| m\_dCommission | float | 手续费 (旧版本为 m\_dComission) |
| m\_dPositionProfit | float | 持仓盈亏，指当前持有的证券或期货合约的盈亏金额 |
| m\_dCloseProfit | float | 平仓盈亏，在期货交易中表示已经平仓的交易的盈亏金额 |
| m\_dCashIn | float | 出入金净值，表示账户中出入金的净额 |
| m\_dCurrMargin | float | 当前使用的保证金金额 |
| m\_dInitBalance | float | 初始权益，指账户初始时的权益金额 |
| m\_strStatus | str | 状态，表示账户的当前状态 |
| m\_dInitCloseMoney | float | 期初平仓盈亏，指账户初始时的平仓盈亏金额 |
| m\_dInstrumentValue | float | 总市值，表示持有的证券或期货合约的总市值 |
| m\_dDeposit | float | 入金，指账户中的入金金额 |
| m\_dWithdraw | float | 出金，指账户中的出金金额 |
| m\_dPreCredit | float | 上次信用额度，用于表示上次的信用额度 |
| m\_dPreMortgage | float | 上次质押，指上次的质押金额 |
| m\_dMortgage | float | 质押，指当前的质押金额 |
| m\_dCredit | float | 信用额度，表示账户的信用额度 |
| m\_dAssetBalance | float | 证券初始资金，表示股票账户的初始资金 |
| m\_strOpenDate | str | 起始日期，表示账户的起始日期 |
| m\_dFetchBalance | float | 可取金额，指账户中可取出的金额 |
| m\_strTradingDate | str | 交易日，表示当前的交易日期 |
| m\_dStockValue | float | 股票总市值，表示股票账户中持有的股票的总市值 |
| m\_dLoanValue | float | 债券总市值，表示账户中持有的债券的总市值 |
| m\_dFundValue | float | 基金总市值，包括ETF和封闭式基金在内的基金的总市值 |
| m\_dRepurchaseValue | float | 回购总市值，表示账户中持有的所有回购交易的总市值 |
| m\_dLongValue | float | 多单总市值，指现货账户中多单持仓的总市值 |
| m\_dShortValue | float | 空单总市值，指现货账户中空单持仓的总市值 |
| m\_dNetValue | float | 净持仓总市值，指现货账户中多单总市值减去空单总市值的差额 |
| m\_dAssureAsset | float | 净资产，表示账户的净资产金额 |
| m\_dTotalDebit | float | 总负债，表示账户的总负债金额 |
| m\_dEntrustAsset | float | 可信资产，用于校对账户资金的准确性 |
| m\_dInstrumentValueRMB | float | 总市值（人民币），指沪港通账户中的持仓证券的总市值 |
| m\_dSubscribeFee | float | 申购费，指申购基金时支付的费用 |
| m\_dGoldValue | float | 库存市值，表示黄金现货账户中黄金库存的市值 |
| m\_dGoldFrozen | float | 现货冻结，表示黄金现货账户中被冻结的黄金金额 |
| m\_dMargin | float | 占用保证金，用于维持保证金 |
| m\_strMoneyType | str | 币种，表示账户的资金所使用的货币种类 |
| m\_dPurchasingPower | float | 购买力，指账户可用于购买投资品的金额 |
| m\_dRawMargin | float | 原始保证金，指期货账户中的原始保证金金额 |
| m\_dBuyWaitMoney | float | 买入待交收金额（元），指账户中买入股票但尚未交收的金额 |
| m\_dSellWaitMoney | float | 卖出待交收金额（元），指账户中卖出股票但尚未交收的金额 |
| m\_dReceiveInterestTotal | float | 本期间应计利息，指账户本期间内应计的利息金额 |
| m\_dRoyalty | float | 权利金收支，指期货期权交易中的权利金收支金额 |
| m\_dFrozenRoyalty | float | 冻结权利金，指期货期权交易中被冻结的权利金金额 |
| m\_dRealUsedMargin | float | 实时占用保证金，用于股票期权交易中表示实时占用的保证金金额 |
| m\_dRealRiskDegree | float | 实时风险度，用于股票期权交易中表示实时的风险度 |

### Order - 委托对象

| 字段 | 数据类型 | 解释 |
| --- | --- | --- |
| m\_strAccountID | str | 资金账号，账号，账号，资金账号 |
| m\_strExchangeID | str | 证券市场 |
| m\_strExchangeName | str | 交易市场 |
| m\_strProductID | str | 品种代码 |
| m\_strProductName | str | 品种名称 |
| m\_strInstrumentID | str | 证券代码 |
| m\_strInstrumentName | str | 证券名称，合约名称 |
| m\_nRef | int | 订单编号 |
| m\_strOrderRef | str | 内部委托号，下单引用等于股票的内部委托号 |
| m\_nOrderPriceType | int | [EBrokerPriceType 类型，例如市价单、限价单](enum_constants.md#enum-ebrokerpricetype-%E4%BB%B7%E6%A0%BC%E7%B1%BB%E5%9E%8B) |
| m\_nDirection | int | [EEntrustBS 类型，操作，多空，期货多空，股票买卖永远是 48，其他的 dir 同理](enum_constants.md#enum-eentrustbs-%E4%B9%B0%E5%8D%96%E6%96%B9%E5%90%91) |
| m\_nOffsetFlag | int | [EOffset\_Flag\_Type类型，买卖/开平，用此字段区分股票买卖，期货开、平仓，期权买卖等](enum_constants.md#enum-eoffset-flag-type-%E6%93%8D%E4%BD%9C%E7%B1%BB%E5%9E%8B) |
| m\_nHedgeFlag | int | [EHedge\_Flag\_Type 类型，投保](enum_constants.md#enum-ehedge-flag-type) |
| m\_dLimitPrice | float | 委托价格，限价单的限价，即报价 |
| m\_nVolumeTotalOriginal | int | 委托数量，最初的委托数量 |
| m\_nOrderSubmitStatus | int | [EEntrustSubmitStatus 类型，报单状态，提交状态，股票中不需要报单状态](enum_constants.md#eentrustsubmitstatus-%E6%8A%A5%E5%8D%95%E7%8A%B6%E6%80%81) |
| m\_strOrderSysID | str | 合同编号，委托号 |
| m\_nOrderStatus | int | [EEntrustStatus，委托状态](enum_constants.md#enum-eentruststatus-%E5%A7%94%E6%89%98%E7%8A%B6%E6%80%81) |
| m\_nVolumeTraded | int | 成交数量，已成交量 |
| m\_nVolumeTotal | int | 委托剩余量，当前总委托量，股票中表示总委托量减去成交量 |
| m\_nErrorID | int | 状态ID |
| m\_strErrorMsg | str | 状态信息 |
| m\_nTaskId | int | 任务号 |
| m\_dFrozenMargin | float | 冻结金额，冻结保证金 |
| m\_dFrozenCommission | float | 冻结手续费 |
| m\_strInsertDate | str | 委托日期，报单日期 |
| m\_strInsertTime | str | 委托时间 |
| m\_dTradedPrice | float | 成交均价（股票） |
| m\_dCancelAmount | float | 已撤数量 |
| m\_strOptName | str | 买卖标记，展示委托属性的中文 |
| m\_dTradeAmount | float | 成交金额，期货的计算方式为均价乘以数量乘以合约乘数 |
| m\_eEntrustType | int | [EEntrustTypes，委托类别](enum_constants.md#enum-eentrusttypes-%E5%A7%94%E6%89%98%E7%B1%BB%E5%9E%8B) |
| m\_strCancelInfo | str | 废单原因 |
| m\_strUnderCode | str | 标的证券代码 |
| m\_eCoveredFlag | int | 备兑标记，'0’表示非备兑，'1’表示备兑 |
| m\_dOrderPriceRMB | float | 委托价格（人民币），目前用于港股通 |
| m\_dTradeAmountRMB | float | 成交金额（人民币），目前用于港股通 |
| m\_dReferenceRate | float | 汇率，目前用于港股通 |
| m\_strCompactNo | str | 合约编号 |
| m\_eCashgroupProp | int | [EXTCompactBrushSource类型，头寸来源](enum_constants.md#enum-extcompactbrushsource-%E5%A4%B4%E5%AF%B8%E6%9D%A5%E6%BA%90) |
| m\_dShortOccupedMargin | float | 预估在途占用保证金，用于期权 |
| m\_strXTTrade | str | 是否是迅投交易 |
| m\_strAccountKey | str | 账号key，唯一区别不同账号的key |
| m\_strRemark | str | 投资备注 |

### Deal - 成交对象

| 字段 | 数据类型 | 解释 |
| --- | --- | --- |
| m\_strAccountID | str | 资金账号 |
| m\_strExchangeID | str | 证券市场 |
| m\_strExchangeName | str | 交易市场 |
| m\_strProductID | str | 品种代码 |
| m\_strProductName | str | 品种名称 |
| m\_strInstrumentID | str | 证券代码 |
| m\_strInstrumentName | str | 证券名称 |
| m\_strTradeID | str | 成交编号 |
| m\_strOrderRef | str | 下单引用，等于股票的内部委托号 |
| m\_strOrderSysID | str | 合同编号，报单编号，委托号 |
| m\_nDirection | int | [EEntrustBS，买卖方向 对于股票该值始终是48](enum_constants.md#enum-eentrustbs-%E4%B9%B0%E5%8D%96%E6%96%B9%E5%90%91) |
| m\_nOffsetFlag | int | [EOffset\_Flag\_Type，买卖/开平，用此字段区分股票买卖，期货开、平仓，期权买卖等](enum_constants.md#enum-eoffset-flag-type-%E6%93%8D%E4%BD%9C%E7%B1%BB%E5%9E%8B) |
| m\_nHedgeFlag | int | [EHedge\_Flag\_Type 类型，投保](enum_constants.md#enum-ehedge-flag-type) |
| m\_dPrice | float | 成交均价 |
| m\_nVolume | int | 成交量，期货单位手，股票做到股 |
| m\_strTradeDate | str | 成交日期 |
| m\_strTradeTime | str | 成交时间 |
| m\_dCommission | float | 手续费 (旧版本为 `m_dComission`) |
| m\_dTradeAmount | float | 成交额，期货 = 均价 \\* 量 \\* 合约乘数 |
| m\_nTaskId | int | 任务号 |
| m\_nOrderPriceType | int | [EBrokerPriceType 类型，例如市价单、限价单](enum_constants.md#enum-eentrusttypes-%E5%A7%94%E6%89%98%E7%B1%BB%E5%9E%8B) |
| m\_strOptName | str | 买卖标记，展示委托属性的中文 |
| m\_eEntrustType | int | [EEntrustTypes，委托类别](enum_constants.md#enum-eentrusttypes-%E5%A7%94%E6%89%98%E7%B1%BB%E5%9E%8B) |
| m\_eFutureTradeType | int | [EFutureTradeType 类型，成交类型](enum_constants.md#enum-efuturetradetype-%E6%88%90%E4%BA%A4%E7%B1%BB%E5%9E%8B) |
| m\_nRealOffsetFlag | int | [EOffset\_Flag\_Type 类型，实际开平，主要是区分平今和平昨](enum_constants.md#enum-eoffset-flag-type-%E6%93%8D%E4%BD%9C%E7%B1%BB%E5%9E%8B) |
| m\_eCoveredFlag | int | ECoveredFlag类型，备兑标记 '0' - 非备兑，'1' - 备兑 |
| m\_nCloseTodayVolume | int | 平今量，不显示 |
| m\_dOrderPriceRMB | float | 委托价格（人民币），目前用于港股通 |
| m\_dPriceRMB | float | 成交价格（人民币），目前用于港股通 |
| m\_dTradeAmountRMB | float | 成交金额（人民币），目前用于港股通 |
| m\_dReferenceRate | float | 汇率，目前用于港股通 |
| m\_strXTTrade | str | 是否是迅投交易 |
| m\_strCompactNo | str | 合约编号 |
| m\_dCloseProfit | float | 平仓盈亏，目前用于外盘 |
| m\_strRemark | str | 投资备注 |
| m\_strAccountKey | str | 账号key，唯一区别不同账号的key |
| m\_nRef | int | 订单编号 |

### Position - 持仓对象

| 字段名 | 数据类型 | 含义 |
| --- | --- | --- |
| m\_strAccountID | string | 资金账号 |
| m\_strExchangeID | string | 证券市场 |
| m\_strExchangeName | string | 市场名称 |
| m\_strProductID | string | 品种代码 |
| m\_strProductName | string | 品种名称 |
| m\_strInstrumentID | string | 证券代码 |
| m\_strInstrumentName | string | 证券名称 |
| m\_nHedgeFlag | int | [EHedge\_Flag\_Type 类型，投保 ，股票不适用](enum_constants.md#enum-ehedge-flag-type) |
| m\_nDirection | int | [EEntrustBS，买卖方向 对于股票该值始终是48](enum_constants.md#enum-eentrustbs-%E4%B9%B0%E5%8D%96%E6%96%B9%E5%90%91) |
| m\_strOpenDate | string | 开仓日期 股票此字段无效 |
| m\_strTradeID | string | 成交号，最初开仓位的成交 |
| m\_nVolume | int | 当前拥股/持仓量 |
| m\_dOpenPrice | float | 持仓成本 ；持仓成本 = (总买入金额 \- 总卖出金额) / 剩余数量 |
| m\_strTradingDay | string | 在实盘运行中是当前交易日，在回测中是股票最后交易过的日期 |
| m\_dMargin | float | 使用的保证金，历史的直接用ctp的，新的自己用成本价 _存量_ 系数算，股票不适用 |
| m\_dOpenCost | float | 开仓成本，等于成本价\*第一次建仓的量，后续减持会影响，不算手续费，股票不适用 |
| m\_dSettlementPrice | float | 最新结算价/当前价 |
| m\_nCloseVolume | int | 平仓量（对于股票不适用） |
| m\_dCloseAmount | float | 平仓额（对于股票不适用） |
| m\_dFloatProfit | float | 浮动盈亏 |
| m\_dCloseProfit | float | 平仓盈亏（对于股票不适用） |
| m\_dMarketValue | float | 市值/合约价值 |
| m\_dPositionCost | float | 持仓成本（对于股票不适用） |
| m\_dPositionProfit | float | 持仓盈亏（对于股票不适用） |
| m\_dLastSettlementPrice | float | 最新结算价（对于股票不适用） |
| m\_dInstrumentValue | float | 合约价值（对于股票不适用） |
| m\_bIsToday | bool | 是否今仓 |
| m\_strStockHolder | string | 股东账号 |
| m\_nFrozenVolume | int | 冻结数量 |
| m\_nCanUseVolume | int | 可用余额 |
| m\_nOnRoadVolume | int | 在途股份 |
| m\_nYesterdayVolume | int | 昨夜拥股 |
| m\_dLastPrice | float | 最新价/当前价 |
| m\_dAvgOpenPrice | float | 开仓均价（对于股票不适用） |
| m\_dProfitRate | float | 盈亏比例 |
| m\_eFutureTradeType | int | [EFutureTradeType 类型，成交类型](enum_constants.md#enum-efuturetradetype-%E6%88%90%E4%BA%A4%E7%B1%BB%E5%9E%8B) |
| m\_strExpireDate | string | 到期日（针对逆回购） |
| m\_strComTradeID | string | 组合成交号 |
| m\_nLegId | int | 组合序号 |
| m\_dTotalCost | float | 累计成本（自定义，股票信用用到） |
| m\_dSingleCost | float | 单股成本（自定义，股票信用用 |
| m\_nCoveredVolume | int | 备兑数量，用于个股期权 |
| m\_eSideFlag | int | 持仓类型 ，用于个股期权，标记 '0' - 权利，'1' - 义务，'2' - '备兑' |
| m\_dReferenceRate | float | 汇率，目前用于港股通 |
| m\_dStructFundVol | float | 分级基金可用（可分拆或可合并） |
| m\_dRedemptionVolume | float | 分级基金可赎回量 |
| m\_nPREnableVolume | int | 申赎可用量（记录当日申购赎回的股票或基金数量） |
| m\_dRealUsedMargin | float | 实时占用保证金，用于期权 |
| m\_dRoyalty | float | 权利金 |
| m\_dStockLastPrice | float | 标的证券最新价，用于期权 |
| m\_dStaticHoldMargin | float | 静态持仓占用保证金，用于期权 |
| m\_nOptCombUsedVolume | int | 期权组合占用数量 |
| m\_nEnableExerciseVolume | int | 能够行使的数量，用于个股期权 |
| m\_strAccountKey | string | 账号key，唯一区别不同账号的key |

### PositionStatistics - 持仓统计对象

| 字段名 | 数据类型 | 描述 |
| --- | --- | --- |
| `m_strAccountID` | `string` | 账号 |
| `m_strExchangeID` | `string` | 市场代码 |
| `m_strExchangeName` | `string` | 市场名称 |
| `m_strProductID` | `string` | 品种代码 |
| `m_strInstrumentID` | `string` | 合约代码 |
| `m_strInstrumentName` | `string` | 合约名称 |
| `m_nDirection` | `int` | 多空 |
| `m_nHedgeFlag` | `int` | 投保 |
| `m_nPosition` | `int` | 持仓 |
| `m_nYestodayPosition` | `int` | 昨仓 |
| `m_nTodayPosition` | `int` | 今仓 |
| `m_nCanCloseVol` | `int` | 可平 |
| `m_dPositionCost` | `float` | 持仓成本 |
| `m_dAvgPrice` | `float` | 持仓均价 |
| `m_dPositionProfit` | `float` | 持仓盈亏 |
| `m_dFloatProfit` | `float` | 浮动盈亏 |
| `m_dOpenPrice` | `float` | 开仓均价 |
| `m_dUsedMargin` | `float` | 已使用保证金 |
| `m_dUsedCommission` | `float` | 已使用的手续费 |
| `m_dFrozenMargin` | `float` | 冻结保证金 |
| `m_dFrozenCommission` | `float` | 冻结手续费 |
| `m_dInstrumentValue` | `float` | 市值，合约价值 |
| `m_nOpenTimes` | `int` | 开仓次数 |
| `m_nOpenVolume` | `int` | 总开仓量 中间平仓不减 |
| `m_nCancelTimes` | `int` | 撤单次数 |
| `m_dLastPrice` | `float` | 最新价 |
| `m_dRiseRatio` | `float` | 当日涨幅 |
| `m_strProductName` | `string` | 产品名称 |
| `m_dRoyalty` | `float` | 权利金市值 |
| `m_strExpireDate` | `string` | 到期日 |
| `m_dAssestWeight` | `float` | 资产占比 |
| `m_dIncreaseBySettlement` | `float` | 当日涨幅（结） |
| `m_dMarginRatio` | `float` | 保证金占比 |
| `m_dFloatProfitDivideByUsedMargin` | `float` | 浮盈比例（保证金） |
| `m_dFloatProfitDivideByBalance` | `float` | 浮盈比例（动态权益） |
| `m_dTodayProfitLoss` | `float` | 当日盈亏（结） |
| `m_nYestodayInitPosition` | `int` | 昨日持仓 |
| `m_dFrozenRoyalty` | `float` | 冻结权利金 |
| `m_dTodayCloseProfitLoss` | `float` | 当日盈亏（收） |
| `m_dCloseProfit` | `float` | 平仓盈亏 |
| `m_strFtProductName` | `string` | 品种名称 |
| `m_dOpenCost` | `float` | 开仓成本 |

### CCreditAccountDetail - 信用账号对象(非查柜台)

| 字段名 | 数据类型 | 解释 |
| --- | --- | --- |
| m\_strAccountID | str | 资金账号 |
| m\_nBrokerType | int | 账号类型，1-期货账号，2-股票账号，3-信用账号，5-期货期权账号，6-股票期权账号，7-沪港通账号，11-深港通账号 |
| m\_strAccountKey | str | 唯一区别不同账号的key |
| m\_dMaxMarginRate | float | 保证金比率，股票的保证金率等于1 |
| m\_dFrozenMargin | float | 冻结保证金，外源性，股票的保证金就是冻结资金，股票不适用 |
| m\_dFrozenCash | float | 冻结金额，内外源冻结保证金和手续费四个的和 |
| m\_dFrozenCommission | float | 冻结手续费，外源性冻结资金源 |
| m\_dRisk | float | 风险度，冻结资金/可用资金 |
| m\_dNav | float | 单位净值 |
| m\_dPreBalance | float | 期初权益，也叫静态权益，股票不适用 |
| m\_dBalance | float | 总资产，动态权益，即市值 |
| m\_dAvailable | float | 可用金额 |
| m\_dCommission | float | 手续费(旧版本为 m\_dComission) |
| m\_dPositionProfit | float | 持仓盈亏 |
| m\_dCloseProfit | float | 平仓盈亏，股票不适用 |
| m\_dCashIn | float | 出入金净值 |
| m\_dCurrMargin | float | 当前使用的保证金，股票不适用 |
| m\_dInitBalance | float | 初始权益 |
| m\_strStatus | str | 状态 |
| m\_dInitCloseMoney | float | 期初平仓盈亏，初始平仓盈亏 |
| m\_dInstrumentValue | float | 总市值，合约价值，合约价值 |
| m\_dDeposit | float | 入金 |
| m\_dWithdraw | float | 出金 |
| m\_dPreCredit | float | 上次信用额度，股票不适用 |
| m\_dPreMortgage | float | 上次质押，股票不适用 |
| m\_dMortgage | float | 质押，股票不适用 |
| m\_dCredit | float | 信用额度，股票不适用 |
| m\_dAssetBalance | float | 证券初始资金，股票不适用 |
| m\_strOpenDate | str | 起始日期股票不适用 |
| m\_dFetchBalance | float | 可取金额 |
| m\_strTradingDate | str | 交易日 |
| m\_dStockValue | float | 股票总市值，期货没有 |
| m\_dLoanValue | float | 债券总市值，期货没有 |
| m\_dFundValue | float | 基金总市值，包括 ETF 和封闭式基金，期货没有 |
| m\_dRepurchaseValue | float | 回购总市值，所有回购，期货没有 |
| m\_dLongValue | float | 多单总市值，现货没有 |
| m\_dShortValue | float | 单总市值，现货没有 |
| m\_dNetValue | float | 净持仓总市值，净持仓市值 = 多 \- 空 |
| m\_dAssureAsset | float | 净资产 |
| m\_dEntrustAsset | float | 可信资产，用于校对 |
| m\_dInstrumentValueRMB | float | 总市值（人民币），沪港通 |
| m\_dSubscribeFee | float | 申购费，申购费 |
| m\_dGoldValue | float | 库存市值，黄金现货库存市值 |
| m\_dGoldFrozen | float | 现货冻结，黄金现货冻结 |
| m\_dMargin | float | 占用保证金，维持保证金 |
| m\_strMoneyType | str | 币种 |
| m\_dPurchasingPower | float | 购买力，盈透购买力 |
| m\_dRawMargin | float | 原始保证金 |
| m\_dBuyWaitMoney | float | 买入待交收金额（元），买入待交收 |
| m\_dSellWaitMoney | float | 卖出待交收金额（元），卖出待交收 |
| m\_dReceiveInterestTotal | float | 本期间应计利息 |
| m\_dRoyalty | float | 权利金收支，期货期权用 |
| m\_dFrozenRoyalty | float | 冻结权利金，期货期权用 |
| m\_dRealUsedMargin | float | 实时占用保证金，用于股票期权 |
| m\_dRealRiskDegree | float | 实时风险度 |
| m\_dPerAssurescaleValue | float | 个人维持担保比例 |
| m\_dEnableBailBalance | float | 可用保证金 |
| m\_dUsedBailBalance | float | 已用保证金 |
| m\_dAssureEnbuyBalance | float | 可买担保品资金 |
| m\_dFinEnbuyBalance | float | 可买标的券资金 |
| m\_dSloEnrepaidBalance | float | 可还券资金 |
| m\_dFinEnrepaidBalance | float | 可还款资金 |
| m\_dFinMaxQuota | float | 融资授信额度 |
| m\_dFinEnableQuota | float | 融资可用额度 |
| m\_dFinUsedQuota | float | 融资已用额度 |
| m\_dFinUsedBail | float | 融资已用保证金额 |
| m\_dFinCompactBalance | float | 融资合约金额 |
| m\_dFinCompactFare | float | 融资合约费用 |
| m\_dFinCompactInterest | float | 融资合约利息 |
| m\_dFinMarketValue | float | 融资市值 |
| m\_dFinIncome | float | 融资合约盈亏 |
| m\_dSloMaxQuota | float | 融券授信额度 |
| m\_dSloEnableQuota | float | 融券可用额度 |
| m\_dSloUsedQuota | float | 融券已用额度 |
| m\_dSloUsedBail | float | 融券已用保证金额 |
| m\_dSloCompactBalance | float | 融券合约金额 |
| m\_dSloCompactFare | float | 融券合约费用 |
| m\_dSloCompactInterest | float | 融券合约利息 |
| m\_dSloMarketValue | float | 融券市值 |
| m\_dSloIncome | float | 融券合约盈亏 |
| m\_dOtherFare | float | 其它费用 |
| m\_dUnderlyMarketValue | float | 标的证券市值 |
| m\_dFinEnableBalance | float | 可融资金额 |
| m\_dDiffEnableBailBalance | float | 可用保证金调整值 |
| m\_dBuySecuRepayFrozenMargin | float | 买券还券冻结资金 |
| m\_dBuySecuRepayFrozenCommission | float | 买券还券冻结手续费 |
| m\_dSpecialEnableBalance | float | 专项可融金额 |
| m\_dEncumberedAssets | float | 担保资产 |
| m\_dSloSellBalance | float | 融券卖出资金 |
| m\_dDiffAssureEnbuyBalance | float | 可买担保品资金调整值 |
| m\_dDiffFinEnbuyBalance | float | 可买标的券资金调整值 |
| m\_dDiffFinEnrepaidBalance | float | 可还款资金调整值 |
| m\_dOtherRealCompactBalance | float | 其他负债合约金额 |
| m\_dOtherFinCompactInterest | float | 其他负债合约利息金额 |
| m\_dUsedSloSellBalance | float | 已用融券卖出资金 |
| m\_dFetchAssetBalance | float | 可提出资产总额 |
| m\_dTotalEnableQuota | float | 可用总信用额度 |
| m\_dTotalUsedQuota | float | 已用总信用额度 |
| m\_dDebtProfit | float | 负债总浮盈 |
| m\_dDebtLoss | float | 负债总浮亏 |
| m\_nContractEndDate | int | 合同到期日期 |
| m\_dFinDebt | float | 融资负债 |
| m\_dFinProfitAmortized | float | 融资浮盈折算 |
| m\_dSloProfit | float | 融券浮盈 |
| m\_dSloProfitAmortized | float | 融券浮盈折算 |
| m\_dFinLoss | float | 融资浮亏 |
| m\_dSloLoss | float | 融券浮亏 |

### CCreditDetail - 两融资金信息(查柜台)

| 字段名 | 数据类型 | 解释 |
| --- | --- | --- |
| m\_dPerAssurescaleValue | float | 维持担保比例 |
| m\_dBalance | float | 总资产 |
| m\_dTotalDebt | float | 总负债 |
| m\_dAssureAsset | float | 净资产 |
| m\_dMarketValue | float | 总市值 |
| m\_dEnableBailBalance | float | 可用保证金 |
| m\_dAvailable | float | 可用资金 |
| m\_dFinDebt | float | 融资负债 |
| m\_dFinDealAvl | float | 融资本金 |
| m\_dFinFee | float | 融资息费 |
| m\_dSloDebt | float | 融券负债 |
| m\_dSloMarketValue | float | 融券市值 |
| m\_dSloFee | float | 融券息费 |
| m\_dOtherFare | float | 其它费用 |
| m\_dFinMaxQuota | float | 融资授信额度 |
| m\_dFinEnableQuota | float | 融资可用额度 |
| m\_dFinUsedQuota | float | 融资冻结额度 |
| m\_dSloMaxQuota | float | 融券授信额度 |
| m\_dSloEnableQuota | float | 融券可用额度 |
| m\_dSloUsedQuota | float | 融券冻结额度 |
| m\_dSloSellBalance | float | 融券卖出资金 |
| m\_dUsedSloSellBalance | float | 已用融券卖出资金 |
| m\_dSurplusSloSellBalance | float | 剩余融券卖出资金 |
| m\_dStockValue | float | 股票市值 |
| m\_dFundValue | float | 基金市值 |
| error | string | 错误信息 |

### CreditSloEnableAmount - 可融券明细对象

提示

由于字段m\_dSloRatio、m\_dSloStatus提供来源和取担保品明细 **get\_assure\_contract** 重复，字段在2021年9月移除，后续用担保品明细接口获取,具体见 [担保标的对象字段说明](data_structure.md?id=null#stksubjects-%E6%8B%85%E4%BF%9D%E6%A0%87%E7%9A%84%E5%AF%B9%E8%B1%A1)

| 字段名 | 数据类型 | 解释 |
| --- | --- | --- |
| m\_nPlatformID | int | 平台号 |
| m\_strBrokerID | string | 经纪公司编号 |
| m\_strBrokerName | string | 经纪公司 |
| m\_strAccountID | string | 资金账号 |
| m\_strExchangeID | string | 交易所 |
| m\_strInstrumentID | string | 证券代码 |
| m\_nEnableAmount | int | 融券可融数量 |
| m\_eQuerySloType | enum | [EXTSloTypeQueryMode](enum_constants.md#enum-extslotypequerymode-%E6%9F%A5%E8%AF%A2%E7%B1%BB%E5%9E%8B)，查询类型 |

### StkCompacts - 负债合约对象

| 字段名 | 数据类型 | 解释 |
| --- | --- | --- |
| m\_strAccountID | string | 资金账号，账号，账号，资金账号 |
| m\_strExchangeID | string | 交易所 |
| m\_strInstrumentID | string | 证券代码 |
| m\_strExchangeName | string | 交易所名称 |
| m\_strInstrumentName | string | 股票名称 |
| m\_nOpenDate | int | 合约开仓日期 |
| m\_strCompactId | string | 合约编号 |
| m\_dCrdtRatio | float | 融资融券保证金比例 |
| m\_strEntrustNo | string | 委托编号 |
| m\_dEntrustPrice | float | 委托价格 |
| m\_nEntrustVol | int | 委托数量 |
| m\_nBusinessVol | int | 合约开仓数量 |
| m\_dBusinessBalance | float | 合约开仓金额 |
| m\_dBusinessFare | float | 合约开仓费用 |
| m\_eCompactType | enum | [EXTCompactType](enum_constants.md#enum-extcompacttype-%E5%90%88%E7%BA%A6%E7%B1%BB%E5%9E%8B)，合约类型 |
| m\_eCompactStatus | enum | [EXTCompactStatus](enum_constants.md#enum-extcompactstatus-%E5%90%88%E7%BA%A6%E7%8A%B6%E6%80%81)，合约状态 |
| m\_dRealCompactBalance | float | 未还合约金额 |
| m\_nRealCompactVol | int | 未还合约数量 |
| m\_dRealCompactFare | float | 未还合约费用 |
| m\_dRealCompactInterest | float | 未还合约利息 |
| m\_dRepaidInterest | float | 已还利息 |
| m\_nRepaidVol | int | 已还数量 |
| m\_dRepaidBalance | float | 已还金额 |
| m\_dCompactInterest | float | 合约总利息 |
| m\_dUsedBailBalance | float | 占用保证金 |
| m\_dYearRate | float | 合约年利率 |
| m\_nRetEndDate | int | 归还截止日 |
| m\_strDateClear | string | 了结日期 |
| m\_strPositionStr | string | 定位串 |
| m\_dPrice | float | 最新价 |
| m\_nOpenTime | int | 合约开仓时间 |
| m\_nCancelVol | int | 合约撤单数量 |
| m\_eCashgroupProp | enum | [EXTCompactBrushSource](enum_constants.md#enum-extcompactbrushsource-%E5%A4%B4%E5%AF%B8%E6%9D%A5%E6%BA%90)，头寸来源 |
| m\_dUnRepayBalance | float | 负债金额 |
| m\_nRepayPriority | int | 偿还优先级 |
| m\_dRealDefaultInterest | float | 未还罚息 |
| m\_dOtherRealCompactBalance | float | 其他负债合约金额 |
| m\_dOtherRealCompactInterest | float | 其他负债合约利息金额 |

### StkSubjects - 担保标的对象

| 字段名 | 数据类型 | 解释 |
| --- | --- | --- |
| m\_nPlatformID | int | 平台号//目前主要用于区别不同的行情，根据此来选择对应行情 |
| m\_strBrokerID | string | 经纪公司编号 |
| m\_strBrokerName | string | 经纪公司名称 |
| m\_strExchangeID | string | 交易所 |
| m\_strInstrumentID | string | 证券代码 |
| m\_dSloRatio | float | 融券保证金比例 |
| m\_eSloStatus | enum | [EXTSubjectsStatus](enum_constants.md#enum-extsubjectsstatus-%E8%9E%8D%E8%B5%84%E8%9E%8D%E5%88%B8%E7%8A%B6%E6%80%81)，融券状态 |
| m\_dFinRatio | float | 融资保证金比例 |
| m\_eFinStatus | enum | [EXTSubjectsStatus](enum_constants.md#enum-extsubjectsstatus-%E8%9E%8D%E8%B5%84%E8%9E%8D%E5%88%B8%E7%8A%B6%E6%80%81)，融资状态 |
| m\_strAccountID | string | 资金账号 |
| m\_eCreditFundCtl | enum | [EXTCreditFundCtl](enum_constants.md#enum-extcreditfundctl-%E8%9E%8D%E8%B5%84%E4%BA%A4%E6%98%93%E6%8E%A7%E5%88%B6)，融资交易控制 |
| m\_eCreditStkCtl | enum | [EXTCreditStkCtl](enum_constants.md#enum-extcreditstkctl-%E8%9E%8D%E5%88%B8%E4%BA%A4%E6%98%93%E6%8E%A7%E5%88%B6)，融券交易控制 |
| m\_eAssureStatus | enum | [EXTSubjectsStatus](enum_constants.md#enum-extsubjectsstatus-%E8%9E%8D%E8%B5%84%E8%9E%8D%E5%88%B8%E7%8A%B6%E6%80%81)，是否可做担保 |
| m\_dAssureRatio | float | 担保品折算比例 |

### PassorderArguments - 下单函数参数对象

| 字段名 | 数据类型 | 解释 |
| --- | --- | --- |
| opType | int | passorder的opType参数 |
| orderType | int | passorder的orderType参数 |
| accountID | string | 资金账号 |
| orderCode | string | 交易代码 |
| prType | int | passorder的prType，价格类型 |
| modelPrice | float | 下单价格 |
| modelVolume | int | 下单量（手数或股数） |
| strategyName | string | 策略名 \_ &&& \_ 投资备注 |

### CTaskDetail - 任务对象

| 字段名 | 数据类型 | 解释 |
| --- | --- | --- |
| m\_nTaskId | int | 任务号 |
| m\_eStatus | enum | 任务状态 [ETaskStatus类型,见ETaskStatus说明](enum_constants.md#enum-etaskstatus-%E4%BB%BB%E5%8A%A1%E7%8A%B6%E6%80%81) |
| m\_strMsg | string | 任务状态消息 |
| m\_startTime | int | 任务开始时间, 时间戳类型 |
| m\_endTime | int | 任务结束时间, 时间戳类型 |
| m\_cancelTime | int | 任务取消时间 |
| m\_nBusinessNum | int | 已成交量 |
| m\_nGroupId | int | 组合Id |
| m\_stockCode | string | 下单代码(不针对组合下单) |
| m\_strAccountID | string | 下单用户(单用户下单) |
| m\_eOperationType | enum | 下单操作： [开平、多空……EOperationType类型, 见EOperationType说明](enum_constants.md#enum-eoperationtype-%E4%B8%8B%E5%8D%95%E6%93%8D%E4%BD%9C%E7%B1%BB%E5%9E%8B-%E4%B8%BB%E8%A6%81%E4%BA%A4%E6%98%93%E7%B1%BB%E5%9E%8B) |
| m\_eOrderType | enum | 算法交易、普通交易 [EOrderType类型, 见EOrderType说明](enum_constants.md#enum-eordertype-%E7%AE%97%E6%B3%95%E4%BA%A4%E6%98%93%E3%80%81%E6%99%AE%E9%80%9A%E4%BA%A4%E6%98%93%E7%B1%BB%E5%9E%8B) |
| m\_ePriceType | enum | 报价方式：对手、最新…… [EPriceType类型见EPriceType说明](enum_constants.md#enum-epricetype-%E4%BB%B7%E6%A0%BC%E7%B1%BB%E5%9E%8B) |
| m\_dFixPrice | float | 委托价 |
| m\_nNum | int | 委托量 |
| m\_strRemark | string | 投资备注 |

### CLockPosition - 期权标的持仓

| 字段名 | 数据类型 | 解释 |
| --- | --- | --- |
| m\_strAccountID | string | 账号名 |
| m\_strExchangeID | string | 交易所 |
| m\_strExchangeName | string | 交易所名 |
| m\_strInstrumentID | string | 标的代码 |
| m\_strInstrumentName | string | 标的名称 |
| m\_totalVol | int | 总持仓量 |
| m\_lockVol | int | 可用锁定量 |
| m\_unlockVol | int | 未锁定量 |
| m\_coveredVol | int | 备兑量 |
| m\_nOnRoadcoveredVol | int | 在途备兑量 |

### CStkOptCombPositionDetail - 期权组合持仓

| 字段名 | 数据类型 | 解释 |
| --- | --- | --- |
| m\_strAccountID | string | 账号名 |
| m\_strExchangeID | string | 交易所 |
| m\_strExchangeName | string | 交易所名 |
| m\_strContractAccount | string | 合约账号 |
| m\_strCombID | string | 组合编号 |
| m\_strCombCode | string | 组合策略编码 |
| m\_strCombCodeName | string | 组合策略名称 |
| m\_nVolume | int | 持仓量 |
| m\_nFrozenVolume | int | 冻结数量 |
| m\_nCanUseVolume | int | 可用数量 |
| m\_strFirstCode | string | 合约一 |
| m\_eFirstCodeType | enum | 合约一类型 认购:48,认沽:49 |
| m\_strFirstCodeName | string | 合约一名称 |
| m\_eFirstCodePosType | enum | 合约一持仓类型 认购:48,义务:49,备兑:50 |
| m\_nFirstCodeAmt | int | 合约一数量 |
| m\_strSecondCode | string | 合约二 |
| m\_eSecondCodeType | enum | 合约二类型 认购:48,认沽:49 |
| m\_strSecondCodeName | string | 合约二名称 |
| m\_eSecondCodePosType | enum | 合约二持仓类型 权利:48,义务:49,备兑:50 |
| m\_nSecondCodeAmt | int | 合约二数量 |
| m\_dCombBailBalance | float | 占用保证金 |

### entrustType - 委托类型

- 0 - 未知
- 1 - 正常交易业务
- 2 - 即时成交剩余撤销
- 3 - ETF基金申报
- 4 - 最优五档即时成交剩余撤销
- 5 - 全额成交或撤销
- 6 - 本方最优价格
- 7 - 对手方最优价格

### openInt - 证券状态

| 编码 | 状态 |
| --- | --- |
| 0,10 | 默认为未知 |
| 1 | 停牌 |
| 11 | 开盘前S |
| 12 | 集合竞价时段C |
| 13 | 连续交易T |
| 14 | 休市B |
| 15 | 闭市E |
| 16 | 波动性中断V,例如(10006742.SHO)50ETF沽9月2300在2024/08/28 10:15:34 - 2024/08/28 10:18:34 触发熔断临时停牌，此时的openInt值为16 |
| 17 | 临时停牌P |
| 18 | 收盘集合竞价U |
| 19 | 盘中集合竞价M |
| 20 | 暂停交易至闭市N |
| 21 | 获取字段异常 |
| 22 | 盘后固定价格行情 |
| 23 | 盘后固定价格行情完毕 |