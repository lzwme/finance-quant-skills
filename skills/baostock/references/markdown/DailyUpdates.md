### 每日更新

## 目录

* [1 获取每日数据](#获取每日数据)
  + [1.1 获取某日所有股票日K线数据：query_daily_history_k_AStock()](#query_daily_history_k_AStock)
  + [1.2 获取某日所有ETF日K线数据：query_daily_history_k_ETF](#query_daily_history_k_ETF)
  + [1.3 获取某日复权因子信息：query_daily_adjust_factor](#query_daily_adjust_factor)

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