## 存款利率
### 存款利率：query_deposit_rate_data()

方法说明：通过API接口获取存款利率，可以通过参数设置获取对应起止日期的数据。 返回类型：pandas的DataFrame类型。 使用示例

```python
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

| pubDate                          | demandDepositRate  | fixedDepositRate3Month  | fixedDepositRate6Month  | fixedDepositRate1Year  | fixedDepositRate2Year  | fixedDepositRate3Year
----------------------------------|---|---|---|---|---|---
 2015-03-01                       | 0.350000  | 2.100000  | 2.300000  | 2.500000  | 3.100000  | 3.750000
 2015-05-11                       | 0.350000  | 1.850000  | 2.050000  | 2.250000  | 2.850000  | 3.500000

返回示例数据

| fixedDepositRate5Year            | installmentFixedDepositRate1Year  | installmentFixedDepositRate3Year  | installmentFixedDepositRate5Year
 ----------------------------------|---|---|---
| 2.100000                         | 2.300000  |
| 1.850000                         | 2.050000  |

返回数据说明

| 参数名称                             | 参数描述
 ----------------------------------|---
 pubDate                          | 发布日期
 demandDepositRate                | 活期存款(不定期)
 fixedDepositRate3Month           | 定期存款(三个月)
 fixedDepositRate6Month           | 定期存款(半年)
 fixedDepositRate1Year            | 定期存款整存整取(一年)
 fixedDepositRate2Year            | 定期存款整存整取(二年)
 fixedDepositRate3Year            | 定期存款整存整取(三年)
 fixedDepositRate5Year            | 定期存款整存整取(五年)
 installmentFixedDepositRate1Year | 零存整取、整存零取、存本取息定期存款(一年)
 installmentFixedDepositRate3Year | 零存整取、整存零取、存本取息定期存款(三年)
 installmentFixedDepositRate5Year | 零存整取、整存零取、存本取息定期存款(五年)