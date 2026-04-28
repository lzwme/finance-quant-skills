## 估值指标(日频)

## 沪深A股估值指标(日频) 示例

通过query_history_k_data_plus()获取沪深A股估值指标(日频)数据（指数未提供估值数据），未提供周、月估值数据。示例数据：[<button>下载</button>](helpdocs/csv/history_A_stock_valuation_indicator_data.xlsx)

```python
    import baostock as bs
    import pandas as pd

    #### 登陆系统 ####
    lg = bs.login()
    # 显示登陆返回信息
    print('login respond error_code:'+lg.error_code)
    print('login respond  error_msg:'+lg.error_msg)

    #### 获取沪深A股估值指标(日频)数据 ####
    # peTTM    滚动市盈率
    # psTTM    滚动市销率
    # pcfNcfTTM    滚动市现率
    # pbMRQ    市净率
    rs = bs.query_history_k_data_plus("sh.600000",
        "date,code,close,peTTM,pbMRQ,psTTM,pcfNcfTTM",
        start_date='2015-01-01', end_date='2017-12-31',
        frequency="d", adjustflag="3")
    print('query_history_k_data_plus respond error_code:'+rs.error_code)
    print('query_history_k_data_plus respond  error_msg:'+rs.error_msg)

    #### 打印结果集 ####
    result_list = []
    while (rs.error_code == '0') & rs.next():
        # 获取一条记录，将记录合并在一起
        result_list.append(rs.get_row_data())
    result = pd.DataFrame(result_list, columns=rs.fields)

    #### 结果集输出到csv文件 ####
    result.to_csv("D:\\history_A_stock_valuation_indicator_data.csv", encoding="gbk", index=False)
    print(result)

    #### 登出系统 ####
    bs.logout()
```

返回数据说明

| 参数名称      | 参数描述  | 说明
-----------|---|---
 date      | 交易所行情日期  | 格式：YYYY-MM-DD
 code      | 证券代码  | 格式：sh.600000。sh：上海，sz：深圳
 close     | 今收盘价  | 精度：小数点后4位；单位：人民币元
 peTTM     | 滚动市盈率  | 精度：小数点后4位
 psTTM     | 滚动市销率  | 精度：小数点后4位
 pcfNcfTTM | 滚动市现率  | 精度：小数点后4位
 pbMRQ     | 市净率  | 精度：小数点后4位