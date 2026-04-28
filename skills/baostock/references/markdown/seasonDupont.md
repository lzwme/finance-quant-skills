## 季频杜邦指数

### 季频杜邦指数：query_dupont_data()

方法说明：通过API接口获取季频杜邦指数信息，可以通过参数设置获取对应年份、季度数据，提供2007年至今数据。 返回类型：pandas的DataFrame类型。 使用示例

  ```python
    import baostock as bs
    import pandas as pd

    # 登陆系统
    lg = bs.login()
    # 显示登陆返回信息
    print('login respond error_code:'+lg.error_code)
    print('login respond  error_msg:'+lg.error_msg)

    # 查询杜邦指数
    dupont_list = []
    rs_dupont = bs.query_dupont_data(code="sh.600000", year=2017, quarter=2)
    while (rs_dupont.error_code == '0') & rs_dupont.next():
        dupont_list.append(rs_dupont.get_row_data())
    result_dupont = pd.DataFrame(dupont_list, columns=rs_dupont.fields)
    # 打印输出
    print(result_dupont)
    # 结果集输出到csv文件
    result_dupont.to_csv("D:\\dupont_data.csv", encoding="gbk", index=False)

    # 登出系统
    bs.logout()
  ```

参数含义：

  * code：股票代码，sh或sz.+6位数字代码，或者指数代码，如：sh.601398。sh：上海；sz：深圳。此参数不可为空；
  * year：统计年份，为空时默认当前年；
  * quarter：统计季度，为空时默认当前季度。不为空时只有4个取值：1，2，3，4。

返回示例数据

| code                 | pubDate  | statDate  | dupontROE  | dupontAssetStoEquity  | dupontAssetTurn  | dupontPnitoni
----------------------|---|---|---|---|---|---
 sh.600000            | 2017-08-30  | 2017-06-30  | 0.074617  | 15.594453  | 0.014161  | 0.987483

返回示例数据

| dupontNitogr | dupontTaxBurden  | dupontIntburden  | dupontEbittogr
 --------------|---|---|---
 0.342179     | 0.776088  |  |

返回数据说明

|  参数名称         | 参数描述  | 算法说明
 ---                  |---|---
 code                 | 证券代码  |
 pubDate              | 公司发布财报的日期  |
 statDate             | 财报统计的季度的最后一天, 比如2017-03-31, 2017-06-30  |
 dupontROE            | 净资产收益率  | 归属母公司股东净利润/[(期初归属母公司股东的权益+期末归属母公司股东的权益)/2]*100%
 dupontAssetStoEquity | 权益乘数，反映企业财务杠杆效应强弱和财务风险  | 平均总资产/平均归属于母公司的股东权益
 dupontAssetTurn      | 总资产周转率，反映企业资产管理效率的指标  | 营业总收入/[(期初资产总额+期末资产总额)/2]
 dupontPnitoni        | 归属母公司股东的净利润/净利润，反映母公司控股子公司百分比。如果企业追加投资，扩大持股比例，则本指标会增加。  |
 dupontNitogr         | 净利润/营业总收入，反映企业销售获利率  |
 dupontTaxBurden      | 净利润/利润总额，反映企业税负水平，该比值高则税负较低。净利润/利润总额=1-所得税/利润总额  |
 dupontIntburden      | 利润总额/息税前利润，反映企业利息负担，该比值高则税负较低。利润总额/息税前利润=1-利息费用/息税前利润
 dupontEbittogr       | 息税前利润/营业总收入，反映企业经营利润率，是企业经营获得的可供全体投资人（股东和债权人）分配的盈利占企业全部营收收入的百分比  |