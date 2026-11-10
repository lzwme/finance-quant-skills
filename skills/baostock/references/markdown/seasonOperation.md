## 季频营运能力

### 季频营运能力：query_operation_data()

方法说明：通过API接口获取季频营运能力信息，可以通过参数设置获取对应年份、季度数据，提供2007年至今数据。

返回类型：pandas的DataFrame类型。

使用示例

  ```python
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

**说明：**

* quarter 取值为1、2、3、4，分别对应一季报（3月31日）、半年报（6月30日）、三季报（9月30日）、年报（12月31日）。quarter=4 即为**年报**数据，statDate 为当年的12-31；
* 周转天数（NRTurnDays、INVTurnDays）按报告期累计天数折算：一季报90天、中报180天、三季报270天、年报360天，并非单季度天数；
* 同一证券同一报告期（year+quarter）在数据库中仅保留一条记录，如财报数据被修正，返回的是最新披露口径的数据；
* 当指定季度尚未披露、或该证券当年无对应报告时，返回空结果集，error_code 仍为"0"；周转率/周转天数字段在分母为0或数据缺失时返回空字符串。

返回示例数据

| code           | pubDate  | statDate  | NRTurnRatio  | NRTurnDays  | INVTurnRatio  | INVTurnDays  | CATurnRatio  | AssetTurnRatio
----------------|---|---|---|---|---|---|---|---
 sh.600000      | 2017-08-30  | 2017-06-30  |  |  |  |  |  | 0.014161

返回数据说明

| 参数名称   | 参数描述  | 算法说明
 ---            |---|---
 code           | 证券代码  |
 pubDate        | 公司发布财报的日期  |
 statDate       | 财报统计的季度的最后一天, 比如2017-03-31, 2017-06-30  |
 NRTurnRatio    | 应收账款周转率(次)  | 营业收入/[(期初应收票据及应收账款净额+期末应收票据及应收账款净额)/2]
 NRTurnDays     | 应收账款周转天数(天)  | 季报天数/应收账款周转率(一季报：90天，中报：180天，三季报：270天，年报：360天)
 INVTurnRatio   | 存货周转率(次)  | 营业成本/[(期初存货净额+期末存货净额)/2]
 INVTurnDays    | 存货周转天数(天)  | 季报天数/存货周转率(一季报：90天，中报：180天，三季报：270天，年报：360天)
 CATurnRatio    | 流动资产周转率(次)  | 营业总收入/[(期初流动资产+期末流动资产)/2]
 AssetTurnRatio | 总资产周转率  | 营业总收入/[(期初资产总额+期末资产总额)/2]