### Python API文档

## 目录

* [1 入门示例](#入门示例)
  + [1.1 HelloWorld](#HelloWorld)
* [2 登录](#登录)
  + [2.1 login()](#login)
* [3 登出](#登出)
  + [3.1 logout()](#logout)
* [4 获取历史A股K线数据](#获取历史A股K线数据)
  + [4.1 获取历史A股K线数据：query_history_k_data_plus()](#query_history_k_data_plus)
  + [4.2 历史行情指标参数](#历史行情指标参数)
* [5 获取每日数据](#获取每日数据)
  + [5.1 获取某日所有股票日K线数据：query_daily_history_k_AStock()](#query_daily_history_k_AStock)
  + [5.2 获取某日所有ETF日K线数据：query_daily_history_k_ETF()](#query_daily_history_k_ETF)
  + [5.3 获取某日复权因子信息：query_daily_adjust_factor()](#query_daily_adjust_factor)
* [6 查询除权除息信息](#查询除权除息信息)
  + [6.1 除权除息信息：query_dividend_data()](#query_dividend_data)
* [7 查询复权因子信息](#查询复权因子信息)
  + [7.1 复权因子：query_adjust_factor()](#query_adjust_factor)
* [8 查询季频财务数据信息](#查询季频财务数据信息)
  + [8.1 季频盈利能力：query_profit_data()](#query_profit_data)
  + [8.2 季频营运能力：query_operation_data()](#query_operation_data)
  + [8.3 季频成长能力：query_growth_data()](#query_growth_data)
  + [8.4 季频偿债能力：query_balance_data()](#query_balance_data)
  + [8.5 季频现金流量：query_cash_flow_data()](#query_cash_flow_data)
  + [8.6 季频杜邦指数：query_dupont_data()](#query_dupont_data)
* [9 查询季频公司报告信息](#查询季频公司报告信息)
  + [9.1 季频公司业绩快报：query_performance_express_report()](#query_performance_express_report)
  + [9.2 季频公司业绩预告：query_forecast_report()](#query_forecast_report)
* [10 证券基本资料](#证券基本资料)
  + [10.1 证券基本资料：query_stock_basic()](#query_stock_basic)
* [11 获取证券元信息](#获取证券元信息)
  + [11.1 交易日查询：query_trade_dates()](#query_trade_dates)
  + [11.2 证券代码查询：query_all_stock()](#query_all_stock)
* [12 宏观经济数据](#宏观经济数据)
  + [12.1 存款利率：query_deposit_rate_data()](#query_deposit_rate_data)
  + [12.2 贷款利率：query_loan_rate_data()](#query_loan_rate_data)
  + [12.3 存款准备金率：query_required_reserve_ratio_data()](#query_required_reserve_ratio_data)
  + [12.4 货币供应量：query_money_supply_data_month()](#query_money_supply_data_month)
  + [12.5 货币供应量(年底余额)：query_money_supply_data_year()](#query_money_supply_data_year)
* [13 板块数据](#板块数据)
  + [13.1 行业分类：query_stock_industry()](#query_stock_industry)
  + [13.2 上证50成分股：query_sz50_stocks()](#query_sz50_stocks)
  + [13.3 沪深300成分股：query_hs300_stocks()](#query_hs300_stocks)
  + [13.4 中证500成分股：query_zz500_stocks()](#query_zz500_stocks)
* [14 示例程序](#示例程序)
  + [14.1 获取指定日期全部股票的日K线数据：query_history_k_data_plus()](#example_query_history_k_data_plus)

## 入门示例

### HelloWorld

此篇为平台入门示例，安装baostock后，可导入包运行此示例。示例数据：[下载](https://www.baostock.com/helpdocs/csv/history_k_data.xlsx)

```python

import baostock as bs
import pandas as pd

#### 登陆系统 ####
lg = bs.login()
# 显示登陆返回信息
print('login respond error_code:'+lg.error_code)
print('login respond  error_msg:'+lg.error_msg)

#### 获取历史K线数据 ####
# 详细指标参数，参见“历史行情指标参数”章节
rs = bs.query_history_k_data_plus("sh.600000",
    "date,code,open,high,low,close,preclose,volume,amount,adjustflag,turn,tradestatus,pctChg,peTTM,pbMRQ,psTTM,pcfNcfTTM,isST",
    start_date='2017-06-01', end_date='2017-12-31',
    frequency="d", adjustflag="3") #frequency="d"取日k线，adjustflag="3"默认不复权
print('query_history_k_data_plus respond error_code:'+rs.error_code)
print('query_history_k_data_plus respond  error_msg:'+rs.error_msg)

#### 打印结果集 ####
data_list = []
while (rs.error_code == '0') & rs.next():
    # 获取一条记录，将记录合并在一起
    data_list.append(rs.get_row_data())
result = pd.DataFrame(data_list, columns=rs.fields)
#### 结果集输出到csv文件 ####
result.to_csv("D:/history_k_data.csv", encoding="gbk", index=False)
print(result)

#### 登出系统 ####
bs.logout()

```

## 登录
### login()

方法说明：登录系统。

使用示例：lg = login()

返回信息：

* lg.error_code：错误代码，当为“0”时表示成功，当为非0时表示失败；
* lg.error_msg：错误信息，对错误的详细解释。

## 登出

### logout()

方法说明：登出系统

使用示例：lg = logout()

返回信息：

* lg.error_code：错误代码，当为“0”时表示成功，当为非0时表示失败；
* lg.error_msg：错误信息，对错误的详细解释。

## 获取历史A股K线数据

### 获取历史A股K线数据：query_history_k_data_plus()

方法说明：通过API接口获取A股历史交易数据，可以通过参数设置获取日k线、周k线、月k线，以及5分钟、15分钟、30分钟和60分钟k线数据，适合搭配均线数据进行选股和分析。

返回类型：pandas的DataFrame类型。

分钟K线，日、周、月K线支持日期范围请看“平台介绍-数据范围说明”；

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
# 分钟线指标：date,time,code,open,high,low,close,volume,amount,adjustflag
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

周线使用示例：

```python

import baostock as bs
import pandas as pd

#### 登陆系统 ####
lg = bs.login()
# 显示登陆返回信息
print('login respond error_code:'+lg.error_code)
print('login respond  error_msg:'+lg.error_msg)

#### 获取沪深A股历史周K线数据 ####
# 周线指标：date,code,open,high,low,close,volume,amount,adjustflag,turn,pctChg
rs = bs.query_history_k_data_plus("sh.600000",
    "date,code,open,high,low,close,volume,amount,adjustflag,turn,pctChg",
    start_date='2024-07-01', end_date='2024-12-31',
    frequency="w", adjustflag="3")
print('query_history_k_data_plus respond error_code:'+rs.error_code)
print('query_history_k_data_plus respond  error_msg:'+rs.error_msg)

#### 打印结果集 ####
data_list = []
while (rs.error_code == '0') & rs.next():
    # 获取一条记录，将记录合并在一起
    data_list.append(rs.get_row_data())
result = pd.DataFrame(data_list, columns=rs.fields)

#### 结果集输出到csv文件 ####
result.to_csv("D:\\history_A_stock_k_data_week.csv", index=False)
print(result)

#### 登出系统 ####
bs.logout()

```

月线使用示例：

```python

import baostock as bs
import pandas as pd

#### 登陆系统 ####
lg = bs.login()
# 显示登陆返回信息
print('login respond error_code:'+lg.error_code)
print('login respond  error_msg:'+lg.error_msg)

#### 获取沪深A股历史月K线数据 ####
# 月线指标：date,code,open,high,low,close,volume,amount,adjustflag,turn,pctChg
rs = bs.query_history_k_data_plus("sh.600000",
    "date,code,open,high,low,close,volume,amount,adjustflag,turn,pctChg",
    start_date='2024-07-01', end_date='2024-12-31',
    frequency="m", adjustflag="3")
print('query_history_k_data_plus respond error_code:'+rs.error_code)
print('query_history_k_data_plus respond  error_msg:'+rs.error_msg)

#### 打印结果集 ####
data_list = []
while (rs.error_code == '0') & rs.next():
    # 获取一条记录，将记录合并在一起
    data_list.append(rs.get_row_data())
result = pd.DataFrame(data_list, columns=rs.fields)

#### 结果集输出到csv文件 ####
result.to_csv("D:\\history_A_stock_k_data_month.csv", index=False)
print(result)

#### 登出系统 ####
bs.logout()

```

参数含义：

* code：股票代码，sh或sz.+6位数字代码，或者指数代码，如：sh.601398。sh：上海；sz：深圳。此参数不可为空；
* fields：指示简称，支持多指标输入，以半角逗号分隔，填写内容作为返回类型的列。**详细指标列表见历史行情指标参数章节，日线与分钟线参数不同**。此参数不可为空；
* start_date：开始日期（包含），格式“YYYY-MM-DD”，为空时取2015-01-01；
* end_date：结束日期（包含），格式“YYYY-MM-DD”，为空时取最近一个交易日；
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

| date       | code       | open  | high  | low   | close | preclose | volume    | amount     | adjustflag | turn     | tradestatus | pctChg     | isST |
|------------|------------|-------|-------|-------|-------|----------|-----------|------------|------------|----------|-------------|------------|------|
| 2017-07-03 | sh.600000  | 12.64 | 12.65 | 12.47 | 12.56 | 12.65    | 38778949  | 486264672  | 3          | 0.137985 | 1           | -0.711456  | 0    |
| 2017-07-04 | sh.600000  | 12.55 | 12.58 | 12.41 | 12.55 | 12.56    | 36659128  | 458434432  | 3          | 0.130442 | 1           | -0.07962   | 0    |
| 2017-07-05 | sh.600000  | 12.5  | 12.65 | 12.47 | 12.62 | 12.55    | 26470507  | 332542464  | 3          | 0.094188 | 1           | 0.557767   | 0    |
| 2017-07-06 | sh.600000  | 12.62 | 12.72 | 12.51 | 12.66 | 12.62    | 37414241  | 471582096  | 3          | 0.133129 | 1           | 0.316957   | 0    |
| 2017-07-07 | sh.600000  | 12.62 | 12.69 | 12.55 | 12.6  | 12.66    | 24667294  | 311101536  | 3          | 0.087772 | 1           | -0.473929  | 0    |

返回数据说明

| 参数名称     | 参数描述                     | 算法说明                                                                 |
|--------------|------------------------------|--------------------------------------------------------------------------|
| date         | 交易所行情日期               |                                              |
| code         | 证券代码                     |                   |
| open         | 开盘价                       |                                           |
| high         | 最高价                       |                                                 |
| low          | 最低价                       |                                              |
| close        | 收盘价                       |                                           |
| preclose     | 前收盘价                     | 见表格下方详细说明                                |
| volume       | 成交量（累计，单位：股）     |                                                    |
| amount       | 成交额（单位：人民币元）     |                                             |
| adjustflag   | 复权状态（1：后复权，2：前复权，3：不复权）|                           |
| turn         | 换手率                       | [指定交易日的成交量(股)/指定交易日的股票的流通股总股数(股)]*100%                        |
| tradestatus  | 交易状态（1：正常交易，0：停牌）  |                                          |
| pctChg       | 涨跌幅，单位：%             | 日涨跌幅=[(指定交易日的收盘价-指定交易日前收盘价)/指定交易日前收盘价]*100%                   |
| peTTM        | 滚动市盈率                   | (指定交易日的股票收盘价/指定交易日的每股盈余TTM)=(指定交易日的股票收盘价*截至当日公司总股本)/归属母公司股东净利润TTM                 |
| pbMRQ        | 市净率                       | (指定交易日的股票收盘价/指定交易日的每股净资产)=总市值/(最近披露的归属母公司股东的权益-其他权益工具)                  |
| psTTM        | 滚动市销率                   | (指定交易日的股票收盘价/指定交易日的每股销售额)=(指定交易日的股票收盘价*截至当日公司总股本)/营业总收入TTM                             |
| pcfNcfTTM    | 滚动市现率                   | (指定交易日的股票收盘价/指定交易日的每股现金流TTM)=(指定交易日的股票收盘价*截至当日公司总股本)/现金以及现金等价物净增加额TTM              |
| isST         | 是否ST股，1是，0否                    |                                                 |

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
| adjustflag | 复权状态 | 1：后复权，2：前复权，3：不复权 |
| turn | 换手率 | 精度：小数点后6位，单位：% |
| tradestatus | 交易状态 | 1：正常交易，0：停牌 |
| pctChg | 涨跌幅，单位：% | 精度：小数点后6位 |
| peTTM | 滚动市盈率 | 精度：小数点后6位 |
| psTTM | 滚动市销率 | 精度：小数点后6位 |
| pcfNcfTTM | 滚动市现率 | 精度：小数点后6位 |
| pbMRQ | 市净率 | 精度：小数点后6位 |
| isST | 是否ST | 1：是，0：否 |

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
| adjustflag | 复权状态 | 1：后复权，2：前复权，3：不复权 |  |
| turn | 换手率 | 精度：小数点后6位，单位：% |  |
| pctChg | 涨跌幅，单位：% | 精度：小数点后6位 | 涨跌幅=[(区间最后交易日收盘价-区间首个交易日前收盘价)/区间首个交易日前收盘价]\*100% |

5、15、30、60分钟线指标参数(不包含指数)

| 参数名称 | 参数描述 | 说明 |
|------------|------------|-------|
| date | 交易所行情日期 | 格式：YYYY-MM-DD |
| time | 交易所行情时间 | 格式：YYYYMMDDHHMMSSsss |
| code | 证券代码 | 格式：sh.600000。sh：上海，sz：深圳 |
| open | 开盘价格 | 精度：小数点后4位；单位：人民币元 |
| high | 最高价 | 精度：小数点后4位；单位：人民币元；取时间区间内所有最新价中的最大值 |
| low | 最低价 | 精度：小数点后4位；单位：人民币元；取时间区间内所有最新价中的最小值 |
| close | 收盘价 | 精度：小数点后4位；单位：人民币元 |
| volume | 成交数量 | 单位：股； 时间范围内的累计成交数量 |
| amount | 成交金额 | 精度：小数点后4位；单位：人民币元； 时间范围内的累计成交金额 |
| adjustflag | 复权状态 | 1：后复权，2：前复权，3：不复权 |

## 获取每日数据

### 获取某日所有股票日K线数据：query_daily_history_k_AStock()

方法说明：通过API接口获取A股历史交易数据，可以通过参数设置获取指定日期A股日k线数据，适合搭配均线数据进行选股和分析。

返回类型：pandas的DataFrame类型。

使用示例：

```python

import baostock as bs
import pandas as pd

#### 登陆系统 ####
lg = bs.login()
# 显示登陆返回信息
print('login respond error_code:'+lg.error_code)
print('login respond  error_msg:'+lg.error_msg)

#### 获取某日所有股票日K线数据 ####
#返回字段：date,code,open,high,low,close,preclose,volume,amount,adjustflag,turn,tradestatus,pctChg,peTTM,pbMRQ,psTTM,pcfNcfTTM,isST
rs = bs.query_daily_history_k_AStock(date='2026-02-05') #
pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
pd.set_option('display.width', 1000)
print('query_daily_history_k_AStock respond error_code:'+rs.error_code)
print('query_daily_history_k_AStock respond  error_msg:'+rs.error_msg)

#### 打印结果集 ####
data_list = []
while (rs.error_code == '0') & rs.next():
    # 获取一条记录，将记录合并在一起
    data_list.append(rs.get_row_data())
result = pd.DataFrame(data_list, columns=rs.fields)

#### 结果集输出到csv文件 ####
result.to_csv("D:/daily_history_k_AStock_data.csv", encoding="gbk", index=False)
print(result)

#### 登出系统 ####
bs.logout()

```

参数含义：

* date：获取日期，格式“YYYY-MM-DD”，为空时取当前自然日；

**注意：**

* 股票停牌时，对于日线，开、高、低、收价都相同，且都为前一交易日的收盘价，成交量、成交额为0，换手率为空。

如果需要将换手率转为float类型，可使用如下方法转换：result["turn"] = [0 if x == "" else float(x) for x in result["turn"]]

返回示例数据

| date       | code       | open    | high    | low     | close   | preclose | volume     | amount        | adjustflag | turn     | tradestatus | pctChg    | peTTM      | pbMRQ    | psTTM    | pcfNcfTTM    | isST |
|------------|------------|---------|---------|---------|---------|----------|------------|---------------|------------|----------|-------------|-----------|------------|----------|----------|--------------|------|
| 2026-02-05 | sh.600648  | 10.7000 | 10.7800 | 10.6400 | 10.7400 | 10.6800  | 4465487    | 47925519.1900 | 3          | 0.392500 | 1           | 0.561800  | 21.493688  | 0.962863 | 2.226877 | -58.658491   | 0    |
| 2026-02-05 | sh.600649  | 5.5200  | 5.7800  | 5.4600  | 5.6400  | 5.5500   | 106503170  | 598013239.0900| 3          | 4.252500 | 1           | 1.621600  | 18.947748  | 0.670040 | 0.783396 | 18.948974    | 0    |
| 2026-02-05 | sh.600650  | 15.1800 | 15.3500 | 15.1200 | 15.2500 | 15.2600  | 3477800    | 52978520.0000 | 3          | 0.890500 | 1           | -0.065500 | 67.776938  | 1.964848 | 4.942318 | 53.735923    | 0    |
| 2026-02-05 | sh.600651  | 8.0100  | 8.1000  | 7.9000  | 8.0100  | 8.0500   | 18066100   | 144088874.0000| 3          | 0.720600 | 1           | -0.496900 | 404.504618 | 8.055464 | 10.498675| 151.923309   | 0    |

返回数据说明

| 参数名称     | 参数描述                     | 算法说明                                                                 |
|--------------|------------------------------|--------------------------------------------------------------------------|
| date         | 交易所行情日期               |                                              |
| code         | 证券代码                     |                   |
| open         | 开盘价                       |                                           |
| high         | 最高价                       |                                                 |
| low          | 最低价                       |                                              |
| close        | 收盘价                       |                                           |
| preclose     | 前收盘价                     | 见表格下方详细说明                                |
| volume       | 成交量（累计，单位：股）     |                                                    |
| amount       | 成交额（单位：人民币元）     |                                             |
| adjustflag   | 复权状态（1：后复权，2：前复权，3：不复权）|                           |
| turn         | 换手率                       | [指定交易日的成交量(股)/指定交易日的股票的流通股总数(股)]*100%                        |
| tradestatus  | 交易状态（1：正常交易，0：停牌）  |                                          |
| pctChg       | 涨跌幅，单位：%             | 日涨跌幅=[(指定交易日的收盘价-指定交易日前收盘价)/指定交易日前收盘价]*100%                   |
| peTTM        | 滚动市盈率                   | (指定交易日的股票收盘价/指定交易日的每股盈余TTM)=(指定交易日的股票收盘价*截至当日公司总股本)/归属母公司股东净利润TTM                 |
| pbMRQ        | 市净率                       | (指定交易日的股票收盘价/指定交易日的每股净资产)=总市值/(最近披露的归属母公司股东的权益-其他权益工具)                  |
| psTTM        | 滚动市销率                   | (指定交易日的股票收盘价/指定交易日的每股销售额)=(指定交易日的股票收盘价*截至当日公司总股本)/营业总收入TTM                             |
| pcfNcfTTM    | 滚动市现率                   | (指定交易日的股票收盘价/指定交易日的每股现金流TTM)=(指定交易日的股票收盘价*截至当日公司总股本)/现金以及现金等价物净增加额TTM              |
| isST         | 是否ST股,1：是，0：否                    |                                                 |

### 获取某日所有ETF日K线数据：query_daily_history_k_ETF()

方法说明：通过API接口获取ETF历史交易数据，可以通过参数设置获取指定日期ETF日k线数据，适合搭配均线数据进行选股和分析。

返回类型：pandas的DataFrame类型。

使用示例：

```python

import baostock as bs
import pandas as pd

#### 登陆系统 ####
lg = bs.login()
# 显示登陆返回信息
print('login respond error_code:'+lg.error_code)
print('login respond  error_msg:'+lg.error_msg)

#### 获取某日所有ETF日K线数据 ####
#返回字段：date,code,open,high,low,close,preclose,volume,amount,adjustflag,turn,tradestatus,pctChg,isST
rs = bs.query_daily_history_k_ETF(date='2026-02-05')  #
print('query_daily_history_k_ETF respond error_code:'+rs.error_code)
print('query_daily_history_k_ETF respond  error_msg:'+rs.error_msg)

#### 打印结果集 ####
data_list = []
while (rs.error_code == '0') & rs.next():
    # 获取一条记录，将记录合并在一起
    data_list.append(rs.get_row_data())
result = pd.DataFrame(data_list, columns=rs.fields)

#### 结果集输出到csv文件 ####
result.to_csv("D:/daily_history_k_ETF_data.csv", encoding="gbk", index=False)
print(result)

#### 登出系统 ####
bs.logout()

```

参数含义：

* date：获取日期，格式“YYYY-MM-DD”，为空时取当前自然日；

**注意：**

* 股票停牌时，对于日线，开、高、低、收价都相同，且都为前一交易日的收盘价，成交量、成交额为0，换手率为空。

如果需要将换手率转为float类型，可使用如下方法转换：result["turn"] = [0 if x == "" else float(x) for x in result["turn"]]

返回示例数据

| date         | code      | open   | high   | low    | close  | preclose | volume  | amount      | adjustflag | turn     | tradestatus | pctChg    |
|--------------|-----------|--------|--------|--------|--------|----------|---------|-------------|------------|----------|-------------|-----------|
| 2026-02-05 | sh.510010 | 1.8230 | 1.8280 | 1.8180 | 1.8280 | 1.8290   | 59000   | 107477.0000 | 3          | 0.041986 | 1           | -0.054700 |
| 2026-02-05 | sh.510020 | 3.8450 | 3.8810 | 3.8450 | 3.8780 | 3.8840   | 265300  | 1025309.0000| 3          | 0.740069 | 1           | -0.154500 |
| 2026-02-05 | sh.510030 | 1.0830 | 1.0910 | 1.0770 | 1.0870 | 1.0820   | 4610000 | 4990416.0000| 3          | 2.748468 | 1           | 0.462100  |
| 2026-02-05 | sh.510040 | 1.2060 | 1.2090 | 1.1960 | 1.2050 | 1.2120   | 346500  | 416305.0000 | 3          | 1.004930 | 1           | -0.577600 |

返回数据说明

| 参数名称     | 参数描述                     | 算法说明                                                                 |
|--------------|------------------------------|--------------------------------------------------------------------------|
| date         | 交易所行情日期               |                                              |
| code         | 证券代码                     |                   |
| open         | 开盘价                       |                                           |
| high         | 最高价                       |                                                 |
| low          | 最低价                       |                                              |
| close        | 收盘价                       |                                           |
| preclose     | 前收盘价                     | 见表格下方详细说明                                |
| volume       | 成交量（累计，单位：股）     |                                                    |
| amount       | 成交额（单位：人民币元）     |                                             |
| adjustflag   | 复权状态（1：后复权，2：前复权，3：不复权）|                           |
| turn         | 换手率                       | [指定交易日的成交量(股)/指定交易日的股票的流通股总数(股)]*100%                        |
| tradestatus  | 交易状态（1：正常交易，0：停牌）  |                                          |
| pctChg       | 涨跌幅，单位：%             | 日涨跌幅=[(指定交易日的收盘价-指定交易日前收盘价)/指定交易日前收盘价]*100%                   |

### 获取某日复权因子信息：query_daily_adjust_factor()

方法说明：通过API接口获取指定日期复权因子信息数据。

返回类型：pandas的DataFrame类型。

使用示例：

```python

import baostock as bs
import pandas as pd

# 登陆系统
lg = bs.login()
# 显示登陆返回信息
print('login respond error_code:'+lg.error_code)
print('login respond  error_msg:'+lg.error_msg)

# 获取某日复权因子信息
rs_list = []
#返回字段：code, dividOperateDate, foreAdjustFactor, backAdjustFactor, adjustFactor
rs_factor = bs.query_daily_adjust_factor(date="2026-02-05") #
print('query_daily_adjust_factor respond error_code:'+rs_factor.error_code)
print('query_daily_adjust_factor respond  error_msg:'+rs_factor.error_msg)

while (rs_factor.error_code == '0') & rs_factor.next():
    # 获取一条记录，将记录合并在一起
    rs_list.append(rs_factor.get_row_data())
result = pd.DataFrame(rs_list, columns=rs_factor.fields)
# 打印输出
print(result)

# 结果集输出到csv文件
result.to_csv("D:\\daily_adjust_factor_data.csv", encoding="gbk", index=False)

# 登出系统
bs.logout()

```

参数含义：

* date：获取日期，格式“YYYY-MM-DD”，为空时取当前自然日；

**注意：**

* 该接口只返回指定日期**发生除权除息**的证券复权因子，当日没有除权除息的证券不会出现在结果集中；复权因子只在除权除息日产生记录，并非逐日记录；
* date 为空时取当前自然日；该日期为非交易日或当日无任何除权除息事件时，返回空结果集，error_code 仍为"0"；
* 结果集为分页数据，需用 while 循环逐页读取。若需某只证券连续区间的复权因子，应使用 query_adjust_factor() 而非本接口。

返回示例数据

| code       | dividOperateDate | foreAdjustFactor | backAdjustFactor | adjustFactor |
|------------|------------------|------------------|------------------|--------------|
| sh.601818  | 2026-02-05       | 1.000000         | 2.072976         | 2.072976     |
| sh.601860  | 2026-02-05       | 0.980989         | 1.257941         | 1.257941     |
| sh.603019  | 2026-02-05       | 0.995693         | 4.082735         | 4.082735     |
| sh.603727  | 2026-02-05       | 0.991643         | 1.109671         | 1.109671     |

返回数据说明

| 参数名称     | 参数描述                     | 算法说明                                                                 |
|--------------|------------------------------|--------------------------------------------------------------------------|
| code | 证券代码 | |
| dividOperateDate | 除权除息日期 | |
| foreAdjustFactor | 向前复权因子 | 当天的前收/前一天的收盘价，最近一次除权除息日后的交易日前复权因子为1 |
| backAdjustFactor | 向后复权因子 | 前一天的收盘价/当天的前收，上市首日后复权因子为1 |
| adjustFactor | 本次复权因子 | |

## 查询除权除息信息

### 除权除息信息：query_dividend_data()

通过API接口获取除权除息信息数据（预披露、预案、正式都已通过）。示例数据：[下载](https://www.baostock.com/helpdocs/csv/history_Dividend_data.xlsx)

```py
import baostock as bs
import pandas as pd

#### 登陆系统 ####
lg = bs.login()
# 显示登陆返回信息
print('login respond error_code:'+lg.error_code)
print('login respond  error_msg:'+lg.error_msg)

#### 查询除权除息信息####
# 查询2015年除权除息信息
rs_list = []
rs_dividend_2015 = bs.query_dividend_data(code="sh.600000", year="2015", yearType="report")
while (rs_dividend_2015.error_code == '0') & rs_dividend_2015.next():
    rs_list.append(rs_dividend_2015.get_row_data())

# 查询2016年除权除息信息
rs_dividend_2016 = bs.query_dividend_data(code="sh.600000", year="2016", yearType="report")
while (rs_dividend_2016.error_code == '0') & rs_dividend_2016.next():
    rs_list.append(rs_dividend_2016.get_row_data())

# 查询2017年除权除息信息
rs_dividend_2017 = bs.query_dividend_data(code="sh.600000", year="2017", yearType="report")
while (rs_dividend_2017.error_code == '0') & rs_dividend_2017.next():
    rs_list.append(rs_dividend_2017.get_row_data())

result_dividend = pd.DataFrame(rs_list, columns=rs_dividend_2017.fields)
# 打印输出
print(result_dividend)

#### 结果集输出到csv文件 ####
result_dividend.to_csv("D:\\history_Dividend_data.csv", encoding="gbk",index=False)

#### 登出系统 ####
bs.logout()

```

参数含义：

* code：股票代码，sh或sz.+6位数字代码，或者指数代码，如：sh.601398。sh：上海；sz：深圳。此参数不可为空；
* year：年份，如：2017。此参数不可为空；
* yearType：年份类别，默认为"report":预案公告年份，可选项"operate":除权除息年份。此参数不可为空。

**说明：**

* yearType 仅支持"report"和"operate"两个取值，区分大小写，必须使用小写字符串；
* "report"按预案公告年份（dividPlanAnnounceDate 所在年份）筛选；"operate"按除权除息年份（dividOperateDate 所在年份）筛选。两种取值的返回字段完全相同，区别仅在于筛选所依据的日期；
* dividCashPsAfterTax 中出现的两个数值（如 0.6813 或 0.71915）是按不同税率（10%、5%）计算出的税后每股股利，具体返回哪一个以接口实际返回的字符串为准；
* 某一年度没有分红方案时，返回空结果集，error_code 仍为"0"；预披露公告日等日期字段在尚未披露时返回空字符串。

返回示例数据

| code | dividPreNoticeDate | dividAgmPumDate | dividPlanAnnounceDate | dividPlanDate | dividRegistDate | dividOperateDate | dividPayDate |
|------------|------------|-------|-------|-------|-------|----------|-----------|
| sh.600000 |  | 2015-05-16 | 2015-03-19 | 2015-06-16 | 2015-06-19 | 2015-06-23 | 2015-06-23 |
| sh.600000 |  | 2016-04-29 | 2016-04-07 | 2016-06-16 | 2016-06-22 | 2016-06-23 | 2016-06-23 |
| sh.600000 |  | 2017-04-26 | 2017-04-01 | 2017-05-19 | 2017-05-24 | 2017-05-25 | 2017-05-25 |

返回示例数据

| dividStockMarketDate | dividCashPsBeforeTax | dividCashPsAfterTax | dividStocksPs | dividCashStock | dividReserveToStockPs |
|------------|------------|-------|------------|------------|-------|
|  | 0.757 | 0.6813或0.71915 | 0.000000 | 10派7.57元（含税，扣税后6.813或7.1915元） |  |
| 2016-06-24 | 0.515 | 0.4635或0.515 | 0.000000 | 10转1派5.15元（含税，扣税后4.635或5.15元） | 0.100000 |
| 2017-05-26 | 0.2 | 0.18或0.2 | 0.000000 | 10转3派2元（含税，扣税后1.8或2元） | 0.300000 |

返回数据说明

| 参数名称 | 参数描述 | 算法说明 |
|------------|------------|-------|
| code | 证券代码 |  |
| dividPreNoticeDate | 预批露公告日 |  |
| dividAgmPumDate | 股东大会公告日期 |  |
| dividPlanAnnounceDate | 预案公告日 |  |
| dividPlanDate | 分红实施公告日 |  |
| dividRegistDate | 股权登记告日 |  |
| dividOperateDate | 除权除息日期 |  |
| dividPayDate | 派息日 |  |
| dividStockMarketDate | 红股上市交易日 |  |
| dividCashPsBeforeTax | 每股股利税前 | 派息比例分子(税前)/派息比例分母 |
| dividCashPsAfterTax | 每股股利税后 | 派息比例分子(税后)/派息比例分母 |
| dividStocksPs | 每股红股 |  |
| dividCashStock | 分红送转 | 每股派息数(税前)+每股送股数+每股转增股本数 |
| dividReserveToStockPs | 每股转增资本 |  |

## 查询复权因子信息

### 复权因子：query_adjust_factor()

通过API接口获取复权因子信息数据。示例数据：[下载](https://www.baostock.com/helpdocs/csv/adjust_factor_data.xlsx)

BaoStock提供的是**涨跌幅复权算法**复权因子，具体介绍见： [媒体文件:BaoStock复权因子简介.pdf](https://www.baostock.com/helpdocs/pdf/BaoStock%E5%A4%8D%E6%9D%83%E5%9B%A0%E5%AD%90%E7%AE%80%E4%BB%8B.pdf "BaoStock复权因子简介.pdf")。

基于BaoStock复权因子与本地BaoStock日K线数据**生成复权行情**，具体介绍见：<a href="localdatafactorInfo.md">利用本地Baostock日K线数据手动计算复权价格</a>。

```py
import baostock as bs
import pandas as pd

# 登陆系统
lg = bs.login()
# 显示登陆返回信息
print('login respond error_code:'+lg.error_code)
print('login respond  error_msg:'+lg.error_msg)

# 查询2015至2017年复权因子
rs_list = []
rs_factor = bs.query_adjust_factor(code="sh.600000", start_date="2015-01-01", end_date="2017-12-31")
while (rs_factor.error_code == '0') & rs_factor.next():
    rs_list.append(rs_factor.get_row_data())
result_factor = pd.DataFrame(rs_list, columns=rs_factor.fields)
# 打印输出
print(result_factor)

# 结果集输出到csv文件
result_factor.to_csv("D:\\adjust_factor_data.csv", encoding="gbk", index=False)

# 登出系统
bs.logout()

```

参数含义：

* code：股票代码，sh或sz.+6位数字代码，或者指数代码，如：sh.601398。sh：上海；sz：深圳。此参数不可为空；
* start_date：开始日期，为空时默认为2015-01-01，包含此日期；
* end_date：结束日期，为空时默认当前日期，包含此日期。

**说明：**

* start_date 为空时默认取2015-01-01，只返回该日期之后的复权因子。若需计算2015年之前的前复权/后复权价格，必须显式传入更早的 start_date（如该股票上市日期），否则会丢失早期的复权因子，导致复权价格计算错误；
* 复权因子**只在除权除息日（dividOperateDate）产生记录**，并非每个交易日一条记录。计算某一交易日的复权价格时，应取“小于等于该交易日”的最近一条复权因子；
* 查询区间内没有除权除息事件（如新股上市后从未分红送配）时，返回空结果集，error_code 仍为"0"；
* 复权因子与除权除息信息（query_dividend_data()）一一对应，两者返回的除权除息日期数量应当一致，可据此交叉校验数据完整性。

返回示例数据

| code | dividOperateDate | foreAdjustFactor | backAdjustFactor | adjustFactor |
|------------|------------|-------|-------|-------|
| sh.600000 | 2015-06-23 | 0.663792 | 6.295967 | 6.295967 |
| sh.600000 | 2016-06-23 | 0.751598 | 7.128788 | 7.128788 |
| sh.600000 | 2017-05-25 | 0.989551 | 9.385732 | 9.385732 |

返回数据说明

| 参数名称 | 参数描述 | 算法说明 |
|------------|------------|-------|
| code | 证券代码 |  |
| dividOperateDate | 除权除息日期 |  |
| foreAdjustFactor | 向前复权因子 | 当天的前收/前一天的收盘价，最近一次除权除息日后的交易日前复权因子为1 |
| backAdjustFactor | 向后复权因子 | 前一天的收盘价/当天的前收，上市首日后复权因子为1 |
| adjustFactor | 本次复权因子 |  |

## 查询季频财务数据信息

**说明（适用于本章节6个季频财务接口）：**

* quarter 取值为1、2、3、4，分别对应一季报（3月31日）、半年报（6月30日）、三季报（9月30日）、年报（12月31日）。quarter=4 即为**年报**数据，statDate 为当年的12-31；
* 同一证券同一报告期（year+quarter）在数据库中仅保留一条记录，如财报数据被修正，返回的是最新披露口径的数据；
* 当指定季度尚未披露、或该证券当年无对应报告时，返回空结果集，error_code 仍为"0"，此时不应视为接口异常；
* 财务比率类字段在分母为0或数据缺失时返回空字符串，使用前需先做空值判断，不能直接转为 float；
* 营运能力的周转天数按报告期累计天数折算（一季报90天、中报180天、三季报270天、年报360天），并非单季度天数；
* 成长能力的同比增速均与上年同一报告期比较，而非与上一季度环比；
* 偿债能力指标基于资产负债表时点数计算，四个季度可直接横向比较；现金流量表数据为报告期累计口径，如需单季度数据须用本期累计值减去上一报告期累计值；
* 杜邦指数各分解项相乘即可还原 dupontROE，可用于归因分析。

### 季频盈利能力：query_profit_data()

方法说明：通过API接口获取季频盈利能力信息，可以通过参数设置获取对应年份、季度数据，提供2007年至今数据。

返回类型：pandas的DataFrame类型。

使用示例

```py
import baostock as bs
import pandas as pd

# 登陆系统
lg = bs.login()
# 显示登陆返回信息
print('login respond error_code:'+lg.error_code)
print('login respond  error_msg:'+lg.error_msg)

# 查询季频估值指标盈利能力
profit_list = []
rs_profit = bs.query_profit_data(code="sh.600000", year=2017, quarter=2)
while (rs_profit.error_code == '0') & rs_profit.next():
    profit_list.append(rs_profit.get_row_data())
result_profit = pd.DataFrame(profit_list, columns=rs_profit.fields)
# 打印输出
print(result_profit)
# 结果集输出到csv文件
result_profit.to_csv("D:\\profit_data.csv", encoding="gbk", index=False)

# 登出系统
bs.logout()

```

参数含义：

* code：股票代码，sh或sz.+6位数字代码，或者指数代码，如：sh.601398。sh：上海；sz：深圳。此参数不可为空；
* year：统计年份，为空时默认当前年；
* quarter：统计季度，可为空，默认当前季度。不为空时只有4个取值：1，2，3，4。

返回示例数据

| code | pubDate | statDate | roeAvg | npMargin | gpMargin | netProfit | epsTTM | MBRevenue | totalShare | liqaShare |
|------------|------------|-------|------------|------------|-------|------------|-------|------------|------------|-------|
| sh.600000 | 2017-08-30 | 2017-06-30 | 0.074617 | 0.342179 |  | 28522000000.000000 | 1.939029 | 83354000000.000000 | 28103763899.00 | 28103763899.00 |

返回数据说明

| 参数名称 | 参数描述 | 算法说明 |
|------------|------------|-------|
| code | 证券代码 |  |
| pubDate | 公司发布财报的日期 |  |
| statDate | 财报统计的季度的最后一天, 比如2017-03-31, 2017-06-30 |  |
| roeAvg | 净资产收益率(平均)(%) | 归属母公司股东净利润/[(期初归属母公司股东的权益+期末归属母公司股东的权益)/2]\*100% |
| npMargin | 销售净利率(%) | 净利润/营业收入\*100% |
| gpMargin | 销售毛利率(%) | 毛利/营业收入\*100%=(营业收入-营业成本)/营业收入\*100% |
| netProfit | 净利润(元) |  |
| epsTTM | 每股收益 | 归属母公司股东的净利润TTM/最新总股本 |
| MBRevenue | 主营营业收入(元) |  |
| totalShare | 总股本 |  |
| liqaShare | 流通股本 |  |

### 季频营运能力：query_operation_data()

方法说明：通过API接口获取季频营运能力信息，可以通过参数设置获取对应年份、季度数据，提供2007年至今数据。

返回类型：pandas的DataFrame类型。

使用示例

```py
import baostock as bs
import pandas as pd

# 登陆系统
lg = bs.login()
# 显示登陆返回信息
print('login respond error_code:'+lg.error_code)
print('login respond  error_msg:'+lg.error_msg)

# 营运能力
operation_list = []
rs_operation = bs.query_operation_data(code="sh.600000", year=2017, quarter=2)
while (rs_operation.error_code == '0') & rs_operation.next():
    operation_list.append(rs_operation.get_row_data())
result_operation = pd.DataFrame(operation_list, columns=rs_operation.fields)
# 打印输出
print(result_operation)
# 结果集输出到csv文件
result_operation.to_csv("D:\\operation_data.csv", encoding="gbk", index=False)

# 登出系统
bs.logout()

```

参数含义：

* code：股票代码，sh或sz.+6位数字代码，或者指数代码，如：sh.601398。sh：上海；sz：深圳。此参数不可为空；
* year：统计年份，为空时默认当前年；
* quarter：统计季度，为空时默认当前季度。不为空时只有4个取值：1，2，3，4。

返回示例数据

| code | pubDate | statDate | NRTurnRatio | NRTurnDays | INVTurnRatio | INVTurnDays | CATurnRatio | AssetTurnRatio |
|------------|------------|-------|------------|------------|-------|------------|------------|-------|
| sh.600000 | 2017-08-30 | 2017-06-30 |  |  |  |  |  | 0.014161 |

返回数据说明

| 参数名称 | 参数描述 | 算法说明 |
|------------|------------|-------|
| code | 证券代码 |  |
| pubDate | 公司发布财报的日期 |  |
| statDate | 财报统计的季度的最后一天, 比如2017-03-31, 2017-06-30 |  |
| NRTurnRatio | 应收账款周转率(次) | 营业收入/[(期初应收票据及应收账款净额+期末应收票据及应收账款净额)/2] |
| NRTurnDays | 应收账款周转天数(天) | 季报天数/应收账款周转率(一季报：90天，中报：180天，三季报：270天，年报：360天) |
| INVTurnRatio | 存货周转率(次) | 营业成本/[(期初存货净额+期末存货净额)/2] |
| INVTurnDays | 存货周转天数(天) | 季报天数/存货周转率(一季报：90天，中报：180天，三季报：270天，年报：360天) |
| CATurnRatio | 流动资产周转率(次) | 营业总收入/[(期初流动资产+期末流动资产)/2] |
| AssetTurnRatio | 总资产周转率 | 营业总收入/[(期初资产总额+期末资产总额)/2] |

### 季频成长能力：query_growth_data()

方法说明：通过API接口获取季频成长能力信息，可以通过参数设置获取对应年份、季度数据，提供2007年至今数据。
返回类型：pandas的DataFrame类型。
使用示例

```py
import baostock as bs
import pandas as pd

# 登陆系统
lg = bs.login()
# 显示登陆返回信息
print('login respond error_code:'+lg.error_code)
print('login respond  error_msg:'+lg.error_msg)

# 成长能力
growth_list = []
rs_growth = bs.query_growth_data(code="sh.600000", year=2017, quarter=2)
while (rs_growth.error_code == '0') & rs_growth.next():
    growth_list.append(rs_growth.get_row_data())
result_growth = pd.DataFrame(growth_list, columns=rs_growth.fields)
# 打印输出
print(result_growth)
# 结果集输出到csv文件
result_growth.to_csv("D:\\growth_data.csv", encoding="gbk", index=False)

# 登出系统
bs.logout()

```

参数含义：

* code：股票代码，sh或sz.+6位数字代码，或者指数代码，如：sh.601398。sh：上海；sz：深圳。此参数不可为空；
* year：统计年份，为空时默认当前年；
* quarter：统计季度，为空时默认当前季度。不为空时只有4个取值：1，2，3，4。

返回示例数据

| code | pubDate | statDate | YOYEquity | YOYAsset | YOYNI | YOYEPSBasic | YOYPNI |
|------------|------------|-------|------------|------------|-------|------------|-------|
| sh.600000 | 2017-08-30 | 2017-06-30 | 0.120243 | 0.101298 | 0.054808 | 0.021053 | 0.052111 |

返回数据说明

| 参数名称 | 参数描述 | 算法说明 |
|------------|------------|-------|
| code | 证券代码 |  |
| pubDate | 公司发布财报的日期 |  |
| statDate | 财报统计的季度的最后一天, 比如2017-03-31, 2017-06-30 |  |
| YOYEquity | 净资产同比增长率，单位：% | (本期净资产-上年同期净资产)/上年同期净资产的绝对值\*100% |
| YOYAsset | 总资产同比增长率，单位：% | (本期总资产-上年同期总资产)/上年同期总资产的绝对值\*100% |
| YOYNI | 净利润同比增长率，单位：% | (本期净利润-上年同期净利润)/上年同期净利润的绝对值\*100% |
| YOYEPSBasic | 基本每股收益同比增长率，单位：% | (本期基本每股收益-上年同期基本每股收益)/上年同期基本每股收益的绝对值\*100% |
| YOYPNI | 归属母公司股东净利润同比增长率，单位：% | (本期归属母公司股东净利润-上年同期归属母公司股东净利润)/上年同期归属母公司股东净利润的绝对值\*100% |

### 季频偿债能力：query_balance_data()

方法说明：通过API接口获取季频偿债能力信息，可以通过参数设置获取对应年份、季度数据，提供2007年至今数据。
返回类型：pandas的DataFrame类型。
使用示例

```py
import baostock as bs
import pandas as pd

# 登陆系统
lg = bs.login()
# 显示登陆返回信息
print('login respond error_code:'+lg.error_code)
print('login respond  error_msg:'+lg.error_msg)

# 偿债能力
balance_list = []
rs_balance = bs.query_balance_data(code="sh.600000", year=2017, quarter=2)
while (rs_balance.error_code == '0') & rs_balance.next():
    balance_list.append(rs_balance.get_row_data())
result_balance = pd.DataFrame(balance_list, columns=rs_balance.fields)
# 打印输出
print(result_balance)
# 结果集输出到csv文件
result_balance.to_csv("D:\\balance_data.csv", encoding="gbk", index=False)

# 登出系统
bs.logout()

```

参数含义：

* code：股票代码，sh或sz.+6位数字代码，或者指数代码，如：sh.601398。sh：上海；sz：深圳。此参数不可为空；
* year：统计年份，为空时默认当前年；
* quarter：统计季度，为空时默认当前季度。不为空时只有4个取值：1，2，3，4。

返回示例数据

| code | pubDate | statDate | currentRatio | quickRatio | cashRatio | YOYLiability | liabilityToAsset | assetToEquity |
|------------|------------|-------|------------|------------|-------|------------|------------|-------|
| sh.600000 | 2017-08-30 | 2017-06-30 |  |  |  | 0.100020 | 0.933703 | 15.083598 |

返回数据说明

| 参数名称 | 参数描述 | 算法说明 |
|------------|------------|-------|
| code | 证券代码 |  |
| pubDate | 公司发布财报的日期 |  |
| statDate | 财报统计的季度的最后一天, 比如2017-03-31, 2017-06-30 |  |
| currentRatio | 流动比率，单位：% | 流动资产/流动负债 |
| quickRatio | 速动比率，单位：% | (流动资产-存货净额)/流动负债 |
| cashRatio | 现金比率，单位：% | (货币资金+交易性金融资产)/流动负债 |
| YOYLiability | 总负债同比增长率，单位：% | (本期总负债-上年同期总负债)/上年同期中负债的绝对值\*100% |
| liabilityToAsset | 资产负债率，单位：% | 负债总额/资产总额 |
| assetToEquity | 权益乘数 | 资产总额/股东权益总额=1/(1-资产负债率) |

### 季频现金流量：query_cash_flow_data()

方法说明：通过API接口获取季频现金流量信息，可以通过参数设置获取对应年份、季度数据，提供2007年至今数据。
返回类型：pandas的DataFrame类型。
使用示例

```py
import baostock as bs
import pandas as pd

# 登陆系统
lg = bs.login()
# 显示登陆返回信息
print('login respond error_code:'+lg.error_code)
print('login respond  error_msg:'+lg.error_msg)

# 季频现金流量
cash_flow_list = []
rs_cash_flow = bs.query_cash_flow_data(code="sh.600000", year=2017, quarter=2)
while (rs_cash_flow.error_code == '0') & rs_cash_flow.next():
    cash_flow_list.append(rs_cash_flow.get_row_data())
result_cash_flow = pd.DataFrame(cash_flow_list, columns=rs_cash_flow.fields)
# 打印输出
print(result_cash_flow)
# 结果集输出到csv文件
result_cash_flow.to_csv("D:\\cash_flow_data.csv", encoding="gbk", index=False)

# 登出系统
bs.logout()

```

参数含义：

* code：股票代码，sh或sz.+6位数字代码，或者指数代码，如：sh.601398。sh：上海；sz：深圳。此参数不可为空；
* year：统计年份，为空时默认当前年；
* quarter：统计季度，为空时默认当前季度。不为空时只有4个取值：1，2，3，4。

返回示例数据

| code | pubDate | statDate | CAToAsset | NCAToAsset | tangibleAssetToAsset | ebitToInterest | CFOToOR | CFOToNP | CFOToGr |
|------------|------------|-------|------------|------------|-------|------------|------------|-------|-------|
| sh.600000 | 2017-08-30 | 2017-06-30 |  |  |  |  | —3.071550 | —8.976439 | —3.071550 |

返回数据说明

| 参数名称 | 参数描述 | 算法说明 |
|------------|------------|-------|
| code | 证券代码 |  |
| pubDate | 公司发布财报的日期 |  |
| statDate | 财报统计的季度的最后一天, 比如2017-03-31, 2017-06-30 |  |
| CAToAsset | 流动资产除以总资产 |  |
| NCAToAsset | 非流动资产除以总资产 |  |
| tangibleAssetToAsset | 有形资产除以总资产 |  |
| ebitToInterest | 已获利息倍数 | 息税前利润/利息费用 |
| CFOToOR | 经营活动产生的现金流量净额除以营业收入 |  |
| CFOToNP | 经营性现金净流量除以净利润 |  |
| CFOToGr | 经营性现金净流量除以营业总收入 |  |

### 季频杜邦指数：query_dupont_data()

方法说明：通过API接口获取季频杜邦指数信息，可以通过参数设置获取对应年份、季度数据，提供2007年至今数据。
返回类型：pandas的DataFrame类型。
使用示例

```py
import baostock as bs
import pandas as pd

# 登陆系统
lg = bs.login()
# 显示登陆返回信息
print('login respond error_code:'+lg.error_code)
print('login respond  error_msg:'+lg.error_msg)

# 查询杜邦指数
dupont_list = []
rs_dupont = bs.query_dupont_data(code="sh.600000", year=2017, quarter=2)
while (rs_dupont.error_code == '0') & rs_dupont.next():
    dupont_list.append(rs_dupont.get_row_data())
result_dupont = pd.DataFrame(dupont_list, columns=rs_dupont.fields)
# 打印输出
print(result_dupont)
# 结果集输出到csv文件
result_dupont.to_csv("D:\\dupont_data.csv", encoding="gbk", index=False)

# 登出系统
bs.logout()

```

参数含义：

* code：股票代码，sh或sz.+6位数字代码，或者指数代码，如：sh.601398。sh：上海；sz：深圳。此参数不可为空；
* year：统计年份，为空时默认当前年；
* quarter：统计季度，为空时默认当前季度。不为空时只有4个取值：1，2，3，4。

返回示例数据

| code | pubDate | statDate | dupontROE | dupontAssetStoEquity | dupontAssetTurn | dupontPnitoni |
|------------|------------|-------|------------|------------|-------|------------|
| sh.600000 | 2017-08-30 | 2017-06-30 | 0.074617 | 15.594453 | 0.014161 | 0.987483 |

返回示例数据

| dupontNitogr | dupontTaxBurden | dupontIntburden | dupontEbittogr |
|------------|------------|-------|-------|
| 0.342179 | 0.776088 |  |  |

返回数据说明

| 参数名称 | 参数描述 | 算法说明 |
|------------|------------|-------|
| code | 证券代码 |  |
| pubDate | 公司发布财报的日期 |  |
| statDate | 财报统计的季度的最后一天, 比如2017-03-31, 2017-06-30 |  |
| dupontROE | 净资产收益率，单位：% | 归属母公司股东净利润/[(期初归属母公司股东的权益+期末归属母公司股东的权益)/2]\*100% |
| dupontAssetStoEquity | 权益乘数，反映企业财务杠杆效应强弱和财务风险 | 平均总资产/平均归属于母公司的股东权益 |
| dupontAssetTurn | 总资产周转率，反映企业资产管理效率的指标，单位：% | 营业总收入/[(期初资产总额+期末资产总额)/2] |
| dupontPnitoni | 归属母公司股东的净利润/净利润，反映母公司控股子公司百分比。如果企业追加投资，扩大持股比例，则本指标会增加。 |  |
| dupontNitogr | 净利润/营业总收入，反映企业销售获利率，单位：% |  |
| dupontTaxBurden | 净利润/利润总额，反映企业税负水平，该比值高则税负较低。净利润/利润总额=1-所得税/利润总额 |  |
| dupontIntburden | 利润总额/息税前利润，反映企业利息负担，该比值高则税负较低。利润总额/息税前利润=1-利息费用/息税前利润 |
| dupontEbittogr | 息税前利润/营业总收入，反映企业经营利润率，是企业经营获得的可供全体投资人（股东和债权人）分配的盈利占企业全部营收收入的百分比 |  |

## 查询季频公司报告信息

### 季频公司业绩快报：query_performance_express_report()

方法说明：通过API接口获取季频公司业绩快报信息，可以通过参数设置获取起止年份数据，提供2006年至今数据。除几种特殊情况外，交易所未要求必须发布。

返回类型：pandas的DataFrame类型。

使用示例

```py
import baostock as bs
import pandas as pd

#### 登陆系统 ####
lg = bs.login()
# 显示登陆返回信息
print('login respond error_code:'+lg.error_code)
print('login respond  error_msg:'+lg.error_msg)

#### 获取公司业绩快报 ####
rs = bs.query_performance_express_report("sh.600000", start_date="2015-01-01", end_date="2017-12-31")
print('query_performance_express_report respond error_code:'+rs.error_code)
print('query_performance_express_report respond  error_msg:'+rs.error_msg)

result_list = []
while (rs.error_code == '0') & rs.next():
    result_list.append(rs.get_row_data())
    # 获取一条记录，将记录合并在一起
result = pd.DataFrame(result_list, columns=rs.fields)
#### 结果集输出到csv文件 ####
result.to_csv("D:\\performance_express_report.csv", encoding="gbk", index=False)
print(result)

#### 登出系统 ####
bs.logout()

```

参数含义：

* code：股票代码，sh或sz.+6位数字代码，或者指数代码，如：sh.601398。sh：上海；sz：深圳。此参数不可为空；
* start_date：开始日期，发布日期或更新日期在这个范围内；
* end_date：结束日期，发布日期或更新日期在这个范围内。

**说明：**

* 业绩快报属于自愿披露信息，除几种特殊情况外交易所未要求必须发布，因此并非每家公司、每个报告期都有记录；
* performanceExpUpdateDate 为该报告期快报的最新披露日；若快报被更正，可能晚于 performanceExpPubDate，同一报告期应以 performanceExpUpdateDate 最新的记录为准；
* 该接口返回的是**分页数据**，示例中 while (rs.error_code == '0') & rs.next() 循环会逐页自动读取直至结束，不可只调用一次 next() 就结束；
* 当指定区间内公司未发布业绩快报时，返回空结果集，error_code 仍为"0"；
* performanceExpressTotalAsset、performanceExpressNetAsset 单位为元；performanceExpressROEWa 为加权净资产收益率（%）。

返回示例数据

| code | performanceExpPubDate | performanceExpStatDate | performanceExpUpdateDate | performanceExpressTotalAsset | performanceExpressNetAsset |
|------------|------------|-------|------------|------------|-------|
| sh.600000 | 2015-01-06 | 2014-12-31 | 2015-01-06 | 4195602000000.000000 | 260011000000.000000 |
| sh.600000 | 2016-01-05 | 2015-12-31 | 2016-01-05 | 5043060000000.000000 | 285245000000.000000 |
| sh.600000 | 2017-01-04 | 2016-12-31 | 2017-01-04 | 5857263000000.000000 | 338027000000.000000 |

返回示例数据

| performanceExpressEPSChgPct | performanceExpressROEWa | performanceExpressEPSDiluted | performanceExpressGRYOY | performanceExpressOPYOY |
|------------|------------|-------|------------|------------|
| 0.326910 | 21.020000 | 2.520000 | 0.228390 | 0.153803 |
| 0.191493 | 18.820000 | 2.660000 | 0.192395 | 0.069764 |
| 0.115412 | 16.350000 | 2.400000 | 0.097234 | 0.054384 |

返回数据说明

| 参数名称 | 参数描述 |
|------------|------------|
| code | 证券代码 |
| performanceExpPubDate | 业绩快报披露日 |
| performanceExpStatDate | 业绩快报统计日期 |
| performanceExpUpdateDate | 业绩快报披露日(最新) |
| performanceExpressTotalAsset | 业绩快报总资产 |
| performanceExpressNetAsset | 业绩快报净资产 |
| performanceExpressEPSChgPct | 业绩每股收益增长率 |
| performanceExpressROEWa | 业绩快报净资产收益率ROE-加权 |
| performanceExpressEPSDiluted | 业绩快报每股收益EPS-摊薄 |
| performanceExpressGRYOY | 业绩快报营业总收入同比 |
| performanceExpressOPYOY | 业绩快报营业利润同比 |

### 季频公司业绩预告：query_forecast_report()

方法说明：通过API接口获取季频公司业绩预告信息，可以通过参数设置获取起止年份数据，提供2003年至今数据。除几种特殊情况外，交易所未要求必须发布。

返回类型：pandas的DataFrame类型。

使用示例

```py
import baostock as bs
import pandas as pd

#### 登陆系统 ####
lg = bs.login()
# 显示登陆返回信息
print('login respond error_code:'+lg.error_code)
print('login respond  error_msg:'+lg.error_msg)

#### 获取公司业绩预告 ####
rs_forecast = bs.query_forecast_report("sh.600000", start_date="2010-01-01", end_date="2017-12-31")
print('query_forecast_reprot respond error_code:'+rs_forecast.error_code)
print('query_forecast_reprot respond  error_msg:'+rs_forecast.error_msg)
rs_forecast_list = []
while (rs_forecast.error_code == '0') & rs_forecast.next():
    # 分页查询，将每页信息合并在一起
    rs_forecast_list.append(rs_forecast.get_row_data())
result_forecast = pd.DataFrame(rs_forecast_list, columns=rs_forecast.fields)
#### 结果集输出到csv文件 ####
result_forecast.to_csv("D:\\forecast_report.csv", encoding="gbk", index=False)
print(result_forecast)

#### 登出系统 ####
bs.logout()

```

参数含义：

* code：股票代码，sh或sz.+6位数字代码，或者指数代码，如：sh.601398。sh：上海；sz：深圳。此参数不可为空；
* start_date：开始日期，发布日期或更新日期在这个范围内；
* end_date：结束日期，发布日期或更新日期在这个范围内。

**说明：**

* profitForcastType 为交易所公告中的业绩预告类型原文，常见取值有：预增、略增、续盈、扭亏、首亏、续亏、预减、略减、不确定等，接口按公告原文返回，不限于上述列举，使用前不宜按固定枚举做强校验；
* profitForcastChgPctUp、profitForcastChgPctDwn 分别表示预告的净利润增长上限、下限（%）；公告未给出区间时，两者可能相同，或其中一个为 0.000000；
* 该接口返回的是**分页数据**，示例中 while (rs.error_code == '0') & rs.next() 循环会逐页自动读取直至结束，不可只调用一次 next() 就结束；
* 当指定区间内公司未发布业绩预告时，返回空结果集，error_code 仍为"0"。

返回示例数据

| code | profitForcastExpPubDate | profitForcastExpStatDate | profitForcastType | profitForcastAbstract |
|------------|------------|-------|------------|-------|
| sh.600000 | 2010-01-05 | 2009-12-31 | 略增 | 预计2009年归属于上市公司股东净利润1319500万元，同比增长5.43%。 |
| sh.600000 | 2011-01-05 | 2010-12-31 | 略增 | 预计公司2010年年度归属于上市公司股东净利润为190.76亿元，较上年同期增长44.33％。 |
| sh.600000 | 2012-01-05 | 2011-12-31 | 略增 | 预计2011年1月1日至2011年12月31日，归属于上市公司股东的净利润：盈利272.36亿元，与上年同期相比增加了42.02%。 |

返回示例数据

| profitForcastChgPctUp | profitForcastChgPctDwn |
|------------|------------|
| 5.430000 | 0.000000 |
| 44.330000 | 44.330000 |
| 42.020000 | 42.020000 |

返回数据说明

| 参数名称 | 参数描述 |
|------------|------------|
| code | 证券代码 |
| profitForcastExpPubDate | 业绩预告发布日期 |
| profitForcastExpStatDate | 业绩预告统计日期 |
| profitForcastType | 业绩预告类型 |
| profitForcastAbstract | 业绩预告摘要 |
| profitForcastChgPctUp | 预告归属于母公司的净利润增长上限(%) |
| profitForcastChgPctDwn | 预告归属于母公司的净利润增长下限(%) |

## 证券基本资料

### 证券基本资料：query_stock_basic()

方法说明：通过API接口获取证券基本资料，可以通过参数设置获取对应证券代码、证券名称的数据。
返回类型：pandas的DataFrame类型。
使用示例

```py
import baostock as bs
import pandas as pd

# 登陆系统
lg = bs.login()
# 显示登陆返回信息
print('login respond error_code:'+lg.error_code)
print('login respond  error_msg:'+lg.error_msg)

# 获取证券基本资料
rs = bs.query_stock_basic(code="sh.600000")
# rs = bs.query_stock_basic(code_name="浦发银行")  # 支持模糊查询
print('query_stock_basic respond error_code:'+rs.error_code)
print('query_stock_basic respond  error_msg:'+rs.error_msg)

# 打印结果集
data_list = []
while (rs.error_code == '0') & rs.next():
    # 获取一条记录，将记录合并在一起
    data_list.append(rs.get_row_data())
result = pd.DataFrame(data_list, columns=rs.fields)
# 结果集输出到csv文件
result.to_csv("D:/stock_basic.csv", encoding="gbk", index=False)
print(result)

# 登出系统
bs.logout()

```

参数含义：

* code：A股股票代码，sh或sz.+6位数字代码，或者指数代码，如：sh.601398。sh：上海；sz：深圳。可以为空；
* code_name：股票名称，支持模糊查询，可以为空。
* 当参数为空时，输出全部股票的基本信息。

**说明：**

* type 枚举：1：股票，2：指数，3：其它，4：可转债，5：ETF；status 枚举：1：上市，0：退市；
* outDate 为退市日期，未退市证券该字段返回空字符串；
* code_name 支持模糊查询，可能同时匹配多只证券（如"银行"会命中多只名称含"银行"的股票），返回多条记录，不可默认结果唯一；
* 参数为空时返回全部证券基本资料。

返回示例数据

| code | code_name | ipoDate | outDate | type | status |
|------------|------------|-------|------------|------------|-------|
| sh.600000 | 浦发银行 | 1999-11-10 |  | 1 | 1 |

返回数据说明

| 参数名称 | 参数描述 |
|------------|------------|
| code | 证券代码 |
| code_name | 证券名称 |
| ipoDate | 上市日期 |
| outDate | 退市日期 |
| type | 证券类型，其中1：股票，2：指数，3：其它，4：可转债，5：ETF |
| status | 上市状态，其中1：上市，0：退市 |

## 获取证券元信息

### 交易日查询：query_trade_dates()

方法说明：通过API接口获取股票交易日信息，可以通过参数设置获取起止年份数据，提供上交所1990-今年数据。
返回类型：pandas的DataFrame类型。
使用示例

```py
import baostock as bs
import pandas as pd

#### 登陆系统 ####
lg = bs.login()
# 显示登陆返回信息
print('login respond error_code:'+lg.error_code)
print('login respond  error_msg:'+lg.error_msg)

#### 获取交易日信息 ####
rs = bs.query_trade_dates(start_date="2017-01-01", end_date="2017-06-30")
print('query_trade_dates respond error_code:'+rs.error_code)
print('query_trade_dates respond  error_msg:'+rs.error_msg)

#### 打印结果集 ####
data_list = []
while (rs.error_code == '0') & rs.next():
    # 获取一条记录，将记录合并在一起
    data_list.append(rs.get_row_data())
result = pd.DataFrame(data_list, columns=rs.fields)

#### 结果集输出到csv文件 ####
result.to_csv("D:\\trade_datas.csv", encoding="gbk", index=False)
print(result)

#### 登出系统 ####
bs.logout()

```

参数含义：

* start_date：查询交易日的开始日期；
* end_date：查询交易日的截止日期。

**说明：**

* 返回区间内**每一个自然日**（含周末、法定节假日），而非仅交易日，需通过 is_trading_day 字段判断是否交易日；
* 数据范围为上交所1990年至今年，超出范围的日期不返回记录；start_date 为空时默认取2015-01-01，查询更早年份须显式传入；

返回示例数据

| calendar_date | is_trading_day |
|------------|------------|
| 2024-01-01 | 0 |
| 2024-01-02 | 1 |
| 2024-01-03 | 1 |

返回数据说明

| 参数名称 | 参数描述 |
|------------|------------|
| calendar_date | 日期 |
| is_trading_day | 是否交易日，其中0：非交易日，1：交易日 |

### 证券代码查询：query_all_stock()

方法说明：获取指定交易日期所有股票列表。通过API接口获取证券代码及股票交易状态信息，与日K线数据同时更新。可以通过参数‘某交易日’获取数据（包括：A股、指数），数据范围同接口query_history_k_data_plus()。

返回类型：pandas的DataFrame类型。

更新时间：与日K线同时更新。

使用示例

```py
import baostock as bs
import pandas as pd

#### 登陆系统 ####
lg = bs.login()
# 显示登陆返回信息
print('login respond error_code:'+lg.error_code)
print('login respond  error_msg:'+lg.error_msg)

#### 获取某日所有证券信息 ####
rs = bs.query_all_stock(day="2024-10-25")  #当参数“day”为空时，默认取当天日期。闭市后日K线数据更新，该接口才会返回当天数据，否则返回空。
print('query_all_stock respond error_code:'+rs.error_code)
print('query_all_stock respond  error_msg:'+rs.error_msg)

#### 打印结果集 ####
data_list = []
while (rs.error_code == '0') & rs.next():
    # 获取一条记录，将记录合并在一起
    data_list.append(rs.get_row_data())
result = pd.DataFrame(data_list, columns=rs.fields)

#### 结果集输出到csv文件 ####
result.to_csv("D:\\all_stock.csv", encoding="gbk", index=False)
print(result)

#### 登出系统 ####
bs.logout()

```

参数含义：

* day：有值：获取指定交易日沪深市场的所有证券信息；为空时默认取当天沪深市场的所有证券信息。

**说明：**

* 该接口返回指定交易日的全部证券列表（含A股、指数），数据范围同 query_history_k_data_plus()，更新时间与日K线一致（闭市后更新）；指定当天且日K数据尚未更新时，返回空结果集，error_code 仍为"0"；
* 非交易日（周末、节假日）没有日K数据，day 为非交易日时同样返回空结果集；
* tradeStatus 枚举：1：正常交易，0：停牌；

返回示例数据

| code | tradeStatus | code_name |
|------------|------------|-------|
| sh.600000 | 1 | 浦发银行 |
| sh.600423 | 0 | \*ST柳化 |
| sz.000001 | 1 | 平安银行 |

返回数据说明

| 参数名称 | 参数描述 |
|------------|------------|
| code | 证券代码 |
| tradeStatus | 交易状态，其中1：正常交易，0：停牌 |
| code_name | 证券名称 |

## 宏观经济数据

### 存款利率：query_deposit_rate_data()

方法说明：通过API接口获取存款利率，可以通过参数设置获取对应起止日期的数据。
返回类型：pandas的DataFrame类型。
使用示例

```py
import baostock as bs
import pandas as pd

# 登陆系统
lg = bs.login()
# 显示登陆返回信息
print('login respond error_code:'+lg.error_code)
print('login respond  error_msg:'+lg.error_msg)

# 获取存款利率
rs = bs.query_deposit_rate_data(start_date="2015-01-01", end_date="2015-12-31")
print('query_deposit_rate_data respond error_code:'+rs.error_code)
print('query_deposit_rate_data respond  error_msg:'+rs.error_msg)

# 打印结果集
data_list = []
while (rs.error_code == '0') & rs.next():
    # 获取一条记录，将记录合并在一起
    data_list.append(rs.get_row_data())
result = pd.DataFrame(data_list, columns=rs.fields)
# 结果集输出到csv文件
result.to_csv("D:/deposit_rate.csv", encoding="gbk", index=False)
print(result)

# 登出系统
bs.logout()

```

参数含义：

* start_date：开始日期，格式XXXX-XX-XX，发布日期在这个范围内，可以为空；
* end_date：结束日期，格式XXXX-XX-XX，发布日期在这个范围内，可以为空。

**说明：**

* **数据仅更新至2015年**：央行自2015年10月起不再公布存款基准利率（利率市场化后改由 LPR 报价机制形成），本接口无2015年之后的新增数据，查询2016年及以后的日期区间返回空结果集；
* 各利率字段单位均为**年化百分比（%）**，如 0.350000 表示 0.35%，如需小数形式参与计算应除以100；
* 数据为每次利率调整后的一条记录，按发布日期（pubDate）升序返回；
* 某期限品种当次调整未公布时返回空字符串（如示例中 fixedDepositRate5Year、installmentFixedDepositRate5Year），属正常情况，需做空值判断；
* start_date、end_date 可以为空，为空时不限制该侧日期范围；结果集为分页数据，需用 while 循环逐页读取。

返回示例数据

| pubDate | demandDepositRate | fixedDepositRate3Month | fixedDepositRate6Month | fixedDepositRate1Year | fixedDepositRate2Year | fixedDepositRate3Year |
|------------|------------|-------|------------|------------|-------|------------|
| 2015-03-01 | 0.350000 | 2.100000 | 2.300000 | 2.500000 | 3.100000 | 3.750000 |
| 2015-05-11 | 0.350000 | 1.850000 | 2.050000 | 2.250000 | 2.850000 | 3.500000 |

返回示例数据

| fixedDepositRate5Year | installmentFixedDepositRate1Year | installmentFixedDepositRate3Year | installmentFixedDepositRate5Year |
|------------|------------|-------|------------|
|  | 2.100000 | 2.300000 |  |
|  | 1.850000 | 2.050000 |  |

返回数据说明

| 参数名称 | 参数描述 |
|------------|------------|
| pubDate | 发布日期 |
| demandDepositRate | 活期存款(不定期) |
| fixedDepositRate3Month | 定期存款(三个月) |
| fixedDepositRate6Month | 定期存款(半年) |
| fixedDepositRate1Year | 定期存款整存整取(一年) |
| fixedDepositRate2Year | 定期存款整存整取(二年) |
| fixedDepositRate3Year | 定期存款整存整取(三年) |
| fixedDepositRate5Year | 定期存款整存整取(五年) |
| installmentFixedDepositRate1Year | 零存整取、整存零取、存本取息定期存款(一年) |
| installmentFixedDepositRate3Year | 零存整取、整存零取、存本取息定期存款(三年) |
| installmentFixedDepositRate5Year | 零存整取、整存零取、存本取息定期存款(五年) |

### 贷款利率：query_loan_rate_data()

方法说明：通过API接口获取贷款利率，可以通过参数设置获取对应起止日期的数据。
返回类型：pandas的DataFrame类型。
使用示例

```py
import baostock as bs
import pandas as pd

# 登陆系统
lg = bs.login()
# 显示登陆返回信息
print('login respond error_code:'+lg.error_code)
print('login respond  error_msg:'+lg.error_msg)

# 获取贷款利率
rs = bs.query_loan_rate_data(start_date="2010-01-01", end_date="2015-12-31")
print('query_loan_rate_data respond error_code:'+rs.error_code)
print('query_loan_rate_data respond  error_msg:'+rs.error_msg)

# 打印结果集
data_list = []
while (rs.error_code == '0') & rs.next():
    # 获取一条记录，将记录合并在一起
    data_list.append(rs.get_row_data())
result = pd.DataFrame(data_list, columns=rs.fields)
# 结果集输出到csv文件
result.to_csv("D:/loan_rate.csv", encoding="gbk", index=False)
print(result)

# 登出系统
bs.logout()

```

参数含义：

* start_date：开始日期，格式XXXX-XX-XX，发布日期在这个范围内，可以为空；
* end_date：结束日期，格式XXXX-XX-XX，发布日期在这个范围内，可以为空。

**说明：**

* **数据仅更新至2015年**：央行自2015年10月起不再公布贷款基准利率，贷款利率改由 LPR（贷款市场报价利率）报价形成，本接口无2015年之后的新增数据，查询2016年及以后的日期区间返回空结果集；
* 各利率字段单位均为**年化百分比（%）**，如 5.100000 表示 5.10%，如需小数形式参与计算应除以100；
* 数据为每次利率调整后的一条记录，按发布日期（pubDate）升序返回；
* 某期限品种当次调整未公布时返回空字符串，属正常情况，需做空值判断；
* start_date、end_date 可以为空，为空时不限制该侧日期范围。

返回示例数据

| pubDate | loanRate6Month | loanRate6MonthTo1Year | loanRate1YearTo3Year | loanRate3YearTo5Year |
|------------|------------|-------|------------|------------|
| 2010-10-20 | 5.100000 | 5.560000 | 5.600000 | 5.960000 |
| 2010-12-26 | 5.350000 | 5.810000 | 5.850000 | 6.220000 |

返回示例数据

| loanRateAbove5Year | mortgateRateBelow5Year | mortgateRateAbove5Year |
|------------|------------|-------|
| 6.140000 | 3.500000 | 4.050000 |
| 6.400000 | 3.750000 | 4.300000 |

返回数据说明

| 参数名称 | 参数描述 |
|------------|------------|
| pubDate | 发布日期 |
| loanRate6Month | 6个月贷款利率 |
| loanRate6MonthTo1Year | 6个月至1年贷款利率 |
| loanRate1YearTo3Year | 1年至3年贷款利率 |
| loanRate3YearTo5Year | 3年至5年贷款利率 |
| loanRateAbove5Year | 5年以上贷款利率 |
| mortgateRateBelow5Year | 5年以下住房公积金贷款利率 |
| mortgateRateAbove5Year | 5年以上住房公积金贷款利率 |

### 存款准备金率：query_required_reserve_ratio_data()

方法说明：通过API接口获取存款准备金率，可以通过参数设置获取对应起止日期的数据。
返回类型：pandas的DataFrame类型。
使用示例

```py
import baostock as bs
import pandas as pd

# 登陆系统
lg = bs.login()
# 显示登陆返回信息
print('login respond error_code:'+lg.error_code)
print('login respond  error_msg:'+lg.error_msg)

# 获取存款准备金率
rs = bs.query_required_reserve_ratio_data(start_date="2010-01-01", end_date="2015-12-31")
print('query_required_reserve_ratio_data respond error_code:'+rs.error_code)
print('query_required_reserve_ratio_data respond  error_msg:'+rs.error_msg)

# 打印结果集
data_list = []
while (rs.error_code == '0') & rs.next():
    # 获取一条记录，将记录合并在一起
    data_list.append(rs.get_row_data())
result = pd.DataFrame(data_list, columns=rs.fields)
# 结果集输出到csv文件
result.to_csv("D:/required_reserve_ratio.csv", encoding="gbk", index=False)
print(result)

# 登出系统
bs.logout()

```

参数含义：

* start_date：开始日期，格式XXXX-XX-XX，发布日期在这个范围内，可以为空；
* end_date：结束日期，格式XXXX-XX-XX，发布日期在这个范围内，可以为空；
* yearType:年份类别，默认为0，查询公告日期；1查询生效日期。

**说明：**

* yearType 枚举：0：按公告日期（pubDate）筛选；1：按生效日期（effectiveDate）筛选。start_date、end_date 的过滤对象随 yearType 变化；
* 各准备金率字段单位均为**百分比（%）**，如 15.5 表示 15.5%；
* Pre 为调整前、After 为调整后，同一条记录中的调整后值通常等于下一次调整的调整前值，可据此校验数据连续性；
* start_date、end_date 可以为空，为空时不限制该侧日期范围。

返回示例数据

| pubDate | effectiveDate | bigInstitutionsRatioPre | bigInstitutionsRatioAfter |
|------------|------------|-------|------------|
| 2010-01-12 | 2010-01-18 | 15.5 | 16.0 |
| 2010-02-12 | 2010-02-25 | 16.0 | 16.5 |

返回示例数据

| mediumInstitutionsRatioPre | mediumInstitutionsRatioAfter |
|------------|------------|
| 13.5 | 14.0 |
| 14.0 | 14.5 |

返回数据说明

| 参数名称 | 参数描述 |
|------------|------------|
| pubDate | 公告日期 |
| effectiveDate | 生效日期 |
| bigInstitutionsRatioPre | 人民币存款准备金率：大型存款类金融机构 调整前，单位：% |
| bigInstitutionsRatioAfter | 人民币存款准备金率：大型存款类金融机构 调整后，单位：% |
| mediumInstitutionsRatioPre | 人民币存款准备金率：中小型存款类金融机构 调整前，单位：% |
| mediumInstitutionsRatioAfter | 人民币存款准备金率：中小型存款类金融机构 调整后，单位：% |

### 货币供应量：query_money_supply_data_month()

方法说明：通过API接口获取货币供应量，可以通过参数设置获取对应起止日期的数据。
返回类型：pandas的DataFrame类型。
使用示例

```py
import baostock as bs
import pandas as pd

# 登陆系统
lg = bs.login()
# 显示登陆返回信息
print('login respond error_code:'+lg.error_code)
print('login respond  error_msg:'+lg.error_msg)

# 获取货币供应量
rs = bs.query_money_supply_data_month(start_date="2010-01", end_date="2015-12")
print('query_money_supply_data_month respond error_code:'+rs.error_code)
print('query_money_supply_data_month respond  error_msg:'+rs.error_msg)

# 打印结果集
data_list = []
while (rs.error_code == '0') & rs.next():
    # 获取一条记录，将记录合并在一起
    data_list.append(rs.get_row_data())
result = pd.DataFrame(data_list, columns=rs.fields)
# 结果集输出到csv文件
result.to_csv("D:/money_supply_data_month.csv", encoding="gbk", index=False)
print(result)

# 登出系统
bs.logout()

```

参数含义：

* start_date：开始日期，格式XXXX-XX，发布日期在这个范围内，可以为空；
* end_date：结束日期，格式XXXX-XX，发布日期在这个范围内，可以为空。

**说明：**

* m0Month、m1Month、m2Month 单位为**亿元**，表示当月末货币供应量余额；m0YOY、m1YOY、m2YOY 为同比增长率（%），m0ChainRelative、m1ChainRelative、m2ChainRelative 为环比增长率（%）；
* statMonth 为月份数字字符串（"01"—"12"），需与 statYear 组合才能确定具体月份，不能单独作为日期使用；
* start_date、end_date 格式为"YYYY-MM"，按发布日期筛选，可以为空，为空时不限制该侧范围；

返回示例数据

| statYear | statMonth | m0Month | m0YOY | m0ChainRelative | m1Month | m1YOY | m1ChainRelative |
|------------|------------|-------|------------|------------|-------|------------|------------|
| 2010 | 01 | 40758.580000 | —0.790000 | 6.566809 | 229588.980000 | 38.960000 | 3.677276 |
| 2010 | 02 | 42865.790000 | 21.980000 | 5.169979 | 224286.950000 | 34.990000 | —2.309357 |

返回示例数据

| m2Month | m2YOY | m2ChainRelative |
|------------|------------|-------|
| 625609.290000 | 25.980000 | 2.521165 |
| 636072.260000 | 25.520000 | 1.672445 |

返回数据说明

| 参数名称 | 参数描述 |
|------------|------------|
| statYear | 统计年度 |
| statMonth | 统计月份 |
| m0Month | 货币供应量M0（月） |
| m0YOY | 货币供应量M0（同比），单位：% |
| m0ChainRelative | 货币供应量M0（环比），单位：% |
| m1Month | 货币供应量M1（月） |
| m1YOY | 货币供应量M1（同比），单位：% |
| m1ChainRelative | 货币供应量M1（环比），单位：% |
| m2Month | 货币供应量M2（月） |
| m2YOY | 货币供应量M2（同比），单位：% |
| m2ChainRelative | 货币供应量M2（环比），单位：% |

### 货币供应量(年底余额)：query_money_supply_data_year()

方法说明：通过API接口获取货币供应量(年底余额)，可以通过参数设置获取对应起止日期的数据。
返回类型：pandas的DataFrame类型。
使用示例

```py
import baostock as bs
import pandas as pd

# 登陆系统
lg = bs.login()
# 显示登陆返回信息
print('login respond error_code:'+lg.error_code)
print('login respond  error_msg:'+lg.error_msg)

# 获取货币供应量(年底余额)
rs = bs.query_money_supply_data_year(start_date="2010", end_date="2015")
print('query_money_supply_data_year respond error_code:'+rs.error_code)
print('query_money_supply_data_year respond  error_msg:'+rs.error_msg)

# 打印结果集
data_list = []
while (rs.error_code == '0') & rs.next():
    # 获取一条记录，将记录合并在一起
    data_list.append(rs.get_row_data())
result = pd.DataFrame(data_list, columns=rs.fields)
# 结果集输出到csv文件
result.to_csv("D:/money_supply_data_year.csv", encoding="gbk", index=False)
print(result)

# 登出系统
bs.logout()

```

参数含义：

* start_date：开始日期，格式XXXX，发布日期在这个范围内，可以为空；
* end_date：结束日期，格式XXXX，发布日期在这个范围内，可以为空。

**说明：**

* m0Year、m1Year、m2Year 单位为**亿元**，表示年末货币供应量余额；m0YearYOY、m1YearYOY、m2YearYOY 为同比增长率（%）；
* statYear 为统计年度，start_date、end_date 格式为"YYYY"，按发布日期筛选，可以为空，为空时不限制该侧范围；

返回示例数据

| statYear | m0Year | m0YearYOY | m1Year | m1YearYOY | m2Year | m2YearYOY |
|------------|------------|-------|------------|------------|-------|------------|
| 2010 | 44628.170000 | 16.700000 | 266621.540000 | 21.200000 | 725851.800000 | 19.700000 |
| 2011 | 50748.460000 | 13.760000 | 289847.700000 | 7.850000 | 851590.900000 | 13.610000 |

返回数据说明

| 参数名称 | 参数描述 |
|------------|------------|
| statYear | 统计年度 |
| m0Year | 年货币供应量M0（亿元） |
| m0YearYOY | 年货币供应量M0（同比） |
| m1Year | 年货币供应量M1（亿元） |
| m1YearYOY | 年货币供应量M1（同比） |
| m2Year | 年货币供应量M2（亿元） |
| m2YearYOY | 年货币供应量M2（同比） |

## 板块数据

### 行业分类：query_stock_industry()

方法说明：通过API接口获取行业分类信息，更新频率：每周一更新。返回类型：pandas的DataFrame类型。 使用示例

```py
import baostock as bs
import pandas as pd

# 登陆系统
lg = bs.login()
# 显示登陆返回信息
print('login respond error_code:'+lg.error_code)
print('login respond  error_msg:'+lg.error_msg)

# 获取行业分类数据
rs = bs.query_stock_industry()
# rs = bs.query_stock_basic(code_name="浦发银行")
print('query_stock_industry error_code:'+rs.error_code)
print('query_stock_industry respond  error_msg:'+rs.error_msg)

# 打印结果集
industry_list = []
while (rs.error_code == '0') & rs.next():
    # 获取一条记录，将记录合并在一起
    industry_list.append(rs.get_row_data())
result = pd.DataFrame(industry_list, columns=rs.fields)
# 结果集输出到csv文件
result.to_csv("D:/stock_industry.csv", encoding="gbk", index=False)
print(result)

# 登出系统
bs.logout()

```

参数含义：

* code：A股股票代码，sh或sz.+6位数字代码，或者指数代码，如：sh.601398。sh：上海；sz：深圳。可以为空；
* date：查询日期，格式XXXX-XX-XX，为空时默认最新日期。

**说明：**

* industryClassification 表示行业分类标准，常见取值为"申万一级行业""证监会行业分类"；不同分类标准下 industry 字段的行业名称/代码格式不同（如证监会行业分类为"J66货币金融服务"，申万一级行业为"银行"），使用前应先确认返回的分类标准，不可将两种标准的行业名称混用；
* industry 字段可能为空字符串（如该证券暂无行业分类数据或已退市），属正常情况，需做空值判断；
* 行业分类数据每周一更新，date 为空时返回最新一期数据；
* 该接口一次返回全部股票。

返回示例数据

| updateDate | code | code_name | industry | industryClassification |
|------------|------------|-------|------------|------------|
| 2018-11-26 | sh.600000 | 浦发银行 | J66货币金融服务 | 证监会行业分类 |
| 2018-11-26 | sh.600001 | 邯郸钢铁 |  | 证监会行业分类 |

返回数据说明

| 参数名称 | 参数描述 |
|------------|------------|
| updateDate | 更新日期 |
| code | 证券代码 |
| code_name | 证券名称 |
| industry | 所属行业 |
| industryClassification | 所属行业类别 |

### 上证50成分股：query_sz50_stocks()

方法说明：通过API接口获取上证50成分股信息，更新频率：每周一更新。返回类型：pandas的DataFrame类型。 使用示例

```py
import baostock as bs
import pandas as pd

# 登陆系统
lg = bs.login()
# 显示登陆返回信息
print('login respond error_code:'+lg.error_code)
print('login respond  error_msg:'+lg.error_msg)

# 获取上证50成分股
rs = bs.query_sz50_stocks()
print('query_sz50 error_code:'+rs.error_code)
print('query_sz50  error_msg:'+rs.error_msg)

# 打印结果集
sz50_stocks = []
while (rs.error_code == '0') & rs.next():
    # 获取一条记录，将记录合并在一起
    sz50_stocks.append(rs.get_row_data())
result = pd.DataFrame(sz50_stocks, columns=rs.fields)
# 结果集输出到csv文件
result.to_csv("D:/sz50_stocks.csv", encoding="gbk", index=False)
print(result)

# 登出系统
bs.logout()

```

参数含义：

* date：查询日期，格式XXXX-XX-XX，为空时默认最新日期。

**说明：**

* 成分股名单**会随指数调整而变化**，date 为空时返回最新一期成分股，传入历史日期时返回该日期所在更新周期（每周一更新）的成分股快照；
* 不同日期的成分股名单不可直接合并使用，如需构建历史成分股序列，应按日期逐期获取并保留 updateDate，用于规避幸存者偏差；
* 若指定日期早于数据起始时间或该期无数据，返回空结果集，error_code 仍为"0"；

返回示例数据

| updateDate | code | code_name |
|------------|------------|-------|
| 2018-11-26 | sh.600000 | 浦发银行 |
| 2018-11-26 | sh.600016 | 民生银行 |

返回数据说明

| 参数名称 | 参数描述 |
|------------|------------|
| updateDate | 更新日期 |
| code | 证券代码 |
| code_name | 证券名称 |

### 沪深300成分股：query_hs300_stocks()

方法说明：通过API接口获取沪深300成分股信息，更新频率：每周一更新。返回类型：pandas的DataFrame类型。 使用示例

```py
import baostock as bs
import pandas as pd

# 登陆系统
lg = bs.login()
# 显示登陆返回信息
print('login respond error_code:'+lg.error_code)
print('login respond  error_msg:'+lg.error_msg)

# 获取沪深300成分股
rs = bs.query_hs300_stocks()
print('query_hs300 error_code:'+rs.error_code)
print('query_hs300  error_msg:'+rs.error_msg)

# 打印结果集
hs300_stocks = []
while (rs.error_code == '0') & rs.next():
    # 获取一条记录，将记录合并在一起
    hs300_stocks.append(rs.get_row_data())
result = pd.DataFrame(hs300_stocks, columns=rs.fields)
# 结果集输出到csv文件
result.to_csv("D:/hs300_stocks.csv", encoding="gbk", index=False)
print(result)

# 登出系统
bs.logout()

```

参数含义：

* date：查询日期，格式XXXX-XX-XX，为空时默认最新日期。

**说明：**

* 成分股名单**会随指数调整而变化**，date 为空时返回最新一期成分股，传入历史日期时返回该日期所在更新周期（每周一更新）的成分股快照；
* 不同日期的成分股名单不可直接合并使用，如需构建历史成分股序列，应按日期逐期获取并保留 updateDate，用于规避幸存者偏差；
* 若指定日期早于数据起始时间或该期无数据，返回空结果集，error_code 仍为"0"；

返回示例数据

| updateDate | code | code_name |
|------------|------------|-------|
| 2018-11-26 | sh.600000 | 浦发银行 |
| 2018-11-26 | sh.600008 | 首创股份 |

返回数据说明

| 参数名称 | 参数描述 |
|------------|------------|
| updateDate | 更新日期 |
| code | 证券代码 |
| code_name | 证券名称 |

### 中证500成分股：query_zz500_stocks()

方法说明：通过API接口获取中证500成分股信息，更新频率：每周一更新。返回类型：pandas的DataFrame类型。 使用示例

```py
import baostock as bs
import pandas as pd

# 登陆系统
lg = bs.login()
# 显示登陆返回信息
print('login respond error_code:'+lg.error_code)
print('login respond  error_msg:'+lg.error_msg)

# 获取中证500成分股
rs = bs.query_zz500_stocks()
print('query_zz500 error_code:'+rs.error_code)
print('query_zz500  error_msg:'+rs.error_msg)

# 打印结果集
zz500_stocks = []
while (rs.error_code == '0') & rs.next():
    # 获取一条记录，将记录合并在一起
    zz500_stocks.append(rs.get_row_data())
result = pd.DataFrame(zz500_stocks, columns=rs.fields)
# 结果集输出到csv文件
result.to_csv("D:/zz500_stocks.csv", encoding="gbk", index=False)
print(result)

# 登出系统
bs.logout()

```

参数含义：

* date：查询日期，格式XXXX-XX-XX，为空时默认最新日期。

**说明：**

* 成分股名单**会随指数调整而变化**，date 为空时返回最新一期成分股，传入历史日期时返回该日期所在更新周期（每周一更新）的成分股快照；
* 不同日期的成分股名单不可直接合并使用，如需构建历史成分股序列，应按日期逐期获取并保留 updateDate，用于规避幸存者偏差；
* 若指定日期早于数据起始时间或该期无数据，返回空结果集，error_code 仍为"0"；

返回示例数据

| updateDate | code | code_name |
|------------|------------|-------|
| 2018-11-26 | sh.600004 | 白云机场 |
| 2018-11-26 | sh.600006 | 东风汽车 |

返回数据说明

| 参数名称 | 参数描述 |
|------------|------------|
| updateDate | 更新日期 |
| code | 证券代码 |
| code_name | 证券名称 |

## 示例程序

### 获取指定日期全部股票的日K线数据

示例代码如下：

```py
import baostock as bs
import pandas as pd

def download_data(date):
    bs.login()

    # 获取指定日期的指数、股票数据
    stock_rs = bs.query_all_stock(date)
    stock_df = stock_rs.get_data()
    data_df = pd.DataFrame()
    for code in stock_df["code"]:
        print("Downloading :" + code)
        k_rs = bs.query_history_k_data_plus(code, "date,code,open,high,low,close", date, date)
        data_df = data_df.append(k_rs.get_data())
    bs.logout()
    data_df.to_csv("D:\\demo_assignDayData.csv", encoding="gbk", index=False)
    print(data_df)

if __name__ == '__main__':
    # 获取指定日期全部股票的日K线数据
    download_data("2019-02-25")
```