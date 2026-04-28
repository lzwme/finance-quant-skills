## 行业分类
### 行业分类：query_stock_industry()

方法说明：通过API接口获取行业分类信息，更新频率：每周一更新。返回类型：pandas的DataFrame类型。 使用示例

```Python
    import baostock as bs
    import pandas as pd

    # 登陆系统
    lg = bs.login()
    # 显示登陆返回信息
    print('login respond error_code:'+lg.error_code)
    print('login respond  error_msg:'+lg.error_msg)

    # 获取行业分类数据
    rs = bs.query_stock_industry()
    # rs = bs.query_stock_basic(code_name="浦发银行")
    print('query_stock_industry error_code:'+rs.error_code)
    print('query_stock_industry respond  error_msg:'+rs.error_msg)

    # 打印结果集
    industry_list = []
    while (rs.error_code == '0') & rs.next():
    # 获取一条记录，将记录合并在一起
    industry_list.append(rs.get_row_data())
    result = pd.DataFrame(industry_list, columns=rs.fields)
    # 结果集输出到csv文件
    result.to_csv("D:/stock_industry.csv", encoding="gbk", index=False)
    print(result)

    # 登出系统
    bs.logout()
```

参数含义：

  * code：A股股票代码，sh或sz.+6位数字代码，或者指数代码，如：sh.601398。sh：上海；sz：深圳。可以为空；
  * date：查询日期，格式XXXX-XX-XX，为空时默认最新日期。

返回示例数据

updateDate  | code  | code_name  | industry  | industryClassification
---|---|---|---|---
2018-11-26  | sh.600000  | 浦发银行  | J66货币金融服务  | 证监会行业分类
2018-11-26  | sh.600001  | 邯郸钢铁  |  | 证监会行业分类

返回数据说明

参数名称  | 参数描述
---|---
updateDate  | 更新日期
code  | 证券代码
code_name  | 证券名称
industry  | 所属行业
industryClassification  | 所属行业类别