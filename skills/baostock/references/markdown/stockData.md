## A股K线数据


### 获取历史A股K线数据：query_history_k_data_plus()

方法说明：通过API接口获取A股历史交易数据，可以通过参数设置获取日k线、周k线、月k线，以及5分钟、15分钟、30分钟和60分钟k线数据，适合搭配均线数据进行选股和分析。

返回类型：pandas的DataFrame类型。

能获取1990-12-19至当前时间的数据；

可查询不复权、**前复权**、**后复权**数据。

示例数据：[下载](https://www.baostock.com/helpdocs/csv/history_A_stock_k_data.xlsx)

日线使用示例：

```python

    import baostock as bs
    import pandas as pd

    #### 登陆系统 ####
    lg = bs.login()
    # 显示登陆返回信息
    print('login respond error_code:'+lg.error_code)
    print('login respond  error_msg:'+lg.error_msg)

    #### 获取沪深A股历史K线数据 ####
    # 详细指标参数，参见“历史行情指标参数”章节；“分钟线”参数与“日线”参数不同。“分钟线”不包含指数。
    # 分钟线指标：date,time,code,open,high,low,close,volume,amount,adjustflag
    # 周月线指标：date,code,open,high,low,close,volume,amount,adjustflag,turn,pctChg
    rs = bs.query_history_k_data_plus("sh.600000",
        "date,code,open,high,low,close,preclose,volume,amount,adjustflag,turn,tradestatus,pctChg,isST",
        start_date='2024-07-01', end_date='2024-12-31',
        frequency="d", adjustflag="3")
    print('query_history_k_data_plus respond error_code:'+rs.error_code)
    print('query_history_k_data_plus respond  error_msg:'+rs.error_msg)

    #### 打印结果集 ####
    data_list = []
    while (rs.error_code == '0') & rs.next():
        # 获取一条记录，将记录合并在一起
        data_list.append(rs.get_row_data())
    result = pd.DataFrame(data_list, columns=rs.fields)

    #### 结果集输出到csv文件 ####
    result.to_csv("D:\\history_A_stock_k_data.csv", index=False)
    print(result)

    #### 登出系统 ####
    bs.logout()

```


分钟线使用示例：

```python

    import baostock as bs
    import pandas as pd

    #### 登陆系统 ####
    lg = bs.login()
    # 显示登陆返回信息
    print('login respond error_code:'+lg.error_code)
    print('login respond  error_msg:'+lg.error_msg)

    #### 获取沪深A股历史K线数据 ####
    # 详细指标参数，参见“历史行情指标参数”章节；“分钟线”参数与“日线”参数不同。“分钟线”不包含指数。
    # 分钟线指标：date,time,code,open,high,low,close,volume,amount,adjustflag
    # 周月线指标：date,code,open,high,low,close,volume,amount,adjustflag,turn,pctChg
    rs = bs.query_history_k_data_plus("sh.600000",
        "date,time,code,open,high,low,close,volume,amount,adjustflag",
        start_date='2024-07-01', end_date='2024-12-31',
        frequency="5", adjustflag="3")
    print('query_history_k_data_plus respond error_code:'+rs.error_code)
    print('query_history_k_data_plus respond  error_msg:'+rs.error_msg)

    #### 打印结果集 ####
    data_list = []
    while (rs.error_code == '0') & rs.next():
        # 获取一条记录，将记录合并在一起
        data_list.append(rs.get_row_data())
    result = pd.DataFrame(data_list, columns=rs.fields)

    #### 结果集输出到csv文件 ####
    result.to_csv("D:\\history_A_stock_k_data.csv", index=False)
    print(result)

    #### 登出系统 ####
    bs.logout()

```


参数含义：

* code：股票代码，sh或sz.+6位数字代码，或者指数代码，如：sh.601398。sh：上海；sz：深圳。此参数不可为空；
* fields：指示简称，支持多指标输入，以半角逗号分隔，填写内容作为返回类型的列。**详细指标列表见历史行情指标参数章节，日线与分钟线参数不同**。此参数不可为空；
* start：开始日期（包含），格式“YYYY-MM-DD”，为空时取2015-01-01；
* end：结束日期（包含），格式“YYYY-MM-DD”，为空时取最近一个交易日；
* frequency：数据类型，默认为d，日k线；d=日k线、w=周、m=月、5=5分钟、15=15分钟、30=30分钟、60=60分钟k线数据，不区分大小写；指数没有分钟线数据；周线每周最后一个交易日才可以获取，月线每月最后一个交易日才可以获取。
* adjustflag：**复权类型，默认不复权：3；1：后复权；2：前复权。已支持分钟线、日线、周线、月线前后复权。** BaoStock提供的是**涨跌幅复权算法**复权因子，具体介绍见[BaoStock复权因子简介](https://www.baostock.com/helpdocs/pdf/BaoStock%E5%A4%8D%E6%9D%83%E5%9B%A0%E5%AD%90%E7%AE%80%E4%BB%8B.pdf "BaoStock复权因子简介.pdf")。



**注意：**

* 股票停牌时，对于日线，开、高、低、收价都相同，且都为前一交易日的收盘价，成交量、成交额为0，换手率为空。

如果需要将换手率转为float类型，可使用如下方法转换：result["turn"] = [0 if x == "" else float(x) for x in result["turn"]]



**关于复权数据的说明：**

BaoStock使用“涨跌幅复权法”进行复权，详细说明参考上文“复权因子简介”。不同系统间采用复权方式可能不一致，导致数据不一致。

“涨跌幅复权法的”优点：可以计算出资金收益率，确保初始投入的资金运用率为100%，既不会因为分红而导致投资减少，也不会因为配股导致投资增加。


与同花顺、通达信等存在不同。


返回示例数据

| date | code | open | high | low | close | preclose | volume | amount | adjustflag | turn | tradestatus | pctChg | isST |
|------------|------------|-------|------------|------------|-------|------------|------------|-------|------------|-------|------------|------------|-------|
| 2017-07-03 | sh.600000 | 12.64 | 12.65 | 12.47 | 12.56 | 12.65 | 38778949 | 486264672 | 3 | 0.137985 | 1 | —0.711456 | 0 |
| 2017-07-04 | sh.600000 | 12.55 | 12.58 | 12.41 | 12.55 | 12.56 | 36659128 | 458434432 | 3 | 0.130442 | 1 | —0.07962 | 0 |
| 2017-07-05 | sh.600000 | 12.5 | 12.65 | 12.47 | 12.62 | 12.55 | 26470507 | 332542464 | 3 | 0.094188 | 1 | 0.557767 | 0 |
| 2017-07-06 | sh.600000 | 12.62 | 12.72 | 12.51 | 12.66 | 12.62 | 37414241 | 471582096 | 3 | 0.133129 | 1 | 0.316957 | 0 |
| 2017-07-07 | sh.600000 | 12.62 | 12.69 | 12.55 | 12.6 | 12.66 | 24667294 | 311101536 | 3 | 0.087772 | 1 | —0.473929 | 0 |

返回数据说明

| 参数名称 | 参数描述 | 算法说明 |
|------------|------------|-------|
| date | 交易所行情日期 |  |
| code | 证券代码 |  |
| open | 开盘价 |  |
| high | 最高价 |  |
| low | 最低价 |  |
| close | 收盘价 |  |
| preclose | 前收盘价 | 见表格下方详细说明 |
| volume | 成交量（累计 单位：股） |  |
| amount | 成交额（单位：人民币元） |  |
| adjustflag | 复权状态(1：后复权， 2：前复权，3：不复权） |  |
| turn | 换手率 | [指定交易日的成交量(股)/指定交易日的股票的流通股总股数(股)]\*100% |
| tradestatus | 交易状态(1：正常交易 0：停牌） |  |
| pctChg | 涨跌幅（百分比） | 日涨跌幅=[(指定交易日的收盘价-指定交易日前收盘价)/指定交易日前收盘价]\*100% |
| peTTM | 滚动市盈率 | (指定交易日的股票收盘价/指定交易日的每股盈余TTM)=(指定交易日的股票收盘价\*截至当日公司总股本)/归属母公司股东净利润TTM |
| pbMRQ | 市净率 | (指定交易日的股票收盘价/指定交易日的每股净资产)=总市值/(最近披露的归属母公司股东的权益-其他权益工具) |
| psTTM | 滚动市销率 | (指定交易日的股票收盘价/指定交易日的每股销售额)=(指定交易日的股票收盘价\*截至当日公司总股本)/营业总收入TTM |
| pcfNcfTTM | 滚动市现率 | (指定交易日的股票收盘价/指定交易日的每股现金流TTM)=(指定交易日的股票收盘价\*截至当日公司总股本)/现金以及现金等价物净增加额TTM |
| isST | 是否ST股，1是，0否 |  |



**注意“前收盘价”说明**：


证券在指定交易日行情数据的前收盘价，当日发生除权除息时，“前收盘价”不是前一天的实际收盘价，而是根据股权登记日收盘价与分红现金的数量、配送股的数里和配股价的高低等结合起来算出来的价格。


具体计算方法如下:


1、计算除息价:


除息价=股息登记日的收盘价-每股所分红利现金额


2、计算除权价:


送红股后的除权价=股权登记日的收盘价/(1+每股送红股数)

配股后的除权价=(股权登记日的收盘价+配股价\*每股配股数)/(1+每股配股数)


3、计算除权除息价


除权除息价=(股权登记日的收盘价-每股所分红利现金额+配股价\*每股配股数)/(1+每股送红股数+每股配股数)

“前收盘价”由交易所计算并公布。首发日的“前收盘价”等于“首发价格”。


### 历史行情指标参数


日线指标参数（包含停牌证券）

| 参数名称 | 参数描述 | 说明 |
|------------|------------|-------|
| date | 交易所行情日期 | 格式：YYYY-MM-DD |
| code | 证券代码 | 格式：sh.600000。sh：上海，sz：深圳 |
| open | 今开盘价格 | 精度：小数点后4位；单位：人民币元 |
| high | 最高价 | 精度：小数点后4位；单位：人民币元 |
| low | 最低价 | 精度：小数点后4位；单位：人民币元 |
| close | 今收盘价 | 精度：小数点后4位；单位：人民币元 |
| preclose | 昨日收盘价 | 精度：小数点后4位；单位：人民币元 |
| volume | 成交数量 | 单位：股 |
| amount | 成交金额 | 精度：小数点后4位；单位：人民币元 |
| adjustflag | 复权状态 | 不复权、前复权、后复权 |
| turn | 换手率 | 精度：小数点后6位；单位：% |
| tradestatus | 交易状态 | 1：正常交易 0：停牌 |
| pctChg | 涨跌幅（百分比） | 精度：小数点后6位 |
| peTTM | 滚动市盈率 | 精度：小数点后6位 |
| psTTM | 滚动市销率 | 精度：小数点后6位 |
| pcfNcfTTM | 滚动市现率 | 精度：小数点后6位 |
| pbMRQ | 市净率 | 精度：小数点后6位 |
| isST | 是否ST | 1是，0否 |

周、月线指标参数

| 参数名称 | 参数描述 | 说明 | 算法说明 |
|------------|------------|-------|-------|
| date | 交易所行情日期 | 格式：YYYY-MM-DD |  |
| code | 证券代码 | 格式：sh.600000。sh：上海，sz：深圳 |  |
| open | 开盘价格 | 精度：小数点后4位；单位：人民币元 |  |
| high | 最高价 | 精度：小数点后4位；单位：人民币元 |  |
| low | 最低价 | 精度：小数点后4位；单位：人民币元 |  |
| close | 收盘价 | 精度：小数点后4位；单位：人民币元 |  |
| volume | 成交数量 | 单位：股 |  |
| amount | 成交金额 | 精度：小数点后4位；单位：人民币元 |  |
| adjustflag | 复权状态 | 不复权、前复权、后复权 |  |
| turn | 换手率 | 精度：小数点后6位；单位：% |  |
| pctChg | 涨跌幅（百分比） | 精度：小数点后6位 | 涨跌幅=[(区间最后交易日收盘价-区间首个交易日前收盘价)/区间首个交易日前收盘价]\*100% |

5、15、30、60分钟线指标参数(不包含指数)

| 参数名称 | 参数描述 | 说明 |
|------------|------------|-------|
| date | 交易所行情日期 | 格式：YYYY-MM-DD |
| time | 交易所行情时间 | 格式：YYYYMMDDHHMMSSsss |
| code | 证券代码 | 格式：sh.600000。sh：上海，sz：深圳 |
| open | 开盘价格 | 精度：小数点后4位；单位：人民币元 |
| high | 最高价 | 精度：小数点后4位；单位：人民币元 |
| low | 最低价 | 精度：小数点后4位；单位：人民币元 |
| close | 收盘价 | 精度：小数点后4位；单位：人民币元 |
| volume | 成交数量 | 单位：股； 时间范围内的累计成交数量 |
| amount | 成交金额 | 精度：小数点后4位；单位：人民币元； 时间范围内的累计成交金额 |
| adjustflag | 复权状态 | 不复权、前复权、后复权 |
