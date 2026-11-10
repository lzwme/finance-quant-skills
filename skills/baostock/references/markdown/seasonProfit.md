## 季频盈利能力

### 季频盈利能力：query_profit_data()

方法说明：通过API接口获取季频盈利能力信息，可以通过参数设置获取对应年份、季度数据，提供2007年至今数据。

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

**说明：**

* quarter 取值为1、2、3、4，分别对应一季报（3月31日）、半年报（6月30日）、三季报（9月30日）、年报（12月31日）。quarter=4 即为**年报**数据，statDate 为当年的12-31；
* 同一证券同一报告期（year+quarter）在数据库中仅保留一条记录，如财报数据被修正，返回的是最新披露口径的数据；
* 当指定季度尚未披露、或该证券当年无对应报告时，返回空结果集，error_code 仍为"0"，此时不应视为接口异常；
* 财务比率类字段（roeAvg、npMargin、gpMargin 等）在分母为0或数据缺失时返回空字符串，使用前需先做空值判断，不能直接转为 float。

返回示例数据

| code         | pubDate  | statDate  | roeAvg  | npMargin  | gpMargin  | netProfit  | epsTTM  | MBRevenue  | totalShare  | liqaShare
--------------|---|---|---|---|---|---|---|---|---|---
 sh.600000    | 2017-08-30  | 2017-06-30  | 0.074617  | 0.342179  |  | 28522000000.000000  | 1.939029  | 83354000000.000000  | 28103763899.00  | 28103763899.00

返回数据说明

|参数名称 | 参数描述  | 算法说明
 ---          |---|---
 code         | 证券代码  |
 pubDate      | 公司发布财报的日期  |
 statDate     | 财报统计的季度的最后一天, 比如2017-03-31, 2017-06-30  |
 roeAvg       | 净资产收益率(平均)(%)  | 归属母公司股东净利润/[(期初归属母公司股东的权益+期末归属母公司股东的权益)/2]*100%
 npMargin     | 销售净利率(%)  | 净利润/营业收入*100%
 gpMargin     | 销售毛利率(%)  | 毛利/营业收入*100%=(营业收入-营业成本)/营业收入*100%
 netProfit    | 净利润(元)  |
 epsTTM       | 每股收益  | 归属母公司股东的净利润TTM/最新总股本
 MBRevenue    | 主营营业收入(元)  |
 totalShare   | 总股本  |
 liqaShare    | 流通股本  |