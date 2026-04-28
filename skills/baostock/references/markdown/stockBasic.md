## 证券基本资料

### 证券基本资料：query_stock_basic()

方法说明：通过API接口获取证券基本资料，可以通过参数设置获取对应证券代码、证券名称的数据。 返回类型：pandas的DataFrame类型。 使用示例

  ```python
    import baostock as bs
    import pandas as pd

    # 登陆系统
    lg = bs.login()
    # 显示登陆返回信息
    print('login respond error_code:'+lg.error_code)
    print('login respond  error_msg:'+lg.error_msg)

    # 获取证券基本资料
    rs = bs.query_stock_basic(code="sh.600000")
    # rs = bs.query_stock_basic(code_name="浦发银行")  # 支持模糊查询
    print('query_stock_basic respond error_code:'+rs.error_code)
    print('query_stock_basic respond  error_msg:'+rs.error_msg)

    # 打印结果集
    data_list = []
    while (rs.error_code == '0') & rs.next():
        # 获取一条记录，将记录合并在一起
        data_list.append(rs.get_row_data())
    result = pd.DataFrame(data_list, columns=rs.fields)
    # 结果集输出到csv文件
    result.to_csv("D:/stock_basic.csv", encoding="gbk", index=False)
    print(result)

    # 登出系统
    bs.logout()
  ```

参数含义：

  * code：A股股票代码，sh或sz.+6位数字代码，或者指数代码，如：sh.601398。sh：上海；sz：深圳。可以为空；
  * code_name：股票名称，支持模糊查询，可以为空。
  * 当参数为空时，输出全部股票的基本信息。

返回示例数据

| code         | code_name  | ipoDate  | outDate  | type  | status
--------------|---|---|---|---|---
 sh.600000    | 浦发银行  | 1999-11-10  |  | 1  | 1

返回数据说明

| 参数名称      | 参数描述
 -----------|---
 code      | 证券代码
 code_name | 证券名称
 ipoDate   | 上市日期
 outDate   | 退市日期
 type      | 证券类型，其中1：股票，2：指数，3：其它，4：可转债，5：ETF
 status    | 上市状态，其中1：上市，0：退市