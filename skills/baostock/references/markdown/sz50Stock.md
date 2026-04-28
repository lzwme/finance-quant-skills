## 上证50成分股

### 上证50成分股：query_sz50_stocks()

方法说明：通过API接口获取上证50成分股信息，更新频率：每周一更新。返回类型：pandas的DataFrame类型。 使用示例

 ```python
    import baostock as bs
    import pandas as pd

    # 登陆系统
    lg = bs.login()
    # 显示登陆返回信息
    print('login respond error_code:'+lg.error_code)
    print('login respond  error_msg:'+lg.error_msg)

    # 获取上证50成分股
    rs = bs.query_sz50_stocks()
    print('query_sz50 error_code:'+rs.error_code)
    print('query_sz50  error_msg:'+rs.error_msg)

    # 打印结果集
    sz50_stocks = []
    while (rs.error_code == '0') & rs.next():
        # 获取一条记录，将记录合并在一起
        sz50_stocks.append(rs.get_row_data())
    result = pd.DataFrame(sz50_stocks, columns=rs.fields)
    # 结果集输出到csv文件
    result.to_csv("D:/sz50_stocks.csv", encoding="gbk", index=False)
    print(result)

    # 登出系统
    bs.logout()
  ```

参数含义：

  * date：查询日期，格式XXXX-XX-XX，为空时默认最新日期。

返回示例数据

| updateDate   | code  | code_name
--------------|---|---
 2018-11-26   | sh.600000  | 浦发银行
 2018-11-26   | sh.600016  | 民生银行

返回数据说明

| 参数名称       | 参数描述
 ------------|---
 updateDate | 更新日期
 code       | 证券代码
 code_name  | 证券名称