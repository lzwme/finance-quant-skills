## 季频业绩预告

### 季频公司业绩预告：query_forecast_report()

方法说明：通过API接口获取季频公司业绩预告信息，可以通过参数设置获取起止年份数据，提供2003年至今数据。除几种特殊情况外，交易所未要求必须发布。

返回类型：pandas的DataFrame类型。

使用示例

  ```python
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

返回示例数据

| code                          | profitForcastExpPubDate  | profitForcastExpStatDate  | profitForcastType  | profitForcastAbstract
-------------------------------|---|---|---|---
 sh.600000                     | 2010-01-05  | 2009-12-31  | 略增  | 预计2009年归属于上市公司股东净利润1319500万元，同比增长5.43%。
 sh.600000                     | 2011-01-05  | 2010-12-31  | 略增  | 预计公司2010年年度归属于上市公司股东净利润为190.76亿元，较上年同期增长44.33％。
 sh.600000                     | 2012-01-05  | 2011-12-31  | 略增  | 预计2011年1月1日至2011年12月31日，归属于上市公司股东的净利润：盈利272.36亿元，与上年同期相比增加了42.02%。

返回示例数据

| profitForcastChgPctUp    | profitForcastChgPctDwn
 --------------------------|---
 5.430000                 | 0.000000
 44.330000                | 44.330000
 42.020000                | 42.020000

返回数据说明

|  参数名称                    | 参数描述
 --------------------------|---
 code                     | 证券代码
 profitForcastExpPubDate  | 业绩预告发布日期
 profitForcastExpStatDate | 业绩预告统计日期
 profitForcastType        | 业绩预告类型
 profitForcastAbstract    | 业绩预告摘要
 profitForcastChgPctUp    | 预告归属于母公司的净利润增长上限(%)
 profitForcastChgPctDwn   | 预告归属于母公司的净利润增长下限(%)