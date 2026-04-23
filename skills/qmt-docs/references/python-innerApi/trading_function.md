---
url: "https://dict.thinktrader.net/innerApi/trading_function.html"
title: "交易函数 | 迅投知识库"
---

## 交易下单函数

### passorder - 综合下单函数

综合下单函数，用于股票、期货、期权等下单和新股、新债申购、融资融券等交易操作 **推荐使用**

提示

1. 推荐使用
2. 可覆盖多品种下单
3. 注意参数的变化

**调用方法：**

python示例

```
passorder(
    opType, orderType, accountid
    , orderCode, prType, price, volume
    , strategyName, quickTrade, userOrderId
    , ContextInfo
)
'''
passorder(
    2 #opType 操作号
    , 1101 #orderType 组合方式
    , '1000044' #accountid 资金账号
    , 'cu2403.SF' #orderCode 品种代码
    , 14 #prType 报价类型
    , 0.0 #price 价格
    , 2 #volume 下单量
    , '示例下单' #strategyName 策略名称
    , 1 #quickTrade 快速下单标记
    , '投资备注' #userOrderId 投资备注
    , C #ContextInfo 策略上下文
)
'''
```

 ```py
#coding:gbk

'''
# 在策略交易界面运行时，account的值会被赋值为策略配置中的账号，编辑器界面运行时，需要手动赋值
# 编译器界面里执行的下单函数不会产生实际委托
'''
account = "test"
def init(ContextInfo):
    pass
def handlebar(ContextInfo):
    if not ContextInfo.is_last_bar():
        return
    # 单股单账号期货最新价买入 10 手，快速下单参数设置为 1
    passorder(0, 1101, account, "rb2405.SF", 5, -1, 10, "示例", 1, "投资备注",ContextInfo)

    # 单股单账号期货指定价买入 10 手，快速下单参数设置为 1
    passorder(0, 1101, account,  "rb2405.SF", 11, 3000, 10, "示例", 1, "投资备注",ContextInfo)

    # 单股单账号股票最新价买入 100 股（1 手），快速下单参数设置为 1
    passorder(23, 1101, account, "000001.SZ", 5, 0, 100, "示例", 1, "投资备注",ContextInfo)

    # 单股单账号股票指定价买入 100 股（1 手），快速下单参数设置为 1
    passorder(23, 1101, account, "000001.SZ", 11, 7, 100, "示例", 1, "投资备注",ContextInfo)
```

**参数：**

