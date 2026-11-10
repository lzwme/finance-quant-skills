## 贷款利率
### 贷款利率：query_loan_rate_data()

方法说明：通过API接口获取贷款利率，可以通过参数设置获取对应起止日期的数据。 返回类型：pandas的DataFrame类型。 使用示例

```python
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

| pubDate                    | loanRate6Month  | loanRate6MonthTo1Year  | loanRate1YearTo3Year  | loanRate3YearTo5Year
----------------------------|---|---|---|---
 2010-10-20                 | 5.100000  | 5.560000  | 5.600000  | 5.960000
 2010-12-26                 | 5.350000  | 5.810000  | 5.850000  | 6.220000

 返回示例数据

| loanRateAbove5Year     | mortgateRateBelow5Year  | mortgateRateAbove5Year
 ------------------------|---|---
 6.140000               | 3.500000  | 4.050000
 6.400000               | 3.750000  | 4.300000

返回数据说明

|参数名称           | 参数描述
 ---                    |---
 pubDate                | 发布日期
 loanRate6Month         | 6个月贷款利率
 loanRate6MonthTo1Year  | 6个月至1年贷款利率
 loanRate1YearTo3Year   | 1年至3年贷款利率
 loanRate3YearTo5Year   | 3年至5年贷款利率
 loanRateAbove5Year     | 5年以上贷款利率
 mortgateRateBelow5Year | 5年以下住房公积金贷款利率
 mortgateRateAbove5Year | 5年以上住房公积金贷款利率