## 季频现金流量

### 季频现金流量：query_cash_flow_data()

方法说明：通过API接口获取季频现金流量信息，可以通过参数设置获取对应年份、季度数据，提供2007年至今数据。 返回类型：pandas的DataFrame类型。 使用示例

  ```python
    import baostock as bs
    import pandas as pd

    # 登陆系统
    lg = bs.login()
    # 显示登陆返回信息
    print('login respond error_code:'+lg.error_code)
    print('login respond  error_msg:'+lg.error_msg)

    # 季频现金流量
    cash_flow_list = []
    rs_cash_flow = bs.query_cash_flow_data(code="sh.600000", year=2017, quarter=2)
    while (rs_cash_flow.error_code == '0') & rs_cash_flow.next():
        cash_flow_list.append(rs_cash_flow.get_row_data())
    result_cash_flow = pd.DataFrame(cash_flow_list, columns=rs_cash_flow.fields)
    # 打印输出
    print(result_cash_flow)
    # 结果集输出到csv文件
    result_cash_flow.to_csv("D:\\cash_flow_data.csv", encoding="gbk", index=False)

    # 登出系统
    bs.logout()
  ```

参数含义：

  * code：股票代码，sh或sz.+6位数字代码，或者指数代码，如：sh.601398。sh：上海；sz：深圳。此参数不可为空；
  * year：统计年份，为空时默认当前年；
  * quarter：统计季度，为空时默认当前季度。不为空时只有4个取值：1，2，3，4。

返回示例数据

| code                | pubDate  | statDate  | CAToAsset  | NCAToAsset  | tangibleAssetToAsset  | ebitToInterest  | CFOToOR  | CFOToNP  | CFOToGr
---------------------|---|---|---|---|---|---|---|---|---
 sh.600000           | 2017-08-30  | 2017-06-30  |  |  |  |  | —3.071550  | —8.976439  | —3.071550

返回数据说明

|  参数名称         | 参数描述  | 算法说明
 ---                 |---|---
 code                | 证券代码  |
 pubDate             | 公司发布财报的日期  |
 statDate            | 财报统计的季度的最后一天, 比如2017-03-31, 2017-06-30  |
 CAToAsset           | 流动资产除以总资产  |
 NCAToAsset          | 非流动资产除以总资产  |
 tangibleAssetToAsset | 有形资产除以总资产  |
 ebitToInterest      | 已获利息倍数  | 息税前利润/利息费用
 CFOToOR             | 经营活动产生的现金流量净额除以营业收入  |
 CFOToNP             | 经营性现金净流量除以净利润  |
 CFOToGr             | 经营性现金净流量除以营业总收入  |