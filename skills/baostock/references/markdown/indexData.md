## 指数数据

通过API接口获取指数(综合指数、规模指数、一级行业指数、二级行业指数、策略指数、成长指数、价值指数、主题指数)K线数据。

     1. 综合指数，例如：sh.000001 上证指数，sz.399106 深证综指 等；
     2. 规模指数，例如：sh.000016 上证50，sh.000300 沪深300，sh.000905 中证500，sz.399001 深证成指等；
     3. 一级行业指数，例如：sh.000037 上证医药，sz.399433 国证交运 等；
     4. 二级行业指数，例如：sh.000952 300地产，sz.399951 300银行 等；
     5. 策略指数，例如：sh.000050 50等权，sh.000982 500等权 等；
     6. 成长指数，例如：sz.399376 小盘成长 等；
     7. 价值指数，例如：sh.000029 180价值 等；
     8. 主题指数，例如：sh.000015 红利指数，sh.000063 上证周期 等；
     9. 基金指数，例如：sh.000011 上证基金指数 等；
     10. 债券指数，例如：sh.000012 上证国债指数 等；

## 沪深指数K线数据 示例

指数未提供分钟线数据。示例数据：[下载](https://www.baostock.com/helpdocs/csv/history_Index_k_data.xlsx)

```python
    import baostock as bs
    import pandas as pd

    # 登陆系统
    lg = bs.login()
    # 显示登陆返回信息
    print('login respond error_code:'+lg.error_code)
    print('login respond  error_msg:'+lg.error_msg)

    # 获取指数(综合指数、规模指数、一级行业指数、二级行业指数、策略指数、成长指数、价值指数、主题指数)K线数据
    # 综合指数，例如：sh.000001 上证指数，sz.399106 深证综指 等；
    # 规模指数，例如：sh.000016 上证50，sh.000300 沪深300，sh.000905 中证500，sz.399001 深证成指等；
    # 一级行业指数，例如：sh.000037 上证医药，sz.399433 国证交运 等；
    # 二级行业指数，例如：sh.000952 300地产，sz.399951 300银行 等；
    # 策略指数，例如：sh.000050 50等权，sh.000982 500等权 等；
    # 成长指数，例如：sz.399376 小盘成长 等；
    # 价值指数，例如：sh.000029 180价值 等；
    # 主题指数，例如：sh.000015 红利指数，sh.000063 上证周期 等；

    # 详细指标参数，参见“历史行情指标参数”章节；“周月线”参数与“日线”参数不同。
    # 周月线指标：date,code,open,high,low,close,volume,amount,adjustflag,turn,pctChg
    rs = bs.query_history_k_data_plus("sh.000001",
        "date,code,open,high,low,close,preclose,volume,amount,pctChg",
        start_date='2017-01-01', end_date='2017-06-30', frequency="d")
    print('query_history_k_data_plus respond error_code:'+rs.error_code)
    print('query_history_k_data_plus respond  error_msg:'+rs.error_msg)

    # 打印结果集
    data_list = []
    while (rs.error_code == '0') & rs.next():
        # 获取一条记录，将记录合并在一起
        data_list.append(rs.get_row_data())
    result = pd.DataFrame(data_list, columns=rs.fields)
    # 结果集输出到csv文件
    result.to_csv("D:\\history_Index_k_data.csv", index=False)
    print(result)

    # 登出系统
    bs.logout()

```
参数含义：

  * code：股票代码，sh或sz.+6位数字代码，或者指数代码，如：sh.601398。sh：上海；sz：深圳。此参数不可为空；
  * fields：指示简称，支持多指标输入，以半角逗号分隔，填写内容作为返回类型的列。**详细指标列表见历史行情指标参数章节** 。此参数不可为空；
  * start：开始日期（包含），格式“YYYY-MM-DD”，为空时取2015-01-01；
  * end：结束日期（不包含），格式“YYYY-MM-DD”，为空时取最近一个交易日；
  * frequency：数据类型，默认为d，日k线；d=日k线、w=周、m=月、5=5分钟、15=15分钟、30=30分钟、60=60分钟k线数据，不区分大小写；指数没有分钟线数据；周线每周最后一个交易日才可以获取，月线第月最后一个交易日才可以获取。

返回示例数据

|date  | code  | open  | high  | low  | close  | preclose  | volume  | amount  | pctChg
---|---|---|---|---|---|---|---|---|---
2017-01-03  | sh.000001  | 3105.3080  | 3136.4550  | 3105.3080  | 3135.9200  | 3103.6370  | 14156718592  | 159887138816.0000  | 1.040200
2017-01-04  | sh.000001  | 3133.7870  | 3160.1020  | 3130.1140  | 3158.7940  | 3135.9200  | 16786085120  | 195914293248.0000  | 0.729400

返回数据说明

|参数名称  | 参数描述  | 说明
---|---|---
date  | 交易所行情日期  | 格式：YYYY-MM-DD
code  | 证券代码  | 格式：sh.600000。sh：上海，sz：深圳
open  | 今开盘价格  | 精度：小数点后4位；单位：人民币元
high  | 最高价  | 精度：小数点后4位；单位：人民币元
low  | 最低价  | 精度：小数点后4位；单位：人民币元
close  | 今收盘价  | 精度：小数点后4位；单位：人民币元
preclose  | 昨日收盘价  | 精度：小数点后4位；单位：人民币元
volume  | 成交数量  | 单位：股
amount  | 成交金额  | 精度：小数点后4位；单位：人民币元
pctChg  | 涨跌幅  | 精度：小数点后6位