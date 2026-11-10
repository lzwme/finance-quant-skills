## 证券元信息

## 获取交易日信息

```python
    import baostock as bs
    import pandas as pd

    #### 登陆系统 ####
    lg = bs.login()
    # 显示登陆返回信息
    print('login respond error_code:'+lg.error_code)
    print('login respond  error_msg:'+lg.error_msg)

    #### 获取交易日信息 ####
    rs = bs.query_trade_dates(start_date="2017-01-01", end_date="2017-06-30")
    print('query_trade_dates respond error_code:'+rs.error_code)
    print('query_trade_dates respond  error_msg:'+rs.error_msg)

    #### 打印结果集 ####
    data_list = []
    while (rs.error_code == '0') & rs.next():
        # 获取一条记录，将记录合并在一起
        data_list.append(rs.get_row_data())
    result = pd.DataFrame(data_list, columns=rs.fields)

    #### 结果集输出到csv文件 ####
    result.to_csv("D:\\trade_datas.csv", encoding="gbk", index=False)
    print(result)

    #### 登出系统 ####
    bs.logout()
  ```

参数含义：

  * start_date：查询交易日的开始日期
  * end_date：查询交易日的截止日期

**说明：**

* 返回区间内**每一个自然日**（含周末、法定节假日），而非仅交易日，需通过 is_trading_day 字段判断是否交易日；

返回示例数据

|calendar_date | is_trading_day
---------------|---
2024-01-01 | 0
2024-01-02 | 1
2024-01-03 | 1

返回数据说明

| 参数名称      | 参数描述
 ---------------|---
 calendar_date  | 日期
 is_trading_day | 是否交易日，其中0：非交易日，1：交易日

## 获取某日所有证券信息

```python
    import baostock as bs
    import pandas as pd

    #### 登陆系统 ####
    lg = bs.login()
    # 显示登陆返回信息
    print('login respond error_code:'+lg.error_code)
    print('login respond  error_msg:'+lg.error_msg)

    #### 获取某日所有证券信息 ####
    rs = bs.query_all_stock(day="2024-10-25")  #当参数“day”为空时，默认取当天日期。闭市后日K线数据更新，该接口才会返回当天数据，否则返回空。
    print('query_all_stock respond error_code:'+rs.error_code)
    print('query_all_stock respond  error_msg:'+rs.error_msg)

    #### 打印结果集 ####
    data_list = []
    while (rs.error_code == '0') & rs.next():
        # 获取一条记录，将记录合并在一起
        data_list.append(rs.get_row_data())
    result = pd.DataFrame(data_list, columns=rs.fields)

    #### 结果集输出到csv文件 ####
    result.to_csv("D:\\all_stock.csv", encoding="gbk", index=False)
    print(result)

    #### 登出系统 ####
    bs.logout()
```

参数含义：

  * day：有值：获取指定交易日沪深市场的所有证券信息；为空时默认取当天沪深市场的所有证券信息

**说明：**

* 该接口返回指定交易日的全部证券列表（含A股、指数），数据范围同 query_history_k_data_plus()，更新时间与日K线一致（闭市后更新）；指定当天且日K数据尚未更新时，返回空结果集，error_code 仍为"0"；
* 非交易日（周末、节假日）没有日K数据，day 为非交易日时同样返回空结果集；
* tradeStatus 枚举：1：正常交易，0：停牌；

返回示例数据

| code | tradeStatus |code_name
--------------|---|---
sh.600000	| 1	| 浦发银行
sh.600423	| 0	| *ST柳化
sz.000001	| 1	| 平安银行

返回数据说明

| 参数名称      | 参数描述
 ------------|---
 code       | 证券代码
 tradeStatus| 交易状态，其中1：正常交易，0：停牌
 code_name  | 证券名称