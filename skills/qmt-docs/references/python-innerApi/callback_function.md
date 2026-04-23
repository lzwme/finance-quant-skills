---
url: "https://dict.thinktrader.net/innerApi/callback_function.html"
title: "成交回报实时主推函数 | 迅投知识库"
---

## 实时主推函数

### account\_callback - 资金账号状态变化主推

提示

1. 仅在实盘运行模式下生效。
2. 需要先在init里调用ContextInfo.set\_account后生效。

**用法：** account\_callback(ContextInfo, accountInfo)

**释义：** 当资金账号状态有变化时，这个函数被客户端调用

**参数：**

- ContextInfo：特定对象
- accountInfo： [账号对象](data_structure.html#account-%E8%B4%A6%E6%88%B7%E5%AF%B9%E8%B1%A1) 或 [信用账号对象](data_structure.md)

**返回：** 无

**示例：**

示例返回值

 ```py
#coding:gbk
def show_data(data):
    tdata = {}
    for ar in dir(data):
        if ar[:2] != 'm_':continue
        try:
            tdata[ar] = data.__getattribute__(ar)
        except:
            tdata[ar] = '<CanNotConvert>'
    return tdata

def init(ContextInfo):
    # 设置对应的资金账号
    # 示例需要在策略交易界面运行
    ContextInfo.set_account(account)

def after_init(ContextInfo):
    # 在策略交易界面运行时，account的值会被赋值为策略配置中的账号，编辑器界面运行时，需要手动赋值
    # 编译器界面里执行的下单函数不会产生实际委托
    passorder(23, 1101, account, "000001.SZ", 5, 0, 100, "示例", 2, "投资备注",ContextInfo)
    pass

def account_callback(ContextInfo, accountInfo):
    print(show_data(accountInfo))
```

```
{'m_Enable': True, 'm_dAssetBalance': 9975010.001775814, 'm_dAssureAsset': 9975010.001775814, 'm_dAvailable': 9556221.001775814, 'm_dBalance': 9975010.001775814, 'm_dBuyWaitMoney': 0.0, 'm_dCashIn': 0.0, 'm_dCloseProfit': 0.0, 'm_dCommission': 14.284000000000006, 'm_dCredit': 0.0, 'm_dCurrMargin': 0.0, 'm_dDeposit': 0.0, 'm_dEntrustAsset': 0.0, 'm_dFetchBalance': 9556221.001775814, 'm_dFrozenCash': 0.0, 'm_dFrozenCommission': 0.0, 'm_dFrozenMargin': 9556221.001775814, 'm_dFrozenRoyalty': 0.0, 'm_dFundValue': 0.0, 'm_dGoldFrozen': 0.0, 'm_dGoldValue': 0.0, 'm_dInitBalance': 0.0, 'm_dInitCloseMoney': -4249.283999999998, 'm_dInstrumentValue': 418789.0, 'm_dInstrumentValueRMB': 0.0, 'm_dIntradayBalance': 0.0, 'm_dIntradayFreedBalance': 0.0, 'm_dLoanValue': 0.0, 'm_dLongValue': 0.0, 'm_dMargin': 0.0, 'm_dMaxMarginRate': 0.0, 'm_dMortgage': 0.0, 'm_dNav': 0.0, 'm_dNetValue': 0.0, 'm_dOccupiedBalance': 0.0, 'm_dPositionProfit': -3441.6657800000025, 'm_dPreBalance': 9556221.001775814, 'm_dPreCredit': 0.0, 'm_dPreMortgage': 0.0, 'm_dPurchasingPower': 0.0, 'm_dRawMargin': 0.0, 'm_dRealRiskDegree': 0.0, 'm_dRealUsedMargin': 0.0, 'm_dReceiveInterestTotal': 0.0, 'm_dRepurchaseValue': 0.0, 'm_dRisk': 0.0, 'm_dRoyalty': 0.0, 'm_dSellWaitMoney': 0.0, 'm_dShortValue': 0.0, 'm_dStockValue': 418789.0, 'm_dSubscribeFee': 0.0, 'm_dTotalDebit': 0.0, 'm_dWithdraw': 0.0, 'm_nBrokerType': 2, 'm_nDirection': 48, 'm_strAccountID': '2000567', 'm_strAccountKey': '2____11194____114911____49____2000567____', 'm_strAccountRemark': '', 'm_strBrokerName': '', 'm_strMoneyType': '', 'm_strOpenDate': '', 'm_strStatus': '准备登录', 'm_strTradingDate': '20240220'}
```

### task\_callback - 账号任务状态变化主推

提示

1. 仅在实盘运行模式下生效。
2. 需要先在init里调用ContextInfo.set\_account后生效。

**用法：** task\_callback(ContextInfo, taskInfo)

**释义：** 当账号任务状态有变化时，这个函数被客户端调用

**参数：**

- ContextInfo：特定对象
- taskInfo [任务对象](data_structure.md)

**返回：** 无

**示例：**

示例返回值

 ```py
#coding:gbk
def show_data(data):
    tdata = {}
    for ar in dir(data):
        if ar[:2] != 'm_':continue
        try:
            tdata[ar] = data.__getattribute__(ar)
        except:
            tdata[ar] = '<CanNotConvert>'
    return tdata

def init(ContextInfo):
    # 设置对应的资金账号
    # 示例需要在策略交易界面运行
    ContextInfo.set_account(account)

def after_init(ContextInfo):
    # 在策略交易界面运行时，account的值会被赋值为策略配置中的账号，编辑器界面运行时，需要手动赋值
    # 编译器界面里执行的下单函数不会产生实际委托
    passorder(23, 1101, account, "000001.SZ", 5, 0, 100, "示例", 2, "投资备注",ContextInfo)
    pass

def task_callback(ContextInfo, taskInfo):
    print(show_data(taskInfo))
```

```
{'m_3rdPartyTradeParam': '', 'm_cancelTime': 2147483647, 'm_dFixPrice': 9.82, 'm_eOperationType': 18, 'm_eOrderType': 0, 'm_ePriceType': 5, 'm_eStatus': 7, 'm_endTime': 1708420476, 'm_nBusinessNum': 100, 'm_nGroupId': 11, 'm_nNum': 100, 'm_nTaskId': '11', 'm_script': '', 'm_startTime': 1708420476, 'm_stockCode': '000001.SZ', 'm_strAccountID': '2000567', 'm_strMsg': '任务完成', 'm_strRemark': '投资备注'}
```

### order\_callback - 账号委托状态变化主推

提示

1. 仅在实盘运行模式下生效。
2. 需要先在init里调用ContextInfo.set\_account后生效。

**用法：** order\_callback(ContextInfo, orderInfo)

**释义：** 当账号委托状态有变化时，这个函数被客户端调用

**参数：**

- ContextInfo：特定对象
- orderInfo： [委托](data_structure.md)

**返回：** 无

**示例：**

示例返回值

 ```py
#coding:gbk
def show_data(data):
    tdata = {}
    for ar in dir(data):
        if ar[:2] != 'm_':continue
        try:
            tdata[ar] = data.__getattribute__(ar)
        except:
            tdata[ar] = '<CanNotConvert>'
    return tdata

def init(ContextInfo):
    # 设置对应的资金账号
    # 示例需要在策略交易界面运行
    ContextInfo.set_account(account)

def after_init(ContextInfo):
    # 在策略交易界面运行时，account的值会被赋值为策略配置中的账号，编辑器界面运行时，需要手动赋值
    # 编译器界面里执行的下单函数不会产生实际委托
    passorder(23, 1101, account, "000001.SZ", 5, 0, 100, "示例", 2, "投资备注",ContextInfo)
    pass

def order_callback(ContextInfo, orderInfo):
    print(show_data(orderInfo))
```

```
{'m_bEnable': True, 'm_dCancelAmount': 0.0, 'm_dFrozenCommission': 0.21600000000000003, 'm_dFrozenMargin': 1080.0, 'm_dLimitPrice': 10.8, 'm_dOrderPriceRMB': 0.0, 'm_dReferenceRate': 0.0, 'm_dShortOccupedMargin': 1.7976931348623157e+308, 'm_dTradeAmount': 0.0, 'm_dTradeAmountRMB': 0.0, 'm_dTradedPrice': 0.0, 'm_eCashgroupProp': 48, 'm_eCoveredFlag': 0, 'm_eEntrustType': 48, 'm_nDirection': 48, 'm_nErrorID': 2147483647, 'm_nFrontID': -1, 'm_nGroupId': 2147483647, 'm_nHedgeFlag': 49, 'm_nOffsetFlag': 48, 'm_nOpType': 23, 'm_nOrderPriceType': 50, 'm_nOrderStatus': 50, 'm_nOrderStrategyType': -946575058, 'm_nOrderSubmitStatus': 51, 'm_nRef': 1745879041, 'm_nSessionID': -1, 'm_nStrategyID': 0, 'm_nTaskId': 1, 'm_nVolumeTotal': 100, 'm_nVolumeTotalOriginal': 100, 'm_nVolumeTraded': 0, 'm_strAccountID': '2000567', 'm_strAccountKey': '2____11194____114911____49____2000567____', 'm_strAccountName': '', 'm_strAccountRemark': '', 'm_strBrokerName': '', 'm_strCancelInfo': '', 'm_strCompactNo': '', 'm_strErrorMsg': '', 'm_strExchangeID': 'SZ', 'm_strExchangeName': '深交所', 'm_strInsertDate': '20240222', 'm_strInsertTime': '091259', 'm_strInstrumentID': '000001', 'm_strInstrumentName': '平安银行', 'm_strLocalInfo': '', 'm_strOptName': '限价买入', 'm_strOption': '', 'm_strOrderParam': '', 'm_strOrderRef': '8875341038780543374', 'm_strOrderStrategyType': '函数下单', 'm_strOrderSysID': '87', 'm_strProductID': '', 'm_strProductName': '', 'm_strRemark': '投资备注', 'm_strSource': '新建策略文件15', 'm_strUnderCode': '', 'm_strXTTrade': '本终端', 'm_xtTag': '<CanNotConvert>'}
```

### deal\_callback - 账号成交状态变化主推

提示

1. 仅在实盘运行模式下生效。
2. 需要先在init里调用ContextInfo.set\_account后生效。

**用法：** deal\_callback(ContextInfo, dealInfo)

**释义：** 当账号成交状态有变化时，这个函数被客户端调用

**参数：**

- ContextInfo：特定对象
- dealInfo： [成交](data_structure.md)

**返回：** 无

**示例：**

示例返回值

 ```py
#coding:gbk
def show_data(data):
    tdata = {}
    for ar in dir(data):
        if ar[:2] != 'm_':continue
        try:
            tdata[ar] = data.__getattribute__(ar)
        except:
            tdata[ar] = '<CanNotConvert>'
    return tdata

def init(ContextInfo):
    # 设置对应的资金账号
    # 示例需要在策略交易界面运行
    ContextInfo.set_account(account)

def after_init(ContextInfo):
    # 在策略交易界面运行时，account的值会被赋值为策略配置中的账号，编辑器界面运行时，需要手动赋值
    # 编译器界面里执行的下单函数不会产生实际委托
    passorder(23, 1101, account, "000001.SZ", 5, 0, 100, "示例", 2, "投资备注",ContextInfo)
    pass

def deal_callback(ContextInfo, dealInfo):
    print(show_data(dealInfo))
```

```
{'m_dCloseProfit': 0.0, 'm_dComssion': 0.19640000000000002, 'm_dOrderPriceRMB': 0.0, 'm_dPrice': 9.82, 'm_dPriceRMB': 0.0, 'm_dReferenceRate': 0.0, 'm_dTradeAmount': 982.0, 'm_dTradeAmountRMB': 0.0, 'm_eCoveredFlag': 48, 'm_eEntrustType': 48, 'm_eFutureTradeType': 48, 'm_nCloseTodayVolume': 0, 'm_nDirection': 48, 'm_nGroupId': 2147483647, 'm_nHedgeFlag': 49, 'm_nOffsetFlag': 48, 'm_nOrderPriceType': 50, 'm_nOrderStrategyType': 0, 'm_nRealOffsetFlag': -1, 'm_nRef': 1209008141, 'm_nStrategyID': 0, 'm_nTaskId': 14, 'm_nVolume': 100, 'm_strAccountID': '2000567', 'm_strAccountKey': '2____11194____114911____49____2000567____', 'm_strAccountRemark': '', 'm_strCompactNo': '', 'm_strExchangeID': 'SZ', 'm_strExchangeName': '深交所', 'm_strInstrumentID': '000001', 'm_strInstrumentName': '平安银行', 'm_strLocalInfo': '', 'm_strOperation': '', 'm_strOptName': '限价买入', 'm_strOrderRef': '8875341038780443523', 'm_strOrderStrategyType': '函数下单', 'm_strOrderSysID': '24500', 'm_strProductID': '', 'm_strProductName': '', 'm_strRemark': '投资备注', 'm_strSource': '新建策略文件15', 'm_strTradeDate': '20240220', 'm_strTradeID': '13', 'm_strTradeTime': '172341', 'm_strXTTrade': '本终端', 'm_xtTag': '<CanNotConvert>'}
```

### position\_callback - 账号持仓状态变化主推

提示

1. 仅在实盘运行模式下生效。
2. 需要先在init里调用ContextInfo.set\_account后生效。

**用法：** position\_callback(ContextInfo, positonInfo)

**释义：** 当账号持仓状态有变化时，这个函数被客户端调用

**参数：**

- ContextInfo：特定对象
- positonInfo： [持仓](data_structure.md)

**返回：** 无

**示例：**

示例返回值

 ```py
#coding:gbk
def show_data(data):
    tdata = {}
    for ar in dir(data):
        if ar[:2] != 'm_':continue
        try:
            tdata[ar] = data.__getattribute__(ar)
        except:
            tdata[ar] = '<CanNotConvert>'
    return tdata

def init(ContextInfo):
    # 设置对应的资金账号
    # 示例需要在策略交易界面运行
    ContextInfo.set_account(account)

def after_init(ContextInfo):
    # 在策略交易界面运行时，account的值会被赋值为策略配置中的账号，编辑器界面运行时，需要手动赋值
    # 编译器界面里执行的下单函数不会产生实际委托
    passorder(23, 1101, account, "000001.SZ", 5, 0, 100, "示例", 2, "投资备注",ContextInfo)
    pass

def position_callback(ContextInfo, positionInfo):
    print(show_data(positionInfo))
```

```
{'m_bIsToday': True, 'm_dAvgOpenPrice': 9.417861115, 'm_dCloseAmount': 0.0, 'm_dCloseProfit': 0.0, 'm_dFloatProfit': 11.999999999999744, 'm_dInstrumentValue': 19640.0, 'm_dLastPrice': 9.82, 'm_dLastSettlementPrice': 0.0, 'm_dMargin': 0.0, 'm_dMarketValue': 19640.0, 'm_dOpenCost': 18835.72223, 'm_dOpenPrice': 9.417861115, 'm_dPositionCost': 18835.72223, 'm_dPositionProfit': 804.2777700000006, 'm_dProfitRate': 0.04269959814543308, 'm_dRealUsedMargin': 0.0, 'm_dRedemptionVolume': 0, 'm_dReferenceRate': 0.0, 'm_dRoyalty': 0.0, 'm_dSettlementPrice': 9.82, 'm_dSingleCost': 2.946, 'm_dStaticHoldMargin': 1.7976931348623157e+308, 'm_dStockLastPrice': 1.7976931348623157e+308, 'm_dStructFundVol': 0, 'm_dTotalCost': 5892.0, 'm_eFutureTradeType': 48, 'm_eSideFlag': 48, 'm_nCanUseVolume': 1200, 'm_nCidIncrease': 1953394499, 'm_nCidIsDelist': 678126433, 'm_nCidRateOfCurrentLine': 1667199589, 'm_nCidRateOfTotalValue': 1651272801, 'm_nCloseVolume': 0, 'm_nCoveredVolume': 0, 'm_nDirection': 48, 'm_nEnableExerciseVolume': -1, 'm_nFrozenVolume': 0, 'm_nHedgeFlag': 49, 'm_nLegId': 0, 'm_nOnRoadVolume': 800, 'm_nOptCombUsedVolume': 0, 'm_nPREnableVolume': 2000, 'm_nSettledAmt': 0, 'm_nStrategyID': 0, 'm_nVolume': 2000, 'm_nYesterdayVolume': 1200, 'm_strAccountID': '2000567', 'm_strAccountKey': '2____11194____114911____49____2000567____', 'm_strComTradeID': '', 'm_strExchangeID': 'SZ', 'm_strExchangeName': '深交所', 'm_strExpireDate': '', 'm_strInstrumentID': '000001', 'm_strInstrumentName': '平安银行', 'm_strOpenDate': '', 'm_strProductID': '', 'm_strProductName': '', 'm_strStockHolder': '', 'm_strTradeID': '', 'm_strTradingDay': '20240220', 'm_xtTag': None}
```

### orderError\_callback - 账号异常下单主推

提示

1. 仅在实盘运行模式下生效。
2. 需要先在init里调用ContextInfo.set\_account后生效。

**用法：** orderError\_callback(ContextInfo,orderArgs,errMsg)

**释义：** 当账号下单异常时，这个函数被客户端调用

**参数：**

- ContextInfo：特定对象
- orderArgs： [下单参数](data_structure.md)
- errMsg：错误信息

**返回：** 无

**示例：**

示例返回值

```py
#coding:gbk
def show_data(data):
    tdata = {}
    for ar in dir(data):
        if ar[:2] != 'm_':continue
        try:
            tdata[ar] = data.__getattribute__(ar)
        except:
            tdata[ar] = '<CanNotConvert>'
    return tdata

def init(ContextInfo):
    # 设置对应的资金账号
    # 示例需要在策略交易界面运行
    ContextInfo.set_account(account)

def after_init(ContextInfo):
    # 在策略交易界面运行时，account的值会被赋值为策略配置中的账号，编辑器界面运行时，需要手动赋值
    # 编译器界面里执行的下单函数不会产生实际委托
    passorder(23, 1101, account, "000001.SZ", 11, 0, 100, "示例", 2, "投资备注",ContextInfo)
    pass

def orderError_callback(ContextInfo,orderArgs,errMsg):
    print(show_data(orderArgs))
    print(errMsg)
```

```
{'accountID': '2000567', 'currentTime': 0, 'formulaName': '', 'modelPrice': 0.0, 'modelVolume': 100.0, 'opType': 23, 'orderCode': 'SZ000001', 'orderType': 1101, 'prType': 11, 'strategyName': '示例_&&&_投资备注'}
[函数交易]　函数: passorder,　证券 [SZ000001] 指定价 无效, 无法下单!
```

## 其他主推函数

### credit\_account\_callback - 查询信用账户明细回调

**用法：** credit\_account\_callback(ContextInfo,seq,result)

**释义：** 查询信用账户明细回调

**参数：**

- ContextInfo：策略模型全局对象
- seq:query\_credit\_account时输入查询seq
- result: [信用账户明细](data_structure.md)

### credit\_opvolume\_callback - 查询两融最大可下单量的回调

**用法：** credit\_opvolume\_callback(ContextInfo,accid,seq,ret,result)

**释义：** 查询两融最大可下单量的回调。

**参数：**

- `ContextInfo`：策略模型全局对象
- `accid`:查询的账号
- `seq`:`query_credit_opvolume`时输入查询`seq`
- `ret`:查询结果状态。正常返回:`1`,正在查询中`-1`,输入账号非法:`-2`,输入查询参数非法:`-3`,超时等服务器返回报错:`-4`
- `result`:查询到的结果

**示例** 见 [query\_credit\_opvolume](callback_function.md)
