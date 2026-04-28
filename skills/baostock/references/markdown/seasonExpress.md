## 季频业绩快报

### 季频公司业绩快报：query_performance_express_report()

方法说明：通过API接口获取季频公司业绩快报信息，可以通过参数设置获取起止年份数据，提供2006年至今数据。除几种特殊情况外，交易所未要求必须发布。

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

返回示例数据

| code                                | performanceExpPubDate  | performanceExpStatDate  | performanceExpUpdateDate  | performanceExpressTotalAsset  | performanceExpressNetAsset
-------------------------------------|---|---|---|---|---
 sh.600000                           | 2015-01-06  | 2014-12-31  | 2015-01-06  | 4195602000000.000000  | 260011000000.000000
 sh.600000                           | 2016-01-05  | 2015-12-31  | 2016-01-05  | 5043060000000.000000  | 285245000000.000000
 sh.600000                           | 2017-01-04  | 2016-12-31  | 2017-01-04  | 5857263000000.000000  | 338027000000.000000

返回示例数据

 |performanceExpressEPSChgPct | performanceExpressROEWa  | performanceExpressEPSDiluted  | performanceExpressGRYOY  | performanceExpressOPYOY
 ---                                 |---|---|---|---
 0.326910                            | 21.020000  | 2.520000  | 0.228390  | 0.153803
 0.191493                            | 18.820000  | 2.660000  | 0.192395  | 0.069764
 0.115412                            | 16.350000  | 2.400000  | 0.097234  | 0.054384

 返回数据说明

|参数名称                        | 参数描述
 ---                                 |---
 code                                | 证券代码
 performanceExpPubDate               | 业绩快报披露日
 performanceExpStatDate              | 业绩快报统计日期
 performanceExpUpdateDate            | 业绩快报披露日(最新)
 performanceExpressTotalAsset        | 业绩快报总资产
 performanceExpressNetAsset          | 业绩快报净资产
 performanceExpressEPSChgPct         | 业绩每股收益增长率
 performanceExpressROEWa             | 业绩快报净资产收益率ROE-加权
 performanceExpressEPSDiluted        | 业绩快报每股收益EPS-摊薄
 performanceExpressGRYOY             | 业绩快报营业总收入同比
 performanceExpressOPYOY             | 业绩快报营业利润同比