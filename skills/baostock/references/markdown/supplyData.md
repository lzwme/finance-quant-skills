## 货币供应量
### 货币供应量：query_money_supply_data_month()

方法说明：通过API接口获取货币供应量，可以通过参数设置获取对应起止日期的数据。 返回类型：pandas的DataFrame类型。 使用示例

```python
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

返回示例数据

| statYear        | statMonth  | m0Month  | m0YOY  | m0ChainRelative  | m1Month  | m1YOY  | m1ChainRelative
-----------------|---|---|---|---|---|---|---
 2010            | 01  | 40758.580000  | —0.790000  | 6.566809  | 229588.980000  | 38.960000  | 3.677276
 2010            | 02  | 42865.790000  | 21.980000  | 5.169979  | 224286.950000  | 34.990000  | —2.309357

返回示例数据

| m2Month         | m2YOY  | m2ChainRelative
 -----------------|---|---
 625609.290000   | 25.980000  | 2.521165
 636072.260000   | 25.520000  | 1.672445

返回数据说明

| 参数名称            | 参数描述
 -----------------|---
 statYear        | 统计年度
 statMonth       | 统计月份
 m0Month         | 货币供应量M0（月）
 m0YOY           | 货币供应量M0（同比）
 m0ChainRelative | 货币供应量M0（环比）
 m1Month         | 货币供应量M1（月）
 m1YOY           | 货币供应量M1（同比）
 m1ChainRelative | 货币供应量M1（环比）
 m2Month         | 货币供应量M2（月）
 m2YOY           | 货币供应量M2（同比）
 m2ChainRelative | 货币供应量M2（环比）