| 参数名 | 类型 | 说明 | 提示 |
| --- | --- | --- | --- |
| `opType` | `int` | 交易类型 | 可选买、买，期货开仓、平仓等<br>可选值参考 [opType-操作类型](enum_constants.md#optype-%E6%93%8D%E4%BD%9C%E7%B1%BB%E5%9E%8B) |
| `orderType` | `int` | 下单方式 | 可选值参考 [orderType-下单方式](enum_constants.md#ordertype-%E4%B8%8B%E5%8D%95%E6%96%B9%E5%BC%8F)<br> 可选按股票数量买卖或按照金额等方式买卖<br>一、期货不支持 1102 和 1202;<br>二、对所有账号组的操作相当于对账号组里的每个账号做一样的操作，如 `passorder (23, 1202, 'testS', '000001. SZ', 5, -1, 50000, ContextInfo)`，意思就是对账号组 `testS` 里的所有账号都以最新价开仓买入 50000 元市值的 `000001.SZ` 平安银行；`passorder (60,1101,"test",'510050. SH', 5,-1,1, ContextInfo)`意思就是账号`test`申购 1 个单位 (900000股)的华夏上证50ETF (只申购不买入成分股)。 |
| `accountID` | `string` | 资金账号 | 下单的账号ID（可多个）或账号组名或套利组名（一个篮子一个套利账号，如 accountID = '股票账户名, 期货账号'） |
| `orderCode` | `string` | 下单代码 | 1\. 如果是单股或单期货、港股，则该参数填合约代码；<br>2\. 如果是组合交易, 则该参数填篮子名称，参考 [组合交易](code_examples.html#%E7%BB%84%E5%90%88%E4%BA%A4%E6%98%93-1)；<br>3\. 如果是组合套利，则填一个篮子名和一个期货合约名（如orderCode = '篮子名, 期货合约名'），请参考 [组合套利交易](code_examples.md#%E7%BB%84%E5%90%88%E5%A5%97%E5%88%A9%E4%BA%A4%E6%98%93-1) |
| `prType` | `int` | 下单选价类型 | 可选值参考 [prType-下单选价类型](enum_constants.md#prtype-%E4%B8%8B%E5%8D%95%E9%80%89%E4%BB%B7%E7%B1%BB%E5%9E%8B)<br>特别的对于套利，这个 prType 只对篮子起作用，期货的采用默认的方式） |
| `price` | `float` | 下单价格 | 一、单股下单时，`prType` 是模型价/科创板盘后定价时 `price` 有效；其它情况无效；<br>1.1 即单股时， `prType` 参数为 `11`，`49` 时被使用。 <br>1.2 `prType` 参数不为 `11`，`49` 时也需填写，填写的内容可为 `-1`，`0`，`2`，`100` 等任意数字；<br>二、组合下单时，是组合套利时，price 作套利比例有效，其它情况无效。 |
| `volume` | `int` | 下单数量（股 / 手 / 元 / %） | 根据 orderType 值最后一位确定 volume 的单位，可选值参考 [volume - 下单](enum_constants.md#volume-%E4%B8%8B%E5%8D%95%E6%95%B0%E9%87%8F) |
| `strategyName` | `string` | 自定义策略名 | 一、用来区分 `order` 委托和`deal` 成交来自不同的策略。<br>根据该策略名，`get_trade_detail_data`，`get_last_order_id` 函数可以获取相应策略名对应的委托或成交集合。 <br>`strategyName` 只对同账号本地客户端有效，即 `strategyName` 只对当前客户端下的单进行策略区分，且该策略区分只能当前客户端使用。 |
| `quickTrade` | `int` | 设定是否立即触发下单 | 可选值参考 [quicktrade - 快速下单](enum_constants.md#quicktrade-%E5%BF%AB%E9%80%9F%E4%B8%8B%E5%8D%95)<br>`passorder`是对最后一根K线完全走完后生成的模型信号在下一根K线的第一个tick数据来时触发下单交易；<br>采用`quickTrade`参数设置为`1`时，非历史bar上执行时`（ContextInfo.is_last_bar()`为`True`），只要策略模型中调用到就触发下单交易。<br>`quickTrade`参数设置为`2`时，不判断bar状态，只要策略模型中调用到就触发下单交易，历史bar上也能触发下单，请谨慎使用。 |
| `userOrderId` | `string` | 用户自设委托 ID | 如果传入该参数，<br>则 `strategyName` 和 `quickTrade` 参数也填写。<br>对应 `order` 委托对象和 `deal` 成交对象中的 `m_strRemark` 属性，通过 `get_trade_detail_data` 函数或委托主推函数 `order_callback` 和成交主推函数 `deal_callback` 可拿到这两个对象信息。 |
| ContextInfo | class | 系统参数 | 含有k线信息和接口的上下文对象 |

**返回：**

无

**更多示例：**

01. [股票](code_examples.md#%E8%82%A1%E7%A5%A8)
02. [基金](code_examples.md#%E5%9F%BA%E9%87%91)
03. [两融](code_examples.md#%E4%B8%A4%E8%9E%8D-1)
04. [期货](code_examples.md#%E6%9C%9F%E8%B4%A7)
05. [期权](code_examples.md#%E6%9C%9F%E6%9D%83)
06. [新股申购](code_examples.md#%E6%96%B0%E8%82%A1%E7%94%B3%E8%B4%AD)
07. [债券](code_examples.md#%E5%80%BA%E5%88%B8)
08. [ETF](code_examples.md#etf)
09. [组合交易](code_examples.md#%E7%BB%84%E5%90%88%E4%BA%A4%E6%98%93)
10. [组合套利交易](code_examples.md#%E7%BB%84%E5%90%88%E5%A5%97%E5%88%A9%E4%BA%A4%E6%98%93)

### algo\_passorder - 算法下单（拆单）函数

用于按固定时间间隔和固定规则把目标交易数量拆分成多次下单的交易函数

**调用用法：**

python

```
algo_passorder(opType,orderType,accountid,orderCode,prType,price,volume,[strategyName,quickTrade,userOrderId,userOrderParam],ContextInfo)`
```

提示

算法交易下单，此时使用 **交易面板-程序交易-函数交易-函数交易** 参数中设置的下单类型(普通交易,算法交易,随机量交易) 如果函数交易参数使用未修改的默认值,此函数和`passorder`函数一致， 设置了函数交易参数后，将会使用函数交易参数的超价等拆单参数，`algo_passorder`内的`prType`若赋值,则优先使用该参数，若`algo_passorder`内的`prType=-1`,将会使用`userOrderParam`内的`opType`，若`userOrderParam`未赋值，则使用界面上的函数交易参数的报价方式

**参数：**

其他参数同`passorder`，详细解释可参考`passorder`的说明

`userOrderParam``dict[str:value]` 是用户自定义交易参数,主要用于修改算法交易的参数 其中`Key``Value`定义如下

注：所有参数均为非必选

| Key | Value类型 | Value |
| --- | --- | --- |
| OrderType | int | 普通交易:`0`<br>算法交易:`1`<br>随机量交易:`2` |
| PriceType | int | 报价方式:数值同passorde prType |
| MaxOrderCount | int | 最大下单次数 |
| SinglePriceRange | int | 波动区间是否单向:<br>否:`0`，<br>是:`1` |
| PriceRangeType | int | 波动区间类型按比例:`0`,按数值`1` |
| PriceRangeValue | float | 波动区间(按数值) |
| PriceRangeRate | float | 波动区间(按比例)\[`0-1`\] |
| SuperPriceType | int | 单笔超价类型:<br>按比例:`0`<br>按数值`1` |
| SuperPriceRate | float | 单笔超价(按比例)\[`0-1`\] |
| SuperPriceValue | float | 单笔超价(按数值) |
| VolumeType | int | 单笔基准量类型卖1+2+3+4+5量:`0`<br>卖1+2+3+4量:`1`<br>...<br>卖1量:`4`<br>买1量:`5`<br>...<br>买1+2+3+4+5量:`9`<br>目标量:`10`<br>目标剩余量:`11`<br>持仓数量:`12` |
| VolumeRate | float | 单笔下单比率\[`0-1`\] |
| SingleNumMin | float | 单笔下单量最小值 |
| SingleNumMax | float | 单笔下单量最大值 |
| ValidTimeType | int | 有效时间类型:<br>`0`:按持续时间<br>`1` 按时间区间，默认为0 |
| ValidTimeElapse | int | 有效持续时间,ValidTimeType设置为0时生效 |
| ValidTimeStart | int | 有效开始时间偏移,ValidTimeType设置为1时生效 |
| ValidTimeEnd | int | 有效结束时间偏移,ValidTimeType设置为1时生效 |
| UndealtEntrustRule | int | 未成委托处理数值同prType |
| PlaceOrderInterval | int | 下撤单时间间隔 |
| UseTrigger | int | 是否触价:<br>否:`0`<br>是:`1` |
| TriggerType | int | 触价类型:<br>最新价大于:`1`<br>最新价小于:`2` |
| TriggerPrice | float | 触价价格 |
| SuperPriceEnable | int | 超价启用笔数 |

**返回**

无

**示例**

python

 ```py
#coding:gbk
userparam = {
    "OrderType": 1,
    "MaxOrderCount": 20,
    "SuperPriceType": 1,
    "SuperPriceValue": 1.12}
accid = '918800000818'  #资金账号
algo_passorder(23,1101,accid,'000001.SZ',5,15,1000,'',1,'strReMark',userparam,ContextInfo)
#表示修改算法交易的最大委托次数为20,单笔下单基准类型为按价格类型超价,单笔超价1.12元,其他参数同函数交易参数中设置
```

### smart\_algo\_passorder - 智能算法（VWAP 等）函数

提示

1. 调用该函数需要有【智能算法】使用权限

用于使用主动算法或被动算法交易的函数如VWAP TWAP等

**调用方法一：**

python

```
smart_algo_passorder(opType,orderType,accountid,orderCode,prType,price,volume,strageName,quickTrade,userOrderId,smartAlgoType,limitOverRate,minAmountPerOrder,[targetPriceLevel,startTime,endTime,limitControl],ContextInfo)
```

提示

可选参数可缺省

**参数：**

其他参数同`passorder`，详细解释可参考 [passorder的说明](trading_function.md#passorder-%E7%BB%BC%E5%90%88%E4%B8%8B%E5%8D%95%E5%87%BD%E6%95%B0)

| 参数名 | 类型 | 说明 | 提示 |
| --- | --- | --- | --- |
| prType | int | **可选值**：<br>11:限价（只对单股情况支持,对组合交易不支持）<br> 12:市价 <br>**特别的对于套利：这个prType只对篮子起作用，期货的采用默认的方式** |  |
| smartAlgoType | str | 智能算法类型 \[ [enum\_constants#smartAlgoType智能算法类型](enum_constants.md#enum-eordertype-%E7%AE%97%E6%B3%95%E4%BA%A4%E6%98%93%E3%80%81%E6%99%AE%E9%80%9A%E4%BA%A4%E6%98%93%E7%B1%BB%E5%9E%8B)\] |  |
| limitOverRate | int | 量比 数据范围0-100 | 网格算法无此项<br>若在algoParam中填写量比，则填写范围0-1的小数。 |
| minAmountPerOrder | int | 智能算法最小委托金额，数据范围0-100000 |  |
| targetPriceLevel | int | 智能算法目标价格,可选值：<br>1：己方盘口 1<br> 2：己方盘口2<br>3：己方盘口3<br>4：己方盘口4<br>5：己方盘口5<br>6：最新价<br>7：对方盘口 | 一、输入无效值则targetPriceLevel为1<br>二、本项只针对冰山算法,其他算法可缺省。 |
| startTime | str | 智能算法开始时间 | 格式"HH:MM:SS"，如"10:30:00"。如果缺省值，则默认为"09:30:00" |
| endTime | str | 智能算法截止时间 | 格式"HH:MM:SS"，如"14:30:00"。如果缺省值，则默认为"15:30:00" |
| limitControl | int | 涨跌停控制 | 默认值为1<br>1：涨停不卖跌停不买<br>0：无限制 |

**返回**

无

**示例：**

python

 ```py
#coding:gbk

def init(ContextInfo):
    pass

def after_init(ContextInfo):
    # # 使用smart_algo_passorder 下单
    smart_algo_passorder(
        23,                # 买入
        1101,              # 表示volume的单位是股
        account,           # 资金账号
        '000001.SZ',
        12,                #  11限价，12市价
        0,                 # 限价时，价格填任意数量占位
        50000,             # 5000股
        '',
        2,                 # quickTrade
        '',
        'VWAP',
        25,                 # 量比25%
        0,                  # 智能算法最小委托金额
        1,                  # 智能算法目标价格 本项只针对冰山算法,其他算法可缺省。
        "10:25:00",         # 开始时间
        "14:50:00",         # 结束时间
        1,                  # 涨跌停控制 1为涨停不卖跌停不卖 0 为无限制
        ContextInfo
        )
```

**调用方法二：**

当时用algoParam时，函数声明为：`smart_algo_passorder(opType,orderType,accountid,orderCode,prType,modelprice,volume,strageName,quickTrade,userid,smartAlgoType,startTime,endTime,algoParam,ContextInfo)`参数均不可缺省

`smartAlgoType`,`startTime`,`endTime` 含义同上，`algoParam`请使用下面的方法获取：

#### 获取algoParam具体字段

**释义**

获取智能算法参数配置信息

**用法**

python

```
get_smart_algo_param(algoList)
```

**参数**

| 参数 | 类型 | 说明 |
| --- | --- | --- |
| `algoList` | list | 需要查询参数配置信息的算法名称列表, 若传空则查询全部有权限的算法参数配置信息 |

**返回**

返回一个字典，键为算法名称，值为参数字典列表。

| 字段 | 类型 | 说明 |
| --- | --- | --- |
| `key` | string | 参数名称key值,即`smart_algo_order`中`algoList`字典需要传的键值 |
| `name` | string | 参数名称 |
| `dataType` | string | 参数类型 |
| `valueRange` | string | 参数范围 |
| `defaultValue` | string | 参数默认值 |
| `enumName` | string | 参数枚举值的名称 |
| `enumValue` | string | 参数实际的枚举值 |
| `unit` | string | 参数的单位, 当单位为%时, 值要填写小数而非参数范围所示的百分数值 |
| `valueRangeByName` | string | 不同算法参数范围 |
| `defaultValueByName` | string | 不同算法参数默认值 |

**示例**

python

 ```py
#coding:gbk

def init(ContextInfo):
    pass

    # 方法2 使用algoParam 和smart_algo_passorder
    # 该方法部分旧版本客户端可能会不支持
    # algoParam
    # 先获取所有需要传入的参数
    #
    print(get_smart_algo_param(['VWAP']))
    '''
    输出：[2024-01-30 11:21:10][智能算法1][SH000300][日线]
    {'VWAP': [\
        {'key': 'm_dLimitOverRate', 'name': '量比比例', 'dataType': '浮点数', 'valueRange': '0.00-100.00', 'defaultValue': '20.00', 'enumName': '', 'enumValue': '', 'unit': '%', 'valueRangByName': '', 'defaultValueByName': ''},\
        {'key': 'm_dMinAmountPerOrder', 'name': '委托最小金额', 'dataType': '整数', 'valueRange': '0-100000', 'defaultValue': '0', 'enumName': '', 'enumValue': '', 'unit': '', 'valueRangByName': '', 'defaultValueByName': ''},\
        {'key': 'm_dMaxAmountPerOrder', 'name': '委托最大金额', 'dataType': '浮点数', 'valueRange': '0.00-100000000.00', 'defaultValue': '0', 'enumName': '', 'enumValue': '', 'unit': '', 'valueRangByName': '', 'defaultValueByName': ''},\
        {'key': 'm_nStopTradeForOwnHiLow', 'name': '涨跌停控制', 'dataType': '整数', 'valueRange': '', 'defaultValue': '涨停不卖跌停不买', 'enumName': '无,涨停不卖跌停不买', 'enumValue': '0,1', 'unit': '', 'valueRangByName': '', 'defaultValueByName': ''},\
        {'key': 'm_dMulitAccountRate', 'name': '多账号总量比', 'dataType': '浮点数', 'valueRange': '0.00-100.00', 'defaultValue': '0', 'enumName': '', 'enumValue': '', 'unit': '%', 'valueRangByName': '', 'defaultValueByName': ''},\
        {'key': 'm_strCmdRemark', 'name': '投资备注', 'dataType': '字符串', 'valueRange': '', 'defaultValue': '', 'enumName': '', 'enumValue': '', 'unit': '', 'valueRangByName': '', 'defaultValueByName': ''}]}
    '''
    algoParam={
    'm_dLimitOverRate': 0.25,      # 量比 25%
    'm_dMinAmountPerOrder':0,      # 委托最小金额
    'm_dMaxAmountPerOrder':10000,  # 委托最大金额
    'm_nStopTradeForOwnHiLow': 1,  # 涨跌停控制
    'm_dMulitAccountRate':0.30,    # 多账号总量比
    'm_strCmdRemark':  '投资备注1'  # 投资备注
    }
    smart_algo_passorder(
        23,
        1101,
        account,
        '600000.SH',
        12,
        0,
        10000,
        '',
        2,               # quickTrade
        '投资备注',
        'VWAP',
        "10:25:00",      # 开始时间
        "14:50:00",      # 结束时间
        algoParam,       # 算法参数
        ContextInfo
        )

```

### cancel-撤销委托

**调用方法**`cancel(orderId, accountId, accountType, ContextInfo)`

**参数**

| 参数名 | 类型 | 含义 | 说明 |
| --- | --- | --- | --- |
| orderId | string | 委托号 | 必填 |
| accountID | string | 资金账号 | 必填 |
| AccountType | string | 账号类型 可选：<br>'FUTURE'：期货<br>'STOCK'：股票<br>'CREDIT'：信用<br>'HUGANGTONG'：沪港通<br>'SHENGANGTONG'：深港通<br>'STOCK\_OPTION'：期权 | 必填 |
| ContextInfo | class | 含有k线信息和接口的上下文对象 | 必填 |

**返回** bool，是否发出了取消委托信号，返回值含义：

> True：是
>
> False：否

**示例**

python返回值

 ```py
#coding:gbk
'''
（1）下单前,根据 get_trade_detail_data 函数返回账号的信息，判定资金是否充足，账号是否在登录状态，统计持仓情况等等。
（2）满足一定的模型条件，用 passorder 下单。
（3）下单后，时刻根据 get_last_order_id 函数获取委托和成交的最新id，注意如果委托生成了，就有了委托号（这个id需要自己保存做一个全局控制）。
（4）用该委托号根据 get_value_by_order_id 函数查看委托的状态，各种情况等。
当一个委托的状态变成“已成'后，那么对应的成交 deal 信息就有一条成交数据；用该委托号可查看成交情况。
*注：委托列表和成交列表中的委托号是一样的,都是这个 m_strOrderSysID 属性值。
可用 get_last_order_id 获取最新的 order 的委托号,然后根据这个委托号获取 deal 的信息，当获取成功后，也说明这笔交易是成了，可再根据 position 持仓信息再进一步验证。
（5）根据委托号获取委托信息，根据委托状态，或模型设定，用 cancel 取消委托。
'''

def init(ContextInfo):
    ContextInfo.accid = '6000000248'

def handlebar(ContextInfo):
    if ContextInfo.is_last_bar():
        orderid = get_last_order_id(ContextInfo.accid, 'stock', 'order')
        print(cancel(orderid, ContextInfo.accid, 'stock', ContextInfo))
```

```
[2023-10-31 13:27:48][TESTC][SH000300][日线] True
```

### cancel\_task - 撤销任务

**调用方法**`cancel_task(taskId,accountId,accountType,ContextInfo)`

**参数**

| 参数名 | 类型 | 含义 | 说明 |
| --- | --- | --- | --- |
| taskId | string | 委托号 | 必填 |
| accountID | string | 资金账号 | 必填 |
| AccountType | string | 账号类型 可选：<br>'FUTURE'：期货<br>'STOCK'：股票<br>'CREDIT'：信用<br>'HUGANGTONG'：沪港通<br>'SHENGANGTONG'：深港通<br>'STOCK\_OPTION'：期权 | 必填 |
| ContextInfo | class | 含有k线信息和接口的上下文对象 | 必填 |

**返回** bool，是否发出了撤销任务信号，返回值含义：

> True：是
>
> False：否

**示例**

python

 ```py
#coding:gbk
'''
（1）根据get_trade_detail_data函数返回任务的信息,获取任务编号（m_nTaskId），任务状态等等；
（2）根据任务编号，用cancel_task取消委托。
'''

def init(ContextInfo):
    ContextInfo.accid = '6000000248'

def handlebar(ContextInfo):
    # 获取当前客户端所有的任务
    if ContextInfo.is_last_bar():
        objlist = get_trade_detail_data(ContextInfo.accid,'stock','task')
        for obj in objlist:
            cancel_task(str(obj.m_nTaskId),ContextInfo.accid,'stock',ContextInfo)
```

### pause\_task - 暂停任务

暂停智能算法任务

**调用方法** pause\_task(taskId,accountId,accountType,ContextInfo)

**参数**

| 参数名 | 类型 | 含义 | 说明 |
| --- | --- | --- | --- |
| taskId | string | 委托号 | 必填 |
| accountID | string | 资金账号 | 必填 |
| AccountType | string | 账号类型 可选：<br>'FUTURE'：期货<br>'STOCK'：股票<br>'CREDIT'：信用<br>'HUGANGTONG'：沪港通<br>'SHENGANGTONG'：深港通<br>'STOCK\_OPTION'：期权 | 必填 |
| ContextInfo | class | 含有k线信息和接口的上下文对象 | 必填 |

**返回** bool，是否发出了暂停任务信号，返回值含义：

> True：是
>
> False：否

**示例**

python

 ```py
#coding:gbk
'''
（1）根据get_trade_detail_data函数返回任务的信息,获取任务编号（m_nTaskId），任务状态等等；
（2）根据任务编号，用pause_task暂停智能算法任务。
'''

def init(ContextInfo):
    ContextInfo.accid = '6000000248'

def handlebar(ContextInfo):

    if ContextInfo.is_last_bar():
        # 获取当前客户端所有的任务
        objlist = get_trade_detail_data(ContextInfo.accid,'stock','task')
        for obj in objlist:
            pause_task(obj.m_nTaskId,ContextInfo.accid,'stock',ContextInfo)
```

### resume\_task - 继续任务

继续智能算法任务

**调用方法**`resume_task(taskId,accountId,accountType,ContextInfo)`

**参数**

| 参数名 | 类型 | 含义 | 说明 |
| --- | --- | --- | --- |
| taskId | string | 委托号 | 必填 |
| accountID | string | 资金账号 | 必填 |
| AccountType | string | 账号类型 可选：<br>'FUTURE'：期货<br>'STOCK'：股票<br>'CREDIT'：信用<br>'HUGANGTONG'：沪港通<br>'SHENGANGTONG'：深港通<br>'STOCK\_OPTION'：期权 | 必填 |
| ContextInfo | class | 含有k线信息和接口的上下文对象 | 必填 |

**返回** bool，是否发出了重启任务信号，返回值含义：

> True：是
>
> False：否

**示例**

python

 ```py
#coding:gbk
'''
（1）根据get_trade_detail_data函数返回任务的信息,获取任务编号（m_nTaskId），任务状态等等；
（2）根据任务编号，用resume_task启动已暂停智能算法任务。
'''

def init(ContextInfo):
    ContextInfo.accid = '6000000248'
def handlebar(ContextInfo):
    if ContextInfo.is_last_bar():
        # 获取当前客户端所有的任务
        objlist = get_trade_detail_data(ContextInfo.accid,'stock','task')
        for obj in objlist:
            resume_task(obj.m_nTaskId,ContextInfo.accid,'stock',ContextInfo)
```

### get\_basket-获取股票篮子

**用法：** get\_basket(basketName)

**释义：** 获取股票篮子

**参数：**

- basketName：股票篮子名称

**示例：**

```
print( get_basket('basket1') )
```

### set\_basket-设置股票篮子

**用法：** set\_basket(basketDict)

**释义：** 设置passorder的股票篮子,仅用于passorder进行篮子交易,设置成功后,用get\_basket可以取出后即可进行passorder组合交易下单

**参数：**

- basketDict：股票篮子 {'name':股票篮子名称,'stocks':\[{'stock':股票名称,'weight',权重,'quantity':数量,'optType':交易类型}\]} 。

**示例：**

```
table=[\
    {'stock':'600000.SH','weight':0.11,'quantity':100,'optType':23},\
    {'stock':'600028.SH','weight':0.11,'quantity':200,'optType':24},\
]
basket={'name':'basket1','stocks':table}
set_basket(basket)
#一键买卖2份(2101代表用篮子里quantity字段)basket1里面的股票组合，即600000.SH买入200股，600028.SH卖出400股
passorder(35,2101,ContextInfo.accid,'basket1',5,-1,2,'basketOrder',2,'basketOrder',ContextInfo)
```

## 交易查询函数

### get\_trade\_detail\_data-查询账号资金信息、委托记录等

**调用方法**`get_trade_detail_data(accountID, strAccountType, strDatatype, strategyName)`

或不区分策略

`get_trade_detail_data(accountID, strAccountType, strDatatype)`

**参数**

| 参数名 | 类型 | 说明 | 备注 |
| --- | --- | --- | --- |
| accountID | string | 资金账号 | 必填 |
| strAccountType | string | 账号类型 可选：<br>'FUTURE'：期货<br>'STOCK'：股票<br>'CREDIT'：信用<br>'HUGANGTONG'：沪港通<br>'SHENGANGTONG'：深港通<br>'STOCK\_OPTION'：期权 | 必填 |
| strDatatype | string | 要查询数据类型 可选：<br>`ACCOUNT`： [账号对象](data_structure.html#account-%E8%B4%A6%E6%88%B7%E5%AF%B9%E8%B1%A1) 或 [信用账号对象](data_structure.html#ccreditaccountdetail-%E4%BF%A1%E7%94%A8%E8%B4%A6%E5%8F%B7%E5%AF%B9%E8%B1%A1-%E9%9D%9E%E6%9F%A5%E6%9F%9C%E5%8F%B0)<br>`POSITION`： [持仓](data_structure.md#position-statistics-%E6%8C%81%E4%BB%93%E7%BB%9F%E8%AE%A1%E5%AF%B9%E8%B1%A1)<br>`POSITION_STATISTICS`： [持仓统计](data_structure.md#position-statistics-%E6%8C%81%E4%BB%93%E7%BB%9F%E8%AE%A1%E5%AF%B9%E8%B1%A1)<br>`ORDER`： [委托](data_structure.md#order-%E5%A7%94%E6%89%98%E5%AF%B9%E8%B1%A1)<br>`DEAL` ： [成交](data_structure.md#deal-%E6%88%90%E4%BA%A4%E5%AF%B9%E8%B1%A1)<br>`TASK`： [任务](data_structure.md#ctaskdetail-%E4%BB%BB%E5%8A%A1%E5%AF%B9%E8%B1%A1) | 必填 |
| strategyName | string | 策略 当用`passorder`下单时指定了strategyName 参数时，当查询成交和委托时传入同样的`strageName`，则可以只返回包含`strategyName`的委托子集或成交子集 | `strategyName`参数只对成交和委托有效,选填 |

**返回** list，list 中放的是对应strDatatype的 Python对象，通过 dir(pythonobj) 可返回某个对象的属性列表。

有五种交易相关信息，包括：

ACCOUNT： [账号对象](data_structure.html#account-%E8%B4%A6%E6%88%B7%E5%AF%B9%E8%B1%A1) 或 [信用账号对象](data_structure.md#ccreditaccountdetail-%E4%BF%A1%E7%94%A8%E8%B4%A6%E5%8F%B7%E5%AF%B9%E8%B1%A1-%E9%9D%9E%E6%9F%A5%E6%9F%9C%E5%8F%B0)

POSITION： [持仓明细](data_structure.md#position-%E6%8C%81%E4%BB%93%E5%AF%B9%E8%B1%A1)

POSITION\_STATISTICS: [持仓统计](data_structure.md#position-statistics-%E6%8C%81%E4%BB%93%E7%BB%9F%E8%AE%A1%E5%AF%B9%E8%B1%A1)

ORDER： [委托](data_structure.md#order-%E5%A7%94%E6%89%98%E5%AF%B9%E8%B1%A1)

DEAL： [成交](data_structure.md#deal-%E6%88%90%E4%BA%A4%E5%AF%B9%E8%B1%A1)

TASK： [任务](data_structure.md#ctaskdetail-%E4%BB%BB%E5%8A%A1%E5%AF%B9%E8%B1%A1)

**示例：**

python返回值

```

#coding:gbk

account = '800174' # 在策略交易界面运行时，account的值会被赋值为策略配置中的账号，编辑器界面运行时，需要手动赋值；编译器环境里执行的下单函数不会产生实际委托

def init(ContextInfo):
    pass

def handlebar(ContextInfo):
    if not ContextInfo.is_last_bar():
        return

    orders = get_trade_detail_data(account, 'stock', 'order')
    print('查询委托结果：')
    for o in orders:
        print(f'股票代码: {o.m_strInstrumentID}, 市场类型: {o.m_strExchangeID}, 证券名称: {o.m_strInstrumentName}, 买卖方向: {o.m_nOffsetFlag}',
        f'委托数量: {o.m_nVolumeTotalOriginal}, 成交均价: {o.m_dTradedPrice}, 成交数量: {o.m_nVolumeTraded}, 成交金额:{o.m_dTradeAmount}')

    deals = get_trade_detail_data(account, 'stock', 'deal')
    print('查询成交结果：')
    for dt in deals:
        print(f'股票代码: {dt.m_strInstrumentID}, 市场类型: {dt.m_strExchangeID}, 证券名称: {dt.m_strInstrumentName}, 买卖方向: {dt.m_nOffsetFlag}',
        f'成交价格: {dt.m_dPrice}, 成交数量: {dt.m_nVolume}, 成交金额: {dt.m_dTradeAmount}')

    positions = get_trade_detail_data(account, 'stock', 'position')
    print('查询持仓结果：')
    for dt in positions:
        print(f'股票代码: {dt.m_strInstrumentID}, 市场类型: {dt.m_strExchangeID}, 证券名称: {dt.m_strInstrumentName}, 持仓量: {dt.m_nVolume}, 可用数量: {dt.m_nCanUseVolume}',
        f'成本价: {dt.m_dOpenPrice:.2f}, 市值: {dt.m_dInstrumentValue:.2f}, 持仓成本: {dt.m_dPositionCost:.2f}, 盈亏: {dt.m_dPositionProfit:.2f}')

    accounts = get_trade_detail_data(account, 'stock', 'account')
    print('查询账号结果：')
    for dt in accounts:
        print(f'总资产: {dt.m_dBalance:.2f}, 净资产: {dt.m_dAssureAsset:.2f}, 总市值: {dt.m_dInstrumentValue:.2f}',
        f'总负债: {dt.m_dTotalDebit:.2f}, 可用金额: {dt.m_dAvailable:.2f}, 盈亏: {dt.m_dPositionProfit:.2f}')

    position_statistics = get_trade_detail_data(account,"FUTURE",'POSITION_STATISTICS')
    for obj in position_statistics:
        if obj.m_nDirection == 49:
			continue
		PositionInfo_dict[obj.m_strInstrumentID+"."+obj.m_strExchangeID]={
		"持仓":obj.m_nPosition,
		"成本":obj.m_dPositionCost,
		"浮动盈亏":obj.m_dFloatProfit,
		"保证金占用":obj.m_dUsedMargin
		}
	print(PositionInfo_dict)


```

```
8000000213
【2023-10-31 13:35:41.063】  [quote]start simulation mode
【2023-10-31 13:35:41.125】  查询委托结果：
股票代码: 000001, 市场类型: SZ, 证券名称: 平安银行, 买卖方向: 48 委托数量: 5000, 成交均价: 10.43, 成交数量: 2500, 成交金额:26075.0
查询成交结果：
股票代码: 000001, 市场类型: SZ, 证券名称: 平安银行, 买卖方向: 48 成交价格: 10.43, 成交数量: 2500, 成交金额: 26075.0
查询持仓结果：
股票代码: 110055, 市场类型: SH, 证券名称: 伊力转债, 持仓量: 10, 可用数量: 10 成本价: 174.66, 市值: 1767.50, 持仓成本: 1746.57, 盈亏: 20.93
股票代码: 000001, 市场类型: SZ, 证券名称: 平安银行, 持仓量: 2500, 可用数量: 0 成本价: 10.43, 市值: 26150.00, 持仓成本: 26075.00, 盈亏: 75.00
股票代码: 123018, 市场类型: SZ, 证券名称: 溢利转债, 持仓量: 10, 可用数量: 10 成本价: 353.02, 市值: 3117.42, 持仓成本: 3530.23, 盈亏: -412.81
股票代码: 128136, 市场类型: SZ, 证券名称: 立讯转债, 持仓量: 60, 可用数量: 60 成本价: 109.30, 市值: 6715.56, 持仓成本: 6558.03, 盈亏: 157.53
查询账号结果：总资产: 999999839.30, 净资产: 999999839.30, 总市值: 37750.48 总负债: 0.00, 可用金额: 999962089.17, 盈亏: -159.35
{'持仓': 22, '成本': 1726450.0, '浮动盈亏': 0.0, '保证金占用': 207174.0}
```

### get\_history\_trade\_detail\_data - 查询历史交易明细

**用法：** get\_history\_trade\_detail\_data(accountID,strAccountType,strDatatype,strStratDate,strEndDate);

**释义：** 获取历史成交明细数据，返回结果为一个(\[timetag,obj...\])的元组

**参数：**

accountID：string,账号； strAccountType：string,账号类型,有"FUTURE","STOCK","CREDIT","HUGANGTONG","SHENGANGTONG","STOCK\_OPTION"； strDatatype：string,交易明细数据类型,有：持仓"POSITION"、委托"ORDER"、成交"DEAL"； strStratDate：string,开始时间,如'20240513'； strEndDate：string,结束时间,如'20240514'；

\*\*返回：\*\*list,list中放的是PythonObj,通过dir(pythonobj)可返回某个对象的属性列表 **示例：**

示例

```
def handlebar(ContextInfo):
    obj_list = get_history_trade_detail_data('6000000248','stock','position','20240513','20240514')
    for time,data in obj_list:
        for obj in data:
            print(obj.m_strInstrumentID)
            print(dir(obj))#查看有哪些属性字段
```

### get\_ipo\_data-获取当日新股新债信息

**用法：** get\_ipo\_data(\[,type\])

**释义：** 获取当日新股新债信息，返回结果为一个字典,包括新股申购代码,申购名称,最大申购数量,最小申购数量等数据

**参数：**

- type：为空时返回新股新债信息，type="STOCK"时只返回新股申购信息，type="BOND"时只返回新债申购信息

**示例：**

 ```py
#coding:gbk
def init(ContextInfo):
    ipoData=get_ipo_data()# 返回新股新债信息
    ipoStock=get_ipo_data("STOCK")# 返回新股信息
    ipoCB=get_ipo_data("BOND")# 返回新债申购信息
```

### get\_new\_purchase\_limit-获取账户新股申购额度

**用法：** get\_new\_purchase\_limit(accid)

**释义：** 获取账户新股申购额度，返回结果为一个字典,包括上海主板,深圳市场,上海科创版的申购额度

**参数：**

- accid：资金账号，必须时股票账号或者信用账号

**示例：**

```
def init(ContextInfo):
    ContextInfo.accid="10000001"# 返回新股新债信息
    purchase_limit=get_new_purchase_limit(ContextInfo.accid)
```

### get\_value\_by\_order\_id-根据委托号获取委托或成交信息

**调用方法**`get_value_by_order_id(orderId, accountID, strAccountType, strDatatype)`

**参数**

| 参数名 | 类型 | 含义 | 说明 |
| --- | --- | --- | --- |
| orderId | string | 委托号 | 必填 |
| accountID | string | 资金账号 | 必填 |
| strAccountType | string | 账号类型 可选：<br>'FUTURE'：期货<br>'STOCK'：股票<br>'CREDIT'：信用<br>'HUGANGTONG'：沪港通<br>'SHENGANGTONG'：深港通<br>'STOCK\_OPTION'：期权 | 必填 |
| strDatatype | string | 要查询数据类型 可选：<br>'ORDER'：委托<br>'DEAL' ：成交 | 必填 |

**返回**

[委托对象](trading_function.html) 或 [成交对象](trading_function.md)

**示例**

python返回值

```
def init(ContextInfo):
    ContextInfo.accid = '6000000248'

def handlebar(ContextInfo):
    orderid = get_last_order_id(ContextInfo.accid, 'stock', 'order')
    print(orderid)
    obj = get_value_by_order_id(orderid,ContextInfo.accid, 'stock', 'order')
    print(obj.m_strInstrumentID)
```

```

【2023-10-31 13:20:51.440】  [quote]start simulation mode
【2023-10-31 13:20:51.464】  719000001
000001
```

### get\_last\_order\_id-获取最新的委托或成交的委托号

获取最新的委托或成交的委托号

提示

注意，下单后需要一段不确定的时间才能查询到此次委托的委托号，而且如果委托废单，则只能查询到上次成功下单的委托号

**调用方法**

python

```
# 区分策略，添加策略名称参数 strategyName
get_last_order_id(accountID, strAccountType, strDatatype, strategyName)

# 不区分策略
get_last_order_id(accountID, strAccountType, strDatatype)
```

**参数**

| 参数名 | 类型 | 含义 | 说明 |
| --- | --- | --- | --- |
| accountID | string | 资金账号 | 必填 |
| strAccountType | string | 账号类型 可选：<br>'FUTURE'：期货<br>'STOCK'：股票<br>'CREDIT'：信用<br>'HUGANGTONG'：沪港通<br>'SHENGANGTONG'：深港通<br>'STOCK\_OPTION'：期权 | 必填 |
| strDatatype | string | 要查询数据类型 可选：<br>'ORDER'：委托<br>'DEAL' ：成交 | 必填 |
| strategyName | string | 策略 当用passorder下单时指定了strategyName 参数时，当查询成交和委托时传入同样的strageName，则可以只返回包含strategyName的委托子集或成交子集 | 选填 |

**返回**

String，委托号，如果没找到返回 '-1'。

**示例**

```
def init(ContextInfo):
    ContextInfo.accid = '6000000248'

def handlebar(ContextInfo):
    orderid = get_last_order_id(ContextInfo.accid, 'stock', 'order')
    print(orderid)
    obj = get_value_by_order_id(orderid,ContextInfo.accid, 'stock', 'order')
    print(obj.m_strInstrumentID)
```

### get\_assure\_contract-获取两融担保标的明细

**用法：** get\_assure\_contract(accId)

**释义：** 获取信用账户担保合约明细

**参数：**

- accId：信用账户

**返回：** list，list 中放的是 [StkSubjects](data_structure.md#stkcompacts-%E8%B4%9F%E5%80%BA%E5%90%88%E7%BA%A6%E5%AF%B9%E8%B1%A1)，通过 dir(pythonobj) 可返回某个对象的属性列表。

**示例：**

python

```

def show_data(data):
    tdata = {}
    for ar in dir(data):
        if ar[:2] != 'm_':continue
        try:
            tdata[ar] = data.__getattribute__(ar)
        except:
            tdata[ar] = '<CanNotConvert>'
    return tdata

def handlebar(ContextInfo):
    obj = get_assure_contract('6000000248')
    for i in obj[:3]:
		print(show_data(i))

"""
{'m_dAssureRatio': 0.0, # 担保品折算比例
'm_dFinRatio': 0.8, # 融资保证金比例
'm_dSloRatio': 1.0,  # 融券保证金比例
'm_eAssureStatus': 50,  # 是否可做担保
'm_eCreditFundCtl': 50, # 融资交易控制
'm_eCreditStkCtl': 50, # 融券交易控制
'm_eFinStatus': 48, # 融资状态
'm_eSloStatus': 48, # 融券状态
'm_nPlatformID': 10064,  # 平台号
'm_strAccountID': '95000857',  # 资金账号
'm_strBrokerID': '003', # 经纪公司编号
'm_strBrokerName': '光大证券信用',  # 证券公司
'm_strExchangeID': 'SH', # 交易所
'm_strInstrumentID':'510150' # 证券代码
"""

```

### get\_enable\_short\_contract-获取可融券明细

提示

注:由于字段m\_dSloRatio、m\_dSloStatus提供来源和取担保品明细( [get\_assure\_contract](innerApi/trading_function.html#get-assure-contract-%E8%8E%B7%E5%8F%96%E4%B8%A4%E8%9E%8D%E6%8B%85%E4%BF%9D%E6%A0%87%E7%9A%84%E6%98%8E%E7%BB%86))重复，字段在2021年9月移除，后续用担保品明细接口获取,具体见 [担保标的对象字段说明](data_structure.md#stkcompacts-%E8%B4%9F%E5%80%BA%E5%90%88%E7%BA%A6%E5%AF%B9%E8%B1%A1)

**用法：** get\_enable\_short\_contract(accId)

**释义：** 获取信用账户当前可融券的明细

**参数：**

- accId：信用账户

**返回：** list，list 中放的是 [CreditSloEnableAmount](data_structure.md#creditsloenableamount-%E5%8F%AF%E8%9E%8D%E5%88%B8%E6%98%8E%E7%BB%86%E5%AF%B9%E8%B1%A1)，通过 dir(pythonobj) 可返回某个对象的属性列表。

**示例：**

python

```

def show_data(data):
    tdata = {}
    for ar in dir(data):
        if ar[:2] != 'm_':continue
        try:
            tdata[ar] = data.__getattribute__(ar)
        except:
            tdata[ar] = '<CanNotConvert>'
    return tdata

def handlebar(ContextInfo):
    obj = get_enable_short_contract('6000000248')
    for i in obj[:3]:
		print(show_data(i))

"""
Rerutn:

{'m_eQuerySloType': 48, # 查询类型
'm_nEnableAmount': 0,  # 融券可融数量
'm_nPlatformID': 10064,  # 平台号
'm_strAccountID': '95000857',  # 资金账号
'm_strBrokerID': '003',  # 经纪公司编号
'm_strBrokerName': '光大证券信用',  # 证券公司
'm_strExchangeID': 'SH', # 标的市场
'm_strInstrumentID': '688321' # 证券代码
}

"""
```

### query\_credit\_account - 查询信用账户明细

注意

1. 本函数一次最多查询200只股票的两融最大下单量，且同时只能有一个查询,如果前面的查询正在进行中,后面的查询将会提前返回。本函数从服务器查询数据,建议平均查询时间间隔180s一次,不可频繁调用。
2. 该函数必须配合credit\_account\_callback回调才能使用，关于此回调的说明请看 [credit\_account\_callback](callback_function.md?id=7zqjlm#credit-account-callback-%E6%9F%A5%E8%AF%A2%E4%BF%A1%E7%94%A8%E8%B4%A6%E6%88%B7%E6%98%8E%E7%BB%86%E5%9B%9E%E8%B0%83)
3. callback返回的对象是 [CCreditAccountDetail](data_structure.md?id=7zqjlm#ccreditaccountdetail-%E4%BF%A1%E7%94%A8%E8%B4%A6%E5%8F%B7%E5%AF%B9%E8%B1%A1-%E9%9D%9E%E6%9F%A5%E6%9F%9C%E5%8F%B0)

调用query\_credit\_account，该接口的查询结果将会推送给credit\_account\_callback，所以程序里需要按照函数参数实现函数`credit_account_callback`,callback返回的对象是 [CCreditAccountDetail](data_structure.md?id=7zqjlm#ccreditaccountdetail-%E4%BF%A1%E7%94%A8%E8%B4%A6%E5%8F%B7%E5%AF%B9%E8%B1%A1-%E9%9D%9E%E6%9F%A5%E6%9F%9C%E5%8F%B0)

**用法：** query\_credit\_account(accountId,seq,ContextInfo)

**释义：** 查询信用账户明细。本函数只能有一个查询，如果前面的查询正在进行中，后面的查询将会提前返回。

**参数：**

- accountId：string，查询的两融账号

- seq：int，查询序列号，建议输入唯一值以便对应结果回调


**示例：**

python返回值

 ```py
#coding:gbk

import time

def init(ContextInfo):
	ContextInfo.accid='200133'

def handlebar(ContextInfo):
	if ContextInfo.is_last_bar():
		query_credit_account(ContextInfo.accid,int(time.time()),ContextInfo)
# 该函数必须配合credit_account_callback回调才能使用
def credit_account_callback(ContextInfo,seq,result):
	print(seq)
	print(f":维持担保比例:{result.m_dPerAssurescaleValue:.2f},总负债:{result.m_dTotalDebt:.2f}")
```

```
{'m_dAssureAsset': 0.0, 'm_dAssureEnbuyBalance': 0.0, 'm_dAvailable': 0.0, 'm_dBalance': 0.0, 'm_dEnableBailBalance': 0.0, 'm_dFinDealAvl': 0.0, 'm_dFinDebt': 0.0, 'm_dFinEnableQuota': 0.0, 'm_dFinFee': 0.0, 'm_dFinMaxQuota': 0.0, 'm_dFinUsedQuota': 0.0, 'm_dFundValue': 1.7976931348623157e+308, 'm_dMarketValue': 0.0, 'm_dOtherFare': 0.0, 'm_dPerAssurescaleValue': 9999.0, 'm_dSloDebt': 0.0, 'm_dSloEnableQuota': 0.0, 'm_dSloFee': 0.0, 'm_dSloMarketValue': 0.0, 'm_dSloMaxQuota': 0.0, 'm_dSloSellBalance': 0.0, 'm_dSloUsedQuota': 0.0, 'm_dStockValue': 1.7976931348623157e+308, 'm_dSurplusSloSellBalance': 0.0, 'm_dTotalDebt': 0.0, 'm_dUsedSloSellBalance': 0.0, 'm_strAccountID': '800000857'}
```

**回调示例** 见 [query\_credit\_account](code_examples.md?id=7zqjlm#%E8%8E%B7%E5%8F%96%E4%B8%A4%E8%9E%8D%E8%B4%A6%E5%8F%B7%E4%BF%A1%E6%81%AF%E7%A4%BA%E4%BE%8B)

### query\_credit\_opvolume - 查询两融最大可下单量

注意

1. 本函数一次最多查询200只股票的两融最大下单量，且同时只能有一个查询,如果前面的查询正在进行中,后面的查询将会提前返回。本函数从服务器查询数据,建议平均查询时间间隔180s一次,不可频繁调用。
2. 该函数必须配合credit\_opvolume\_callback回调才能使用,关于此回调的说明请看 [credit\_account\_callback](callback_function.md?id=7zqjlm#credit-opvolume-callback-%E6%9F%A5%E8%AF%A2%E4%B8%A4%E8%9E%8D%E6%9C%80%E5%A4%A7%E5%8F%AF%E4%B8%8B%E5%8D%95%E9%87%8F%E7%9A%84%E5%9B%9E%E8%B0%83)

调用query\_credit\_opvolume，该接口的查询结果将会推送给credit\_opvolume\_callback，所以必须配合credit\_opvolume\_callback回调才能使用

**用法：** query\_credit\_opvolume(accountId,stockCode,opType,prType,price,seq,ContextInfo)

**释义：** 查询两融最大可下单量。

**参数：**

- `accountId`:查询的两融账号
- `stockCode`:需要查询的股票代码,stockCode为List的类型,可以查询多只股票
- `opType`:两融下单类型,同`passorder`的下单类型
- `prType`:报单价格类型,同`passorder`的报价类型
- `seq`:查询序列号,int型，建议输入唯一值以便对应结果回调
- `price`:报价(非限价单可以填任意值), **如果`stockCode`为`List`类型,报价也需要为长度相同的List**
- `ContextInfo`:ContextInfo类

**示例：**

python返回值

 ```py
#coding:gbk

import time

def init(ContextInfo):
	ContextInfo.accid='200133'

def handlebar(ContextInfo):
	if ContextInfo.is_last_bar():
        #查询accid账号担保品买入600000,SH限价10元的最大可下单量
		query_credit_opvolume(ContextInfo.accid,'600000.SH',33,11,10,int(time.time()),C) # 查询两融最大可下单量。
		time.sleep(0.5)
        #查询accid账号担保品买入600000,SH限价10元,000001.SZ担保品买入限价20元的最大可下单量
		query_credit_opvolume(ContextInfo.accid,["600000.SH","000001.SZ"],33,11,[10,20],int(time.time()),C) # 查询两融最大可下单量。

# 该函数必须配合credit_opvolume_callback回调才能使用
def credit_opvolume_callback(ContextInfo,accid,seq,ret,result):
	print(seq)
	print(f'查询结果:{ret}') # 正常返回:1,正在查询中-1,输入账号非法:-2,输入查询参数非法:-3,超时等服务器返回报错:-4
	print(result)
```

```
10
查询结果:1
{'000001.SZ': 0}
```

### get\_option\_subject\_position-取期权标的持仓

**用法：** get\_option\_subject\_position(accountID)

**释义：** 取期权标的持仓

**参数：**

- accountID：string,账号

**返回：** list,list中放的是 [CLockPosition](data_structure.md?id=7zqjlm#clockposition-%E6%9C%9F%E6%9D%83%E6%A0%87%E7%9A%84%E6%8C%81%E4%BB%93),通过dir(pythonobj)可返回某个对象的属性列表

**示例：**

```
data=get_option_subject_position('880399990383')
print(len(data));
forobjindata:
    print(obj.m_strInstrumentName,obj.m_lockVol,obj.m_coveredVol);
```

### get\_comb\_option-取期权组合持仓

**用法：** get\_comb\_option(accountID)

**释义：** 取期权组合持仓

**参数：**

- accountID：string,账号

**返回：** list,list中放的是 [CStkOptCombPositionDetail ](data_structure.md?id=7zqjlm#cstkoptcombpositiondetail-%E6%9C%9F%E6%9D%83%E7%BB%84%E5%90%88%E6%8C%81%E4%BB%93),通过dir(pythonobj)可返回某个对象的属性列表

**示例：**

```
obj_list=get_comb_option('880399990383')
print(len(obj_list));
forobjinobj_list:
    print(obj.m_strCombCodeName,obj.m_strCombID,obj.m_nVolume,obj.m_nFrozenVolume)
```

### get\_unclosed\_compacts-获取未了结负债合约明细

**用法：** get\_unclosed\_compacts(accountID,accountType)

**释义：** 获取未了结负债合约明细

**参数：**

- accountID：str，资金账号
- accountType：str，账号类型，这里应该填'CREDIT'

**返回：**

list(\[ CStkUnclosedCompacts, ... \]) 负债列表，CStkUnclosedCompacts属性如下：

| 字段名称 | 类型 | 说明 |
| --- | --- | --- |
| `m_strAccountID` | string | 账号ID |
| `m_nBrokerType` | int | 账号类型<br>1-期货账号<br>2-股票账号<br>3-信用账号<br>5-期货期权账号<br>6-股票期权账号<br>7-沪港通账号<br>11-深港通账号 |
| `m_strExchangeID` | string | 市场 |
| `m_strInstrumentID` | string | 证券代码 |
| `m_eCompactType` | int | 合约类型<br>32-不限制<br>48-融资<br>49-融券 |
| `m_eCashgroupProp` | int | 头寸来源<br>32-不限制<br>48-普通头寸<br>49-专项头寸 |
| `m_nOpenDate` | int | 开仓日期(如'20201231') |
| `m_nBusinessVol` | int | 合约证券数量 |
| `m_nRealCompactVol` | int | 未还合约数量 |
| `m_nRetEndDate` | int | 到期日(如'20201231') |
| `m_dBusinessBalance` | float | 合约金额 |
| `m_dBusinessFare` | float | 合约息费 |
| `m_dRealCompactBalance` | float | 未还合约金额 |
| `m_dRealCompactFare` | float | 未还合约息费 |
| `m_dRepaidFare` | float | 已还息费 |
| `m_dRepaidBalance` | float | 已还金额 |
| `m_strCompactId` | string | 合约编号 |
| `m_strEntrustNo` | string | 委托编号 |
| `m_nRepayPriority` | int | 偿还优先级 |
| `m_strPositionStr` | string | 定位串 |
| `m_eCompactRenewalStatus` | int | 合约展期状态<br>48-可申请<br>49-已申请<br>50-审批通过<br>51-审批不通过<br>52-不可申请<br>53-已执行<br>54-已取消 |
| `m_nDeferTimes` | int | 展期次数 |

**示例：**

```
get_unclosed_compacts('6000000248', 'CREDIT')
```

### get\_closed\_compacts-获取已了结负债合约明细

**用法：** get\_closed\_compacts(accountID,accountType)

**释义：** 获取已了结负债合约明细

**参数：**

- accountID：str，资金账号
- accountType：str，账号类型，这里应该填'CREDIT'

**返回：**

list(\[ CStkUnclosedCompacts, ... \]) 负债列表，CStkUnclosedCompacts属性如下：

| 字段名 | 类型 | 描述 |
| --- | --- | --- |
| `m_strAccountID` | string | 账号ID |
| `m_nBrokerType` | int | 账号类型<br>1-期货账号<br>2-股票账号<br>3-信用账号<br>5-期货期权账号<br>6-股票期权账号<br>7-沪港通账号<br>11-深港通账号 |
| `m_strExchangeID` | string | 市场 |
| `m_strInstrumentID` | string | 证券代码 |
| `m_eCompactType` | int | 合约类型<br>32-不限制<br>48-融资<br>49-融券 |
| `m_eCashgroupProp` | int | 头寸来源<br>32-不限制<br>48-普通头寸<br>49-专项头寸 |
| `m_nOpenDate` | int | 开仓日期(如'20201231') |
| `m_nBusinessVol` | int | 合约证券数量 |
| `m_nRetEndDate` | int | 到期日(如'20201231') |
| `m_nDateClear` | int | 了结日期(如'20201231') |
| `m_nEntrustVol` | int | 委托数量 |
| `m_dEntrustBalance` | float | 委托金额 |
| `m_dBusinessBalance` | float | 合约金额 |
| `m_dBusinessFare` | float | 合约息费 |
| `m_dRepaidFare` | float | 已还息费 |
| `m_dRepaidBalance` | float | 已还金额 |
| `m_strCompactId` | string | 合约编号 |
| `m_strEntrustNo` | string | 委托编号 |
| `m_strPositionStr` | string | 定位串 |

**示例：**

```
get_closed_compacts('6000000248', 'CREDIT')
```

## 其他交易函数（仅回测可用）

警告

以下函数仅回测生效，实盘和模拟盘交易均不可用

### order\_lots-指定手数交易

**用法：** order\_lots(stockcode, lots\[, style, price\], ContextInfo\[, accId\])

**释义：** 指定手数交易，指定手数发送买/卖单。如有需要落单类型当做一个参量传入，如果忽略掉落单类型，那么默认以最新价下单。

**参数：**

- stockcode：代码，string，如 '000002.SZ'

- lots：手数，int

- style：下单选价类型，string，默认为最新价 'LATEST'，可选值：


> 'LATEST'：最新
>
> 'FIX'：指定 选此参数时必须指定有效的`price`参数，其他style值可不用传入price参数
>
> 'HANG'：挂单 用己方盘口挂单，即买入时用盘口买一价下单，卖出时用卖一价挂单，
>
> 'COMPETE'：对手
>
> 'MARKET'：市价
>
> 'SALE5', 'SALE4', 'SALE3', 'SALE2', 'SALE1'：卖5-1价
>
> 'BUY1', 'BUY2', 'BUY3', 'BUY4', 'BUY5'：买1-5价

- price：价格，double

- ContextInfo：PythonObj，Python 对象，这里必须是 ContextInfo

- accId：账号，string


**返回：** 无

**示例：**

```
def handlebar(ContextInfo):
    # 按最新价下 1 手买入
    order_lots('000002.SZ', 1, ContextInfo, '600000248')

    # 用对手价下 1 手卖出
    order_lots('000002.SZ', -1, 'COMPETE', ContextInfo, '600000248')

    # 用指定价 37.5 下 2 手卖出
    order_lots('000002.SZ', -2, 'fix', 37.5, ContextInfo, '600000248')
```

### order\_value-指定价值交易

**用法：** order\_value(stockcode, value\[, style, price\], ContextInfo\[, accId\])

**释义：** 指定价值交易，使用想要花费的金钱买入 / 卖出股票，而不是买入 / 卖出想要的股数，正数代表买入，负数代表卖出。股票的股数总是会被调整成对应的 100 的倍数（在中国 A 股市场 1 手是 100 股）。当您提交一个卖单时，该方法代表的意义是您希望通过卖出该股票套现的金额，如果金额超出了您所持有股票的价值，那么您将卖出所有股票。需要注意，如果资金不足，该 API 将不会创建发送订单。

**参数：**

- stockcode：代码，string，如 '000002.SZ'

- value：金额（元），double

- style：下单选价类型，string，默认为最新价 'LATEST'，可选值：


> 'LATEST'：最新
>
> 'FIX'：指定
>
> 'HANG'：挂单
>
> 'COMPETE'：对手
>
> 'MARKET'：市价
>
> 'SALE5', 'SALE4', 'SALE3', 'SALE2', 'SALE1'：卖5-1价
>
> 'BUY1', 'BUY2', 'BUY3', 'BUY4', 'BUY5'：买1-5价

- price：价格，double

- ContextInfo：PythonObj，Python 对象，这里必须是 ContextInfo

- accId：账号，string


**返回：** 无

**示例：**

```
def handlebar(ContextInfo):
    # 按最新价下 10000 元买入
    order_value('000002.SZ', 10000, ContextInfo, '600000248')

    # 用对手价下 10000 元卖出
    order_value('000002.SZ', -10000, 'COMPETE', ContextInfo, '600000248')

    # 用指定价 37.5 下 20000 元卖出
    order_value('000002.SZ', -20000, 'fix', 37.5, ContextInfo, '600000248')
```

### order\_percent-指定比例交易

**用法：** order\_percent(stockcode, percent\[, style, price\], ContextInfo\[, accId\])

**释义：** 指定比例交易，发送一个等于目前投资组合价值（市场价值和目前现金的总和）一定百分比的买 / 卖单，正数代表买，负数代表卖。股票的股数总是会被调整成对应的一手的股票数的倍数（1 手是 100 股）。百分比是一个小数，并且小于或等于1（小于等于100%），0.5 表示的是 50%。需要注意，如果资金不足，该 API 将不会创建发送订单。

**参数：**

- stockcode：代码，string，如 '000002.SZ'

- percent：比例，double

- style：下单选价类型，string，默认为最新价 'LATEST'，可选值：


> 'LATEST'：最新
>
> 'FIX'：指定
>
> 'HANG'：挂单
>
> 'COMPETE'：对手
>
> 'MARKET'：市价
>
> 'SALE5', 'SALE4', 'SALE3', 'SALE2', 'SALE1'：卖5-1价
>
> 'BUY1', 'BUY2', 'BUY3', 'BUY4', 'BUY5'：买1-5价

- price：价格，double

- ContextInfo：PythonObj，Python 对象，这里必须是 ContextInfo

- accId：账号，string


**返回：** 无

**示例：**

```
def handlebar(ContextInfo):
    # 按最新价下 5.1% 价值买入
    order_percent('000002.SZ', 0.051, ContextInfo, '600000248')

    # 用对手价下 5.1% 价值卖出
    order_percent('000002.SZ', -0.051, 'COMPETE', ContextInfo, '600000248')

    # 用指定价 37.5 下 10.2% 价值卖出
    order_percent('000002.SZ', -0.102, 'fix', 37.5, ContextInfo, '600000248')
```

### order\_target\_value-指定目标价值交易

**用法：** order\_target\_value(stockcode, tar\_value\[, style, price\], ContextInfo\[, accId\])

**释义：** 指定目标价值交易，买入 / 卖出并且自动调整该证券的仓位到一个目标价值。如果还没有任何该证券的仓位，那么会买入全部目标价值的证券；如果已经有了该证券的仓位，则会买入 / 卖出调整该证券的现在仓位和目标仓位的价值差值的数目的证券。需要注意，如果资金不足，该API将不会创建发送订单。

**参数：**

- stockcode：代码，string，如 '000002.SZ'

- tar\_value：目标金额（元），double，非负数

- style：下单选价类型，string，默认为最新价 'LATEST'，可选值：


> 'LATEST'：最新
>
> 'FIX'：指定
>
> 'HANG'：挂单
>
> 'COMPETE'：对手
>
> 'MARKET'：市价
>
> 'SALE5', 'SALE4', 'SALE3', 'SALE2', 'SALE1'：卖5-1价
>
> 'BUY1', 'BUY2', 'BUY3', 'BUY4', 'BUY5'：买1-5价

- price：价格，double

- ContextInfo：PythonObj，Python 对象，这里必须是 ContextInfo

- accId：账号，string


**返回：** 无

**示例：**

```
def handlebar(ContextInfo):
    # 按最新价下调仓到 10000 元持仓
    order_target_value('000002.SZ', 10000, ContextInfo, '600000248')

    # 用对手价调仓到 10000 元持仓
    order_target_value('000002.SZ', 10000, 'COMPETE', ContextInfo, '600000248')

    # 用指定价 37.5 下调仓到 20000 元持仓
    order_target_value('000002.SZ', 20000, 'fix', 37.5, ContextInfo, '600000248')
```

### order\_target\_percent-指定目标比例交易

**用法：** order\_target\_percent(stockcode, tar\_percent\[, style, price\], ContextInfo\[, accId\])

**释义：** 指定目标比例交易，买入 / 卖出证券以自动调整该证券的仓位到占有一个指定的投资组合的目标百分比。投资组合价值等于所有已有仓位的价值和剩余现金的总和。买 / 卖单会被下舍入一手股数（A 股是 100 的倍数）的倍数。目标百分比应该是一个小数，并且最大值应该小于等于1，比如 0.5 表示 50%，需要注意，如果资金不足，该API将不会创建发送订单。

**参数：**

- stockcode：代码，string，如 '000002.SZ'

- tar\_percent：目标百分比 \[0 ~ 1\]，double

- style：下单选价类型，string，默认为最新价 'LATEST'，可选值：


> 'LATEST'：最新
>
> 'FIX'：指定
>
> 'HANG'：挂单
>
> 'COMPETE'：对手
>
> 'MARKET'：市价
>
> 'SALE5', 'SALE4', 'SALE3', 'SALE2', 'SALE1'：卖5-1价
>
> 'BUY1', 'BUY2', 'BUY3', 'BUY4', 'BUY5'：买1-5价

- price：价格，double

- ContextInfo：PythonObj，Python 对象，这里必须是 ContextInfo

- accId：账号，string


**返回：** 无

**示例：**

```
def handlebar(ContextInfo):
    # 按最新价下买入调仓到 5.1% 持仓
    order_target_percent('000002.SZ', 0.051, ContextInfo, '600000248')

    # 用对手价调仓到 5.1% 持仓
    order_target_percent('000002.SZ', 0.051, 'COMPETE', ContextInfo, '600000248')

    # 用指定价 37.5 调仓到 10.2% 持仓
    order_target_percent('000002.SZ', 0.102, 'fix', 37.5, ContextInfo, '600000248')
```

### order\_shares-指定股数交易

**用法：** order\_shares(stockcode, shares\[, style, price\], ContextInfo\[, accId\])

**释义：** 指定股数交易，指定股数的买 / 卖单,最常见的落单方式之一。如有需要落单类型当做一个参量传入，如果忽略掉落单类型，那么默认以最新价下单。

**参数：**

- stockcode：代码，string，如 '000002.SZ'

- shares：股数，int

- style：下单选价类型，string，默认为最新价 'LATEST'，可选值：


> 'LATEST'：最新
>
> 'FIX'：指定
>
> 'HANG'：挂单
>
> 'COMPETE'：对手
>
> 'MARKET'：市价
>
> 'SALE5', 'SALE4', 'SALE3', 'SALE2', 'SALE1'：卖5-1价
>
> 'BUY1', 'BUY2', 'BUY3', 'BUY4', 'BUY5'：买1-5价

- price：价格，double

- ContextInfo：PythonObj，Python 对象，这里必须是 ContextInfo

- accId：账号，string


**返回：** 无

**示例：**

```
def handlebar(ContextInfo):
    # 按最新价下 100 股买入
    order_shares('000002.SZ', 100, ContextInfo, '600000248')

    # 用对手价下 100 股卖出
    order_shares('000002.SZ', -100, 'COMPETE', ContextInfo, '600000248')

    # 用指定价 37.5 下 200 股卖出
    order_shares('000002.SZ', -200, 'fix', 37.5, ContextInfo, '600000248')
```

### buy\_open-期货买入开仓

**用法：** buy\_open(stockcode, amount\[, style, price\], ContextInfo\[, accId\])

**释义：** 期货买入开仓

**参数：**

- stockcode：代码，string，如 'IF1805.IF'

- amount：手数，int

- style：下单选价类型，string，默认为最新价 'LATEST'，可选值：


> 'LATEST'：最新
>
> 'FIX'：指定
>
> 'HANG'：挂单
>
> 'COMPETE'：对手
>
> 'MARKET'：市价
>
> 'SALE1'：卖一价
>
> 'BUY1'：买一价

- price：价格，double

- ContextInfo：PythonObj，Python 对象，这里必须是 ContextInfo

- accId：账号，string


**返回：** 无

**示例：**

```
def handlebar(ContextInfo):
    # 按最新价 1 手买入开仓
    buy_open('IF1805.IF', 1, ContextInfo, '110476')

    # 用对手价 1 手买入开仓
    buy_open('IF1805.IF', 1, 'COMPETE', ContextInfo, '110476')

    # 用指定价 3750 元 2 手买入开仓
    buy_open('IF1805.IF', 2, 'fix', 3750, ContextInfo, '110476')
```

### buy\_close\_tdayfirst-期货买入平仓（平今优先）

**用法：** buy\_close\_tdayfirst(stockcode, amount\[, style, price\], ContextInfo\[, accId\])

**释义：** 期货买入平仓，平今优先

**参数：**

- stockcode：代码，string，如 'IF1805.IF'

- amount：手数，int

- style：下单选价类型，string，默认为最新价 'LATEST'，可选值：


> 'LATEST'：最新
>
> 'FIX'：指定
>
> 'HANG'：挂单
>
> 'COMPETE'：对手
>
> 'MARKET'：市价
>
> 'SALE1'：卖一价
>
> 'BUY1'：买一价

- price：价格，double

- ContextInfo：PythonObj，Python 对象，这里必须是 ContextInfo

- accId：账号，string


**返回：** 无

**示例：**

```
def handlebar(ContextInfo):
    # 按最新价 1 手买入平仓，平今优先
    buy_close_tdayfirst('IF1805.IF', 1, ContextInfo, '110476')

    # 用对手价 1 手买入平仓，平今优先
    buy_close_tdayfirst('IF1805.IF', 1, 'COMPETE', ContextInfo, '110476')

    # 用指定价 3750 元 2 手买入平仓，平今优先
    buy_close_tdayfirst('IF1805.IF', 2, 'fix', 3750, ContextInfo, '110476')
```

### buy\_close\_ydayfirst-期货买入平仓（平昨优先）

**用法：** buy\_close\_ydayfirst(stockcode, amount\[, style, price\], ContextInfo\[, accId\])

**释义：** 期货买入开仓，平昨优先

**参数：**

- stockcode：代码，string，如 'IF1805.IF'

- amount：手数，int

- style：下单选价类型，string，默认为最新价 'LATEST'，可选值：


> 'LATEST'：最新
>
> 'FIX'：指定
>
> 'HANG'：挂单
>
> 'COMPETE'：对手
>
> 'MARKET'：市价
>
> 'SALE1'：卖一价
>
> 'BUY1'：买一价

- price：价格，double

- ContextInfo：PythonObj，Python 对象，这里必须是 ContextInfo

- accId：账号，string


**返回：** 无

**示例：**

```
def handlebar(ContextInfo):
    # 按最新价 1 手买入平仓，平昨优先
    buy_close_ydayfirst('IF1805.IF', 1, ContextInfo, '110476')

    # 用对手价 1 手买入平仓，平昨优先
    buy_close_ydayfirst('IF1805.IF', 1, 'COMPETE', ContextInfo, '110476')

    # 用指定价 3750 元 2 手买入平仓，平昨优先
    buy_close_ydayfirst('IF1805.IF', 2, 'fix', 3750, ContextInfo, '110476')
```

### sell\_open-期货卖出开仓

**用法：** sell\_open(stockcode, amount\[, style, price\], ContextInfo\[, accId\])

**释义：** 期货卖出开仓

**参数：**

- stockcode：代码，string，如 'IF1805.IF'

- amount：手数，int

- style：下单选价类型，string，默认为最新价 'LATEST'，可选值：


> 'LATEST'：最新
>
> 'FIX'：指定
>
> 'HANG'：挂单
>
> 'COMPETE'：对手
>
> 'MARKET'：市价
>
> 'SALE1'：卖一价
>
> 'BUY1'：买一价

- price：价格，double

- ContextInfo：PythonObj，Python 对象，这里必须是 ContextInfo

- accId：账号，string


**返回：** 无

**示例：**

```
def handlebar(ContextInfo):
    # 按最新价 1 手卖出开仓
    sell_open('IF1805.IF', 1, ContextInfo, '110476')

    # 用对手价 1 手卖出开仓
    sell_open('IF1805.IF', 1, 'COMPETE', ContextInfo, '110476')

    # 用指定价 3750 元 2 手卖出开仓
    sell_open('IF1805.IF', 2, 'fix',3750, ContextInfo, '110476')
```

### sell\_close\_tdayfirst-期货卖出平仓（平今优先）

**用法：** sell\_close\_tdayfirst(stockcode, amount\[, style, price\], ContextInfo\[, accId\])

**释义：** 期货卖出平仓，平今优先

**参数：**

- stockcode：代码，string，如 'IF1805.IF'

- amount：手数，int

- style：下单选价类型，string，默认为最新价 'LATEST'，可选值：


> 'LATEST'：最新
>
> 'FIX'：指定
>
> 'HANG'：挂单
>
> 'COMPETE'：对手
>
> 'MARKET'：市价
>
> 'SALE1'：卖一价
>
> 'BUY1'：买一价

- price：价格，double

- ContextInfo：PythonObj，Python 对象，这里必须是 ContextInfo

- accId：账号，string


**返回：** 无

**示例：**

```
def handlebar(ContextInfo):
    # 按最新价下 1 手卖出平仓，平今优先
    sell_close_tdayfirst('IF1805.IF', 1, ContextInfo, '110476')

    # 用对手价 1 手卖出平仓，平今优先
    sell_close_tdayfirst('IF1805.IF', 1, 'COMPETE', ContextInfo, '110476')

    # 用指定价 3750 元 2 手卖出平仓，平今优先
    sell_close_tdayfirst('IF1805.IF', 1, 'fix', 3750, ContextInfo, '110476')
```

### sell\_close\_ydayfirst-期货卖出平仓（平昨优先）

**用法：** sell\_close\_ydayfirst(stockcode, amount\[, style, price\], ContextInfo\[, accId\])

**释义：** 期货卖出平仓，平昨优先

**参数：**

- stockcode：代码，string，如 'IF1805.IF'

- amount：手数，int

- style：下单选价类型，string，默认为最新价 'LATEST'，可选值：


> 'LATEST'：最新
>
> 'FIX'：指定
>
> 'HANG'：挂单
>
> 'COMPETE'：对手
>
> 'MARKET'：市价
>
> 'SALE1'：卖一价
>
> 'BUY1'：买一价

- price：价格，double

- ContextInfo：PythonObj，Python 对象，这里必须是 ContextInfo

- accId：账号，string


**返回：** 无

**示例：**

```
def handlebar(ContextInfo):
    # 按最新价 1 手卖出平仓，平昨优先
    sell_close_ydayfirst('IF1805.IF', 1, ContextInfo, '110476')

    # 用对手价 1 手卖出平仓，平昨优先
    sell_close_ydayfirst('IF1805.IF', 1, 'COMPETE', ContextInfo, '110476')

    # 用指定价 3750 元 2 手卖出平仓，平昨优先
    sell_close_ydayfirst('IF1805.IF', 2, 'fix', 3750, ContextInfo, '110476')
```

### \[已弃用\] get\_debt\_contract-获取两融负债合约明细

**用法：** get\_debt\_contract(accId)

**释义：** 获取信用账户负债合约明细

此接口已弃用，替代接口为get\_unclosed\_compacts（获取未了结负债）和get\_closed\_compacts（获取已了结负债）

**参数：**

- accId：信用账户

**返回：** list，list 中放的是 [PythonObj](https://dict.thinktrader.net/pages/e148c4/#_5-3-7-stkcompacts%E8%B4%9F%E5%80%BA%E5%90%88%E7%BA%A6%E5%AF%B9%E8%B1%A1)，通过 dir(pythonobj) 可返回某个对象的属性列表。

**示例：**

```
def handlebar(ContextInfo):
    obj_list = get_debt_contract('6000000248')
    for obj in obj_list:
        # 输出负债合约名
        print(obj.m_strInstrumentName)
```

### get\_hkt\_exchange\_rate-获取沪深港通汇率数据

**用法：** get\_hkt\_exchange\_rate(accountID,accountType)

**释义：** 获取沪深港通汇率数据

**参数：**

- accountID：string,账号；
- accountType:string,账号类型,必须填HUGANGTONG或者SHENGANGTONG

**返回：**

> dict,字段释义：
>
> bidReferenceRate:买入参考汇率
>
> askReferenceRate:卖出参考汇率
>
> dayBuyRiseRate:日间买入参考汇率浮动比例
>
> daySaleRiseRate:日间卖出参考汇率浮动比例

**示例：**

```
def init(ContextInfo):
      data=get_hkt_exchange_rate('6000000248','HUGANGTONG')
      print(data)
```