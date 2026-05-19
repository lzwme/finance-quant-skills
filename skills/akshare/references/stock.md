## AKShare 股票数据

### A股

#### 股票市场总貌

##### 上海证券交易所

接口: stock_sse_summary

目标地址: http://www.sse.com.cn/market/stockdata/statistic/

描述: 上海证券交易所-股票数据总貌

限量: 单次返回最近交易日的股票数据总貌(当前交易日的数据需要交易所收盘后统计)

输入参数

| 名称  | 类型  | 描述  |
|-----|-----|-----|
| -   | -   | -   |

输出参数-实时行情数据

| 名称  | 类型     | 描述  |
|-----|--------|-----|
| 项目  | object | -   |
| 股票  | object | -   |
| 科创板 | object | -   |
| 主板  | object | -   |

接口示例

```python
import akshare as ak

stock_sse_summary_df = ak.stock_sse_summary()
print(stock_sse_summary_df)
```

##### 深圳证券交易所

###### 证券类别统计

接口: stock_szse_summary

目标地址: http://www.szse.cn/market/overview/index.html

描述: 深圳证券交易所-市场总貌-证券类别统计

限量: 单次返回指定 date 的市场总貌数据-证券类别统计(当前交易日的数据需要交易所收盘后统计)

输入参数

| 名称   | 类型  | 描述                                  |
|------|-----|-------------------------------------|
| date | str | date="20200619"; 当前交易日的数据需要交易所收盘后统计 |

输出参数

| 名称   | 类型      | 描述      |
|------|---------|---------|
| 证券类别 | object  | -       |
| 数量   | int64   | 注意单位: 只 |
| 成交金额 | float64 | 注意单位: 元 |
| 总市值  | float64 | -       |
| 流通市值 | float64 | -       |

接口示例

```python
import akshare as ak

stock_szse_summary_df = ak.stock_szse_summary(date="20200619")
print(stock_szse_summary_df)
```

###### 地区交易排序

接口: stock_szse_area_summary

目标地址: http://www.szse.cn/market/overview/index.html

描述: 深圳证券交易所-市场总貌-地区交易排序

限量: 单次返回指定 date 的市场总貌数据-地区交易排序数据

输入参数

| 名称   | 类型  | 描述                |
|------|-----|-------------------|
| date | str | date="202203"; 年月 |

输出参数

| 名称    | 类型      | 描述      |
|-------|---------|---------|
| 序号    | int64   | -       |
| 地区    | object  | -       |
| 总交易额  | float64 | 注意单位: 元 |
| 占市场   | float64 | 注意单位: % |
| 股票交易额 | float64 | 注意单位: 元 |
| 基金交易额 | float64 | 注意单位: 元 |
| 债券交易额 | float64 | 注意单位: 元 |

2025年添加优先股交易额与期权交易额

| 名称     | 类型      | 描述      |
|--------|---------|---------|
| 序号     | int64   | -       |
| 地区     | object  | -       |
| 总交易额   | float64 | 注意单位: 元 |
| 占市场    | float64 | 注意单位: % |
| 股票交易额  | float64 | 注意单位: 元 |
| 基金交易额  | float64 | 注意单位: 元 |
| 债券交易额  | float64 | 注意单位: 元 |
| 优先股交易额 | float64 | 注意单位: 元 |
| 期权交易额  | float64 | 注意单位: 元 |
| 接口示例   |         |         |

```python
import akshare as ak

stock_szse_area_summary_df = ak.stock_szse_area_summary(date="202412")
print(stock_szse_area_summary_df)
```

```python
import akshare as ak

stock_szse_area_summary_df = ak.stock_szse_area_summary(date="202508")
print(stock_szse_area_summary_df)
```

###### 股票行业成交

接口: stock_szse_sector_summary

目标地址: http://docs.static.szse.cn/www/market/periodical/month/W020220511355248518608.html

描述: 深圳证券交易所-统计资料-股票行业成交数据

限量: 单次返回指定 symbol 和 date 的统计资料-股票行业成交数据

输入参数

| 名称     | 类型  | 描述                                  |
|--------|-----|-------------------------------------|
| symbol | str | symbol="当月"; choice of {"当月", "当年"} |
| date   | str | date="202501"; 年月                   |

输出参数

| 名称        | 类型      | 描述      |
|-----------|---------|---------|
| 项目名称      | object  | -       |
| 项目名称-英文   | object  | -       |
| 交易天数      | int64   | -       |
| 成交金额-人民币元 | int64   |         |
| 成交金额-占总计  | float64 | 注意单位: % |
| 成交股数-股数   | int64   | -       |
| 成交股数-占总计  | float64 | 注意单位: % |
| 成交笔数-笔    | int64   | -       |
| 成交笔数-占总计  | float64 | 注意单位: % |

接口示例

```python
import akshare as ak

stock_szse_sector_summary_df = ak.stock_szse_sector_summary(symbol="当年", date="202501")
print(stock_szse_sector_summary_df)
```

##### 上海证券交易所-每日概况

接口: stock_sse_deal_daily

目标地址: http://www.sse.com.cn/market/stockdata/overview/day/

描述: 上海证券交易所-数据-股票数据-成交概况-股票成交概况-每日股票情况

限量: 单次返回指定日期的每日概况数据, 当前交易日数据需要在收盘后获取; 注意仅支持获取在 20211227（包含）之后的数据

输入参数

| 名称   | 类型  | 描述                                                              |
|------|-----|-----------------------------------------------------------------|
| date | str | date="20250221"; 当前交易日的数据需要交易所收盘后统计; 注意仅支持获取在 20211227（包含）之后的数据 |

输出参数

| 名称   | 类型      | 描述        |
|------|---------|-----------|
| 单日情况 | object  | 包含了网页所有字段 |
| 股票   | float64 | -         |
| 主板A  | float64 | -         |
| 主板B  | float64 | -         |
| 科创板  | float64 | -         |
| 股票回购 | float64 | -         |

接口示例

```python
import akshare as ak

stock_sse_deal_daily_df = ak.stock_sse_deal_daily(date="20250221")
print(stock_sse_deal_daily_df)
```

#### 个股信息查询-东财

接口: stock_individual_info_em

目标地址: http://quote.eastmoney.com/concept/sh603777.html?from=classic

描述: 东方财富-个股-股票信息

限量: 单次返回指定 symbol 的个股信息

输入参数

| 名称      | 类型    | 描述                      |
|---------|-------|-------------------------|
| symbol  | str   | symbol="603777"; 股票代码   |
| timeout | float | timeout=None; 默认不设置超时参数 |

输出参数

| 名称    | 类型     | 描述  |
|-------|--------|-----|
| item  | object | -   |
| value | object | -   |

接口示例

```python
import akshare as ak

stock_individual_info_em_df = ak.stock_individual_info_em(symbol="000001")
print(stock_individual_info_em_df)
```

#### 个股信息查询-雪球

接口: stock_individual_basic_info_xq

目标地址: https://xueqiu.com/snowman/S/SH601127/detail#/GSJJ

描述: 雪球财经-个股-公司概况-公司简介

限量: 单次返回指定 symbol 的个股信息

输入参数

| 名称      | 类型    | 描述                      |
|---------|-------|-------------------------|
| symbol  | str   | symbol="SH601127"; 股票代码 |
| token   | str   | token=None;             |
| timeout | float | timeout=None; 默认不设置超时参数 |

输出参数

| 名称    | 类型     | 描述  |
|-------|--------|-----|
| item  | object | -   |
| value | object | -   |

接口示例

```python
import akshare as ak

stock_individual_basic_info_xq_df = ak.stock_individual_basic_info_xq(symbol="SH601127")
print(stock_individual_basic_info_xq_df)
```

#### 行情报价

接口: stock_bid_ask_em

目标地址: https://quote.eastmoney.com/sz000001.html

描述: 东方财富-行情报价

限量: 单次返回指定股票的行情报价数据

输入参数

| 名称     | 类型  | 描述                    |
|--------|-----|-----------------------|
| symbol | str | symbol="000001"; 股票代码 |

输出参数

| 名称    | 类型      | 描述 |
|-------|---------|----|
| item  | object  | -  |
| value | float64 | -  |

接口示例

```python
import akshare as ak

stock_bid_ask_em_df = ak.stock_bid_ask_em(symbol="000001")
print(stock_bid_ask_em_df)
```

#### 实时行情数据

##### 实时行情数据-东财

###### 沪深京 A 股

接口: stock_zh_a_spot_em

目标地址: https://quote.eastmoney.com/center/gridlist.html#hs_a_board

描述: 东方财富网-沪深京 A 股-实时行情数据

限量: 单次返回所有沪深京 A 股上市公司的实时行情数据

输入参数

| 名称  | 类型  | 描述  |
|-----|-----|-----|
| -   | -   | -   |

输出参数

| 名称      | 类型      | 描述      |
|---------|---------|---------|
| 序号      | int64   | -       |
| 代码      | object  | -       |
| 名称      | object  | -       |
| 最新价     | float64 | -       |
| 涨跌幅     | float64 | 注意单位: % |
| 涨跌额     | float64 | -       |
| 成交量     | float64 | 注意单位: 手 |
| 成交额     | float64 | 注意单位: 元 |
| 振幅      | float64 | 注意单位: % |
| 最高      | float64 | -       |
| 最低      | float64 | -       |
| 今开      | float64 | -       |
| 昨收      | float64 | -       |
| 量比      | float64 | -       |
| 换手率     | float64 | 注意单位: % |
| 市盈率-动态  | float64 | -       |
| 市净率     | float64 | -       |
| 总市值     | float64 | 注意单位: 元 |
| 流通市值    | float64 | 注意单位: 元 |
| 涨速      | float64 | -       |
| 5分钟涨跌   | float64 | 注意单位: % |
| 60日涨跌幅  | float64 | 注意单位: % |
| 年初至今涨跌幅 | float64 | 注意单位: % |

接口示例

```python
import akshare as ak

stock_zh_a_spot_em_df = ak.stock_zh_a_spot_em()
print(stock_zh_a_spot_em_df)
```

###### 沪 A 股

接口: stock_sh_a_spot_em

目标地址: http://quote.eastmoney.com/center/gridlist.html#sh_a_board

描述: 东方财富网-沪 A 股-实时行情数据

限量: 单次返回所有沪 A 股上市公司的实时行情数据

输入参数

| 名称  | 类型  | 描述  |
|-----|-----|-----|
| -   | -   | -   |

输出参数

| 名称      | 类型      | 描述      |
|---------|---------|---------|
| 序号      | int64   | -       |
| 代码      | object  | -       |
| 名称      | object  | -       |
| 最新价     | float64 | -       |
| 涨跌幅     | float64 | 注意单位: % |
| 涨跌额     | float64 | -       |
| 成交量     | float64 | 注意单位: 手 |
| 成交额     | float64 | 注意单位: 元 |
| 振幅      | float64 | 注意单位: % |
| 最高      | float64 | -       |
| 最低      | float64 | -       |
| 今开      | float64 | -       |
| 昨收      | float64 | -       |
| 量比      | float64 | -       |
| 换手率     | float64 | 注意单位: % |
| 市盈率-动态  | float64 | -       |
| 市净率     | float64 | -       |
| 总市值     | float64 | 注意单位: 元 |
| 流通市值    | float64 | 注意单位: 元 |
| 涨速      | float64 | -       |
| 5分钟涨跌   | float64 | 注意单位: % |
| 60日涨跌幅  | float64 | 注意单位: % |
| 年初至今涨跌幅 | float64 | 注意单位: % |

接口示例

```python
import akshare as ak

stock_sh_a_spot_em_df = ak.stock_sh_a_spot_em()
print(stock_sh_a_spot_em_df)
```

###### 深 A 股

接口: stock_sz_a_spot_em

目标地址: http://quote.eastmoney.com/center/gridlist.html#sz_a_board

描述: 东方财富网-深 A 股-实时行情数据

限量: 单次返回所有深 A 股上市公司的实时行情数据

输入参数

| 名称  | 类型  | 描述  |
|-----|-----|-----|
| -   | -   | -   |

输出参数

| 名称      | 类型      | 描述      |
|---------|---------|---------|
| 序号      | int64   | -       |
| 代码      | object  | -       |
| 名称      | object  | -       |
| 最新价     | float64 | -       |
| 涨跌幅     | float64 | 注意单位: % |
| 涨跌额     | float64 | -       |
| 成交量     | float64 | 注意单位: 手 |
| 成交额     | float64 | 注意单位: 元 |
| 振幅      | float64 | 注意单位: % |
| 最高      | float64 | -       |
| 最低      | float64 | -       |
| 今开      | float64 | -       |
| 昨收      | float64 | -       |
| 量比      | float64 | -       |
| 换手率     | float64 | 注意单位: % |
| 市盈率-动态  | float64 | -       |
| 市净率     | float64 | -       |
| 总市值     | float64 | 注意单位: 元 |
| 流通市值    | float64 | 注意单位: 元 |
| 涨速      | float64 | -       |
| 5分钟涨跌   | float64 | 注意单位: % |
| 60日涨跌幅  | float64 | 注意单位: % |
| 年初至今涨跌幅 | float64 | 注意单位: % |

接口示例

```python
import akshare as ak

stock_sz_a_spot_em_df = ak.stock_sz_a_spot_em()
print(stock_sz_a_spot_em_df)
```

###### 京 A 股

接口: stock_bj_a_spot_em

目标地址: http://quote.eastmoney.com/center/gridlist.html#bj_a_board

描述: 东方财富网-京 A 股-实时行情数据

限量: 单次返回所有京 A 股上市公司的实时行情数据

输入参数

| 名称  | 类型  | 描述  |
|-----|-----|-----|
| -   | -   | -   |

输出参数

| 名称      | 类型      | 描述      |
|---------|---------|---------|
| 序号      | int64   | -       |
| 代码      | object  | -       |
| 名称      | object  | -       |
| 最新价     | float64 | -       |
| 涨跌幅     | float64 | 注意单位: % |
| 涨跌额     | float64 | -       |
| 成交量     | float64 | 注意单位: 手 |
| 成交额     | float64 | 注意单位: 元 |
| 振幅      | float64 | 注意单位: % |
| 最高      | float64 | -       |
| 最低      | float64 | -       |
| 今开      | float64 | -       |
| 昨收      | float64 | -       |
| 量比      | float64 | -       |
| 换手率     | float64 | 注意单位: % |
| 市盈率-动态  | float64 | -       |
| 市净率     | float64 | -       |
| 总市值     | float64 | 注意单位: 元 |
| 流通市值    | float64 | 注意单位: 元 |
| 涨速      | float64 | -       |
| 5分钟涨跌   | float64 | 注意单位: % |
| 60日涨跌幅  | float64 | 注意单位: % |
| 年初至今涨跌幅 | float64 | 注意单位: % |

接口示例

```python
import akshare as ak

stock_bj_a_spot_em_df = ak.stock_bj_a_spot_em()
print(stock_bj_a_spot_em_df)
```

###### 新股

接口: stock_new_a_spot_em

目标地址: http://quote.eastmoney.com/center/gridlist.html#newshares

描述: 东方财富网-新股-实时行情数据

限量: 单次返回所有新股上市公司的实时行情数据

输入参数

| 名称  | 类型  | 描述  |
|-----|-----|-----|
| -   | -   | -   |

输出参数

| 名称      | 类型      | 描述      |
|---------|---------|---------|
| 序号      | int64   | -       |
| 代码      | object  | -       |
| 名称      | object  | -       |
| 最新价     | float64 | -       |
| 涨跌幅     | float64 | 注意单位: % |
| 涨跌额     | float64 | -       |
| 成交量     | float64 | 注意单位: 手 |
| 成交额     | float64 | 注意单位: 元 |
| 振幅      | float64 | 注意单位: % |
| 最高      | float64 | -       |
| 最低      | float64 | -       |
| 今开      | float64 | -       |
| 昨收      | float64 | -       |
| 量比      | float64 | -       |
| 换手率     | float64 | 注意单位: % |
| 市盈率-动态  | float64 | -       |
| 市净率     | float64 | -       |
| 上市时间    | object  | -       |
| 总市值     | float64 | 注意单位: 元 |
| 流通市值    | float64 | 注意单位: 元 |
| 涨速      | float64 | -       |
| 5分钟涨跌   | float64 | 注意单位: % |
| 60日涨跌幅  | float64 | 注意单位: % |
| 年初至今涨跌幅 | float64 | 注意单位: % |

接口示例

```python
import akshare as ak

stock_new_a_spot_em_df = ak.stock_new_a_spot_em()
print(stock_new_a_spot_em_df)
```

###### 创业板

接口: stock_cy_a_spot_em

目标地址: https://quote.eastmoney.com/center/gridlist.html#gem_board

描述: 东方财富网-创业板-实时行情

限量: 单次返回所有创业板的实时行情数据

输入参数

| 名称  | 类型  | 描述  |
|-----|-----|-----|
| -   | -   | -   |

输出参数

| 名称      | 类型      | 描述      |
|---------|---------|---------|
| 序号      | int64   | -       |
| 代码      | object  | -       |
| 名称      | object  | -       |
| 最新价     | float64 | -       |
| 涨跌幅     | float64 | 注意单位: % |
| 涨跌额     | float64 | -       |
| 成交量     | float64 | 注意单位: 手 |
| 成交额     | float64 | 注意单位: 元 |
| 振幅      | float64 | 注意单位: % |
| 最高      | float64 | -       |
| 最低      | float64 | -       |
| 今开      | float64 | -       |
| 昨收      | float64 | -       |
| 量比      | float64 | -       |
| 换手率     | float64 | 注意单位: % |
| 市盈率-动态  | float64 | -       |
| 市净率     | float64 | -       |
| 总市值     | float64 | 注意单位: 元 |
| 流通市值    | float64 | 注意单位: 元 |
| 涨速      | float64 | -       |
| 5分钟涨跌   | float64 | 注意单位: % |
| 60日涨跌幅  | float64 | 注意单位: % |
| 年初至今涨跌幅 | float64 | 注意单位: % |

接口示例

```python
import akshare as ak

stock_cy_a_spot_em_df = ak.stock_cy_a_spot_em()
print(stock_cy_a_spot_em_df)
```

###### 科创板

接口: stock_kc_a_spot_em

目标地址: http://quote.eastmoney.com/center/gridlist.html#kcb_board

描述: 东方财富网-科创板-实时行情

限量: 单次返回所有科创板的实时行情数据

输入参数

| 名称  | 类型  | 描述  |
|-----|-----|-----|
| -   | -   | -   |

输出参数

| 名称      | 类型      | 描述      |
|---------|---------|---------|
| 序号      | int64   | -       |
| 代码      | object  | -       |
| 名称      | object  | -       |
| 最新价     | float64 | -       |
| 涨跌幅     | float64 | 注意单位: % |
| 涨跌额     | float64 | -       |
| 成交量     | float64 | 注意单位: 手 |
| 成交额     | float64 | 注意单位: 元 |
| 振幅      | float64 | 注意单位: % |
| 最高      | float64 | -       |
| 最低      | float64 | -       |
| 今开      | float64 | -       |
| 昨收      | float64 | -       |
| 量比      | float64 | -       |
| 换手率     | float64 | 注意单位: % |
| 市盈率-动态  | float64 | -       |
| 市净率     | float64 | -       |
| 总市值     | float64 | 注意单位: 元 |
| 流通市值    | float64 | 注意单位: 元 |
| 涨速      | float64 | -       |
| 5分钟涨跌   | float64 | 注意单位: % |
| 60日涨跌幅  | float64 | 注意单位: % |
| 年初至今涨跌幅 | float64 | 注意单位: % |

接口示例

```python
import akshare as ak

stock_kc_a_spot_em_df = ak.stock_kc_a_spot_em()
print(stock_kc_a_spot_em_df)
```

###### AB 股比价

接口: stock_zh_ab_comparison_em

目标地址: https://quote.eastmoney.com/center/gridlist.html#ab_comparison

描述: 东方财富网-行情中心-沪深京个股-AB股比价-全部AB股比价

限量: 单次返回全部 AB 股比价的实时行情数据

输入参数

| 名称  | 类型  | 描述  |
|-----|-----|-----|
| -   | -   | -   |

输出参数

| 名称   | 类型      | 描述 |
|------|---------|----|
| 序号   | int64   | -  |
| B股代码 | object  | -  |
| B股名称 | object  | -  |
| 最新价B | float64 | -  |
| 涨跌幅B | float64 | -  |
| A股代码 | object  | -  |
| A股名称 | object  | -  |
| 最新价A | float64 | -  |
| 涨跌幅A | float64 | -  |
| 比价   | float64 | -  |

接口示例

```python
import akshare as ak

stock_zh_ab_comparison_em_df = ak.stock_zh_ab_comparison_em()
print(stock_zh_ab_comparison_em_df)
```

##### 实时行情数据-新浪

接口: stock_zh_a_spot

目标地址: https://vip.stock.finance.sina.com.cn/mkt/#hs_a

描述: 新浪财经-沪深京 A 股数据, 重复运行本函数会被新浪暂时封 IP, 建议增加时间间隔

限量: 单次返回沪深京 A 股上市公司的实时行情数据

输入参数

| 名称  | 类型  | 描述  |
|-----|-----|-----|
| -   | -   | -   |

输出参数

| 名称  | 类型      | 描述      |
|-----|---------|---------|
| 代码  | object  | -       |
| 名称  | object  | -       |
| 最新价 | float64 | -       |
| 涨跌额 | float64 | -       |
| 涨跌幅 | float64 | 注意单位: % |
| 买入  | float64 | -       |
| 卖出  | float64 | -       |
| 昨收  | float64 | -       |
| 今开  | float64 | -       |
| 最高  | float64 | -       |
| 最低  | float64 | -       |
| 成交量 | float64 | 注意单位: 股 |
| 成交额 | float64 | 注意单位: 元 |
| 时间戳 | object  | -       |

接口示例

```python
import akshare as ak

stock_zh_a_spot_df = ak.stock_zh_a_spot()
print(stock_zh_a_spot_df)
```

##### 实时行情数据-雪球

接口: stock_individual_spot_xq

目标地址: https://xueqiu.com/S/SH513520

描述: 雪球-行情中心-个股

限量: 单次获取指定 symbol 的最新行情数据

输入参数

| 名称      | 类型    | 描述                                                             |
|---------|-------|----------------------------------------------------------------|
| symbol  | str   | symbol="SH600000"; 证券代码，可以是 A 股个股代码，A 股场内基金代码，A 股指数，美股代码, 美股指数 |
| token   | float | token=None; 默认不设置token                                         |
| timeout | float | timeout=None; 默认不设置超时参数                                        |

输出参数

| 名称    | 类型     | 描述 |
|-------|--------|----|
| item  | object | -  |
| value | object | -  |

接口示例

```python
import akshare as ak

stock_individual_spot_xq_df = ak.stock_individual_spot_xq(symbol="SH600000")
print(stock_individual_spot_xq_df)
```

#### 历史行情数据

##### 历史行情数据-东财

接口: stock_zh_a_hist

目标地址: https://quote.eastmoney.com/concept/sh603777.html?from=classic(示例)

描述: 东方财富-沪深京 A 股日频率数据; 历史数据按日频率更新, 当日收盘价请在收盘后获取

限量: 单次返回指定沪深京 A 股上市公司、指定周期和指定日期间的历史行情日频率数据

输入参数

| 名称         | 类型    | 描述                                                       |
|------------|-------|----------------------------------------------------------|
| symbol     | str   | symbol='603777'; 股票代码可以在 **ak.stock_zh_a_spot_em()** 中获取 |
| period     | str   | period='daily'; choice of {'daily', 'weekly', 'monthly'} |
| start_date | str   | start_date='20210301'; 开始查询的日期                           |
| end_date   | str   | end_date='20210616'; 结束查询的日期                             |
| adjust     | str   | 默认返回不复权的数据; qfq: 返回前复权后的数据; hfq: 返回后复权后的数据               |
| timeout    | float | timeout=None; 默认不设置超时参数                                  |

**股票数据复权**

1. 为何要复权：由于股票存在配股、分拆、合并和发放股息等事件，会导致股价出现较大的缺口。
若使用不复权的价格处理数据、计算各种指标，将会导致它们失去连续性，且使用不复权价格计算收益也会出现错误。
为了保证数据连贯性，常通过前复权和后复权对价格序列进行调整。

2. 前复权：保持当前价格不变，将历史价格进行增减，从而使股价连续。
前复权用来看盘非常方便，能一眼看出股价的历史走势，叠加各种技术指标也比较顺畅，是各种行情软件默认的复权方式。
这种方法虽然很常见，但也有两个缺陷需要注意。

    2.1 为了保证当前价格不变，每次股票除权除息，均需要重新调整历史价格，因此其历史价格是时变的。
这会导致在不同时点看到的历史前复权价可能出现差异。

    2.2 对于有持续分红的公司来说，前复权价可能出现负值。

3. 后复权：保证历史价格不变，在每次股票权益事件发生后，调整当前的股票价格。
后复权价格和真实股票价格可能差别较大，不适合用来看盘。
其优点在于，可以被看作投资者的长期财富增长曲线，反映投资者的真实收益率情况。

4. 在量化投资研究中普遍采用后复权数据。

输出参数-历史行情数据

| 名称   | 类型      | 描述          |
|------|---------|-------------|
| 日期   | object  | 交易日         |
| 股票代码 | object  | 不带市场标识的股票代码 |
| 开盘   | float64 | 开盘价         |
| 收盘   | float64 | 收盘价         |
| 最高   | float64 | 最高价         |
| 最低   | float64 | 最低价         |
| 成交量  | int64   | 注意单位: 手     |
| 成交额  | float64 | 注意单位: 元     |
| 振幅   | float64 | 注意单位: %     |
| 涨跌幅  | float64 | 注意单位: %     |
| 涨跌额  | float64 | 注意单位: 元     |
| 换手率  | float64 | 注意单位: %     |

接口示例-历史行情数据-不复权

```python
import akshare as ak

stock_zh_a_hist_df = ak.stock_zh_a_hist(symbol="000001", period="daily", start_date="20170301", end_date='20240528', adjust="")
print(stock_zh_a_hist_df)
```

接口示例-历史行情数据-前复权

```python
import akshare as ak

stock_zh_a_hist_df = ak.stock_zh_a_hist(symbol="000001", period="daily", start_date="20170301", end_date='20240528', adjust="qfq")
print(stock_zh_a_hist_df)
```

接口示例-历史行情数据-后复权

```python
import akshare as ak

stock_zh_a_hist_df = ak.stock_zh_a_hist(symbol="000001", period="daily", start_date="20170301", end_date='20240528', adjust="hfq")
print(stock_zh_a_hist_df)
```

##### 历史行情数据-新浪

接口: stock_zh_a_daily

P.S. 建议切换为 stock_zh_a_hist 接口使用(该接口数据质量高, 访问无限制)

目标地址: https://finance.sina.com.cn/realstock/company/sh600006/nc.shtml(示例)

描述: 新浪财经-沪深京 A 股的数据, 历史数据按日频率更新; 注意其中的 **sh689009** 为 CDR, 请 通过 **ak.stock_zh_a_cdr_daily** 接口获取

限量: 单次返回指定沪深京 A 股上市公司指定日期间的历史行情日频率数据, 多次获取容易封禁 IP

输入参数

| 名称         | 类型  | 描述                                                                                   |
|------------|-----|--------------------------------------------------------------------------------------|
| symbol     | str | symbol='sh600000'; 股票代码可以在 **ak.stock_zh_a_spot()** 中获取                              |
| start_date | str | start_date='20201103'; 开始查询的日期                                                       |
| end_date   | str | end_date='20201116'; 结束查询的日期                                                         |
| adjust     | str | 默认返回不复权的数据; qfq: 返回前复权后的数据; hfq: 返回后复权后的数据; hfq-factor: 返回后复权因子; qfq-factor: 返回前复权因子 |

**股票数据复权**

1.为何要复权：由于股票存在配股、分拆、合并和发放股息等事件，会导致股价出现较大的缺口。
若使用不复权的价格处理数据、计算各种指标，将会导致它们失去连续性，且使用不复权价格计算收益也会出现错误。
为了保证数据连贯性，常通过前复权和后复权对价格序列进行调整。

2.前复权：保持当前价格不变，将历史价格进行增减，从而使股价连续。
前复权用来看盘非常方便，能一眼看出股价的历史走势，叠加各种技术指标也比较顺畅，是各种行情软件默认的复权方式。
这种方法虽然很常见，但也有两个缺陷需要注意。

2.1 为了保证当前价格不变，每次股票除权除息，均需要重新调整历史价格，因此其历史价格是时变的。
这会导致在不同时点看到的历史前复权价可能出现差异。

2.2 对于有持续分红的公司来说，前复权价可能出现负值。

3.后复权：保证历史价格不变，在每次股票权益事件发生后，调整当前的股票价格。
后复权价格和真实股票价格可能差别较大，不适合用来看盘。
其优点在于，可以被看作投资者的长期财富增长曲线，反映投资者的真实收益率情况。

4.在量化投资研究中普遍采用后复权数据。

输出参数-历史行情数据

| 名称                | 类型      | 描述            |
|-------------------|---------|---------------|
| date              | object  | 交易日           |
| open              | float64 | 开盘价           |
| high              | float64 | 最高价           |
| low               | float64 | 最低价           |
| close             | float64 | 收盘价           |
| volume            | float64 | 成交量; 注意单位: 股  |
| amount            | float64 | 成交额; 注意单位: 元  |
| outstanding_share | float64 | 流动股本; 注意单位: 股 |
| turnover          | float64 | 换手率=成交量/流动股本  |

接口示例-历史行情数据(前复权)

```python
import akshare as ak

stock_zh_a_daily_qfq_df = ak.stock_zh_a_daily(symbol="sz000001", start_date="19910403", end_date="20231027", adjust="qfq")
print(stock_zh_a_daily_qfq_df)
```

接口示例-历史行情数据(后复权)

```python
import akshare as ak

stock_zh_a_daily_hfq_df = ak.stock_zh_a_daily(symbol="sz000001", start_date="19910403", end_date="20231027", adjust="hfq")
print(stock_zh_a_daily_hfq_df)
```

接口示例-前复权因子

```python
import akshare as ak

qfq_factor_df = ak.stock_zh_a_daily(symbol="sz000002", adjust="qfq-factor")
print(qfq_factor_df)
```

接口示例-后复权因子

```python
import akshare as ak

hfq_factor_df = ak.stock_zh_a_daily(symbol="sz000002", adjust="hfq-factor")
print(hfq_factor_df)
```

##### 历史行情数据-腾讯

接口: stock_zh_a_hist_tx

目标地址: https://gu.qq.com/sh000919/zs

描述: 腾讯证券-日频-股票历史数据; 历史数据按日频率更新, 当日收盘价请在收盘后获取

限量: 单次返回指定沪深京 A 股上市公司、指定周期和指定日期间的历史行情日频率数据

输入参数

| 名称         | 类型    | 描述                                         |
|------------|-------|--------------------------------------------|
| symbol     | str   | symbol='sz000001'; 带市场标识                   |
| start_date | str   | start_date='19000101'; 开始查询的日期             |
| end_date   | str   | end_date='20500101'; 结束查询的日期               |
| adjust     | str   | 默认返回不复权的数据; qfq: 返回前复权后的数据; hfq: 返回后复权后的数据 |
| timeout    | float | timeout=None; 默认不设置超时参数                    |

**股票数据复权**

1.为何要复权：由于股票存在配股、分拆、合并和发放股息等事件，会导致股价出现较大的缺口。
若使用不复权的价格处理数据、计算各种指标，将会导致它们失去连续性，且使用不复权价格计算收益也会出现错误。
为了保证数据连贯性，常通过前复权和后复权对价格序列进行调整。

2.前复权：保持当前价格不变，将历史价格进行增减，从而使股价连续。
前复权用来看盘非常方便，能一眼看出股价的历史走势，叠加各种技术指标也比较顺畅，是各种行情软件默认的复权方式。
这种方法虽然很常见，但也有两个缺陷需要注意。

2.1 为了保证当前价格不变，每次股票除权除息，均需要重新调整历史价格，因此其历史价格是时变的。
这会导致在不同时点看到的历史前复权价可能出现差异。

2.2 对于有持续分红的公司来说，前复权价可能出现负值。

3.后复权：保证历史价格不变，在每次股票权益事件发生后，调整当前的股票价格。
后复权价格和真实股票价格可能差别较大，不适合用来看盘。
其优点在于，可以被看作投资者的长期财富增长曲线，反映投资者的真实收益率情况。

4.在量化投资研究中普遍采用后复权数据。

输出参数-历史行情数据

| 名称     | 类型      | 描述      |
|--------|---------|---------|
| date   | object  | 交易日     |
| open   | float64 | 开盘价     |
| close  | float64 | 收盘价     |
| high   | float64 | 最高价     |
| low    | float64 | 最低价     |
| amount | int64   | 注意单位: 手 |

接口示例-不复权

```python
import akshare as ak

stock_zh_a_hist_tx_df = ak.stock_zh_a_hist_tx(symbol="sz000001", start_date="20200101", end_date="20231027", adjust="")
print(stock_zh_a_hist_tx_df)
```

接口示例-前复权

```python
import akshare as ak

stock_zh_a_hist_tx_df = ak.stock_zh_a_hist_tx(symbol="sz000001", start_date="20200101", end_date="20231027", adjust="qfq")
print(stock_zh_a_hist_tx_df)
```

接口示例-后复权

```python
import akshare as ak

stock_zh_a_hist_tx_df = ak.stock_zh_a_hist_tx(symbol="sz000001", start_date="20200101", end_date="20231027", adjust="hfq")
print(stock_zh_a_hist_tx_df)
```

##### 分时数据-新浪

接口: stock_zh_a_minute

目标地址: http://finance.sina.com.cn/realstock/company/sh600519/nc.shtml

描述: 新浪财经-沪深京 A 股股票或者指数的分时数据，目前可以获取 1, 5, 15, 30, 60 分钟的数据频率, 可以指定是否复权

限量: 单次返回指定股票或指数的指定频率的最近交易日的历史分时行情数据; 注意调用频率

输入参数

| 名称     | 类型  | 描述                                                         |
|--------|-----|------------------------------------------------------------|
| symbol | str | symbol='sh000300'; 同日频率数据接口                                |
| period | str | period='1'; 获取 1, 5, 15, 30, 60 分钟的数据频率                    |
| adjust | str | adjust=""; 默认为空: 返回不复权的数据; qfq: 返回前复权后的数据; hfq: 返回后复权后的数据; |

输出参数

| 名称     | 类型      | 描述  |
|--------|---------|-----|
| day    | object  | -   |
| open   | float64 | -   |
| high   | float64 | -   |
| low    | float64 | -   |
| close  | float64 | -   |
| volume | float64 | -   |
| amount | float64 | -   |

接口示例

```python
import akshare as ak

stock_zh_a_minute_df = ak.stock_zh_a_minute(symbol='sh600751', period='1', adjust="qfq")
print(stock_zh_a_minute_df)
```

##### 分时数据-东财

接口: stock_zh_a_hist_min_em

目标地址: https://quote.eastmoney.com/concept/sh603777.html

描述: 东方财富网-行情首页-沪深京 A 股-每日分时行情; 该接口只能获取近期的分时数据，注意时间周期的设置

限量: 单次返回指定股票、频率、复权调整和时间区间的分时数据, 其中 1 分钟数据只返回近 5 个交易日数据且不复权

输入参数

| 名称         | 类型  | 描述                                                                                                  |
|------------|-----|-----------------------------------------------------------------------------------------------------|
| symbol     | str | symbol='000300'; 股票代码                                                                               |
| start_date | str | start_date="1979-09-01 09:32:00"; 日期时间; 默认返回所有数据                                                    |
| end_date   | str | end_date="2222-01-01 09:32:00"; 日期时间; 默认返回所有数据                                                      |
| period     | str | period='5'; choice of {'1', '5', '15', '30', '60'}; 其中 1 分钟数据返回近 5 个交易日数据且不复权                       |
| adjust     | str | adjust=''; choice of {'', 'qfq', 'hfq'}; '': 不复权, 'qfq': 前复权, 'hfq': 后复权, 其中 1 分钟数据返回近 5 个交易日数据且不复权 |

输出参数-1分钟数据

| 名称  | 类型      | 描述      |
|-----|---------|---------|
| 时间  | object  | -       |
| 开盘  | float64 | -       |
| 收盘  | float64 | -       |
| 最高  | float64 | -       |
| 最低  | float64 | -       |
| 成交量 | float64 | 注意单位: 手 |
| 成交额 | float64 | -       |
| 均价  | float64 | -       |

接口示例-1分钟数据

```python
import akshare as ak

# 注意：该接口返回的数据只有最近一个交易日的有开盘价，其他日期开盘价为 0
stock_zh_a_hist_min_em_df = ak.stock_zh_a_hist_min_em(symbol="000001", start_date="2024-03-20 09:30:00", end_date="2024-03-20 15:00:00", period="1", adjust="")
print(stock_zh_a_hist_min_em_df)
```

输出参数-其他

| 名称  | 类型      | 描述      |
|-----|---------|---------|
| 时间  | object  | -       |
| 开盘  | float64 | -       |
| 收盘  | float64 | -       |
| 最高  | float64 | -       |
| 最低  | float64 | -       |
| 涨跌幅 | float64 | 注意单位: % |
| 涨跌额 | float64 | -       |
| 成交量 | float64 | 注意单位: 手 |
| 成交额 | float64 | -       |
| 振幅  | float64 | 注意单位: % |
| 换手率 | float64 | 注意单位: % |

接口示例-其他

```python
import akshare as ak

stock_zh_a_hist_min_em_df = ak.stock_zh_a_hist_min_em(symbol="000001", start_date="2024-03-20 09:30:00", end_date="2024-03-20 15:00:00", period="5", adjust="hfq")
print(stock_zh_a_hist_min_em_df)
```

##### 日内分时数据-东财

接口: stock_intraday_em

目标地址: https://quote.eastmoney.com/f1.html?newcode=0.000001

描述: 东方财富-分时数据

限量: 单次返回指定股票最近一个交易日的分时数据, 包含盘前数据

输入参数

| 名称         | 类型  | 描述                                  |
|------------|-----|-------------------------------------|
| symbol     | str | symbol="000001"; 股票代码               |

输出参数

| 名称    | 类型      | 描述 |
|-------|---------|----|
| 时间    | object  | -  |
| 成交价   | float64 | -  |
| 手数    | int64   | -  |
| 买卖盘性质 | object  | -  |

接口示例

```python
import akshare as ak

stock_intraday_em_df = ak.stock_intraday_em(symbol="000001")
print(stock_intraday_em_df)
```

##### 日内分时数据-新浪

接口: stock_intraday_sina

目标地址: https://vip.stock.finance.sina.com.cn/quotes_service/view/cn_bill.php?symbol=sz000001

描述: 新浪财经-日内分时数据

限量: 单次返回指定交易日的分时数据；只能获取近期的数据，此处仅返回大单数据（成交量大于等于: 400手）

输入参数

| 名称     | 类型  | 描述                            |
|--------|-----|-------------------------------|
| symbol | str | symbol="sz000001"; 带市场标识的股票代码 |
| date   | str | date="20240321"; 交易日          |

输出参数

| 名称         | 类型      | 描述            |
|------------|---------|---------------|
| symbol     | object  | -             |
| name       | object  | -             |
| ticktime   | object  | -             |
| price      | float64 | -             |
| volume     | int64   | 注意单位: 股       |
| prev_price | float64 | -             |
| kind       | object  | D 表示卖盘，表示 是买盘 |

接口示例

```python
import akshare as ak

stock_intraday_sina_df = ak.stock_intraday_sina(symbol="sz000001", date="20240321")
print(stock_intraday_sina_df)
```

##### 盘前数据

接口: stock_zh_a_hist_pre_min_em

目标地址: https://quote.eastmoney.com/concept/sh603777.html

描述: 东方财富-股票行情-盘前数据

限量: 单次返回指定 symbol 的最近一个交易日的股票分钟数据, 包含盘前分钟数据

输入参数

| 名称         | 类型  | 描述                                  |
|------------|-----|-------------------------------------|
| symbol     | str | symbol="000001"; 股票代码               |
| start_time | str | start_time="09:00:00"; 时间; 默认返回所有数据 |
| end_time   | str | end_time="15:40:00"; 时间; 默认返回所有数据   |

输出参数

| 名称  | 类型      | 描述      |
|-----|---------|---------|
| 时间  | object  | -       |
| 开盘  | float64 | -       |
| 收盘  | float64 | -       |
| 最高  | float64 | -       |
| 最低  | float64 | -       |
| 成交量 | float64 | 注意单位: 手 |
| 成交额 | float64 | -       |
| 最新价 | float64 | -       |

接口示例

```python
import akshare as ak

stock_zh_a_hist_pre_min_em_df = ak.stock_zh_a_hist_pre_min_em(symbol="000001", start_time="09:00:00", end_time="15:40:00")
print(stock_zh_a_hist_pre_min_em_df)
```

#### 历史分笔数据

##### 腾讯财经

接口: stock_zh_a_tick_tx

目标地址: http://gu.qq.com/sz300494/gp/detail(示例)

描述: 每个交易日 16:00 提供当日数据; 如遇到数据缺失, 请使用 **ak.stock_zh_a_tick_163()** 接口(注意数据会有一定差异)

限量: 单次返回最近交易日的历史分笔行情数据

输入参数-历史行情数据

| 名称         | 类型  | 描述                    |
|------------|-----|-----------------------|
| symbol     | str | symbol="sh600000"     |

输出参数

| 名称   | 类型      | 描述      |
|------|---------|---------|
| 成交时间 | object  | -       |
| 成交价格 | float64 | 注意单位: 元 |
| 价格变动 | float64 | 注意单位: 元 |
| 成交量  | int32   | 注意单位: 手 |
| 成交额  | int32   | 注意单位: 元 |
| 性质   | object  | 买卖盘标记   |

接口示例

```python
import akshare as ak

stock_zh_a_tick_tx_js_df = ak.stock_zh_a_tick_tx_js(symbol="sz000001")
print(stock_zh_a_tick_tx_js_df)
```


#### 同行比较

##### 成长性比较

接口: stock_zh_growth_comparison_em

目标地址: https://emweb.securities.eastmoney.com/pc_hsf10/pages/index.html?type=web&code=000895&color=b#/thbj/czxbj

描述: 东方财富-行情中心-同行比较-成长性比较

限量: 单次返回全部数据

输入参数

| 名称         | 类型  | 描述                    |
|------------|-----|-----------------------|
| symbol     | str | symbol="SZ000895"     |

输出参数

| 名称               | 类型      | 描述 |
|------------------|---------|----|
| 代码               | object  | -  |
| 简称               | object  | -  |
| 基本每股收益增长率-3年复合   | float64 | -  |
| 基本每股收益增长率-24A    | float64 | -  |
| 基本每股收益增长率-TTM    | float64 | -  |
| 基本每股收益增长率-25E    | float64 | -  |
| 基本每股收益增长率-26E    | float64 | -  |
| 基本每股收益增长率-27E    | float64 | -  |
| 营业收入增长率-3年复合     | float64 | -  |
| 营业收入增长率-24A      | float64 | -  |
| 营业收入增长率-TTM      | float64 | -  |
| 营业收入增长率-25E      | float64 | -  |
| 营业收入增长率-26E      | float64 | -  |
| 营业收入增长率-27E      | float64 | -  |
| 净利润增长率-3年复合      | float64 | -  |
| 净利润增长率-24A       | float64 | -  |
| 净利润增长率-TTM       | float64 | -  |
| 净利润增长率-25E       | float64 | -  |
| 净利润增长率-26E       | float64 | -  |
| 净利润增长率-27E       | float64 | -  |
| 基本每股收益增长率-3年复合排名 | float64 | -  |

接口示例

```python
import akshare as ak

stock_zh_growth_comparison_em_df = ak.stock_zh_growth_comparison_em(symbol="SZ000895")
print(stock_zh_growth_comparison_em_df)
```

##### 估值比较

接口: stock_zh_valuation_comparison_em

目标地址: https://emweb.securities.eastmoney.com/pc_hsf10/pages/index.html?type=web&code=000895&color=b#/thbj/gzbj

描述: 东方财富-行情中心-同行比较-估值比较

限量: 单次返回全部数据

输入参数

| 名称         | 类型  | 描述                    |
|------------|-----|-----------------------|
| symbol     | str | symbol="SZ000895"     |

输出参数

| 名称            | 类型      | 描述 |
|---------------|---------|----|
| 排名            | object  | -  |
| 代码            | object  | -  |
| 简称            | object  | -  |
| PEG           | float64 | -  |
| 市盈率-24A       | float64 | -  |
| 市盈率-TTM       | float64 | -  |
| 市盈率-25E       | float64 | -  |
| 市盈率-26E       | float64 | -  |
| 市盈率-27E       | float64 | -  |
| 市销率-24A       | float64 | -  |
| 市销率-TTM       | float64 | -  |
| 市销率-25E       | float64 | -  |
| 市销率-26E       | float64 | -  |
| 市销率-27E       | float64 | -  |
| 市净率-24A       | float64 | -  |
| 市净率-MRQ       | float64 | -  |
| 市现率1-24A      | float64 | -  |
| 市现率1-TTM      | float64 | -  |
| 市现率2-24A      | float64 | -  |
| 市现率2-TTM      | float64 | -  |
| EV/EBITDA-24A | float64 | -  |

接口示例

```python
import akshare as ak

stock_zh_valuation_comparison_em_df = ak.stock_zh_valuation_comparison_em(symbol="SZ000895")
print(stock_zh_valuation_comparison_em_df)
```

##### 杜邦分析比较

接口: stock_zh_dupont_comparison_em

目标地址: https://emweb.securities.eastmoney.com/pc_hsf10/pages/index.html?type=web&code=000895&color=b#/thbj/dbfxbj

描述: 东方财富-行情中心-同行比较-杜邦分析比较

限量: 单次返回全部数据

输入参数

| 名称         | 类型  | 描述                    |
|------------|-----|-----------------------|
| symbol     | str | symbol="SZ000895"     |

输出参数

| 名称          | 类型      | 描述 |
|-------------|---------|----|
| 代码          | object  | -  |
| 简称          | object  | -  |
| ROE-3年平均    | float64 | -  |
| ROE-22A     | float64 | -  |
| ROE-23A     | float64 | -  |
| ROE-24A     | float64 | -  |
| 净利率-3年平均    | float64 | -  |
| 净利率-22A     | float64 | -  |
| 净利率-23A     | float64 | -  |
| 净利率-24A     | float64 | -  |
| 总资产周转率-3年平均 | float64 | -  |
| 总资产周转率-22A  | float64 | -  |
| 总资产周转率-23A  | float64 | -  |
| 总资产周转率-24A  | float64 | -  |
| 权益乘数-3年平均   | float64 | -  |
| 权益乘数-22A    | float64 | -  |
| 权益乘数-23A    | float64 | -  |
| 权益乘数-24A    | float64 | -  |
| ROE-3年平均排名  | float64 | -  |


接口示例

```python
import akshare as ak

stock_zh_dupont_comparison_em_df = ak.stock_zh_dupont_comparison_em(symbol="SZ000895")
print(stock_zh_dupont_comparison_em_df)
```

##### 公司规模

接口: stock_zh_scale_comparison_em

目标地址: https://emweb.securities.eastmoney.com/pc_hsf10/pages/index.html?type=web&code=000895&color=b#/thbj/gsgm

描述: 东方财富-行情中心-同行比较-公司规模

限量: 单次返回全部数据

输入参数

| 名称         | 类型  | 描述                    |
|------------|-----|-----------------------|
| symbol     | str | symbol="SZ000895"     |

输出参数

| 名称     | 类型      | 描述 |
|--------|---------|----|
| 代码     | object  | -  |
| 简称     | object  | -  |
| 总市值    | float64 | -  |
| 总市值排名  | int64   | -  |
| 流通市值   | float64 | -  |
| 流通市值排名 | int64   | -  |
| 营业收入   | float64 | -  |
| 营业收入排名 | int64   | -  |
| 净利润    | float64 | -  |
| 净利润排名  | int64   | -  |

接口示例

```python
import akshare as ak

stock_zh_scale_comparison_em_df = ak.stock_zh_scale_comparison_em(symbol="SZ000895")
print(stock_zh_scale_comparison_em_df)
```

### A股-CDR

#### 历史行情数据

接口: stock_zh_a_cdr_daily

目标地址: https://finance.sina.com.cn/realstock/company/sh689009/nc.shtml

描述: 上海证券交易所-科创板-CDR

限量: 单次返回指定 CDR 的日频率数据, 分钟历史行情数据可以通过 stock_zh_a_minute 获取

名词解释:

1. [Investopedia-CDR](https://www.investopedia.com/terms/c/cdr.asp)
2. [百度百科-中国存托凭证](https://baike.baidu.com/item/%E4%B8%AD%E5%9B%BD%E5%AD%98%E6%89%98%E5%87%AD%E8%AF%81/2489906?fr=aladdin)

输入参数

| 名称         | 类型  | 描述                          |
|------------|-----|-----------------------------|
| symbol     | str | symbol='sh689009'; CDR 股票代码 |
| start_date | str | start_date='20201103'       |
| end_date   | str | end_date='20201116'         |

输出参数

| 名称     | 类型      | 描述      |
|--------|---------|---------|
| date   | object  | 交易日     |
| open   | float64 | -       |
| high   | float64 | -       |
| low    | float64 | -       |
| close  | float64 | -       |
| volume | float64 | 注意单位: 手 |

接口示例

```python
import akshare as ak

stock_zh_a_cdr_daily_df = ak.stock_zh_a_cdr_daily(symbol='sh689009', start_date='20201103', end_date='20201116')
print(stock_zh_a_cdr_daily_df)
```

### B股

#### 实时行情数据

##### 实时行情数据-东财

接口: stock_zh_b_spot_em

目标地址: http://quote.eastmoney.com/center/gridlist.html#hs_b_board

描述: 东方财富网-实时行情数据

限量: 单次返回所有 B 股上市公司的实时行情数据

输入参数

| 名称  | 类型  | 描述  |
|-----|-----|-----|
| -   | -   | -   |

输出参数

| 名称      | 类型      | 描述      |
|---------|---------|---------|
| 序号      | int64   | -       |
| 代码      | object  | -       |
| 名称      | object  | -       |
| 最新价     | float64 | -       |
| 涨跌幅     | float64 | 注意单位: % |
| 涨跌额     | float64 | -       |
| 成交量     | float64 | 注意单位: 手 |
| 成交额     | float64 | 注意单位: 元 |
| 振幅      | float64 | 注意单位: % |
| 最高      | float64 | -       |
| 最低      | float64 | -       |
| 今开      | float64 | -       |
| 昨收      | float64 | -       |
| 量比      | float64 | -       |
| 换手率     | float64 | 注意单位: % |
| 市盈率-动态  | float64 | -       |
| 市净率     | float64 | -       |
| 总市值     | float64 | 注意单位: 元 |
| 流通市值    | float64 | 注意单位: 元 |
| 涨速      | float64 | -       |
| 5分钟涨跌   | float64 | 注意单位: % |
| 60日涨跌幅  | float64 | 注意单位: % |
| 年初至今涨跌幅 | float64 | 注意单位: % |

接口示例

```python
import akshare as ak

stock_zh_b_spot_em_df = ak.stock_zh_b_spot_em()
print(stock_zh_b_spot_em_df)
```

##### 实时行情数据-新浪

接口: stock_zh_b_spot

目标地址: http://vip.stock.finance.sina.com.cn/mkt/#hs_b

描述: B 股数据是从新浪财经获取的数据, 重复运行本函数会被新浪暂时封 IP, 建议增加时间间隔

限量: 单次返回所有 B 股上市公司的实时行情数据

输入参数-实时行情数据

| 名称  | 类型  | 描述  |
|-----|-----|-----|
| -   | -   | -   |

输出参数-实时行情数据

| 名称  | 类型      | 描述      |
|-----|---------|---------|
| 代码  | object  | -       |
| 名称  | object  | -       |
| 最新价 | float64 | -       |
| 涨跌额 | float64 | -       |
| 涨跌幅 | float64 | 注意单位: % |
| 买入  | float64 | -       |
| 卖出  | float64 | -       |
| 昨收  | float64 | -       |
| 今开  | float64 | -       |
| 最高  | float64 | -       |
| 最低  | float64 | -       |
| 成交量 | float64 | 注意单位: 股 |
| 成交额 | float64 | 注意单位: 元 |

接口示例-实时行情数据

```python
import akshare as ak

stock_zh_b_spot_df = ak.stock_zh_b_spot()
print(stock_zh_b_spot_df)
```

#### 历史行情数据

##### 历史行情数据

接口: stock_zh_b_daily

目标地址: https://finance.sina.com.cn/realstock/company/sh900901/nc.shtml

描述: B 股数据是从新浪财经获取的数据, 历史数据按日频率更新

限量: 单次返回指定 B 股上市公司指定日期间的历史行情日频率数据

输入参数

| 名称         | 类型  | 描述                                                                                   |
|------------|-----|--------------------------------------------------------------------------------------|
| symbol     | str | symbol='sh900901'; 股票代码可以在 **ak.stock_zh_b_spot()** 中获取                              |
| start_date | str | start_date='20201103'; 开始查询的日期                                                       |
| end_date   | str | end_date='20201116'; 结束查询的日期                                                         |
| adjust     | str | 默认返回不复权的数据; qfq: 返回前复权后的数据; hfq: 返回后复权后的数据; hfq-factor: 返回后复权因子; qfq-factor: 返回前复权因子 |

**股票数据复权**

1.为何要复权：由于股票存在配股、分拆、合并和发放股息等事件，会导致股价出现较大的缺口。
若使用不复权的价格处理数据、计算各种指标，将会导致它们失去连续性，且使用不复权价格计算收益也会出现错误。
为了保证数据连贯性，常通过前复权和后复权对价格序列进行调整。

2.前复权：保持当前价格不变，将历史价格进行增减，从而使股价连续。
前复权用来看盘非常方便，能一眼看出股价的历史走势，叠加各种技术指标也比较顺畅，是各种行情软件默认的复权方式。
这种方法虽然很常见，但也有两个缺陷需要注意。

2.1 为了保证当前价格不变，每次股票除权除息，均需要重新调整历史价格，因此其历史价格是时变的。
这会导致在不同时点看到的历史前复权价可能出现差异。

2.2 对于有持续分红的公司来说，前复权价可能出现负值。

3.后复权：保证历史价格不变，在每次股票权益事件发生后，调整当前的股票价格。
后复权价格和真实股票价格可能差别较大，不适合用来看盘。
其优点在于，可以被看作投资者的长期财富增长曲线，反映投资者的真实收益率情况。

4.在量化投资研究中普遍采用后复权数据。

输出参数-历史行情数据

| 名称                | 类型      | 描述            |
|-------------------|---------|---------------|
| date              | object  | 交易日           |
| close             | float64 | 收盘价           |
| high              | float64 | 最高价           |
| low               | float64 | 最低价           |
| open              | float64 | 开盘价           |
| volume            | float64 | 成交量; 注意单位: 股  |
| outstanding_share | float64 | 流动股本; 注意单位: 股 |
| turnover          | float64 | 换手率=成交量/流动股本  |

接口示例-历史行情数据(前复权)

```python
import akshare as ak

stock_zh_b_daily_qfq_df = ak.stock_zh_b_daily(symbol="sh900901", start_date="19900103", end_date="20240722", adjust="qfq")
print(stock_zh_b_daily_qfq_df)
```

接口示例-历史行情数据(后复权)

```python
import akshare as ak

stock_zh_b_daily_hfq_df = ak.stock_zh_b_daily(symbol="sh900901", start_date="19900103", end_date="20240722", adjust="hfq")
print(stock_zh_b_daily_hfq_df)
```

接口示例-前复权因子

```python
import akshare as ak

qfq_factor_df = ak.stock_zh_b_daily(symbol="sh900901", adjust="qfq-factor")
print(qfq_factor_df)
```

接口示例-后复权因子

```python
import akshare as ak

hfq_factor_df = ak.stock_zh_b_daily(symbol="sh900901", adjust="hfq-factor")
print(hfq_factor_df)
```

##### 分时数据

接口: stock_zh_b_minute

目标地址: http://finance.sina.com.cn/realstock/company/sh900901/nc.shtml

描述: 新浪财经 B 股股票或者指数的分时数据，目前可以获取 1, 5, 15, 30, 60 分钟的数据频率, 可以指定是否复权

限量: 单次返回指定股票或指数的指定频率的最近交易日的历史分时行情数据

输入参数

| 名称     | 类型  | 描述                                                         |
|--------|-----|------------------------------------------------------------|
| symbol | str | symbol='sh900901'; 同日频率数据接口                                |
| period | str | period='1'; 获取 1, 5, 15, 30, 60 分钟的数据频率                    |
| adjust | str | adjust=""; 默认为空: 返回不复权的数据; qfq: 返回前复权后的数据; hfq: 返回后复权后的数据; |

输出参数

| 名称     | 类型      | 描述  |
|--------|---------|-----|
| day    | object  | -   |
| open   | float64 | -   |
| high   | float64 | -   |
| low    | float64 | -   |
| close  | float64 | -   |
| volume | float64 | -   |

接口示例

```python
import akshare as ak

stock_zh_b_minute_df = ak.stock_zh_b_minute(symbol='sh900901', period='1', adjust="qfq")
print(stock_zh_b_minute_df)
```

### 次新股

接口: stock_zh_a_new

目标地址: http://vip.stock.finance.sina.com.cn/mkt/#new_stock

描述: 新浪财经-行情中心-沪深股市-次新股

限量: 单次返回所有次新股行情数据, 由于次新股名单随着交易日变化而变化，只能获取最近交易日的数据

输入参数

| 名称  | 类型  | 描述  |
|-----|-----|-----|
| -   | -   | -   |

输出参数

| 名称            | 类型      | 描述   |
|---------------|---------|------|
| symbol        | object  | 新浪代码 |
| code          | object  | 股票代码 |
| name          | object  | 股票简称 |
| open          | float64 | 开盘价  |
| high          | float64 | 最高价  |
| low           | float64 | 最低价  |
| volume        | int64   | 成交量  |
| amount        | int64   | 成交额  |
| mktcap        | float64 | 市值   |
| turnoverratio | float64 | 换手率  |

接口示例

```python
import akshare as ak

stock_zh_a_new_df = ak.stock_zh_a_new()
print(stock_zh_a_new_df)
```

### 股市日历

#### 公司动态

接口: stock_gsrl_gsdt_em

目标地址: https://data.eastmoney.com/gsrl/gsdt.html

描述: 东方财富网-数据中心-股市日历-公司动态

限量: 单次返回指定交易日的数据

输入参数

| 名称   | 类型  | 描述                   |
|------|-----|----------------------|
| date | str | date="20230808"; 交易日 |

输出参数

| 名称   | 类型     | 描述 |
|------|--------|----|
| 序号   | int64  | -  |
| 代码   | object | -  |
| 简称   | object | -  |
| 事件类型 | object | -  |
| 具体事项 | object | -  |
| 交易日  | object | -  |

接口示例

```python
import akshare as ak

stock_gsrl_gsdt_em_df = ak.stock_gsrl_gsdt_em(date="20230808")
print(stock_gsrl_gsdt_em_df)
```

### 风险警示板

接口: stock_zh_a_st_em

目标地址: https://quote.eastmoney.com/center/gridlist.html#st_board

描述: 东方财富网-行情中心-沪深个股-风险警示板

限量: 单次返回当前交易日风险警示板的所有股票的行情数据

输入参数

| 名称  | 类型  | 描述  |
|-----|-----|-----|
| -   | -   | -   |

输出参数

| 名称     | 类型      | 描述      |
|--------|---------|---------|
| 序号     | int64   | -       |
| 代码     | object  | -       |
| 名称     | object  | -       |
| 最新价    | float64 | -       |
| 涨跌幅    | float64 | 注意单位: % |
| 涨跌额    | float64 | -       |
| 成交量    | float64 | -       |
| 成交额    | float64 | -       |
| 振幅     | float64 | 注意单位: % |
| 最高     | float64 | -       |
| 最低     | float64 | -       |
| 今开     | float64 | -       |
| 昨收     | float64 | -       |
| 量比     | float64 | -       |
| 换手率    | float64 | 注意单位: % |
| 市盈率-动态 | float64 | -       |
| 市净率    | float64 | -       |

接口示例

```python
import akshare as ak

stock_zh_a_st_em_df = ak.stock_zh_a_st_em()
print(stock_zh_a_st_em_df)
```

### 新股

接口: stock_zh_a_new_em

目标地址: https://quote.eastmoney.com/center/gridlist.html#newshares

描述: 东方财富网-行情中心-沪深个股-新股

限量: 单次返回当前交易日新股板块的所有股票的行情数据

输入参数

| 名称  | 类型  | 描述  |
|-----|-----|-----|
| -   | -   | -   |

输出参数

| 名称     | 类型      | 描述      |
|--------|---------|---------|
| 序号     | int64   | -       |
| 代码     | object  | -       |
| 名称     | object  | -       |
| 最新价    | float64 | -       |
| 涨跌幅    | float64 | 注意单位: % |
| 涨跌额    | float64 | -       |
| 成交量    | float64 | -       |
| 成交额    | float64 | -       |
| 振幅     | float64 | 注意单位: % |
| 最高     | float64 | -       |
| 最低     | float64 | -       |
| 今开     | float64 | -       |
| 昨收     | float64 | -       |
| 量比     | float64 | -       |
| 换手率    | float64 | 注意单位: % |
| 市盈率-动态 | float64 | -       |
| 市净率    | float64 | -       |

接口示例

```python
import akshare as ak

stock_zh_a_new_em_df = ak.stock_zh_a_new_em()
print(stock_zh_a_new_em_df)
```

### 新股上市首日

接口: stock_xgsr_ths

目标地址: https://data.10jqka.com.cn/ipo/xgsr/

描述: 同花顺-数据中心-新股数据-新股上市首日

限量: 单次返回当前交易日的所有数据

输入参数

| 名称  | 类型  | 描述  |
|-----|-----|-----|
| -   | -   | -   |

输出参数

| 名称    | 类型      | 描述 |
|-------|---------|----|
| 序号    | int64   | -  |
| 股票代码  | object  | -  |
| 股票简称  | object  | -  |
| 上市日期  | object  | -  |
| 发行价   | float64 | -  |
| 最新价   | float64 | -  |
| 首日开盘价 | float64 | -  |
| 首日收盘价 | float64 | -  |
| 首日最高价 | float64 | -  |
| 首日最低价 | float64 | -  |
| 首日涨跌幅 | float64 | -  |
| 是否破发  | object  | -  |

接口示例

```python
import akshare as ak

stock_xgsr_ths_df = ak.stock_xgsr_ths()
print(stock_xgsr_ths_df)
```

### IPO 受益股

接口: stock_ipo_benefit_ths

目标地址: https://data.10jqka.com.cn/ipo/syg/

描述: 同花顺-数据中心-新股数据-IPO受益股

限量: 单次返回当前交易日的所有数据; 该数据每周更新一次, 返回最近一周的数据

输入参数

| 名称  | 类型  | 描述  |
|-----|-----|-----|
| -   | -   | -   |

输出参数

| 名称     | 类型      | 描述      |
|--------|---------|---------|
| 序号     | int64   | -       |
| 股票代码   | object  | -       |
| 股票简称   | object  | -       |
| 收盘价    | float64 | 注意单位: 元 |
| 涨跌幅    | float64 | 注意单位: % |
| 市值     | object  | 注意单位: 元 |
| 参股家数   | int64   | -       |
| 投资总额   | object  | 注意单位: 元 |
| 投资占市值比 | float64 | 注意单位: % |
| 参股对象   | object  | -       |

接口示例

```python
import akshare as ak

stock_ipo_benefit_ths_df = ak.stock_ipo_benefit_ths()
print(stock_ipo_benefit_ths_df)
```

### 两网及退市

接口: stock_zh_a_stop_em

目标地址: http://quote.eastmoney.com/center/gridlist.html#staq_net_board

描述: 东方财富网-行情中心-沪深个股-两网及退市

限量: 单次返回当前交易日两网及退市的所有股票的行情数据

输入参数

| 名称  | 类型  | 描述  |
|-----|-----|-----|
| -   | -   | -   |

输出参数

| 名称     | 类型      | 描述      |
|--------|---------|---------|
| 序号     | int64   | -       |
| 代码     | object  | -       |
| 名称     | object  | -       |
| 最新价    | float64 | -       |
| 涨跌幅    | float64 | 注意单位: % |
| 涨跌额    | float64 | -       |
| 成交量    | float64 | -       |
| 成交额    | float64 | -       |
| 振幅     | float64 | 注意单位: % |
| 最高     | float64 | -       |
| 最低     | float64 | -       |
| 今开     | float64 | -       |
| 昨收     | float64 | -       |
| 量比     | float64 | -       |
| 换手率    | float64 | 注意单位: % |
| 市盈率-动态 | float64 | -       |
| 市净率    | float64 | -       |

接口示例

```python
import akshare as ak

stock_zh_a_stop_em_df = ak.stock_zh_a_stop_em()
print(stock_zh_a_stop_em_df)
```

### 科创板

#### 实时行情数据

接口: stock_zh_kcb_spot

目标地址: http://vip.stock.finance.sina.com.cn/mkt/#kcb

描述: 新浪财经-科创板股票实时行情数据

限量: 单次返回所有科创板上市公司的实时行情数据; 请控制采集的频率, 大量抓取容易封IP

输入参数

| 名称  | 类型  | 描述  |
|-----|-----|-----|
| -   | -   | -   |

输出参数-实时行情数据

| 名称   | 类型      | 描述           |
|------|---------|--------------|
| 代码   | object  | -            |
| 名称   | object  | -            |
| 最新价  | float64 | -            |
| 涨跌额  | float64 | -            |
| 涨跌幅  | float64 | -            |
| 买入   | float64 | -            |
| 卖出   | float64 | -            |
| 昨收   | float64 | -            |
| 今开   | float64 | -            |
| 最高   | float64 | -            |
| 最低   | float64 | -            |
| 成交量  | float64 | 注意单位: 股      |
| 成交额  | float64 | 注意单位: 元      |
| 时点   | object  | 注意: 数据获取的时间点 |
| 市盈率  | float64 | -            |
| 市净率  | float64 | -            |
| 流通市值 | float64 | -            |
| 总市值  | float64 | -            |
| 换手率  | float64 | -            |

接口示例

```python
import akshare as ak

stock_zh_kcb_spot_df = ak.stock_zh_kcb_spot()
print(stock_zh_kcb_spot_df)
```

#### 历史行情数据

接口: stock_zh_kcb_daily

目标地址: https://finance.sina.com.cn/realstock/company/sh688001/nc.shtml(示例)

描述: 新浪财经-科创板股票历史行情数据

限量: 单次返回指定 symbol 和 adjust 的所有历史行情数据; 请控制采集的频率, 大量抓取容易封IP

输入参数

| 名称     | 类型  | 描述                                                                                 |
|--------|-----|------------------------------------------------------------------------------------|
| symbol | str | symbol="sh688008"; 带市场标识的股票代码                                                      |
| adjust | str | 默认不复权的数据; qfq: 返回前复权后的数据; hfq: 返回后复权后的数据; hfq-factor: 返回后复权因子; qfq-factor: 返回前复权因子 |

输出参数

| 名称                | 类型      | 描述                                                                                           |
|-------------------|---------|----------------------------------------------------------------------------------------------|
| date              | object  | -                                                                                            |
| close             | float64 | 收盘价                                                                                          |
| high              | float64 | 最高价                                                                                          |
| low               | float64 | 最低价                                                                                          |
| open              | float64 | 开盘价                                                                                          |
| volume            | float64 | 成交量(股)                                                                                       |
| after_volume      | float64 | 盘后量; 参见[科创板盘后固定价格交易](http://www.sse.com.cn/lawandrules/sserules/tib/trading/c/4729491.shtml) |
| after_amount      | float64 | 盘后额; 参见[科创板盘后固定价格交易](http://www.sse.com.cn/lawandrules/sserules/tib/trading/c/4729491.shtml) |
| outstanding_share | float64 | 流通股本(股)                                                                                      |
| turnover          | float64 | 换手率=成交量(股)/流通股本(股)                                                                           |

接口示例

```python
import akshare as ak

stock_zh_kcb_daily_df = ak.stock_zh_kcb_daily(symbol="sh688399", adjust="hfq")
print(stock_zh_kcb_daily_df)
```

#### 科创板公告

接口: stock_zh_kcb_report_em

目标地址: https://data.eastmoney.com/notices/kcb.html

描述: 东方财富-科创板报告数据

限量: 单次返回所有科创板上市公司的报告数据

输入参数

| 名称        | 类型  | 描述                   |
|-----------|-----|----------------------|
| from_page | int | from_page=1; 始获取的页码  |
| to_page   | int | to_page=100; 结束获取的页码 |

输出参数

| 名称   | 类型     | 描述                                                                          |
|------|--------|-----------------------------------------------------------------------------|
| 代码   | object | -                                                                           |
| 名称   | object | -                                                                           |
| 公告标题 | object | -                                                                           |
| 公告类型 | object | -                                                                           |
| 公告日期 | object | -                                                                           |
| 公告代码 | object | 本代码可以用来获取公告详情: http://data.eastmoney.com/notices/detail/688595/{替换到此处}.html |

接口示例

```python
import akshare as ak

stock_zh_kcb_report_em_df = ak.stock_zh_kcb_report_em(from_page=1, to_page=100)
print(stock_zh_kcb_report_em_df)
```

### A+H股

#### 实时行情数据-东财

接口: stock_zh_ah_spot_em

目标地址: https://quote.eastmoney.com/center/gridlist.html#ah_comparison

描述: 东方财富网-行情中心-沪深港通-AH股比价-实时行情, 延迟 15 分钟更新

限量: 单次返回所有 A+H 上市公司的实时行情数据

输入参数

| 名称  | 类型  | 描述  |
|-----|-----|-----|
| -   | -   | -   |

输出参数

| 名称      | 类型      | 描述        |
|---------|---------|-----------|
| 序号      | int64   | -         |
| 名称      | object  | -         |
| H股代码    | object  | -         |
| 最新价-HKD | float64 | 注意单位: HKD |
| H股-涨跌幅  | float64 | 注意单位: %   |
| A股代码    | object  | -         |
| 最新价-RMB | float64 | 注意单位: RMB |
| A股-涨跌幅  | float64 | 注意单位: %   |
| 比价      | float64 | -         |
| 溢价      | float64 | 注意单位: %   |

接口示例

```python
import akshare as ak

stock_zh_ah_spot_em_df = ak.stock_zh_ah_spot_em()
print(stock_zh_ah_spot_em_df)
```

#### 实时行情数据-腾讯

接口: stock_zh_ah_spot

目标地址: https://stockapp.finance.qq.com/mstats/#mod=list&id=hk_ah&module=HK&type=AH

描述: A+H 股数据是从腾讯财经获取的数据, 延迟 15 分钟更新

限量: 单次返回所有 A+H 上市公司的实时行情数据

输入参数

| 名称  | 类型  | 描述  |
|-----|-----|-----|
| -   | -   | -   |

输出参数

| 名称  | 类型      | 描述      |
|-----|---------|---------|
| 代码  | object  | -       |
| 名称  | object  | -       |
| 最新价 | float64 | -       |
| 涨跌幅 | float64 | 注意单位: % |
| 涨跌额 | float64 | -       |
| 买入  | float64 | -       |
| 卖出  | float64 | -       |
| 成交量 | float64 | -       |
| 成交额 | float64 | -       |
| 今开  | float64 | -       |
| 昨收  | float64 | -       |
| 最高  | float64 | -       |
| 最低  | float64 | -       |

接口示例

```python
import akshare as ak

stock_zh_ah_spot_df = ak.stock_zh_ah_spot()
print(stock_zh_ah_spot_df)
```

#### 历史行情数据

接口: stock_zh_ah_daily

目标地址: https://gu.qq.com/hk02359/gp

描述: 腾讯财经-A+H 股数据

限量: 单次返回指定参数的 A+H 上市公司的历史行情数据

输入参数

| 名称         | 类型  | 描述                                                          |
|------------|-----|-------------------------------------------------------------|
| symbol     | str | symbol="02318"; 港股股票代码, 可以通过 **ak.stock_zh_ah_name()** 函数获取 |
| start_year | str | start_year="2000"; 开始年份                                     |
| end_year   | str | end_year="2019"; 结束年份                                       |
| adjust     | str | adjust=""; 默认为空不复权; 'qfq': 前复权, 'hfq': 后复权                  |

输出参数

| 名称  | 类型      | 描述  |
|-----|---------|-----|
| 日期  | object  | -   |
| 开盘  | float64 | -   |
| 收盘  | float64 | -   |
| 最高  | float64 | -   |
| 最低  | float64 | -   |
| 成交量 | float64 | -   |

接口示例

```python
import akshare as ak

stock_zh_ah_daily_df = ak.stock_zh_ah_daily(symbol="02318", start_year="2022", end_year="2024", adjust="")
print(stock_zh_ah_daily_df)
```

#### A+H股票字典

接口: stock_zh_ah_name

目标地址: https://stockapp.finance.qq.com/mstats/#mod=list&id=hk_ah&module=HK&type=AH

描述: A+H 股数据是从腾讯财经获取的数据, 历史数据按日频率更新

限量: 单次返回所有 A+H 上市公司的代码和名称

输入参数

| 名称  | 类型  | 描述  |
|-----|-----|-----|
| -   | -   | -   |

输出参数

| 名称  | 类型     | 描述  |
|-----|--------|-----|
| 代码  | object | -   |
| 名称  | object | -   |

接口示例

```python
import akshare as ak

stock_zh_ah_name_df = ak.stock_zh_ah_name()
print(stock_zh_ah_name_df)
```

### 美股

#### 实时行情数据-东财

接口: stock_us_spot_em

目标地址: https://quote.eastmoney.com/center/gridlist.html#us_stocks

描述: 东方财富网-美股-实时行情

限量: 单次返回美股所有上市公司的实时行情数据

输入参数

| 名称  | 类型  | 描述  |
|-----|-----|-----|
| -   | -   | -   |

输出参数

| 名称  | 类型      | 描述              |
|-----|---------|-----------------|
| 序号  | int64   | -               |
| 名称  | object  | -               |
| 最新价 | float64 | 注意单位: 美元        |
| 涨跌额 | float64 | 注意单位: 美元        |
| 涨跌幅 | float64 | 注意单位: %         |
| 开盘价 | float64 | 注意单位: 美元        |
| 最高价 | float64 | 注意单位: 美元        |
| 最低价 | float64 | 注意单位: 美元        |
| 昨收价 | float64 | 注意单位: 美元        |
| 总市值 | float64 | 注意单位: 美元        |
| 市盈率 | float64 | -               |
| 成交量 | float64 | -               |
| 成交额 | float64 | 注意单位: 美元        |
| 振幅  | float64 | 注意单位: %         |
| 换手率 | float64 | 注意单位: %         |
| 代码  | object  | 注意: 用来获取历史数据的代码 |

接口示例

```python
import akshare as ak

stock_us_spot_em_df = ak.stock_us_spot_em()
print(stock_us_spot_em_df)
```

#### 实时行情数据-新浪

接口: stock_us_spot

目标地址: https://finance.sina.com.cn/stock/usstock/sector.shtml

描述: 新浪财经-美股; 获取的数据有 15 分钟延迟; 建议使用 ak.stock_us_spot_em() 来获取数据

限量: 单次返回美股所有上市公司的实时行情数据

输入参数

| 名称  | 类型  | 描述  |
|-----|-----|-----|
| -   | -   | -   |

输出参数

| 名称  | 类型  | 描述   |
|-----|-----|------|
| -   | -   | 新浪默认 |

接口示例

```python
import akshare as ak

us_stock_current_df = ak.stock_us_spot()
print(us_stock_current_df)
```

#### 历史行情数据-东财

接口: stock_us_hist

目标地址: https://quote.eastmoney.com/us/ENTX.html#fullScreenChart

描述: 东方财富网-行情-美股-每日行情

限量: 单次返回指定上市公司的指定 adjust 后的所有历史行情数据；注意其中复权参数是否生效！

输入参数

| 名称         | 类型  | 描述                                                                          |
|------------|-----|-----------------------------------------------------------------------------|
| symbol     | str | 美股代码, 可以通过 **ak.stock_us_spot_em()** 函数返回所有的 pandas.DataFrame 里面的 `代码` 字段获取 |
| period     | str | period='daily'; choice of {'daily', 'weekly', 'monthly'}                    |
| start_date | str | start_date="20210101"                                                       |
| end_date   | str | end_date="20210601"                                                         |
| adjust     | str | 默认 adjust="", 则返回未复权的数据; adjust="qfq" 则返回前复权的数据, adjust="hfq" 则返回后复权的数据     |

输出参数

| 名称  | 类型      | 描述       |
|-----|---------|----------|
| 日期  | object  | -        |
| 开盘  | float64 | 注意单位: 美元 |
| 收盘  | float64 | 注意单位: 美元 |
| 最高  | float64 | 注意单位: 美元 |
| 最低  | float64 | 注意单位: 美元 |
| 成交量 | int32   | 注意单位: 股  |
| 成交额 | float64 | 注意单位: 美元 |
| 振幅  | float64 | 注意单位: %  |
| 涨跌幅 | float64 | 注意单位: %  |
| 涨跌额 | float64 | 注意单位: 美元 |
| 换手率 | float64 | 注意单位: %  |

接口示例

```python
import akshare as ak

stock_us_hist_df = ak.stock_us_hist(symbol='106.TTE', period="daily", start_date="20200101", end_date="20240214", adjust="qfq")
print(stock_us_hist_df)
```

#### 个股信息查询-雪球

接口: stock_individual_basic_info_us_xq

目标地址: https://xueqiu.com/snowman/S/NVDA/detail#/GSJJ

描述: 雪球-个股-公司概况-公司简介

限量: 单次返回指定 symbol 的个股信息

输入参数

| 名称      | 类型    | 描述                      |
|---------|-------|-------------------------|
| symbol  | str   | symbol="NVDA"; 股票代码     |
| token   | str   | token=None;             |
| timeout | float | timeout=None; 默认不设置超时参数 |

输出参数

| 名称    | 类型     | 描述  |
|-------|--------|-----|
| item  | object | -   |
| value | object | -   |

接口示例

```python
import akshare as ak

stock_individual_basic_info_us_xq_df = ak.stock_individual_basic_info_us_xq(symbol="SH601127")
print(stock_individual_basic_info_us_xq_df)
```

#### 分时数据-东财

接口: stock_us_hist_min_em

目标地址: https://quote.eastmoney.com/us/ATER.html

描述: 东方财富网-行情首页-美股-每日分时行情

限量: 单次返回指定上市公司最近 5 个交易日分钟数据, 注意美股数据更新有延时

输入参数

| 名称         | 类型  | 描述                                                                                           |
|------------|-----|----------------------------------------------------------------------------------------------|
| symbol     | str | symbol="105.ATER"; 美股代码可以通过 **ak.stock_us_spot_em()** 函数返回所有的 pandas.DataFrame 里面的 `代码` 字段获取 |
| start_date | str | start_date="1979-09-01 09:32:00"; 日期时间; 默认返回所有数据                                             |
| end_date   | str | end_date="2222-01-01 09:32:00"; 日期时间; 默认返回所有数据                                               |

输出参数

| 名称  | 类型      | 描述       |
|-----|---------|----------|
| 时间  | object  | -        |
| 开盘  | float64 | 注意单位: 美元 |
| 收盘  | float64 | 注意单位: 美元 |
| 最高  | float64 | 注意单位: 美元 |
| 最低  | float64 | 注意单位: 美元 |
| 成交量 | float64 | 注意单位: 股  |
| 成交额 | float64 | 注意单位: 美元 |
| 最新价 | float64 | 注意单位: 美元 |

接口示例

```python
import akshare as ak

stock_us_hist_min_em_df = ak.stock_us_hist_min_em(symbol="105.ATER")
print(stock_us_hist_min_em_df)
```

#### 历史行情数据-新浪

接口: stock_us_daily

目标地址: http://finance.sina.com.cn/stock/usstock/sector.shtml

描述: 美股历史行情数据，设定 adjust="qfq" 则返回前复权后的数据，默认 adjust="", 则返回未复权的数据，历史数据按日频率更新

限量: 单次返回指定上市公司的指定 adjust 后的所有历史行情数据

输入参数

| 名称     | 类型  | 描述                                                                  |
|--------|-----|---------------------------------------------------------------------|
| symbol | str | 美股代码, 可以通过 **ak.get_us_stock_name()** 函数返回所有美股代码, 由于美股数据量大, 建议按需要获取 |
| adjust | str | adjust="qfq" 则返回前复权后的数据，默认 adjust="", 则返回未复权的数据                     |

**ak.get_us_stock_name()**: will return a pandas.DataFrame, which contains name, cname and symbol, you should use
symbol!

输出参数-历史数据

| 名称     | 类型         | 描述  |
|--------|------------|-----|
| date   | datetime64 | -   |
| open   | float64    | 开盘价 |
| high   | float64    | 最高价 |
| low    | float64    | 最低价 |
| close  | float64    | 收盘价 |
| volume | float64    | 成交量 |

输出参数-前复权因子

| 名称         | 类型         | 描述                  |
|------------|------------|---------------------|
| date       | datetime64 | 日期                  |
| qfq_factor | float      | 前复权因子               |
| adjust     | float      | 由于前复权会出现负值, 该值为调整因子 |

P.S. 复权计算公式: 未复权数据 * qfq_factor + adjust

P.S. "CIEN" 股票的新浪美股数据由于复权因子错误，暂不返回前复权数据

接口示例-未复权数据

```python
import akshare as ak

stock_us_daily_df = ak.stock_us_daily(symbol="AAPL", adjust="")
print(stock_us_daily_df)
```

接口示例-前复权调整后的数据

```python
import akshare as ak

stock_us_daily_df = ak.stock_us_daily(symbol="AAPL", adjust="qfq")
print(stock_us_daily_df)
```

接口示例-前复权因子

```python
import akshare as ak

qfq_df = ak.stock_us_daily(symbol="AAPL", adjust="qfq-factor")
print(qfq_df)
```

#### 粉单市场

接口: stock_us_pink_spot_em

目标地址: http://quote.eastmoney.com/center/gridlist.html#us_pinksheet

描述: 美股粉单市场的实时行情数据

限量: 单次返回指定所有粉单市场的行情数据

输入参数

| 名称  | 类型  | 描述  |
|-----|-----|-----|
| -   | -   | -   |

输出参数

| 名称  | 类型      | 描述              |
|-----|---------|-----------------|
| 序号  | int64   | -               |
| 名称  | object  | -               |
| 最新价 | float64 | 注意单位: 美元        |
| 涨跌额 | float64 | 注意单位: 美元        |
| 涨跌幅 | float64 | 注意单位: %         |
| 开盘价 | float64 | 注意单位: 美元        |
| 最高价 | float64 | 注意单位: 美元        |
| 最低价 | float64 | 注意单位: 美元        |
| 昨收价 | float64 | 注意单位: 美元        |
| 总市值 | float64 | 注意单位: 美元        |
| 市盈率 | float64 | -               |
| 代码  | object  | 注意: 用来获取历史数据的代码 |

接口示例

```python
import akshare as ak

stock_us_pink_spot_em_df = ak.stock_us_pink_spot_em()
print(stock_us_pink_spot_em_df)
```

#### 知名美股

接口: stock_us_famous_spot_em

目标地址: http://quote.eastmoney.com/center/gridlist.html#us_wellknown

描述: 美股-知名美股的实时行情数据

限量: 单次返回指定 symbol 的行情数据

输入参数

| 名称     | 类型  | 描述                                                                       |
|--------|-----|--------------------------------------------------------------------------|
| symbol | str | symbol="科技类"; choice of {'科技类', '金融类', '医药食品类', '媒体类', '汽车能源类', '制造零售类'} |

输出参数

| 名称  | 类型      | 描述              |
|-----|---------|-----------------|
| 序号  | int64   | -               |
| 名称  | object  | -               |
| 最新价 | float64 | 注意单位: 美元        |
| 涨跌额 | float64 | 注意单位: 美元        |
| 涨跌幅 | float64 | 注意单位: %         |
| 开盘价 | float64 | 注意单位: 美元        |
| 最高价 | float64 | 注意单位: 美元        |
| 最低价 | float64 | 注意单位: 美元        |
| 昨收价 | float64 | 注意单位: 美元        |
| 总市值 | float64 | 注意单位: 美元        |
| 市盈率 | float64 | -               |
| 代码  | object  | 注意: 用来获取历史数据的代码 |

接口示例

```python
import akshare as ak

stock_us_famous_spot_em_df = ak.stock_us_famous_spot_em(symbol='科技类')
print(stock_us_famous_spot_em_df)
```

### 港股

#### 实时行情数据-东财

接口: stock_hk_spot_em

目标地址: http://quote.eastmoney.com/center/gridlist.html#hk_stocks

描述: 所有港股的实时行情数据; 该数据有 15 分钟延时

限量: 单次返回最近交易日的所有港股的数据

输入参数

| 名称  | 类型  | 描述  |
|-----|-----|-----|
| -   | -   | -   |

输出参数

| 名称  | 类型      | 描述       |
|-----|---------|----------|
| 序号  | int64   | -        |
| 代码  | object  | -        |
| 名称  | object  | -        |
| 最新价 | float64 | 注意单位: 港元 |
| 涨跌额 | float64 | 注意单位: 港元 |
| 涨跌幅 | float64 | 注意单位: %  |
| 今开  | float64 | -        |
| 最高  | float64 | -        |
| 最低  | float64 | -        |
| 昨收  | float64 | -        |
| 成交量 | float64 | 注意单位: 股  |
| 成交额 | float64 | 注意单位: 港元 |

接口示例

```python
import akshare as ak

stock_hk_spot_em_df = ak.stock_hk_spot_em()
print(stock_hk_spot_em_df)
```

#### 港股主板实时行情数据-东财

接口: stock_hk_main_board_spot_em

目标地址: https://quote.eastmoney.com/center/gridlist.html#hk_mainboard

描述: 港股主板的实时行情数据; 该数据有 15 分钟延时

限量: 单次返回港股主板的数据

输入参数

| 名称  | 类型  | 描述  |
|-----|-----|-----|
| -   | -   | -   |

输出参数

| 名称  | 类型      | 描述       |
|-----|---------|----------|
| 序号  | int64   | -        |
| 代码  | object  | -        |
| 名称  | object  | -        |
| 最新价 | float64 | 注意单位: 港元 |
| 涨跌额 | float64 | 注意单位: 港元 |
| 涨跌幅 | float64 | 注意单位: %  |
| 今开  | float64 | -        |
| 最高  | float64 | -        |
| 最低  | float64 | -        |
| 昨收  | float64 | -        |
| 成交量 | float64 | 注意单位: 股  |
| 成交额 | float64 | 注意单位: 港元 |

接口示例

```python
import akshare as ak

stock_hk_main_board_spot_em_df = ak.stock_hk_main_board_spot_em()
print(stock_hk_main_board_spot_em_df)
```

#### 实时行情数据-新浪

接口: stock_hk_spot

目标地址: https://vip.stock.finance.sina.com.cn/mkt/#qbgg_hk

描述: 获取所有港股的实时行情数据 15 分钟延时

限量: 单次返回当前时间戳的所有港股的数据

输入参数

| 名称  | 类型  | 描述  |
|-----|-----|-----|
| -   | -   | -   |

输出参数

| 名称   | 类型      | 描述 |
|------|---------|----|
| 日期时间 | object  | -  |
| 代码   | object  | -  |
| 中文名称 | object  | -  |
| 英文名称 | object  | -  |
| 交易类型 | object  | -  |
| 最新价  | float64 | -  |
| 涨跌额  | float64 | -  |
| 涨跌幅  | float64 | -  |
| 昨收   | float64 | -  |
| 今开   | float64 | -  |
| 最高   | float64 | -  |
| 最低   | float64 | -  |
| 成交量  | float64 | -  |
| 成交额  | float64 | -  |
| 买一   | float64 | -  |
| 卖一   | float64 | -  |

接口示例

```python
import akshare as ak

stock_hk_spot_df = ak.stock_hk_spot()
print(stock_hk_spot_df)
```

#### 个股信息查询-雪球

接口: stock_individual_basic_info_hk_xq

目标地址: https://xueqiu.com/S/00700

描述: 雪球-个股-公司概况-公司简介

限量: 单次返回指定 symbol 的个股信息

输入参数

| 名称      | 类型    | 描述                      |
|---------|-------|-------------------------|
| symbol  | str   | symbol="02097"; 股票代码    |
| token   | str   | token=None;             |
| timeout | float | timeout=None; 默认不设置超时参数 |

输出参数

| 名称    | 类型     | 描述  |
|-------|--------|-----|
| item  | object | -   |
| value | object | -   |

接口示例

```python
import akshare as ak

stock_individual_basic_info_hk_xq_df = ak.stock_individual_basic_info_hk_xq(symbol="02097")
print(stock_individual_basic_info_hk_xq_df)
```

#### 分时数据-东财

接口: stock_hk_hist_min_em

目标地址: http://quote.eastmoney.com/hk/00948.html

描述: 东方财富网-行情首页-港股-每日分时行情

限量: 单次返回指定上市公司最近 5 个交易日分钟数据, 注意港股有延时

输入参数

| 名称         | 类型  | 描述                                                                                                  |
|------------|-----|-----------------------------------------------------------------------------------------------------|
| symbol     | str | symbol="01611"; 港股代码可以通过 **ak.stock_hk_spot_em()** 函数返回所有的 pandas.DataFrame 里面的 `代码` 字段获取           |
| period     | str | period='5'; choice of {'1', '5', '15', '30', '60'}; 其中 1 分钟数据返回近 5 个交易日数据且不复权                       |
| adjust     | str | adjust=''; choice of {'', 'qfq', 'hfq'}; '': 不复权, 'qfq': 前复权, 'hfq': 后复权, 其中 1 分钟数据返回近 5 个交易日数据且不复权 |
| start_date | str | start_date="1979-09-01 09:32:00"; 日期时间; 默认返回所有数据                                                    |
| end_date   | str | end_date="2222-01-01 09:32:00"; 日期时间; 默认返回所有数据                                                      |

输出参数-1分钟数据

| 名称  | 类型      | 描述       |
|-----|---------|----------|
| 时间  | object  | -        |
| 开盘  | float64 | 注意单位: 港元 |
| 收盘  | float64 | 注意单位: 港元 |
| 最高  | float64 | 注意单位: 港元 |
| 最低  | float64 | 注意单位: 港元 |
| 成交量 | float64 | 注意单位: 股  |
| 成交额 | float64 | 注意单位: 港元 |
| 最新价 | float64 | 注意单位: 港元 |

接口示例-1分钟数据

```python
import akshare as ak

stock_hk_hist_min_em_df = ak.stock_hk_hist_min_em(symbol="01611", period='1', adjust='',
                                                  start_date="2021-09-01 09:32:00",
                                                  end_date="2021-09-07 18:32:00")  # 其中的 start_date 和 end_date 需要设定为近期
print(stock_hk_hist_min_em_df)
```

输出参数-其他

| 名称  | 类型      | 描述       |
|-----|---------|----------|
| 时间  | object  | -        |
| 开盘  | float64 | 注意单位: 港元 |
| 收盘  | float64 | 注意单位: 港元 |
| 最高  | float64 | 注意单位: 港元 |
| 最低  | float64 | 注意单位: 港元 |
| 涨跌幅 | float64 | 注意单位: %  |
| 涨跌额 | float64 | 注意单位: 港元 |
| 成交量 | float64 | 注意单位: 股  |
| 成交额 | float64 | 注意单位: 港元 |
| 振幅  | float64 | 注意单位: %  |
| 换手率 | float64 | 注意单位: %  |

接口示例-其他

```python
import akshare as ak

stock_hk_hist_min_em_df = ak.stock_hk_hist_min_em(symbol="01611", period='5', adjust='hfq',
                                                  start_date="2021-09-01 09:32:00",
                                                  end_date="2021-09-07 18:32:00")  # 其中的 start_date 和 end_date 需要设定为近期
print(stock_hk_hist_min_em_df)
```

#### 历史行情数据-东财

接口: stock_hk_hist

目标地址: https://quote.eastmoney.com/hk/08367.html

描述: 港股-历史行情数据, 可以选择返回复权后数据, 更新频率为日频

限量: 单次返回指定上市公司的历史行情数据

输入参数

| 名称         | 类型  | 描述                                                             |
|------------|-----|----------------------------------------------------------------|
| symbol     | str | symbol="00593"; 港股代码,可以通过 **ak.stock_hk_spot_em()** 函数返回所有港股代码 |
| period     | str | period='daily'; choice of {'daily', 'weekly', 'monthly'}       |
| start_date | str | start_date="19700101"; 开始日期                                    |
| end_date   | str | end_date="22220101"; 结束日期                                      |
| adjust     | str | adjust="": 返回未复权的数据, 默认; qfq: 返回前复权数据; hfq: 返回后复权数据;           |

输出参数

| 名称  | 类型      | 描述       |
|-----|---------|----------|
| 日期  | object  | -        |
| 开盘  | float64 | 注意单位: 港元 |
| 收盘  | float64 | 注意单位: 港元 |
| 最高  | float64 | 注意单位: 港元 |
| 最低  | float64 | 注意单位: 港元 |
| 成交量 | int64   | 注意单位: 股  |
| 成交额 | float64 | 注意单位: 港元 |
| 振幅  | float64 | 注意单位: %  |
| 涨跌幅 | float64 | 注意单位: %  |
| 涨跌额 | float64 | 注意单位: 港元 |
| 换手率 | float64 | 注意单位: %  |

接口示例-未复权

```python
import akshare as ak

stock_hk_hist_df = ak.stock_hk_hist(symbol="00593", period="daily", start_date="19700101", end_date="22220101", adjust="")
print(stock_hk_hist_df)
```

输出参数-前复权

| 名称  | 类型      | 描述       |
|-----|---------|----------|
| 日期  | object  | -        |
| 开盘  | float64 | 注意单位: 港元 |
| 收盘  | float64 | 注意单位: 港元 |
| 最高  | float64 | 注意单位: 港元 |
| 最低  | float64 | 注意单位: 港元 |
| 成交量 | int64   | 注意单位: 股  |
| 成交额 | float64 | 注意单位: 港元 |
| 振幅  | float64 | 注意单位: %  |
| 涨跌幅 | float64 | 注意单位: %  |
| 涨跌额 | float64 | 注意单位: 港元 |
| 换手率 | float64 | 注意单位: %  |

接口示例-前复权

```python
import akshare as ak

stock_hk_hist_qfq_df = ak.stock_hk_hist(symbol="00593", period="daily", start_date="19700101", end_date="22220101", adjust="qfq")
print(stock_hk_hist_qfq_df)
```

输出参数-后复权

| 名称  | 类型      | 描述       |
|-----|---------|----------|
| 日期  | object  | -        |
| 开盘  | float64 | 注意单位: 港元 |
| 收盘  | float64 | 注意单位: 港元 |
| 最高  | float64 | 注意单位: 港元 |
| 最低  | float64 | 注意单位: 港元 |
| 成交量 | int32   | 注意单位: 股  |
| 成交额 | float64 | 注意单位: 港元 |
| 振幅  | float64 | 注意单位: %  |
| 涨跌幅 | float64 | 注意单位: %  |
| 涨跌额 | float64 | 注意单位: 港元 |
| 换手率 | float64 | 注意单位: %  |

接口示例-后复权

```python
import akshare as ak

stock_hk_hist_hfq_df = ak.stock_hk_hist(symbol="00593", period="daily", start_date="19700101", end_date="22220101", adjust="hfq")
print(stock_hk_hist_hfq_df)
```

#### 历史行情数据-新浪

接口: stock_hk_daily

目标地址: http://stock.finance.sina.com.cn/hkstock/quotes/01336.html(个例)

描述:港股-历史行情数据, 可以选择返回复权后数据,更新频率为日频

限量: 单次返回指定上市公司的历史行情数据(包括前后复权因子), 提供新浪财经拥有的该股票的所有数据(
并不等于该股票从上市至今的数据)

输入参数

| 名称     | 类型  | 描述                                                                                             |
|--------|-----|------------------------------------------------------------------------------------------------|
| symbol | str | 港股代码,可以通过 **ak.stock_hk_spot()** 函数返回所有港股代码                                                    |
| adjust | str | "": 返回未复权的数据 ; qfq: 返回前复权后的数据; hfq: 返回后复权后的数据; qfq-factor: 返回前复权因子和调整; hfq-factor: 返回后复权因子和调整; |

输出参数-历史行情数据(后复权)

| 名称     | 类型      | 描述  |
|--------|---------|-----|
| date   | object  | 日期  |
| open   | float64 | 开盘价 |
| high   | float64 | 最高价 |
| low    | float64 | 最低价 |
| close  | float64 | 收盘价 |
| volume | float64 | 成交量 |

接口示例-历史行情数据(后复权)

```python
import akshare as ak

stock_hk_daily_hfq_df = ak.stock_hk_daily(symbol="00700", adjust="hfq")
print(stock_hk_daily_hfq_df)
```

输出参数-历史行情数据(未复权)

| 名称     | 类型      | 描述  |
|--------|---------|-----|
| date   | object  | 日期  |
| open   | float64 | 开盘价 |
| high   | float64 | 最高价 |
| low    | float64 | 最低价 |
| close  | float64 | 收盘价 |
| volume | float64 | 成交量 |

接口示例-历史行情数据(未复权)

```python
import akshare as ak

stock_hk_daily_df = ak.stock_hk_daily(symbol="00700", adjust="")
print(stock_hk_daily_df)
```

输出参数-后复权因子

| 名称         | 类型     | 描述    |
|------------|--------|-------|
| date       | object | 日期    |
| hfq_factor | object | 后复权因子 |
| cash       | object | 现金分红  |

接口示例-后复权因子

```python
import akshare as ak

stock_hk_daily_hfq_factor_df = ak.stock_hk_daily(symbol="00700", adjust="hfq-factor")
print(stock_hk_daily_hfq_factor_df)
```

#### 知名港股

接口: stock_hk_famous_spot_em

目标地址: https://quote.eastmoney.com/center/gridlist.html#hk_wellknown

描述: 东方财富网-行情中心-港股市场-知名港股实时行情数据

限量: 单次返回全部行情数据

输入参数

| 名称 | 类型 | 描述 |
|----|----|----|
| -  | -  | -  |

输出参数

| 名称  | 类型      | 描述       |
|-----|---------|----------|
| 序号  | int64   | -        |
| 代码  | object  | -        |
| 名称  | object  | -        |
| 最新价 | float64 | 注意单位: 港元 |
| 涨跌额 | float64 | 注意单位: 港元 |
| 涨跌幅 | float64 | 注意单位: %  |
| 今开  | float64 | 注意单位: 港元 |
| 最高  | float64 | 注意单位: 港元 |
| 最低  | float64 | 注意单位: 港元 |
| 昨收  | float64 | 注意单位: 港元 |
| 成交量 | float64 | 注意单位: 股  |
| 成交额 | float64 | 注意单位: 港元 |

接口示例

```python
import akshare as ak

stock_hk_famous_spot_em_df = ak.stock_hk_famous_spot_em()
print(stock_hk_famous_spot_em_df)
```

#### 证券资料

接口: stock_hk_security_profile_em

目标地址: https://emweb.securities.eastmoney.com/PC_HKF10/pages/home/index.html?code=03900&type=web&color=w#/CompanyProfile

描述: 东方财富-港股-证券资料

限量: 单次返回全部数据

输入参数

| 名称     | 类型  | 描述             |
|--------|-----|----------------|
| symbol | str | symbol="03900" |

输出参数

| 名称             | 类型      | 描述 |
|----------------|---------|----|
| 证券代码           | object  | -  |
| 证券简称           | object  | -  |
| 上市日期           | object  | -  |
| 证券类型           | object  | -  |
| 发行价            | float64 | -  |
| 发行量(股)         | int64   | -  |
| 每手股数           | int64   | -  |
| 每股面值           | object  | -  |
| 交易所            | object  | -  |
| 板块             | object  | -  |
| 年结日            | object  | -  |
| ISIN（国际证券识别编码） | object  | -  |
| 是否沪港通标的        | object  | -  |

接口示例

```python
import akshare as ak

stock_hk_security_profile_em_df = ak.stock_hk_security_profile_em(symbol="03900")
print(stock_hk_security_profile_em_df)
```

#### 公司资料

接口: stock_hk_company_profile_em

目标地址: https://emweb.securities.eastmoney.com/PC_HKF10/pages/home/index.html?code=03900&type=web&color=w#/CompanyProfile

描述: 东方财富-港股-公司资料

限量: 单次返回全部数据

输入参数

| 名称     | 类型  | 描述             |
|--------|-----|----------------|
| symbol | str | symbol="03900" |

输出参数

| 名称     | 类型     | 描述 |
|--------|--------|----|
| 公司名称   | object | -  |
| 英文名称   | object | -  |
| 注册地    | object | -  |
| 公司成立日期 | object | -  |
| 所属行业   | object | -  |
| 董事长    | object | -  |
| 公司秘书   | object | -  |
| 员工人数   | int64  | -  |
| 办公地址   | object | -  |
| 公司网址   | object | -  |
| E-MAIL | object | -  |
| 年结日    | object | -  |
| 联系电话   | object | -  |
| 核数师    | object | -  |
| 传真     | object | -  |
| 公司介绍   | object | -  |

接口示例

```python
import akshare as ak

stock_hk_company_profile_em_df = ak.stock_hk_company_profile_em(symbol="03900")
print(stock_hk_company_profile_em_df)
```

#### 财务指标

接口: stock_hk_financial_indicator_em

目标地址: https://emweb.securities.eastmoney.com/PC_HKF10/pages/home/index.html?code=03900&type=web&color=w#/CoreReading

描述: 东方财富-港股-核心必读-最新指标

限量: 单次返回全部数据

输入参数

| 名称     | 类型  | 描述             |
|--------|-----|----------------|
| symbol | str | symbol="03900" |

输出参数

| 名称             | 类型     | 描述 |
|----------------|--------|----|
| 基本每股收益(元)      | object | -  |
| 每股净资产(元)       | object | -  |
| 法定股本(股)        | object | -  |
| 每手股            | object | -  |
| 每股股息TTM(港元)    | object | -  |
| 派息比率(%)        | object | -  |
| 已发行股本(股)       | object | -  |
| 已发行股本-H股(股)    | int64  | -  |
| 每股经营现金流(元)     | object | -  |
| 股息率TTM(%)      | object | -  |
| 总市值(港元)        | object | -  |
| 港股市值(港元)       | object | -  |
| 营业总收入          | object | -  |
| 营业总收入滚动环比增长(%) | object | -  |
| 销售净利率(%)       | object | -  |
| 净利润            | object | -  |
| 净利润滚动环比增长(%)   | object | -  |
| 股东权益回报率(%)     | object | -  |
| 市盈率            | object | -  |
| 市净率            | object | -  |
| 总资产回报率(%)      | object | -  |

接口示例

```python
import akshare as ak

stock_hk_financial_indicator_em_df = ak.stock_hk_financial_indicator_em(symbol="03900")
print(stock_hk_financial_indicator_em_df)
```


#### 分红派息

接口: stock_hk_dividend_payout_em

目标地址: https://emweb.securities.eastmoney.com/PC_HKF10/pages/home/index.html?code=03900&type=web&color=w#/CoreReading

描述: 东方财富-港股-核心必读-分红派息

限量: 单次返回全部数据

输入参数

| 名称     | 类型  | 描述             |
|--------|-----|----------------|
| symbol | str | symbol="03900" |

输出参数

| 名称     | 类型     | 描述 |
|--------|--------|----|
| 最新公告日期 | object | -  |
| 财政年度   | object | -  |
| 分红方案   | object | -  |
| 分配类型   | object | -  |
| 除净日    | object | -  |
| 截至过户日  | object | -  |
| 发放日    | object | -  |

接口示例

```python
import akshare as ak

stock_hk_dividend_payout_em_df = ak.stock_hk_dividend_payout_em(symbol="03900")
print(stock_hk_dividend_payout_em_df)
```


#### 行业对比

##### 成长性对比

接口: stock_hk_growth_comparison_em

目标地址: https://emweb.securities.eastmoney.com/PC_HKF10/pages/home/index.html?code=03900&type=web&color=w#/IndustryComparison

描述: 东方财富-港股-行业对比-成长性对比

限量: 单次返回全部数据

输入参数

| 名称     | 类型  | 描述             |
|--------|-----|----------------|
| symbol | str | symbol="03900" |

输出参数

| 名称                  | 类型      | 描述 |
|---------------------|---------|----|
| 代码                  | object  | -  |
| 简称                  | object  | -  |
| 基本每股收益同比增长率         | float64 | -  |
| 基本每股收益同比增长率排名       | int64   | -  |
| 营业收入同比增长率           | float64 | -  |
| 营业收入同比增长率排名         | int64   | -  |
| 营业利润率同比增长率          | float64 | -  |
| 营业利润率同比增长率排名        | int64   | -  |
| 基本每股收总资产同比增长率益同比增长率 | float64 | -  |
| 总资产同比增长率排名          | int64   | -  |

接口示例

```python
import akshare as ak

stock_hk_growth_comparison_em_df = ak.stock_hk_growth_comparison_em(symbol="03900")
print(stock_hk_growth_comparison_em_df)
```

##### 估值对比

接口: stock_hk_valuation_comparison_em

目标地址: https://emweb.securities.eastmoney.com/PC_HKF10/pages/home/index.html?code=03900&type=web&color=w#/IndustryComparison

描述: 东方财富-港股-行业对比-估值对比

限量: 单次返回全部数据

输入参数

| 名称     | 类型  | 描述             |
|--------|-----|----------------|
| symbol | str | symbol="03900" |

输出参数

| 名称        | 类型      | 描述 |
|-----------|---------|----|
| 代码        | object  | -  |
| 简称        | object  | -  |
| 市盈率-TTM   | float64 | -  |
| 市盈率-TTM排名 | int64   | -  |
| 市盈率-LYR   | float64 | -  |
| 市盈率-LYR排名 | int64   | -  |
| 市净率-MRQ   | float64 | -  |
| 市净率-MRQ排名 | int64   | -  |
| 市净率-LYR   | float64 | -  |
| 市净率-LYR排名 | int64   | -  |
| 市销率-TTM   | float64 | -  |
| 市销率-TTM排名 | int64   | -  |
| 市销率-LYR   | float64 | -  |
| 市销率-LYR排名 | int64   | -  |
| 市现率-TTM   | float64 | -  |
| 市现率-TTM排名 | int64   | -  |
| 市现率-LYR   | float64 | -  |
| 市现率-LYR排名 | int64   | -  |

接口示例

```python
import akshare as ak

stock_hk_valuation_comparison_em_df = ak.stock_hk_valuation_comparison_em(symbol="03900")
print(stock_hk_valuation_comparison_em_df)
```


##### 规模对比

接口: stock_hk_scale_comparison_em

目标地址: https://emweb.securities.eastmoney.com/PC_HKF10/pages/home/index.html?code=03900&type=web&color=w#/IndustryComparison

描述: 东方财富-港股-行业对比-规模对比

限量: 单次返回全部数据

输入参数

| 名称     | 类型  | 描述             |
|--------|-----|----------------|
| symbol | str | symbol="03900" |

输出参数

| 名称      | 类型      | 描述 |
|---------|---------|----|
| 代码      | object  | -  |
| 简称      | object  | -  |
| 总市值     | float64 | -  |
| 总市值排名   | int64   | -  |
| 流通市值    | float64 | -  |
| 流通市值排名  | int64   | -  |
| 营业总收入   | int64   | -  |
| 营业总收入排名 | int64   | -  |
| 净利润     | int64   | -  |
| 净利润排名   | int64   | -  |

接口示例

```python
import akshare as ak

stock_hk_scale_comparison_em_df = ak.stock_hk_scale_comparison_em(symbol="03900")
print(stock_hk_scale_comparison_em_df)
```

### 机构调研

#### 机构调研-统计

接口: stock_jgdy_tj_em

目标地址: http://data.eastmoney.com/jgdy/tj.html

描述: 东方财富网-数据中心-特色数据-机构调研-机构调研统计

限量: 单次返回所有历史数据

输入参数

| 名称   | 类型  | 描述                       |
|------|-----|--------------------------|
| date | str | date="20180928"; 开始查询的时间 |

输出参数

| 名称     | 类型      | 描述      |
|--------|---------|---------|
| 序号     | int64   | -       |
| 代码     | object  | -       |
| 名称     | object  | -       |
| 最新价    | float64 | -       |
| 涨跌幅    | float64 | 注意单位: % |
| 接待机构数量 | int64   | -       |
| 接待方式   | object  | -       |
| 接待人员   | object  | -       |
| 接待地点   | object  | -       |
| 接待日期   | object  | -       |
| 公告日期   | object  | -       |

接口示例

```python
import akshare as ak

stock_jgdy_tj_em_df = ak.stock_jgdy_tj_em(date="20210128")
print(stock_jgdy_tj_em_df)
```

#### 机构调研-详细

接口: stock_jgdy_detail_em

目标地址: http://data.eastmoney.com/jgdy/xx.html

描述: 东方财富网-数据中心-特色数据-机构调研-机构调研详细

限量: 单次所有历史数据, 由于数据量比较大需要等待一定时间

输入参数

| 名称   | 类型  | 描述                       |
|------|-----|--------------------------|
| date | str | date="20241211"; 开始查询的时间 |

输出参数

| 名称   | 类型      | 描述      |
|------|---------|---------|
| 序号   | int64   | -       |
| 代码   | object  | -       |
| 名称   | object  | -       |
| 最新价  | float64 | -       |
| 涨跌幅  | float64 | 注意单位: % |
| 调研机构 | object  | -       |
| 机构类型 | object  | -       |
| 调研人员 | object  | -       |
| 接待方式 | object  | -       |
| 接待人员 | object  | -       |
| 接待地点 | object  | -       |
| 调研日期 | object  | -       |
| 公告日期 | object  | -       |

接口示例

```python
import akshare as ak

stock_jgdy_detail_em_df = ak.stock_jgdy_detail_em(date="20241211")
print(stock_jgdy_detail_em_df)
```

### 主营介绍-同花顺

接口: stock_zyjs_ths

目标地址: https://basic.10jqka.com.cn/new/000066/operate.html

描述: 同花顺-主营介绍

限量: 单次返回所有数据

输入参数

| 名称     | 类型  | 描述              |
|--------|-----|-----------------|
| symbol | str | symbol="000066" |

输出参数

| 名称   | 类型      | 描述      |
|------|---------|---------|
| 股票代码 | object  | -       |
| 主营业务 | object  | -       |
| 产品类型 | object  | -       |
| 产品名称 | object  | -       |
| 经营范围 | object  | -       |

接口示例

```python
import akshare as ak

stock_zyjs_ths_df = ak.stock_zyjs_ths(symbol="000066")
print(stock_zyjs_ths_df)
```

### 主营构成-东财

接口: stock_zygc_em

目标地址: https://emweb.securities.eastmoney.com/PC_HSF10/BusinessAnalysis/Index?type=web&code=SH688041#

描述: 东方财富网-个股-主营构成

限量: 单次返回所有历史数据

输入参数

| 名称     | 类型  | 描述                |
|--------|-----|-------------------|
| symbol | str | symbol="SH688041" |

输出参数

| 名称   | 类型      | 描述      |
|------|---------|---------|
| 股票代码 | object  | -       |
| 报告日期 | object  | -       |
| 分类类型 | object  | -       |
| 主营构成 | int64   | -       |
| 主营收入 | float64 | 注意单位: 元 |
| 收入比例 | float64 | -       |
| 主营成本 | float64 | 注意单位: 元 |
| 成本比例 | float64 | -       |
| 主营利润 | float64 | 注意单位: 元 |
| 利润比例 | float64 | -       |
| 毛利率  | float64 | -       |

接口示例

```python
import akshare as ak

stock_zygc_em_df = ak.stock_zygc_em(symbol="SH688041")
print(stock_zygc_em_df)
```

### 股票质押

#### 股权质押市场概况

接口: stock_gpzy_profile_em

目标地址: https://data.eastmoney.com/gpzy/marketProfile.aspx

描述: 东方财富网-数据中心-特色数据-股权质押-股权质押市场概况

限量: 单次所有历史数据, 由于数据量比较大需要等待一定时间

输入参数

| 名称  | 类型  | 描述  |
|-----|-----|-----|
| -   | -   | -   |

输出参数

| 名称      | 类型      | 描述      |
|---------|---------|---------|
| 交易日期    | object  | -       |
| A股质押总比例 | float64 | 注意单位: % |
| 质押公司数量  | float64 | -       |
| 质押笔数    | float64 | 注意单位: 笔 |
| 质押总股数   | float64 | 注意单位: 股 |
| 质押总市值   | float64 | 注意单位: 元 |
| 沪深300指数 | float64 | -       |
| 涨跌幅     | float64 | 注意单位: % |

接口示例

```python
import akshare as ak

stock_gpzy_profile_em_df = ak.stock_gpzy_profile_em()
print(stock_gpzy_profile_em_df)
```

#### 上市公司质押比例

接口: stock_gpzy_pledge_ratio_em

目标地址: https://data.eastmoney.com/gpzy/pledgeRatio.aspx

描述: 东方财富网-数据中心-特色数据-股权质押-上市公司质押比例

限量: 单次返回指定交易日的所有历史数据; 其中的交易日需要根据网站提供的为准; 请访问 http://data.eastmoney.com/gpzy/pledgeRatio.aspx 查询具体交易日

输入参数

| 名称   | 类型  | 描述                                                                           |
|------|-----|------------------------------------------------------------------------------|
| date | str | date="20240906"; 请访问 http://data.eastmoney.com/gpzy/pledgeRatio.aspx 查询具体交易日 |

输出参数

| 名称      | 类型      | 描述       |
|---------|---------|----------|
| 序号      | int64   | -        |
| 股票代码    | object  | -        |
| 股票简称    | object  | -        |
| 交易日期    | object  | -        |
| 所属行业    | object  | -        |
| 质押比例    | float64 | 注意单位: %  |
| 质押股数    | float64 | 注意单位: 万股 |
| 质押市值    | float64 | 注意单位: 万元 |
| 质押笔数    | float64 | -        |
| 无限售股质押数 | float64 | 注意单位: 万股 |
| 限售股质押数  | float64 | 注意单位: 万股 |
| 近一年涨跌幅  | float64 | 注意单位: %  |
| 所属行业代码  | object  | -        |

接口示例

```python
import akshare as ak

stock_gpzy_pledge_ratio_em_df = ak.stock_gpzy_pledge_ratio_em(date="20241220")
print(stock_gpzy_pledge_ratio_em_df)
```

#### 重要股东股权质押明细

接口: stock_gpzy_pledge_ratio_detail_em

目标地址: https://data.eastmoney.com/gpzy/pledgeDetail.aspx

描述: 东方财富网-数据中心-特色数据-股权质押-重要股东股权质押明细

限量: 单次所有历史数据, 由于数据量比较大需要等待一定时间

输入参数

| 名称  | 类型  | 描述  |
|-----|-----|-----|
| -   | -   | -   |

输出参数

| 名称      | 类型      | 描述      |
|---------|---------|---------|
| 序号      | int64   | -       |
| 股票代码    | object  | -       |
| 股票简称    | object  | -       |
| 股东名称    | object  | -       |
| 质押股份数量  | float64 | 注意单位: 股 |
| 占所持股份比例 | float64 | 注意单位: % |
| 占总股本比例  | float64 | 注意单位: % |
| 质押机构    | object  | -       |
| 最新价     | float64 | 注意单位: 元 |
| 质押日收盘价  | float64 | 注意单位: 元 |
| 预估平仓线   | float64 | 注意单位: 元 |
| 公告日期    | object  | -       |
| 质押开始日期  | object  | -       |
| 质押结束日期  | object  | -       |
| 状态      | object  | -       |

接口示例

```python
import akshare as ak

stock_gpzy_pledge_ratio_detail_em_df = ak.stock_gpzy_pledge_ratio_detail_em()
print(stock_gpzy_pledge_ratio_detail_em_df)
```

#### 个股重要股东股权质押明细

接口: stock_gpzy_individual_pledge_ratio_detail_em

目标地址: https://data.eastmoney.com/gpzy/detail/{symbol}.html

描述: 东方财富网-数据中心-股权质押-个股

限量: 单次所有历史数据

输入参数

| 名称     | 类型  | 描述              |
|--------|-----|-----------------|
| symbol | str | symbol="603132" |

输出参数

| 名称      | 类型      | 描述      |
|---------|---------|---------|
| 序号      | int64   | -       |
| 股票代码    | object  | -       |
| 股票简称    | object  | -       |
| 股东名称    | object  | -       |
| 质押股份数量  | float64 | 注意单位: 股 |
| 占所持股份比例 | float64 | 注意单位: % |
| 占总股本比例  | float64 | 注意单位: % |
| 质押机构    | object  | -       |
| 最新价     | float64 | 注意单位: 元 |
| 质押日收盘价  | float64 | 注意单位: 元 |
| 预估平仓线   | float64 | 注意单位: 元 |
| 公告日期    | object  | -       |
| 质押开始日期  | object  | -       |
| 质押结束日期  | object  | -       |
| 状态      | object  | -       |

接口示例

```python
import akshare as ak

stock_gpzy_individual_pledge_ratio_detail_em_df = ak.stock_gpzy_individual_pledge_ratio_detail_em(symbol="603132")
print(stock_gpzy_individual_pledge_ratio_detail_em_df)
```

#### 质押机构分布统计-证券公司

接口: stock_gpzy_distribute_statistics_company_em

目标地址: https://data.eastmoney.com/gpzy/distributeStatistics.aspx

描述: 东方财富网-数据中心-特色数据-股权质押-质押机构分布统计-证券公司

限量: 单次返回当前时点所有历史数据

输入参数

| 名称  | 类型  | 描述  |
|-----|-----|-----|
| -   | -   | -   |

输出参数

| 名称           | 类型      | 描述      |
|--------------|---------|---------|
| 序号           | int64   | -       |
| 质押机构         | object  | -       |
| 质押公司数量       | int64   | -       |
| 质押笔数         | int64   | -       |
| 质押数量         | float64 | 注意单位: 股 |
| 未达预警线比例      | float64 | 注意单位: % |
| 达到预警线未达平仓线比例 | float64 | 注意单位: % |
| 达到平仓线比例      | float64 | 注意单位: % |

接口示例

```python
import akshare as ak

stock_gpzy_distribute_statistics_company_em_df = ak.stock_gpzy_distribute_statistics_company_em()
print(stock_gpzy_distribute_statistics_company_em_df)
```

#### 质押机构分布统计-银行

接口: stock_gpzy_distribute_statistics_bank_em

目标地址: https://data.eastmoney.com/gpzy/distributeStatistics.aspx

描述: 东方财富网-数据中心-特色数据-股权质押-质押机构分布统计-银行

限量: 单次返回当前时点所有历史数据

输入参数

| 名称  | 类型  | 描述  |
|-----|-----|-----|
| -   | -   | -   |

输出参数

| 名称           | 类型      | 描述      |
|--------------|---------|---------|
| 序号           | int64   | -       |
| 质押机构         | object  | -       |
| 质押公司数量       | int64   | -       |
| 质押笔数         | int64   | -       |
| 质押数量         | float64 | 注意单位: 股 |
| 未达预警线比例      | float64 | 注意单位: % |
| 达到预警线未达平仓线比例 | float64 | 注意单位: % |
| 达到平仓线比例      | float64 | 注意单位: % |

接口示例

```python
import akshare as ak

stock_em_gpzy_distribute_statistics_bank_df = ak.stock_gpzy_distribute_statistics_bank_em()
print(stock_em_gpzy_distribute_statistics_bank_df)
```

#### 上市公司质押比例

接口: stock_gpzy_industry_data_em

目标地址: https://data.eastmoney.com/gpzy/industryData.aspx

描述: 东方财富网-数据中心-特色数据-股权质押-上市公司质押比例-行业数据

限量: 单次返回所有历史数据

输入参数

| 名称  | 类型  | 描述  |
|-----|-----|-----|
| -   | -   | -   |

输出参数

| 名称     | 类型      | 描述      |
|--------|---------|---------|
| 行业     | object  | -       |
| 平均质押比例 | float64 | 注意单位: % |
| 公司家数   | float64 | -       |
| 质押总笔数  | float64 | -       |
| 质押总股本  | float64 | -       |
| 最新质押市值 | float64 | -       |
| 统计时间   | object  | -       |

接口示例

```python
import akshare as ak

stock_gpzy_industry_data_em_df = ak.stock_gpzy_industry_data_em()
print(stock_gpzy_industry_data_em_df)
```

### 商誉专题

#### A股商誉市场概况

接口: stock_sy_profile_em

目标地址:  https://data.eastmoney.com/sy/scgk.html

描述: 东方财富网-数据中心-特色数据-商誉-A股商誉市场概况

限量: 单次所有历史数据

输入参数

| 名称  | 类型  | 描述  |
|-----|-----|-----|
| -   | -   | -   |

输出参数

| 名称         | 类型      | 描述      |
|------------|---------|---------|
| 报告期        | object  | -       |
| 商誉         | float64 | 注意单位: 元 |
| 商誉减值       | float64 | 注意单位: 元 |
| 净资产        | float64 | 注意单位: 元 |
| 商誉占净资产比例   | float64 | -       |
| 商誉减值占净资产比例 | float64 | -       |
| 净利润规模      | float64 | 注意单位: 元 |
| 商誉减值占净利润比例 | float64 | -       |

接口示例

```python
import akshare as ak

stock_sy_profile_em_df = ak.stock_sy_profile_em()
print(stock_sy_profile_em_df)
```

#### 商誉减值预期明细

接口: stock_sy_yq_em

目标地址: https://data.eastmoney.com/sy/yqlist.html

描述: 东方财富网-数据中心-特色数据-商誉-商誉减值预期明细

限量: 单次所有历史数据

输入参数

| 名称   | 类型  | 描述                      |
|------|-----|-------------------------|
| date | str | date="20221231"; 参见网页选项 |

输出参数

| 名称        | 类型      | 描述      |
|-----------|---------|---------|
| 序号        | int64   | -       |
| 股票代码      | object  | -       |
| 股票简称      | object  | -       |
| 业绩变动原因    | object  | -       |
| 最新商誉报告期   | object  | -       |
| 最新一期商誉    | float64 | 主要单位: 元 |
| 上年商誉      | float64 | 主要单位: 元 |
| 预计净利润-下限  | int64   | 主要单位: 元 |
| 预计净利润-上限  | int64   | 主要单位: 元 |
| 业绩变动幅度-下限 | float64 | 主要单位: % |
| 业绩变动幅度-上限 | float64 | 主要单位: % |
| 上年度同期净利润  | float64 | 主要单位: 元 |
| 公告日期      | object  | -       |
| 交易市场      | object  | -       |

接口示例

```python
import akshare as ak

stock_sy_yq_em_df = ak.stock_sy_yq_em(date="20221231")
print(stock_sy_yq_em_df)
```

#### 个股商誉减值明细

接口: stock_sy_jz_em

目标地址: https://data.eastmoney.com/sy/jzlist.html

描述: 东方财富网-数据中心-特色数据-商誉-个股商誉减值明细

限量: 单次返回所有历史数据

输入参数

| 名称   | 类型  | 描述                      |
|------|-----|-------------------------|
| date | str | date="20230331"; 参见网页选项 |

输出参数

| 名称         | 类型      | 描述      |
|------------|---------|---------|
| 序号         | int64   | -       |
| 股票代码       | object  | -       |
| 股票简称       | object  | -       |
| 商誉         | float64 | 注意单位: 元 |
| 商誉减值       | float64 | 注意单位: 元 |
| 商誉减值占净资产比例 | float64 | -       |
| 净利润        | float64 | 注意单位: 元 |
| 商誉减值占净利润比例 | float64 | -       |
| 公告日期       | object  | -       |
| 交易市场       | object  | -       |

接口示例

```python
import akshare as ak

stock_sy_jz_em_df = ak.stock_sy_jz_em(date="20230331")
print(stock_sy_jz_em_df)
```

#### 个股商誉明细

接口: stock_sy_em

目标地址: https://data.eastmoney.com/sy/list.html

描述: 东方财富网-数据中心-特色数据-商誉-个股商誉明细

限量: 单次返回所有历史数据

输入参数

| 名称   | 类型  | 描述                      |
|------|-----|-------------------------|
| date | str | date="20240630"; 参见网页选项 |

输出参数

| 名称       | 类型      | 描述      |
|----------|---------|---------|
| 序号       | int64   | -       |
| 股票代码     | object  | -       |
| 股票简称     | object  | -       |
| 商誉       | float64 | 注意单位: 元 |
| 商誉占净资产比例 | float64 |         |
| 净利润      | float64 | 注意单位: 元 |
| 净利润同比    | float64 |         |
| 上年商誉     | float64 | 注意单位: 元 |
| 公告日期     | object  | -       |
| 交易市场     | object  | -       |

接口示例

```python
import akshare as ak

stock_sy_em_df = ak.stock_sy_em(date="20240630")
print(stock_sy_em_df)
```

#### 行业商誉

接口: stock_sy_hy_em

目标地址: https://data.eastmoney.com/sy/hylist.html

描述: 东方财富网-数据中心-特色数据-商誉-行业商誉

限量: 单次返回所有历史数据

输入参数

| 名称   | 类型  | 描述                      |
|------|-----|-------------------------|
| date | str | date="20240930"; 参见网页选项 |

输出参数

| 名称           | 类型      | 描述 |
|--------------|---------|----|
| 行业名称         | object  | -  |
| 公司家数         | int64   | -  |
| 商誉规模         | float64 | -  |
| 净资产          | float64 | -  |
| 商誉规模占净资产规模比例 | float64 | -  |
| 净利润规模        | float64 | -  |

接口示例

```python
import akshare as ak

stock_sy_hy_em_df = ak.stock_sy_hy_em(date="20240930")
print(stock_sy_hy_em_df)
```

### 股票账户统计

#### 股票账户统计月度

接口: stock_account_statistics_em

目标地址: https://data.eastmoney.com/cjsj/gpkhsj.html

描述: 东方财富网-数据中心-特色数据-股票账户统计

限量: 单次返回从 201504 开始 202308 的所有历史数据

输入参数

| 名称  | 类型  | 描述  |
|-----|-----|-----|
| -   | -   | -   |

输出参数

| 名称         | 类型      | 描述       |
|------------|---------|----------|
| 数据日期       | object  | -        |
| 新增投资者-数量   | float64 | 注意单位: 万户 |
| 新增投资者-环比   | float64 | -        |
| 新增投资者-同比   | float64 | -        |
| 期末投资者-总量   | float64 | 注意单位: 万户 |
| 期末投资者-A股账户 | float64 | 注意单位: 万户 |
| 期末投资者-B股账户 | float64 | 注意单位: 万户 |
| 沪深总市值      | float64 | -        |
| 沪深户均市值     | float64 | 注意单位: 万  |
| 上证指数-收盘    | float64 | -        |
| 上证指数-涨跌幅   | float64 | -        |

接口示例

```python
import akshare as ak

stock_account_statistics_em_df = ak.stock_account_statistics_em()
print(stock_account_statistics_em_df)
```

### 分析师指数

#### 分析师指数排行

接口: stock_analyst_rank_em

目标地址: https://data.eastmoney.com/invest/invest/list.html

描述: 东方财富网-数据中心-研究报告-东方财富分析师指数

限量: 单次获取指定年份的所有数据

输入参数

| 名称   | 类型  | 描述                      |
|------|-----|-------------------------|
| year | str | year='2024'; 从 2013 年至今 |

输出参数

| 名称              | 类型      | 描述                       |
|-----------------|---------|--------------------------|
| 序号              | int64   | -                        |
| 分析师名称           | object  | -                        |
| 分析师单位           | object  | -                        |
| 年度指数            | float64 | -                        |
| xxxx年收益率        | float64 | 其中 xxxx 表示指定的年份; 注意单位: % |
| 3个月收益率          | float64 | 注意单位: %                  |
| 6个月收益率          | float64 | 注意单位: %                  |
| 12个月收益率         | float64 | 注意单位: %                  |
| 成分股个数           | int64   | -                        |
| xxxx最新个股评级-股票名称 | object  | 其中 xxxx 表示指定的年份          |
| xxxx最新个股评级-股票代码 | object  | 其中 xxxx 表示指定的年份          |
| 分析师ID           | object  | -                        |
| 行业代码            | object  | -                        |
| 行业              | object  | -                        |
| 更新日期            | object  | 数据更新日期                   |
| 年度              | object  | 数据更新年度                   |

接口示例

```python
import akshare as ak

stock_analyst_rank_em_df = ak.stock_analyst_rank_em(year='2024')
print(stock_analyst_rank_em_df)
```

#### 分析师详情

接口: stock_analyst_detail_em

目标地址: https://data.eastmoney.com/invest/invest/11000257131.html

描述: 东方财富网-数据中心-研究报告-东方财富分析师指数-分析师详情

限量: 单次获取指定 indicator 指定的数据

输入参数

| 名称         | 类型  | 描述                                                               |
|------------|-----|------------------------------------------------------------------|
| analyst_id | str | analyst_id="11000257131"; 分析师ID, 从 ak.stock_analyst_rank_em() 获取 |
| indicator  | str | indicator="最新跟踪成分股"; 从 {"最新跟踪成分股", "历史跟踪成分股", "历史指数"} 中选择        |

输出参数-最新跟踪成分股

| 名称        | 类型      | 描述      |
|-----------|---------|---------|
| 序号        | int64   | -       |
| 股票代码      | object  | -       |
| 股票名称      | object  | -       |
| 调入日期      | object  | -       |
| 最新评级日期    | object  | -       |
| 当前评级名称    | object  | -       |
| 成交价格(前复权) | float64 | -       |
| 最新价格      | float64 | -       |
| 阶段涨跌幅     | float64 | 注意单位: % |

接口示例-最新跟踪成分股

```python
import akshare as ak

stock_analyst_detail_em_df = ak.stock_analyst_detail_em(analyst_id="11000200926", indicator="最新跟踪成分股")
print(stock_analyst_detail_em_df)
```

输出参数-历史跟踪成分股

| 名称      | 类型      | 描述      |
|---------|---------|---------|
| 序号      | int64   | -       |
| 股票代码    | object  | -       |
| 股票名称    | object  | -       |
| 调入日期    | object  | -       |
| 调出日期    | object  | -       |
| 调入时评级名称 | object  | -       |
| 调出原因    | object  | -       |
| 累计涨跌幅   | float64 | 注意单位: % |

接口示例-历史跟踪成分股

```python
import akshare as ak

stock_em_analyst_detail_df = ak.stock_analyst_detail_em(analyst_id="11000200926", indicator="历史跟踪成分股")
print(stock_em_analyst_detail_df)
```

输出参数-历史指数

| 名称    | 类型      | 描述                   |
|-------|---------|----------------------|
| date  | object  | 日期                   |
| value | float64 | 指数数值; 注意: 此指数为东方财富制定 |

接口示例-历史指数

```python
import akshare as ak

stock_em_analyst_detail_df = ak.stock_analyst_detail_em(analyst_id="11000200926", indicator="历史指数")
print(stock_em_analyst_detail_df)
```

### 千股千评

接口: stock_comment_em

目标地址: https://data.eastmoney.com/stockcomment/

描述: 东方财富网-数据中心-特色数据-千股千评

限量: 单次获取所有数据

输入参数

| 名称  | 类型  | 描述  |
|-----|-----|-----|
| -   | -   | -   |

输出参数

| 名称    | 类型      | 描述      |
|-------|---------|---------|
| 序号    | int64   | -       |
| 代码    | object  | -       |
| 名称    | object  | -       |
| 最新价   | float64 | -       |
| 涨跌幅   | float64 | -       |
| 换手率   | float64 | 注意单位: % |
| 市盈率   | float64 | -       |
| 主力成本  | float64 | -       |
| 机构参与度 | float64 | -       |
| 综合得分  | float64 | -       |
| 上升    | int64   | 注意: 正负号 |
| 目前排名  | int64   | -       |
| 关注指数  | float64 | -       |
| 交易日   | float64 | -       |

接口示例

```python
import akshare as ak

stock_comment_em_df = ak.stock_comment_em()
print(stock_comment_em_df)
```

### 千股千评详情

#### 主力控盘

##### 机构参与度

接口: stock_comment_detail_zlkp_jgcyd_em

目标地址: https://data.eastmoney.com/stockcomment/stock/600000.html

描述: 东方财富网-数据中心-特色数据-千股千评-主力控盘-机构参与度

限量: 单次获取所有 symbol 的数据

输入参数

| 名称     | 类型  | 描述              |
|--------|-----|-----------------|
| symbol | str | symbol="600000" |

输出参数

| 名称    | 类型      | 描述      |
|-------|---------|---------|
| 交易日   | object  | -       |
| 机构参与度 | float64 | 注意单位: % |

接口示例

```python
import akshare as ak

stock_comment_detail_zlkp_jgcyd_em_df = ak.stock_comment_detail_zlkp_jgcyd_em(symbol="600000")
print(stock_comment_detail_zlkp_jgcyd_em_df)
```

#### 综合评价

##### 历史评分

接口: stock_comment_detail_zhpj_lspf_em

目标地址: https://data.eastmoney.com/stockcomment/stock/600000.html

描述: 东方财富网-数据中心-特色数据-千股千评-综合评价-历史评分

限量: 单次获取指定 symbol 的数据

输入参数

| 名称     | 类型  | 描述              |
|--------|-----|-----------------|
| symbol | str | symbol="600000" |

输出参数

| 名称  | 类型      | 描述  |
|-----|---------|-----|
| 日期  | object  | -   |
| 评分  | float64 | -   |

接口示例

```python
import akshare as ak

stock_comment_detail_zhpj_lspf_em_df = ak.stock_comment_detail_zhpj_lspf_em(symbol="600000")
print(stock_comment_detail_zhpj_lspf_em_df)
```

#### 市场热度

##### 用户关注指数

接口: stock_comment_detail_scrd_focus_em

目标地址: https://data.eastmoney.com/stockcomment/stock/600000.html

描述: 东方财富网-数据中心-特色数据-千股千评-市场热度-用户关注指数

限量: 单次获取所有数据

输入参数

| 名称     | 类型  | 描述              |
|--------|-----|-----------------|
| symbol | str | symbol="600000" |

输出参数

| 名称     | 类型      | 描述 |
|--------|---------|----|
| 交易日    | object  | -  |
| 用户关注指数 | float64 | -  |

接口示例

```python
import akshare as ak

stock_comment_detail_scrd_focus_em_df = ak.stock_comment_detail_scrd_focus_em(symbol="600000")
print(stock_comment_detail_scrd_focus_em_df)
```

##### 市场参与意愿

接口: stock_comment_detail_scrd_desire_em

目标地址: https://data.eastmoney.com/stockcomment/stock/600000.html

描述: 东方财富网-数据中心-特色数据-千股千评-市场热度-市场参与意愿

限量: 单次获取所有数据

输入参数

| 名称     | 类型  | 描述              |
|--------|-----|-----------------|
| symbol | str | symbol="600000" |

输出参数

| 名称       | 类型      | 描述 |
|----------|---------|----|
| 交易日期     | object  | -  |
| 股票代码     | object  | -  |
| 参与意愿     | float64 | -  |
| 5日平均参与意愿 | float64 | -  |
| 参与意愿变化   | float64 | -  |
| 5日平均变化   | float64 | -  |

接口示例

```python
import akshare as ak

stock_comment_detail_scrd_desire_em_df = ak.stock_comment_detail_scrd_desire_em(symbol="600000")
print(stock_comment_detail_scrd_desire_em_df)
```

### 沪深港通资金流向

接口: stock_hsgt_fund_flow_summary_em

目标地址: https://data.eastmoney.com/hsgt/index.html#lssj

描述: 东方财富网-数据中心-资金流向-沪深港通资金流向

限量: 单次获取沪深港通资金流向数据

输入参数

| 名称  | 类型  | 描述  |
|-----|-----|-----|
| -   | -   | -   |

输出参数

| 名称     | 类型      | 描述       |
|--------|---------|----------|
| 交易日    | object  | -        |
| 类型     | object  | -        |
| 板块     | object  | -        |
| 资金方向   | object  | -        |
| 交易状态   | int64   | 3 为收盘    |
| 成交净买额  | float64 | 注意单位: 亿元 |
| 资金净流入  | float64 | 注意单位: 亿元 |
| 当日资金余额 | float64 | 注意单位: 亿元 |
| 上涨数    | int64   | -        |
| 持平数    | int64   | -        |
| 下跌数    | int64   | -        |
| 相关指数   | object  | -        |
| 指数涨跌幅  | float64 | 注意单位: %  |

接口示例

```python
import akshare as ak

stock_hsgt_fund_flow_summary_em_df = ak.stock_hsgt_fund_flow_summary_em()
print(stock_hsgt_fund_flow_summary_em_df)
```

### 沪深港通持股

#### 结算汇率-深港通

接口: stock_sgt_settlement_exchange_rate_szse

目标地址: https://www.szse.cn/szhk/hkbussiness/exchangerate/index.html

描述: 深港通-港股通业务信息-结算汇率

限量: 单次获取所有深港通结算汇率数据

输入参数

| 名称  | 类型  | 描述  |
|-----|-----|-----|
| -   | -   | -   |

输出参数

| 名称       | 类型      | 描述  |
|----------|---------|-----|
| 适用日期     | object  | -   |
| 买入结算汇兑比率 | float64 | -   |
| 卖出结算汇兑比率 | float64 | -   |
| 货币种类     | object  | -   |

接口示例

```python
import akshare as ak

stock_sgt_settlement_exchange_rate_szse_df = ak.stock_sgt_settlement_exchange_rate_szse()
print(stock_sgt_settlement_exchange_rate_szse_df)
```

#### 结算汇率-沪港通

接口: stock_sgt_settlement_exchange_rate_sse

目标地址: http://www.sse.com.cn/services/hkexsc/disclo/ratios

描述: 沪港通-港股通信息披露-结算汇兑

限量: 单次获取所有沪港通结算汇率数据

输入参数

| 名称  | 类型  | 描述  |
|-----|-----|-----|
| -   | -   | -   |

输出参数

| 名称       | 类型      | 描述  |
|----------|---------|-----|
| 适用日期     | object  | -   |
| 买入结算汇兑比率 | float64 | -   |
| 卖出结算汇兑比率 | float64 | -   |
| 货币种类     | object  | -   |

接口示例

```python
import akshare as ak

stock_sgt_settlement_exchange_rate_sse_df = ak.stock_sgt_settlement_exchange_rate_sse()
print(stock_sgt_settlement_exchange_rate_sse_df)
```

#### 参考汇率-深港通

接口: stock_sgt_reference_exchange_rate_szse

目标地址: https://www.szse.cn/szhk/hkbussiness/exchangerate/index.html

描述: 深港通-港股通业务信息-参考汇率

限量: 单次获取所有深港通参考汇率数据

输入参数

| 名称  | 类型  | 描述  |
|-----|-----|-----|
| -   | -   | -   |

输出参数

| 名称      | 类型      | 描述  |
|---------|---------|-----|
| 适用日期    | object  | -   |
| 参考汇率买入价 | float64 | -   |
| 参考汇率卖出价 | float64 | -   |
| 货币种类    | object  | -   |

接口示例

```python
import akshare as ak

stock_sgt_reference_exchange_rate_szse_df = ak.stock_sgt_reference_exchange_rate_szse()
print(stock_sgt_reference_exchange_rate_szse_df)
```

#### 参考汇率-沪港通

接口: stock_sgt_reference_exchange_rate_sse

目标地址: http://www.sse.com.cn/services/hkexsc/disclo/ratios/

描述: 沪港通-港股通信息披露-参考汇率

限量: 单次获取所有沪港通参考汇率数据

输入参数

| 名称  | 类型  | 描述  |
|-----|-----|-----|
| -   | -   | -   |

输出参数

| 名称      | 类型      | 描述  |
|---------|---------|-----|
| 适用日期    | object  | -   |
| 参考汇率买入价 | float64 | -   |
| 参考汇率卖出价 | float64 | -   |
| 货币种类    | object  | -   |

接口示例

```python
import akshare as ak

stock_sgt_reference_exchange_rate_sse_df = ak.stock_sgt_reference_exchange_rate_sse()
print(stock_sgt_reference_exchange_rate_sse_df)
```

#### 港股通成份股

接口: stock_hk_ggt_components_em

目标地址: https://quote.eastmoney.com/center/gridlist.html#hk_components

描述: 东方财富网-行情中心-港股市场-港股通成份股

限量: 单次获取所有港股通成份股数据

输入参数

| 名称  | 类型  | 描述  |
|-----|-----|-----|
| -   | -   | -   |

输出参数

| 名称  | 类型      | 描述        |
|-----|---------|-----------|
| 序号  | int64   | -         |
| 代码  | object  | -         |
| 名称  | object  | -         |
| 最新价 | float64 | 注意单位: HKD |
| 涨跌额 | float64 | -         |
| 涨跌幅 | float64 | -         |
| 今开  | float64 | -         |
| 最高  | float64 | -         |
| 最低  | float64 | -         |
| 昨收  | float64 | -         |
| 成交量 | float64 | 注意单位: 股   |
| 成交额 | float64 | 注意单位: 港元  |

接口示例

```python
import akshare as ak

stock_hk_ggt_components_em_df = ak.stock_hk_ggt_components_em()
print(stock_hk_ggt_components_em_df)
```

#### 沪深港通分时数据

接口: stock_hsgt_fund_min_em

目标地址: https://data.eastmoney.com/hsgt/hsgtDetail/scgk.html

描述: 东方财富-数据中心-沪深港通-市场概括-分时数据

限量: 单次返回指定 symbol 的所有数据；20240513起数据源不再提供数据

输入参数

| 名称     | 类型  | 描述                                        |
|--------|-----|-------------------------------------------|
| symbol | str | symbol="北向资金"; choice of {"北向资金", "南向资金"} |

输出参数-北向资金

| 名称   | 类型      | 描述       |
|------|---------|----------|
| 日期   | object  | 日期       |
| 时间   | object  | 时间       |
| 沪股通  | float64 | 注意单位: 万元 |
| 深股通  | float64 | 注意单位: 万元 |
| 北向资金 | float64 | 注意单位: 万元 |

接口示例-北向资金

```python
import akshare as ak

stock_hsgt_fund_min_em_df = ak.stock_hsgt_fund_min_em(symbol="北向资金")
print(stock_hsgt_fund_min_em_df)
```

输出参数-南向资金

| 名称     | 类型      | 描述       |
|--------|---------|----------|
| 日期     | object  | 日期       |
| 时间     | object  | 时间       |
| 港股通(沪) | float64 | 注意单位: 万元 |
| 港股通(深) | float64 | 注意单位: 万元 |
| 南向资金   | float64 | 注意单位: 万元 |

接口示例-南向资金

```python
import akshare as ak

stock_hsgt_fund_min_em_df = ak.stock_hsgt_fund_min_em(symbol="南向资金")
print(stock_hsgt_fund_min_em_df)
```

#### 板块排行

接口: stock_hsgt_board_rank_em

目标地址: https://data.eastmoney.com/hsgtcg/bk.html

描述: 东方财富网-数据中心-沪深港通持股-板块排行

限量: 单次获取指定 symbol 和 indicator 的所有数据

输入参数

| 名称        | 类型  | 描述                                                                                |
|-----------|-----|-----------------------------------------------------------------------------------|
| symbol    | str | symbol="北向资金增持行业板块排行"; choice of {"北向资金增持行业板块排行", "北向资金增持概念板块排行", "北向资金增持地域板块排行"} |
| indicator | str | indicator="今日"; choice of {"今日", "3日", "5日", "10日", "1月", "1季", "1年"}             |

输出参数

| 名称                | 类型      | 描述      |
|-------------------|---------|---------|
| 序号                | int64   | -       |
| 名称                | object  | -       |
| 最新涨跌幅             | float64 | 注意单位: % |
| 北向资金今日持股-股票只数     | float64 | -       |
| 北向资金今日持股-市值       | float64 | 注意单位: 元 |
| 北向资金今日持股-占板块比     | float64 | -       |
| 北向资金今日持股-占北向资金比   | float64 | -       |
| 北向资金今日增持估计-股票只数   | float64 | -       |
| 北向资金今日增持估计-市值     | float64 | 注意单位: 元 |
| 北向资金今日增持估计-市值增幅   | float64 | -       |
| 北向资金今日增持估计-占板块比   | float64 | -       |
| 北向资金今日增持估计-占北向资金比 | float64 | -       |
| 今日增持最大股-市值        | float64 | -       |
| 今日增持最大股-占股本比      | float64 | -       |
| 今日减持最大股-占股本比      | float64 | -       |
| 今日减持最大股-市值        | float64 | -       |
| 报告时间              | object  | -       |

接口示例

```python
import akshare as ak

stock_hsgt_board_rank_em_df = ak.stock_hsgt_board_rank_em(symbol="北向资金增持行业板块排行", indicator="今日")
print(stock_hsgt_board_rank_em_df)
```

#### 个股排行

接口: stock_hsgt_hold_stock_em

目标地址: https://data.eastmoney.com/hsgtcg/list.html

描述: 东方财富网-数据中心-沪深港通持股-个股排行

限量: 单次获取指定 market 和 indicator 的所有数据

输入参数

| 名称        | 类型  | 描述                                                                                |
|-----------|-----|-----------------------------------------------------------------------------------|
| market    | str | market="沪股通"; choice of {"北向", "沪股通", "深股通"}                                      |
| indicator | str | indicator="沪股通"; choice of {"今日排行", "3日排行", "5日排行", "10日排行", "月排行", "季排行", "年排行"} |

输出参数

| 名称         | 类型      | 描述                            |
|------------|---------|-------------------------------|
| 序号         | int32   | -                             |
| 代码         | object  | -                             |
| 名称         | object  | -                             |
| 今日收盘价      | float64 | -                             |
| 今日涨跌幅      | float64 | 注意单位: %                       |
| 今日持股-股数    | float64 | 注意单位: 万                       |
| 今日持股-市值    | float64 | 注意单位: 万                       |
| 今日持股-占流通股比 | float64 | 注意单位: %                       |
| 今日持股-占总股本比 | float64 | 注意单位: %                       |
| 增持估计-股数    | float64 | 注意单位: 万; 主要字段名根据 indicator 变化 |
| 增持估计-市值    | float64 | 注意单位: 万; 主要字段名根据 indicator 变化 |
| 增持估计-市值增幅  | object  | 注意单位: %; 主要字段名根据 indicator 变化 |
| 增持估计-占流通股比 | float64 | 注意单位: ‰; 主要字段名根据 indicator 变化 |
| 增持估计-占总股本比 | float64 | 注意单位: ‰; 主要字段名根据 indicator 变化 |
| 所属板块       | object  | -                             |
| 日期         | object  | -                             |

接口示例

```python
import akshare as ak

stock_em_hsgt_hold_stock_df = ak.stock_hsgt_hold_stock_em(market="北向", indicator="今日排行")
print(stock_em_hsgt_hold_stock_df)
```

#### 每日个股统计

接口: stock_hsgt_stock_statistics_em

目标地址: http://data.eastmoney.com/hsgtcg/StockStatistics.aspx

描述: 东方财富网-数据中心-沪深港通-沪深港通持股-每日个股统计

限量: 单次获取指定 market 的 start_date 和 end_date 之间的所有数据, 该接口只能获取近期的数据

输入参数

| 名称         | 类型  | 描述                                                          |
|------------|-----|-------------------------------------------------------------|
| symbol     | str | symbol="北向持股"; choice of {"北向持股", "沪股通持股", "深股通持股", "南向持股"} |
| start_date | str | start_date="20210601"; 此处指定近期交易日                            |
| end_date   | str | end_date="20210608"; 此处指定近期交易日                              |

输出参数

| 名称          | 类型      | 描述                   |
|-------------|---------|----------------------|
| 持股日期        | object  | -                    |
| 股票代码        | object  | -                    |
| 股票简称        | object  | -                    |
| 当日收盘价       | float64 | 注意单位: 元; 南向持股单位为: 港元 |
| 当日涨跌幅       | float64 | 注意单位: %              |
| 持股数量        | float64 | 注意单位: 万股             |
| 持股市值        | float64 | 注意单位: 万元             |
| 持股数量占发行股百分比 | float64 | 注意单位: %              |
| 持股市值变化-1日   | float64 | 注意单位: 元              |
| 持股市值变化-5日   | float64 | 注意单位: 元              |
| 持股市值变化-10日  | float64 | 注意单位: 元              |

接口示例

```python
import akshare as ak

stock_hsgt_stock_statistics_em_df = ak.stock_hsgt_stock_statistics_em(symbol="北向持股", start_date="20211027", end_date="20211027")
print(stock_hsgt_stock_statistics_em_df)
```

#### 机构排行

接口: stock_hsgt_institution_statistics_em

目标地址: http://data.eastmoney.com/hsgtcg/InstitutionStatistics.aspx

描述: 东方财富网-数据中心-沪深港通-沪深港通持股-机构排行

限量: 单次获取指定 market 的所有数据, 该接口只能获取近期的数据

输入参数

| 名称         | 类型  | 描述                                                          |
|------------|-----|-------------------------------------------------------------|
| market     | str | market="北向持股"; choice of {"北向持股", "沪股通持股", "深股通持股", "南向持股"} |
| start_date | str | start_date="20201218"; 此处指定近期交易日                            |
| end_date   | str | end_date="20201218"; 此处指定近期交易日                              |

输出参数

| 名称         | 类型      | 描述                   |
|------------|---------|----------------------|
| 持股日期       | object  | -                    |
| 机构名称       | object  | -                    |
| 持股只数       | float64 | 注意单位: 只              |
| 持股市值       | float64 | 注意单位: 元; 南向持股单位为: 港元 |
| 持股市值变化-1日  | float64 | 注意单位: 元; 南向持股单位为: 港元 |
| 持股市值变化-5日  | float64 | 注意单位: 元; 南向持股单位为: 港元 |
| 持股市值变化-10日 | float64 | 注意单位: 元; 南向持股单位为: 港元 |

接口示例

```python
import akshare as ak

stock_hsgt_institution_statistics_em_df = ak.stock_hsgt_institution_statistics_em(market="北向持股", start_date="20201218", end_date="20201218")
print(stock_hsgt_institution_statistics_em_df)
```

#### 沪深港通-港股通(沪>港)实时行情

接口: stock_hsgt_sh_hk_spot_em

目标地址: https://quote.eastmoney.com/center/gridlist.html#hk_sh_stocks

描述: 东方财富网-行情中心-沪深港通-港股通(沪>港)-股票；按股票代码排序

限量: 单次获取所有数据

输入参数

| 名称 | 类型 | 描述 |
|----|----|----|
| -  | -  | -  |

输出参数

| 名称  | 类型      | 描述        |
|-----|---------|-----------|
| 序号  | int64   | -         |
| 代码  | object  | -         |
| 名称  | object  | -         |
| 最新价 | float64 | 注意单位: HKD |
| 涨跌额 | float64 | -         |
| 涨跌幅 | float64 | 注意单位: %   |
| 今开  | float64 | -         |
| 最高  | float64 | -         |
| 最低  | float64 | -         |
| 昨收  | float64 | -         |
| 成交量 | float64 | 注意单位: 亿股  |
| 成交额 | float64 | 注意单位: 亿港元 |

接口示例

```python
import akshare as ak

stock_hsgt_sh_hk_spot_em_df = ak.stock_hsgt_sh_hk_spot_em()
print(stock_hsgt_sh_hk_spot_em_df)
```

#### 沪深港通历史数据

接口: stock_hsgt_hist_em

目标地址: https://data.eastmoney.com/hsgt/index.html

描述: 东方财富网-数据中心-资金流向-沪深港通资金流向-沪深港通历史数据

限量: 单次获取指定 symbol 的所有数据

输入参数

| 名称     | 类型  | 描述                                                                      |
|--------|-----|-------------------------------------------------------------------------|
| symbol | str | symbol="北向资金"; choice of {"北向资金", "沪股通", "深股通", "南向资金", "港股通沪", "港股通深"} |

输出参数-北向资金

| 名称        | 类型      | 描述        |
|-----------|---------|-----------|
| 日期        | object  | -         |
| 当日成交净买额   | float64 | 注意单位: 亿元  |
| 买入成交额     | float64 | 注意单位: 亿元  |
| 卖出成交额     | float64 | 注意单位: 亿元  |
| 历史累计净买额   | float64 | 注意单位: 万亿元 |
| 当日资金流入    | float64 | 注意单位: 亿元  |
| 当日余额      | float64 | 注意单位: 亿元  |
| 持股市值      | float64 | 注意单位: 元   |
| 领涨股       | object  | -         |
| 领涨股-涨跌幅   | float64 | 注意单位: %   |
| 沪深300     | float64 | -         |
| 沪深300-涨跌幅 | float64 | 注意单位: %   |
| 领涨股-代码    | object  | -         |

接口示例-北向资金

```python
import akshare as ak

stock_hsgt_hist_em_df = ak.stock_hsgt_hist_em(symbol="北向资金")
print(stock_hsgt_hist_em_df)
```

输出参数-港股通沪

| 名称       | 类型      | 描述        |
|----------|---------|-----------|
| 日期       | object  | -         |
| 当日成交净买额  | float64 | 注意单位: 亿港元 |
| 买入成交额    | float64 | 注意单位: 亿港元 |
| 卖出成交额    | float64 | 注意单位: 亿港元 |
| 历史累计净买额  | float64 | 注意单位: 万亿元 |
| 当日资金流入   | float64 | 注意单位: 亿元  |
| 当日余额     | float64 | 注意单位: 亿元  |
| 持股市值     | float64 | 注意单位: 元   |
| 领涨股      | object  | -         |
| 领涨股-涨跌幅  | float64 | 注意单位: %   |
| 恒生指数     | float64 | -         |
| 恒生指数-涨跌幅 | float64 | 注意单位: %   |
| 领涨股-代码   | object  | -         |

接口示例-港股通沪

```python
import akshare as ak

stock_hsgt_hist_em_df = ak.stock_hsgt_hist_em(symbol="港股通沪")
print(stock_hsgt_hist_em_df)
```

#### 沪深港通持股-个股

接口: stock_hsgt_individual_em

目标地址: https://data.eastmoney.com/hsgt/StockHdDetail/002008.html

描述: 东方财富网-数据中心-沪深港通-沪深港通持股-具体股票

限量: 单次获取指定 symbol 的截至 20240816 的数据

输入参数

| 名称     | 类型  | 描述                       |
|--------|-----|--------------------------|
| symbol | str | symbol="002008"; 支持港股和A股 |

输出参数-A股

| 名称         | 类型      | 描述      |
|------------|---------|---------|
| 持股日期       | object  | -       |
| 当日收盘价      | float64 | 注意单位: 元 |
| 当日涨跌幅      | float64 | 注意单位: % |
| 持股数量       | int64   | 注意单位: 股 |
| 持股市值       | float64 | 注意单位: 元 |
| 持股数量占A股百分比 | float64 | 注意单位: % |
| 今日增持股数     | float64 | 注意单位: 股 |
| 今日增持资金     | float64 | 注意单位: 元 |
| 今日持股市值变化   | float64 | 注意单位: 元 |

输出参数-港股

| 名称         | 类型      | 描述       |
|------------|---------|----------|
| 持股日期       | object  | -        |
| 当日收盘价      | float64 | 注意单位: 港元 |
| 当日涨跌幅      | float64 | 注意单位: %  |
| 持股数量       | int64   | 注意单位: 股  |
| 持股市值       | float64 | 注意单位: 港元 |
| 持股数量占A股百分比 | float64 | 注意单位: %  |
| 持股市值变化-1日  | float64 | 注意单位: 港元 |
| 持股市值变化-5日  | float64 | 注意单位: 港元 |
| 持股市值变化-10日 | float64 | 注意单位: 港元 |

接口示例-A股

```python
import akshare as ak

stock_hsgt_individual_em_df = ak.stock_hsgt_individual_em(symbol="002008")
print(stock_hsgt_individual_em_df)
```

#### 沪深港通持股-个股详情

接口: stock_hsgt_individual_detail_em

目标地址: http://data.eastmoney.com/hsgtcg/StockHdStatistics/002008.html(示例)

描述: 东方财富网-数据中心-沪深港通-沪深港通持股-具体股票-个股详情

限量: 单次获取指定 symbol 的在 start_date 和 end_date 之间的所有数据; 注意只能返回 90 个交易日内的数据

输入参数

| 名称         | 类型  | 描述                                              |
|------------|-----|-------------------------------------------------|
| symbol     | str | symbol="002008"                                 |
| start_date | str | start_date="20210830"; 注意只能返回离最近交易日 90 个交易日内的数据 |
| end_date   | str | end_date="20211026"; 注意只能返回离最近交易日 90 个交易日内的数据   |

输出参数

| 名称         | 类型      | 描述      |
|------------|---------|---------|
| 持股日期       | object  | -       |
| 当日收盘价      | float64 | 注意单位: 元 |
| 当日涨跌幅      | float64 | 注意单位: % |
| 机构名称       | object  | -       |
| 持股数量       | int64   | 注意单位: 股 |
| 持股市值       | float64 | 注意单位: 元 |
| 持股数量占A股百分比 | float64 | 注意单位: % |
| 持股市值变化-1日  | float64 | 注意单位: 元 |
| 持股市值变化-5日  | float64 | 注意单位: 元 |
| 持股市值变化-10日 | float64 | 注意单位: 元 |

接口示例

```python
import akshare as ak

stock_hsgt_individual_detail_em_df = ak.stock_hsgt_individual_detail_em(
	symbol="002008",
	start_date="20210830",
	end_date="20211026"
)
print(stock_hsgt_individual_detail_em_df)
```

### 停复牌信息

接口: stock_tfp_em

目标地址: https://data.eastmoney.com/tfpxx/

描述: 东方财富网-数据中心-特色数据-停复牌信息

限量: 单次获取指定 date 的停复牌数据, 具体更新逻辑跟目标网页统一

输入参数

| 名称   | 类型  | 描述              |
|------|-----|-----------------|
| date | str | date="20240426" |

输出参数

| 名称     | 类型     | 描述  |
|--------|--------|-----|
| 序号     | int64  |     |
| 代码     | object |     |
| 名称     | object |     |
| 停牌时间   | object |     |
| 停牌截止时间 | object |     |
| 停牌期限   | object |     |
| 停牌原因   | object |     |
| 所属市场   | object |     |
| 预计复牌时间 | object |     |

接口示例

```python
import akshare as ak

stock_tfp_em_df = ak.stock_tfp_em(date="20240426")
print(stock_tfp_em_df)
```

### 停复牌

接口: news_trade_notify_suspend_baidu

目标地址: https://gushitong.baidu.com/calendar

描述: 百度股市通-交易提醒-停复牌

限量: 单次获取指定 date 的停复牌数据, 提供港股的停复牌数据

输入参数

| 名称   | 类型  | 描述              |
|------|-----|-----------------|
| date | str | date="20241107" |

输出参数

| 名称     | 类型     | 描述  |
|--------|--------|-----|
| 股票代码   | object |     |
| 股票简称   | object |     |
| 交易所    | object |     |
| 停牌时间   | object |     |
| 复牌时间   | object |     |
| 停牌事项说明 | object |     |

接口示例

```python
import akshare as ak

news_trade_notify_suspend_baidu_df = ak.news_trade_notify_suspend_baidu(date="20241107")
print(news_trade_notify_suspend_baidu_df)
```

### 分红派息

接口: news_trade_notify_dividend_baidu

目标地址: https://gushitong.baidu.com/calendar

描述: 百度股市通-交易提醒-分红派息

限量: 单次获取指定 date 的分红派息数据, 提供港股的分红派息数据

输入参数

| 名称     | 类型  | 描述              |
|--------|-----|-----------------|
| date   | str | date="20241107" |
| cookie | str | 可以指定 cookie     |

输出参数

| 名称   | 类型     | 描述  |
|------|--------|-----|
| 股票代码 | object |     |
| 除权日  | object |     |
| 分红   | object |     |
| 送股   | object |     |
| 转增   | object |     |
| 实物   | object |     |
| 交易所  | object |     |
| 股票简称 | object |     |
| 报告期  | object |     |

接口示例

```python
import akshare as ak

news_trade_notify_dividend_baidu_df = ak.news_trade_notify_dividend_baidu(date="20251126")
print(news_trade_notify_dividend_baidu_df)
```

### 个股新闻

接口: stock_news_em

目标地址: https://so.eastmoney.com/news/s?keyword=603777

描述: 东方财富指定个股的新闻资讯数据

限量: 指定 symbol 当日最近 100 条新闻资讯数据

输入参数

| 名称     | 类型  | 描述                          |
|--------|-----|-----------------------------|
| symbol | str | symbol="603777"; 股票代码或其他关键词 |

输出参数

| 名称   | 类型     | 描述  |
|------|--------|-----|
| 关键词  | object | -   |
| 新闻标题 | object | -   |
| 新闻内容 | object | -   |
| 发布时间 | object | -   |
| 文章来源 | object | -   |
| 新闻链接 | object | -   |

接口示例

```python
import akshare as ak

stock_news_em_df = ak.stock_news_em(symbol="603777")
print(stock_news_em_df)
```

### 财经内容精选

接口: stock_news_main_cx

目标地址: https://cxdata.caixin.com/pc/

描述: 财新网-财新数据通-最新

限量: 返回最新 100 条新闻数据

输入参数

| 名称 | 类型 | 描述 |
|----|----|----|
| -  | -  | -  |

输出参数

| 名称            | 类型     | 描述 |
|---------------|--------|----|
| tag           | object | -  |
| summary       | object | -  |
| url           | object | -  |

接口示例

```python
import akshare as ak

stock_news_main_cx_df = ak.stock_news_main_cx()
print(stock_news_main_cx_df)
```

### 财报发行

接口: news_report_time_baidu

目标地址: https://gushitong.baidu.com/calendar

描述: 百度股市通-财报发行

限量: 单次获取指定 date 的财报发行, 提供港股的财报发行数据

输入参数

| 名称   | 类型  | 描述              |
|------|-----|-----------------|
| date | str | date="20241107" |

输出参数

| 名称   | 类型     | 描述  |
|------|--------|-----|
| 股票代码 | object |     |
| 交易所  | object |     |
| 股票简称 | object |     |
| 财报期  | object |     |

接口示例

```python
import akshare as ak

news_report_time_baidu_df = ak.news_report_time_baidu(date="20241107")
print(news_report_time_baidu_df)
```

### 新股数据

#### 打新收益率

接口: stock_dxsyl_em

目标地址: https://data.eastmoney.com/xg/xg/dxsyl.html

描述: 东方财富网-数据中心-新股申购-打新收益率

限量: 单次获取所有打新收益率数据

输入参数

| 名称  | 类型  | 描述  |
|-----|-----|-----|
| -   | -   | -   |

输出参数

| 名称       | 类型      | 描述      |
|----------|---------|---------|
| 股票代码     | object  | -       |
| 股票简称     | object  | -       |
| 发行价      | float64 | -       |
| 最新价      | float64 | -       |
| 网上发行中签率  | float64 | 注意单位: % |
| 网上有效申购股数 | int64   | -       |
| 网上有效申购户数 | int64   | 注意单位: 户 |
| 网上超额认购倍数 | float64 | -       |
| 网下配售中签率  | float64 | 注意单位: % |
| 网下有效申购股数 | int64   | -       |
| 网下有效申购户数 | int64   | 注意单位: 户 |
| 网下配售认购倍数 | float64 | -       |
| 总发行数量    | int64   | -       |
| 开盘溢价     | float64 | -       |
| 首日涨幅     | float64 | -       |
| 上市日期     | object  | -       |

接口示例

```python
import akshare as ak

stock_dxsyl_em_df = ak.stock_dxsyl_em()
print(stock_dxsyl_em_df)
```

#### 新股申购与中签

接口: stock_xgsglb_em

目标地址: https://data.eastmoney.com/xg/xg/default_2.html

描述: 东方财富网-数据中心-新股数据-新股申购-新股申购与中签查询

限量: 单次获取指定 market 的新股申购与中签查询数据

输入参数

| 名称     | 类型  | 描述                                                                     |
|--------|-----|------------------------------------------------------------------------|
| symbol | str | symbol="全部股票"; choice of {"全部股票", "沪市主板", "科创板", "深市主板", "创业板", "北交所"} |

输出参数-其他（除北交所外）

| 名称       | 类型      | 描述      |
|----------|---------|---------|
| 股票代码     | object  | -       |
| 股票简称     | object  | -       |
| 交易所      | object  | -       |
| 板块       | object  | -       |
| 申购代码     | object  | -       |
| 发行总数     | float64 | 注意单位: 股 |
| 网上发行     | int64   | 注意单位: 股 |
| 顶格申购需配市值 | float64 | 注意单位: 股 |
| 申购上限     | int64   | -       |
| 发行价格     | float64 | -       |
| 最新价      | float64 | -       |
| 首日收盘价    | float64 | -       |
| 申购日期     | object  | -       |
| 中签号公布日   | object  | -       |
| 中签缴款日期   | object  | -       |
| 上市日期     | object  | -       |
| 发行市盈率    | float64 | -       |
| 行业市盈率    | float64 | -       |
| 中签率      | float64 | 注意单位: % |
| 询价累计报价倍数 | float64 | -       |
| 配售对象报价家数 | float64 | -       |
| 连续一字板数量  | object  | -       |
| 涨幅       | float64 | 注意单位: % |
| 每中一签获利   | float64 | 注意单位: 元 |

接口示例-其他（除北交所外）

```python
import akshare as ak

stock_xgsglb_em_df = ak.stock_xgsglb_em(symbol="全部股票")
print(stock_xgsglb_em_df)
```

输出参数-北交所

| 名称          | 类型      | 描述      |
|-------------|---------|---------|
| 代码          | object  | -       |
| 简称          | object  | -       |
| 申购代码        | object  | -       |
| 发行总数        | int64   | 注意单位: 股 |
| 网上-发行数量     | int64   | 注意单位: 股 |
| 网上-申购上限     | int64   | 注意单位: 股 |
| 网上-顶格所需资金   | int64   | 注意单位: 元 |
| 发行价格        | float64 | -       |
| 申购日         | object  | -       |
| 中签率         | float64 | -       |
| 稳获百股需配资金    | float64 | -       |
| 最新价格-价格     | float64 | -       |
| 最新价格-累计涨幅   | float64 | -       |
| 上市首日-上市日    | object  | -       |
| 上市首日-均价     | float64 | -       |
| 上市首日-涨幅     | float64 | -       |
| 上市首日-每百股获利  | float64 | -       |
| 上市首日-约合年化收益 | float64 | -       |
| 发行市盈率       | float64 | -       |
| 行业市盈率       | float64 | -       |
| 参与申购资金      | float64 | -       |
| 参与申购人数      | float64 | -       |

接口示例-北交所

```python
import akshare as ak

stock_xgsglb_em_df = ak.stock_xgsglb_em(symbol="北交所")
print(stock_xgsglb_em_df)
```

#### 新股申购与中签-同花顺

接口: stock_ipo_ths

目标地址: https://data.10jqka.com.cn/ipo/xgsgyzq/

描述: 同花顺-数据中心-新股申购与中签

限量: 单次返回指定 symbol 的历史新股申购与中签数据

输入参数

| 名称     | 类型  | 描述                                                                      |
|--------|-----|-------------------------------------------------------------------------|
| symbol | str | symbol="全部A股"; choice of {"全部A股", "沪市主板", "深市主板", "创业板", "科创板", "京市主板"} |

输出参数

| 名称           | 类型     | 描述 |
|--------------|--------|----|
| 股票代码         | object | -  |
| 股票简称         | object | -  |
| 申购代码         | object | -  |
| 发行总数（万股）     | object | -  |
| 网上发行（万股）     | object | -  |
| 申购上限（万股）     | object | -  |
| 顶格申购需配市值（万元） | object | -  |
| 发行价格         | object | -  |
| 发行市盈率        | object | -  |
| 行业市盈率        | object | -  |
| 申购日期         | object | -  |
| 中签率（%）       | object | -  |
| 中签号          | object | -  |
| 中签缴款日期       | object | -  |
| 上市日期         | object | -  |
| 打新收益（元）      | object | -  |
| 首日最高涨幅       | object | -  |
| 连板天数         | object | -  |

接口示例

```python
import akshare as ak

stock_ipo_ths_df = ak.stock_ipo_ths(symbol="全部A股")
print(stock_ipo_ths_df)
```

#### 新股申购与中签-港股-同花顺

接口: stock_ipo_hk_ths

目标地址: https://data.10jqka.com.cn/ipo/xgsgyzq/

描述: 同花顺-数据中心-新股申购与中签-港股

限量: 单次返回所有港股新股申购与中签数据

输入参数

| 名称 | 类型 | 描述 |
|----|----|----|
| -  | -  | -  |

输出参数

| 名称           | 类型     | 描述 |
|--------------|--------|----|
| 股票代码         | object | -  |
| 股票简称         | object | -  |
| 申购代码         | object | -  |
| 发行总数（万股）     | object | -  |
| 网上发行（万股）     | object | -  |
| 申购上限（万股）     | object | -  |
| 顶格申购需配市值（万元） | object | -  |
| 发行价格         | object | -  |
| 发行市盈率        | object | -  |
| 行业市盈率        | object | -  |
| 申购日期         | object | -  |
| 中签率（%）       | object | -  |
| 中签号          | object | -  |
| 中签缴款日期       | object | -  |
| 上市日期         | object | -  |
| 打新收益（元）      | object | -  |
| 首日最高涨幅       | object | -  |
| 连板天数         | object | -  |

接口示例

```python
import akshare as ak

stock_ipo_hk_ths_df = ak.stock_ipo_hk_ths()
print(stock_ipo_hk_ths_df)
```

### 年报季报

#### 业绩报表

接口: stock_yjbb_em

目标地址: http://data.eastmoney.com/bbsj/202003/yjbb.html

描述: 东方财富-数据中心-年报季报-业绩报表

限量: 单次获取指定 date 的业绩报告数据

输入参数

| 名称   | 类型  | 描述                                                                                         |
|------|-----|--------------------------------------------------------------------------------------------|
| date | str | date="20200331"; choice of {"XXXX0331", "XXXX0630", "XXXX0930", "XXXX1231"}; 从 20100331 开始 |

输出参数

| 名称           | 类型      | 描述      |
|--------------|---------|---------|
| 序号           | int64   | -       |
| 股票代码         | object  | -       |
| 股票简称         | object  | -       |
| 每股收益         | float64 | 注意单位: 元 |
| 营业总收入-营业总收入  | float64 | 注意单位: 元 |
| 营业总收入-同比增长   | float64 | 注意单位: % |
| 营业总收入-季度环比增长 | float64 | 注意单位: % |
| 净利润-净利润      | float64 | 注意单位: 元 |
| 净利润-同比增长     | float64 | 注意单位: % |
| 净利润-季度环比增长   | float64 | 注意单位: % |
| 每股净资产        | float64 | 注意单位: 元 |
| 净资产收益率       | float64 | 注意单位: % |
| 每股经营现金流量     | float64 | 注意单位: 元 |
| 销售毛利率        | float64 | 注意单位: % |
| 所处行业         | object  | -       |
| 最新公告日期       | object  | -       |

接口示例

```python
import akshare as ak

stock_yjbb_em_df = ak.stock_yjbb_em(date="20220331")
print(stock_yjbb_em_df)
```

#### 业绩快报

接口: stock_yjkb_em

目标地址: https://data.eastmoney.com/bbsj/202003/yjkb.html

描述: 东方财富-数据中心-年报季报-业绩快报

限量: 单次获取指定 date 的业绩快报数据

输入参数

| 名称   | 类型  | 描述                                                                                         |
|------|-----|--------------------------------------------------------------------------------------------|
| date | str | date="20200331"; choice of {"XXXX0331", "XXXX0630", "XXXX0930", "XXXX1231"}; 从 20100331 开始 |

输出参数

| 名称          | 类型     | 描述  |
|-------------|--------|-----|
| 序号          | object | -   |
| 股票代码        | object | -   |
| 股票简称        | object | -   |
| 每股收益        | object | -   |
| 营业收入-营业收入   | object | -   |
| 营业收入-去年同期   | object | -   |
| 营业收入-同比增长   | str    | -   |
| 营业收入-季度环比增长 | object | -   |
| 净利润-净利润     | object | -   |
| 净利润-去年同期    | object | -   |
| 净利润-同比增长    | str    | -   |
| 净利润-季度环比增长  | object | -   |
| 每股净资产       | object | -   |
| 净资产收益率      | object | -   |
| 所处行业        | object | -   |
| 公告日期        | object | -   |
| 市场板块        | object | -   |
| 证券类型        | object | -   |

接口示例

```python
import akshare as ak

stock_yjkb_em_df = ak.stock_yjkb_em(date="20200331")
print(stock_yjkb_em_df)
```

#### 业绩预告

接口: stock_yjyg_em

目标地址: https://data.eastmoney.com/bbsj/202003/yjyg.html

描述: 东方财富-数据中心-年报季报-业绩预告

限量: 单次获取指定 date 的业绩预告数据

输入参数

| 名称   | 类型  | 描述                                                                                         |
|------|-----|--------------------------------------------------------------------------------------------|
| date | str | date="20200331"; choice of {"XXXX0331", "XXXX0630", "XXXX0930", "XXXX1231"}; 从 20081231 开始 |

输出参数

| 名称     | 类型      | 描述      |
|--------|---------|---------|
| 序号     | object  | -       |
| 股票代码   | object  | -       |
| 股票简称   | object  | -       |
| 预测指标   | float64 | -       |
| 业绩变动   | float64 | -       |
| 预测数值   | float64 | 注意单位: 元 |
| 业绩变动幅度 | float64 | 注意单位: % |
| 业绩变动原因 | float64 | -       |
| 预告类型   | float64 | -       |
| 上年同期值  | float64 | 注意单位: 元 |
| 公告日期   | float64 | -       |

接口示例

```python
import akshare as ak

stock_yjyg_em_df = ak.stock_yjyg_em(date="20190331")
print(stock_yjyg_em_df)
```

#### 预约披露时间-东方财富

接口: stock_yysj_em

目标地址: https://data.eastmoney.com/bbsj/202003/yysj.html

描述: 东方财富-数据中心-年报季报-预约披露时间

限量: 单次获取指定 symbol 和 date 的预约披露时间数据

输入参数

| 名称     | 类型  | 描述                                                                                         |
|--------|-----|--------------------------------------------------------------------------------------------|
| symbol | str | symbol="沪深A股"; choice of {'沪深A股', '沪市A股', '科创板', '深市A股', '创业板', '京市A股', 'ST板'}             |
| date   | str | date="20200331"; choice of {"XXXX0331", "XXXX0630", "XXXX0930", "XXXX1231"}; 从 20081231 开始 |

输出参数

| 名称     | 类型     | 描述  |
|--------|--------|-----|
| 序号     | int64  | -   |
| 股票代码   | object | -   |
| 股票简称   | object | -   |
| 首次预约时间 | object | -   |
| 一次变更日期 | object | -   |
| 二次变更日期 | object | -   |
| 三次变更日期 | object | -   |
| 实际披露时间 | object | -   |

接口示例

```python
import akshare as ak

stock_yysj_em_df = ak.stock_yysj_em(symbol="沪深A股", date="20211231")
print(stock_yysj_em_df)
```

#### 预约披露时间-巨潮资讯

接口: stock_report_disclosure

目标地址: http://www.cninfo.com.cn/new/commonUrl?url=data/yypl

描述: 巨潮资讯-数据-预约披露的数据

限量: 单次获取指定 market 和 period 的预约披露数据

输入参数

| 名称     | 类型  | 描述                                                                                   |
|--------|-----|--------------------------------------------------------------------------------------|
| market | str | market="沪深京"; choice of {"沪深京", "深市", "深主板", "创业板", "沪市", "沪主板", "科创板", "北交所"}       |
| period | str | period="2021年报"; 近四期的财务报告; e.g., choice of {"2021一季", "2021半年报", "2021三季", "2021年报"} |

输出参数

| 名称   | 类型     | 描述  |
|------|--------|-----|
| 股票代码 | object | -   |
| 股票简称 | object | -   |
| 首次预约 | object | -   |
| 初次变更 | object | -   |
| 二次变更 | object | -   |
| 三次变更 | object | -   |
| 实际披露 | object | -   |

接口示例

```python
import akshare as ak

stock_report_disclosure_df = ak.stock_report_disclosure(market="沪深京", period="2022年报")
print(stock_report_disclosure_df)
```

#### 信息披露公告-巨潮资讯

接口: stock_zh_a_disclosure_report_cninfo

目标地址: http://www.cninfo.com.cn/new/commonUrl/pageOfSearch?url=disclosure/list/search

描述: 巨潮资讯-首页-公告查询-信息披露公告-沪深京

限量: 单次获取指定 symbol 的信息披露公告数据

输入参数

| 名称         | 类型  | 描述                                                                                                                                                                                                                         |
|------------|-----|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| symbol     | str | symbol="000001"; 股票代码                                                                                                                                                                                                      |
| market     | str | market="沪深京"; choice of {"沪深京", "港股", "三板", "基金", "债券", "监管", "预披露"}                                                                                                                                                       |
| keyword    | str | keyword=""; 关键词                                                                                                                                                                                                            |
| category   | str | category=""; choice of {'年报', '半年报', '一季报', '三季报', '业绩预告', '权益分派', '董事会', '监事会', '股东大会', '日常经营', '公司治理', '中介报告', '首发', '增发', '股权激励', '配股', '解禁', '公司债', '可转债', '其他融资', '股权变动', '补充更正', '澄清致歉', '风险提示', '特别处理和退市', '退市整理期'} |
| start_date | str | start_date="20230618"                                                                                                                                                                                                      |
| end_date   | str | end_date="20231219"                                                                                                                                                                                                        |

输出参数

| 名称   | 类型     | 描述 |
|------|--------|----|
| 代码   | object | -  |
| 简称   | object | -  |
| 公告标题 | object | -  |
| 公告时间 | object | -  |
| 公告链接 | object | -  |

接口示例

```python
import akshare as ak

stock_zh_a_disclosure_report_cninfo_df = ak.stock_zh_a_disclosure_report_cninfo(symbol="000001", market="沪深京", category="公司治理", start_date="20230619", end_date="20231220")
print(stock_zh_a_disclosure_report_cninfo_df)
```

#### 信息披露调研-巨潮资讯

接口: stock_zh_a_disclosure_relation_cninfo

目标地址: http://www.cninfo.com.cn/new/commonUrl/pageOfSearch?url=disclosure/list/search

描述: 巨潮资讯-首页-公告查询-信息披露调研-沪深京

限量: 单次获取指定 symbol 的信息披露调研数据

输入参数

| 名称         | 类型  | 描述                                                                   |
|------------|-----|----------------------------------------------------------------------|
| symbol     | str | symbol="000001"; 股票代码                                                |
| market     | str | market="沪深京"; choice of {"沪深京", "港股", "三板", "基金", "债券", "监管", "预披露"} |
| start_date | str | start_date="20230618"                                                |
| end_date   | str | end_date="20231219"                                                  |

输出参数

| 名称   | 类型     | 描述 |
|------|--------|----|
| 代码   | object | -  |
| 简称   | object | -  |
| 公告标题 | object | -  |
| 公告时间 | object | -  |
| 公告链接 | object | -  |

接口示例

```python
import akshare as ak

stock_zh_a_disclosure_relation_cninfo_df = ak.stock_zh_a_disclosure_relation_cninfo(symbol="000001", market="沪深京", start_date="20230619", end_date="20231220")
print(stock_zh_a_disclosure_relation_cninfo_df)
```

#### 行业分类数据-巨潮资讯

接口: stock_industry_category_cninfo

目标地址: https://webapi.cninfo.com.cn/#/apiDoc

描述: 巨潮资讯-数据-行业分类数据

限量: 单次获取指定 symbol 的行业分类数据

输入参数

| 名称     | 类型  | 描述                                                                                                                                 |
|--------|-----|------------------------------------------------------------------------------------------------------------------------------------|
| symbol | str | symbol="巨潮行业分类标准"; choice of {"证监会行业分类标准", "巨潮行业分类标准", "申银万国行业分类标准", "新财富行业分类标准", "国资委行业分类标准", "巨潮产业细分标准", "天相行业分类标准", "全球行业分类标准"} |

输出参数

| 名称     | 类型         | 描述  |
|--------|------------|-----|
| 类目编码   | object     | -   |
| 类目名称   | object     | -   |
| 终止日期   | datetime64 | -   |
| 行业类型   | object     | -   |
| 行业类型编码 | object     | -   |
| 类目名称英文 | object     | -   |
| 父类编码   | object     | -   |
| 分级     | int32      | -   |

接口示例

```python
import akshare as ak

stock_industry_category_cninfo_df = ak.stock_industry_category_cninfo(symbol="巨潮行业分类标准")
print(stock_industry_category_cninfo_df)
```

#### 上市公司行业归属的变动情况-巨潮资讯

接口: stock_industry_change_cninfo

目标地址: http://webapi.cninfo.com.cn/#/apiDoc

描述: 巨潮资讯-数据-上市公司行业归属的变动情况

限量: 单次获取指定 symbol 在 start_date 和 end_date 之间的上市公司行业归属的变动情况数据

输入参数

| 名称         | 类型  | 描述                    |
|------------|-----|-----------------------|
| symbol     | str | symbol="002594"       |
| start_date | str | start_date="20091227" |
| end_date   | str | end_date="20220708"   |

输出参数

| 名称     | 类型     | 描述  |
|--------|--------|-----|
| 新证券简称  | object | -   |
| 行业中类   | object | -   |
| 行业大类   | object | -   |
| 行业次类   | object | -   |
| 行业门类   | object | -   |
| 机构名称   | object | -   |
| 行业编码   | object | -   |
| 分类标准   | object | -   |
| 分类标准编码 | object | -   |
| 证券代码   | object | -   |
| 变更日期   | object | -   |

接口示例

```python
import akshare as ak

stock_industry_change_cninfo_df = ak.stock_industry_change_cninfo(symbol="002594", start_date="20091227", end_date="20220708")
print(stock_industry_change_cninfo_df)
```

#### 公司股本变动-巨潮资讯

接口: stock_share_change_cninfo

目标地址: https://webapi.cninfo.com.cn/#/apiDoc

描述: 巨潮资讯-数据-公司股本变动

限量: 单次获取指定 symbol 在 start_date 和 end_date 之间的公司股本变动数据

输入参数

| 名称         | 类型  | 描述                    |
|------------|-----|-----------------------|
| symbol     | str | symbol="002594"       |
| start_date | str | start_date="20091227" |
| end_date   | str | end_date="20241021"   |

输出参数

| 名称         | 类型      | 描述  |
|------------|---------|-----|
| 证券简称       | object  | -   |
| 机构名称       | object  | -   |
| 境外法人持股     | float64 | -   |
| 证券投资基金持股   | float64 | -   |
| 国家持股-受限    | float64 | -   |
| 国有法人持股     | float64 | -   |
| 配售法人股      | float64 | -   |
| 发起人股份      | float64 | -   |
| 未流通股份      | float64 | -   |
| 其中：境外自然人持股 | float64 | -   |
| 其他流通受限股份   | float64 | -   |
| 其他流通股      | float64 | -   |
| 外资持股-受限    | float64 | -   |
| 内部职工股      | float64 | -   |
| 境外上市外资股-H股 | float64 | -   |
| 其中：境内法人持股  | float64 | -   |
| 自然人持股      | float64 | -   |
| 人民币普通股     | float64 | -   |
| 国有法人持股-受限  | float64 | -   |
| 一般法人持股     | float64 | -   |
| 控股股东、实际控制人 | float64 | -   |
| 其中：限售H股    | float64 | -   |
| 变动原因       | object  | -   |
| 公告日期       | object  | -   |
| 境内法人持股     | float64 | -   |
| 证券代码       | object  | -   |
| 变动日期       | object  | -   |
| 战略投资者持股    | float64 | -   |
| 国家持股       | float64 | -   |
| 其中：限售B股    | float64 | -   |
| 其他未流通股     | float64 | -   |
| 流通受限股份     | float64 | -   |
| 优先股        | float64 | -   |
| 高管股        | float64 | -   |
| 总股本        | float64 | -   |
| 其中：限售高管股   | float64 | -   |
| 转配股        | float64 | -   |
| 境内上市外资股-B股 | float64 | -   |
| 其中：境外法人持股  | float64 | -   |
| 募集法人股      | float64 | -   |
| 已流通股份      | float64 | -   |
| 其中：境内自然人持股 | float64 | -   |
| 其他内资持股-受限  | float64 | -   |
| 变动原因编码     | object  | -   |

接口示例

```python
import akshare as ak

stock_share_change_cninfo_df = ak.stock_share_change_cninfo(symbol="002594", start_date="20091227", end_date="20241021")
print(stock_share_change_cninfo_df)
```

#### 配股实施方案-巨潮资讯

接口: stock_allotment_cninfo

目标地址: http://webapi.cninfo.com.cn/#/dataBrowse

描述: 巨潮资讯-个股-配股实施方案

限量: 单次获取指定 symbol 在 start_date 和 end_date 之间的公司股本变动数据

输入参数

| 名称         | 类型  | 描述                    |
|------------|-----|-----------------------|
| symbol     | str | symbol="600030"       |
| start_date | str | start_date="19700101" |
| end_date   | str | end_date="22220222"   |

输出参数

| 名称           | 类型         | 描述  |
|--------------|------------|-----|
| 记录标识         | int64      | -   |
| 证券简称         | object     | -   |
| 停牌起始日        | object     | -   |
| 上市公告日期       | object     | -   |
| 配股缴款起始日      | object     | -   |
| 可转配股数量       | float64    | -   |
| 停牌截止日        | object     | -   |
| 实际配股数量       | float64    | -   |
| 配股价格         | float64    | -   |
| 配股比例         | float64    | -   |
| 配股前总股本       | float64    | -   |
| 每股配权转让费(元)   | float64    | -   |
| 法人股实配数量      | float64    | -   |
| 实际募资净额       | float64    | -   |
| 大股东认购方式      | object     | -   |
| 其他配售简称       | object     | -   |
| 发行方式         | object     | -   |
| 配股失败，退还申购款日期 | object     | -   |
| 除权基准日        | object     | -   |
| 预计发行费用       | float64    | -   |
| 配股发行结果公告日    | object     | -   |
| 证券代码         | object     | -   |
| 配股权证交易截止日    | datetime64 | -   |
| 其他股份实配数量     | float64    | -   |
| 国家股实配数量      | float64    | -   |
| 委托单位         | object     | -   |
| 公众获转配数量      | float64    | -   |
| 其他配售代码       | object     | -   |
| 配售对象         | object     | -   |
| 配股权证交易起始日    | datetime64 | -   |
| 资金到账日        | datetime64 | -   |
| 机构名称         | object     | -   |
| 股权登记日        | object     | -   |
| 实际募资总额       | float64    | -   |
| 预计募集资金       | float64    | -   |
| 大股东认购数量      | float64    | -   |
| 公众股实配数量      | float64    | -   |
| 转配股实配数量      | float64    | -   |
| 承销费用         | float64    | -   |
| 法人获转配数量      | float64    | -   |
| 配股后流通股本      | float64    | -   |
| 股票类别         | object     | -   |
| 公众配售简称       | object     | -   |
| 发行方式编码       | object     | -   |
| 承销方式         | object     | -   |
| 公告日期         | object     | -   |
| 配股上市日        | object     | -   |
| 配股缴款截止日      | object     | -   |
| 承销余额(股)      | float64    | -   |
| 预计配股数量       | float64    | -   |
| 配股后总股本       | float64    | -   |
| 职工股实配数量      | float64    | -   |
| 承销方式编码       | object     | -   |
| 发行费用总额       | float64    | -   |
| 配股前流通股本      | float64    | -   |
| 股票类别编码       | object     | -   |
| 公众配售代码       | object     | -   |

接口示例

```python
import akshare as ak

stock_allotment_cninfo_df = ak.stock_allotment_cninfo(symbol="600030", start_date="19900101", end_date="20241022")
print(stock_allotment_cninfo_df)
```

#### 公司概况-巨潮资讯

接口: stock_profile_cninfo

目标地址: http://webapi.cninfo.com.cn/#/company

描述: 巨潮资讯-个股-公司概况

限量: 单次获取指定 symbol 的公司概况

输入参数

| 名称         | 类型  | 描述                    |
|------------|-----|-----------------------|
| symbol     | str | symbol="600030"       |

输出参数

| 名称   | 类型     | 描述  |
|------|--------|-----|
| 公司名称 | object | -   |
| 英文名称 | object | -   |
| 曾用简称 | object | -   |
| A股代码 | object | -   |
| A股简称 | object | -   |
| B股代码 | object | -   |
| B股简称 | object | -   |
| H股代码 | object | -   |
| H股简称 | object | -   |
| 入选指数 | object | -   |
| 所属市场 | object | -   |
| 所属行业 | object | -   |
| 法人代表 | object | -   |
| 注册资金 | object | -   |
| 成立日期 | object | -   |
| 上市日期 | object | -   |
| 官方网站 | object | -   |
| 电子邮箱 | object | -   |
| 联系电话 | object | -   |
| 传真   | object | -   |
| 注册地址 | object | -   |
| 办公地址 | object | -   |
| 邮政编码 | object | -   |
| 主营业务 | object | -   |
| 经营范围 | object | -   |
| 机构简介 | object | -   |

接口示例

```python
import akshare as ak

stock_profile_cninfo_df = ak.stock_profile_cninfo(symbol="600030")
print(stock_profile_cninfo_df)
```

#### 上市相关-巨潮资讯

接口: stock_ipo_summary_cninfo

目标地址: https://webapi.cninfo.com.cn/#/company

描述: 巨潮资讯-个股-上市相关

限量: 单次获取指定 symbol 的上市相关数据

输入参数

| 名称         | 类型  | 描述                    |
|------------|-----|-----------------------|
| symbol     | str | symbol="600030"       |

输出参数

| 名称       | 类型      | 描述       |
|----------|---------|----------|
| 股票代码     | object  | -        |
| 招股公告日期   | object  | -        |
| 中签率公告日   | object  | -        |
| 每股面值     | float64 | 注意单位: 元  |
| 总发行数量    | float64 | 注意单位: 万股 |
| 发行前每股净资产 | float64 | 注意单位: 元  |
| 摊薄发行市盈率  | float64 | -        |
| 募集资金净额   | float64 | 注意单位: 万元 |
| 上网发行日期   | object  | -        |
| 上市日期     | object  | -        |
| 发行价格     | float64 | 注意单位: 元  |
| 发行费用总额   | float64 | 注意单位: 万元 |
| 发行后每股净资产 | float64 | 注意单位: 元  |
| 上网发行中签率  | float64 | 注意单位: %  |
| 主承销商     | float64 | -        |

接口示例

```python
import akshare as ak

stock_ipo_summary_cninfo_df = ak.stock_ipo_summary_cninfo(symbol="600030")
print(stock_ipo_summary_cninfo_df)
```

#### 资产负债表-沪深

接口: stock_zcfz_em

目标地址: https://data.eastmoney.com/bbsj/202003/zcfz.html

描述: 东方财富-数据中心-年报季报-业绩快报-资产负债表

限量: 单次获取指定 date 的资产负债表数据

输入参数

| 名称   | 类型  |  描述                                                                                        |
|------|-----|--------------------------------------------------------------------------------------------|
| date | str | date="20240331"; choice of {"XXXX0331", "XXXX0630", "XXXX0930", "XXXX1231"}; 从 20081231 开始 |

输出参数

| 名称       | 类型      | 描述      |
|----------|---------|---------|
| 序号       | int64   | -       |
| 股票代码     | object  | -       |
| 股票简称     | object  | -       |
| 资产-货币资金  | float64 | 注意单位: 元 |
| 资产-应收账款  | float64 | 注意单位: 元 |
| 资产-存货    | float64 | 注意单位: 元 |
| 资产-总资产   | float64 | 注意单位: 元 |
| 资产-总资产同比 | float64 | 注意单位: % |
| 负债-应付账款  | float64 | 注意单位: 元 |
| 负债-总负债   | float64 | 注意单位: 元 |
| 负债-预收账款  | float64 | 注意单位: 元 |
| 负债-总负债同比 | float64 | 注意单位: % |
| 资产负债率    | float64 | 注意单位: % |
| 股东权益合计   | float64 | 注意单位: 元 |
| 公告日期     | object  | -       |

接口示例

```python
import akshare as ak

stock_zcfz_em_df = ak.stock_zcfz_em(date="20240331")
print(stock_zcfz_em_df)
```

#### 资产负债表-北交所

接口: stock_zcfz_bj_em

目标地址: https://data.eastmoney.com/bbsj/202003/zcfz.html

描述: 东方财富-数据中心-年报季报-业绩快报-资产负债表

限量: 单次获取指定 date 的资产负债表数据

输入参数

| 名称   | 类型  | 描述                                                                                         |
|------|-----|--------------------------------------------------------------------------------------------|
| date | str | date="20240331"; choice of {"XXXX0331", "XXXX0630", "XXXX0930", "XXXX1231"}; 从 20081231 开始 |

输出参数

| 名称       | 类型      | 描述      |
|----------|---------|---------|
| 序号       | int64   | -       |
| 股票代码     | object  | -       |
| 股票简称     | object  | -       |
| 资产-货币资金  | float64 | 注意单位: 元 |
| 资产-应收账款  | float64 | 注意单位: 元 |
| 资产-存货    | float64 | 注意单位: 元 |
| 资产-总资产   | float64 | 注意单位: 元 |
| 资产-总资产同比 | float64 | 注意单位: % |
| 负债-应付账款  | float64 | 注意单位: 元 |
| 负债-总负债   | float64 | 注意单位: 元 |
| 负债-预收账款  | float64 | 注意单位: 元 |
| 负债-总负债同比 | float64 | 注意单位: % |
| 资产负债率    | float64 | 注意单位: % |
| 股东权益合计   | float64 | 注意单位: 元 |
| 公告日期     | object  | -       |

接口示例

```python
import akshare as ak

stock_zcfz_bj_em_df = ak.stock_zcfz_bj_em(date="20240331")
print(stock_zcfz_bj_em_df)
```

#### 利润表

接口: stock_lrb_em

目标地址: http://data.eastmoney.com/bbsj/202003/lrb.html

描述: 东方财富-数据中心-年报季报-业绩快报-利润表

限量: 单次获取指定 date 的利润表数据

输入参数

| 名称   | 类型  | 描述                                                                                         |
|------|-----|--------------------------------------------------------------------------------------------|
| date | str | date="20240331"; choice of {"XXXX0331", "XXXX0630", "XXXX0930", "XXXX1231"}; 从 20120331 开始 |

输出参数

| 名称          | 类型      | 描述      |
|-------------|---------|---------|
| 序号          | int64   | -       |
| 股票代码        | object  | -       |
| 股票简称        | object  | -       |
| 净利润         | float64 | 注意单位: 元 |
| 净利润同比       | float64 | 注意单位: % |
| 营业总收入       | float64 | 注意单位: 元 |
| 营业总收入同比     | float64 | 注意单位: % |
| 营业总支出-营业支出  | float64 | 注意单位: 元 |
| 营业总支出-销售费用  | float64 | 注意单位: 元 |
| 营业总支出-管理费用  | float64 | 注意单位: 元 |
| 营业总支出-财务费用  | float64 | 注意单位: 元 |
| 营业总支出-营业总支出 | float64 | 注意单位: 元 |
| 营业利润        | float64 | 注意单位: 元 |
| 利润总额        | float64 | 注意单位: 元 |
| 公告日期        | object  | -       |

接口示例

```python
import akshare as ak

stock_lrb_em_df = ak.stock_lrb_em(date="20240331")
print(stock_lrb_em_df)
```

#### 现金流量表

接口: stock_xjll_em

目标地址: http://data.eastmoney.com/bbsj/202003/xjll.html

描述: 东方财富-数据中心-年报季报-业绩快报-现金流量表

限量: 单次获取指定 date 的现金流量表数据

输入参数

| 名称   | 类型  | 描述                                                                                         |
|------|-----|--------------------------------------------------------------------------------------------|
| date | str | date="20200331"; choice of {"XXXX0331", "XXXX0630", "XXXX0930", "XXXX1231"}; 从 20081231 开始 |

输出参数

| 名称            | 类型      | 描述      |
|---------------|---------|---------|
| 序号            | int64   | -       |
| 股票代码          | object  | -       |
| 股票简称          | object  | -       |
| 净现金流-净现金流     | float64 | 注意单位: 元 |
| 净现金流-同比增长     | float64 | 注意单位: % |
| 经营性现金流-现金流量净额 | float64 | 注意单位: 元 |
| 经营性现金流-净现金流占比 | float64 | 注意单位: % |
| 投资性现金流-现金流量净额 | float64 | 注意单位: 元 |
| 投资性现金流-净现金流占比 | float64 | 注意单位: % |
| 融资性现金流-现金流量净额 | float64 | 注意单位: 元 |
| 融资性现金流-净现金流占比 | float64 | 注意单位: % |
| 公告日期          | object  | -       |

接口示例

```python
import akshare as ak

stock_xjll_em_df = ak.stock_xjll_em(date="20240331")
print(stock_xjll_em_df)
```

### 高管持股

#### 股东增减持

接口: stock_ggcg_em

目标地址: http://data.eastmoney.com/executive/gdzjc.html

描述: 东方财富网-数据中心-特色数据-高管持股

限量: 单次获取所有高管持股数据数据

输入参数

| 名称     | 类型  | 描述                                            |
|--------|-----|-----------------------------------------------|
| symbol | str | symbol="全部"; choice of {"全部", "股东增持", "股东减持"} |

输出参数

| 名称             | 类型      | 描述       |
|----------------|---------|----------|
| 代码             | object  | -        |
| 名称             | object  | -        |
| 最新价            | float64 | -        |
| 涨跌幅            | float64 | 注意单位: %  |
| 股东名称           | object  | -        |
| 持股变动信息-增减      | float64 | -        |
| 持股变动信息-变动数量    | float64 | 注意单位: 万股 |
| 持股变动信息-占总股本比例  | float64 | 注意单位: %  |
| 持股变动信息-占流通股比例  | float64 | 注意单位: %  |
| 变动后持股情况-持股总数   | float64 | 注意单位: 万股 |
| 变动后持股情况-占总股本比例 | float64 | 注意单位: %  |
| 变动后持股情况-持流通股数  | float64 | 注意单位: 万股 |
| 变动后持股情况-占流通股比例 | float64 | 注意单位: %  |
| 变动开始日          | object  | -        |
| 变动截止日          | object  | -        |
| 公告日            | object  | -        |

接口示例

```python
import akshare as ak

stock_ggcg_em_df = ak.stock_ggcg_em(symbol="全部")
print(stock_ggcg_em_df)
```

### 分红配送

#### 分红配送-东财

接口: stock_fhps_em

目标地址: https://data.eastmoney.com/yjfp/

描述: 东方财富-数据中心-年报季报-分红配送

限量: 单次获取指定日期的分红配送数据

输入参数

| 名称   | 类型  | 描述                                                                 |
|------|-----|--------------------------------------------------------------------|
| date | str | date="20231231"; choice of {"XXXX0630", "XXXX1231"}; 从 19901231 开始 |

输出参数

| 名称          | 类型      | 描述  |
|-------------|---------|-----|
| 代码          | object  | -   |
| 名称          | object  | -   |
| 送转股份-送转总比例  | float64 | -   |
| 送转股份-送转比例   | float64 | -   |
| 送转股份-转股比例   | float64 | -   |
| 现金分红-现金分红比例 | float64 | -   |
| 现金分红-股息率    | float64 | -   |
| 每股收益        | float64 | -   |
| 每股净资产       | float64 | -   |
| 每股公积金       | float64 | -   |
| 每股未分配利润     | float64 | -   |
| 净利润同比增长     | float64 | -   |
| 总股本         | int64   | -   |
| 预案公告日       | object  | -   |
| 股权登记日       | object  | -   |
| 除权除息日       | object  | -   |
| 方案进度        | object  | -   |
| 最新公告日期      | object  | -   |

接口示例

```python
import akshare as ak

stock_fhps_em_df = ak.stock_fhps_em(date="20231231")
print(stock_fhps_em_df)
```

#### 分红配送详情-东财

接口: stock_fhps_detail_em

目标地址: https://data.eastmoney.com/yjfp/detail/300073.html

描述: 东方财富网-数据中心-分红送配-分红送配详情

限量: 单次获取指定 symbol 的分红配送详情数据

输入参数

| 名称     | 类型  | 描述              |
|--------|-----|-----------------|
| symbol | str | symbol="300073" |

输出参数

| 名称            | 类型      | 描述 |
|---------------|---------|----|
| 报告期           | object  | -  |
| 业绩披露日期        | object  | -  |
| 送转股份-送转总比例    | float64 | -  |
| 送转股份-送股比例     | float64 | -  |
| 送转股份-转股比例     | float64 | -  |
| 现金分红-现金分红比例   | float64 | -  |
| 现金分红-现金分红比例描述 | object  | -  |
| 现金分红-股息率      | float64 | -  |
| 每股收益          | float64 | -  |
| 每股净资产         | float64 | -  |
| 每股公积金         | float64 | -  |
| 每股未分配利润       | float64 | -  |
| 净利润同比增长       | float64 | -  |
| 总股本           | int64   | -  |
| 预案公告日         | object  | -  |
| 股权登记日         | object  | -  |
| 除权除息日         | object  | -  |
| 方案进度          | object  | -  |
| 最新公告日期        | object  | -  |

接口示例

```python
import akshare as ak

stock_fhps_detail_em_df = ak.stock_fhps_detail_em(symbol="300073")
print(stock_fhps_detail_em_df)
```

#### 分红情况-同花顺

接口: stock_fhps_detail_ths

目标地址: https://basic.10jqka.com.cn/new/603444/bonus.html

描述: 同花顺-分红情况

限量: 单次获取指定 symbol 的分红情况数据

输入参数

| 名称     | 类型  | 描述                           |
|--------|-----|------------------------------|
| symbol | str | symbol="603444"; 兼容 A 股和 B 股 |

输出参数

| 名称         | 类型     | 描述                |
|------------|--------|-------------------|
| 报告期        | object | -                 |
| 董事会日期      | object | -                 |
| 股东大会预案公告日期 | object | -                 |
| 实施公告日      | object | -                 |
| 分红方案说明     | object | -                 |
| A股股权登记日    | object | 注意: 根据 A 股和 B 股变化 |
| A股除权除息日    | object | 注意: 根据 A 股和 B 股变化 |
| 分红总额       | object | -                 |
| 方案进度       | object | -                 |
| 股利支付率      | object | -                 |
| 税前分红率      | object | -                 |

接口示例

```python
import akshare as ak

stock_fhps_detail_ths_df = ak.stock_fhps_detail_ths(symbol="603444")
print(stock_fhps_detail_ths_df)
```

#### 分红配送详情-港股-同花顺

接口: stock_hk_fhpx_detail_ths

目标地址: https://stockpage.10jqka.com.cn/HK0700/bonus/

描述: 同花顺-港股-分红派息

限量: 单次获取指定股票的分红派息数据

输入参数

| 名称     | 类型  | 描述                  |
|--------|-----|---------------------|
| symbol | str | symbol="0700"; 港股代码 |

输出参数

| 名称         | 类型     | 描述 |
|------------|--------|----|
| 公告日期       | object | -  |
| 方案         | object | -  |
| 除净日        | object | -  |
| 派息日        | object | -  |
| 过户日期起止日-起始 | object | -  |
| 过户日期起止日-截止 | object | -  |
| 类型         | object | -  |
| 进度         | object | -  |
| 以股代息       | object | -  |

接口示例

```python
import akshare as ak

stock_hk_fhpx_detail_ths_df = ak.stock_hk_fhpx_detail_ths(symbol="0700")
print(stock_hk_fhpx_detail_ths_df)
```

### 资金流向

#### 同花顺

##### 个股资金流

接口: stock_fund_flow_individual

目标地址: https://data.10jqka.com.cn/funds/ggzjl/#refCountId=data_55f13c2c_254

描述: 同花顺-数据中心-资金流向-个股资金流

限量: 单次获取指定 symbol 的概念资金流数据

输入参数

| 名称     | 类型  | 描述                                                              |
|--------|-----|-----------------------------------------------------------------|
| symbol | str | symbol="即时"; choice of {“即时”, "3日排行", "5日排行", "10日排行", "20日排行"} |

输出参数-即时

| 名称   | 类型      | 描述      |
|------|---------|---------|
| 序号   | int32   | -       |
| 股票代码 | int64   | -       |
| 股票简称 | object  | -       |
| 最新价  | float64 | -       |
| 涨跌幅  | object  | 注意单位: % |
| 换手率  | object  | -       |
| 流入资金 | object  | 注意单位: 元 |
| 流出资金 | object  | 注意单位: 元 |
| 净额   | object  | 注意单位: 元 |
| 成交额  | object  | 注意单位: 元 |

接口示例-即时

```python
import akshare as ak

stock_fund_flow_individual_df = ak.stock_fund_flow_individual(symbol="即时")
print(stock_fund_flow_individual_df)
```

输出参数-3日、5日、10日和20日

| 名称     | 类型      | 描述      |
|--------|---------|---------|
| 序号     | int32   | -       |
| 股票代码   | int64   | -       |
| 股票简称   | object  | -       |
| 最新价    | float64 | -       |
| 阶段涨跌幅  | object  | 注意单位: % |
| 连续换手率  | object  | 注意单位: % |
| 资金流入净额 | float64 | 注意单位: 元 |

接口示例-3日、5日、10日和20日

```python
import akshare as ak

stock_fund_flow_individual_df = ak.stock_fund_flow_individual(symbol="3日排行")
print(stock_fund_flow_individual_df)
```

##### 概念资金流

接口: stock_fund_flow_concept

目标地址: https://data.10jqka.com.cn/funds/gnzjl/#refCountId=data_55f13c2c_254

描述: 同花顺-数据中心-资金流向-概念资金流

限量: 单次获取指定 symbol 的概念资金流数据

输入参数

| 名称     | 类型  | 描述                                                              |
|--------|-----|-----------------------------------------------------------------|
| symbol | str | symbol="即时"; choice of {“即时”, "3日排行", "5日排行", "10日排行", "20日排行"} |

输出参数-即时

| 名称      | 类型      | 描述      |
|---------|---------|---------|
| 序号      | int32   | -       |
| 行业      | object  | -       |
| 行业指数    | float64 | -       |
| 行业-涨跌幅  | float64 | 注意单位: % |
| 流入资金    | float64 | 注意单位: 亿 |
| 流出资金    | float64 | 注意单位: 亿 |
| 净额      | float64 | 注意单位: 亿 |
| 公司家数    | float64 | -       |
| 领涨股     | object  | -       |
| 领涨股-涨跌幅 | float64 | 注意单位: % |
| 当前价     | float64 | 注意单位: 元 |

接口示例-即时

```python
import akshare as ak

stock_fund_flow_concept_df = ak.stock_fund_flow_concept(symbol="即时")
print(stock_fund_flow_concept_df)
```

输出参数-3日、5日、10日和20日

| 名称    | 类型      | 描述      |
|-------|---------|---------|
| 序号    | int32   | -       |
| 行业    | object  | -       |
| 公司家数  | int64   | -       |
| 行业指数  | float64 | -       |
| 阶段涨跌幅 | object  | 注意单位: % |
| 流入资金  | float64 | 注意单位: 亿 |
| 流出资金  | float64 | 注意单位: 亿 |
| 净额    | float64 | 注意单位: 亿 |

接口示例-3日、5日、10日和20日

```python
import akshare as ak

stock_fund_flow_concept_df = ak.stock_fund_flow_concept(symbol="3日排行")
print(stock_fund_flow_concept_df)
```

##### 行业资金流

接口: stock_fund_flow_industry

目标地址: http://data.10jqka.com.cn/funds/hyzjl/#refCountId=data_55f13c2c_254

描述: 同花顺-数据中心-资金流向-行业资金流

限量: 单次获取指定 symbol 的行业资金流数据

输入参数

| 名称     | 类型  | 描述                                                              |
|--------|-----|-----------------------------------------------------------------|
| symbol | str | symbol="即时"; choice of {“即时”, "3日排行", "5日排行", "10日排行", "20日排行"} |

输出参数-即时

| 名称      | 类型      | 描述      |
|---------|---------|---------|
| 序号      | int32   | -       |
| 行业      | object  | -       |
| 行业指数    | float64 | -       |
| 行业-涨跌幅  | object  | 注意单位: % |
| 流入资金    | float64 | 注意单位: 亿 |
| 流出资金    | float64 | 注意单位: 亿 |
| 净额      | float64 | 注意单位: 亿 |
| 公司家数    | float64 | -       |
| 领涨股     | object  | -       |
| 领涨股-涨跌幅 | object  | 注意单位: % |
| 当前价     | float64 | -       |

接口示例-即时

```python
import akshare as ak

stock_fund_flow_industry_df = ak.stock_fund_flow_industry(symbol="即时")
print(stock_fund_flow_industry_df)
```

输出参数-3日、5日、10日和20日

| 名称    | 类型      | 描述      |
|-------|---------|---------|
| 序号    | int32   | -       |
| 行业    | object  | -       |
| 公司家数  | int64   | -       |
| 行业指数  | float64 | -       |
| 阶段涨跌幅 | object  | 注意单位: % |
| 流入资金  | float64 | 注意单位: 亿 |
| 流出资金  | float64 | 注意单位: 亿 |
| 净额    | float64 | 注意单位: 亿 |

接口示例-3日、5日、10日和20日

```python
import akshare as ak

stock_fund_flow_industry_df = ak.stock_fund_flow_industry(symbol="3日排行")
print(stock_fund_flow_industry_df)
```

##### 大单追踪

接口: stock_fund_flow_big_deal

目标地址: https://data.10jqka.com.cn/funds/ddzz

描述: 同花顺-数据中心-资金流向-大单追踪

限量: 单次获取当前时点的所有大单追踪数据

输入参数

| 名称  | 类型  | 描述  |
|-----|-----|-----|
| -   | -   | -   |

输出参数-即时

| 名称   | 类型      | 描述       |
|------|---------|----------|
| 成交时间 | object  | -        |
| 股票代码 | int64   | -        |
| 股票简称 | object  | -        |
| 成交价格 | float64 | -        |
| 成交量  | int64   | 注意单位: 股  |
| 成交额  | float64 | 注意单位: 万元 |
| 大单性质 | object  | -        |
| 涨跌幅  | object  | -        |
| 涨跌额  | object  | -        |

接口示例-即时

```python
import akshare as ak

stock_fund_flow_big_deal_df = ak.stock_fund_flow_big_deal()
print(stock_fund_flow_big_deal_df)
```

#### 东方财富

##### 个股资金流

接口: stock_individual_fund_flow

目标地址: https://data.eastmoney.com/zjlx/detail.html

描述: 东方财富网-数据中心-个股资金流向

限量: 单次获取指定市场和股票的近 100 个交易日的资金流数据

输入参数

| 名称     | 类型  | 描述                                                 |
|--------|-----|----------------------------------------------------|
| stock  | str | stock="000425"; 股票代码                               |
| market | str | market="sh"; 上海证券交易所: sh, 深证证券交易所: sz, 北京证券交易所: bj |

输出参数

| 名称         | 类型      | 描述      |
|------------|---------|---------|
| 日期         | object  | -       |
| 收盘价        | float64 | -       |
| 涨跌幅        | float64 | 注意单位: % |
| 主力净流入-净额   | float64 | -       |
| 主力净流入-净占比  | float64 | 注意单位: % |
| 超大单净流入-净额  | float64 | -       |
| 超大单净流入-净占比 | float64 | 注意单位: % |
| 大单净流入-净额   | float64 | -       |
| 大单净流入-净占比  | float64 | 注意单位: % |
| 中单净流入-净额   | float64 | -       |
| 中单净流入-净占比  | float64 | 注意单位: % |
| 小单净流入-净额   | float64 | -       |
| 小单净流入-净占比  | float64 | 注意单位: % |

接口示例

```python
import akshare as ak

stock_individual_fund_flow_df = ak.stock_individual_fund_flow(stock="600094", market="sh")
print(stock_individual_fund_flow_df)
```

##### 个股资金流排名

接口: stock_individual_fund_flow_rank

目标地址: http://data.eastmoney.com/zjlx/detail.html

描述: 东方财富网-数据中心-资金流向-排名

限量: 单次获取指定类型的个股资金流排名数据

输入参数

| 名称        | 类型  | 描述                                               |
|-----------|-----|--------------------------------------------------|
| indicator | str | indicator="今日"; choice {"今日", "3日", "5日", "10日"} |

输出参数-今日

| 名称           | 类型      | 描述      |
|--------------|---------|---------|
| 序号           | int64   | -       |
| 代码           | object  | -       |
| 名称           | object  | -       |
| 最新价          | float64 | -       |
| 今日涨跌幅        | float64 | 注意单位: % |
| 今日主力净流入-净额   | float64 | -       |
| 今日主力净流入-净占比  | float64 | 注意单位: % |
| 今日超大单净流入-净额  | float64 | -       |
| 今日超大单净流入-净占比 | float64 | 注意单位: % |
| 今日大单净流入-净额   | float64 | -       |
| 今日大单净流入-净占比  | float64 | 注意单位: % |
| 今日中单净流入-净额   | float64 | -       |
| 今日中单净流入-净占比  | float64 | 注意单位: % |
| 今日小单净流入-净额   | float64 | -       |
| 今日小单净流入-净占比  | float64 | 注意单位: % |

接口示例-今日

```python
import akshare as ak

stock_individual_fund_flow_rank_df = ak.stock_individual_fund_flow_rank(indicator="今日")
print(stock_individual_fund_flow_rank_df)
```

输出参数-3日

| 名称           | 类型      | 描述      |
|--------------|---------|---------|
| 序号           | int64   | -       |
| 代码           | object  | -       |
| 名称           | object  | -       |
| 最新价          | float64 | -       |
| 3日涨跌幅        | float64 | 注意单位: % |
| 3日主力净流入-净额   | float64 | -       |
| 3日主力净流入-净占比  | float64 | 注意单位: % |
| 3日超大单净流入-净额  | float64 | -       |
| 3日超大单净流入-净占比 | float64 | 注意单位: % |
| 3日大单净流入-净额   | float64 | -       |
| 3日大单净流入-净占比  | float64 | 注意单位: % |
| 3日中单净流入-净额   | float64 | -       |
| 3日中单净流入-净占比  | float64 | 注意单位: % |
| 3日小单净流入-净额   | float64 | -       |
| 3日小单净流入-净占比  | float64 | 注意单位: % |

接口示例-3日

```python
import akshare as ak

stock_individual_fund_flow_rank_df = ak.stock_individual_fund_flow_rank(indicator="3日")
print(stock_individual_fund_flow_rank_df)
```

输出参数-5日

| 名称           | 类型      | 描述      |
|--------------|---------|---------|
| 序号           | int64   | -       |
| 代码           | object  | -       |
| 名称           | object  | -       |
| 最新价          | float64 | -       |
| 5日涨跌幅        | float64 | 注意单位: % |
| 5日主力净流入-净额   | float64 | -       |
| 5日主力净流入-净占比  | float64 | 注意单位: % |
| 5日超大单净流入-净额  | float64 | -       |
| 5日超大单净流入-净占比 | float64 | 注意单位: % |
| 5日大单净流入-净额   | float64 | -       |
| 5日大单净流入-净占比  | float64 | 注意单位: % |
| 5日中单净流入-净额   | float64 | -       |
| 5日中单净流入-净占比  | float64 | 注意单位: % |
| 5日小单净流入-净额   | float64 | -       |
| 5日小单净流入-净占比  | float64 | 注意单位: % |

接口示例-5日

```python
import akshare as ak

stock_individual_fund_flow_rank_df = ak.stock_individual_fund_flow_rank(indicator="5日")
print(stock_individual_fund_flow_rank_df)
```

输出参数-10日

| 名称            | 类型      | 描述      |
|---------------|---------|---------|
| 序号            | int32   | -       |
| 代码            | object  | -       |
| 名称            | object  | -       |
| 最新价           | float64 | -       |
| 10日涨跌幅        | float64 | 注意单位: % |
| 10日主力净流入-净额   | float64 | -       |
| 10日主力净流入-净占比  | float64 | 注意单位: % |
| 10日超大单净流入-净额  | float64 | -       |
| 10日超大单净流入-净占比 | float64 | 注意单位: % |
| 10日大单净流入-净额   | float64 | -       |
| 10日大单净流入-净占比  | float64 | 注意单位: % |
| 10日中单净流入-净额   | float64 | -       |
| 10日中单净流入-净占比  | float64 | 注意单位: % |
| 10日小单净流入-净额   | float64 | -       |
| 10日小单净流入-净占比  | float64 | 注意单位: % |

接口示例-10日

```python
import akshare as ak

stock_individual_fund_flow_rank_df = ak.stock_individual_fund_flow_rank(indicator="10日")
print(stock_individual_fund_flow_rank_df)
```

##### 大盘资金流

接口: stock_market_fund_flow

目标地址: https://data.eastmoney.com/zjlx/dpzjlx.html

描述: 东方财富网-数据中心-资金流向-大盘

限量: 单次获取大盘资金流向历史数据

输入参数

| 名称  | 类型  | 描述  |
|-----|-----|-----|
| -   | -   | -   |

输出参数

| 名称         | 类型      | 描述      |
|------------|---------|---------|
| 日期         | object  | -       |
| 上证-收盘价     | float64 | -       |
| 上证-涨跌幅     | float64 | 注意单位: % |
| 深证-收盘价     | float64 | -       |
| 深证-涨跌幅     | float64 | 注意单位: % |
| 主力净流入-净额   | float64 | -       |
| 主力净流入-净占比  | float64 | 注意单位: % |
| 超大单净流入-净额  | float64 | -       |
| 超大单净流入-净占比 | float64 | 注意单位: % |
| 大单净流入-净额   | float64 | -       |
| 大单净流入-净占比  | float64 | 注意单位: % |
| 中单净流入-净额   | float64 | -       |
| 中单净流入-净占比  | float64 | 注意单位: % |
| 小单净流入-净额   | float64 | -       |
| 小单净流入-净占比  | float64 | 注意单位: % |

接口示例

```python
import akshare as ak

stock_market_fund_flow_df = ak.stock_market_fund_flow()
print(stock_market_fund_flow_df)
```

##### 板块资金流排名

接口: stock_sector_fund_flow_rank

目标地址: https://data.eastmoney.com/bkzj/hy.html

描述: 东方财富网-数据中心-资金流向-板块资金流-排名

限量: 单次获取指定板块的指定期限的资金流排名数据

输入参数

| 名称          | 类型  | 描述                                                         |
|-------------|-----|------------------------------------------------------------|
| indicator   | str | indicator="今日"; choice of {"今日", "5日", "10日"}              |
| sector_type | str | sector_type="行业资金流"; choice of {"行业资金流", "概念资金流", "地域资金流"} |

输出参数-行业资金流-今日

| 名称         | 类型      | 描述      |
|------------|---------|---------|
| 序号         | int64   | -       |
| 名称         | object  | -       |
| 今日涨跌幅      | float64 | 注意单位: % |
| 主力净流入-净额   | float64 | -       |
| 主力净流入-净占比  | float64 | 注意单位: % |
| 超大单净流入-净额  | float64 | -       |
| 超大单净流入-净占比 | float64 | 注意单位: % |
| 大单净流入-净额   | float64 | -       |
| 大单净流入-净占比  | float64 | 注意单位: % |
| 中单净流入-净额   | float64 | -       |
| 中单净流入-净占比  | float64 | 注意单位: % |
| 小单净流入-净额   | float64 | -       |
| 小单净流入-净占比  | float64 | 注意单位: % |
| 主力净流入最大股   | object  | -       |

接口示例-行业资金流-今日

```python
import akshare as ak

stock_sector_fund_flow_rank_df = ak.stock_sector_fund_flow_rank(indicator="今日", sector_type="行业资金流")
print(stock_sector_fund_flow_rank_df)
```

##### 主力净流入排名

接口: stock_main_fund_flow

目标地址: https://data.eastmoney.com/zjlx/list.html

描述: 东方财富网-数据中心-资金流向-主力净流入排名

限量: 单次获取指定 symbol 的主力净流入排名数据

输入参数

| 名称     | 类型  | 描述                                                                                     |
|--------|-----|----------------------------------------------------------------------------------------|
| symbol | str | symbol="全部股票"；choice of {"全部股票", "沪深A股", "沪市A股", "科创板", "深市A股", "创业板", "沪市B股", "深市B股"} |

输出参数

| 名称           | 类型      | 描述      |
|--------------|---------|---------|
| 序号           | int64   | -       |
| 代码           | object  | -       |
| 名称           | object  | -       |
| 最新价          | float64 | -       |
| 今日排行榜-主力净占比  | float64 | 注意单位: % |
| 今日排行榜-今日排名   | float64 | -       |
| 今日排行榜-今日涨跌   | float64 | 注意单位: % |
| 5日排行榜-主力净占比  | float64 | 注意单位: % |
| 5日排行榜-5日排名   | int64   | -       |
| 5日排行榜-5日涨跌   | float64 | 注意单位: % |
| 10日排行榜-主力净占比 | float64 | 注意单位: % |
| 10日排行榜-10日排名 | int64   | -       |
| 10日排行榜-10日涨跌 | float64 | 注意单位: % |
| 所属板块         | object  | -       |


接口示例

```python
import akshare as ak

stock_main_fund_flow_df = ak.stock_main_fund_flow(symbol="全部股票")
print(stock_main_fund_flow_df)
```

##### 行业个股资金流

接口: stock_sector_fund_flow_summary

目标地址: https://data.eastmoney.com/bkzj/BK1034.html

描述: 东方财富网-数据中心-资金流向-行业资金流-xx行业个股资金流

限量: 单次获取指定 symbol 的个股资金流

输入参数

| 名称        | 类型  | 描述                                            |
|-----------|-----|-----------------------------------------------|
| symbol    | str | symbol="电源设备"                                 |
| indicator | str | indicator="今日"; choice of {"今日", "5日", "10日"} |

输出参数-今日

| 名称           | 类型      | 描述      |
|--------------|---------|---------|
| 序号           | int64   | -       |
| 代码           | object  | -       |
| 名称           | object  | -       |
| 最新价          | float64 | -       |
| 今日涨跌幅        | float64 | 注意单位: % |
| 今日主力净流入-净额   | float64 | -       |
| 今日主力净流入-净占比  | float64 | 注意单位: % |
| 今日超大单净流入-净额  | float64 | -       |
| 今日超大单净流入-净占比 | float64 | 注意单位: % |
| 今日大单净流入-净额   | float64 | -       |
| 今日大单净流入-净占比  | float64 | 注意单位: % |
| 今日中单净流入-净额   | float64 | -       |
| 今日中单净流入-净占比  | float64 | 注意单位: % |
| 今日小单净流入-净额   | float64 | -       |
| 今日小单净流入-净占比  | float64 | 注意单位: % |

接口示例

```python
import akshare as ak

stock_sector_fund_flow_summary_df = ak.stock_sector_fund_flow_summary(symbol="电源设备", indicator="今日")
print(stock_sector_fund_flow_summary_df)
```

##### 行业历史资金流

接口: stock_sector_fund_flow_hist

目标地址: https://data.eastmoney.com/bkzj/BK1034.html

描述: 东方财富网-数据中心-资金流向-行业资金流-行业历史资金流

限量: 单次获取指定行业的行业历史资金流数据

输入参数

| 名称     | 类型  | 描述            |
|--------|-----|---------------|
| symbol | str | symbol="汽车服务" |

输出参数

| 名称         | 类型      | 描述      |
|------------|---------|---------|
| 日期         | object  | 注意单位: % |
| 主力净流入-净额   | float64 | -       |
| 主力净流入-净占比  | float64 | 注意单位: % |
| 超大单净流入-净额  | float64 | -       |
| 超大单净流入-净占比 | float64 | 注意单位: % |
| 大单净流入-净额   | float64 | -       |
| 大单净流入-净占比  | float64 | 注意单位: % |
| 中单净流入-净额   | float64 | -       |
| 中单净流入-净占比  | float64 | 注意单位: % |
| 小单净流入-净额   | float64 | -       |
| 小单净流入-净占比  | float64 | 注意单位: % |

接口示例

```python
import akshare as ak

stock_sector_fund_flow_hist_df = ak.stock_sector_fund_flow_hist(symbol="汽车服务")
print(stock_sector_fund_flow_hist_df)
```

##### 概念历史资金流

接口: stock_concept_fund_flow_hist

目标地址: https://data.eastmoney.com/bkzj/BK0574.html

描述: 东方财富网-数据中心-资金流向-概念资金流-概念历史资金流

限量: 单次获取指定 symbol 的近期概念历史资金流数据

输入参数

| 名称     | 类型  | 描述            |
|--------|-----|---------------|
| symbol | str | symbol="数据要素" |

输出参数

| 名称         | 类型      | 描述      |
|------------|---------|---------|
| 日期         | object  | 注意单位: % |
| 主力净流入-净额   | float64 | -       |
| 主力净流入-净占比  | float64 | 注意单位: % |
| 超大单净流入-净额  | float64 | -       |
| 超大单净流入-净占比 | float64 | 注意单位: % |
| 大单净流入-净额   | float64 | -       |
| 大单净流入-净占比  | float64 | 注意单位: % |
| 中单净流入-净额   | float64 | -       |
| 中单净流入-净占比  | float64 | 注意单位: % |
| 小单净流入-净额   | float64 | -       |
| 小单净流入-净占比  | float64 | 注意单位: % |

接口示例

```python
import akshare as ak

stock_concept_fund_flow_hist_df = ak.stock_concept_fund_flow_hist(symbol="数据要素")
print(stock_concept_fund_flow_hist_df)
```

### 筹码分布

接口: stock_cyq_em

目标地址: https://quote.eastmoney.com/concept/sz000001.html

描述: 东方财富网-概念板-行情中心-日K-筹码分布

限量: 单次返回指定 symbol 和 adjust 的近 90 个交易日数据

输入参数

| 名称     | 类型  | 描述                                                           |
|--------|-----|--------------------------------------------------------------|
| symbol | str | symbol="000001"; 股票代码                                        |
| adjust | str | adjust=""; choice of {"qfq": "前复权", "hfq": "后复权", "": "不复权"} |

输出参数

| 名称     | 类型      | 描述 |
|--------|---------|----|
| 日期     | object  | -  |
| 获利比例   | float64 | -  |
| 平均成本   | float64 | -  |
| 90成本-低 | float64 | -  |
| 90成本-高 | float64 | -  |
| 90集中度  | float64 | -  |
| 70成本-低 | float64 | -  |
| 70成本-高 | float64 | -  |
| 70集中度  | float64 | -  |

接口示例

```python
import akshare as ak

stock_cyq_em_df = ak.stock_cyq_em(symbol="000001", adjust="")
print(stock_cyq_em_df)
```

### 基本面数据

#### 股东大会

接口: stock_gddh_em

目标地址: https://data.eastmoney.com/gddh/

描述: 东方财富网-数据中心-股东大会

限量: 单次返回所有数据

输入参数

| 名称 | 类型 | 描述 |
|----|----|----|
| -  | -  | -  |

输出参数

| 名称         | 类型     | 描述 |
|------------|--------|----|
| 代码         | object | -  |
| 简称         | object | -  |
| 股东大会名称     | object | -  |
| 召开开始日      | object | -  |
| 股权登记日      | object | -  |
| 现场登记日      | object | -  |
| 网络投票时间-开始日 | object | -  |
| 网络投票时间-结束日 | object | -  |
| 决议公告日      | object | -  |
| 公告日        | object | -  |
| 序列号        | object | -  |
| 提案         | object | -  |

接口示例

```python
import akshare as ak

stock_gddh_em_df = ak.stock_gddh_em()
print(stock_gddh_em_df)
```

#### 重大合同

接口: stock_zdhtmx_em

目标地址: https://data.eastmoney.com/zdht/mx.html

描述: 东方财富网-数据中心-重大合同-重大合同明细

限量: 单次返回指定 start_date 和 end_date 的所有数据

输入参数

| 名称         | 类型  | 描述                    |
|------------|-----|-----------------------|
| start_date | str | start_date="20200819" |
| end_date   | str | end_date="20230819"   |

输出参数

| 名称            | 类型      | 描述 |
|---------------|---------|----|
| 序号            | int64   | -  |
| 股票代码          | object  | -  |
| 股票简称          | object  | -  |
| 签署主体          | object  | -  |
| 签署主体-与上市公司关系  | object  | -  |
| 其他签署方         | object  | -  |
| 其他签署方-与上市公司关系 | object  | -  |
| 合同类型          | object  | -  |
| 合同名称          | object  | -  |
| 合同金额          | float64 | -  |
| 上年度营业收入       | float64 | -  |
| 占上年度营业收入比例    | float64 | -  |
| 最新财务报表的营业收入   | float64 | -  |
| 签署日期          | object  | -  |
| 公告日期          | object  | -  |

接口示例

```python
import akshare as ak

stock_zdhtmx_em_df = ak.stock_zdhtmx_em(start_date="20220819", end_date="20230819")
print(stock_zdhtmx_em_df)
```

#### 个股研报

接口: stock_research_report_em

目标地址: https://data.eastmoney.com/report/stock.jshtml

描述: 东方财富网-数据中心-研究报告-个股研报

限量: 单次返回指定 symbol 的所有数据

输入参数

| 名称     | 类型  | 描述              |
|--------|-----|-----------------|
| symbol | str | symbol="000001" |

输出参数

| 名称            | 类型      | 描述 |
|---------------|---------|----|
| 序号            | int64   | -  |
| 股票代码          | object  | -  |
| 股票简称          | object  | -  |
| 报告名称          | object  | -  |
| 东财评级          | object  | -  |
| 机构            | object  | -  |
| 近一月个股研报数      | int64   | -  |
| 2024-盈利预测-收益  | float64 | -  |
| 2024-盈利预测-市盈率 | float64 | -  |
| 2025-盈利预测-收益  | float64 | -  |
| 2025-盈利预测-市盈率 | float64 | -  |
| 2026-盈利预测-收益  | float64 | -  |
| 2026-盈利预测-市盈率 | float64 | -  |
| 行业            | object  | -  |
| 日期            | object  | -  |
| 报告PDF链接       | object  | -  |

接口示例

```python
import akshare as ak

stock_research_report_em_df = ak.stock_research_report_em(symbol="000001")
print(stock_research_report_em_df)
```

#### 沪深京 A 股公告

接口: stock_notice_report

目标地址: https://data.eastmoney.com/notices/hsa/5.html

描述: 东方财富网-数据中心-公告大全-沪深京 A 股公告

限量: 单次获取指定 symbol 和 date 的数据

输入参数

| 名称     | 类型  | 描述                                                                                      |
|--------|-----|-----------------------------------------------------------------------------------------|
| symbol | str | symbol='财务报告'; choice of {"全部", "重大事项", "财务报告", "融资公告", "风险提示", "资产重组", "信息变更", "持股变动"} |
| date   | str | date="20220511"; 指定日期                                                                   |

输出参数

| 名称   | 类型     | 描述  |
|------|--------|-----|
| 代码   | object | -   |
| 名称   | object | -   |
| 公告标题 | object | -   |
| 公告类型 | object | -   |
| 公告日期 | object | -   |
| 网址   | object | -   |

接口示例

```python
import akshare as ak

stock_notice_report_df = ak.stock_notice_report(symbol='财务报告', date="20240613")
print(stock_notice_report_df)
```

#### 沪深京 A 股个股公告

接口: stock_individual_notice_report

目标地址: https://data.eastmoney.com/notices/stock/300237.html

描述: 东方财富网-数据中心-公告大全-个股

限量: 单次获取指定 security, symbol, begin_date 和 end_date 的数据

输入参数

| 名称         | 类型  | 描述                                                                                      |
|------------|-----|-----------------------------------------------------------------------------------------|
| security   | str | security="300237"; 股票代码                                                                 |
| symbol     | str | symbol='财务报告'; choice of {"全部", "重大事项", "财务报告", "融资公告", "风险提示", "资产重组", "信息变更", "持股变动"} |
| begin_date | str | date="20250408"; 指定开始日期; 默认为空即不限制开始日期                                                   |
| end_date   | str | date="20260408"; 指定结束日期; 默认为空即不限制结束日期                                                   |

输出参数

| 名称   | 类型     | 描述  |
|------|--------|-----|
| 代码   | object | -   |
| 名称   | object | -   |
| 公告标题 | object | -   |
| 公告类型 | object | -   |
| 公告日期 | object | -   |
| 网址   | object | -   |

接口示例

```python
import akshare as ak

stock_individual_notice_report_df = ak.stock_individual_notice_report(security="300237", symbol="财务报告", begin_date="20250401", end_date="20260101")
print(stock_individual_notice_report_df)
```

#### 财务报表-新浪

接口: stock_financial_report_sina

目标地址: https://vip.stock.finance.sina.com.cn/corp/go.php/vFD_FinanceSummary/stockid/600600/displaytype/4.phtml?source=fzb&qq-pf-to=pcqq.group

描述: 新浪财经-财务报表-三大报表

限量: 单次获取指定报表的所有年份数据的历史数据

注意: 原始数据中有 `国内票证结算` 和 `内部应收款` 字段重, 返回数据中已经剔除

输入参数

| 名称     | 类型  | 描述                                                  |
|--------|-----|-----------------------------------------------------|
| stock  | str | stock="sh600600"; 带市场标识的股票代码                        |
| symbol | str | symbol="现金流量表"; choice of {"资产负债表", "利润表", "现金流量表"} |

输出参数

| 名称   | 类型     | 描述   |
|------|--------|------|
| 报告日  | object | 报告日期 |
| 流动资产 | object | -    |
| ...  | object | -    |
| 类型   | object | -    |
| 更新日期 | object | -    |

接口示例

```python
import akshare as ak

stock_financial_report_sina_df = ak.stock_financial_report_sina(stock="sh600600", symbol="资产负债表")
print(stock_financial_report_sina_df)
```

#### 财务报表-东财

##### 资产负债表-按报告期

接口: stock_balance_sheet_by_report_em

目标地址: https://emweb.securities.eastmoney.com/PC_HSF10/NewFinanceAnalysis/Index?type=web&code=sh600519#lrb-0

描述: 东方财富-股票-财务分析-资产负债表-按报告期

限量: 单次获取指定 symbol 的资产负债表-按报告期数据

输入参数

| 名称     | 类型  | 描述                      |
|--------|-----|-------------------------|
| symbol | str | symbol="SH600519"; 股票代码 |

输出参数

| 名称  | 类型  | 描述          |
|-----|-----|-------------|
| -   | -   | 319 项，不逐一列出 |

接口示例

```python
import akshare as ak

stock_balance_sheet_by_report_em_df = ak.stock_balance_sheet_by_report_em(symbol="SH600519")
print(stock_balance_sheet_by_report_em_df)
```

##### 资产负债表-按年度

接口: stock_balance_sheet_by_yearly_em

目标地址: https://emweb.securities.eastmoney.com/PC_HSF10/NewFinanceAnalysis/Index?type=web&code=sh600519#lrb-0

描述: 东方财富-股票-财务分析-资产负债表-按年度

限量: 单次获取指定 symbol 的资产负债表-按年度数据

输入参数

| 名称     | 类型  | 描述                      |
|--------|-----|-------------------------|
| symbol | str | symbol="SH600519"; 股票代码 |

输出参数

| 名称  | 类型  | 描述          |
|-----|-----|-------------|
| -   | -   | 319 项，不逐一列出 |

接口示例

```python
import akshare as ak

stock_balance_sheet_by_yearly_em_df = ak.stock_balance_sheet_by_yearly_em(symbol="SH600519")
print(stock_balance_sheet_by_yearly_em_df)
```

##### 利润表-按报告期

接口: stock_profit_sheet_by_report_em

目标地址: https://emweb.securities.eastmoney.com/PC_HSF10/NewFinanceAnalysis/Index?type=web&code=sh600519#lrb-0

描述: 东方财富-股票-财务分析-利润表-报告期

限量: 单次获取指定 symbol 的利润表-报告期数据

输入参数

| 名称     | 类型  | 描述                      |
|--------|-----|-------------------------|
| symbol | str | symbol="SH600519"; 股票代码 |

输出参数

| 名称  | 类型  | 描述          |
|-----|-----|-------------|
| -   | -   | 203 项，不逐一列出 |

接口示例

```python
import akshare as ak

stock_profit_sheet_by_report_em_df = ak.stock_profit_sheet_by_report_em(symbol="SH600519")
print(stock_profit_sheet_by_report_em_df)
```

##### 利润表-按年度

接口: stock_profit_sheet_by_yearly_em

目标地址: https://emweb.securities.eastmoney.com/PC_HSF10/NewFinanceAnalysis/Index?type=web&code=sh600519#lrb-0

描述: 东方财富-股票-财务分析-利润表-按年度

限量: 单次获取指定 symbol 的利润表-按年度数据

输入参数

| 名称     | 类型  | 描述                      |
|--------|-----|-------------------------|
| symbol | str | symbol="SH600519"; 股票代码 |

输出参数

| 名称  | 类型  | 描述          |
|-----|-----|-------------|
| -   | -   | 203 项，不逐一列出 |

接口示例

```python
import akshare as ak

stock_profit_sheet_by_yearly_em_df = ak.stock_profit_sheet_by_yearly_em(symbol="SH600519")
print(stock_profit_sheet_by_yearly_em_df)
```

##### 利润表-按单季度

接口: stock_profit_sheet_by_quarterly_em

目标地址: https://emweb.securities.eastmoney.com/PC_HSF10/NewFinanceAnalysis/Index?type=web&code=sh600519#lrb-0

描述: 东方财富-股票-财务分析-利润表-按单季度

限量: 单次获取指定 symbol 的利润表-按单季度数据

输入参数

| 名称     | 类型  | 描述                      |
|--------|-----|-------------------------|
| symbol | str | symbol="SH600519"; 股票代码 |

输出参数

| 名称  | 类型  | 描述          |
|-----|-----|-------------|
| -   | -   | 204 项，不逐一列出 |

接口示例

```python
import akshare as ak

stock_profit_sheet_by_quarterly_em_df = ak.stock_profit_sheet_by_quarterly_em(symbol="SH600519")
print(stock_profit_sheet_by_quarterly_em_df)
```

##### 现金流量表-按报告期

接口: stock_cash_flow_sheet_by_report_em

目标地址: https://emweb.securities.eastmoney.com/PC_HSF10/NewFinanceAnalysis/Index?type=web&code=sh600519#lrb-0

描述: 东方财富-股票-财务分析-现金流量表-按报告期

限量: 单次获取指定 symbol 的现金流量表-按报告期数据

输入参数

| 名称     | 类型  | 描述                      |
|--------|-----|-------------------------|
| symbol | str | symbol="SH600519"; 股票代码 |

输出参数

| 名称  | 类型  | 描述          |
|-----|-----|-------------|
| -   | -   | 252 项，不逐一列出 |

接口示例

```python
import akshare as ak

stock_cash_flow_sheet_by_report_em_df = ak.stock_cash_flow_sheet_by_report_em(symbol="SH600519")
print(stock_cash_flow_sheet_by_report_em_df)
```

##### 现金流量表-按年度

接口: stock_cash_flow_sheet_by_yearly_em

目标地址: https://emweb.securities.eastmoney.com/PC_HSF10/NewFinanceAnalysis/Index?type=web&code=sh600519#lrb-0

描述: 东方财富-股票-财务分析-现金流量表-按年度

限量: 单次获取指定 symbol 的现金流量表-按年度数据

输入参数

| 名称     | 类型  | 描述                      |
|--------|-----|-------------------------|
| symbol | str | symbol="SH600519"; 股票代码 |

输出参数

| 名称  | 类型  | 描述          |
|-----|-----|-------------|
| -   | -   | 314 项，不逐一列出 |

接口示例

```python
import akshare as ak

stock_cash_flow_sheet_by_yearly_em_df = ak.stock_cash_flow_sheet_by_yearly_em(symbol="SH600519")
print(stock_cash_flow_sheet_by_yearly_em_df)
```

##### 现金流量表-按单季度

接口: stock_cash_flow_sheet_by_quarterly_em

目标地址: https://emweb.securities.eastmoney.com/PC_HSF10/NewFinanceAnalysis/Index?type=web&code=sh600519#lrb-0

描述: 东方财富-股票-财务分析-现金流量表-按单季度

限量: 单次获取指定 symbol 的现金流量表-按单季度数据

输入参数

| 名称     | 类型  | 描述                      |
|--------|-----|-------------------------|
| symbol | str | symbol="SH600519"; 股票代码 |

输出参数

| 名称  | 类型  | 描述          |
|-----|-----|-------------|
| -   | -   | 315 项，不逐一列出 |

接口示例

```python
import akshare as ak

stock_cash_flow_sheet_by_quarterly_em_df = ak.stock_cash_flow_sheet_by_quarterly_em(symbol="SH600519")
print(stock_cash_flow_sheet_by_quarterly_em_df)
```

#### 财务报表-同花顺

##### 资产负债表

接口: stock_financial_debt_new_ths

目标地址: https://basic.10jqka.com.cn/astockpc/astockmain/index.html#/financen?code=000063

描述: 同花顺-财务指标-资产负债表；替换 stock_financial_debt_ths 接口

限量: 单次获取资产负债表所有历史数据

输入参数

| 名称        | 类型  | 描述                                          |
|-----------|-----|---------------------------------------------|
| symbol    | str | symbol="000063"; 股票代码                       |
| indicator | str | indicator="按报告期"; choice of {"按报告期", "按年度"} |

输出参数

| 名称            | 类型      | 描述 |
|---------------|---------|----|
| report_date   | object  | -  |
| report_name   | object  | -  |
| report_period | object  | -  |
| quarter_name  | object  | -  |
| metric_name   | object  | -  |
| value         | float64 | -  |
| single        | object  | -  |
| yoy           | float64 | -  |
| mom           | object  | -  |
| single_yoy    | object  | -  |

接口示例

```python
import akshare as ak

stock_financial_debt_new_ths_df = ak.stock_financial_debt_new_ths(symbol="000063", indicator="按年度")
print(stock_financial_debt_new_ths_df)
```

##### 利润表

接口: stock_financial_benefit_new_ths

目标地址: https://basic.10jqka.com.cn/astockpc/astockmain/index.html#/financen?code=000063

描述: 同花顺-财务指标-利润表；替换 stock_financial_benefit_ths 接口

限量: 单次获取利润表所有历史数据

输入参数

| 名称        | 类型  | 描述                                                                      |
|-----------|-----|-------------------------------------------------------------------------|
| symbol    | str | symbol="000063"; 股票代码                                                   |
| indicator | str | indicator="按报告期"; choice of {"按报告期", "一季度", "二季度", "三季度", "四季度", "按年度"} |

输出参数

| 名称            | 类型      | 描述 |
|---------------|---------|----|
| report_date   | object  | -  |
| report_name   | object  | -  |
| report_period | object  | -  |
| quarter_name  | object  | -  |
| metric_name   | object  | -  |
| value         | float64 | -  |
| single        | object  | -  |
| yoy           | float64 | -  |
| mom           | object  | -  |
| single_yoy    | object  | -  |

接口示例

```python
import akshare as ak

stock_financial_benefit_new_ths_df = ak.stock_financial_benefit_new_ths(symbol="000063", indicator="按报告期")
print(stock_financial_benefit_new_ths_df)
```

##### 现金流量表

接口: stock_financial_cash_new_ths

目标地址: https://basic.10jqka.com.cn/astockpc/astockmain/index.html#/financen?code=000063

描述: 同花顺-财务指标-现金流量表；替换 stock_financial_cash_ths 接口

限量: 单次获取现金流量表所有历史数据

输入参数

| 名称        | 类型  | 描述                                                                      |
|-----------|-----|-------------------------------------------------------------------------|
| symbol    | str | symbol="000063"; 股票代码                                                   |
| indicator | str | indicator="按报告期"; choice of {"按报告期", "一季度", "二季度", "三季度", "四季度", "按年度"} |

输出参数

| 名称            | 类型      | 描述 |
|---------------|---------|----|
| report_date   | object  | -  |
| report_name   | object  | -  |
| report_period | object  | -  |
| quarter_name  | object  | -  |
| metric_name   | object  | -  |
| value         | float64 | -  |
| single        | object  | -  |
| yoy           | float64 | -  |
| mom           | object  | -  |
| single_yoy    | object  | -  |

接口示例

```python
import akshare as ak

stock_financial_cash_new_ths_df = ak.stock_financial_cash_new_ths(symbol="000063", indicator="按年度")
print(stock_financial_cash_new_ths_df)
```

#### 财务报表-东财-已退市股票

##### 资产负债表-按报告期

接口: stock_balance_sheet_by_report_delisted_em

目标地址: https://emweb.securities.eastmoney.com/pc_hsf10/pages/index.html?type=web&code=SZ000013#/cwfx/zcfzb

描述: 东方财富-股票-财务分析-资产负债表-已退市股票-按报告期

限量: 单次获取指定 symbol 的资产负债表-按报告期数据

输入参数

| 名称     | 类型  | 描述                               |
|--------|-----|----------------------------------|
| symbol | str | symbol="SZ000013"; 带市场标识的已退市股票代码 |

输出参数

| 名称  | 类型  | 描述         |
|-----|-----|------------|
| -   | -   | 319项，不逐一列出 |

接口示例

```python
import akshare as ak

stock_balance_sheet_by_report_delisted_em_df = ak.stock_balance_sheet_by_report_delisted_em(symbol="SZ000013")
print(stock_balance_sheet_by_report_delisted_em_df)
```

##### 利润表-按报告期

接口: stock_profit_sheet_by_report_delisted_em

目标地址: https://emweb.securities.eastmoney.com/pc_hsf10/pages/index.html?type=web&code=SZ000013#/cwfx/lrb

描述: 东方财富-股票-财务分析-利润表-已退市股票-按报告期

限量: 单次获取指定 symbol 的利润表-按报告期数据

输入参数

| 名称     | 类型  | 描述                               |
|--------|-----|----------------------------------|
| symbol | str | symbol="SZ000013"; 带市场标识的已退市股票代码 |

输出参数

| 名称  | 类型  | 描述          |
|-----|-----|-------------|
| -   | -   | 203 项，不逐一列出 |

接口示例

```python
import akshare as ak

stock_profit_sheet_by_report_delisted_em_df = ak.stock_profit_sheet_by_report_delisted_em(symbol="SZ000013")
print(stock_profit_sheet_by_report_delisted_em_df)
```

##### 现金流量表-按报告期

接口: stock_cash_flow_sheet_by_report_delisted_em

目标地址: https://emweb.securities.eastmoney.com/pc_hsf10/pages/index.html?type=web&code=SZ000013#/cwfx/xjllb

描述: 东方财富-股票-财务分析-现金流量表-已退市股票-按报告期

限量: 单次获取指定 symbol 的现金流量表-按报告期数据

输入参数

| 名称     | 类型  | 描述                               |
|--------|-----|----------------------------------|
| symbol | str | symbol="SZ000013"; 带市场标识的已退市股票代码 |

输出参数

| 名称  | 类型  | 描述          |
|-----|-----|-------------|
| -   | -   | 252 项，不逐一列出 |

接口示例

```python
import akshare as ak

stock_cash_flow_sheet_by_report_delisted_em_df = ak.stock_cash_flow_sheet_by_report_delisted_em(symbol="SZ000013")
print(stock_cash_flow_sheet_by_report_delisted_em_df)
```

#### 港股财务报表

接口: stock_financial_hk_report_em

目标地址: https://emweb.securities.eastmoney.com/PC_HKF10/FinancialAnalysis/index?type=web&code=00700

描述: 东方财富-港股-财务报表-三大报表

限量: 单次获取指定股票、指定报告且指定报告期的数据

输入参数

| 名称        | 类型  | 描述                                                  |
|-----------|-----|-----------------------------------------------------|
| stock     | str | stock="00700"; 股票代码                                 |
| symbol    | str | symbol="现金流量表"; choice of {"资产负债表", "利润表", "现金流量表"} |
| indicator | str | indicator="年度"; choice of {"年度", "报告期"}             |

输出参数

| 名称                 | 类型      | 描述 |
|--------------------|---------|----|
| SECUCODE           | object  | -  |
| SECURITY_CODE      | object  | -  |
| SECURITY_NAME_ABBR | object  | -  |
| ORG_CODE           | object  | -  |
| REPORT_DATE        | object  | -  |
| DATE_TYPE_CODE     | object  | -  |
| FISCAL_YEAR        | object  | -  |
| STD_ITEM_CODE      | object  | -  |
| STD_ITEM_NAME      | object  | -  |
| AMOUNT             | float64 | -  |
| STD_REPORT_DATE    | object  | -  |

```python
import akshare as ak

stock_financial_hk_report_em_df = ak.stock_financial_hk_report_em(stock="00700", symbol="资产负债表", indicator="年度")
print(stock_financial_hk_report_em_df)
```

#### 美股财务报表

接口: stock_financial_us_report_em

目标地址: https://emweb.eastmoney.com/PC_USF10/pages/index.html?code=TSLA&type=web&color=w#/cwfx/zyzb

描述: 东方财富-美股-财务分析-三大报表

限量: 单次获取指定股票、指定报告且指定报告期的数据

输入参数

| 名称        | 类型  | 描述                                                    |
|-----------|-----|-------------------------------------------------------|
| stock     | str | stock="TSLA"; 股票代码, 比如 BRK.A 需修改为 BRK_A 再获取           |
| symbol    | str | symbol="资产负债表"; choice of {"资产负债表", "综合损益表", "现金流量表"} |
| indicator | str | indicator="年报"; choice of {"年报", "单季报", "累计季报"}       |

输出参数

| 名称                 | 类型      | 描述 |
|--------------------|---------|----|
| SECUCODE           | object  | -  |
| SECURITY_CODE      | object  | -  |
| SECURITY_NAME_ABBR | object  | -  |
| REPORT_DATE        | object  | -  |
| REPORT_TYPE        | object  | -  |
| REPORT             | object  | -  |
| STD_ITEM_CODE      | object  | -  |
| AMOUNT             | float64 | -  |
| ITEM_NAME          | object  | -  |


```python
import akshare as ak

stock_financial_us_report_em_df = ak.stock_financial_us_report_em(stock="TSLA", symbol="资产负债表", indicator="年报")
print(stock_financial_us_report_em_df)
```

#### 关键指标-新浪

接口: stock_financial_abstract

目标地址: https://vip.stock.finance.sina.com.cn/corp/go.php/vFD_FinanceSummary/stockid/600004.phtml

描述: 新浪财经-财务报表-关键指标

限量: 单次获取关键指标所有历史数据

输入参数

| 名称     | 类型  | 描述                    |
|--------|-----|-----------------------|
| symbol | str | symbol="600004"; 股票代码 |

输出参数

| 名称       | 类型     | 描述  |
|----------|--------|-----|
| 选项       | object | -   |
| 指标       | object | -   |
| 【具体的报告期】 | object | -   |

接口示例

```python
import akshare as ak

stock_financial_abstract_df = ak.stock_financial_abstract(symbol="600004")
print(stock_financial_abstract_df)
```

#### 关键指标-同花顺

接口: stock_financial_abstract_new_ths

目标地址: https://basic.10jqka.com.cn/new/000063/finance.html

描述: 同花顺-财务指标-重要指标；替换 stock_financial_abstract_ths 接口

限量: 单次获取指定 symbol 的所有数据

输入参数

| 名称        | 类型  | 描述                                                                      |
|-----------|-----|-------------------------------------------------------------------------|
| symbol    | str | symbol="000063"; 股票代码                                                   |
| indicator | str | indicator="按报告期"; choice of {"按报告期", "一季度", "二季度", "三季度", "四季度", "按年度"} |

输出参数

| 名称            | 类型      | 描述 |
|---------------|---------|----|
| report_date   | object  | -  |
| report_name   | object  | -  |
| report_period | object  | -  |
| quarter_name  | object  | -  |
| metric_name   | object  | -  |
| value         | float64 | -  |
| single        | object  | -  |
| yoy           | float64 | -  |
| mom           | object  | -  |
| single_yoy    | object  | -  |

接口示例

```python
import akshare as ak

stock_financial_abstract_new_ths_df = ak.stock_financial_abstract_new_ths(symbol="000063", indicator="按报告期")
print(stock_financial_abstract_new_ths_df)
```

#### 主要指标-东方财富

接口: stock_financial_analysis_indicator_em

目标地址: https://emweb.securities.eastmoney.com/pc_hsf10/pages/index.html?type=web&code=SZ301389&color=b#/cwfx

描述: 东方财富-A股-财务分析-主要指标

限量: 单次获取指定 symbol 的所有数据

输入参数

| 名称        | 类型  | 描述                                           |
|-----------|-----|----------------------------------------------|
| symbol    | str | symbol="301389.SZ"; 股票代码                     |
| indicator | str | indicator="按报告期"; choice of {"按报告期", "按单季度"} |

输出参数

| 名称                 | 类型      | 描述               |
|--------------------|---------|------------------|
| SECUCODE           | object  | 股票代码(带后缀)        |
| SECURITY_CODE      | object  | 股票代码             |
| SECURITY_NAME_ABBR | object  | 股票名称             |
| REPORT_DATE        | object  | 报告日期             |
| REPORT_TYPE        | object  | 报告类型             |
| REPORT_DATE_NAME   | object  | 报告日期名称           |
| EPSJB              | float64 | 基本每股收益(元)        |
| EPSKCJB            | float64 | 扣非每股收益(元)        |
| EPSXS              | float64 | 稀释每股收益(元)        |
| BPS                | float64 | 每股净资产(元)         |
| MGZBGJ             | float64 | 每股公积金(元)         |
| MGWFPLR            | float64 | 每股未分配利润(元)       |
| MGJYXJJE           | float64 | 每股经营现金流(元)       |
| TOTALOPERATEREVE   | float64 | 营业总收入(元)         |
| MLR                | float64 | 毛利润(元)           |
| PARENTNETPROFIT    | float64 | 归属净利润(元)         |
| KCFJCXSYJLR        | float64 | 扣非净利润(元)         |
| TOTALOPERATEREVETZ | float64 | 营业总收入同比增长(%)     |
| PARENTNETPROFITTZ  | float64 | 归属净利润同比增长(%)     |
| KCFJCXSYJLRTZ      | float64 | 扣非净利润同比增长(%)     |
| YYZSRGDHBZC        | float64 | 营业总收入滚动环比增长(%)   |
| NETPROFITRPHBZC    | float64 | 归属净利润滚动环比增长(%)   |
| KFJLRGDHBZC        | float64 | 扣非净利润滚动环比增长(%)   |
| ROEJQ              | float64 | 净资产收益率(加权)(%)    |
| ROEKCJQ            | float64 | 净资产收益率(扣非/加权)(%) |
| ZZCJLL             | float64 | 总资产收益率(加权)(%)    |
| XSJLL              | float64 | 净利率(%)           |
| XSMLL              | float64 | 毛利率(%)           |
| YSZKYYSR           | float64 | 预收账款/营业收入        |
| XSJXLYYSR          | float64 | 销售净现金流/营业收入      |
| JYXJLYYSR          | float64 | 经营净现金流/营业收入      |
| TAXRATE            | float64 | 实际税率(%)          |
| LD                 | float64 | 流动比率             |
| SD                 | float64 | 速动比率             |
| XJLLB              | float64 | 现金流量比率           |
| ZCFZL              | float64 | 资产负债率(%)         |
| QYCS               | float64 | 权益系数             |
| CQBL               | float64 | 产权比率             |
| ZZCZZTS            | float64 | 总资产周转天数(天)       |
| CHZZTS             | float64 | 存货周转天数(天)        |
| YSZKZZTS           | float64 | 应收账款周转天数(天)      |
| TOAZZL             | float64 | 总资产周转率(次)        |
| CHZZL              | float64 | 存货周转率(次)         |
| YSZKZZL            | float64 | 应收账款周转率(次)       |
| ...                | ...     | ...              |

接口示例

```python
import akshare as ak

stock_financial_analysis_indicator_em_df = ak.stock_financial_analysis_indicator_em(symbol="301389.SZ", indicator="按报告期")
print(stock_financial_analysis_indicator_em_df)
```

#### 财务指标

接口: stock_financial_analysis_indicator

目标地址: https://money.finance.sina.com.cn/corp/go.php/vFD_FinancialGuideLine/stockid/600004/ctrl/2019/displaytype/4.phtml

描述: 新浪财经-财务分析-财务指标

限量: 单次获取指定 symbol 和 start_year 的所有财务指标历史数据

输入参数

| 名称         | 类型  | 描述                         |
|------------|-----|----------------------------|
| symbol     | str | symbol="600004"; 股票代码      |
| start_year | str | start_year="2020"; 开始查询的时间 |

输出参数

| 名称                | 类型      | 描述 |
|-------------------|---------|----|
| 日期                | object  | -  |
| 摊薄每股收益(元)         | float64 | -  |
| 加权每股收益(元)         | float64 | -  |
| 每股收益_调整后(元)       | float64 | -  |
| 扣除非经常性损益后的每股收益(元) | float64 | -  |
| 每股净资产_调整前(元)      | float64 | -  |
| 每股净资产_调整后(元)      | float64 | -  |
| 每股经营性现金流(元)       | float64 | -  |
| 每股资本公积金(元)        | float64 | -  |
| 每股未分配利润(元)        | float64 | -  |
| 调整后的每股净资产(元)      | float64 | -  |
| 总资产利润率(%)         | float64 | -  |
| 主营业务利润率(%)        | float64 | -  |
| 总资产净利润率(%)        | float64 | -  |
| 成本费用利润率(%)        | float64 | -  |
| 营业利润率(%)          | float64 | -  |
| 主营业务成本率(%)        | float64 | -  |
| 销售净利率(%)          | float64 | -  |
| 股本报酬率(%)          | float64 | -  |
| 净资产报酬率(%)         | float64 | -  |
| 资产报酬率(%)          | float64 | -  |
| 销售毛利率(%)          | float64 | -  |
| 三项费用比重            | float64 | -  |
| 非主营比重             | float64 | -  |
| 主营利润比重            | float64 | -  |
| 股息发放率(%)          | float64 | -  |
| 投资收益率(%)          | float64 | -  |
| 主营业务利润(元)         | float64 | -  |
| 净资产收益率(%)         | float64 | -  |
| 加权净资产收益率(%)       | float64 | -  |
| 扣除非经常性损益后的净利润(元)  | float64 | -  |
| 主营业务收入增长率(%)      | float64 | -  |
| 净利润增长率(%)         | float64 | -  |
| 净资产增长率(%)         | float64 | -  |
| 总资产增长率(%)         | float64 | -  |
| 应收账款周转率(次)        | float64 | -  |
| 应收账款周转天数(天)       | float64 | -  |
| 存货周转天数(天)         | float64 | -  |
| 存货周转率(次)          | float64 | -  |
| 固定资产周转率(次)        | float64 | -  |
| 总资产周转率(次)         | float64 | -  |
| 总资产周转天数(天)        | float64 | -  |
| 流动资产周转率(次)        | float64 | -  |
| 流动资产周转天数(天)       | float64 | -  |
| 股东权益周转率(次)        | float64 | -  |
| 流动比率              | float64 | -  |
| 速动比率              | float64 | -  |
| 现金比率(%)           | float64 | -  |
| 利息支付倍数            | float64 | -  |
| 长期债务与营运资金比率(%)    | float64 | -  |
| 股东权益比率(%)         | float64 | -  |
| 长期负债比率(%)         | float64 | -  |
| 股东权益与固定资产比率(%)    | float64 | -  |
| 负债与所有者权益比率(%)     | float64 | -  |
| 长期资产与长期资金比率(%)    | float64 | -  |
| 资本化比率(%)          | float64 | -  |
| 固定资产净值率(%)        | float64 | -  |
| 资本固定化比率(%)        | float64 | -  |
| 产权比率(%)           | float64 | -  |
| 清算价值比率(%)         | float64 | -  |
| 固定资产比重(%)         | float64 | -  |
| 资产负债率(%)          | float64 | -  |
| 总资产(元)            | float64 | -  |
| 经营现金净流量对销售收入比率(%) | float64 | -  |
| 资产的经营现金流量回报率(%)   | float64 | -  |
| 经营现金净流量与净利润的比率(%) | float64 | -  |
| 经营现金净流量对负债比率(%)   | float64 | -  |
| 现金流量比率(%)         | float64 | -  |
| 短期股票投资(元)         | float64 | -  |
| 短期债券投资(元)         | float64 | -  |
| 短期其它经营性投资(元)      | float64 | -  |
| 长期股票投资(元)         | float64 | -  |
| 长期债券投资(元)         | float64 | -  |
| 长期其它经营性投资(元)      | float64 | -  |
| 1年以内应收帐款(元)       | float64 | -  |
| 1-2年以内应收帐款(元)     | float64 | -  |
| 2-3年以内应收帐款(元)     | float64 | -  |
| 3年以内应收帐款(元)       | float64 | -  |
| 1年以内预付货款(元)       | float64 | -  |
| 1-2年以内预付货款(元)     | float64 | -  |
| 2-3年以内预付货款(元)     | float64 | -  |
| 3年以内预付货款(元)       | float64 | -  |
| 1年以内其它应收款(元)      | float64 | -  |
| 1-2年以内其它应收款(元)    | float64 | -  |
| 2-3年以内其它应收款(元)    | float64 | -  |
| 3年以内其它应收款(元)      | float64 | -  |

接口示例

```python
import akshare as ak

stock_financial_analysis_indicator_df = ak.stock_financial_analysis_indicator(symbol="600004", start_year="2020")
print(stock_financial_analysis_indicator_df)
```

#### 港股财务指标

接口: stock_financial_hk_analysis_indicator_em

目标地址: https://emweb.securities.eastmoney.com/PC_HKF10/NewFinancialAnalysis/index?type=web&code=00700

描述: 东方财富-港股-财务分析-主要指标

限量: 单次获取财务指标所有历史数据

输入参数

| 名称        | 类型  | 描述                                      |
|-----------|-----|-----------------------------------------|
| symbol    | str | symbol="00700"; 股票代码                    |
| indicator | str | indicator="年度"; choice of {"年度", "报告期"} |

输出参数

| 名称                  | 类型      | 描述             |
|---------------------|---------|----------------|
| SECUCODE            | object  | 股票代码(带HK后缀)    |
| SECURITY_CODE       | object  | 股票代码(不带HK后缀)   |
| SECURITY_NAME_ABBR  | object  | 股票名称           |
| ORG_CODE            | object  | ORG_CODE       |
| REPORT_DATE         | object  | 报告日期           |
| DATE_TYPE_CODE      | object  | 报告日期类型         |
| PER_NETCASH_OPERATE | float64 | 每股经营现金流(元)     |
| PER_OI              | float64 | 每股营业收入(元)      |
| BPS                 | float64 | 每股净资产(元)       |
| BASIC_EPS           | float64 | 基本每股收益(元)      |
| DILUTED_EPS         | float64 | 稀释每股收益(元)      |
| OPERATE_INCOME      | int64   | 营业总收入(元)       |
| OPERATE_INCOME_YOY  | float64 | 营业总收入同比增长(%)   |
| GROSS_PROFIT        | int64   | 毛利润(元)         |
| GROSS_PROFIT_YOY    | float64 | 毛利润同比增长(%)     |
| HOLDER_PROFIT       | int64   | 归母净利润(元)       |
| HOLDER_PROFIT_YOY   | float64 | 归母净利润同比增长(%)   |
| GROSS_PROFIT_RATIO  | float64 | 毛利率(%)         |
| EPS_TTM             | float64 | TTM每股收益(元)     |
| OPERATE_INCOME_QOQ  | float64 | 营业总收入滚动环比增长(%) |
| NET_PROFIT_RATIO    | float64 | 净利率(%)         |
| ROE_AVG             | float64 | 平均净资产收益率(%)    |
| GROSS_PROFIT_QOQ    | float64 | 毛利润滚动环比增长(%)   |
| ROA                 | float64 | 总资产净利率(%)      |
| HOLDER_PROFIT_QOQ   | float64 | 归母净利润滚动环比增长(%) |
| ROE_YEARLY          | float64 | 年化净资产收益率(%)    |
| ROIC_YEARLY         | float64 | 年化投资回报率(%)     |
| TAX_EBT             | float64 | 所得税/利润总额(%)    |
| OCF_SALES           | float64 | 经营现金流/营业收入(%)  |
| DEBT_ASSET_RATIO    | float64 | 资产负债率(%)       |
| CURRENT_RATIO       | float64 | 流动比率(倍)        |
| CURRENTDEBT_DEBT    | float64 | 流动负债/总负债(%)    |
| START_DATE          | object  | START_DATE     |
| FISCAL_YEAR         | object  | 年结日            |
| CURRENCY            | object  | CURRENCY       |
| IS_CNY_CODE         | int64   | IS_CNY_CODE    |

接口示例

```python
import akshare as ak

stock_financial_hk_analysis_indicator_em_df = ak.stock_financial_hk_analysis_indicator_em(symbol="00700", indicator="年度")
print(stock_financial_hk_analysis_indicator_em_df)
```

#### 美股财务指标

接口: stock_financial_us_analysis_indicator_em

目标地址: https://emweb.eastmoney.com/PC_USF10/pages/index.html?code=TSLA&type=web&color=w#/cwfx/zyzb

描述: 东方财富-美股-财务分析-主要指标

限量: 单次获取指定股票的所有历史数据

输入参数

| 名称        | 类型  | 描述                                              |
|-----------|-----|-------------------------------------------------|
| symbol    | str | symbol="TSLA"; 股票代码                             |
| indicator | str | indicator="年报"; choice of {"年报", "单季报", "累计季报"} |

输出参数

| 名称                          | 类型      | 描述 |
|-----------------------------|---------|----|
| SECUCODE                    | object  | -  |
| SECURITY_CODE               | object  | -  |
| SECURITY_NAME_ABBR          | object  | -  |
| ORG_CODE                    | object  | -  |
| SECURITY_INNER_CODE         | object  | -  |
| ACCOUNTING_STANDARDS        | object  | -  |
| NOTICE_DATE                 | object  | -  |
| START_DATE                  | object  | -  |
| REPORT_DATE                 | object  | -  |
| FINANCIAL_DATE              | object  | -  |
| STD_REPORT_DATE             | object  | -  |
| CURRENCY                    | object  | -  |
| DATE_TYPE                   | object  | -  |
| DATE_TYPE_CODE              | object  | -  |
| REPORT_TYPE                 | object  | -  |
| REPORT_DATA_TYPE            | object  | -  |
| ORGTYPE                     | object  | -  |
| OPERATE_INCOME              | float64 | -  |
| OPERATE_INCOME_YOY          | float64 | -  |
| GROSS_PROFIT                | float64 | -  |
| GROSS_PROFIT_YOY            | float64 | -  |
| PARENT_HOLDER_NETPROFIT     | int64   | -  |
| PARENT_HOLDER_NETPROFIT_YOY | float64 | -  |
| BASIC_EPS                   | float64 | -  |
| DILUTED_EPS                 | float64 | -  |
| GROSS_PROFIT_RATIO          | float64 | -  |
| NET_PROFIT_RATIO            | float64 | -  |
| ACCOUNTS_RECE_TR            | float64 | -  |
| INVENTORY_TR                | float64 | -  |
| TOTAL_ASSETS_TR             | float64 | -  |
| ACCOUNTS_RECE_TDAYS         | float64 | -  |
| INVENTORY_TDAYS             | float64 | -  |
| TOTAL_ASSETS_TDAYS          | float64 | -  |
| ROE_AVG                     | float64 | -  |
| ROA                         | float64 | -  |
| CURRENT_RATIO               | float64 | -  |
| SPEED_RATIO                 | float64 | -  |
| OCF_LIQDEBT                 | float64 | -  |
| DEBT_ASSET_RATIO            | float64 | -  |
| EQUITY_RATIO                | float64 | -  |
| BASIC_EPS_YOY               | float64 | -  |
| GROSS_PROFIT_RATIO_YOY      | float64 | -  |
| NET_PROFIT_RATIO_YOY        | float64 | -  |
| ROE_AVG_YOY                 | float64 | -  |
| ROA_YOY                     | float64 | -  |
| DEBT_ASSET_RATIO_YOY        | float64 | -  |
| CURRENT_RATIO_YOY           | float64 | -  |
| SPEED_RATIO_YOY             | float64 | -  |

接口示例

```python
import akshare as ak

stock_financial_us_analysis_indicator_em_df = ak.stock_financial_us_analysis_indicator_em(symbol="TSLA", indicator="年报")
print(stock_financial_us_analysis_indicator_em_df)
```

#### 历史分红

接口: stock_history_dividend

目标地址: http://vip.stock.finance.sina.com.cn/q/go.php/vInvestConsult/kind/lsfh/index.phtml

描述: 新浪财经-发行与分配-历史分红

限量: 单次获取所有股票的历史分红数据

输入参数

| 名称  | 类型  | 描述  |
|-----|-----|-----|
| -   | -   | -   |

输出参数

| 名称   | 类型      | 描述      |
|------|---------|---------|
| 代码   | object  | -       |
| 名称   | object  | -       |
| 上市日期 | object  | -       |
| 累计股息 | float64 | 注意单位: % |
| 年均股息 | float64 | 注意单位: % |
| 分红次数 | float64 | -       |
| 融资总额 | float64 | 注意单位: 亿 |
| 融资次数 | float64 | -       |

接口示例

```python
import akshare as ak

stock_history_dividend_df = ak.stock_history_dividend()
print(stock_history_dividend_df)
```

#### 十大流通股东(个股)

接口: stock_gdfx_free_top_10_em

目标地址: https://emweb.securities.eastmoney.com/PC_HSF10/ShareholderResearch/Index?type=web&code=SH688686#sdltgd-0

描述: 东方财富网-个股-十大流通股东

限量: 单次返回指定 symbol 和 date 的所有数据

输入参数

| 名称     | 类型  | 描述                            |
|--------|-----|-------------------------------|
| symbol | str | symbol="sh688686"; 带市场标识的股票代码 |
| date   | str | date="20240930"; 财报发布季度最后日    |

输出参数

| 名称         | 类型      | 描述      |
|------------|---------|---------|
| 名次         | int64   | -       |
| 股东名称       | object  | -       |
| 股东性质       | object  | -       |
| 股份类型       | object  | -       |
| 持股数        | int64   | 注意单位: 股 |
| 占总流通股本持股比例 | float64 | 注意单位: % |
| 增减         | object  | 注意单位: 股 |
| 变动比率       | float64 | 注意单位: % |

接口示例

```python
import akshare as ak

stock_gdfx_free_top_10_em_df = ak.stock_gdfx_free_top_10_em(symbol="sh688686", date="20240930")
print(stock_gdfx_free_top_10_em_df)
```

#### 十大股东(个股)

接口: stock_gdfx_top_10_em

目标地址: https://emweb.securities.eastmoney.com/PC_HSF10/ShareholderResearch/Index?type=web&code=SH688686#sdltgd-0

描述: 东方财富网-个股-十大股东

限量: 单次返回指定 symbol 和 date 的所有数据

输入参数

| 名称     | 类型  | 描述                            |
|--------|-----|-------------------------------|
| symbol | str | symbol="sh688686"; 带市场标识的股票代码 |
| date   | str | date="20210630"; 财报发布季度最后日    |

输出参数

| 名称       | 类型      | 描述      |
|----------|---------|---------|
| 名次       | int64   | -       |
| 股东名称     | object  | -       |
| 股份类型     | object  | -       |
| 持股数      | int64   | 注意单位: 股 |
| 占总股本持股比例 | float64 | 注意单位: % |
| 增减       | object  | 注意单位: 股 |
| 变动比率     | float64 | 注意单位: % |

接口示例

```python
import akshare as ak

stock_gdfx_top_10_em_df = ak.stock_gdfx_top_10_em(symbol="sh688686", date="20210630")
print(stock_gdfx_top_10_em_df)
```

#### 股东持股变动统计-十大流通股东

接口: stock_gdfx_free_holding_change_em

目标地址: https://data.eastmoney.com/gdfx/HoldingAnalyse.html

描述: 东方财富网-数据中心-股东分析-股东持股变动统计-十大流通股东

限量: 单次返回指定 date 的所有数据

输入参数

| 名称   | 类型  | 描述                         |
|------|-----|----------------------------|
| date | str | date="20210930"; 财报发布季度最后日 |

输出参数

| 名称           | 类型      | 描述      |
|--------------|---------|---------|
| 序号           | int64   | -       |
| 股东名称         | object  | -       |
| 股东类型         | object  | -       |
| 期末持股只数统计-总持有 | float64 | -       |
| 期末持股只数统计-新进  | float64 | -       |
| 期末持股只数统计-增加  | float64 | -       |
| 期末持股只数统计-不变  | float64 | -       |
| 期末持股只数统计-减少  | float64 | -       |
| 流通市值统计       | float64 | 注意单位: 元 |
| 持有个股         | object  | -       |

接口示例

```python
import akshare as ak

stock_gdfx_free_holding_change_em_df = ak.stock_gdfx_free_holding_change_em(date="20210930")
print(stock_gdfx_free_holding_change_em_df)
```

#### 股东持股变动统计-十大股东

接口: stock_gdfx_holding_change_em

目标地址: https://data.eastmoney.com/gdfx/HoldingAnalyse.html

描述: 东方财富网-数据中心-股东分析-股东持股变动统计-十大股东

限量: 单次返回指定 date 的所有数据

输入参数

| 名称   | 类型  | 描述                         |
|------|-----|----------------------------|
| date | str | date="20210930"; 财报发布季度最后日 |

输出参数

| 名称           | 类型      | 描述      |
|--------------|---------|---------|
| 序号           | int64   | -       |
| 股东名称         | object  | -       |
| 股东类型         | object  | -       |
| 期末持股只数统计-总持有 | float64 | -       |
| 期末持股只数统计-新进  | float64 | -       |
| 期末持股只数统计-增加  | float64 | -       |
| 期末持股只数统计-不变  | float64 | -       |
| 期末持股只数统计-减少  | float64 | -       |
| 流通市值统计       | float64 | 注意单位: 元 |
| 持有个股         | object  | -       |

接口示例

```python
import akshare as ak

stock_gdfx_holding_change_em_df = ak.stock_gdfx_holding_change_em(date="20210930")
print(stock_gdfx_holding_change_em_df)
```

#### 高管持股变动统计

接口: stock_management_change_ths

目标地址: https://basic.10jqka.com.cn/new/688981/event.html

描述: 同花顺-公司大事-高管持股变动

限量: 单次返回所有数据

输入参数

| 名称     | 类型  | 描述                    |
|--------|-----|-----------------------|
| symbol | str | symbol="688981"; 股票代码 |

输出参数

| 名称      | 类型     | 描述      |
|---------|--------|---------|
| 公告日期    | object | -       |
| 变动人     | object | -       |
| 与公司高管关系 | object | -       |
| 变动数量    | object | 注意单位: 股 |
| 交易均价    | object | 注意单位: 元 |
| 剩余股数    | object | 注意单位: 股 |
| 变动途径    | object | -       |

接口示例

```python
import akshare as ak

stock_management_change_ths_df = ak.stock_management_change_ths(symbol="688981")
print(stock_management_change_ths_df)
```

#### 股东持股变动统计

接口: stock_shareholder_change_ths

目标地址: https://basic.10jqka.com.cn/new/688981/event.html

描述: 同花顺-公司大事-股东持股变动

限量: 单次返回所有数据

输入参数

| 名称     | 类型  | 描述                    |
|--------|-----|-----------------------|
| symbol | str | symbol="688981"; 股票代码 |

输出参数

| 名称     | 类型     | 描述      |
|--------|--------|---------|
| 公告日期   | object | -       |
| 变动股东   | object | -       |
| 变动数量   | object | 注意单位: 股 |
| 交易均价   | object | 注意单位: 元 |
| 剩余股份总数 | object | 注意单位: 股 |
| 变动期间   | object | -       |
| 变动途径   | object | -       |

接口示例

```python
import akshare as ak

stock_shareholder_change_ths_df = ak.stock_shareholder_change_ths(symbol="688981")
print(stock_shareholder_change_ths_df)
```

#### 股东持股分析-十大流通股东

接口: stock_gdfx_free_holding_analyse_em

目标地址: https://data.eastmoney.com/gdfx/HoldingAnalyse.html

描述: 东方财富网-数据中心-股东分析-股东持股分析-十大流通股东

限量: 单次获取返回所有数据

输入参数

| 名称   | 类型  | 描述                         |
|------|-----|----------------------------|
| date | str | date="20230930"; 财报发布季度最后日 |

输出参数

| 名称             | 类型      | 描述      |
|----------------|---------|---------|
| 序号             | int64   | -       |
| 股东名称           | object  | -       |
| 股东类型           | object  | -       |
| 股票代码           | object  | -       |
| 股票简称           | object  | -       |
| 报告期            | object  | -       |
| 期末持股-数量        | float64 | 注意单位: 股 |
| 期末持股-数量变化      | float64 | 注意单位: 股 |
| 期末持股-数量变化比例    | float64 | 注意单位: % |
| 期末持股-持股变动      | float64 | -       |
| 期末持股-流通市值      | float64 | 注意单位: 元 |
| 公告日            | object  | -       |
| 公告日后涨跌幅-10个交易日 | float64 | 注意单位: % |
| 公告日后涨跌幅-30个交易日 | float64 | 注意单位: % |
| 公告日后涨跌幅-60个交易日 | float64 | 注意单位: % |

接口示例

```python
import akshare as ak

stock_gdfx_free_holding_analyse_em_df = ak.stock_gdfx_free_holding_analyse_em(date="20230930")
print(stock_gdfx_free_holding_analyse_em_df)
```

#### 股东持股分析-十大股东

接口: stock_gdfx_holding_analyse_em

目标地址: https://data.eastmoney.com/gdfx/HoldingAnalyse.html

描述: 东方财富网-数据中心-股东分析-股东持股分析-十大股东

限量: 单次获取返回所有数据

输入参数

| 名称   | 类型  | 描述                         |
|------|-----|----------------------------|
| date | str | date="20210930"; 财报发布季度最后日 |

输出参数

| 名称             | 类型      | 描述      |
|----------------|---------|---------|
| 序号             | int64   | -       |
| 股东名称           | object  | -       |
| 股东类型           | object  | -       |
| 股票代码           | object  | -       |
| 股票简称           | object  | -       |
| 报告期            | object  | -       |
| 期末持股-数量        | float64 | 注意单位: 股 |
| 期末持股-数量变化      | float64 | 注意单位: 股 |
| 期末持股-数量变化比例    | float64 | 注意单位: % |
| 期末持股-持股变动      | float64 | -       |
| 期末持股-流通市值      | float64 | 注意单位: 元 |
| 公告日            | object  | -       |
| 公告日后涨跌幅-10个交易日 | float64 | 注意单位: % |
| 公告日后涨跌幅-30个交易日 | float64 | 注意单位: % |
| 公告日后涨跌幅-60个交易日 | float64 | 注意单位: % |

接口示例

```python
import akshare as ak

stock_gdfx_holding_analyse_em_df = ak.stock_gdfx_holding_analyse_em(date="20210930")
print(stock_gdfx_holding_analyse_em_df)
```

#### 股东持股明细-十大流通股东

接口: stock_gdfx_free_holding_detail_em

目标地址: https://data.eastmoney.com/gdfx/HoldingAnalyse.html

描述: 东方财富网-数据中心-股东分析-股东持股明细-十大流通股东

限量: 单次返回指定 date 的所有数据

输入参数

| 名称   | 类型  | 描述                         |
|------|-----|----------------------------|
| date | str | date="20210930"; 财报发布季度最后日 |

输出参数

| 名称           | 类型      | 描述      |
|--------------|---------|---------|
| 序号           | int64   | -       |
| 股东名称         | object  | -       |
| 股东类型         | object  | -       |
| 股票代码         | object  | -       |
| 股票简称         | object  | -       |
| 报告期          | object  | -       |
| 期末持股-数量      | float64 | 注意单位: 股 |
| 期末持股-数量变化    | float64 | 注意单位: 股 |
| 期末持股-数量变化比例  | float64 | 注意单位: % |
| 期末持股-持股变动    | float64 | -       |
| 期末持股-流通市值    | float64 | 注意单位: 元 |
| 公告日          | object  | -       |

接口示例

```python
import akshare as ak

stock_gdfx_free_holding_detail_em_df = ak.stock_gdfx_free_holding_detail_em(date="20210930")
print(stock_gdfx_free_holding_detail_em_df)
```

#### 股东持股明细-十大股东

接口: stock_gdfx_holding_detail_em

目标地址: https://data.eastmoney.com/gdfx/HoldingAnalyse.html

描述: 东方财富网-数据中心-股东分析-股东持股明细-十大股东

限量: 单次返回指定参数的所有数据

输入参数

| 名称        | 类型  | 描述                                                                     |
|-----------|-----|------------------------------------------------------------------------|
| date      | str | date="20230331"; 财报发布季度最后日                                             |
| indicator | str | indicator="个人"; 股东类型; choice of {"个人", "基金", "QFII", "社保", "券商", "信托"} |
| symbol    | str | symbol="新进"; 持股变动; choice of {"新进", "增加", "不变", "减少"}                  |

输出参数

| 名称           | 类型      | 描述      |
|--------------|---------|---------|
| 序号           | int64   | -       |
| 股东名称         | object  | -       |
| 股东排名         | object  | -       |
| 股票代码         | object  | -       |
| 股票简称         | object  | -       |
| 报告期          | object  | -       |
| 期末持股-数量      | float64 | 注意单位: 股 |
| 期末持股-数量变化    | float64 | 注意单位: 股 |
| 期末持股-数量变化比例  | float64 | 注意单位: % |
| 期末持股-持股变动    | float64 | -       |
| 期末持股-流通市值    | float64 | 注意单位: 元 |
| 公告日          | object  | -       |
| 股东类型         | object  | -       |

接口示例

```python
import akshare as ak

stock_gdfx_holding_detail_em_df = ak.stock_gdfx_holding_detail_em(date="20230331", indicator="个人", symbol="新进")
print(stock_gdfx_holding_detail_em_df)
```

#### 股东持股统计-十大流通股东

接口: stock_gdfx_free_holding_statistics_em

目标地址: https://data.eastmoney.com/gdfx/HoldingAnalyse.html

描述: 东方财富网-数据中心-股东分析-股东持股统计-十大股东

限量: 单次返回指定 date 的所有数据

输入参数

| 名称   | 类型  | 描述                         |
|------|-----|----------------------------|
| date | str | date="20210930"; 财报发布季度最后日 |

输出参数

| 名称                   | 类型      | 描述  |
|----------------------|---------|-----|
| 序号                   | int64   | -   |
| 股东名称                 | object  | -   |
| 股东类型                 | object  | -   |
| 统计次数                 | int64   | -   |
| 公告日后涨幅统计-10个交易日-平均涨幅 | float64 | -   |
| 公告日后涨幅统计-10个交易日-最大涨幅 | float64 | -   |
| 公告日后涨幅统计-10个交易日-最小涨幅 | float64 | -   |
| 公告日后涨幅统计-30个交易日-平均涨幅 | float64 | -   |
| 公告日后涨幅统计-30个交易日-最大涨幅 | float64 | -   |
| 公告日后涨幅统计-30个交易日-最小涨幅 | float64 | -   |
| 公告日后涨幅统计-60个交易日-平均涨幅 | float64 | -   |
| 公告日后涨幅统计-60个交易日-最大涨幅 | float64 | -   |
| 公告日后涨幅统计-60个交易日-最小涨幅 | float64 | -   |
| 持有个股                 | object  | -   |

接口示例

```python
import akshare as ak

stock_gdfx_free_holding_statistics_em_df = ak.stock_gdfx_free_holding_statistics_em(date="20210930")
print(stock_gdfx_free_holding_statistics_em_df)
```

#### 股东持股统计-十大股东

接口: stock_gdfx_holding_statistics_em

目标地址: https://data.eastmoney.com/gdfx/HoldingAnalyse.html

描述: 东方财富网-数据中心-股东分析-股东持股统计-十大股东

限量: 单次返回指定 date 的所有数据

输入参数

| 名称   | 类型  | 描述                         |
|------|-----|----------------------------|
| date | str | date="20210930"; 财报发布季度最后日 |

输出参数

| 名称                   | 类型      | 描述  |
|----------------------|---------|-----|
| 序号                   | int64   | -   |
| 股东名称                 | object  | -   |
| 股东类型                 | object  | -   |
| 统计次数                 | int64   | -   |
| 公告日后涨幅统计-10个交易日-平均涨幅 | float64 | -   |
| 公告日后涨幅统计-10个交易日-最大涨幅 | float64 | -   |
| 公告日后涨幅统计-10个交易日-最小涨幅 | float64 | -   |
| 公告日后涨幅统计-30个交易日-平均涨幅 | float64 | -   |
| 公告日后涨幅统计-30个交易日-最大涨幅 | float64 | -   |
| 公告日后涨幅统计-30个交易日-最小涨幅 | float64 | -   |
| 公告日后涨幅统计-60个交易日-平均涨幅 | float64 | -   |
| 公告日后涨幅统计-60个交易日-最大涨幅 | float64 | -   |
| 公告日后涨幅统计-60个交易日-最小涨幅 | float64 | -   |
| 持有个股                 | object  | -   |

接口示例

```python
import akshare as ak

stock_gdfx_holding_statistics_em_df = ak.stock_gdfx_holding_statistics_em(date="20210930")
print(stock_gdfx_holding_statistics_em_df)
```

#### 股东协同-十大流通股东

接口: stock_gdfx_free_holding_teamwork_em

目标地址: https://data.eastmoney.com/gdfx/HoldingAnalyse.html

描述: 东方财富网-数据中心-股东分析-股东协同-十大流通股东

限量: 单次返回所有数据

输入参数

| 名称     | 类型  | 描述                                                                  |
|--------|-----|---------------------------------------------------------------------|
| symbol | str | symbol="社保"; choice of {"全部", "个人", "基金", "QFII", "社保", "券商", "信托"} |

输出参数

| 名称     | 类型     | 描述  |
|--------|--------|-----|
| 序号     | int64  | -   |
| 股东名称   | object | -   |
| 股东类型   | object | -   |
| 协同股东名称 | object | -   |
| 协同股东类型 | object | -   |
| 协同次数   | int64  | -   |
| 个股详情   | object | -   |

接口示例

```python
import akshare as ak

stock_gdfx_free_holding_teamwork_em_df = ak.stock_gdfx_free_holding_teamwork_em(symbol="社保")
print(stock_gdfx_free_holding_teamwork_em_df)
```

#### 股东协同-十大股东

接口: stock_gdfx_holding_teamwork_em

目标地址: https://data.eastmoney.com/gdfx/HoldingAnalyse.html

描述: 东方财富网-数据中心-股东分析-股东协同-十大股东

限量: 单次返回所有数据

输入参数

| 名称     | 类型  | 描述                                                                  |
|--------|-----|---------------------------------------------------------------------|
| symbol | str | symbol="社保"; choice of {"全部", "个人", "基金", "QFII", "社保", "券商", "信托"} |

输出参数

| 名称     | 类型     | 描述  |
|--------|--------|-----|
| 序号     | int64  | -   |
| 股东名称   | object | -   |
| 股东类型   | object | -   |
| 协同股东名称 | object | -   |
| 协同股东类型 | object | -   |
| 协同次数   | int64  | -   |
| 个股详情   | object | -   |

接口示例

```python
import akshare as ak

stock_gdfx_holding_teamwork_em_df = ak.stock_gdfx_holding_teamwork_em(symbol="社保")
print(stock_gdfx_holding_teamwork_em_df)
```

#### 股东户数

接口: stock_zh_a_gdhs

目标地址: http://data.eastmoney.com/gdhs/

描述: 东方财富网-数据中心-特色数据-股东户数数据

限量: 单次获取返回所有数据

输入参数

| 名称     | 类型  | 描述                                                                     |
|--------|-----|------------------------------------------------------------------------|
| symbol | str | symbol="20230930"; choice of {"最新", 每个季度末}, 其中 每个季度末需要写成 `20230930` 格式 |

输出参数

| 名称           | 类型      | 描述      |
|--------------|---------|---------|
| 代码           | object  | -       |
| 名称           | object  | -       |
| 最新价          | float64 | 注意单位: 元 |
| 涨跌幅          | float64 | 注意单位: % |
| 股东户数-本次      | int64   | -       |
| 股东户数-上次      | int64   | -       |
| 股东户数-增减      | int64   | -       |
| 股东户数-增减比例    | float64 | 注意单位: % |
| 区间涨跌幅        | float64 | 注意单位: % |
| 股东户数统计截止日-本次 | object  | -       |
| 股东户数统计截止日-上次 | object  | -       |
| 户均持股市值       | float64 | -       |
| 户均持股数量       | float64 | -       |
| 总市值          | float64 | -       |
| 总股本          | float64 | -       |
| 公告日期         | object  | -       |

接口示例

```python
import akshare as ak

stock_zh_a_gdhs_df = ak.stock_zh_a_gdhs(symbol="20230930")
print(stock_zh_a_gdhs_df)
```

#### 股东户数详情

接口: stock_zh_a_gdhs_detail_em

目标地址: https://data.eastmoney.com/gdhs/detail/000002.html

描述: 东方财富网-数据中心-特色数据-股东户数详情

限量: 单次获取指定 symbol 的所有数据

输入参数

| 名称     | 类型  | 描述                    |
|--------|-----|-----------------------|
| symbol | str | symbol="000001"; 股票代码 |

输出参数

| 名称        | 类型      | 描述      |
|-----------|---------|---------|
| 股东户数统计截止日 | object  | -       |
| 区间涨跌幅     | float64 | 注意单位: % |
| 股东户数-本次   | int64   | -       |
| 股东户数-上次   | int64   | -       |
| 股东户数-增减   | int64   | -       |
| 股东户数-增减比例 | float64 | 注意单位: % |
| 户均持股市值    | float64 | -       |
| 户均持股数量    | float64 | -       |
| 总市值       | float64 | -       |
| 总股本       | int64   | -       |
| 股本变动      | int64   | -       |
| 股本变动原因    | object  | -       |
| 股东户数公告日期  | object  | -       |
| 代码        | object  | -       |
| 名称        | object  | -       |

接口示例

```python
import akshare as ak

stock_zh_a_gdhs_detail_em_df = ak.stock_zh_a_gdhs_detail_em(symbol="000001")
print(stock_zh_a_gdhs_detail_em_df)
```

#### 分红配股

接口: stock_history_dividend_detail

目标地址: https://vip.stock.finance.sina.com.cn/corp/go.php/vISSUE_ShareBonus/stockid/300670.phtml

描述: 新浪财经-发行与分配-分红配股

限量: 单次获取指定股票的新浪财经-发行与分配-分红配股详情

输入参数

| 名称        | 类型  | 描述                                               |
|-----------|-----|--------------------------------------------------|
| symbol    | str | symbol="600012"; 股票代码                            |
| indicator | str | indicator="配股"; choice of {"分红", "配股"}           |
| date      | str | date="1994-12-24"; 分红配股的具体日期, e.g., "1994-12-24" |

输出参数-分红历史

| 名称    | 类型      | 描述          |
|-------|---------|-------------|
| 公告日期  | object  | -           |
| 送股    | int64   | 注意单位: 股     |
| 转增    | int64   | 注意单位: 股     |
| 派息    | float64 | 注意单位: 元; 税前 |
| 进度    | object  | -           |
| 除权除息日 | object  | -           |
| 股权登记日 | object  | -           |
| 红股上市日 | object  | -           |

接口示例-分红历史

```python
import akshare as ak

stock_history_dividend_detail_df = ak.stock_history_dividend_detail(symbol="600012", indicator="分红")
print(stock_history_dividend_detail_df)
```

输出参数-分红详情

| 名称    | 类型     | 描述   |
|-------|--------|------|
| item  | object | 所列项目 |
| value | object | 项目值  |

接口示例-分红详情

```python
import akshare as ak

stock_history_dividend_detail_df = ak.stock_history_dividend_detail(symbol="600012", indicator="分红",
                                                                    date="2019-07-08")
print(stock_history_dividend_detail_df)
```

输出参数-配股历史

| 名称     | 类型      | 描述             |
|--------|---------|----------------|
| 公告日期   | object  | -              |
| 配股方案   | float64 | 注意单位: 每10股配股股数 |
| 配股价格   | float64 | 注意单位: 元        |
| 基准股本   | int64   | 注意单位: 股        |
| 除权日    | object  | -              |
| 股权登记日  | object  | -              |
| 缴款起始日  | object  | -              |
| 缴款终止日  | object  | -              |
| 配股上市日  | object  | -              |
| 募集资金合计 | float64 | 注意单位: 元        |

接口示例-配股历史

```python
import akshare as ak

stock_history_dividend_detail_df = ak.stock_history_dividend_detail(symbol="000002", indicator="配股")
print(stock_history_dividend_detail_df)
```

输出参数-配股详情

| 名称    | 类型     | 描述   |
|-------|--------|------|
| item  | object | 所列项目 |
| value | object | 项目值  |

接口示例-配股详情

```python
import akshare as ak

stock_history_dividend_detail_df = ak.stock_history_dividend_detail(indicator="配股", symbol="000002",
                                                                    date="1999-12-22")
print(stock_history_dividend_detail_df)
```

#### 历史分红

接口: stock_dividend_cninfo

目标地址: http://webapi.cninfo.com.cn/#/company?companyid=600009

描述: 巨潮资讯-个股-历史分红

限量: 单次获取指定股票的历史分红数据

输入参数

| 名称     | 类型  | 描述              |
|--------|-----|-----------------|
| symbol | str | symbol="600009" |

输出参数

| 名称       | 类型      | 描述           |
|----------|---------|--------------|
| 实施方案公告日期 | object  | -            |
| 送股比例     | float64 | 注意单位: 每 10 股 |
| 转增比例     | float64 | 注意单位: 每 10 股 |
| 派息比例     | float64 | 注意单位: 每 10 股 |
| 股权登记日    | object  | -            |
| 除权日      | object  | -            |
| 派息日      | object  | -            |
| 股份到账日    | object  | -            |
| 实施方案分红说明 | object  | -            |
| 分红类型     | object  | -            |
| 报告时间     | object  | -            |

接口示例

```python
import akshare as ak

stock_dividend_cninfo_df = ak.stock_dividend_cninfo(symbol="600009")
print(stock_dividend_cninfo_df)
```

#### 新股发行

接口: stock_ipo_info

目标地址: https://vip.stock.finance.sina.com.cn/corp/go.php/vISSUE_NewStock/stockid/600004.phtml

描述: 新浪财经-发行与分配-新股发行

限量: 单次获取新股发行的基本信息数据

输入参数

| 名称    | 类型  | 描述                   |
|-------|-----|----------------------|
| stock | str | stock="600004"; 股票代码 |

输出参数

| 名称    | 类型     | 描述   |
|-------|--------|------|
| item  | object | 所列项目 |
| value | object | 项目值  |

接口示例

```python
import akshare as ak

stock_ipo_info_df = ak.stock_ipo_info(stock="600004")
print(stock_ipo_info_df)
```

#### 新股上会信息

接口: stock_ipo_review_em

目标地址: https://data.eastmoney.com/xg/gh/default.html

描述: 东方财富网-数据中心-新股申购-新股上会信息

限量: 单次获取所有数据

输入参数

| 名称 | 类型 | 描述 |
|----|----|----|
| -  | -  | -  |

输出参数

| 名称      | 类型     | 描述 |
|---------|--------|----|
| 序号      | int64  | -  |
| 企业名称    | object | -  |
| 股票简称    | object | -  |
| 股票代码    | object | -  |
| 上市板块    | object | -  |
| 上会日期    | object | -  |
| 审核状态    | object | -  |
| 发审委委员   | object | -  |
| 主承销商    | object | -  |
| 发行数量(股) | object | -  |
| 拟融资额(元) | object | -  |
| 公告日期    | object | -  |
| 上市日期    | object | -  |

接口示例

```python
import akshare as ak

stock_ipo_review_em_df = ak.stock_ipo_review_em()
print(stock_ipo_review_em_df)
```

#### IPO辅导信息

接口: stock_ipo_tutor_em

目标地址: https://data.eastmoney.com/xg/gh/default.html

描述: 东方财富网-数据中心-新股申购-IPO辅导信息

限量: 单次获取所有数据

输入参数

| 名称 | 类型 | 描述 |
|----|----|----|
| -  | -  | -  |

输出参数

| 名称      | 类型     | 描述 |
|---------|--------|----|
| 序号      | int64  | -  |
| 企业名称    | object | -  |
| 辅导机构    | object | -  |
| 辅导状态    | object | -  |
| 报告类型    | object | -  |
| 派出机构    | object | -  |
| 备案日期    | object | -  |

接口示例

```python
import akshare as ak

stock_ipo_tutor_em_df = ak.stock_ipo_tutor_em()
print(stock_ipo_tutor_em_df)
```

#### 股票增发

接口: stock_add_stock

目标地址: https://vip.stock.finance.sina.com.cn/corp/go.php/vISSUE_AddStock/stockid/600004.phtml

描述: 新浪财经-发行与分配-增发

限量: 单次指定 symbol 的股票增发详情数据

输入参数

| 名称     | 类型  | 描述                    |
|--------|-----|-----------------------|
| symbol | str | symbol="600004"; 股票代码 |

输出参数

| 名称         | 类型     | 描述 |
|------------|--------|----|
| 公告日期       | object | -  |
| 发行方式       | object | -  |
| 发行价格       | object | -  |
| 实际公司募集资金总额 | object | -  |
| 发行费用总额     | object | -  |
| 实际发行数量     | object | -  |

接口示例

```python
import akshare as ak

stock_add_stock_df = ak.stock_add_stock(symbol="600004")
print(stock_add_stock_df)
```

#### 限售解禁

##### 个股限售解禁-新浪

接口: stock_restricted_release_queue_sina

目标地址: https://vip.stock.finance.sina.com.cn/q/go.php/vInvestConsult/kind/xsjj/index.phtml?symbol=sh600000

描述: 新浪财经-发行分配-限售解禁

限量: 单次获取指定 symbol 的限售解禁数据

输入参数

| 名称     | 类型  | 描述                    |
|--------|-----|-----------------------|
| symbol | str | symbol="600000"; 股票代码 |

输出参数

| 名称      | 类型      | 描述       |
|---------|---------|----------|
| 代码      | object  | -        |
| 名称      | object  | -        |
| 解禁日期    | object  | -        |
| 解禁数量    | float64 | 注意单位: 万股 |
| 解禁股流通市值 | float64 | 注意单位: 亿元 |
| 上市批次    | int64   | -        |
| 公告日期    | object  | -        |

接口示例

```python
import akshare as ak

stock_restricted_release_queue_sina_df = ak.stock_restricted_release_queue_sina(symbol="600000")
print(stock_restricted_release_queue_sina_df)
```

##### 限售股解禁

接口: stock_restricted_release_summary_em

目标地址: https://data.eastmoney.com/dxf/marketStatistics.html?type=day&startdate=2022-11-08&enddate=2022-12-19

描述: 东方财富网-数据中心-特色数据-限售股解禁

限量: 单次获取指定 symbol 在近期限售股解禁数据

输入参数

| 名称         | 类型  | 描述                                                                      |
|------------|-----|-------------------------------------------------------------------------|
| symbol     | str | symbol="全部股票"; choice of {"全部股票", "沪市A股", "科创板", "深市A股", "创业板", "京市A股"} |
| start_date | str | start_date="20221101"                                                   |
| end_date   | str | end_date="20221209"                                                     |

输出参数

| 名称         | 类型      | 描述      |
|------------|---------|---------|
| 序号         | int64   | -       |
| 解禁时间       | object  | -       |
| 当日解禁股票家数   | int64   | -       |
| 解禁数量       | float64 | 注意单位: 股 |
| 实际解禁数量     | float64 | 注意单位: 股 |
| 实际解禁市值     | int64   | 注意单位: 元 |
| 沪深300指数    | float64 | -       |
| 沪深300指数涨跌幅 | float64 | 注意单位: % |

接口示例

```python
import akshare as ak

stock_restricted_release_summary_em_df = ak.stock_restricted_release_summary_em(symbol="全部股票", start_date="20221108", end_date="20221209")
print(stock_restricted_release_summary_em_df)
```

##### 限售股解禁详情

接口: stock_restricted_release_detail_em

目标地址: https://data.eastmoney.com/dxf/detail.html

描述: 东方财富网-数据中心-限售股解禁-解禁详情一览

限量: 单次获取指定时间段限售股解禁数据

输入参数

| 名称         | 类型  | 描述                                                                      |
|------------|-----|-------------------------------------------------------------------------|
| start_date | str | start_date="20221202"                                                   |
| end_date   | str | end_date="20241202"                                                     |

输出参数

| 名称         | 类型      | 描述      |
|------------|---------|---------|
| 序号         | int64   | -       |
| 股票代码       | object  | -       |
| 股票简称       | object  | -       |
| 解禁时间       | object  | -       |
| 限售股类型      | object  | 注意单位: 股 |
| 解禁数量       | float64 | 注意单位: 股 |
| 实际解禁数量     | float64 | 注意单位: 股 |
| 实际解禁市值     | float64 | 注意单位: 元 |
| 占解禁前流通市值比例 | float64 | -       |
| 解禁前一交易日收盘价 | float64 | -       |
| 解禁前20日涨跌幅  | float64 | 注意单位: % |
| 解禁后20日涨跌幅  | float64 | 注意单位: % |

接口示例

```python
import akshare as ak

stock_restricted_release_detail_em_df = ak.stock_restricted_release_detail_em(start_date="20221202", end_date="20221204")
print(stock_restricted_release_detail_em_df)
```

##### 解禁批次

接口: stock_restricted_release_queue_em

目标地址: https://data.eastmoney.com/dxf/q/600000.html

描述: 东方财富网-数据中心-个股限售解禁-解禁批次

限量: 单次获取指定 symbol 的解禁批次数据

输入参数

| 名称     | 类型  | 描述              |
|--------|-----|-----------------|
| symbol | str | symbol="600000" |

输出参数

| 名称         | 类型      | 描述      |
|------------|---------|---------|
| 序号         | int64   | -       |
| 解禁时间       | object  | -       |
| 解禁股东数      | int64   | -       |
| 解禁数量       | float64 | 注意单位: 股 |
| 实际解禁数量     | float64 | 注意单位: 股 |
| 未解禁数量      | int64   | 注意单位: 股 |
| 实际解禁数量市值   | float64 | 注意单位: 元 |
| 占总市值比例     | float64 | -       |
| 占流通市值比例    | float64 | -       |
| 解禁前一交易日收盘价 | float64 | 注意单位: 元 |
| 限售股类型      | object  | -       |
| 解禁前20日涨跌幅  | float64 | 注意单位: % |
| 解禁后20日涨跌幅  | float64 | 注意单位: % |

接口示例

```python
import akshare as ak

stock_restricted_release_queue_em_df = ak.stock_restricted_release_queue_em(symbol="600000")
print(stock_restricted_release_queue_em_df)
```

##### 解禁股东

接口: stock_restricted_release_stockholder_em

目标地址: https://data.eastmoney.com/dxf/q/600000.html

描述: 东方财富网-数据中心-个股限售解禁-解禁股东

限量: 单次获取指定 symbol 的解禁批次数据

输入参数

| 名称     | 类型  | 描述                                                                           |
|--------|-----|------------------------------------------------------------------------------|
| symbol | str | symbol="600000"                                                              |
| date   | str | date="20200904"; 通过 ak.stock_restricted_release_queue_em(symbol="600000") 获取 |

输出参数

| 名称      | 类型      | 描述      |
|---------|---------|---------|
| 序号      | int64   | -       |
| 股东名称    | object  | -       |
| 解禁数量    | int64   | 注意单位: 股 |
| 实际解禁数量  | int64   | 注意单位: 股 |
| 解禁市值    | float64 | 注意单位: 元 |
| 锁定期     | int64   | 注意单位: 月 |
| 剩余未解禁数量 | int64   | 注意单位: 股 |
| 限售股类型   | object  | -       |
| 进度      | object  | -       |

接口示例

```python
import akshare as ak

stock_restricted_release_stockholder_em_df = ak.stock_restricted_release_stockholder_em(symbol="600000", date="20200904")
print(stock_restricted_release_stockholder_em_df)
```

#### 流通股东

接口: stock_circulate_stock_holder

目标地址: https://vip.stock.finance.sina.com.cn/corp/go.php/vCI_CirculateStockHolder/stockid/600000.phtml

描述: 新浪财经-股东股本-流通股东

限量: 单次获取指定 symbol 的流通股东数据

输入参数

| 名称     | 类型  | 描述                    |
|--------|-----|-----------------------|
| symbol | str | symbol="600000"; 股票代码 |

输出参数

| 名称     | 类型      | 描述      |
|--------|---------|---------|
| 截止日期   | object  | -       |
| 公告日期   | object  | -       |
| 编号     | int64   | -       |
| 股东名称   | object  | -       |
| 持股数量   | int64   | 注意单位: 股 |
| 占流通股比例 | float64 | 注意单位: % |
| 股本性质   | object  | -       |

接口示例

```python
import akshare as ak

stock_circulate_stock_holder_df = ak.stock_circulate_stock_holder(symbol="600000")
print(stock_circulate_stock_holder_df)
```

#### 板块行情

接口: stock_sector_spot

目标地址: http://finance.sina.com.cn/stock/sl/

描述: 新浪行业-板块行情

限量: 单次获取指定的板块行情实时数据

输入参数

| 名称        | 类型  | 描述                                                              |
|-----------|-----|-----------------------------------------------------------------|
| indicator | str | indicator="新浪行业"; choice of {"新浪行业", "启明星行业", "概念", "地域", "行业"} |

输出参数

| 名称     | 类型      | 描述       |
|--------|---------|----------|
| label  | object  | -        |
| 板块     | object  | -        |
| 公司家数   | int64   | -        |
| 平均价格   | float64 | -        |
| 涨跌额    | float64 | -        |
| 涨跌幅    | float64 | 注意单位: %  |
| 总成交量   | int64   | 注意单位: 手  |
| 总成交额   | int64   | 注意单位: 万元 |
| 股票代码   | object  | -        |
| 个股-涨跌幅 | float64 | 注意单位: %  |
| 个股-当前价 | float64 | -        |
| 个股-涨跌额 | float64 | -        |
| 股票名称   | object  | -        |

接口示例

```python
import akshare as ak

stock_industry_sina_df = ak.stock_sector_spot(indicator="新浪行业")
print(stock_industry_sina_df)
```

#### 板块详情

接口: stock_sector_detail

目标地址: http://finance.sina.com.cn/stock/sl/#area_1

描述: 新浪行业-板块行情-成份详情, 由于新浪网页提供的统计数据有误, 部分行业数量大于统计数

限量: 单次获取指定的新浪行业-板块行情-成份详情

输入参数

| 名称     | 类型  | 描述                                                                        |
|--------|-----|---------------------------------------------------------------------------|
| sector | str | sector="hangye_ZL01"; 通过 **ak.stock_sector_spot** 返回数据的 label 字段选择 sector |

输出参数

| 名称            | 类型      | 描述  |
|---------------|---------|-----|
| symbol        | object  | -   |
| code          | object  | -   |
| name          | object  | -   |
| trade         | float64 | -   |
| pricechange   | float64 | -   |
| changepercent | float64 | -   |
| buy           | float64 | -   |
| sell          | float64 | -   |
| settlement    | float64 | -   |
| open          | float64 | -   |
| high          | float64 | -   |
| low           | float64 | -   |
| volume        | int64   | -   |
| amount        | int64   | -   |
| ticktime      | object  | -   |
| per           | float64 | -   |
| pb            | float64 | -   |
| mktcap        | float64 | -   |
| nmc           | float64 | -   |
| turnoverratio | float64 | -   |

接口示例

```python
import akshare as ak

stock_sector_detail_df = ak.stock_sector_detail(sector="hangye_ZL01")
print(stock_sector_detail_df)
```

#### 股票列表-A股

接口: stock_info_a_code_name

目标地址: 沪深京三个交易所

描述: 沪深京 A 股股票代码和股票简称数据

限量: 单次获取所有 A 股股票代码和简称数据

输入参数

| 名称  | 类型  | 描述  |
|-----|-----|-----|
| -   | -   | -   |

输出参数

| 名称   | 类型     | 描述  |
|------|--------|-----|
| code | object | -   |
| name | object | -   |

接口示例

```python
import akshare as ak

stock_info_a_code_name_df = ak.stock_info_a_code_name()
print(stock_info_a_code_name_df)
```

#### 股票列表-上证

接口: stock_info_sh_name_code

目标地址: https://www.sse.com.cn/assortment/stock/list/share/

描述: 上海证券交易所股票代码和简称数据

限量: 单次获取所有上海证券交易所股票代码和简称数据

输入参数

| 名称     | 类型  | 描述                                               |
|--------|-----|--------------------------------------------------|
| symbol | str | symbol="主板A股"; choice of {"主板A股", "主板B股", "科创板"} |

输出参数

| 名称   | 类型     | 描述  |
|------|--------|-----|
| 证券代码 | object | -   |
| 证券简称 | object | -   |
| 公司全称 | object | -   |
| 上市日期 | object | -   |

接口示例

```python
import akshare as ak

stock_info_sh_name_code_df = ak.stock_info_sh_name_code(symbol="主板A股")
print(stock_info_sh_name_code_df)
```

#### 股票列表-深证

接口: stock_info_sz_name_code

目标地址: https://www.szse.cn/market/product/stock/list/index.html

描述: 深证证券交易所股票代码和股票简称数据

限量: 单次获取深证证券交易所股票代码和简称数据

输入参数

| 名称     | 类型  | 描述                                                          |
|--------|-----|-------------------------------------------------------------|
| symbol | str | symbol="A股列表"; choice of {"A股列表", "B股列表", "CDR列表", "AB股列表"} |

输出参数-A股列表

| 名称     | 类型     | 描述  |
|--------|--------|-----|
| 板块     | object | -   |
| A股代码   | object | -   |
| A股简称   | object | -   |
| A股上市日期 | object | -   |
| A股总股本  | object | -   |
| A股流通股本 | object | -   |
| 所属行业   | object | -   |

接口示例

```python
import akshare as ak

stock_info_sz_name_code_df = ak.stock_info_sz_name_code(symbol="A股列表")
print(stock_info_sz_name_code_df)
```

#### 股票列表-北证

接口: stock_info_bj_name_code

目标地址: https://www.bse.cn/nq/listedcompany.html

描述: 北京证券交易所股票代码和简称数据

限量: 单次获取北京证券交易所所有的股票代码和简称数据

输入参数

| 名称  | 类型  | 描述  |
|-----|-----|-----|
| -   | -   | -   |

输出参数

| 名称   | 类型     | 描述      |
|------|--------|---------|
| 证券代码 | object | -       |
| 证券简称 | object | -       |
| 总股本  | int64  | 注意单位: 股 |
| 流通股本 | int64  | 注意单位: 股 |
| 上市日期 | object | -       |
| 所属行业 | object | -       |
| 地区   | object | -       |
| 报告日期 | object | -       |

接口示例

```python
import akshare as ak

stock_info_bj_name_code_df = ak.stock_info_bj_name_code()
print(stock_info_bj_name_code_df)
```

#### 终止/暂停上市-深证

接口: stock_info_sz_delist

目标地址: https://www.szse.cn/market/stock/suspend/index.html

描述: 深证证券交易所终止/暂停上市股票

限量: 单次获取深证证券交易所终止/暂停上市数据

输入参数

| 名称     | 类型  | 描述                                              |
|--------|-----|-------------------------------------------------|
| symbol | str | symbol="终止上市公司"; choice of {"暂停上市公司", "终止上市公司"} |

输出参数

| 名称     | 类型     | 描述  |
|--------|--------|-----|
| 证券代码   | object | -   |
| 证券简称   | object | -   |
| 上市日期   | object | -   |
| 终止上市日期 | object | -   |

接口示例

```python
import akshare as ak

stock_info_sz_delist_df = ak.stock_info_sz_delist(symbol="终止上市公司")
print(stock_info_sz_delist_df)
```

#### 两网及退市

接口: stock_staq_net_stop

目标地址: https://quote.eastmoney.com/center/gridlist.html#staq_net_board

描述: 东方财富网-行情中心-沪深个股-两网及退市

限量: 单次获取所有两网及退市的股票数据

输入参数

| 名称  | 类型  | 描述  |
|-----|-----|-----|
| -   | -   | -   |

输出参数

| 名称  | 类型     | 描述  |
|-----|--------|-----|
| 序号  | int64  | -   |
| 代码  | object | -   |
| 名称  | object | -   |

接口示例

```python
import akshare as ak

stock_staq_net_stop_df = ak.stock_staq_net_stop()
print(stock_staq_net_stop_df)
```

#### 暂停/终止上市-上证

接口: stock_info_sh_delist

目标地址: https://www.sse.com.cn/assortment/stock/list/delisting/

描述: 上海证券交易所暂停/终止上市股票

限量: 单次获取上海证券交易所暂停/终止上市股票

输入参数

| 名称     | 类型  | 描述                                         |
|--------|-----|--------------------------------------------|
| symbol | str | symbol="全部"; choice of {"全部", "沪市", "科创板"} |

输出参数

| 名称     | 类型     | 描述  |
|--------|--------|-----|
| 公司代码   | object | -   |
| 公司简称   | object | -   |
| 上市日期   | object | -   |
| 暂停上市日期 | object | -   |

接口示例

```python
import akshare as ak

stock_info_sh_delist_df = ak.stock_info_sh_delist(symbol="全部")
print(stock_info_sh_delist_df)
```

#### 股票更名

接口: stock_info_change_name

目标地址: https://vip.stock.finance.sina.com.cn/corp/go.php/vCI_CorpInfo/stockid/300378.phtml

描述: 新浪财经-股票曾用名

限量: 单次指定 symbol 的所有历史曾用名称

输入参数

| 名称     | 类型  | 描述                    |
|--------|-----|-----------------------|
| symbol | str | symbol="000503"; 股票代码 |

输出参数

| 名称    | 类型     | 描述  |
|-------|--------|-----|
| index | int64  | -   |
| name  | object | -   |

接口示例

```python
import akshare as ak

stock_info_change_name_list = ak.stock_info_change_name(symbol="000503")
print(stock_info_change_name_list)
```

#### 名称变更-深证

接口: stock_info_sz_change_name

目标地址: https://www.szse.cn/www/market/stock/changename/index.html

描述: 深证证券交易所-市场数据-股票数据-名称变更

限量: 单次获取所有历史数据

输入参数

| 名称     | 类型  | 描述                                        |
|--------|-----|-------------------------------------------|
| symbol | str | symbol="全称变更"; choice of {"全称变更", "简称变更"} |

输出参数

| 名称    | 类型     | 描述  |
|-------|--------|-----|
| 变更日期  | object | -   |
| 证券代码  | object | -   |
| 证券简称  | object | -   |
| 变更前全称 | object | -   |
| 变更后全称 | object | -   |

接口示例

```python
import akshare as ak

stock_info_sz_change_name_df = ak.stock_info_sz_change_name(symbol="全称变更")
print(stock_info_sz_change_name_df)
```

#### 基金持股

接口: stock_fund_stock_holder

目标地址: https://vip.stock.finance.sina.com.cn/corp/go.php/vCI_FundStockHolder/stockid/600004.phtml

描述: 新浪财经-股本股东-基金持股

限量: 新浪财经-股本股东-基金持股所有历史数据

输入参数

| 名称     | 类型  | 描述                    |
|--------|-----|-----------------------|
| symbol | str | symbol="600004"; 股票代码 |

输出参数

| 名称     | 类型      | 描述      |
|--------|---------|---------|
| 基金名称   | object  | -       |
| 基金代码   | object  | -       |
| 持仓数量   | int64   | 注意单位: 股 |
| 占流通股比例 | float64 | 注意单位: % |
| 持股市值   | int64   | 注意单位: 元 |
| 占净值比例  | float64 | 注意单位: % |
| 截止日期   | object  | -       |

接口示例

```python
import akshare as ak

stock_fund_stock_holder_df = ak.stock_fund_stock_holder(symbol="601318")
print(stock_fund_stock_holder_df)
```

#### 主要股东

接口: stock_main_stock_holder

目标地址: https://vip.stock.finance.sina.com.cn/corp/go.php/vCI_StockHolder/stockid/600004.phtml

描述: 新浪财经-股本股东-主要股东

限量: 单次获取所有历史数据

输入参数

| 名称    | 类型  | 描述                   |
|-------|-----|----------------------|
| stock | str | stock="600004"; 股票代码 |

输出参数

| 名称    | 类型      | 描述         |
|-------|---------|------------|
| 编号    | object  | -          |
| 股东名称  | object  | -          |
| 持股数量  | float64 | 注意单位: 股    |
| 持股比例  | float64 | 注意单位: %    |
| 股本性质  | object  | -          |
| 截至日期  | object  | -          |
| 公告日期  | object  | -          |
| 股东说明  | object  | -          |
| 股东总数  | float64 | -          |
| 平均持股数 | float64 | 备注: 按总股本计算 |

接口示例

```python
import akshare as ak

stock_main_stock_holder_df = ak.stock_main_stock_holder(stock="600004")
print(stock_main_stock_holder_df)
```

#### 机构持股

##### 机构持股一览表

接口: stock_institute_hold

目标地址: https://vip.stock.finance.sina.com.cn/q/go.php/vComStockHold/kind/jgcg/index.phtml

描述: 新浪财经-机构持股-机构持股一览表

限量: 单次获取所有历史数据

输入参数

| 名称     | 类型  | 描述                                                                                                              |
|--------|-----|-----------------------------------------------------------------------------------------------------------------|
| symbol | str | symbol="20051"; 从 2005 年开始, {"一季报":1, "中报":2 "三季报":3 "年报":4}, e.g., "20191", 其中的 1 表示一季报; "20193", 其中的 3 表示三季报; |

输出参数

| 名称       | 类型      | 描述      |
|----------|---------|---------|
| 证券代码     | object  | -       |
| 证券简称     | object  | -       |
| 机构数      | int64   | -       |
| 机构数变化    | int64   | -       |
| 持股比例     | float64 | 注意单位: % |
| 持股比例增幅   | float64 | 注意单位: % |
| 占流通股比例   | float64 | 注意单位: % |
| 占流通股比例增幅 | float64 | 注意单位: % |

接口示例

```python
import akshare as ak

stock_institute_hold_df = ak.stock_institute_hold(symbol="20201")
print(stock_institute_hold_df)
```

##### 机构持股详情

接口: stock_institute_hold_detail

目标地址: http://vip.stock.finance.sina.com.cn/q/go.php/vComStockHold/kind/jgcg/index.phtml

描述: 新浪财经-机构持股-机构持股详情

限量: 单次所有历史数据

输入参数

| 名称      | 类型  | 描述                                                                                                               |
|---------|-----|------------------------------------------------------------------------------------------------------------------|
| stock   | str | stock="300003"; 股票代码                                                                                             |
| quarter | str | quarter="20201"; 从 2005 年开始, {"一季报":1, "中报":2 "三季报":3 "年报":4}, e.g., "20191", 其中的 1 表示一季报; "20193", 其中的 3 表示三季报; |

输出参数

| 名称       | 类型      | 描述       |
|----------|---------|----------|
| 持股机构类型   | object  | -        |
| 持股机构代码   | object  | -        |
| 持股机构简称   | object  | -        |
| 持股机构全称   | object  | -        |
| 持股数      | float64 | 注意单位: 万股 |
| 最新持股数    | float64 | 注意单位: 万股 |
| 持股比例     | float64 | 注意单位: %  |
| 最新持股比例   | float64 | 注意单位: %  |
| 占流通股比例   | float64 | 注意单位: %  |
| 最新占流通股比例 | float64 | 注意单位: %  |
| 持股比例增幅   | float64 | 注意单位: %  |
| 占流通股比例增幅 | float64 | 注意单位: %  |

接口示例

```python
import akshare as ak

stock_institute_hold_detail_df = ak.stock_institute_hold_detail(stock="300003", quarter="20201")
print(stock_institute_hold_detail_df)
```

#### 机构推荐

##### 机构推荐池

接口: stock_institute_recommend

目标地址: http://stock.finance.sina.com.cn/stock/go.php/vIR_RatingNewest/index.phtml

描述: 新浪财经-机构推荐池-具体指标的数据

限量: 单次获取新浪财经-机构推荐池-具体指标的所有数据

输入参数

| 名称     | 类型  | 描述                                                                                                                 |
|--------|-----|--------------------------------------------------------------------------------------------------------------------|
| symbol | str | symbol="行业关注度"; choice of {'最新投资评级', '上调评级股票', '下调评级股票', '股票综合评级', '首次评级股票', '目标涨幅排名', '机构关注度', '行业关注度', '投资评级选股'} |

输出参数

| 名称  | 类型  | 描述                |
|-----|-----|-------------------|
| -   | -   | 根据特定 indicator 而定 |

接口示例

```python
import akshare as ak

stock_institute_recommend_df = ak.stock_institute_recommend(symbol="投资评级选股")
print(stock_institute_recommend_df)
```

##### 股票评级记录

接口: stock_institute_recommend_detail

目标地址: http://stock.finance.sina.com.cn/stock/go.php/vIR_StockSearch/key/sz000001.phtml

描述: 新浪财经-机构推荐池-股票评级记录

限量: 单次获取新浪财经-机构推荐池-股票评级记录的所有数据

输入参数

| 名称     | 类型  | 描述              |
|--------|-----|-----------------|
| symbol | str | symbol="000001" |

输出参数

| 名称   | 类型  | 描述  |
|------|-----|-----|
| 股票代码 | str | -   |
| 股票名称 | str | -   |
| 目标价  | str | -   |
| 最新评级 | str | -   |
| 评级机构 | str | -   |
| 分析师  | str | -   |
| 行业   | str | -   |
| 评级日期 | str | -   |

接口示例

```python
import akshare as ak

stock_institute_recommend_detail_df = ak.stock_institute_recommend_detail(symbol="002709")
print(stock_institute_recommend_detail_df)
```

##### 投资评级

接口: stock_rank_forecast_cninfo

目标地址: https://webapi.cninfo.com.cn/#/thematicStatistics

描述: 巨潮资讯-数据中心-评级预测-投资评级

限量: 单次获取指定交易日的所有数据

输入参数

| 名称   | 类型  | 描述                   |
|------|-----|----------------------|
| date | str | date="20210910"; 交易日 |

输出参数

| 名称      | 类型      | 描述  |
|---------|---------|-----|
| 证券代码    | object  | -   |
| 证券简称    | object  | -   |
| 发布日期    | object  | -   |
| 研究机构简称  | object  | -   |
| 研究员名称   | object  | -   |
| 投资评级    | object  | -   |
| 是否首次评级  | object  | -   |
| 评级变化    | object  | -   |
| 前一次投资评级 | object  | -   |
| 目标价格-下限 | float64 | -   |
| 目标价格-上限 | float64 | -   |

接口示例

```python
import akshare as ak

stock_rank_forecast_cninfo_df = ak.stock_rank_forecast_cninfo(date="20230817")
print(stock_rank_forecast_cninfo_df)
```

##### 申万个股行业分类变动历史

接口: stock_industry_clf_hist_sw

目标地址: http://www.swhyresearch.com/institute_sw/allIndex/downloadCenter/industryType

描述: 申万宏源研究-行业分类-全部行业分类

限量: 单次获取所有个股的行业分类变动历史数据

输入参数

| 名称 | 类型 | 描述 |
|----|----|----|
| -  | -  | -  |

输出参数

| 名称            | 类型     | 描述     |
|---------------|--------|--------|
| symbol        | object | 股票代码   |
| start_date    | object | 计入日期   |
| industry_code | object | 申万行业代码 |
| update_time   | object | 更新日期   |

接口示例

```python
import akshare as ak

stock_industry_clf_hist_sw_df = ak.stock_industry_clf_hist_sw()
print(stock_industry_clf_hist_sw_df)
```

##### 行业市盈率

接口: stock_industry_pe_ratio_cninfo

目标地址: http://webapi.cninfo.com.cn/#/thematicStatistics

描述: 巨潮资讯-数据中心-行业分析-行业市盈率

限量: 单次获取指定 symbol 在指定交易日的所有数据; 只能获取近期的数据

输入参数

| 名称     | 类型  | 描述                                                |
|--------|-----|---------------------------------------------------|
| symbol | str | symbol="证监会行业分类"; choice of {"证监会行业分类", "国证行业分类"} |
| date   | str | date="20210910"; 交易日                              |

输出参数

| 名称         | 类型      | 描述       |
|------------|---------|----------|
| 变动日期       | object  | -        |
| 行业分类       | object  | -        |
| 行业层级       | int64   | -        |
| 行业编码       | object  | -        |
| 行业名称       | object  | -        |
| 公司数量       | float64 | -        |
| 纳入计算公司数量   | float64 | -        |
| 总市值-静态     | float64 | 注意单位: 亿元 |
| 净利润-静态     | float64 | 注意单位: 亿元 |
| 静态市盈率-加权平均 | float64 | -        |
| 静态市盈率-中位数  | float64 | -        |
| 静态市盈率-算术平均 | float64 | -        |

接口示例

```python
import akshare as ak

stock_industry_pe_ratio_cninfo_df = ak.stock_industry_pe_ratio_cninfo(symbol="国证行业分类", date="20240617")
print(stock_industry_pe_ratio_cninfo_df)
```

##### 新股过会

接口: stock_new_gh_cninfo

目标地址: https://webapi.cninfo.com.cn/#/xinguList

描述: 巨潮资讯-数据中心-新股数据-新股过会

限量: 单次获取近一年所有新股过会的数据

输入参数

| 名称  | 类型  | 描述  |
|-----|-----|-----|
| -   | -   | -   |

输出参数

| 名称    | 类型     | 描述  |
|-------|--------|-----|
| 公司名称  | object | -   |
| 上会日期  | object | -   |
| 审核类型  | object | -   |
| 审议内容  | object | -   |
| 审核结果  | object | -   |
| 审核公告日 | object | -   |

接口示例

```python
import akshare as ak

stock_new_gh_cninfo_df = ak.stock_new_gh_cninfo()
print(stock_new_gh_cninfo_df)
```

##### 新股发行

接口: stock_new_ipo_cninfo

目标地址: https://webapi.cninfo.com.cn/#/xinguList

描述: 巨潮资讯-数据中心-新股数据-新股发行

限量: 单次获取近三年所有新股发行的数据

输入参数

| 名称  | 类型  | 描述  |
|-----|-----|-----|
| -   | -   | -   |

输出参数

| 名称      | 类型      | 描述       |
|---------|---------|----------|
| 证劵代码    | object  | -        |
| 证券简称    | object  | -        |
| 上市日期    | object  | -        |
| 申购日期    | object  | -        |
| 发行价     | float64 | 注意单位: 元  |
| 总发行数量   | float64 | 注意单位: 万股 |
| 发行市盈率   | float64 | -        |
| 上网发行中签率 | float64 | 注意单位: %  |
| 摇号结果公告日 | object  | -        |
| 中签公告日   | object  | -        |
| 中签缴款日   | object  | -        |
| 网上申购上限  | float64 | -        |
| 上网发行数量  | float64 | -        |

接口示例

```python
import akshare as ak

stock_new_ipo_cninfo_df = ak.stock_new_ipo_cninfo()
print(stock_new_ipo_cninfo_df)
```

##### 董监高及相关人员持股变动-上证

接口: stock_share_hold_change_sse

目标地址: http://www.sse.com.cn/disclosure/credibility/supervision/change/

描述: 上海证券交易所-披露-监管信息公开-公司监管-董董监高人员股份变动

限量: 单次获取指定 symbol 的数据

输入参数

| 名称     | 类型  | 描述                                          |
|--------|-----|---------------------------------------------|
| symbol | str | symbol="600000"; choice of {"全部", "具体股票代码"} |

输出参数

| 名称       | 类型      | 描述 |
|----------|---------|----|
| 公司代码     | object  | -  |
| 公司名称     | object  | -  |
| 姓名       | object  | -  |
| 职务       | object  | -  |
| 股票种类     | object  | -  |
| 货币种类     | object  | -  |
| 本次变动前持股数 | int64   | -  |
| 变动数      | int64   | -  |
| 本次变动平均价格 | float64 | -  |
| 变动后持股数   | int64   | -  |
| 变动原因     | object  | -  |
| 变动日期     | object  | -  |
| 填报日期     | object  | -  |

接口示例

```python
import akshare as ak

stock_share_hold_change_sse_df = ak.stock_share_hold_change_sse(symbol="600000")
print(stock_share_hold_change_sse_df)
```

##### 董监高及相关人员持股变动-深证

接口: stock_share_hold_change_szse

目标地址: http://www.szse.cn/disclosure/supervision/change/index.html

描述: 深圳证券交易所-信息披露-监管信息公开-董监高人员股份变动

限量: 单次获取指定 symbol 的数据

输入参数

| 名称     | 类型  | 描述                                          |
|--------|-----|---------------------------------------------|
| symbol | str | symbol="001308"; choice of {"全部", "具体股票代码"} |

输出参数

| 名称         | 类型      | 描述         |
|------------|---------|------------|
| 证券代码       | object  | -          |
| 证券简称       | object  | -          |
| 董监高姓名      | object  | -          |
| 变动日期       | object  | -          |
| 变动股份数量     | float64 | 注意单位: 万股   |
| 成交均价       | float64 | -          |
| 变动原因       | object  | -          |
| 变动比例       | float64 | 注意单位: 千分之一 |
| 当日结存股数     | float64 | 注意单位: 万股   |
| 股份变动人姓名    | object  | -          |
| 职务         | object  | -          |
| 变动人与董监高的关系 | object  | -          |

接口示例

```python
import akshare as ak

stock_share_hold_change_szse_df = ak.stock_share_hold_change_szse(symbol="001308")
print(stock_share_hold_change_szse_df)
```

##### 董监高及相关人员持股变动-北证

接口: stock_share_hold_change_bse

目标地址: https://www.bse.cn/disclosure/djg_sharehold_change.html

描述: 北京证券交易所-信息披露-监管信息-董监高及相关人员持股变动

限量: 单次获取指定 symbol 的数据

输入参数

| 名称     | 类型  | 描述                                          |
|--------|-----|---------------------------------------------|
| symbol | str | symbol="430489"; choice of {"全部", "具体股票代码"} |

输出参数

| 名称     | 类型      | 描述       |
|--------|---------|----------|
| 代码     | object  | -        |
| 简称     | object  | -        |
| 姓名     | object  | -        |
| 职务     | object  | -        |
| 变动日期   | object  | -        |
| 变动股数   | float64 | 注意单位: 万股 |
| 变动前持股数 | float64 | 注意单位: 万股 |
| 变动后持股数 | float64 | 注意单位: 万股 |
| 变动均价   | float64 | 注意单位: 元  |
| 变动原因   | object  | -        |

接口示例

```python
import akshare as ak

stock_share_hold_change_bse_df = ak.stock_share_hold_change_bse(symbol="430489")
print(stock_share_hold_change_bse_df)
```

##### 股东人数及持股集中度

接口: stock_hold_num_cninfo

目标地址: https://webapi.cninfo.com.cn/#/thematicStatistics

描述: 巨潮资讯-数据中心-专题统计-股东股本-股东人数及持股集中度

限量: 单次指定 date 的股东人数及持股集中度数据, 从 20170331 开始

输入参数

| 名称   | 类型  | 描述                                                                                         |
|------|-----|--------------------------------------------------------------------------------------------|
| date | str | date="20210630"; choice of {"XXXX0331", "XXXX0630", "XXXX0930", "XXXX1231"}; 从 20170331 开始 |

输出参数

| 名称       | 类型      | 描述       |
|----------|---------|----------|
| 证劵代码     | object  | -        |
| 证券简称     | object  | -        |
| 变动日期     | object  | -        |
| 本期股东人数   | int64   | -        |
| 上期股东人数   | float64 | -        |
| 股东人数增幅   | float64 | 注意单位: %  |
| 本期人均持股数量 | int64   | 注意单位: 万股 |
| 上期人均持股数量 | float64 | 注意单位: %  |
| 人均持股数量增幅 | float64 | 注意单位: %  |

接口示例

```python
import akshare as ak

stock_hold_num_cninfo_df = ak.stock_hold_num_cninfo(date="20210630")
print(stock_hold_num_cninfo_df)
```

##### 股本变动

接口: stock_hold_change_cninfo

目标地址: https://webapi.cninfo.com.cn/#/thematicStatistics

描述: 巨潮资讯-数据中心-专题统计-股东股本-股本变动

限量: 单次指定 symbol 的股本变动数据

输入参数

| 名称     | 类型  | 描述                                                               |
|--------|-----|------------------------------------------------------------------|
| symbol | str | symbol="全部"; choice of {"深市主板", "沪市", "创业板", "科创板", "北交所", "全部"} |

输出参数

| 名称     | 类型      | 描述     |
|--------|---------|--------|
| 证券代码   | object  | -      |
| 证券简称   | object  | -      |
| 交易市场   | object  | -      |
| 公告日期   | object  | -      |
| 变动日期   | object  | -      |
| 变动原因   | object  | -      |
| 总股本    | float64 | 单位: 万股 |
| 已流通股份  | float64 | 单位: 万股 |
| 已流通比例  | float64 | 单位: %  |
| 流通受限股份 | float64 | 单位: 万股 |

接口示例

```python
import akshare as ak

stock_hold_change_cninfo_df = ak.stock_hold_change_cninfo(symbol="全部")
print(stock_hold_change_cninfo_df)
```

##### 实际控制人持股变动

接口: stock_hold_control_cninfo

目标地址: https://webapi.cninfo.com.cn/#/thematicStatistics

描述: 巨潮资讯-数据中心-专题统计-股东股本-实际控制人持股变动

限量: 单次指定 symbol 的实际控制人持股变动数据, 从 2010 开始

输入参数

| 名称     | 类型  | 描述                                                                         |
|--------|-----|----------------------------------------------------------------------------|
| symbol | str | symbol="全部"; choice of {"单独控制", "实际控制人", "一致行动人", "家族控制", "全部"}; 从 2010 开始 |

输出参数

| 名称      | 类型      | 描述       |
|---------|---------|----------|
| 证劵代码    | object  | -        |
| 证券简称    | object  | -        |
| 变动日期    | object  | -        |
| 实际控制人名称 | object  | -        |
| 控股数量    | float64 | 注意单位: 万股 |
| 控股比例    | float64 | 注意单位: %  |
| 直接控制人名称 | object  | -        |
| 控制类型    | object  | -        |

接口示例

```python
import akshare as ak

stock_hold_control_cninfo_df = ak.stock_hold_control_cninfo(symbol="全部")
print(stock_hold_control_cninfo_df)
```

##### 高管持股变动明细

接口: stock_hold_management_detail_cninfo

目标地址: https://webapi.cninfo.com.cn/#/thematicStatistics

描述: 巨潮资讯-数据中心-专题统计-股东股本-高管持股变动明细

限量: 单次指定 symbol 的高管持股变动明细数据, 返回近一年的数据

输入参数

| 名称     | 类型  | 描述                                  |
|--------|-----|-------------------------------------|
| symbol | str | symbol="增持"; choice of {"增持", "减持"} |

输出参数

| 名称        | 类型      | 描述       |
|-----------|---------|----------|
| 证劵代码      | object  | -        |
| 证券简称      | object  | -        |
| 截止日期      | object  | -        |
| 公告日期      | object  | -        |
| 高管姓名      | object  | -        |
| 董监高姓名     | object  | -        |
| 董监高职务     | object  | -        |
| 变动人与董监高关系 | object  | -        |
| 期初持股数量    | float64 | 注意单位: 万股 |
| 期末持股数量    | float64 | 注意单位: 万股 |
| 变动数量      | float64 | -        |
| 变动比例      | int64   | 注意单位: %  |
| 成交均价      | float64 | 注意单位: 元  |
| 期末市值      | float64 | 注意单位: 万元 |
| 持股变动原因    | object  | -        |
| 数据来源      | object  | -        |

接口示例

```python
import akshare as ak

stock_hold_management_detail_cninfo_df = ak.stock_hold_management_detail_cninfo(symbol="增持")
print(stock_hold_management_detail_cninfo_df)
```

##### 董监高及相关人员持股变动明细

接口: stock_hold_management_detail_em

目标地址: https://data.eastmoney.com/executive/list.html

描述: 东方财富网-数据中心-特色数据-高管持股-董监高及相关人员持股变动明细

限量: 单次返回所有数据

输入参数

| 名称 | 类型 | 描述 |
|----|----|----|
| -  | -  | -  |

输出参数

| 名称         | 类型      | 描述 |
|------------|---------|----|
| 日期         | object  | -  |
| 代码         | object  | -  |
| 名称         | object  | -  |
| 变动人        | object  | -  |
| 变动股数       | int64   | -  |
| 成交均价       | int64   | -  |
| 变动金额       | float64 | -  |
| 变动原因       | object  | -  |
| 变动比例       | float64 | -  |
| 变动后持股数     | float64 | -  |
| 持股种类       | object  | -  |
| 董监高人员姓名    | object  | -  |
| 职务         | object  | -  |
| 变动人与董监高的关系 | object  | -  |
| 开始时持有      | float64 | -  |
| 结束后持有      | float64 | -  |

接口示例

```python
import akshare as ak

stock_hold_management_detail_em_df = ak.stock_hold_management_detail_em()
print(stock_hold_management_detail_em_df)
```

##### 人员增减持股变动明细

接口: stock_hold_management_person_em

目标地址: https://data.eastmoney.com/executive/personinfo.html?name=%E5%90%B4%E8%BF%9C&code=001308

描述: 东方财富网-数据中心-特色数据-高管持股-人员增减持股变动明细

限量: 单次返回指定 symbol 和 name 的数据

输入参数

| 名称     | 类型  | 描述                    |
|--------|-----|-----------------------|
| symbol | str | symbol="001308"; 股票代码 |
| name   | str | name="吴远"; 高管名称       |

输出参数

| 名称         | 类型      | 描述 |
|------------|---------|----|
| 日期         | object  | -  |
| 代码         | object  | -  |
| 名称         | object  | -  |
| 变动人        | object  | -  |
| 变动股数       | int64   | -  |
| 成交均价       | int64   | -  |
| 变动金额       | float64 | -  |
| 变动原因       | object  | -  |
| 变动比例       | float64 | -  |
| 变动后持股数     | float64 | -  |
| 持股种类       | object  | -  |
| 董监高人员姓名    | object  | -  |
| 职务         | object  | -  |
| 变动人与董监高的关系 | object  | -  |
| 开始时持有      | float64 | -  |
| 结束后持有      | float64 | -  |

接口示例

```python
import akshare as ak

stock_hold_management_person_em_df = ak.stock_hold_management_person_em(symbol="001308", name="孙建华")
print(stock_hold_management_person_em_df)
```

##### 对外担保

接口: stock_cg_guarantee_cninfo

目标地址: https://webapi.cninfo.com.cn/#/thematicStatistics

描述: 巨潮资讯-数据中心-专题统计-公司治理-对外担保

限量: 单次指定 symbol 和起始日期的对外担保数据

输入参数

| 名称         | 类型  | 描述                                                        |
|------------|-----|-----------------------------------------------------------|
| symbol     | str | symbol="全部"; choice of {"全部", "深市主板", "沪市", "创业板", "科创板"} |
| start_date | str | start_date="20180630"                                     |
| end_date   | str | end_date="20210927"                                       |

输出参数

| 名称          | 类型      | 描述       |
|-------------|---------|----------|
| 证劵代码        | object  | -        |
| 证券简称        | object  | -        |
| 公告统计区间      | object  | -        |
| 担保笔数        | int64   | -        |
| 担保金额        | float64 | 注意单位: 万元 |
| 归属于母公司所有者权益 | float64 | 注意单位: 万元 |
| 担保金融占净资产比例  | float64 | 注意单位: %  |

接口示例

```python
import akshare as ak

stock_corporate_governance_guarantee_df = ak.stock_cg_guarantee_cninfo(symbol="全部", start_date="20180630", end_date="20210927")
print(stock_corporate_governance_guarantee_df)
```

##### 公司诉讼

接口: stock_cg_lawsuit_cninfo

目标地址: http://webapi.cninfo.com.cn/#/thematicStatistics

描述: 巨潮资讯-数据中心-专题统计-公司治理-公司诉讼

限量: 单次指定 symbol 和起始日期的公司诉讼数据

输入参数

| 名称         | 类型  | 描述                                                        |
|------------|-----|-----------------------------------------------------------|
| symbol     | str | symbol="全部"; choice of {"全部", "深市主板", "沪市", "创业板", "科创板"} |
| start_date | str | start_date="20180630"                                     |
| end_date   | str | end_date="20210927"                                       |

输出参数

| 名称     | 类型      | 描述       |
|--------|---------|----------|
| 证劵代码   | object  | -        |
| 证券简称   | object  | -        |
| 公告统计区间 | object  | -        |
| 诉讼次数   | int64   | -        |
| 诉讼金额   | float64 | 注意单位: 万元 |

接口示例

```python
import akshare as ak

stock_cg_lawsuit_cninfo_df = ak.stock_cg_lawsuit_cninfo(symbol="全部", start_date="20180630", end_date="20210927")
print(stock_cg_lawsuit_cninfo_df)
```

##### 股权质押

接口: stock_cg_equity_mortgage_cninfo

目标地址: https://webapi.cninfo.com.cn/#/thematicStatistics

描述: 巨潮资讯-数据中心-专题统计-公司治理-股权质押

限量: 单次指定 date 的股权质押数据

输入参数

| 名称   | 类型  | 描述              |
|------|-----|-----------------|
| date | str | date="20210930" |

输出参数

| 名称         | 类型      | 描述       |
|------------|---------|----------|
| 股票代码       | object  | -        |
| 股票简称       | object  | -        |
| 公告日期       | object  | -        |
| 出质人        | object  | -        |
| 质权人        | object  | -        |
| 质押数量       | float64 | 注意单位: 万股 |
| 占总股本比例     | float64 | 注意单位: %  |
| 质押解除数量     | float64 | 注意单位: 万股 |
| 质押事项       | object  | 注意单位: 万元 |
| 累计质押占总股本比例 | float64 | 注意单位: %  |

接口示例

```python
import akshare as ak

stock_cg_equity_mortgage_cninfo_df = ak.stock_cg_equity_mortgage_cninfo(date="20210930")
print(stock_cg_equity_mortgage_cninfo_df)
```

#### 美港目标价

接口: stock_price_js

目标地址: https://www.ushknews.com/report.html

描述: 美港电讯-美港目标价数据

限量: 单次获取所有数据, 数据从 2019-至今; 该接口暂时不能使用

输入参数

| 名称     | 类型  | 描述                                  |
|--------|-----|-------------------------------------|
| symbol | str | symbol="us"; choice of {"us", "hk"} |

输出参数

| 名称    | 类型      | 描述  |
|-------|---------|-----|
| 日期    | object  | -   |
| 个股名称  | object  | -   |
| 评级    | object  | -   |
| 先前目标价 | float64 | -   |
| 最新目标价 | float64 | -   |
| 机构名称  | object  | -   |

接口示例

```python
import akshare as ak

stock_price_js_df = ak.stock_price_js(symbol="us")
print(stock_price_js_df)
```

#### 券商业绩月报

接口: stock_qsjy_em

目标地址: http://data.eastmoney.com/other/qsjy.html

描述: 东方财富网-数据中心-特色数据-券商业绩月报

限量: 单次获取所有数据, 数据从 201006-202007, 月频率

输入参数

| 名称   | 类型  | 描述                                |
|------|-----|-----------------------------------|
| date | str | date="20200430"; 输入需要查询月份的最后一天的日期 |

输出参数

| 名称              | 类型      | 描述       |
|-----------------|---------|----------|
| 简称              | object  | -        |
| 代码              | object  | -        |
| 当月净利润-净利润       | float64 | 注意单位: 万元 |
| 当月净利润-同比增长      | float64 | -        |
| 当月净利润-环比增长      | float64 | -        |
| 当年累计净利润-累计净利润   | float64 | 注意单位: 万元 |
| 当年累计净利润-同比增长    | float64 | -        |
| 当月营业收入-营业收入     | float64 | 注意单位: 万元 |
| 当月营业收入-环比增长     | float64 | -        |
| 当月营业收入-同比增长     | float64 | -        |
| 当年累计营业收入-累计营业收入 | float64 | 注意单位: 万元 |
| 当年累计营业收入-同比增长   | float64 | -        |
| 净资产-净资产         | float64 | 注意单位: 万元 |
| 净资产-同比增长        | float64 | -        |

接口示例

```python
import akshare as ak

stock_qsjy_em_df = ak.stock_qsjy_em(date="20200430")
print(stock_qsjy_em_df)
```

#### A 股股息率

接口: stock_a_gxl_lg

目标地址: https://legulegu.com/stockdata/guxilv

描述: 乐咕乐股-股息率-A 股股息率

限量: 单次获取指定 symbol 的所有历史数据

输入参数

| 名称     | 类型  | 描述                                                      |
|--------|-----|---------------------------------------------------------|
| symbol | str | symbol="上证A股"; choice of {"上证A股", "深证A股", "创业板", "科创板"} |

输出参数

| 名称  | 类型      | 描述  |
|-----|---------|-----|
| 日期  | object  | -   |
| 股息率 | float64 | -   |

接口示例

```python
import akshare as ak

stock_a_gxl_lg_df = ak.stock_a_gxl_lg(symbol="上证A股")
print(stock_a_gxl_lg_df)
```

#### 恒生指数股息率

接口: stock_hk_gxl_lg

目标地址: https://legulegu.com/stockdata/market/hk/dv/hsi

描述: 乐咕乐股-股息率-恒生指数股息率

限量: 单次获取所有月度历史数据

输入参数

| 名称  | 类型  | 描述  |
|-----|-----|-----|
| -   | -   | -   |

输出参数

| 名称  | 类型      | 描述  |
|-----|---------|-----|
| 日期  | object  | -   |
| 股息率 | float64 | -   |

接口示例

```python
import akshare as ak

stock_hk_gxl_lg_df = ak.stock_hk_gxl_lg()
print(stock_hk_gxl_lg_df)
```

#### 大盘拥挤度

接口: stock_a_congestion_lg

目标地址: https://legulegu.com/stockdata/ashares-congestion

描述: 乐咕乐股-大盘拥挤度

限量: 单次获取近 4 年的历史数据

输入参数

| 名称  | 类型  | 描述  |
|-----|-----|-----|
| -   | -   | -   |

输出参数

| 名称         | 类型      | 描述  |
|------------|---------|-----|
| date       | object  | 日期  |
| close      | float64 | 收盘价 |
| congestion | float64 | 拥挤度 |

接口示例

```python
import akshare as ak

stock_a_congestion_lg_df = ak.stock_a_congestion_lg()
print(stock_a_congestion_lg_df)
```

#### 股债利差

接口: stock_ebs_lg

目标地址: https://legulegu.com/stockdata/equity-bond-spread

描述: 乐咕乐股-股债利差

限量: 单次所有历史数据

输入参数

| 名称  | 类型  | 描述  |
|-----|-----|-----|
| -   | -   | -   |

输出参数

| 名称      | 类型      | 描述  |
|---------|---------|-----|
| 日期      | object  | -   |
| 沪深300指数 | float64 | -   |
| 股债利差    | float64 | -   |
| 股债利差均线  | float64 | -   |

接口示例

```python
import akshare as ak

stock_ebs_lg_df = ak.stock_ebs_lg()
print(stock_ebs_lg_df)
```

#### 巴菲特指标

接口: stock_buffett_index_lg

目标地址: https://legulegu.com/stockdata/marketcap-gdp

描述: 乐估乐股-底部研究-巴菲特指标

限量: 单次获取所有历史数据

输入参数

| 名称  | 类型  | 描述  |
|-----|-----|-----|
| -   | -   | -   |

输出参数

| 名称     | 类型      | 描述                             |
|--------|---------|--------------------------------|
| 日期     | object  | 交易日                            |
| 收盘价    | float64 | -                              |
| 总市值    | float64 | A股收盘价*已发行股票总股本（A股+B股+H股）       |
| GDP    | float64 | 上年度国内生产总值（例如：2019年，则取2018年GDP） |
| 近十年分位数 | float64 | 当前"总市值/GDP"在历史数据上的分位数          |
| 总历史分位数 | float64 | 当前"总市值/GDP"在历史数据上的分位数          |

接口示例

```python
import akshare as ak

stock_buffett_index_lg_df = ak.stock_buffett_index_lg()
print(stock_buffett_index_lg_df)
```

#### A 股等权重与中位数市盈率

接口: stock_a_ttm_lyr

目标地址: https://www.legulegu.com/stockdata/a-ttm-lyr

描述: 乐咕乐股-A 股等权重市盈率与中位数市盈率

限量: 单次返回所有数据

输入参数

| 名称  | 类型  | 描述  |
|-----|-----|-----|
| -   | -   | -   |

输出参数

| 名称                                  | 类型      | 描述                               |
|-------------------------------------|---------|----------------------------------|
| date                                | object  | 日期                               |
| middlePETTM                         | float64 | 全A股滚动市盈率(TTM)中位数                 |
| averagePETTM                        | float64 | 全A股滚动市盈率(TTM)等权平均                |
| middlePELYR                         | float64 | 全A股静态市盈率(LYR)中位数                 |
| averagePELYR                        | float64 | 全A股静态市盈率(LYR)等权平均                |
| quantileInAllHistoryMiddlePeTtm     | float64 | 当前"TTM(滚动市盈率)中位数"在历史数据上的分位数      |
| quantileInRecent10YearsMiddlePeTtm  | float64 | 当前"TTM(滚动市盈率)中位数"在最近10年数据上的分位数   |
| quantileInAllHistoryAveragePeTtm    | float64 | 当前"TTM(滚动市盈率)等权平均"在历史数据上的分位数     |
| quantileInRecent10YearsAveragePeTtm | float64 | 当前"TTM(滚动市盈率)等权平均"在在最近10年数据上的分位数 |
| quantileInAllHistoryMiddlePeLyr     | float64 | 当前"LYR(静态市盈率)中位数"在历史数据上的分位数      |
| quantileInRecent10YearsMiddlePeLyr  | float64 | 当前"LYR(静态市盈率)中位数"在最近10年数据上的分位数   |
| quantileInAllHistoryAveragePeLyr    | float64 | 当前"LYR(静态市盈率)等权平均"在历史数据上的分位数     |
| quantileInRecent10YearsAveragePeLyr | float64 | 当前"LYR(静态市盈率)等权平均"在最近10年数据上的分位数  |
| close                               | float64 | 沪深300指数                          |

接口示例

```python
import akshare as ak

stock_a_ttm_lyr_df = ak.stock_a_ttm_lyr()
print(stock_a_ttm_lyr_df)
```

#### A 股等权重与中位数市净率

接口: stock_a_all_pb

目标地址: https://www.legulegu.com/stockdata/all-pb

描述: 乐咕乐股-A 股等权重与中位数市净率

限量: 单次返回所有数据

输入参数

| 名称  | 类型  | 描述 |
|-----|-----|----|
| -   | -   | -  |

输出参数

| 名称                                          | 类型      | 描述                     |
|---------------------------------------------|---------|------------------------|
| date                                        | object  | 日期                     |
| middlePB                                    | float64 | 全部A股市净率中位数             |
| equalWeightAveragePB                        | float64 | 全部A股市净率等权平均            |
| close                                       | float64 | 上证指数                   |
| quantileInAllHistoryMiddlePB                | float64 | 当前市净率中位数在历史数据上的分位数     |
| quantileInRecent10YearsMiddlePB             | float64 | 当前市净率中位数在最近10年数据上的分位数  |
| quantileInAllHistoryEqualWeightAveragePB    | float64 | 当前市净率等权平均在历史数据上的分位数    |
| quantileInRecent10YearsEqualWeightAveragePB | float64 | 当前市净率等权平均在最近10年数据上的分位数 |

接口示例

```python
import akshare as ak

stock_a_all_pb_df = ak.stock_a_all_pb()
print(stock_a_all_pb_df)
```

#### 主板市盈率

接口: stock_market_pe_lg

目标地址: https://legulegu.com/stockdata/shanghaiPE

描述: 乐咕乐股-主板市盈率

限量: 单次获取指定 symbol 的所有数据

输入参数

| 名称     | 类型  | 描述                                                |
|--------|-----|---------------------------------------------------|
| symbol | str | symbol="上证"; choice of {"上证", "深证", "创业板", "科创版"} |

输出参数-上证, 深证, 创业板

| 名称    | 类型      | 描述  |
|-------|---------|-----|
| 日期    | object  | -   |
| 指数    | float64 | -   |
| 平均市盈率 | float64 | -   |

接口示例-上证, 深证, 创业板

```python
import akshare as ak

stock_market_pe_lg_df = ak.stock_market_pe_lg(symbol="上证")
print(stock_market_pe_lg_df)
```

输出参数-科创版

| 名称  | 类型      | 描述  |
|-----|---------|-----|
| 日期  | object  | -   |
| 总市值 | float64 | -   |
| 市盈率 | float64 | -   |

接口示例-科创版

```python
import akshare as ak

stock_market_pe_lg_df = ak.stock_market_pe_lg(symbol="科创版")
print(stock_market_pe_lg_df)
```

#### 指数市盈率

接口: stock_index_pe_lg

目标地址: https://legulegu.com/stockdata/sz50-ttm-lyr

描述: 乐咕乐股-指数市盈率

限量: 单次获取指定 symbol 的所有数据

输入参数

| 名称     | 类型  | 描述                                                                                                                                  |
|--------|-----|-------------------------------------------------------------------------------------------------------------------------------------|
| symbol | str | symbol="上证50"; choice of {"上证50", "沪深300", "上证380", "创业板50", "中证500", "上证180", "深证红利", "深证100", "中证1000", "上证红利", "中证100", "中证800"} |

输出参数

| 名称       | 类型      | 描述  |
|----------|---------|-----|
| 日期       | object  | -   |
| 指数       | float64 | -   |
| 等权静态市盈率  | float64 | -   |
| 静态市盈率    | float64 | -   |
| 静态市盈率中位数 | float64 | -   |
| 等权滚动市盈率  | float64 | -   |
| 滚动市盈率    | float64 | -   |
| 滚动市盈率中位数 | float64 | -   |

接口示例

```python
import akshare as ak

stock_index_pe_lg_df = ak.stock_index_pe_lg(symbol="上证50")
print(stock_index_pe_lg_df)
```

#### 主板市净率

接口: stock_market_pb_lg

目标地址: https://legulegu.com/stockdata/shanghaiPB

描述: 乐咕乐股-主板市净率

限量: 单次获取指定 symbol 的所有数据

输入参数

| 名称     | 类型  | 描述                                                |
|--------|-----|---------------------------------------------------|
| symbol | str | symbol="上证"; choice of {"上证", "深证", "创业板", "科创版"} |

输出参数

| 名称     | 类型      | 描述  |
|--------|---------|-----|
| 日期     | object  | -   |
| 指数     | float64 | -   |
| 市净率    | float64 | -   |
| 等权市净率  | float64 | -   |
| 市净率中位数 | float64 | -   |

接口示例

```python
import akshare as ak

stock_market_pb_lg_df = ak.stock_market_pb_lg(symbol="上证")
print(stock_market_pb_lg_df)
```

#### 指数市净率

接口: stock_index_pb_lg

目标地址: https://legulegu.com/stockdata/sz50-pb

描述: 乐咕乐股-指数市净率

限量: 单次获取指定 symbol 的所有数据

输入参数

| 名称     | 类型  | 描述                                                                                                                                  |
|--------|-----|-------------------------------------------------------------------------------------------------------------------------------------|
| symbol | str | symbol="上证50"; choice of {"上证50", "沪深300", "上证380", "创业板50", "中证500", "上证180", "深证红利", "深证100", "中证1000", "上证红利", "中证100", "中证800"} |

输出参数

| 名称     | 类型      | 描述  |
|--------|---------|-----|
| 日期     | object  | -   |
| 指数     | float64 | -   |
| 市净率    | float64 | -   |
| 等权市净率  | float64 | -   |
| 市净率中位数 | float64 | -   |

接口示例

```python
import akshare as ak

stock_index_pb_lg_df = ak.stock_index_pb_lg(symbol="上证50")
print(stock_index_pb_lg_df)
```

#### A 股估值指标

接口: stock_zh_valuation_baidu

目标地址: https://gushitong.baidu.com/stock/ab-002044

描述: 百度股市通-A 股-财务报表-估值数据

限量: 单次获取指定 symbol 和 indicator 的所有历史数据

输入参数

| 名称        | 类型  | 描述                                                                     |
|-----------|-----|------------------------------------------------------------------------|
| symbol    | str | symbol="002044"; A 股代码                                                 |
| indicator | str | indicator="总市值"; choice of {"总市值", "市盈率(TTM)", "市盈率(静)", "市净率", "市现率"} |
| period    | str | period="近一年"; choice of {"近一年", "近三年", "近五年", "近十年", "全部"}             |

输出参数

| 名称    | 类型      | 描述  |
|-------|---------|-----|
| date  | object  | -   |
| value | float64 | -   |

接口示例

```python
import akshare as ak

stock_zh_valuation_baidu_df = ak.stock_zh_valuation_baidu(symbol="002044", indicator="总市值", period="近一年")
print(stock_zh_valuation_baidu_df)
```

#### 个股估值

接口: stock_value_em

目标地址: https://data.eastmoney.com/gzfx/detail/300766.html

描述: 东方财富网-数据中心-估值分析-每日互动-每日互动-估值分析

限量: 单次获取指定 symbol 的所有历史数据

输入参数

| 名称        | 类型  | 描述                                                                     |
|-----------|-----|------------------------------------------------------------------------|
| symbol    | str | symbol="002044"; A 股代码                                                 |

输出参数

| 名称      | 类型      | 描述      |
|---------|---------|---------|
| 数据日期    | object  | -       |
| 当日收盘价   | float64 | 注意单位: 元 |
| 当日涨跌幅   | float64 | 注意单位: % |
| 总市值     | float64 | 注意单位: 元 |
| 流通市值    | float64 | 注意单位: 元 |
| 总股本     | float64 | 注意单位: 股 |
| 流通股本    | float64 | -       |
| PE(TTM) | float64 | -       |
| PE(静)   | float64 | -       |
| 市净率     | float64 | -       |
| PEG值    | float64 | -       |
| 市现率     | float64 | -       |
| 市销率     | float64 | -       |

接口示例

```python
import akshare as ak

stock_value_em_df = ak.stock_value_em(symbol="300766")
print(stock_value_em_df)
```

#### 涨跌投票

接口: stock_zh_vote_baidu

目标地址: https://gushitong.baidu.com/index/ab-000001

描述: 百度股市通- A 股或指数-股评-投票

限量: 单次获取指定 symbol 和 indicator 的所有数据

输入参数

| 名称        | 类型  | 描述                                     |
|-----------|-----|----------------------------------------|
| symbol    | str | symbol="000001"; A 股股票或指数代码            |
| indicator | str | indicator="指数"; choice of {"指数", "股票"} |

输出参数

| 名称   | 类型     | 描述  |
|------|--------|-----|
| 周期   | object | -   |
| 看涨   | object | -   |
| 看跌   | object | -   |
| 看涨比例 | object | -   |
| 看跌比例 | object | -   |

接口示例

```python
import akshare as ak

stock_zh_vote_baidu_df = ak.stock_zh_vote_baidu(symbol="000001", indicator="指数")
print(stock_zh_vote_baidu_df)
```

#### 港股个股指标

P.S. 该数据源暂未更新数据

接口: stock_hk_indicator_eniu

目标地址: https://eniu.com/gu/hk01093/roe

描述: 亿牛网-港股个股指标: 市盈率, 市净率, 股息率, ROE, 市值

限量: 单次获取指定 symbol 和 indicator 的所有历史数据

输入参数

| 名称        | 类型  | 描述                                                                                              |
|-----------|-----|-------------------------------------------------------------------------------------------------|
| symbol    | str | symbol="hk01093"; 可通过调用 **ak.stock_hk_indicator_eniu(symbol="hk01093", indicator="港股")** 获取股票代码 |
| indicator | str | indicator="市盈率"; choice of {"港股", "市盈率", "市净率", "股息率", "ROE", "市值"}                             |

输出参数

| 名称  | 类型  | 描述              |
|-----|-----|-----------------|
| -   | -   | 根据 indicator 而异 |

接口示例-ROE

```python
import akshare as ak

stock_hk_indicator_eniu_df = ak.stock_hk_indicator_eniu(symbol="hk01093", indicator="市净率")
print(stock_hk_indicator_eniu_df)
```

#### 港股估值指标

接口: stock_hk_valuation_baidu

目标地址: https://gushitong.baidu.com/stock/hk-06969

描述: 百度股市通-港股-财务报表-估值数据

限量: 单次获取指定 symbol 的指定 indicator 的特定 period 的历史数据

输入参数

| 名称        | 类型  | 描述                                                                     |
|-----------|-----|------------------------------------------------------------------------|
| symbol    | str | symbol="02358"; 港股代码                                                   |
| indicator | str | indicator="总市值"; choice of {"总市值", "市盈率(TTM)", "市盈率(静)", "市净率", "市现率"} |
| period    | str | period="近一年"; choice of {"近一年", "近三年", "全部"}                           |

输出参数

| 名称    | 类型      | 描述  |
|-------|---------|-----|
| date  | object  | -   |
| value | float64 | -   |

接口示例

```python
import akshare as ak

stock_hk_valuation_baidu_df = ak.stock_hk_valuation_baidu(symbol="06969", indicator="总市值", period="近一年")
print(stock_hk_valuation_baidu_df)
```

#### 美股估值指标

接口: stock_us_valuation_baidu

目标地址: https://gushitong.baidu.com/stock/us-NVDA

描述: 百度股市通-美股-财务报表-估值数据

限量: 单次获取指定 symbol 的指定 indicator 的特定 period 的历史数据

输入参数

| 名称        | 类型  | 描述                                                                     |
|-----------|-----|------------------------------------------------------------------------|
| symbol    | str | symbol="NVDA"; 美股代码                                                    |
| indicator | str | indicator="总市值"; choice of {"总市值", "市盈率(TTM)", "市盈率(静)", "市净率", "市现率"} |
| period    | str | period="近一年"; choice of {"近一年", "近三年", "全部"}                           |

输出参数

| 名称    | 类型      | 描述  |
|-------|---------|-----|
| date  | object  | -   |
| value | float64 | -   |

接口示例

```python
import akshare as ak

stock_us_valuation_baidu_df = ak.stock_us_valuation_baidu(symbol="NVDA", indicator="总市值", period="近一年")
print(stock_us_valuation_baidu_df)
```

#### 创新高和新低的股票数量

接口: stock_a_high_low_statistics

目标地址: https://www.legulegu.com/stockdata/high-low-statistics

描述: 不同市场的创新高和新低的股票数量

限量: 单次获取指定 market 的近两年的历史数据

输入参数

| 名称     | 类型  | 描述                                                                                |
|--------|-----|-----------------------------------------------------------------------------------|
| symbol | str | symbol="all"; {"all": "全部A股", "sz50": "上证50", "hs300": "沪深300", "zz500": "中证500"} |

输出参数

| 名称      | 类型      | 描述      |
|---------|---------|---------|
| date    | object  | 交易日     |
| close   | float64 | 相关指数收盘价 |
| high20  | int64   | 20日新高   |
| low20   | int64   | 20日新低   |
| high60  | int64   | 60日新高   |
| low60   | int64   | 60日新低   |
| high120 | int64   | 120日新高  |
| low120  | int64   | 120日新低  |

接口示例

```python
import akshare as ak

stock_a_high_low_statistics_df = ak.stock_a_high_low_statistics(symbol="all")
print(stock_a_high_low_statistics_df)
```

#### 破净股统计

接口: stock_a_below_net_asset_statistics

目标地址: https://www.legulegu.com/stockdata/below-net-asset-statistics

描述: 乐咕乐股-A 股破净股统计数据

限量: 单次获取指定 symbol 的所有历史数据

输入参数

| 名称     | 类型  | 描述                                                          |
|--------|-----|-------------------------------------------------------------|
| symbol | str | symbol="全部A股"; choice of {"全部A股", "沪深300", "上证50", "中证500"} |

输出参数-全部A股

| 名称                    | 类型      | 描述    |
|-----------------------|---------|-------|
| date                  | object  | 交易日   |
| below_net_asset       | float64 | 破净股家数 |
| total_company         | float64 | 总公司数  |
| below_net_asset_ratio | float64 | 破净股比率 |

接口示例-全部 A 股

```python
import akshare as ak

stock_a_below_net_asset_statistics_df = ak.stock_a_below_net_asset_statistics(symbol="全部A股")
print(stock_a_below_net_asset_statistics_df)
```

输出参数-沪深 300

| 名称                    | 类型      | 描述    |
|-----------------------|---------|-------|
| date                  | object  | 交易日   |
| below_net_asset       | float64 | 破净股家数 |
| total_company         | float64 | 总公司数  |
| below_net_asset_ratio | float64 | 破净股比率 |

接口示例-沪深 300

```python
import akshare as ak

stock_a_below_net_asset_statistics_df = ak.stock_a_below_net_asset_statistics(symbol="沪深300")
print(stock_a_below_net_asset_statistics_df)
```

#### 基金持股

接口: stock_report_fund_hold

目标地址: http://data.eastmoney.com/zlsj/2020-06-30-1-2.html

描述: 东方财富网-数据中心-主力数据-基金持仓

限量: 单次返回指定 symbol 和 date 的所有历史数据

输入参数

| 名称     | 类型  | 描述                                                                          |
|--------|-----|-----------------------------------------------------------------------------|
| symbol | str | symbol="基金持仓"; choice of {"基金持仓", "QFII持仓", "社保持仓", "券商持仓", "保险持仓", "信托持仓"} |
| date   | str | date="20200630"; 财报发布日期, xxxx-03-31, xxxx-06-30, xxxx-09-30, xxxx-12-31     |

输出参数

| 名称     | 类型      | 描述      |
|--------|---------|---------|
| 序号     | int64   | -       |
| 股票代码   | object  | -       |
| 股票简称   | object  | -       |
| 持有基金家数 | int64   | 注意单位: 家 |
| 持股总数   | int64   | 注意单位: 股 |
| 持股市值   | float64 | 注意单位: 元 |
| 持股变化   | object  | -       |
| 持股变动数值 | int64   | 注意单位: 股 |
| 持股变动比例 | float64 | 注意单位: % |

接口示例

```python
import akshare as ak

stock_report_fund_hold_df = ak.stock_report_fund_hold(symbol="基金持仓", date="20200630")
print(stock_report_fund_hold_df)
```

#### 基金持股明细

接口: stock_report_fund_hold_detail

目标地址: http://data.eastmoney.com/zlsj/ccjj/2020-12-31-008286.html

描述: 东方财富网-数据中心-主力数据-基金持仓-基金持仓明细表

限量: 单次返回指定 symbol 和 date 的所有历史数据

输入参数

| 名称     | 类型  | 描述                                                                      |
|--------|-----|-------------------------------------------------------------------------|
| symbol | str | symbol="005827"; 基金代码                                                   |
| date   | str | date="20200630"; 财报发布日期, xxxx-03-31, xxxx-06-30, xxxx-09-30, xxxx-12-31 |

输出参数

| 名称      | 类型      | 描述      |
|---------|---------|---------|
| 序号      | int64   | -       |
| 股票代码    | object  | -       |
| 股票简称    | object  | -       |
| 持股数     | int64   | 注意单位: 股 |
| 持股市值    | float64 | 注意单位: 元 |
| 占总股本比例  | float64 | 注意单位: % |
| 占流通股本比例 | float64 | 注意单位: % |

接口示例

```python
import akshare as ak

stock_report_fund_hold_detail_df = ak.stock_report_fund_hold_detail(symbol="005827", date="20201231")
print(stock_report_fund_hold_detail_df)
```

#### 龙虎榜

##### 龙虎榜-东财

###### 龙虎榜详情

接口: stock_lhb_detail_em

目标地址: https://data.eastmoney.com/stock/tradedetail.html

描述: 东方财富网-数据中心-龙虎榜单-龙虎榜详情

限量: 单次返回所有历史数据

输入参数

| 名称         | 类型  | 描述                    |
|------------|-----|-----------------------|
| start_date | str | start_date="20220314" |
| end_date   | str | end_date="20220315"   |

输出参数

| 名称       | 类型      | 描述      |
|----------|---------|---------|
| 序号       | int64   | -       |
| 代码       | object  | -       |
| 名称       | object  | -       |
| 上榜日      | object  | -       |
| 解读       | object  | -       |
| 收盘价      | float64 | -       |
| 涨跌幅      | float64 | 注意单位: % |
| 龙虎榜净买额   | float64 | 注意单位: 元 |
| 龙虎榜买入额   | float64 | 注意单位: 元 |
| 龙虎榜卖出额   | float64 | 注意单位: 元 |
| 龙虎榜成交额   | float64 | 注意单位: 元 |
| 市场总成交额   | int64   | 注意单位: 元 |
| 净买额占总成交比 | float64 | 注意单位: % |
| 成交额占总成交比 | float64 | 注意单位: % |
| 换手率      | float64 | 注意单位: % |
| 流通市值     | float64 | 注意单位: 元 |
| 上榜原因     | object  | -       |
| 上榜后1日    | float64 | 注意单位: % |
| 上榜后2日    | float64 | 注意单位: % |
| 上榜后5日    | float64 | 注意单位: % |
| 上榜后10日   | float64 | 注意单位: % |

接口示例

```python
import akshare as ak

stock_lhb_detail_em_df = ak.stock_lhb_detail_em(start_date="20230403", end_date="20230417")
print(stock_lhb_detail_em_df)
```

###### 个股上榜统计

接口: stock_lhb_stock_statistic_em

目标地址: https://data.eastmoney.com/stock/tradedetail.html

描述: 东方财富网-数据中心-龙虎榜单-个股上榜统计

限量: 单次返回所有历史数据

输入参数

| 名称     | 类型  | 描述                                                   |
|--------|-----|------------------------------------------------------|
| symbol | str | symbol="近一月"; choice of {"近一月", "近三月", "近六月", "近一年"} |

输出参数

| 名称      | 类型      | 描述 |
|---------|---------|----|
| 序号      | int64   | -  |
| 代码      | object  | -  |
| 名称      | object  | -  |
| 最近上榜日   | object  | -  |
| 收盘价     | float64 | -  |
| 涨跌幅     | float64 | -  |
| 上榜次数    | int64   | -  |
| 龙虎榜净买额  | float64 | -  |
| 龙虎榜买入额  | float64 | -  |
| 龙虎榜卖出额  | float64 | -  |
| 龙虎榜总成交额 | float64 | -  |
| 买方机构次数  | int64   | -  |
| 卖方机构次数  | int64   | -  |
| 机构买入净额  | float64 | -  |
| 机构买入总额  | float64 | -  |
| 机构卖出总额  | float64 | -  |
| 近1个月涨跌幅 | float64 | -  |
| 近3个月涨跌幅 | float64 | -  |
| 近6个月涨跌幅 | float64 | -  |
| 近1年涨跌幅  | float64 | -  |

接口示例

```python
import akshare as ak

stock_lhb_stock_statistic_em_df = ak.stock_lhb_stock_statistic_em(symbol="近一月")
print(stock_lhb_stock_statistic_em_df)
```

###### 机构买卖每日统计

接口: stock_lhb_jgmmtj_em

目标地址: https://data.eastmoney.com/stock/jgmmtj.html

描述: 东方财富网-数据中心-龙虎榜单-机构买卖每日统计

限量: 单次返回所有历史数据

输入参数

| 名称         | 类型  | 描述                    |
|------------|-----|-----------------------|
| start_date | str | start_date="20240417" |
| end_date   | str | end_date="20240430"   |

输出参数

| 名称          | 类型      | 描述       |
|-------------|---------|----------|
| 序号          | int64   | -        |
| 代码          | object  | -        |
| 名称          | object  | -        |
| 收盘价         | float64 | -        |
| 涨跌幅         | float64 | -        |
| 买方机构数       | float64 | -        |
| 卖方机构数       | float64 | -        |
| 机构买入总额      | float64 | 注意单位: 元  |
| 机构卖出总额      | float64 | 注意单位: 元  |
| 机构买入净额      | float64 | 注意单位: 元  |
| 市场总成交额      | float64 | 注意单位: 元  |
| 机构净买额占总成交额比 | float64 | -        |
| 换手率         | float64 | -        |
| 流通市值        | float64 | 注意单位: 亿元 |
| 上榜原因        | object  | -        |
| 上榜日期        | object  | -        |

接口示例

```python
import akshare as ak

stock_lhb_jgmmtj_em_df = ak.stock_lhb_jgmmtj_em(start_date="20240417", end_date="20240430")
print(stock_lhb_jgmmtj_em_df)
```

###### 机构席位追踪

接口: stock_lhb_jgstatistic_em

目标地址: https://data.eastmoney.com/stock/jgstatistic.html

描述: 东方财富网-数据中心-龙虎榜单-机构席位追踪

限量: 单次返回所有历史数据

输入参数

| 名称     | 类型  | 描述                                                   |
|--------|-----|------------------------------------------------------|
| symbol | str | symbol="近一月"; choice of {"近一月", "近三月", "近六月", "近一年"} |

输出参数

| 名称      | 类型      | 描述      |
|---------|---------|---------|
| 序号      | int64   | -       |
| 代码      | object  | -       |
| 名称      | object  | -       |
| 收盘价     | float64 | -       |
| 涨跌幅     | float64 | 注意单位: % |
| 龙虎榜成交金额 | float64 | 注意单位: 元 |
| 上榜次数    | int64   | -       |
| 机构买入额   | float64 | 注意单位: 元 |
| 机构买入次数  | int64   | -       |
| 机构卖出额   | float64 | 注意单位: 元 |
| 机构卖出次数  | int64   | -       |
| 机构净买额   | float64 | 注意单位: 元 |
| 近1个月涨跌幅 | float64 | 注意单位: % |
| 近3个月涨跌幅 | float64 | 注意单位: % |
| 近6个月涨跌幅 | float64 | 注意单位: % |
| 近1年涨跌幅  | float64 | 注意单位: % |

接口示例

```python
import akshare as ak

stock_lhb_jgstatistic_em_df = ak.stock_lhb_jgstatistic_em(symbol="近一月")
print(stock_lhb_jgstatistic_em_df)
```

###### 每日活跃营业部

接口: stock_lhb_hyyyb_em

目标地址: https://data.eastmoney.com/stock/hyyyb.html

描述: 东方财富网-数据中心-龙虎榜单-每日活跃营业部

限量: 单次返回所有历史数据

输入参数

| 名称         | 类型  | 描述                    |
|------------|-----|-----------------------|
| start_date | str | start_date="20220311" |
| end_date   | str | end_date="20220315"   |

输出参数

| 名称    | 类型      | 描述      |
|-------|---------|---------|
| 序号    | int64   | -       |
| 营业部名称 | object  | -       |
| 上榜日   | object  | -       |
| 买入个股数 | float64 | -       |
| 卖出个股数 | float64 | -       |
| 买入总金额 | float64 | 注意单位: 元 |
| 卖出总金额 | float64 | 注意单位: 元 |
| 总买卖净额 | float64 | 注意单位: 元 |
| 买入股票  | object  | -       |

接口示例

```python
import akshare as ak

stock_lhb_hyyyb_em_df = ak.stock_lhb_hyyyb_em(start_date="20220324", end_date="20220324")
print(stock_lhb_hyyyb_em_df)
```

#### 营业部详情数据-东财

接口: stock_lhb_yyb_detail_em

目标地址: https://data.eastmoney.com/stock/lhb/yyb/10188715.html

描述: 东方财富网-数据中心-龙虎榜单-营业部历史交易明细-营业部交易明细

限量: 单次返回指定营业部的所有历史数据

输入参数

| 名称     | 类型  | 描述                                                        |
|--------|-----|-----------------------------------------------------------|
| symbol | str | symbol="10026729"; 营业部代码, 通过 ak.stock_lhb_hyyyb_em() 接口获取 |

输出参数

| 名称       | 类型      | 描述                     |
|----------|---------|------------------------|
| 序号       | int64   | -                      |
| 营业部代码    | object  | -                      |
| 营业部名称    | object  | -                      |
| 营业部简称    | object  | -                      |
| 交易日期     | object  | -                      |
| 股票代码     | object  | -                      |
| 股票名称     | object  | -                      |
| 涨跌幅      | float64 | 注意单位: %                |
| 买入金额     | float64 | 注意单位: 元                |
| 卖出金额     | float64 | 注意单位: 元                |
| 净额       | float64 | 注意单位: 元                |
| 上榜原因     | object  | -                      |
| 1日后涨跌幅   | float64 | 注意单位: %                |
| 2日后涨跌幅   | float64 | 注意单位: %                |
| 3日后涨跌幅   | float64 | 注意单位: %                |
| 5日后涨跌幅   | float64 | 注意单位: %                |
| 10日后涨跌幅  | float64 | 注意单位: %                |
| 20日后涨跌幅  | float64 | 注意单位: %                |
| 30日后涨跌幅  | float64 | 注意单位: %                |

接口示例

```python
import akshare as ak

stock_lhb_yyb_detail_em_df = ak.stock_lhb_yyb_detail_em(symbol="10188715")
print(stock_lhb_yyb_detail_em_df)
```

###### 营业部排行

接口: stock_lhb_yybph_em

目标地址: https://data.eastmoney.com/stock/yybph.html

描述: 东方财富网-数据中心-龙虎榜单-营业部排行

限量: 单次返回所有历史数据

输入参数

| 名称     | 类型  | 描述                                                   |
|--------|-----|------------------------------------------------------|
| symbol | str | symbol="近一月"; choice of {"近一月", "近三月", "近六月", "近一年"} |

输出参数

| 名称          | 类型      | 描述      |
|-------------|---------|---------|
| 序号          | int64   | -       |
| 营业部名称       | object  | -       |
| 上榜后1天-买入次数  | int64   | -       |
| 上榜后1天-平均涨幅  | float64 | 注意单位: % |
| 上榜后1天-上涨概率  | float64 | 注意单位: % |
| 上榜后2天-买入次数  | int64   | -       |
| 上榜后2天-平均涨幅  | float64 | 注意单位: % |
| 上榜后2天-上涨概率  | float64 | 注意单位: % |
| 上榜后3天-买入次数  | int64   | -       |
| 上榜后3天-平均涨幅  | float64 | 注意单位: % |
| 上榜后3天-上涨概率  | float64 | 注意单位: % |
| 上榜后4天-买入次数  | int64   | -       |
| 上榜后4天-平均涨幅  | float64 | 注意单位: % |
| 上榜后4天-上涨概率  | float64 | 注意单位: % |
| 上榜后10天-买入次数 | int64   | -       |
| 上榜后10天-平均涨幅 | float64 | 注意单位: % |
| 上榜后10天-上涨概率 | float64 | 注意单位: % |

接口示例

```python
import akshare as ak

stock_lhb_yybph_em_df = ak.stock_lhb_yybph_em(symbol="近一月")
print(stock_lhb_yybph_em_df)
```

###### 营业部统计

接口: stock_lhb_traderstatistic_em

目标地址: https://data.eastmoney.com/stock/traderstatistic.html

描述: 东方财富网-数据中心-龙虎榜单-营业部统计

限量: 单次返回所有历史数据

输入参数

| 名称     | 类型  | 描述                                                   |
|--------|-----|------------------------------------------------------|
| symbol | str | symbol="近一月"; choice of {"近一月", "近三月", "近六月", "近一年"} |

输出参数

| 名称      | 类型      | 描述      |
|---------|---------|---------|
| 序号      | int64   | -       |
| 营业部名称   | object  | -       |
| 龙虎榜成交金额 | float64 | -       |
| 上榜次数    | int64   | -       |
| 买入额     | float64 | 注意单位: 元 |
| 买入次数    | int64   | -       |
| 卖出额     | float64 | 注意单位: 元 |
| 卖出次数    | int64   | -       |

接口示例

```python
import akshare as ak

stock_lhb_traderstatistic_em_df = ak.stock_lhb_traderstatistic_em(symbol="近一月")
print(stock_lhb_traderstatistic_em_df)
```

###### 个股龙虎榜详情

接口: stock_lhb_stock_detail_em

目标地址: https://data.eastmoney.com/stock/lhb/600077.html

描述: 东方财富网-数据中心-龙虎榜单-个股龙虎榜详情

限量: 单次返回所有历史数据

输入参数

| 名称     | 类型  | 描述                                                                                            |
|--------|-----|-----------------------------------------------------------------------------------------------|
| symbol | str | symbol="600077";                                                                              |
| date   | str | date="20220310"; 需要通过 ak.stock_lhb_stock_detail_date_em(symbol="600077") 接口获取相应股票的有龙虎榜详情数据的日期 |
| flag   | str | flag="卖出";  choice of {"买入", "卖出"}                                                            |

输出参数

| 名称          | 类型      | 描述               |
|-------------|---------|------------------|
| 序号          | int64   | -                |
| 交易营业部名称     | object  | -                |
| 买入金额        | float64 | -                |
| 买入金额-占总成交比例 | float64 | -                |
| 卖出金额-占总成交比例 | float64 | -                |
| 净额          | float64 | -                |
| 类型          | object  | 该字段主要处理多种龙虎榜标准问题 |

接口示例

```python
import akshare as ak

stock_lhb_stock_detail_em_df = ak.stock_lhb_stock_detail_em(symbol="600077", date="20070416", flag="买入")
print(stock_lhb_stock_detail_em_df)
```

##### 龙虎榜-营业部排行

###### 龙虎榜-营业部排行-上榜次数最多

接口: stock_lh_yyb_most

目标地址: https://data.10jqka.com.cn/market/longhu/

描述: 龙虎榜-营业部排行-上榜次数最多

限量: 单次返回所有历史数据

输入参数

| 名称  | 类型  | 描述  |
|-----|-----|-----|
| -   | -   | -   |

输出参数

| 名称        | 类型     | 描述  |
|-----------|--------|-----|
| 序号        | int64  | -   |
| 营业部名称     | object | -   |
| 上榜次数      | int64  | -   |
| 合计动用资金    | object | -   |
| 年内上榜次数    | int64  | -   |
| 年内买入股票只数  | int64  | -   |
| 年内3日跟买成功率 | object | -   |

接口示例

```python
import akshare as ak

stock_lh_yyb_most_df = ak.stock_lh_yyb_most()
print(stock_lh_yyb_most_df)
```

###### 龙虎榜-营业部排行-资金实力最强

接口: stock_lh_yyb_capital

目标地址: https://data.10jqka.com.cn/market/longhu/

描述: 龙虎榜-营业部排行-资金实力最强

限量: 单次返回所有历史数据

输入参数

| 名称  | 类型  | 描述  |
|-----|-----|-----|
| -   | -   | -   |

输出参数

| 名称       | 类型     | 描述  |
|----------|--------|-----|
| 序号       | int64  | -   |
| 营业部名称    | object | -   |
| 今日最高操作   | int64  | -   |
| 今日最高金额   | object | -   |
| 今日最高买入金额 | object | -   |
| 累计参与金额   | object | -   |
| 累计买入金额   | object | -   |

接口示例

```python
import akshare as ak

stock_lh_yyb_capital_df = ak.stock_lh_yyb_capital()
print(stock_lh_yyb_capital_df)
```

###### 龙虎榜-营业部排行-抱团操作实力

接口: stock_lh_yyb_control

目标地址: https://data.10jqka.com.cn/market/longhu/

描述: 龙虎榜-营业部排行-抱团操作实力

限量: 单次返回所有历史数据

输入参数

| 名称  | 类型  | 描述  |
|-----|-----|-----|
| -   | -   | -   |

输出参数

| 名称        | 类型     | 描述  |
|-----------|--------|-----|
| 序号        | int64  | -   |
| 营业部名称     | object | -   |
| 携手营业部家数   | int64  | -   |
| 年内最佳携手对象  | object | -   |
| 年内最佳携手股票数 | int64  | -   |
| 年内最佳携手成功率 | object | -   |

接口示例

```python
import akshare as ak

stock_lh_yyb_control_df = ak.stock_lh_yyb_control()
print(stock_lh_yyb_control_df)
```

##### 龙虎榜-每日详情

接口: stock_lhb_detail_daily_sina

目标地址: https://vip.stock.finance.sina.com.cn/q/go.php/vInvestConsult/kind/lhb/index.phtml

描述: 新浪财经-龙虎榜-每日详情

限量: 单次返回指定 date 的所有数据

输入参数

| 名称   | 类型  | 描述                   |
|------|-----|----------------------|
| date | str | date="20240222"; 交易日 |

输出参数

| 名称   | 类型      | 描述       |
|------|---------|----------|
| 序号   | int64   | -        |
| 股票代码 | object  | -        |
| 股票名称 | object  | -        |
| 收盘价  | float64 | 注意单位: 元  |
| 对应值  | float64 | 注意单位: %  |
| 成交量  | float64 | 注意单位: 万股 |
| 成交额  | float64 | 注意单位: 万元 |
| 指标   | object  | 注意单位: 万元 |

接口示例

```python
import akshare as ak

stock_lhb_detail_daily_sina_df = ak.stock_lhb_detail_daily_sina(date="20240222")
print(stock_lhb_detail_daily_sina_df)
```

##### 龙虎榜-个股上榜统计

接口: stock_lhb_ggtj_sina

目标地址: https://vip.stock.finance.sina.com.cn/q/go.php/vLHBData/kind/ggtj/index.phtml

描述: 新浪财经-龙虎榜-个股上榜统计

限量: 单次返回指定 symbol 的所有历史数据

输入参数

| 名称     | 类型  | 描述                                                                                |
|--------|-----|-----------------------------------------------------------------------------------|
| symbol | str | symbol="5"; choice of {"5": 最近 5 天; "10": 最近 10 天; "30": 最近 30 天; "60": 最近 60 天;} |

输出参数

| 名称    | 类型      | 描述      |
|-------|---------|---------|
| 股票代码  | object  | -       |
| 股票名称  | object  | -       |
| 上榜次数  | int64   | -       |
| 累积购买额 | float64 | 注意单位: 万 |
| 累积卖出额 | float64 | 注意单位: 万 |
| 净额    | float64 | 注意单位: 万 |
| 买入席位数 | int64   | -       |
| 卖出席位数 | int64   | -       |

接口示例

```python
import akshare as ak

stock_lhb_ggtj_sina_df = ak.stock_lhb_ggtj_sina(symbol="5")
print(stock_lhb_ggtj_sina_df)
```

##### 龙虎榜-营业上榜统计

接口: stock_lhb_yytj_sina

目标地址: https://vip.stock.finance.sina.com.cn/q/go.php/vLHBData/kind/yytj/index.phtml

描述: 新浪财经-龙虎榜-营业上榜统计

限量: 单次返回指定 symbol 的所有历史数据

输入参数

| 名称     | 类型  | 描述                                                                                |
|--------|-----|-----------------------------------------------------------------------------------|
| symbol | str | symbol="5"; choice of {"5": 最近 5 天; "10": 最近 10 天; "30": 最近 30 天; "60": 最近 60 天;} |

输出参数

| 名称     | 类型      | 描述      |
|--------|---------|---------|
| 营业部名称  | object  | -       |
| 上榜次数   | int64   | -       |
| 累积购买额  | float64 | 注意单位: 万 |
| 买入席位数  | int64   | -       |
| 累积卖出额  | float64 | 注意单位: 万 |
| 卖出席位数  | int64   | -       |
| 买入前三股票 | object  | -       |

接口示例

```python
import akshare as ak

stock_lhb_yytj_sina_df = ak.stock_lhb_yytj_sina(symbol="5")
print(stock_lhb_yytj_sina_df)
```

##### 龙虎榜-机构席位追踪

接口: stock_lhb_jgzz_sina

目标地址: https://vip.stock.finance.sina.com.cn/q/go.php/vLHBData/kind/jgzz/index.phtml

描述: 新浪财经-龙虎榜-机构席位追踪

限量: 单次返回指定 symbol 的所有历史数据

输入参数

| 名称     | 类型  | 描述                                                                                |
|--------|-----|-----------------------------------------------------------------------------------|
| symbol | str | symbol="5"; choice of {"5": 最近 5 天; "10": 最近 10 天; "30": 最近 30 天; "60": 最近 60 天;} |

输出参数

| 名称    | 类型      | 描述      |
|-------|---------|---------|
| 股票代码  | object  | -       |
| 股票名称  | object  | -       |
| 累积买入额 | float64 | 注意单位: 万 |
| 买入次数  | float64 | -       |
| 累积卖出额 | float64 | 注意单位: 万 |
| 卖出次数  | float64 | -       |
| 净额    | float64 | 注意单位: 万 |

接口示例

```python
import akshare as ak

stock_lhb_jgzz_sina_df = ak.stock_lhb_jgzz_sina(symbol="5")
print(stock_lhb_jgzz_sina_df)
```

##### 龙虎榜-机构席位成交明细

接口: stock_lhb_jgmx_sina

目标地址: https://vip.stock.finance.sina.com.cn/q/go.php/vLHBData/kind/jgzz/index.phtml

描述: 新浪财经-龙虎榜-机构席位成交明细

限量: 单次返回所有历史数据

输入参数

| 名称  | 类型  | 描述  |
|-----|-----|-----|
| -   | -   | -   |

输出参数

| 名称      | 类型      | 描述      |
|---------|---------|---------|
| 股票代码    | object  | -       |
| 股票名称    | object  | -       |
| 交易日期    | object  | -       |
| 机构席位买入额 | float64 | 注意单位: 万 |
| 机构席位卖出额 | float64 | 注意单位: 万 |
| 类型      | object  | -       |

接口示例

```python
import akshare as ak

stock_lhb_jgmx_sina_df = ak.stock_lhb_jgmx_sina()
print(stock_lhb_jgmx_sina_df)
```

#### 首发申报信息

接口: stock_ipo_declare_em

目标地址: https://data.eastmoney.com/xg/xg/sbqy.html

描述: 东方财富网-数据中心-新股申购-首发申报信息-首发申报企业信息

限量: 单次返回所有历史数据

输入参数

| 名称  | 类型  | 描述  |
|-----|-----|-----|
| -   | -   | -   |

输出参数

| 名称     | 类型     | 描述 |
|--------|--------|----|
| 序号     | int64  | -  |
| 企业名称   | object | -  |
| 最新状态   | object | -  |
| 注册地    | object | -  |
| 保荐机构   | object | -  |
| 律师事务所  | object | -  |
| 会计师事务所 | object | -  |
| 拟上市地点  | object | -  |
| 更新日期   | object | -  |
| 招股说明书  | object | -  |

接口示例

```python
import akshare as ak

stock_ipo_declare_em_df = ak.stock_ipo_declare_em()
print(stock_ipo_declare_em_df)
```

#### IPO审核信息

##### 全部

接口: stock_register_all_em

目标地址: https://data.eastmoney.com/xg/ipo/

描述: 东方财富网-数据中心-新股数据-IPO审核信息-全部

限量: 单次返回所有历史数据

输入参数

| 名称  | 类型  | 描述  |
|-----|-----|-----|
| -   | -   | -   |

输出参数

| 名称     | 类型     | 描述 |
|--------|--------|----|
| 序号     | int64  | -  |
| 企业名称   | object | -  |
| 最新状态   | object | -  |
| 注册地    | object | -  |
| 行业     | object | -  |
| 保荐机构   | object | -  |
| 律师事务所  | object | -  |
| 会计师事务所 | object | -  |
| 更新日期   | object | -  |
| 受理日期   | object | -  |
| 拟上市地点  | object | -  |
| 招股说明书  | object | -  |

接口示例

```python
import akshare as ak

stock_register_all_em_df = ak.stock_register_all_em()
print(stock_register_all_em_df)
```

##### 科创板

接口: stock_register_kcb

目标地址: https://data.eastmoney.com/xg/ipo/

描述: 东方财富网-数据中心-新股数据-IPO审核信息-科创板

限量: 单次返回所有历史数据

输入参数

| 名称  | 类型  | 描述  |
|-----|-----|-----|
| -   | -   | -   |

输出参数

| 名称     | 类型     | 描述  |
|--------|--------|-----|
| 序号     | int64  | -   |
| 发行人全称  | object | -   |
| 审核状态   | object | -   |
| 注册地    | object | -   |
| 证监会行业  | object | -   |
| 保荐机构   | object | -   |
| 律师事务所  | object | -   |
| 会计师事务所 | object | -   |
| 更新日期   | object | -   |
| 受理日期   | object | -   |
| 拟上市地点  | object | -   |
| 招股说明书  | object | -   |

接口示例

```python
import akshare as ak

stock_register_kcb_df = ak.stock_register_kcb()
print(stock_register_kcb_df)
```

###### 创业板

接口: stock_register_cyb

目标地址: https://data.eastmoney.com/xg/ipo/

描述: 东方财富网-数据中心-新股数据-IPO审核信息-创业板

限量: 单次返回所有历史数据

输入参数

| 名称  | 类型  | 描述  |
|-----|-----|-----|
| -   | -   | -   |

输出参数

| 名称     | 类型     | 描述  |
|--------|--------|-----|
| 序号     | int32  | -   |
| 发行人全称  | object | -   |
| 审核状态   | object | -   |
| 注册地    | object | -   |
| 证监会行业  | object | -   |
| 保荐机构   | object | -   |
| 律师事务所  | object | -   |
| 会计师事务所 | object | -   |
| 更新日期   | object | -   |
| 受理日期   | object | -   |
| 拟上市地点  | object | -   |
| 招股说明书  | object | -   |

接口示例

```python
import akshare as ak

stock_register_cyb_df = ak.stock_register_cyb()
print(stock_register_cyb_df)
```

###### 上海主板

接口: stock_register_sh

目标地址: https://data.eastmoney.com/xg/ipo/

描述: 东方财富网-数据中心-新股数据-IPO审核信息-上海主板

限量: 单次返回所有历史数据

输入参数

| 名称  | 类型  | 描述  |
|-----|-----|-----|
| -   | -   | -   |

输出参数

| 名称     | 类型     | 描述  |
|--------|--------|-----|
| 序号     | int32  | -   |
| 发行人全称  | object | -   |
| 审核状态   | object | -   |
| 注册地    | object | -   |
| 证监会行业  | object | -   |
| 保荐机构   | object | -   |
| 律师事务所  | object | -   |
| 会计师事务所 | object | -   |
| 更新日期   | object | -   |
| 受理日期   | object | -   |
| 拟上市地点  | object | -   |
| 招股说明书  | object | -   |

接口示例

```python
import akshare as ak

stock_register_sh_df = ak.stock_register_sh()
print(stock_register_sh_df)
```

###### 深圳主板

接口: stock_register_sz

目标地址: https://data.eastmoney.com/xg/ipo/

描述: 东方财富网-数据中心-新股数据-IPO审核信息-深圳主板

限量: 单次返回所有历史数据

输入参数

| 名称  | 类型  | 描述  |
|-----|-----|-----|
| -   | -   | -   |

输出参数

| 名称     | 类型     | 描述  |
|--------|--------|-----|
| 序号     | int32  | -   |
| 发行人全称  | object | -   |
| 审核状态   | object | -   |
| 注册地    | object | -   |
| 证监会行业  | object | -   |
| 保荐机构   | object | -   |
| 律师事务所  | object | -   |
| 会计师事务所 | object | -   |
| 更新日期   | object | -   |
| 受理日期   | object | -   |
| 拟上市地点  | object | -   |
| 招股说明书  | object | -   |

接口示例

```python
import akshare as ak

stock_register_sz_df = ak.stock_register_sz()
print(stock_register_sz_df)
```

###### 北交所

接口: stock_register_bj

目标地址: https://data.eastmoney.com/xg/ipo/

描述: 东方财富网-数据中心-新股数据-IPO审核信息-北交所

限量: 单次返回所有历史数据

输入参数

| 名称  | 类型  | 描述  |
|-----|-----|-----|
| -   | -   | -   |

输出参数

| 名称     | 类型     | 描述  |
|--------|--------|-----|
| 序号     | int32  | -   |
| 发行人全称  | object | -   |
| 审核状态   | object | -   |
| 注册地    | object | -   |
| 证监会行业  | object | -   |
| 保荐机构   | object | -   |
| 律师事务所  | object | -   |
| 会计师事务所 | object | -   |
| 更新日期   | object | -   |
| 受理日期   | object | -   |
| 拟上市地点  | object | -   |
| 招股说明书  | object | -   |

接口示例

```python
import akshare as ak

stock_register_bj_df = ak.stock_register_bj()
print(stock_register_bj_df)
```

##### 达标企业

接口: stock_register_db

目标地址: https://data.eastmoney.com/xg/cyb/

描述: 东方财富网-数据中心-新股数据-注册制审核-达标企业

限量: 单次返回所有历史数据

输入参数

| 名称  | 类型  | 描述  |
|-----|-----|-----|
| -   | -   | -   |

输出参数

| 名称           | 类型      | 描述      |
|--------------|---------|---------|
| 序号           | int32   | -       |
| 企业名称         | object  | -       |
| 经营范围         | object  | -       |
| 近三年营业收入-2019 | float64 | 注意单位: 元 |
| 近三年净利润-2019  | float64 | 注意单位: 元 |
| 近三年研发费用-2019 | object  | 注意单位: 元 |
| 近三年营业收入-2018 | float64 | 注意单位: 元 |
| 近三年净利润-2018  | float64 | 注意单位: 元 |
| 近三年研发费用-2018 | object  | 注意单位: 元 |
| 近三年营业收入-2017 | object  | 注意单位: 元 |
| 近三年净利润-2017  | object  | 注意单位: 元 |
| 近三年研发费用-2017 | object  | 注意单位: 元 |
| 近两年累计净利润     | float64 | 注意单位: 元 |

接口示例

```python
import akshare as ak

stock_register_db_df = ak.stock_register_db()
print(stock_register_db_df)
```

#### 增发

接口: stock_qbzf_em

目标地址: https://data.eastmoney.com/other/gkzf.html

描述: 东方财富网-数据中心-新股数据-增发-全部增发

限量: 单次返回所有历史数据

输入参数

| 名称  | 类型  | 描述  |
|-----|-----|-----|
| -   | -   | -   |

输出参数

| 名称     | 类型      | 描述      |
|--------|---------|---------|
| 股票代码   | object  | -       |
| 股票简称   | object  | -       |
| 增发代码   | object  | -       |
| 发行方式   | object  | -       |
| 发行总数   | int64   | 注意单位: 股 |
| 网上发行   | object  | 注意单位: 股 |
| 发行价格   | float64 | -       |
| 最新价    | float64 | -       |
| 发行日期   | object  | -       |
| 增发上市日期 | object  | -       |
| 锁定期    | object  | -       |

接口示例

```python
import akshare as ak

stock_qbzf_em_df = ak.stock_qbzf_em()
print(stock_qbzf_em_df)
```

#### 配股

接口: stock_pg_em

目标地址: https://data.eastmoney.com/xg/pg/

描述: 东方财富网-数据中心-新股数据-配股

限量: 单次返回所有历史数据

输入参数

| 名称  | 类型  | 描述  |
|-----|-----|-----|
| -   | -   | -   |

输出参数

| 名称     | 类型      | 描述      |
|--------|---------|---------|
| 股票代码   | object  | -       |
| 股票简称   | object  | -       |
| 配售代码   | object  | -       |
| 配股数量   | int64   | 注意单位: 股 |
| 配股比例   | object  | -       |
| 配股价    | float64 | -       |
| 最新价    | float64 | -       |
| 配股前总股本 | int64   | 注意单位: 股 |
| 配股后总股本 | int64   | 注意单位: 股 |
| 股权登记日  | object  | -       |
| 缴款起始日期 | object  | -       |
| 缴款截止日期 | object  | -       |
| 上市日    | object  | -       |

接口示例

```python
import akshare as ak

stock_pg_em_df = ak.stock_pg_em()
print(stock_pg_em_df)
```

#### 股票回购数据

接口: stock_repurchase_em

目标地址: https://data.eastmoney.com/gphg/hglist.html

描述: 东方财富网-数据中心-股票回购-股票回购数据

限量: 单次返回所有历史数据

输入参数

| 名称  | 类型  | 描述  |
|-----|-----|-----|
| -   | -   | -   |

输出参数

| 名称             | 类型      | 描述      |
|----------------|---------|---------|
| 序号             | int64   | -       |
| 股票代码           | object  | -       |
| 股票简称           | object  | -       |
| 最新价            | float64 | -       |
| 计划回购价格区间       | float64 | 注意单位: 元 |
| 计划回购数量区间-下限    | float64 | 注意单位: 股 |
| 计划回购数量区间-上限    | float64 | 注意单位: 股 |
| 占公告前一日总股本比例-下限 | float64 | 注意单位: % |
| 占公告前一日总股本比例-上限 | float64 | 注意单位: % |
| 计划回购金额区间-下限    | float64 | 注意单位: 元 |
| 计划回购金额区间-上限    | float64 | 注意单位: 元 |
| 回购起始时间         | object  | -       |
| 实施进度           | object  | -       |
| 已回购股份价格区间-下限   | float64 | 注意单位: % |
| 已回购股份价格区间-上限   | float64 | 注意单位: % |
| 已回购股份数量        | float64 | 注意单位: 股 |
| 已回购金额          | float64 | 注意单位: 元 |
| 最新公告日期         | object  | -       |

接口示例

```python
import akshare as ak

stock_repurchase_em_df = ak.stock_repurchase_em()
print(stock_repurchase_em_df)
```

#### 股本结构

接口: stock_zh_a_gbjg_em

目标地址: https://emweb.securities.eastmoney.com/pc_hsf10/pages/index.html#/gbjg

描述: 东方财富-A股数据-股本结构

限量: 单次返回所有历史数据

输入参数

| 名称     | 类型  | 描述                 |
|--------|-----|--------------------|
| symbol | str | symbol="603392.SH" |

输出参数

| 名称          | 类型      | 描述 |
|-------------|---------|----|
| 变更日期        | object  | -  |
| 总股本         | int64   | -  |
| 流通受限股份      | float64 | -  |
| 其他内资持股(受限)  | float64 | -  |
| 境内法人持股(受限)  | float64 | -  |
| 境内自然人持股(受限) | float64 | -  |
| 已流通股份       | float64 | -  |
| 已上市流通A股     | int64   | -  |
| 变动原因        | object  | -  |

接口示例

```python
import akshare as ak

stock_zh_a_gbjg_em_df = ak.stock_zh_a_gbjg_em(symbol="603392.SH")
print(stock_zh_a_gbjg_em_df)
```

### 大宗交易

#### 市场统计

接口: stock_dzjy_sctj

目标地址: https://data.eastmoney.com/dzjy/dzjy_sctj.html

描述: 东方财富网-数据中心-大宗交易-市场统计

限量: 单次返回所有历史数据

输入参数

| 名称  | 类型  | 描述  |
|-----|-----|-----|
| -   | -   | -   |

输出参数

| 名称       | 类型      | 描述      |
|----------|---------|---------|
| 序号       | int64   | -       |
| 交易日期     | object  | -       |
| 上证指数     | float64 | -       |
| 上证指数涨跌幅  | float64 | 注意单位: % |
| 大宗交易成交总额 | float64 | 注意单位: 元 |
| 溢价成交总额   | float64 | 注意单位: 元 |
| 溢价成交总额占比 | float64 | 注意单位: % |
| 折价成交总额   | float64 | 注意单位: 元 |
| 折价成交总额占比 | float64 | 注意单位: % |

接口示例

```python
import akshare as ak

stock_dzjy_sctj_df = ak.stock_dzjy_sctj()
print(stock_dzjy_sctj_df)
```

#### 每日明细

接口: stock_dzjy_mrmx

目标地址: https://data.eastmoney.com/dzjy/dzjy_mrmx.html

描述: 东方财富网-数据中心-大宗交易-每日明细

限量: 单次返回所有历史数据

输入参数

| 名称         | 类型  | 描述                                              |
|------------|-----|-------------------------------------------------|
| symbol     | str | symbol='债券'; choice of {'A股', 'B股', '基金', '债券'} |
| start_date | str | start_date='20201123'; 开始日期                     |
| end_date   | sr  | end_date='20201204'; 结束日期                       |

输出参数-A股

| 名称       | 类型      | 描述      |
|----------|---------|---------|
| 序号       | int64   | -       |
| 交易日期     | object  | -       |
| 证券代码     | object  | -       |
| 证券简称     | object  | -       |
| 涨跌幅      | float64 | 注意单位: % |
| 收盘价      | float64 | -       |
| 成交价      | float64 | -       |
| 折溢率      | float64 | -       |
| 成交量      | float64 | 注意单位: 股 |
| 成交额      | float64 | 注意单位: 元 |
| 成交额/流通市值 | float64 | 注意单位: % |
| 买方营业部    | object  | -       |
| 卖方营业部    | object  | -       |

接口示例-A股

```python
import akshare as ak

stock_dzjy_mrmx_df = ak.stock_dzjy_mrmx(symbol='A股', start_date='20220104', end_date='20220104')
print(stock_dzjy_mrmx_df)
```

输出参数-B股

| 名称    | 类型      | 描述      |
|-------|---------|---------|
| 序号    | int64   | -       |
| 交易日期  | object  | -       |
| 证券代码  | object  | -       |
| 证券简称  | object  | -       |
| 成交价   | float64 | -       |
| 成交量   | float64 | 注意单位: 股 |
| 成交额   | float64 | 注意单位: 元 |
| 买方营业部 | object  | -       |
| 卖方营业部 | object  | -       |

接口示例-B股

```python
import akshare as ak

stock_dzjy_mrmx_df = ak.stock_dzjy_mrmx(symbol='B股', start_date='20211104', end_date='20220104')
print(stock_dzjy_mrmx_df)
```

输出参数-基金

| 名称    | 类型      | 描述      |
|-------|---------|---------|
| 序号    | int64   | -       |
| 交易日期  | object  | -       |
| 证券代码  | object  | -       |
| 证券简称  | object  | -       |
| 成交价   | float64 | -       |
| 成交量   | float64 | 注意单位: 股 |
| 成交额   | float64 | 注意单位: 元 |
| 买方营业部 | object  | -       |
| 卖方营业部 | object  | -       |

接口示例-基金

```python
import akshare as ak

stock_dzjy_mrmx_df = ak.stock_dzjy_mrmx(symbol='基金', start_date='20220104', end_date='20220104')
print(stock_dzjy_mrmx_df)
```

输出参数-债券

| 名称    | 类型      | 描述      |
|-------|---------|---------|
| 序号    | int64   | -       |
| 交易日期  | object  | -       |
| 证券代码  | object  | -       |
| 证券简称  | object  | -       |
| 成交价   | float64 | -       |
| 成交量   | float64 | 注意单位: 股 |
| 成交额   | float64 | 注意单位: 元 |
| 买方营业部 | object  | -       |
| 卖方营业部 | object  | -       |

接口示例-债券

```python
import akshare as ak

stock_dzjy_mrmx_df = ak.stock_dzjy_mrmx(symbol='债券', start_date='20220104', end_date='20220104')
print(stock_dzjy_mrmx_df)
```

#### 每日统计

接口: stock_dzjy_mrtj

目标地址: https://data.eastmoney.com/dzjy/dzjy_mrtj.html

描述: 东方财富网-数据中心-大宗交易-每日统计

限量: 单次返回所有历史数据

输入参数

| 名称         | 类型  | 描述                          |
|------------|-----|-----------------------------|
| start_date | str | start_date='20220105'; 开始日期 |
| end_date   | sr  | end_date='20220105'; 结束日期   |

输出参数

| 名称        | 类型      | 描述       |
|-----------|---------|----------|
| 序号        | int64   | -        |
| 交易日期      | object  | -        |
| 证券代码      | object  | -        |
| 证券简称      | object  | -        |
| 涨跌幅       | float64 | 注意单位: %  |
| 收盘价       | float64 | -        |
| 成交均价      | float64 | -        |
| 折溢率       | float64 | -        |
| 成交笔数      | int64   |          |
| 成交总量      | float64 | 注意单位: 万股 |
| 成交总额      | float64 | 注意单位: 万元 |
| 成交总额/流通市值 | float64 | 注意单位: %  |

接口示例

```python
import akshare as ak

stock_dzjy_mrtj_df = ak.stock_dzjy_mrtj(start_date='20220105', end_date='20220105')
print(stock_dzjy_mrtj_df)
```

#### 活跃 A 股统计

接口: stock_dzjy_hygtj

目标地址: https://data.eastmoney.com/dzjy/dzjy_hygtj.html

描述: 东方财富网-数据中心-大宗交易-活跃 A 股统计

限量: 单次返回所有历史数据

输入参数

| 名称     | 类型  | 描述                                                   |
|--------|-----|------------------------------------------------------|
| symbol | str | symbol='近三月'; choice of {'近一月', '近三月', '近六月', '近一年'} |

输出参数

| 名称            | 类型      | 描述       |
|---------------|---------|----------|
| 序号            | int64   | -        |
| 证券代码          | object  | -        |
| 证券简称          | object  | -        |
| 最新价           | float64 | -        |
| 涨跌幅           | float64 | 注意单位: %  |
| 最近上榜日         | object  | -        |
| 上榜次数-总计       | int64   | -        |
| 上榜次数-溢价       | int64   | -        |
| 上榜次数-折价       | int64   |          |
| 总成交额          | float64 | 注意单位: 万元 |
| 折溢率           | float64 | 注意单位: 万元 |
| 成交总额/流通市值     | float64 | -        |
| 上榜日后平均涨跌幅-1日  | float64 | 注意符号: %  |
| 上榜日后平均涨跌幅-5日  | float64 | 注意符号: %  |
| 上榜日后平均涨跌幅-10日 | float64 | 注意符号: %  |
| 上榜日后平均涨跌幅-20日 | float64 | 注意符号: %  |

接口示例

```python
import akshare as ak

stock_dzjy_hygtj_df = ak.stock_dzjy_hygtj(symbol='近三月')
print(stock_dzjy_hygtj_df)
```

#### 活跃营业部统计

接口: stock_dzjy_hyyybtj

目标地址: https://data.eastmoney.com/dzjy/dzjy_hyyybtj.html

描述: 东方财富网-数据中心-大宗交易-活跃营业部统计

限量: 单次返回所有历史数据

输入参数

| 名称     | 类型  | 描述                                                              |
|--------|-----|-----------------------------------------------------------------|
| symbol | str | symbol='近3日'; choice of {'当前交易日', '近3日', '近5日', '近10日', '近30日'} |

输出参数

| 名称          | 类型      | 描述       |
|-------------|---------|----------|
| 序号          | int64   | -        |
| 营业部名称       | str     | -        |
| 最近上榜日       | object  | -        |
| 次数总计-买入     | float64 | -        |
| 次数总计-卖出     | float64 | 注意单位: %  |
| 成交金额统计-买入   | float64 | 注意单位: 万元 |
| 成交金额统计-卖出   | float64 | 注意单位: 万元 |
| 成交金额统计-净买入额 | float64 | 注意单位: 万元 |
| 买入的股票       | object  |          |

接口示例

```python
import akshare as ak

stock_dzjy_hyyybtj_df = ak.stock_dzjy_hyyybtj(symbol='近3日')
print(stock_dzjy_hyyybtj_df)
```

#### 营业部排行

接口: stock_dzjy_yybph

目标地址: https://data.eastmoney.com/dzjy/dzjy_yybph.html

描述: 东方财富网-数据中心-大宗交易-营业部排行

限量: 单次返回所有历史数据

输入参数

| 名称     | 类型  | 描述                                                   |
|--------|-----|------------------------------------------------------|
| symbol | str | symbol='近三月'; choice of {'近一月', '近三月', '近六月', '近一年'} |

输出参数

| 名称          | 类型      | 描述      |
|-------------|---------|---------|
| 序号          | int64   | -       |
| 营业部名称       | object  | -       |
| 上榜后1天-买入次数  | float64 | -       |
| 上榜后1天-平均涨幅  | float64 | 注意单位: % |
| 上榜后1天-上涨概率  | float64 | -       |
| 上榜后5天-买入次数  | float64 | -       |
| 上榜后5天-平均涨幅  | float64 | 注意单位: % |
| 上榜后5天-上涨概率  | float64 | -       |
| 上榜后10天-买入次数 | float64 | -       |
| 上榜后10天-平均涨幅 | float64 | 注意单位: % |
| 上榜后10天-上涨概率 | float64 |         |
| 上榜后20天-买入次数 | float64 | -       |
| 上榜后20天-平均涨幅 | float64 | 注意单位: % |
| 上榜后20天-上涨概率 | float64 |         |

接口示例

```python
import akshare as ak

stock_dzjy_yybph_df = ak.stock_dzjy_yybph(symbol='近三月')
print(stock_dzjy_yybph_df)
```

### 一致行动人

接口: stock_yzxdr_em

目标地址: http://data.eastmoney.com/yzxdr/

描述: 东方财富网-数据中心-特色数据-一致行动人

限量: 单次返回所有历史数据

输入参数

| 名称   | 类型  | 描述                         |
|------|-----|----------------------------|
| date | str | date="20200930"; 每年的季度末时间点 |

输出参数

| 名称     | 类型      | 描述      |
|--------|---------|---------|
| 序号     | int64   | -       |
| 股票代码   | object  | -       |
| 股票简称   | object  | -       |
| 一致行动人  | object  | -       |
| 股东排名   | object  | -       |
| 持股数量   | int64   | -       |
| 持股比例   | float64 | -       |
| 持股数量变动 | object  | 注意单位: % |
| 行业     | object  | -       |
| 公告日期   | object  | -       |

接口示例

```python
import akshare as ak

stock_yzxdr_em_df = ak.stock_yzxdr_em(date="20210331")
print(stock_yzxdr_em_df)
```

### 融资融券

#### 标的证券名单及保证金比例查询

接口: stock_margin_ratio_pa

目标地址: https://stock.pingan.com/static/webinfo/margin/business.html?businessType=0

描述: 融资融券-标的证券名单及保证金比例查询

限量: 单次返回指定交易所和交易日的所有历史数据

输入参数

| 名称     | 类型  | 描述                                         |
|--------|-----|--------------------------------------------|
| symbol | str | symbol="深市"; choice of {"深市", "沪市", "北交所"} |
| date   | str | date="20260113"                            |

输出参数

| 名称   | 类型      | 描述 |
|------|---------|----|
| 证券代码 | object  | -  |
| 证券简称 | object  | -  |
| 融资比例 | float64 | -  |
| 融券比例 | float64 | -  |

接口示例

```python
import akshare as ak

stock_margin_ratio_pa_df = ak.stock_margin_ratio_pa(symbol="沪市", date="20260113")
print(stock_margin_ratio_pa_df)
```

#### 两融账户信息

接口: stock_margin_account_info

目标地址: https://data.eastmoney.com/rzrq/zhtjday.html

描述: 东方财富网-数据中心-融资融券-融资融券账户统计-两融账户信息

限量: 单次返回所有历史数据

输入参数

| 名称 | 类型 | 描述 |
|----|----|----|
| -  | -  | -  |

输出参数

| 名称            | 类型      | 描述       |
|---------------|---------|----------|
| 日期            | object  | -        |
| 融资余额          | float64 | 注意单位: 亿  |
| 融券余额          | float64 | 注意单位: 亿  |
| 融资买入额         | float64 | 注意单位: 亿  |
| 融券卖出额         | float64 | 注意单位: 亿  |
| 证券公司数量        | float64 | 注意单位: 家  |
| 营业部数量         | float64 | 注意单位: 家  |
| 个人投资者数量       | float64 | 注意单位: 万名 |
| 机构投资者数量       | float64 | 注意单位: 家  |
| 参与交易的投资者数量    | float64 | 注意单位: 名  |
| 有融资融券负债的投资者数量 | float64 | 注意单位: 名  |
| 担保物总价值        | float64 | 注意单位: 亿  |
| 平均维持担保比例      | float64 | 注意单位: %  |

接口示例

```python
import akshare as ak

stock_margin_account_info_df = ak.stock_margin_account_info()
print(stock_margin_account_info_df)
```

#### 上海证券交易所

##### 融资融券汇总

接口: stock_margin_sse

目标地址: http://www.sse.com.cn/market/othersdata/margin/sum/

描述: 上海证券交易所-融资融券数据-融资融券汇总数据

限量: 单次返回指定时间段内的所有历史数据

输入参数

| 名称         | 类型  | 描述                    |
|------------|-----|-----------------------|
| start_date | str | start_date="20010106" |
| end_date   | str | end_date="20010106"   |

输出参数

| 名称     | 类型     | 描述      |
|--------|--------|---------|
| 信用交易日期 | object | -       |
| 融资余额   | int64  | 注意单位: 元 |
| 融资买入额  | int64  | 注意单位: 元 |
| 融券余量   | int64  | -       |
| 融券余量金额 | int64  | 注意单位: 元 |
| 融券卖出量  | int64  | -       |
| 融资融券余额 | int64  | 注意单位: 元 |

接口示例

```python
import akshare as ak

stock_margin_sse_df = ak.stock_margin_sse(start_date="20010106", end_date="20210208")
print(stock_margin_sse_df)
```

##### 融资融券明细

接口: stock_margin_detail_sse

目标地址: http://www.sse.com.cn/market/othersdata/margin/detail/

描述: 上海证券交易所-融资融券数据-融资融券明细数据

限量: 单次返回交易日的所有历史数据

输入参数

| 名称   | 类型  | 描述              |
|------|-----|-----------------|
| date | str | date="20210205" |

输出参数

| 名称     | 类型     | 描述      |
|--------|--------|---------|
| 信用交易日期 | object | -       |
| 标的证券代码 | object | -       |
| 标的证券简称 | object | -       |
| 融资余额   | int64  | 注意单位: 元 |
| 融资买入额  | int64  | 注意单位: 元 |
| 融资偿还额  | int64  | 注意单位: 元 |
| 融券余量   | int64  | -       |
| 融券卖出量  | int64  | -       |
| 融券偿还量  | int64  | -       |

接口示例

```python
import akshare as ak

stock_margin_detail_sse_df = ak.stock_margin_detail_sse(date="20230922")
print(stock_margin_detail_sse_df)
```

#### 深圳证券交易所

##### 融资融券汇总

接口: stock_margin_szse

目标地址: https://www.szse.cn/disclosure/margin/margin/index.html

描述: 深圳证券交易所-融资融券数据-融资融券汇总数据

限量: 单次返回指定时间内的所有历史数据

输入参数

| 名称   | 类型  | 描述                    |
|------|-----|-----------------------|
| date | str | date="20240411"; 交易日期 |

输出参数

| 名称     | 类型      | 描述          |
|--------|---------|-------------|
| 融资买入额  | float64 | 注意单位: 亿元    |
| 融资余额   | float64 | 注意单位: 亿元    |
| 融券卖出量  | float64 | 注意单位: 亿股/亿份 |
| 融券余量   | float64 | 注意单位: 亿股/亿份 |
| 融券余额   | float64 | 注意单位: 亿元    |
| 融资融券余额 | float64 | 注意单位: 亿元    |

接口示例

```python
import akshare as ak

stock_margin_sse_df = ak.stock_margin_szse(date="20240411")
print(stock_margin_sse_df)
```

##### 融资融券明细

接口: stock_margin_detail_szse

目标地址: https://www.szse.cn/disclosure/margin/margin/index.html

描述: 深证证券交易所-融资融券数据-融资融券交易明细数据

限量: 单次返回指定 date 的所有历史数据

输入参数

| 名称   | 类型  | 描述              |
|------|-----|-----------------|
| date | str | date="20220118" |

输出参数

| 名称     | 类型     | 描述        |
|--------|--------|-----------|
| 证券代码   | object | -         |
| 证券简称   | object | -         |
| 融资买入额  | int64  | 注意单位: 元   |
| 融资余额   | int64  | 注意单位: 元   |
| 融券卖出量  | int64  | 注意单位: 股/份 |
| 融券余量   | int64  | 注意单位: 股/份 |
| 融券余额   | int64  | 注意单位: 元   |
| 融资融券余额 | int64  | 注意单位: 元   |

接口示例

```python
import akshare as ak

stock_margin_detail_sse_df = ak.stock_margin_detail_szse(date="20230925")
print(stock_margin_detail_sse_df)
```

##### 标的证券信息

接口: stock_margin_underlying_info_szse

目标地址: https://www.szse.cn/disclosure/margin/object/index.html

描述: 深圳证券交易所-融资融券数据-标的证券信息

限量: 单次返回交易日的所有历史数据

输入参数

| 名称   | 类型  | 描述              |
|------|-----|-----------------|
| date | str | date="20210205" |

输出参数

| 名称       | 类型     | 描述  |
|----------|--------|-----|
| 证券代码     | object | -   |
| 证券简称     | object | -   |
| 融资标的     | object | -   |
| 融券标的     | object | -   |
| 当日可融资    | object | -   |
| 当日可融券    | object | -   |
| 融券卖出价格限制 | object | -   |
| 涨跌幅限制    | object | -   |

接口示例

```python
import akshare as ak

stock_margin_underlying_info_szse_df = ak.stock_margin_underlying_info_szse(date="20210727")
print(stock_margin_underlying_info_szse_df)
```

### 盈利预测-东方财富

接口: stock_profit_forecast_em

目标地址: http://data.eastmoney.com/report/profitforecast.jshtml

描述: 东方财富网-数据中心-研究报告-盈利预测; 该数据源网页端返回数据有异常, 本接口已修复该异常

限量: 单次返回指定 symbol 的数据

输入参数

| 名称     | 类型  | 描述                                                                                                 |
|--------|-----|----------------------------------------------------------------------------------------------------|
| symbol | str | symbol="", 默认为获取全部数据; symbol="船舶制造", 则获取具体行业板块的数据; 行业板块可以通过 ak.stock_board_industry_name_em() 接口获取 |

输出参数

| 名称              | 类型      | 描述  |
|-----------------|---------|-----|
| 序号              | int64   | -   |
| 代码              | object  | -   |
| 名称              | object  | -   |
| 研报数             | int64   | -   |
| 机构投资评级(近六个月)-买入 | float64 | -   |
| 机构投资评级(近六个月)-增持 | float64 | -   |
| 机构投资评级(近六个月)-中性 | float64 | -   |
| 机构投资评级(近六个月)-减持 | int64   | -   |
| 机构投资评级(近六个月)-卖出 | int64   | -   |
| xxxx预测每股收益      | float64 | -   |
| xxxx预测每股收益      | float64 | -   |
| xxxx预测每股收益      | float64 | -   |
| xxxx预测每股收益      | float64 | -   |

接口示例

```python
import akshare as ak

stock_profit_forecast_em_df = ak.stock_profit_forecast_em()
print(stock_profit_forecast_em_df)
```

### 港股盈利预测-经济通

接口: stock_hk_profit_forecast_et

目标地址: https://www.etnet.com.hk/www/sc/stocks/realtime/quote_profit.php?code=9999

描述: 经济通-公司资料-盈利预测

限量: 单次返回指定 symbol 和 indicator 的数据

输入参数

| 名称        | 类型  | 描述                                                                    |
|-----------|-----|-----------------------------------------------------------------------|
| symbol    | str | symbol="09999"                                                        |
| indicator | str | indicator="盈利预测概览"; choice of {"评级总览", "去年度业绩表现", "综合盈利预测", "盈利预测概览"} |

输出参数-盈利预测概览

| 名称    | 类型      | 描述               |
|-------|---------|------------------|
| 财政年度  | object  | -                |
| 纯利/亏损 | float64 | 注意单位：百万元人民币/百万港元 |
| 每股盈利  | float64 | 注意单位：分/港仙        |
| 每股派息  | float64 | 注意单位：分/港仙        |
| 证券商   | object  | -                |
| 评级    | object  | -                |
| 目标价   | float64 | 注意单位：港元          |
| 更新日期  | object  | -                |

接口示例-盈利预测概览

```python
import akshare as ak

stock_hk_profit_forecast_et_df = ak.stock_hk_profit_forecast_et(symbol="09999", indicator="盈利预测概览")
print(stock_hk_profit_forecast_et_df)
```

### 盈利预测-同花顺

接口: stock_profit_forecast_ths

目标地址: http://basic.10jqka.com.cn/new/600519/worth.html

描述: 同花顺-盈利预测

限量: 单次返回指定 symbol 和 indicator 的数据

输入参数

| 名称        | 类型  | 描述                                                                                    |
|-----------|-----|---------------------------------------------------------------------------------------|
| symbol    | str | symbol="600519"; 股票代码                                                                 |
| indicator | str | indicator="预测年报每股收益"; choice of {"预测年报每股收益", "预测年报净利润", "业绩预测详表-机构", "业绩预测详表-详细指标预测"} |

输出参数-预测年报每股收益

| 名称    | 类型      | 描述  |
|-------|---------|-----|
| 年度    | object  | -   |
| 预测机构数 | int64   | -   |
| 最小值   | float64 | -   |
| 均值    | float64 | -   |
| 最大值   | float64 | -   |
| 行业平均数 | float64 | -   |

接口示例-预测年报每股收益

```python
import akshare as ak

stock_profit_forecast_ths_df = ak.stock_profit_forecast_ths(symbol="600519", indicator="预测年报每股收益")
print(stock_profit_forecast_ths_df)
```

输出参数-预测年报净利润

| 名称    | 类型      | 描述  |
|-------|---------|-----|
| 年度    | object  | -   |
| 预测机构数 | int64   | -   |
| 最小值   | float64 | -   |
| 均值    | float64 | -   |
| 最大值   | float64 | -   |
| 行业平均数 | float64 | -   |

接口示例-预测年报净利润

```python
import akshare as ak

stock_profit_forecast_ths_df = ak.stock_profit_forecast_ths(symbol="600519", indicator="预测年报净利润")
print(stock_profit_forecast_ths_df)
```

输出参数-业绩预测详表-机构

| 名称             | 类型      | 描述  |
|----------------|---------|-----|
| 机构名称           | object  | -   |
| 研究员            | object  | -   |
| 预测年报每股收益2022预测 | float64 | -   |
| 预测年报每股收益2023预测 | float64 | -   |
| 预测年报每股收益2024预测 | float64 | -   |
| 预测年报净利润2022预测  | object  | -   |
| 预测年报净利润2023预测  | object  | -   |
| 预测年报净利润2024预测  | object  | -   |
| 报告日期           | object  | -   |

接口示例-业绩预测详表-机构

```python
import akshare as ak

stock_profit_forecast_ths_df = ak.stock_profit_forecast_ths(symbol="600519", indicator="业绩预测详表-机构")
print(stock_profit_forecast_ths_df)
```

输出参数-业绩预测详表-详细指标预测

| 名称        | 类型     | 描述  |
|-----------|--------|-----|
| 预测指标      | object | -   |
| 2019-实际值  | object | -   |
| 2020-实际值  | object | -   |
| 2021-实际值  | object | -   |
| 预测2022-平均 | object | -   |
| 预测2023-平均 | object | -   |
| 预测2024-平均 | object | -   |

接口示例-业绩预测详表-详细指标预测

```python
import akshare as ak

stock_profit_forecast_ths_df = ak.stock_profit_forecast_ths(symbol="600519", indicator="业绩预测详表-详细指标预测")
print(stock_profit_forecast_ths_df)
```

### 概念板块

#### 同花顺-概念板块指数

接口: stock_board_concept_index_ths

目标地址: https://q.10jqka.com.cn/gn/detail/code/301558

描述: 同花顺-板块-概念板块-指数日频率数据

限量: 单次返回所有日频指数数据

输入参数

| 名称         | 类型  | 描述                                                                         |
|------------|-----|----------------------------------------------------------------------------|
| symbol     | str | symbol="阿里巴巴概念"; 可以通过调用 **ak.stock_board_concept_name_ths()** 查看同花顺的所有概念名称 |
| start_date | str | start_date="20200101"; 开始时间                                                |
| end_date   | str | end_date="20250228"; 结束时间                                                  |

输出参数

| 名称  | 类型      | 描述  |
|-----|---------|-----|
| 日期  | object  | -   |
| 开盘价 | float64 | -   |
| 最高价 | float64 | -   |
| 最低价 | float64 | -   |
| 收盘价 | float64 | -   |
| 成交量 | int64   | -   |
| 成交额 | float64 | -   |

接口示例

```python
import akshare as ak

stock_board_concept_index_ths_df = ak.stock_board_concept_index_ths(symbol="阿里巴巴概念", start_date="20200101", end_date="20250321")
print(stock_board_concept_index_ths_df)
```

#### 同花顺-概念板块简介

接口: stock_board_concept_info_ths

目标地址: http://q.10jqka.com.cn/gn/detail/code/301558/

描述: 同花顺-板块-概念板块-板块简介

限量: 单次返回所有数据

输入参数

| 名称     | 类型  | 描述                                                                                |
|--------|-----|-----------------------------------------------------------------------------------|
| symbol | str | symbol: str = "阿里巴巴概念"; 可以通过调用 **ak.stock_board_concept_name_ths()** 查看同花顺的所有概念名称 |

输出参数

| 名称 | 类型      | 描述 |
|----|---------|----|
| 项目 | object  | -  |
| 值  | float64 | -  |

接口示例

```python
import akshare as ak

stock_board_concept_info_ths_df = ak.stock_board_concept_info_ths(symbol="阿里巴巴概念")
print(stock_board_concept_info_ths_df)
```

#### 东方财富-概念板块

接口: stock_board_concept_name_em

目标地址: https://quote.eastmoney.com/center/boardlist.html#concept_board

描述: 东方财富网-行情中心-沪深京板块-概念板块

限量: 单次返回当前时刻所有概念板块的实时行情数据

输入参数

| 名称  | 类型  | 描述  |
|-----|-----|-----|
| -   | -   | -   |

输出参数

| 名称       | 类型      | 描述     |
|----------|---------|--------|
| 排名       | int64   | -      |
| 板块名称     | object  | -      |
| 板块代码     | object  | -      |
| 最新价      | float64 | -      |
| 涨跌额      | float64 | -      |
| 涨跌幅      | float64 | 注意单位：% |
| 总市值      | int64   | -      |
| 换手率      | float64 | 注意单位：% |
| 上涨家数     | int64   | -      |
| 下跌家数     | int64   | -      |
| 领涨股票     | object  | -      |
| 领涨股票-涨跌幅 | float64 | 注意单位：% |

接口示例

```python
import akshare as ak

stock_board_concept_name_em_df = ak.stock_board_concept_name_em()
print(stock_board_concept_name_em_df)
```

#### 东方财富-概念板块-实时行情

接口: stock_board_concept_spot_em

目标地址: https://quote.eastmoney.com/bk/90.BK0818.html

描述: 东方财富网-行情中心-沪深京板块-概念板块-实时行情

限量: 单次返回指定概念板块的实时行情数据

输入参数

| 名称  | 类型  | 描述  |
|-----|-----|-----|
| -   | -   | -   |

输出参数

| 名称    | 类型      | 描述 |
|-------|---------|----|
| item  | object  | -  |
| value | float64 | -  |

接口示例

```python
import akshare as ak

stock_board_concept_spot_em_df = ak.stock_board_concept_spot_em(symbol="可燃冰")
print(stock_board_concept_spot_em_df)
```

#### 东方财富-成份股

接口: stock_board_concept_cons_em

目标地址: http://quote.eastmoney.com/center/boardlist.html#boards-BK06551

描述: 东方财富-沪深板块-概念板块-板块成份

限量: 单次返回当前时刻所有成份股

输入参数

| 名称     | 类型  | 描述                                                                                              |
|--------|-----|-------------------------------------------------------------------------------------------------|
| symbol | str | symbol="融资融券"; 支持传入板块代码比如：BK0655，可以通过调用 **ak.stock_board_concept_name_em()** 查看东方财富-概念板块的所有行业名称 |

输出参数

| 名称     | 类型      | 描述      |
|--------|---------|---------|
| 序号     | int64   | -       |
| 代码     | object  | -       |
| 名称     | object  | -       |
| 最新价    | float64 | -       |
| 涨跌幅    | float64 | 注意单位: % |
| 涨跌额    | float64 | -       |
| 成交量    | float64 | 注意单位: 手 |
| 成交额    | float64 | -       |
| 振幅     | float64 | 注意单位: % |
| 最高     | float64 | -       |
| 最低     | float64 | -       |
| 今开     | float64 | -       |
| 昨收     | float64 | -       |
| 换手率    | float64 | 注意单位: % |
| 市盈率-动态 | float64 | -       |
| 市净率    | float64 | -       |

接口示例

```python
import akshare as ak

stock_board_concept_cons_em_df = ak.stock_board_concept_cons_em(symbol="融资融券")
print(stock_board_concept_cons_em_df)
```

#### 东方财富-指数

接口: stock_board_concept_hist_em

目标地址: http://quote.eastmoney.com/bk/90.BK0715.html

描述: 东方财富-沪深板块-概念板块-历史行情数据

限量: 单次返回指定 symbol 和 adjust 的历史数据

输入参数

| 名称         | 类型  | 描述                                                                            |
|------------|-----|-------------------------------------------------------------------------------|
| symbol     | str | symbol="绿色电力"; 可以通过调用 **ak.stock_board_concept_name_em()** 查看东方财富-概念板块的所有概念代码 |
| period     | str | period="daily"; choice of {"daily", "weekly", "monthly"}                      |
| start_date | str | start_date="20220101"                                                         |
| end_date   | str | end_date="20221128"                                                           |
| adjust     | str | adjust=""; choice of {'': 不复权, 默认; "qfq": 前复权, "hfq": 后复权}                    |

输出参数

| 名称  | 类型      | 描述      |
|-----|---------|---------|
| 日期  | object  | -       |
| 开盘  | float64 | -       |
| 收盘  | float64 | -       |
| 最高  | float64 | -       |
| 最低  | float64 | -       |
| 涨跌幅 | float64 | 注意单位: % |
| 涨跌额 | float64 | -       |
| 成交量 | int64   | -       |
| 成交额 | float64 | -       |
| 振幅  | float64 | 注意单位: % |
| 换手率 | float64 | 注意单位: % |

接口示例

```python
import akshare as ak

stock_board_concept_hist_em_df = ak.stock_board_concept_hist_em(symbol="绿色电力", period="daily", start_date="20220101", end_date="20250227", adjust="")
print(stock_board_concept_hist_em_df)
```

#### 东方财富-指数-分时

接口: stock_board_concept_hist_min_em

目标地址: http://quote.eastmoney.com/bk/90.BK0715.html

描述: 东方财富-沪深板块-概念板块-分时历史行情数据

限量: 单次返回指定 symbol 和 period 的历史数据

输入参数

| 名称     | 类型  | 描述                                                                           |
|--------|-----|------------------------------------------------------------------------------|
| symbol | str | symbol="长寿药"; 可以通过调用 **ak.stock_board_concept_name_em()** 查看东方财富-概念板块的所有概念代码 |
| period | str | period="5"; choice of {"1", "5", "15", "30", "60"}                           |

输出参数-1分钟

| 名称   | 类型      | 描述 |
|------|---------|----|
| 日期时间 | object  | -  |
| 开盘   | float64 | -  |
| 收盘   | float64 | -  |
| 最高   | float64 | -  |
| 最低   | float64 | -  |
| 成交量  | int64   | -  |
| 成交额  | float64 | -  |
| 最新价  | float64 | -  |

接口示例-1分钟

```python
import akshare as ak

stock_board_concept_hist_min_em_df = ak.stock_board_concept_hist_min_em(symbol="长寿药", period="1")
print(stock_board_concept_hist_min_em_df)
```

输出参数-其他

| 名称   | 类型      | 描述      |
|------|---------|---------|
| 日期时间 | object  | -       |
| 开盘   | float64 | -       |
| 收盘   | float64 | -       |
| 最高   | float64 | -       |
| 最低   | float64 | -       |
| 涨跌幅  | float64 | 注意单位: % |
| 涨跌额  | float64 | -       |
| 成交量  | int64   | -       |
| 成交额  | float64 | -       |
| 振幅   | float64 | 注意单位: % |
| 换手率  | float64 | 注意单位: % |

接口示例-其他

```python
import akshare as ak

stock_board_concept_hist_min_em_df = ak.stock_board_concept_hist_min_em(symbol="长寿药", period="5")
print(stock_board_concept_hist_min_em_df)
```

#### 富途牛牛-美股概念-成分股

接口: stock_concept_cons_futu

目标地址: https://www.futunn.com/quote/sparks-us

描述: 富途牛牛-主题投资-概念板块-成分股

限量: 单次返回指定概念板块成分股数据

输入参数

| 名称     | 类型  | 描述                                                      |
|--------|-----|---------------------------------------------------------|
| symbol | str | symbol="特朗普概念股"; choice of {"巴菲特持仓", "佩洛西持仓", "特朗普概念股"} |

输出参数

| 名称   | 类型      | 描述 |
|------|---------|----|
| 代码   | object  | -  |
| 股票名称 | object  | -  |
| 最新价  | float64 | -  |
| 涨跌额  | float64 | -  |
| 涨跌幅  | object  | -  |
| 成交量  | object  | -  |
| 成交额  | object  | -  |

接口示例

```python
import akshare as ak

stock_concept_cons_futu_df = ak.stock_concept_cons_futu(symbol="特朗普概念股")
print(stock_concept_cons_futu_df)
```

### 行业板块

#### 同花顺-同花顺行业一览表

接口: stock_board_industry_summary_ths

目标地址: https://q.10jqka.com.cn/thshy/

描述: 同花顺-同花顺行业一览表

限量: 单次返回当前时刻同花顺行业一览表

输入参数

| 名称  | 类型  | 描述  |
|-----|-----|-----|
| -   | -   | -   |

输出参数

| 名称      | 类型      | 描述       |
|---------|---------|----------|
| 序号      | int64   | -        |
| 板块      | object  | -        |
| 涨跌幅     | object  | 注意单位: %  |
| 总成交量    | float64 | 注意单位: 万手 |
| 总成交额    | float64 | 注意单位: 亿元 |
| 净流入     | float64 | 注意单位: 亿元 |
| 上涨家数    | float64 | -        |
| 下跌家数    | float64 | -        |
| 均价      | float64 | -        |
| 领涨股     | float64 | -        |
| 领涨股-最新价 | object  | -        |
| 领涨股-涨跌幅 | object  | 注意单位: %  |

接口示例

```python
import akshare as ak

stock_board_industry_summary_ths_df = ak.stock_board_industry_summary_ths()
print(stock_board_industry_summary_ths_df)
```

#### 同花顺-指数

接口: stock_board_industry_index_ths

目标地址: https://q.10jqka.com.cn/thshy/detail/code/881270/

描述: 同花顺-板块-行业板块-指数日频率数据

限量: 单次返回所有日频指数数据

输入参数

| 名称         | 类型  | 描述                                                                      |
|------------|-----|-------------------------------------------------------------------------|
| symbol     | str | symbol="元件"; 可以通过调用 **ak.stock_board_industry_name_ths()** 查看同花顺的所有行业名称 |
| start_date | str | start_date="20200101"; 开始时间                                             |
| end_date   | str | end_date="20211027"; 结束时间                                               |

输出参数

| 名称  | 类型      | 描述  |
|-----|---------|-----|
| 日期  | object  | -   |
| 开盘价 | float64 | -   |
| 最高价 | float64 | -   |
| 最低价 | float64 | -   |
| 收盘价 | float64 | -   |
| 成交量 | int64   | -   |
| 成交额 | float64 | -   |

接口示例

```python
import akshare as ak

stock_board_industry_index_ths_df = ak.stock_board_industry_index_ths(symbol="元件", start_date="20240101", end_date="20240718")
print(stock_board_industry_index_ths_df)
```

#### 东方财富-行业板块

接口: stock_board_industry_name_em

目标地址: https://quote.eastmoney.com/center/boardlist.html#industry_board

描述: 东方财富-沪深京板块-行业板块

限量: 单次返回当前时刻所有行业板的实时行情数据

输入参数

| 名称  | 类型  | 描述  |
|-----|-----|-----|
| -   | -   | -   |

输出参数

| 名称       | 类型      | 描述     |
|----------|---------|--------|
| 排名       | int64   | -      |
| 板块名称     | object  | -      |
| 板块代码     | object  | -      |
| 最新价      | float64 | -      |
| 涨跌额      | float64 | -      |
| 涨跌幅      | float64 | 注意单位：% |
| 总市值      | int64   | -      |
| 换手率      | float64 | 注意单位：% |
| 上涨家数     | int64   | -      |
| 下跌家数     | int64   | -      |
| 领涨股票     | object  | -      |
| 领涨股票-涨跌幅 | float64 | 注意单位：% |

接口示例

```python
import akshare as ak

stock_board_industry_name_em_df = ak.stock_board_industry_name_em()
print(stock_board_industry_name_em_df)
```

#### 东方财富-行业板块-实时行情

接口: stock_board_industry_spot_em

目标地址: https://quote.eastmoney.com/bk/90.BK1027.html

描述: 东方财富网-沪深板块-行业板块-实时行情

限量: 单次返回指定板块的实时行情数据

输入参数

| 名称     | 类型  | 描述           |
|--------|-----|--------------|
| symbol | str | symbol="小金属" |

输出参数

| 名称    | 类型      | 描述 |
|-------|---------|----|
| item  | object  | -  |
| value | float64 | -  |

接口示例

```python
import akshare as ak

stock_board_industry_spot_em_df = ak.stock_board_industry_spot_em(symbol="小金属")
print(stock_board_industry_spot_em_df)
```

#### 东方财富-成份股

接口: stock_board_industry_cons_em

目标地址: https://data.eastmoney.com/bkzj/BK1027.html

描述: 东方财富-沪深板块-行业板块-板块成份

限量: 单次返回指定 symbol 的所有成份股

输入参数

| 名称     | 类型  | 描述                                                                                              |
|--------|-----|-------------------------------------------------------------------------------------------------|
| symbol | str | symbol="小金属"; 支持传入板块代码比如：BK1027，可以通过调用 **ak.stock_board_industry_name_em()** 查看东方财富-行业板块的所有行业代码 |

输出参数

| 名称     | 类型      | 描述      |
|--------|---------|---------|
| 序号     | int64   | -       |
| 代码     | object  | -       |
| 名称     | object  | -       |
| 最新价    | float64 | -       |
| 涨跌幅    | float64 | 注意单位: % |
| 涨跌额    | float64 | -       |
| 成交量    | float64 | 注意单位: 手 |
| 成交额    | float64 | -       |
| 振幅     | float64 | 注意单位: % |
| 最高     | float64 | -       |
| 最低     | float64 | -       |
| 今开     | float64 | -       |
| 昨收     | float64 | -       |
| 换手率    | float64 | 注意单位: % |
| 市盈率-动态 | float64 | -       |
| 市净率    | float64 | -       |

接口示例

```python
import akshare as ak

stock_board_industry_cons_em_df = ak.stock_board_industry_cons_em(symbol="小金属")
print(stock_board_industry_cons_em_df)
```

#### 东方财富-指数-日频

接口: stock_board_industry_hist_em

目标地址: https://quote.eastmoney.com/bk/90.BK1027.html

描述: 东方财富-沪深板块-行业板块-历史行情数据

限量: 单次返回指定 symbol 和 adjust 的所有历史数据

输入参数

| 名称         | 类型  | 描述                                                                            |
|------------|-----|-------------------------------------------------------------------------------|
| symbol     | str | symbol="小金属"; 可以通过调用 **ak.stock_board_industry_name_em()** 查看东方财富-行业板块的所有行业代码 |
| start_date | str | start_date="20211201";                                                        |
| end_date   | str | end_date="20220401";                                                          |
| period     | str | period="日k"; 周期; choice of {"日k", "周k", "月k"}                                 |
| adjust     | str | adjust=""; choice of {'': 不复权, 默认; "qfq": 前复权, "hfq": 后复权}                    |

输出参数

| 名称  | 类型      | 描述      |
|-----|---------|---------|
| 日期  | object  | -       |
| 开盘  | float64 | -       |
| 收盘  | float64 | -       |
| 最高  | float64 | -       |
| 最低  | float64 | -       |
| 涨跌幅 | float64 | 注意单位: % |
| 涨跌额 | float64 | -       |
| 成交量 | int64   | -       |
| 成交额 | float64 | -       |
| 振幅  | float64 | 注意单位: % |
| 换手率 | float64 | 注意单位: % |

接口示例

```python
import akshare as ak

stock_board_industry_hist_em_df = ak.stock_board_industry_hist_em(symbol="小金属", start_date="20211201", end_date="20240222", period="日k", adjust="")
print(stock_board_industry_hist_em_df)
```

#### 东方财富-指数-分时

接口: stock_board_industry_hist_min_em

目标地址: http://quote.eastmoney.com/bk/90.BK1027.html

描述: 东方财富-沪深板块-行业板块-分时历史行情数据

限量: 单次返回指定 symbol 和 period 的所有历史数据

输入参数

| 名称     | 类型  | 描述                                                                            |
|--------|-----|-------------------------------------------------------------------------------|
| symbol | str | symbol="小金属"; 可以通过调用 **ak.stock_board_industry_name_em()** 查看东方财富-行业板块的所有行业代码 |
| period | str | period=""; choice of {"1", "5", "15", "30", "60"}                             |

输出参数-1分钟

| 名称   | 类型      | 描述 |
|------|---------|----|
| 日期时间 | object  | -  |
| 开盘   | float64 | -  |
| 收盘   | float64 | -  |
| 最高   | float64 | -  |
| 最低   | float64 | -  |
| 成交量  | int64   | -  |
| 成交额  | float64 | -  |
| 最新价  | float64 | -  |

接口示例-1分钟

```python
import akshare as ak

stock_board_industry_hist_min_em_df = ak.stock_board_industry_hist_min_em(symbol="小金属", period="1")
print(stock_board_industry_hist_min_em_df)
```

输出参数-其他

| 名称   | 类型      | 描述      |
|------|---------|---------|
| 日期时间 | object  | -       |
| 开盘   | float64 | -       |
| 收盘   | float64 | -       |
| 最高   | float64 | -       |
| 最低   | float64 | -       |
| 涨跌幅  | float64 | 注意单位: % |
| 涨跌额  | float64 | -       |
| 成交量  | int64   | -       |
| 成交额  | float64 | -       |
| 振幅   | float64 | 注意单位: % |
| 换手率  | float64 | 注意单位: % |

接口示例-其他

```python
import akshare as ak

stock_board_industry_hist_min_em_df = ak.stock_board_industry_hist_min_em(symbol="小金属", period="5")
print(stock_board_industry_hist_min_em_df)
```

### 股票热度

#### 股票热度-雪球

##### 关注排行榜

接口: stock_hot_follow_xq

目标地址: https://xueqiu.com/hq

描述: 雪球-沪深股市-热度排行榜-关注排行榜

限量: 单次返回指定 symbol 的排行数据

输入参数

| 名称     | 类型  | 描述                                      |
|--------|-----|-----------------------------------------|
| symbol | str | symbol="最热门"; choice of {"本周新增", "最热门"} |

输出参数

| 名称   | 类型      | 描述      |
|------|---------|---------|
| 股票代码 | object  | -       |
| 股票简称 | object  | -       |
| 关注   | float64 | -       |
| 最新价  | float64 | 注意单位: 元 |

接口示例

```python
import akshare as ak

stock_hot_follow_xq_df = ak.stock_hot_follow_xq(symbol="最热门")
print(stock_hot_follow_xq_df)
```

##### 讨论排行榜

接口: stock_hot_tweet_xq

目标地址: https://xueqiu.com/hq

描述: 雪球-沪深股市-热度排行榜-讨论排行榜

限量: 单次返回指定 symbol 的排行数据

输入参数

| 名称     | 类型  | 描述                                      |
|--------|-----|-----------------------------------------|
| symbol | str | symbol="最热门"; choice of {"本周新增", "最热门"} |

输出参数

| 名称   | 类型      | 描述      |
|------|---------|---------|
| 股票代码 | object  | -       |
| 股票简称 | object  | -       |
| 关注   | float64 | -       |
| 最新价  | float64 | 注意单位: 元 |

接口示例

```python
import akshare as ak

stock_hot_tweet_xq_df = ak.stock_hot_tweet_xq(symbol="最热门")
print(stock_hot_tweet_xq_df)
```

##### 交易排行榜

接口: stock_hot_deal_xq

目标地址: https://xueqiu.com/hq

描述: 雪球-沪深股市-热度排行榜-交易排行榜

限量: 单次返回指定 symbol 的排行数据

输入参数

| 名称     | 类型  | 描述                                      |
|--------|-----|-----------------------------------------|
| symbol | str | symbol="最热门"; choice of {"本周新增", "最热门"} |

输出参数

| 名称   | 类型      | 描述      |
|------|---------|---------|
| 股票代码 | object  | -       |
| 股票简称 | object  | -       |
| 关注   | float64 | -       |
| 最新价  | float64 | 注意单位: 元 |

接口示例

```python
import akshare as ak

stock_hot_deal_xq_df = ak.stock_hot_deal_xq(symbol="最热门")
print(stock_hot_deal_xq_df)
```

#### 股票热度-东财

##### 人气榜-A股

接口: stock_hot_rank_em

目标地址: http://guba.eastmoney.com/rank/

描述: 东方财富网站-股票热度

限量: 单次返回当前交易日前 100 个股票的人气排名数据

输入参数

| 名称  | 类型  | 描述  |
|-----|-----|-----|
| -   | -   | -   |

输出参数

| 名称   | 类型      | 描述      |
|------|---------|---------|
| 当前排名 | int64   | -       |
| 代码   | object  | -       |
| 股票名称 | object  | -       |
| 最新价  | float64 | -       |
| 涨跌额  | float64 | -       |
| 涨跌幅  | float64 | 注意单位: % |

接口示例

```python
import akshare as ak

stock_hot_rank_em_df = ak.stock_hot_rank_em()
print(stock_hot_rank_em_df)
```

##### 飙升榜-A股

接口: stock_hot_up_em

目标地址: http://guba.eastmoney.com/rank/

描述: 东方财富-个股人气榜-飙升榜

限量: 单次返回当前交易日前 100 个股票的飙升榜排名数据

输入参数

| 名称  | 类型  | 描述  |
|-----|-----|-----|
| -   | -   | -   |

输出参数

| 名称      | 类型      | 描述      |
|---------|---------|---------|
| 排名较昨日变动 | int64   | -       |
| 当前排名    | int64   | -       |
| 代码      | object  | -       |
| 股票名称    | object  | -       |
| 最新价     | float64 | -       |
| 涨跌额     | float64 | -       |
| 涨跌幅     | float64 | 注意单位: % |

接口示例

```python
import akshare as ak

stock_hot_up_em_df = ak.stock_hot_up_em()
print(stock_hot_up_em_df)
```

##### 人气榜-港股

接口: stock_hk_hot_rank_em

目标地址: https://guba.eastmoney.com/rank/

描述: 东方财富-个股人气榜-人气榜-港股市场

限量: 单次返回当前交易日前 100 个股票的人气排名数据

输入参数

| 名称  | 类型  | 描述  |
|-----|-----|-----|
| -   | -   | -   |

输出参数

| 名称   | 类型      | 描述      |
|------|---------|---------|
| 当前排名 | int64   | -       |
| 代码   | object  | -       |
| 股票名称 | object  | -       |
| 最新价  | float64 | -       |
| 涨跌幅  | float64 | 注意单位: % |

接口示例

```python
import akshare as ak

stock_hk_hot_rank_em_df = ak.stock_hk_hot_rank_em()
print(stock_hk_hot_rank_em_df)
```

#### 历史趋势及粉丝特征

##### A股

接口: stock_hot_rank_detail_em

目标地址: http://guba.eastmoney.com/rank/stock?code=000665

描述: 东方财富网-股票热度-历史趋势及粉丝特征

限量: 单次返回指定 symbol 的股票近期历史数据

输入参数

| 名称     | 类型  | 描述                |
|--------|-----|-------------------|
| symbol | str | symbol="SZ000665" |

输出参数

| 名称   | 类型      | 描述  |
|------|---------|-----|
| 时间   | object  | -   |
| 排名   | int64   | -   |
| 证券代码 | object  | -   |
| 新晋粉丝 | float64 | -   |
| 铁杆粉丝 | float64 | -   |

接口示例

```python
import akshare as ak

stock_hot_rank_detail_em_df = ak.stock_hot_rank_detail_em(symbol="SZ000665")
print(stock_hot_rank_detail_em_df)
```

##### 港股

接口: stock_hk_hot_rank_detail_em

目标地址: https://guba.eastmoney.com/rank/stock?code=HK_00700

描述: 东方财富网-股票热度-历史趋势

限量: 单次返回指定 symbol 的股票近期历史数据

输入参数

| 名称     | 类型  | 描述             |
|--------|-----|----------------|
| symbol | str | symbol="00700" |

输出参数

| 名称   | 类型      | 描述  |
|------|---------|-----|
| 时间   | object  | -   |
| 排名   | int64   | -   |
| 证券代码 | object  | -   |

接口示例

```python
import akshare as ak

stock_hk_hot_rank_detail_em_df = ak.stock_hk_hot_rank_detail_em(symbol="00700")
print(stock_hk_hot_rank_detail_em_df)
```

#### 互动平台

##### 互动易-提问

接口: stock_irm_cninfo

目标地址: https://irm.cninfo.com.cn/

描述: 互动易-提问

限量: 单次返回近期 10000 条提问数据

输入参数

| 名称     | 类型  | 描述                |
|--------|-----|-------------------|
| symbol | str | symbol="002594";  |

输出参数

| 名称    | 类型             | 描述 |
|-------|----------------|----|
| 股票代码  | object         | -  |
| 公司简称  | object         | -  |
| 行业    | object         | -  |
| 行业代码  | object         | -  |
| 问题    | object         | -  |
| 提问者   | object         | -  |
| 来源    | object         | -  |
| 提问时间  | datetime64[ns] | -  |
| 更新时间  | datetime64[ns] | -  |
| 提问者编号 | object         | -  |
| 问题编号  | object         | -  |
| 回答ID  | object         | -  |
| 回答内容  | object         | -  |
| 回答者   | object         | -  |

接口示例

```python
import akshare as ak

stock_irm_cninfo_df = ak.stock_irm_cninfo(symbol="002594")
print(stock_irm_cninfo_df)
```

##### 互动易-回答

接口: stock_irm_ans_cninfo

目标地址: https://irm.cninfo.com.cn/

描述: 互动易-回答

限量: 单次返回指定 symbol 的回答数据

输入参数

| 名称     | 类型  | 描述                                                               |
|--------|-----|------------------------------------------------------------------|
| symbol | str | symbol="1495108801386602496"; 通过 ak.stock_irm_cninfo 来获取具体的提问者编号 |

输出参数

| 名称   | 类型             | 描述 |
|------|----------------|----|
| 股票代码 | object         | -  |
| 公司简称 | object         | -  |
| 问题   | object         | -  |
| 回答内容 | object         | -  |
| 提问者  | object         | -  |
| 提问时间 | datetime64[ns] | -  |
| 回答时间 | datetime64[ns] | -  |

接口示例

```python
import akshare as ak

stock_irm_ans_cninfo_df = ak.stock_irm_ans_cninfo(symbol="1495108801386602496")
print(stock_irm_ans_cninfo_df)
```

##### 上证e互动

接口: stock_sns_sseinfo

目标地址: https://sns.sseinfo.com/company.do?uid=65

描述: 上证e互动-提问与回答

限量: 单次返回指定 symbol 的提问与回答数据

输入参数

| 名称     | 类型  | 描述                    |
|--------|-----|-----------------------|
| symbol | str | symbol="603119"; 股票代码 |

输出参数

| 名称   | 类型     | 描述 |
|------|--------|----|
| 股票代码 | object | -  |
| 公司简称 | object | -  |
| 问题   | object | -  |
| 回答   | object | -  |
| 问题时间 | object | -  |
| 回答时间 | object | -  |
| 问题来源 | object | -  |
| 回答来源 | object | -  |
| 用户名  | object | -  |

接口示例

```python
import akshare as ak

stock_sns_sseinfo_df = ak.stock_sns_sseinfo(symbol="603119")
print(stock_sns_sseinfo_df)
```

#### 个股人气榜-实时变动

##### A股

接口: stock_hot_rank_detail_realtime_em

目标地址: http://guba.eastmoney.com/rank/stock?code=000665

描述: 东方财富网-个股人气榜-实时变动

限量: 单次返回指定 symbol 的股票近期历史数据

输入参数

| 名称     | 类型  | 描述                |
|--------|-----|-------------------|
| symbol | str | symbol="SZ000665" |

输出参数

| 名称   | 类型      | 描述  |
|------|---------|-----|
| 时间   | object  | -   |
| 排名   | int64   | -   |

接口示例

```python
import akshare as ak

stock_hot_rank_detail_realtime_em_df = ak.stock_hot_rank_detail_realtime_em(symbol="SZ000665")
print(stock_hot_rank_detail_realtime_em_df)
```

##### 港股

接口: stock_hk_hot_rank_detail_realtime_em

目标地址: https://guba.eastmoney.com/rank/stock?code=HK_00700

描述: 东方财富网-个股人气榜-实时变动

限量: 单次返回指定 symbol 的股票近期历史数据

输入参数

| 名称     | 类型  | 描述             |
|--------|-----|----------------|
| symbol | str | symbol="00700" |

输出参数

| 名称   | 类型      | 描述  |
|------|---------|-----|
| 时间   | object  | -   |
| 排名   | int64   | -   |

接口示例

```python
import akshare as ak

stock_hk_hot_rank_detail_realtime_em_df = ak.stock_hk_hot_rank_detail_realtime_em(symbol="00700")
print(stock_hk_hot_rank_detail_realtime_em_df)
```

#### 热门关键词

接口: stock_hot_keyword_em

目标地址: http://guba.eastmoney.com/rank/stock?code=000665

描述: 东方财富-个股人气榜-热门关键词

限量: 单次返回指定 symbol 的最近交易日时点数据

输入参数

| 名称     | 类型  | 描述                |
|--------|-----|-------------------|
| symbol | str | symbol="SZ000665" |

输出参数

| 名称   | 类型     | 描述  |
|------|--------|-----|
| 时间   | object | -   |
| 股票代码 | object | -   |
| 概念名称 | object | -   |
| 概念代码 | object | -   |
| 热度   | int64  | -   |

接口示例

```python
import akshare as ak

stock_hot_keyword_em_df = ak.stock_hot_keyword_em(symbol="SZ000665")
print(stock_hot_keyword_em_df)
```

#### 内部交易

接口: stock_inner_trade_xq

目标地址: https://xueqiu.com/hq/insider

描述: 雪球-行情中心-沪深股市-内部交易

限量: 单次返回所有历史数据

输入参数

| 名称  | 类型  | 描述  |
|-----|-----|-----|
| -   | -   | -   |

输出参数

| 名称     | 类型      | 描述  |
|--------|---------|-----|
| 股票代码   | object  | -   |
| 股票名称   | object  | -   |
| 变动日期   | object  | -   |
| 变动人    | object  | -   |
| 变动股数   | int64   | -   |
| 成交均价   | float64 | -   |
| 变动后持股数 | float64 | -   |
| 与董监高关系 | object  | -   |
| 董监高职务  | object  | -   |

接口示例

```python
import akshare as ak

stock_inner_trade_xq_df = ak.stock_inner_trade_xq()
print(stock_inner_trade_xq_df)
```

#### 个股人气榜-最新排名

##### A股

接口: stock_hot_rank_latest_em

目标地址: http://guba.eastmoney.com/rank/stock?code=000665

描述: 东方财富-个股人气榜-最新排名

限量: 单次返回指定 symbol 的股票近期历史数据

输入参数

| 名称     | 类型  | 描述                |
|--------|-----|-------------------|
| symbol | str | symbol="SZ000665" |

输出参数

| 名称    | 类型     | 描述  |
|-------|--------|-----|
| item  | object | -   |
| value | object | -   |

接口示例

```python
import akshare as ak

stock_hot_rank_latest_em_df = ak.stock_hot_rank_latest_em(symbol="SZ000665")
print(stock_hot_rank_latest_em_df)
```

##### 港股

接口: stock_hk_hot_rank_latest_em

目标地址: https://guba.eastmoney.com/rank/stock?code=HK_00700

描述: 东方财富-个股人气榜-最新排名

限量: 单次返回指定 symbol 的股票近期历史数据

输入参数

| 名称     | 类型  | 描述             |
|--------|-----|----------------|
| symbol | str | symbol="00700" |

输出参数

| 名称    | 类型     | 描述  |
|-------|--------|-----|
| item  | object | -   |
| value | object | -   |

接口示例

```python
import akshare as ak

stock_hk_hot_rank_latest_em_df = ak.stock_hk_hot_rank_latest_em(symbol="00700")
print(stock_hk_hot_rank_latest_em_df)
```

#### 热搜股票

接口: stock_hot_search_baidu

目标地址: https://gushitong.baidu.com/expressnews

描述: 百度股市通-热搜股票

限量: 单次返回指定 symbol, date 和 time 的热搜股票数据

输入参数

| 名称     | 类型  | 描述                                              |
|--------|-----|-------------------------------------------------|
| symbol | str | symbol="A股"; choice of {"全部", "A股", "港股", "美股"} |
| date   | str | date="20250616"                                 |
| time   | str | time="今日"; choice of {"今日", "1小时"}              |

输出参数

| 名称    | 类型     | 描述 |
|-------|--------|----|
| 名称/代码 | object | -  |
| 涨跌幅   | object | -  |
| 综合热度  | int64  | -  |

接口示例

```python
import akshare as ak

stock_hot_search_baidu_df = ak.stock_hot_search_baidu(symbol="A股", date="20250616", time="今日")
print(stock_hot_search_baidu_df)
```

#### 相关股票

接口: stock_hot_rank_relate_em

目标地址: http://guba.eastmoney.com/rank/stock?code=000665

描述: 东方财富-个股人气榜-相关股票

限量: 单次返回指定 symbol 的股票近期历史数据

输入参数

| 名称     | 类型  | 描述                |
|--------|-----|-------------------|
| symbol | str | symbol="SZ000665" |

输出参数

| 名称     | 类型      | 描述  |
|--------|---------|-----|
| 时间     | object  | -   |
| 股票代码   | object  | -   |
| 相关股票代码 | object  | -   |
| 涨跌幅    | float64 | -   |

接口示例

```python
import akshare as ak

stock_hot_rank_relate_em_df = ak.stock_hot_rank_relate_em(symbol="SZ000665")
print(stock_hot_rank_relate_em_df)
```

### 盘口异动

接口: stock_changes_em

目标地址: http://quote.eastmoney.com/changes/

描述: 东方财富-行情中心-盘口异动数据

限量: 单次指定 symbol 的最近交易日的盘口异动数据

输入参数

| 名称     | 类型  | 描述                                                                                                                                                                                                                    |
|--------|-----|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| symbol | str | symbol="大笔买入"; choice of {'火箭发射', '快速反弹', '大笔买入', '封涨停板', '打开跌停板', '有大买盘', '竞价上涨', '高开5日线', '向上缺口', '60日新高', '60日大幅上涨', '加速下跌', '高台跳水', '大笔卖出', '封跌停板', '打开涨停板', '有大卖盘', '竞价下跌', '低开5日线', '向下缺口', '60日新低', '60日大幅下跌'} |

输出参数

| 名称   | 类型     | 描述                   |
|------|--------|----------------------|
| 时间   | object | -                    |
| 代码   | object | -                    |
| 名称   | object | -                    |
| 板块   | object | -                    |
| 相关信息 | object | 注意: 不同的 symbol 的单位不同 |

接口示例

```python
import akshare as ak

stock_changes_em_df = ak.stock_changes_em(symbol="大笔买入")
print(stock_changes_em_df)
```

### 板块异动详情

接口: stock_board_change_em

目标地址: https://quote.eastmoney.com/changes/

描述: 东方财富-行情中心-当日板块异动详情

限量: 返回最近交易日的数据

输入参数

| 名称  | 类型  | 描述  |
|-----|-----|-----|
| -   | -   | -   |

输出参数

| 名称                  | 类型      | 描述        |
|---------------------|---------|-----------|
| 板块名称                | object  | -         |
| 涨跌幅                 | float64 | 注意单位: %   |
| 主力净流入               | float64 | 注意单位: 万元  |
| 板块异动总次数             | float64 | -         |
| 板块异动最频繁个股及所属类型-股票代码 | object  | -         |
| 板块异动最频繁个股及所属类型-股票名称 | object  | -         |
| 板块异动最频繁个股及所属类型-买卖方向 | object  | -         |
| 板块具体异动类型列表及出现次数     | object  | 返回具体异动的字典 |

接口示例

```python
import akshare as ak

stock_board_change_em_df = ak.stock_board_change_em()
print(stock_board_change_em_df)
```

### 涨停板行情

#### 涨停股池

接口: stock_zt_pool_em

目标地址: https://quote.eastmoney.com/ztb/detail#type=ztgc

描述: 东方财富网-行情中心-涨停板行情-涨停股池

限量: 单次返回指定 date 的涨停股池数据; 该接口只能获取近期的数据

输入参数

| 名称   | 类型  | 描述              |
|------|-----|-----------------|
| date | str | date='20241008' |

输出参数

| 名称     | 类型      | 描述             |
|--------|---------|----------------|
| 序号     | int64   | -              |
| 代码     | object  | -              |
| 名称     | object  | -              |
| 涨跌幅    | float64 | 注意单位: %        |
| 最新价    | float64 | -              |
| 成交额    | int64   | -              |
| 流通市值   | float64 | -              |
| 总市值    | float64 | -              |
| 换手率    | float64 | 注意单位: %        |
| 封板资金   | int64   | -              |
| 首次封板时间 | object  | 注意格式: 09:25:00 |
| 最后封板时间 | object  | 注意格式: 09:25:00 |
| 炸板次数   | int64   | -              |
| 涨停统计   | object  | -              |
| 连板数    | int64   | 注意格式: 1 为首板    |
| 所属行业   | object  | -              |

接口示例

```python
import akshare as ak

stock_zt_pool_em_df = ak.stock_zt_pool_em(date='20241008')
print(stock_zt_pool_em_df)
```

#### 昨日涨停股池

接口: stock_zt_pool_previous_em

目标地址: https://quote.eastmoney.com/ztb/detail#type=zrzt

描述: 东方财富网-行情中心-涨停板行情-昨日涨停股池

限量: 单次返回指定 date 的昨日涨停股池数据; 该接口只能获取近期的数据

输入参数

| 名称   | 类型  | 描述              |
|------|-----|-----------------|
| date | str | date='20240415' |

输出参数

| 名称     | 类型      | 描述             |
|--------|---------|----------------|
| 序号     | int32   | -              |
| 代码     | object  | -              |
| 名称     | object  | -              |
| 涨跌幅    | float64 | 注意单位: %        |
| 最新价    | int64   | -              |
| 涨停价    | int64   | -              |
| 成交额    | int64   | -              |
| 流通市值   | float64 | -              |
| 总市值    | float64 | -              |
| 换手率    | float64 | 注意单位: %        |
| 涨速     | float64 | 注意单位: %        |
| 振幅     | float64 | 注意单位: %        |
| 昨日封板时间 | int64   | 注意格式: 09:25:00 |
| 昨日连板数  | int64   | 注意格式: 1 为首板    |
| 涨停统计   | object  | -              |
| 所属行业   | object  | -              |

接口示例

```python
import akshare as ak

stock_zt_pool_previous_em_df = ak.stock_zt_pool_previous_em(date='20240415')
print(stock_zt_pool_previous_em_df)
```

#### 强势股池

接口: stock_zt_pool_strong_em

目标地址: https://quote.eastmoney.com/ztb/detail#type=qsgc

描述: 东方财富网-行情中心-涨停板行情-强势股池

限量: 单次返回指定 date 的强势股池数据；该接口只能获取近期的数据

输入参数

| 名称   | 类型  | 描述              |
|------|-----|-----------------|
| date | str | date='20241009' |

输出参数

| 名称   | 类型      | 描述      |
|------|---------|---------|
| 序号   | int64   | -       |
| 代码   | object  | -       |
| 名称   | object  | -       |
| 涨跌幅  | float64 | 注意单位: % |
| 最新价  | float64 | -       |
| 涨停价  | float64 | -       |
| 成交额  | int64   | -       |
| 流通市值 | float64 | -       |
| 总市值  | float64 | -       |
| 换手率  | float64 | 注意单位: % |
| 涨速   | float64 | 注意单位: % |
| 是否新高 | object  | -       |
| 量比   | float64 | -       |
| 涨停统计 | object  | -       |
| 入选理由 | object  | -       |
| 所属行业 | object  | -       |

接口示例

```python
import akshare as ak

stock_zt_pool_strong_em_df = ak.stock_zt_pool_strong_em(date='20241231')
print(stock_zt_pool_strong_em_df)
```

#### 次新股池

接口: stock_zt_pool_sub_new_em

目标地址: https://quote.eastmoney.com/ztb/detail#type=cxgc

描述: 东方财富网-行情中心-涨停板行情-次新股池

限量: 单次返回指定 date 的次新股池数据；该接口只能获取近期的数据

输入参数

| 名称   | 类型  | 描述              |
|------|-----|-----------------|
| date | str | date='20241231' |

输出参数

| 名称   | 类型      | 描述      |
|------|---------|---------|
| 序号   | int32   | -       |
| 代码   | object  | -       |
| 名称   | object  | -       |
| 涨跌幅  | float64 | 注意单位: % |
| 最新价  | float64 | -       |
| 涨停价  | float64 | -       |
| 成交额  | int64   | -       |
| 流通市值 | float64 | -       |
| 总市值  | float64 | -       |
| 转手率  | float64 | 注意单位: % |
| 开板几日 | int64   | -       |
| 开板日期 | int64   | -       |
| 上市日期 | int64   | -       |
| 是否新高 | int64   | -       |
| 涨停统计 | object  | -       |
| 所属行业 | object  | -       |

接口示例

```python
import akshare as ak

stock_zt_pool_sub_new_em_df = ak.stock_zt_pool_sub_new_em(date='20241231')
print(stock_zt_pool_sub_new_em_df)
```

#### 炸板股池

接口: stock_zt_pool_zbgc_em

目标地址: https://quote.eastmoney.com/ztb/detail#type=zbgc

描述: 东方财富网-行情中心-涨停板行情-炸板股池

限量: 单次返回指定 date 的炸板股池数据；该接口只能获取近期的数据

输入参数

| 名称   | 类型  | 描述              |
|------|-----|-----------------|
| date | str | date='20241011' |

输出参数

| 名称     | 类型      | 描述             |
|--------|---------|----------------|
| 序号     | int32   | -              |
| 代码     | object  | -              |
| 名称     | object  | -              |
| 涨跌幅    | float64 | 注意单位: %        |
| 最新价    | float64 | -              |
| 涨停价    | float64 | -              |
| 成交额    | int64   | -              |
| 流通市值   | float64 | -              |
| 总市值    | float64 | -              |
| 换手率    | float64 | 注意单位: %        |
| 涨速     | int64   | -              |
| 首次封板时间 | object  | 注意格式: 09:25:00 |
| 炸板次数   | int64   | -              |
| 涨停统计   | int64   | -              |
| 振幅     | object  | -              |
| 所属行业   | object  | -              |

接口示例

```python
import akshare as ak

stock_zt_pool_zbgc_em_df = ak.stock_zt_pool_zbgc_em(date='20241011')
print(stock_zt_pool_zbgc_em_df)
```

#### 跌停股池

接口: stock_zt_pool_dtgc_em

目标地址: https://quote.eastmoney.com/ztb/detail#type=zbgc

描述: 东方财富网-行情中心-涨停板行情-跌停股池

限量: 单次返回指定 date 的跌停股池数据；该接口只能获取近期的数据

输入参数

| 名称   | 类型  | 描述              |
|------|-----|-----------------|
| date | str | date='20241011' |

输出参数

| 名称     | 类型      | 描述             |
|--------|---------|----------------|
| 序号     | int64   | -              |
| 代码     | object  | -              |
| 名称     | object  | -              |
| 涨跌幅    | float64 | 注意单位: %        |
| 最新价    | float64 | -              |
| 成交额    | int64   | -              |
| 流通市值   | float64 | -              |
| 总市值    | float64 | -              |
| 动态市盈率  | float64 | -              |
| 换手率    | float64 | 注意单位: %        |
| 封单资金   | int64   | -              |
| 最后封板时间 | object  | 注意格式: 09:25:00 |
| 板上成交额  | int64   | -              |
| 连续跌停   | int64   | -              |
| 开板次数   | int64   | -              |
| 所属行业   | object  | -              |

接口示例

```python
import akshare as ak

stock_zt_pool_dtgc_em_df = ak.stock_zt_pool_dtgc_em(date='20241011')
print(stock_zt_pool_dtgc_em_df)
```

### 赚钱效应分析

接口: stock_market_activity_legu

目标地址: https://www.legulegu.com/stockdata/market-activity

描述: 乐咕乐股网-赚钱效应分析数据

限量: 单次返回当前赚钱效应分析数据

说明：

1. 涨跌比：即沪深两市上涨个股所占比例，体现的是市场整体涨跌，占比越大则代表大部分个股表现活跃。
2. 涨停板数与跌停板数的意义：涨停家数在一定程度上反映了市场的投机氛围。当涨停家数越多，则市场的多头氛围越强。真实涨停是非一字无量涨停。真实跌停是非一字无量跌停。

输入参数

| 名称  | 类型  | 描述  |
|-----|-----|-----|
| -   | -   | -   |

输出参数

| 名称    | 类型     | 描述  |
|-------|--------|-----|
| item  | object | -   |
| value | object | -   |

接口示例

```python
import akshare as ak

stock_market_activity_legu_df = ak.stock_market_activity_legu()
print(stock_market_activity_legu_df)
```

### 资讯数据

#### 财经早餐-东财财富

接口：stock_info_cjzc_em

目标地址：https://stock.eastmoney.com/a/czpnc.html

描述：东方财富-财经早餐

限量：单次返回全部历史数据

输入参数

| 名称 | 类型 | 描述 |
|----|----|----|
| -  | -  | -  |

输出参数

| 名称   | 类型     | 描述 |
|------|--------|----|
| 标题   | object | -  |
| 摘要   | object | -  |
| 发布时间 | object | -  |
| 链接   | object | -  |

接口示例：

```python
import akshare as ak

stock_info_cjzc_em_df = ak.stock_info_cjzc_em()
print(stock_info_cjzc_em_df)
```

#### 全球财经快讯-东财财富

接口：stock_info_global_em

目标地址：https://kuaixun.eastmoney.com/7_24.html

描述：东方财富-全球财经快讯

限量：单次返回最近 200 条新闻数据

输入参数

| 名称 | 类型 | 描述 |
|----|----|----|
| -  | -  | -  |

输出参数

| 名称   | 类型     | 描述 |
|------|--------|----|
| 标题   | object | -  |
| 摘要   | object | -  |
| 发布时间 | object | -  |
| 链接   | object | -  |

接口示例：

```python
import akshare as ak

stock_info_global_em_df = ak.stock_info_global_em()
print(stock_info_global_em_df)
```

#### 全球财经快讯-新浪财经

接口：stock_info_global_sina

目标地址：https://finance.sina.com.cn/7x24

描述：新浪财经-全球财经快讯

限量：单次返回最近 20 条新闻数据

输入参数

| 名称 | 类型 | 描述 |
|----|----|----|
| -  | -  | -  |

输出参数

| 名称   | 类型     | 描述 |
|------|--------|----|
| 时间   | object | -  |
| 内容   | object | -  |

接口示例

```python
import akshare as ak

stock_info_global_sina_df = ak.stock_info_global_sina()
print(stock_info_global_sina_df)
```

#### 快讯-富途牛牛

接口：stock_info_global_futu

目标地址：https://news.futunn.com/main/live

描述：富途牛牛-快讯

限量：单次返回最近 50 条新闻数据

输入参数

| 名称 | 类型 | 描述 |
|----|----|----|
| -  | -  | -  |

输出参数

| 名称   | 类型     | 描述 |
|------|--------|----|
| 标题   | object | -  |
| 内容   | object | -  |
| 发布时间 | object | -  |
| 链接   | object | -  |

接口示例

```python
import akshare as ak

stock_info_global_futu_df = ak.stock_info_global_futu()
print(stock_info_global_futu_df)
```

#### 全球财经直播-同花顺财经

接口：stock_info_global_ths

目标地址：https://news.10jqka.com.cn/realtimenews.html

描述：同花顺财经-全球财经直播

限量：单次返回最近 20 条新闻数据

输入参数

| 名称 | 类型 | 描述 |
|----|----|----|
| -  | -  | -  |

输出参数

| 名称   | 类型     | 描述 |
|------|--------|----|
| 标题   | object | -  |
| 内容   | object | -  |
| 发布时间 | object | -  |
| 链接   | object | -  |

接口示例

```python
import akshare as ak

stock_info_global_ths_df = ak.stock_info_global_ths()
print(stock_info_global_ths_df)
```

#### 电报-财联社

接口：stock_info_global_cls

目标地址：https://www.cls.cn/telegraph

描述：财联社-电报

限量：单次返回指定 symbol 的最近 20 条财联社-电报的数据

输入参数

| 名称     | 类型  | 描述                                 |
|--------|-----|------------------------------------|
| symbol | str | symbol="全部"；choice of {"全部", "重点"} |

输出参数

| 名称   | 类型     | 描述  |
|------|--------|-----|
| 标题   | object | -   |
| 内容   | object | -   |
| 发布日期 | object | -   |
| 发布时间 | object | -   |

接口示例：

```python
import akshare as ak

stock_info_global_cls_df = ak.stock_info_global_cls(symbol="全部")
print(stock_info_global_cls_df)
```

### 手续费

#### 国内券商佣金

##### 以万 2.5 佣金结构为例

深证证券交易所

| 项目   | 费用      | 收取部门    |
|------|---------|---------|
| 过户费  | 万 0.2   | 由中国结算收取 |
| 证管费  | 万 0.2   | 由证监会收取  |
| 经手费  | 万 0.487 | 由交易所收取  |
| 券商收入 | 万 1.613 | 由券商收取   |

上海证券交易所

| 项目   | 费用      | 收取部门   |
|------|---------|--------|
| 证管费  | 万 0.2   | 由证监会收取 |
| 经手费  | 万 0.487 | 由交易所收取 |
| 券商收入 | 万 1.813 | 由券商收取  |

##### 以万 1.2 佣金结构为例

深证证券交易所

| 项目   | 费用      | 收取部门    |
|------|---------|---------|
| 过户费  | 万 0.2   | 由中国结算收取 |
| 证管费  | 万 0.2   | 由证监会收取  |
| 经手费  | 万 0.487 | 由交易所收取  |
| 券商收入 | 万 0.313 | 由券商收取   |

上海证券交易所

| 项目   | 费用      | 收取部门   |
|------|---------|--------|
| 证管费  | 万 0.2   | 由证监会收取 |
| 经手费  | 万 0.487 | 由交易所收取 |
| 券商收入 | 万 0.513 | 由券商收取  |

##### 结构图

![交易费用](https://jfds-1252952517.cos.ap-chengdu.myqcloud.com/akshare/readme/mindmap/cost_of_trade.svg)

### 技术指标

#### 创新高

接口：stock_rank_cxg_ths

目标地址：https://data.10jqka.com.cn/rank/cxg/

描述：同花顺-数据中心-技术选股-创新高

限量：单次指定 symbol 的所有数据

输入参数

| 名称     | 类型  | 描述                                                        |
|--------|-----|-----------------------------------------------------------|
| symbol | str | symbol="创月新高"; choice of {"创月新高", "半年新高", "一年新高", "历史新高"} |

输出参数

| 名称     | 类型      | 描述      |
|--------|---------|---------|
| 序号     | int64   | -       |
| 股票代码   | object  | -       |
| 股票简称   | object  | -       |
| 涨跌幅    | float64 | 注意单位: % |
| 换手率    | float64 | 注意单位: % |
| 最新价    | float64 | 注意单位: 元 |
| 前期高点   | float64 | -       |
| 前期高点日期 | object  | -       |

接口示例：

```python
import akshare as ak

stock_rank_cxg_ths_df = ak.stock_rank_cxg_ths(symbol="创月新高")
print(stock_rank_cxg_ths_df)
```

#### 创新低

接口：stock_rank_cxd_ths

目标地址：https://data.10jqka.com.cn/rank/cxd/

描述：同花顺-数据中心-技术选股-创新低

限量：单次指定 symbol 的所有数据

输入参数

| 名称     | 类型  | 描述                                                        |
|--------|-----|-----------------------------------------------------------|
| symbol | str | symbol="创月新低"; choice of {"创月新低", "半年新低", "一年新低", "历史新低"} |

输出参数

| 名称     | 类型      | 描述      |
|--------|---------|---------|
| 序号     | int64   | -       |
| 股票代码   | object  | -       |
| 股票简称   | object  | -       |
| 涨跌幅    | float64 | 注意单位: % |
| 换手率    | float64 | 注意单位: % |
| 最新价    | float64 | 注意单位: 元 |
| 前期低点   | float64 | -       |
| 前期低点日期 | object  | -       |

接口示例：

```python
import akshare as ak

stock_rank_cxd_ths_df = ak.stock_rank_cxd_ths(symbol="创月新低")
print(stock_rank_cxd_ths_df)
```

#### 连续上涨

接口：stock_rank_lxsz_ths

目标地址：https://data.10jqka.com.cn/rank/lxsz/

描述：同花顺-数据中心-技术选股-连续上涨

限量：单次返回所有数据

输入参数

| 名称  | 类型  | 描述  |
|-----|-----|-----|
| -   | -   | -   |

输出参数

| 名称    | 类型      | 描述      |
|-------|---------|---------|
| 序号    | int64   | -       |
| 股票代码  | object  | -       |
| 股票简称  | object  | -       |
| 收盘价   | float64 | 注意单位: 元 |
| 最高价   | float64 | 注意单位: 元 |
| 最低价   | float64 | 注意单位: 元 |
| 连涨天数  | int64   | -       |
| 连续涨跌幅 | float64 | 注意单位: % |
| 累计换手率 | float64 | 注意单位: % |
| 所属行业  | object  | -       |

接口示例

```python
import akshare as ak

stock_rank_lxsz_ths_df = ak.stock_rank_lxsz_ths()
print(stock_rank_lxsz_ths_df)
```

#### 连续下跌

接口：stock_rank_lxxd_ths

目标地址：https://data.10jqka.com.cn/rank/lxxd/

描述：同花顺-数据中心-技术选股-连续下跌

限量：单次返回所有数据

输入参数

| 名称  | 类型  | 描述  |
|-----|-----|-----|
| -   | -   | -   |

输出参数

| 名称    | 类型      | 描述      |
|-------|---------|---------|
| 序号    | int64   | -       |
| 股票代码  | object  | -       |
| 股票简称  | object  | -       |
| 收盘价   | float64 | 注意单位: 元 |
| 最高价   | float64 | 注意单位: 元 |
| 最低价   | float64 | 注意单位: 元 |
| 连涨天数  | int64   | -       |
| 连续涨跌幅 | float64 | 注意单位: % |
| 累计换手率 | float64 | 注意单位: % |
| 所属行业  | object  | -       |

接口示例：

```python
import akshare as ak

stock_rank_lxxd_ths_df = ak.stock_rank_lxxd_ths()
print(stock_rank_lxxd_ths_df)
```

#### 持续放量

接口: stock_rank_cxfl_ths

目标地址: https://data.10jqka.com.cn/rank/cxfl/

描述: 同花顺-数据中心-技术选股-持续放量

限量: 单次返回所有数据

输入参数

| 名称  | 类型  | 描述  |
|-----|-----|-----|
| -   | -   | -   |

输出参数

| 名称     | 类型      | 描述      |
|--------|---------|---------|
| 序号     | int64   | -       |
| 股票代码   | object  | -       |
| 股票简称   | object  | -       |
| 涨跌幅    | float64 | 注意单位: % |
| 最新价    | float64 | 注意单位: 元 |
| 成交量    | object  | 注意单位: 股 |
| 基准日成交量 | object  | 注意单位: 股 |
| 放量天数   | int64   | -       |
| 阶段涨跌幅  | float64 | 注意单位: % |
| 所属行业   | object  | -       |

接口示例

```python
import akshare as ak

stock_rank_cxfl_ths_df = ak.stock_rank_cxfl_ths()
print(stock_rank_cxfl_ths_df)
```

#### 持续缩量

接口: stock_rank_cxsl_ths

目标地址: https://data.10jqka.com.cn/rank/cxsl/

描述: 同花顺-数据中心-技术选股-持续缩量

限量: 单次返回所有数据

输入参数

| 名称  | 类型  | 描述  |
|-----|-----|-----|
| -   | -   | -   |

输出参数

| 名称     | 类型      | 描述      |
|--------|---------|---------|
| 序号     | int64   | -       |
| 股票代码   | object  | -       |
| 股票简称   | object  | -       |
| 涨跌幅    | float64 | 注意单位: % |
| 最新价    | float64 | 注意单位: 元 |
| 成交量    | object  | 注意单位: 股 |
| 基准日成交量 | object  | 注意单位: 股 |
| 缩量天数   | int64   | -       |
| 阶段涨跌幅  | float64 | 注意单位: % |
| 所属行业   | object  | -       |

接口示例

```python
import akshare as ak

stock_rank_cxsl_ths_df = ak.stock_rank_cxsl_ths()
print(stock_rank_cxsl_ths_df)
```

#### 向上突破

接口: stock_rank_xstp_ths

目标地址: https://data.10jqka.com.cn/rank/xstp/

描述: 同花顺-数据中心-技术选股-向上突破

限量: 单次返回所有数据

输入参数

| 名称     | 类型  | 描述                                                                                                   |
|--------|-----|------------------------------------------------------------------------------------------------------|
| symbol | str | symbol="500日均线"; choice of {"5日均线", "10日均线", "20日均线", "30日均线", "60日均线", "90日均线", "250日均线", "500日均线"} |

输出参数

| 名称   | 类型      | 描述      |
|------|---------|---------|
| 序号   | int64   | -       |
| 股票代码 | object  | -       |
| 股票简称 | object  | -       |
| 最新价  | float64 | 注意单位: 元 |
| 成交额  | object  | 注意单位: 元 |
| 成交量  | object  | 注意单位: 股 |
| 涨跌幅  | float64 | 注意单位: % |
| 换手率  | float64 | 注意单位: % |

接口示例

```python
import akshare as ak

stock_rank_xstp_ths_df = ak.stock_rank_xstp_ths(symbol="500日均线")
print(stock_rank_xstp_ths_df)
```

#### 向下突破

接口: stock_rank_xxtp_ths

目标地址: https://data.10jqka.com.cn/rank/xxtp/

描述: 同花顺-数据中心-技术选股-向下突破

限量: 单次返回所有数据

输入参数

| 名称     | 类型  | 描述                                                                                                   |
|--------|-----|------------------------------------------------------------------------------------------------------|
| symbol | str | symbol="500日均线"; choice of {"5日均线", "10日均线", "20日均线", "30日均线", "60日均线", "90日均线", "250日均线", "500日均线"} |

输出参数

| 名称   | 类型      | 描述      |
|------|---------|---------|
| 序号   | int64   | -       |
| 股票代码 | object  | -       |
| 股票简称 | object  | -       |
| 最新价  | float64 | 注意单位: 元 |
| 成交额  | object  | 注意单位: 元 |
| 成交量  | object  | 注意单位: 股 |
| 涨跌幅  | float64 | 注意单位: % |
| 换手率  | float64 | 注意单位: % |

接口示例

```python
import akshare as ak

stock_rank_xxtp_ths_df = ak.stock_rank_xxtp_ths(symbol="500日均线")
print(stock_rank_xxtp_ths_df)
```

#### 量价齐升

接口: stock_rank_ljqs_ths

目标地址: https://data.10jqka.com.cn/rank/ljqs/

描述: 同花顺-数据中心-技术选股-量价齐升

限量: 单次返回所有数据

输入参数

| 名称  | 类型  | 描述  |
|-----|-----|-----|
| -   | -   | -   |

输出参数

| 名称     | 类型      | 描述      |
|--------|---------|---------|
| 序号     | int64   | -       |
| 股票代码   | object  | -       |
| 股票简称   | object  | -       |
| 最新价    | float64 | 注意单位: 元 |
| 量价齐升天数 | int64   | -       |
| 阶段涨幅   | float64 | 注意单位: % |
| 累计换手率  | float64 | 注意单位: % |
| 所属行业   | object  | -       |

接口示例

```python
import akshare as ak

stock_rank_ljqs_ths_df = ak.stock_rank_ljqs_ths()
print(stock_rank_ljqs_ths_df)
```

#### 量价齐跌

接口: stock_rank_ljqd_ths

目标地址: https://data.10jqka.com.cn/rank/ljqd/

描述: 同花顺-数据中心-技术选股-量价齐跌

限量: 单次返回所有数据

输入参数

| 名称  | 类型  | 描述  |
|-----|-----|-----|
| -   | -   | -   |

输出参数

| 名称     | 类型      | 描述      |
|--------|---------|---------|
| 序号     | int64   | -       |
| 股票代码   | object  | -       |
| 股票简称   | object  | -       |
| 最新价    | float64 | 注意单位: 元 |
| 量价齐跌天数 | int64   | -       |
| 阶段涨幅   | float64 | 注意单位: % |
| 累计换手率  | float64 | 注意单位: % |
| 所属行业   | object  | -       |

接口示例

```python
import akshare as ak

stock_rank_ljqd_ths_df = ak.stock_rank_ljqd_ths()
print(stock_rank_ljqd_ths_df)
```

#### 险资举牌

接口: stock_rank_xzjp_ths

目标地址: https://data.10jqka.com.cn/financial/xzjp/

描述: 同花顺-数据中心-技术选股-险资举牌

限量: 单次返回所有数据

输入参数

| 名称  | 类型  | 描述  |
|-----|-----|-----|
| -   | -   | -   |

输出参数

| 名称         | 类型      | 描述      |
|------------|---------|---------|
| 序号         | int64   | -       |
| 举牌公告日      | object  | -       |
| 股票代码       | object  | -       |
| 股票简称       | object  | -       |
| 现价         | float64 | 注意单位: 元 |
| 涨跌幅        | float64 | 注意单位: % |
| 举牌方        | object  | -       |
| 增持数量       | object  | 注意单位: 股 |
| 交易均价       | float64 | 注意单位: 元 |
| 增持数量占总股本比例 | float64 | 注意单位: % |
| 变动后持股总数    | object  | 注意单位: 股 |
| 变动后持股比例    | float64 | 注意单位: % |

接口示例

```python
import akshare as ak

stock_rank_xzjp_ths_df = ak.stock_rank_xzjp_ths()
print(stock_rank_xzjp_ths_df)
```

### ESG 评级

#### ESG 评级数据

接口: stock_esg_rate_sina

目标地址: https://finance.sina.com.cn/esg/grade.shtml

描述: 新浪财经-ESG评级中心-ESG评级-ESG评级数据

限量: 单次返回所有数据

输入参数

| 名称  | 类型  | 描述  |
|-----|-----|-----|
| -   | -   | -   |

输出参数

| 名称    | 类型     | 描述 |
|-------|--------|----|
| 成分股代码 | object | -  |
| 评级机构  | object | -  |
| 评级    | object | -  |
| 评级季度  | object | -  |
| 标识    | object | -  |
| 交易市场  | object | -  |

接口示例

```python
import akshare as ak

stock_esg_rate_sina_df = ak.stock_esg_rate_sina()
print(stock_esg_rate_sina_df)
```

#### MSCI

接口: stock_esg_msci_sina

目标地址: https://finance.sina.com.cn/esg/grade.shtml

描述: 新浪财经-ESG评级中心-ESG评级-MSCI

限量: 单次返回所有数据

输入参数

| 名称  | 类型  | 描述  |
|-----|-----|-----|
| -   | -   | -   |

输出参数

| 名称     | 类型      | 描述 |
|--------|---------|----|
| 股票代码   | object  | -  |
| ESG评分  | object  | -  |
| 环境总评   | float64 | -  |
| 社会责任总评 | float64 | -  |
| 治理总评   | float64 | -  |
| 评级日期   | object  | -  |
| 交易市场   | object  | -  |

接口示例

```python
import akshare as ak

stock_esg_msci_sina_df = ak.stock_esg_msci_sina()
print(stock_esg_msci_sina_df)
```

#### 路孚特

接口: stock_esg_rft_sina

目标地址: https://finance.sina.com.cn/esg/grade.shtml

描述: 新浪财经-ESG评级中心-ESG评级-路孚特

限量: 单次返回所有数据

输入参数

| 名称  | 类型  | 描述  |
|-----|-----|-----|
| -   | -   | -   |

输出参数

| 名称       | 类型      | 描述 |
|----------|---------|----|
| 股票代码     | object  | -  |
| ESG评分    | object  | -  |
| ESG评分日期  | object  | -  |
| 环境总评     | float64 | -  |
| 环境总评日期   | float64 | -  |
| 社会责任总评   | float64 | -  |
| 社会责任总评日期 | object  | -  |
| 治理总评     | object  | -  |
| 治理总评日期   | object  | -  |
| 争议总评     | object  | -  |
| 争议总评日期   | object  | -  |
| 行业       | object  | -  |
| 交易所      | object  | -  |

接口示例

```python
import akshare as ak

stock_esg_rft_sina_df = ak.stock_esg_rft_sina()
print(stock_esg_rft_sina_df)
```

#### 秩鼎

接口: stock_esg_zd_sina

目标地址: https://finance.sina.com.cn/esg/grade.shtml

描述: 新浪财经-ESG评级中心-ESG评级-秩鼎

限量: 单次返回所有数据

输入参数

| 名称  | 类型  | 描述  |
|-----|-----|-----|
| -   | -   | -   |

输出参数

| 名称     | 类型     | 描述 |
|--------|--------|----|
| 股票代码   | object | -  |
| ESG评分  | object | -  |
| 环境总评   | object | -  |
| 社会责任总评 | object | -  |
| 治理总评   | object | -  |
| 评分日期   | object | -  |


接口示例

```python
import akshare as ak

stock_esg_zd_sina_df = ak.stock_esg_zd_sina()
print(stock_esg_zd_sina_df)
```

#### 华证指数

接口: stock_esg_hz_sina

目标地址: https://finance.sina.com.cn/esg/grade.shtml

描述: 新浪财经-ESG评级中心-ESG评级-华证指数

限量: 单次返回所有数据

输入参数

| 名称  | 类型  | 描述  |
|-----|-----|-----|
| -   | -   | -   |

输出参数

| 名称     | 类型      | 描述 |
|--------|---------|----|
| 日期     | object  | -  |
| 股票代码   | object  | -  |
| 交易市场   | object  | -  |
| 股票名称   | object  | -  |
| ESG评分  | float64 | -  |
| ESG等级  | object  | -  |
| 环境     | float64 | -  |
| 环境等级   | object  | -  |
| 社会     | float64 | -  |
| 社会等级   | object  | -  |
| 公司治理   | float64 | -  |
| 公司治理等级 | object  | -  |

接口示例

```python
import akshare as ak

stock_esg_hz_sina_df = ak.stock_esg_hz_sina()
print(stock_esg_hz_sina_df)
```
