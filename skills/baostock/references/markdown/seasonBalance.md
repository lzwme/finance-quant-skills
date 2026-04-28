## 季频偿债能力

### 季频偿债能力：query_balance_data()

方法说明：通过API接口获取季频偿债能力信息，可以通过参数设置获取对应年份、季度数据，提供2007年至今数据。 返回类型：pandas的DataFrame类型。 使用示例

  ```python
    import baostock as bs
    import pandas as pd

    # 登陆系统
    lg = bs.login()
    # 显示登陆返回信息
    print('login respond error_code:'+lg.error_code)
    print('login respond  error_msg:'+lg.error_msg)

    # 偿债能力
    balance_list = []
    rs_balance = bs.query_balance_data(code="sh.600000", year=2017, quarter=2)
    while (rs_balance.error_code == '0') & rs_balance.next():
        balance_list.append(rs_balance.get_row_data())
    result_balance = pd.DataFrame(balance_list, columns=rs_balance.fields)
    # 打印输出
    print(result_balance)
    # 结果集输出到csv文件
    result_balance.to_csv("D:\\balance_data.csv", encoding="gbk", index=False)

    # 登出系统
    bs.logout()
  ```

参数含义：

  * code：股票代码，sh或sz.+6位数字代码，或者指数代码，如：sh.601398。sh：上海；sz：深圳。此参数不可为空；
  * year：统计年份，为空时默认当前年；
  * quarter：统计季度，为空时默认当前季度。不为空时只有4个取值：1，2，3，4。

返回示例数据

|code  | pubDate  | statDate  | currentRatio  | quickRatio  | cashRatio  | YOYLiability  | liabilityToAsset  | assetToEquity
---|---|---|---|---|---|---|---|---
sh.600000  | 2017-08-30  | 2017-06-30  |  |  |  | 0.100020  | 0.933703  | 15.083598

返回数据说明

|参数名称  | 参数描述  | 算法说明
---|---|---
code  | 证券代码  |
pubDate  | 公司发布财报的日期  |
statDate  | 财报统计的季度的最后一天, 比如2017-03-31, 2017-06-30  |
currentRatio  | 流动比率  | 流动资产/流动负债
quickRatio  | 速动比率  | (流动资产-存货净额)/流动负债
cashRatio  | 现金比率  | (货币资金+交易性金融资产)/流动负债
YOYLiability  | 总负债同比增长率  | (本期总负债-上年同期总负债)/上年同期中负债的绝对值*100%
liabilityToAsset  | 资产负债率  | 负债总额/资产总额
assetToEquity  | 权益乘数  | 资产总额/股东权益总额=1/(1-资产负债率)