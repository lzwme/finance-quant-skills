## 存款准备金率

### 存款准备金率：query_required_reserve_ratio_data()

方法说明：通过API接口获取存款准备金率，可以通过参数设置获取对应起止日期的数据。 返回类型：pandas的DataFrame类型。 使用示例

```python
    import baostock as bs
    import pandas as pd

    # 登陆系统
    lg = bs.login()
    # 显示登陆返回信息
    print('login respond error_code:'+lg.error_code)
    print('login respond  error_msg:'+lg.error_msg)

    # 获取存款准备金率
    rs = bs.query_required_reserve_ratio_data(start_date="2010-01-01", end_date="2015-12-31")
    print('query_required_reserve_ratio_data respond error_code:'+rs.error_code)
    print('query_required_reserve_ratio_data respond  error_msg:'+rs.error_msg)

    # 打印结果集
    data_list = []
    while (rs.error_code == '0') & rs.next():
        # 获取一条记录，将记录合并在一起
        data_list.append(rs.get_row_data())
    result = pd.DataFrame(data_list, columns=rs.fields)
    # 结果集输出到csv文件
    result.to_csv("D:/required_reserve_ratio.csv", encoding="gbk", index=False)
    print(result)

    # 登出系统
    bs.logout()
 ```

参数含义：

  * start_date：开始日期，格式XXXX-XX-XX，发布日期在这个范围内，可以为空；
  * end_date：结束日期，格式XXXX-XX-XX，发布日期在这个范围内，可以为空；
  * yearType:年份类别，默认为0，查询公告日期；1查询生效日期。

返回示例数据

| pubDate                            | effectiveDate  | bigInstitutionsRatioPre  | bigInstitutionsRatioAfter
------------------------------------|---|---|---
 2010-01-12                         | 2010-01-18  | 15.5  | 16.0
 2010-02-12                         | 2010-02-25  | 16.0  | 16.5

返回示例数据

|  mediumInstitutionsRatioPre | mediumInstitutionsRatioAfter
 ---                                |---
 13.5                               | 14.0
 14.0                               | 14.5

 返回数据说明

|  参数名称                        | 参数描述
 ------------------------------|---
 pubDate                      | 公告日期
 effectiveDate                | 生效日期
 bigInstitutionsRatioPre      | 人民币存款准备金率：大型存款类金融机构 调整前
 bigInstitutionsRatioAfter    | 人民币存款准备金率：大型存款类金融机构 调整后
 mediumInstitutionsRatioPre   | 人民币存款准备金率：中小型存款类金融机构 调整前
 mediumInstitutionsRatioAfter | 人民币存款准备金率：中小型存款类金融机构 调整后