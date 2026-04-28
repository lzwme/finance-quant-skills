## 货币供应量(年底余额)
### 货币供应量(年底余额)：query_money_supply_data_year()

方法说明：通过API接口获取货币供应量(年底余额)，可以通过参数设置获取对应起止日期的数据。 返回类型：pandas的DataFrame类型。 使用示例

 ```python
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

返回示例数据

| statYear     | m0Year  | m0YearYOY  | m1Year  | m1YearYOY  | m2Year  | m2YearYOY
--------------|---|---|---|---|---|---
 2010         | 44628.170000  | 16.700000  | 266621.540000  | 21.200000  | 725851.800000  | 19.700000
 2011         | 50748.460000  | 13.760000  | 289847.700000  | 7.850000  | 851590.900000  | 13.610000

 返回数据说明

| 参数名称      | 参数描述
 -----------|---
 statYear  | 统计年度
 m0Year    | 年货币供应量M0（亿元）
 m0YearYOY | 年货币供应量M0（同比）
 m1Year    | 年货币供应量M1（亿元）
 m1YearYOY | 年货币供应量M1（同比）
 m2Year    | 年货币供应量M2（亿元）
 m2YearYOY | 年货币供应量M2（同比）