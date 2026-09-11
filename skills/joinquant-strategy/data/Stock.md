## 获取股票数据

**注意**

- run_query函数为了防止返回数据量过大, 我们每次最多返回条数为4000行（之前是3000行）
- query函数的更多用法详见：[sqlalchemy.orm.query.Query对象](https://docs.sqlalchemy.org/en/rel_1_0/orm/query.html)
- [Query的简单教程](https://www.joinquant.com/view/community/detail/433d0e9ed9fed11fc9f7772eab8d9376)
- [数据常见疑问汇总](https://www.joinquant.com/view/community/detail/fcb3baa6f926259c4caac3bce7c12b1c?type=2)

### 获取股票概况

包含股票的上市时间、退市时间、代码、名称、是否是ST等。

更多API的可参考[官方API文档](https://www.joinquant.com/api)

#### 获取单支股票数据

获取单支股票的信息

**调用方法**

```python
get_security_info(code)
```

**参数**

- code: 证券代码

**返回值**

- 一个对象, 有如下属性:

1.  display_name # 中文名称
2.  name # 缩写简称
3.  start_date # 上市日期, [datetime.date] 类型
4.  end_date # 退市日期， [datetime.date] 类型, 如果没有退市则为2200-01-01
5.  type # 类型，stock(股票)，index(指数)，etf(ETF基金)，fja（分级A），fjb（分级B）
6.  parent # 分级基金的母基金代码

**示例**

```python
# 输出平安银行信息的中文名称
get_security_info('000001.XSHE').display_name
```

#### 获取所有股票数据

获取平台支持的所有股票数据

**调用方法**

```python
get_all_securities(types=['stock'], date=None)
```

**参数**

- types：默认为stock，这里请在使用时注意防止未来函数。
- date: 日期, 一个字符串或者 [datetime.datetime]/[datetime.date] 对象, 用于获取某日期还在上市的股票信息. 默认值为 None, 表示获取所有日期的股票信息

**返回**

- display_name # 中文名称
- name # 缩写简称
- start_date # 上市日期
- end_date # 退市日期，如果没有退市则为2200-01-01
- type # 类型，stock(股票)

[pandas.DataFrame], 比如:`get_all_securities()[:2]`返回:

```python
               display_name name   start_date   end_date   type
000001.XSHE         平安银行  PAYH  1991-04-03  2200-01-01  stock
000002.XSHE          万科Ａ   WKA   1991-01-29  2200-01-01  stock
```

**示例**

```python
 #将所有股票列表转换成数组
    stocks = list(get_all_securities(['stock']).index)
 #获得2015年10月10日还在上市的所有股票列表
    get_all_securities(date='2015-10-10')
```

#### 判断股票是否是ST

得到多只股票在一段时间是否是ST

**调用方法**

```python
get_extras(info, security_list, start_date='2015-01-01', end_date='2015-12-31', df=True)
```

**参数**

- info: ‘is_st’，是否股改, st,*st和退市整理期标的
- security_list: 股票列表
- start_date/end_date: 开始结束日期, 同[get_price]
- df: 返回[pandas.DataFrame]对象还是一个dict

**返回值**

- df=True: [pandas.DataFrame]对象, 列索引是股票代号, 行索引是[datetime.datetime], 比如
    
    `get_extras('is_st', ['000001.XSHE', '000018.XSHE'], start_date='2013-12-01', end_date='2013-12-03')`返回:
    

```python
            000001.XSHE  000018.XSHE
2013-12-02        False         True
2013-12-03        False         True
```

- df=False:
    一个dict, key是股票代号, value是[numpy.ndarray], 比如`get_extras('is_st', ['000001.XSHE', '000018.XSHE'], start_date='2015-12-01', end_date='2015-12-03', df=False)` 返回:
    
    ```python
    {
       '000001.XSHE': array([False, False, False], dtype=bool),
       '000018.XSHE': array([False, False, False], dtype=bool)
    }
    ```
    

#### 获取股票的融资融券信息

获取一只或者多只股票在一个时间段内的融资融券信息

**调用方法**

```python
get_mtss(security_list, start_date, end_date, fields=None)
```

**参数**

- security_list: 一只股票代码或者一个股票代码的 list
- start_date: 开始日期, 一个字符串或者 [datetime.datetime](https://docs.python.org/2/library/datetime.html#datetime.datetime)/[datetime.date](https://docs.python.org/2/library/datetime.html#datetime.date) 对象
- end_date: 结束日期, 一个字符串或者 [datetime.date](https://docs.python.org/2/library/datetime.html#datetime.date)/[datetime.datetime](https://docs.python.org/2/library/datetime.html#datetime.datetime)对象
- fields: 字段名或者 list, 可选. 默认为 None, 表示取全部字段, 各字段含义如下：

| 字段名 | 含义 |
| --- | --- |
| date | 日期 |
| sec_code | 股票代码 |
| fin_value | 融资余额(元） |
| fin_buy_value | 融资买入额（元） |
| fin_refund_value | 融资偿还额（元） |
| sec_value | 融券余量（股） |
| sec_sell_value | 融券卖出量（股） |
| sec_refund_value | 融券偿还股（股） |
| fin_sec_value | 融资融券余额（元） |

**返回值**
返回一个 [pandas.DataFrame](http://pandas.pydata.org/pandas-docs/version/0.16.2/generated/pandas.DataFrame.html#pandas.DataFrame) 对象，默认的列索引为取得的全部字段. 如果给定了 fields 参数, 则列索引与给定的 fields 对应.

**示例**

```python
from jqdata import *
# 获取一只股票的融资融券信息
get_mtss('000001.XSHE', '2016-01-01', '2016-04-01')
get_mtss('000001.XSHE', '2016-01-01', '2016-04-01', fields=["date", "sec_code", "fin_value", "fin_buy_value"])
get_mtss('000001.XSHE', '2016-01-01', '2016-04-01', fields="sec_sell_value")

# 获取多只股票的融资融券信息
get_mtss(['000001.XSHE', '000002.XSHE', '000099.XSHE'], '2015-03-25', '2016-01-25')
get_mtss(['000001.XSHE', '000002.XSHE', '000099.XSHE'], '2015-03-25', '2016-01-25', fields=["date", "sec_code", "sec_value", "fin_buy_value", "sec_sell_value"])
```

### 股票分类信息

获取指数成份股，或者行业成份股。

#### 获取指数成份股

获取一个指数给定日期在平台可交易的成分股列表，我们支持近600种股票指数数据，包括指数的行情数据以及成分股数据。为了避免未来函数，我们支持获取历史任意时刻的指数成分股信息。请点击[指数列表](/help/api/help?name=index#沪深指数列表)查看指数信息.

**调用方法**

```python
get_index_stocks(index_symbol, date=None)
```

**参数**

- index_symbol, 指数代码
- date: 查询日期, 一个字符串(格式类似’2015-10-15’)或者[datetime.date]/[datetime.datetime]对象, 可以是None, 使用默认日期. 这个默认日期在回测和研究模块上有点差别:

1.  回测模块: 默认值会随着回测日期变化而变化, 等于context.current_dt
2.  研究模块: 默认是今天

**返回**

- 返回股票代码的list

**示例**

```python
# 获取所有沪深300的股票, 设为股票池
stocks = get_index_stocks('000300.XSHG')
set_universe(stocks)
```

#### 获取行业、概念成份股

获取在给定日期一个行业或概念板块的所有股票，行业分类、概念分类列表见数据页面-[行业概念数据](https://www.joinquant.com/help/api/help?name=plateData)。

**调用方法**

```python
# 获取行业板块成分股
get_industry_stocks(industry_code, date=None)

# 获取概念板块成分股
get_concept_stocks(concept_code, date=None)
```

**参数**

- industry_code: 行业编码
    
- date: 查询日期, 一个字符串(格式类似’2015-10-15’)或者[datetime.date]/[datetime.datetime]对象, 可以是None, 使用默认日期. 这个默认日期在回测和研究模块上有点差别:
    

1.  回测模块: 默认值会随着回测日期变化而变化, 等于context.current_dt
2.  研究模块: 默认是今天

**返回**

- 返回股票代码的list

**示例**

```python
# 获取计算机/互联网行业的成分股
stocks = get_industry_stocks('I64')

# 获取风力发电概念板块的成分股
stocks = get_concept_stocks('GN036')
```

#### 查询股票所属行业

```python
get_industry(security, date=None)
```

**参数**

- security：标的代码，类型为字符串，形式如"000001.XSHE"；或为包含标的代码字符串的列表，形如["000001.XSHE", "000002.XSHE"]
- date：查询的日期。类型为字符串，形如"2018-06-01"或"2018-06-01 09:00:00"；或为datetime.datetime对象和datetime.date。注意传入对象的时分秒将被忽略。

**返回**

返回结果是一个dict，key是传入的股票代码

**示例**

```python
#获取贵州茅台("600519.XSHG")的所属行业数据
d = get_industry("600519.XSHG",date="2018-06-01")
print(d)

{'600519.XSHG': {'sw_l1': {'industry_code': '801120', 'industry_name': '食品饮料I'}, 'sw_l2': {'industry_code': '801123', 'industry_name': '饮料制造II'}, 'sw_l3': {'industry_code': '851231', 'industry_name': '白酒III'}, 'zjw': {'industry_code': 'C15', 'industry_name': '酒、饮料和精制茶制造业'}, 'jq_l2': {'industry_code': 'HY478', 'industry_name': '白酒与葡萄酒指数'}, 'jq_l1': {'industry_code': 'HY005', 'industry_name': '日常消费指数'}}}


#同时获取多只股票的所属行业信息
stock_list = ['000001.XSHE','000002.XSHE']
d = get_industry(security=stock_list, date="2018-06-01")
print(d)

{'000001.XSHE': {'sw_l1': {'industry_code': '801780', 'industry_name': '银行I'}, 'sw_l2': {'industry_code': '801192', 'industry_name': '银行II'}, 'sw_l3': {'industry_code': '851911', 'industry_name': '银行III'}, 'zjw': {'industry_code': 'J66', 'industry_name': '货币金融服务'}, 'jq_l2': {'industry_code': 'HY493', 'industry_name': '多元化银行指数'}, 'jq_l1': {'industry_code': 'HY007', 'industry_name': '金融指数'}}, '000002.XSHE': {'sw_l1': {'industry_code': '801180', 'industry_name': '房地产I'}, 'sw_l2': {'industry_code': '801181', 'industry_name': '房地产开发II'}, 'sw_l3': {'industry_code': '851811', 'industry_name': '房地产开发III'}, 'zjw': {'industry_code': 'K70', 'industry_name': '房地产业'}, 'jq_l2': {'industry_code': 'HY509', 'industry_name': '房地产开发指数'}, 'jq_l1': {'industry_code': 'HY011', 'industry_name': '房地产指数'}}}
```

### 获取行情数据

交易类数据提供股票的交易行情数据，通过API接口调用即可获取相应的数据。 具体请查看API,数据获取部分行情相关接口 **[数据获取函数](https://www.joinquant.com/help/api/help#api:%E6%95%B0%E6%8D%AE%E8%8E%B7%E5%8F%96%E5%87%BD%E6%95%B0)**。

| 名称 | 描述 |
| --- | --- |
| get_price | 获取历史数据，可查询多个标的多个数据字段，返回数据格式为 DataFrame |
| history | 获取历史数据，可查询多个标的单个数据字段，返回数据格式为 DataFrame 或 Dict(字典) |
| attribute_history | 获取历史数据，可查询单个标的多个数据字段，返回数据格式为 DataFrame 或 Dict(字典) |
| get_bars | 获取历史数据(包含快照数据)，可查询单个或多个标的多个数据字段，返回数据格式为 numpy.ndarray或DataFrame |
| get_current_data ♠ | 获取当前逻辑时间数据(策略专用) |
| get_current_tick♠ | 获取当前逻辑时间最新的 tick 数据(策略专用) |
| get_ticks | 获取股票、期货、50ETF期权、股票指数及场内基金的tick 数据 |
| get_call_auction | 获取指定时间区间内集合竞价时的 tick 数据 |

## 获取融资融券标的列表

### 获取融资标的列表

```python
get_margincash_stocks(date)
```

**参数** date:默认为None,不指定时返回上交所、深交所最近一次披露的的可融资标的列表的list。

**返回结果** 返回指定日期上交所、深交所披露的的可融资标的列表的list。

**示例**

```python
# 获取融资标的列表，并赋值给 margincash_stocks
margincash_stocks = get_margincash_stocks(date='2018-07-02')

# 判断平安银行是否在可融资列表
>>> '000001.XSHE' in get_margincash_stocks(date='2018-07-02')
>>> True
```

### 获取融券标的列表

```python
get_marginsec_stocks(date)
```

**参数** date:默认为None,不指定时返回上交所、深交所最近一次披露的的可融券标的列表的list。

**返回结果** 返回指定日期上交所、深交所披露的的可融券标的列表的list。

**示例**

```python
# 获取融券标的列表，并赋值给 marginsec_stocks
marginsec_stocks= get_marginsec_stocks(date='2018-07-05')

# 判断平安银行是否在可融券列表
>>> '000001.XSHE' in get_marginsec_stocks(date='2018-07-05')
>>> True
```

## 获取融资融券汇总数据

```python
from jqdata import *
finance.run_query(query(finance.STK_MT_TOTAL).filter(finance.STK_MT_TOTAL.date=='2019-05-23').limit(n))
```

描述：记录上海交易所和深圳交易所的融资融券汇总数据

**参数：**

- **query(finance.STK_MT_TOTAL)**：表示从finance.STK_MT_TOTAL这张表中查询融资融券汇总数据，还可以指定所要查询的字段名，格式如下：query(库名.表名.字段名1，库名.表名.字段名2），多个字段用逗号分隔进行提取；query函数的更多用法详见：[query简易教程](https://www.joinquant.com/view/community/detail/16411)
- **finance.STK_MT_TOTAL**：收录了融资融券汇总数据，表结构和字段信息如下：

**字段设计**

| 名称 | 类型 | 描述 |
| --- | --- | --- |
| date | date | 交易日期 |
| exchange_code | varchar(12) | 交易市场。例如，XSHG-上海证券交易所；XSHE-深圳证券交易所。对应DataAPI.SysCodeGet.codeTypeID=10002。 |
| fin_value | decimal(20,2) | 融资余额（元） |
| fin_buy_value | decimal(20,2) | 融资买入额（元） |
| sec_volume | int | 融券余量（股） |
| sec_value | decimal(20,2) | 融券余量金额（元） |
| sec_sell_volume | int | 融券卖出量（股） |
| fin_sec_value | decimal(20,2) | 融资融券余额（元） |

- **filter(finance.STK_MT_TOTAL.date==date)**：指定筛选条件，通过finance.STK_MT_TOTAL.date==date可以指定你想要查询的日期；除此之外，还可以对表中其他字段指定筛选条件；多个筛选条件用英文逗号分隔。
- **limit(n)**：限制返回的数据条数，n指定返回条数。

**返回结果：**

- 返回一个 dataframe，每一行对应数据表中的一条数据， 列索引是您所查询的字段名称

**注意：**

1.  **为了防止返回数据量过大, 我们每次最多返回4000行**
2.  不能进行连表查询，即同时查询多张表的数据

**示例：**

```python
#查询2019-05-23的融资融券汇总数据。
from jqdata import *
df=finance.run_query(query(finance.STK_MT_TOTAL).filter(finance.STK_MT_TOTAL.date=='2019-05-23').limit(10))
df

     id        date exchange_code      ...           sec_value  sec_sell_volume  fin_sec_value
0  4445  2019-05-23          XSHE      ...        1.465000e+09         26000000   3.615940e+11
1  4446  2019-05-23          XSHG      ...        6.018287e+09        144633497   5.665458e+11
```

## 获取股票资金流向数据

获取一只或者多只股票在一个时间段内的资金流向数据

**调用方法**

```python
from jqdata import *
get_money_flow(security_list, start_date=None, end_date=None, fields=None, count=None)
```

**参数**

- security_list: 一只股票代码或者一个股票代码的 list
- start_date: 开始日期, 一个字符串或者 [datetime.datetime]/[datetime.date] 对象
- end_date: 结束日期, 一个字符串或者 [datetime.date]/[datetime.datetime] 对象
- count: 数量, 与 start_date 二选一，不可同时使用, 必须大于 0. 表示返回 end_date 之前 count 个交易日的数据, 包含 end_date
- fields: 字段名或者 list, 可选. 默认为 None, 表示取全部字段, 各字段含义如下：

| 字段名 | 含义 | 备注 |
| --- | --- | --- |
| date | 日期 |  |
| sec_code | 股票代码 |  |
| change_pct | 涨跌幅(%) |  |
| net_amount_main | 主力净额(万) | 主力净额 = 超大单净额 + 大单净额 |
| net_pct_main | 主力净占比(%) | 主力净占比 = 主力净额 / 成交额 |
| net_amount_xl | 超大单净额(万) | 超大单：大于等于50万股或者100万元的成交单 |
| net_pct_xl | 超大单净占比(%) | 超大单净占比 = 超大单净额 / 成交额 |
| net_amount_l | 大单净额(万) | 大单：大于等于10万股或者20万元且小于50万股和100万元的成交单 |
| net_pct_l | 大单净占比(%) | 大单净占比 = 大单净额 / 成交额 |
| net_amount_m | 中单净额(万) | 中单：大于等于2万股或者4万元且小于10万股和20万元的成交单 |
| net_pct_m | 中单净占比(%) | 中单净占比 = 中单净额 / 成交额 |
| net_amount_s | 小单净额(万) | 小单：小于2万股和4万元的成交单 |
| net_pct_s | 小单净占比(%) | 小单净占比 = 小单净额 / 成交额 |

**返回**

返回一个 [pandas.DataFrame] 对象，默认的列索引为取得的全部字段. 如果给定了 fields 参数, 则列索引与给定的 fields 对应.

**示例**

```python
# 获取一只股票在一个时间段内的资金流量数据
get_money_flow('000001.XSHE', '2016-02-01', '2016-02-04')
get_money_flow('000001.XSHE', '2015-10-01', '2015-12-30', fields="change_pct")
get_money_flow(['000001.XSHE'], '2010-01-01', '2010-01-30', ["date", "sec_code", "change_pct", "net_amount_main", "net_pct_l", "net_amount_m"])

# 获取多只股票在一个时间段内的资金流向数据
get_money_flow(['000001.XSHE', '000040.XSHE', '000099.XSHE'], '2010-01-01', '2010-01-30')
# 获取多只股票在某一天的资金流向数据
get_money_flow(['000001.XSHE', '000040.XSHE', '000099.XSHE'], '2016-04-01', '2016-04-01')
```

## 获取龙虎榜数据

```python
get_billboard_list(stock_list, start_date, end_date, count)
```

获取指定日期区间内的龙虎榜数据

**参数**

- stock_list: 一个股票代码的 list。 当值为 None 时， 返回指定日期的所有股票。
- start_date:开始日期
- end_date: 结束日期
- count: 交易日数量， 可以与 end_date 同时使用， 表示获取 end_date 前 count 个交易日的数据(含 end_date 当日)

**返回值**

- pandas.DataFrame， 各 column 的含义如下:
- code: 股票代码
- day: 日期
- direction: ALL 表示『汇总』，SELL 表示『卖』，BUY 表示『买』
- abnormal_code: 异常波动类型
- abnormal_name: 异常波动名称
- sales_depart_name: 营业部名称
- rank: 0 表示汇总， 1~5 对应买入金额或卖出金额排名第一到第五
- buy_value:买入金额
- buy_rate:买入金额占比(买入金额/市场总成交额)
- sell_value:卖出金额
- sell_rate:卖出金额占比(卖出金额/市场总成交额)
- total_value:总额(买入金额 + 卖出金额)
- net_value:净额(买入金额 - 卖出金额)
- amount:市场总成交额

**异常波动类型**

| 参数编码 | 参数名称 |
| --- | --- |
| 106001 | 涨幅偏离值达7%的证券 |
| 106002 | 跌幅偏离值达7%的证券 |
| 106003 | 日价格振幅达到15%的证券 |
| 106004 | 换手率达20%的证券 |
| 106005 | 无价格涨跌幅限制的证券 |
| 106006 | 连续三个交易日内收盘价格涨幅偏离值累计达到20%的证券 |
| 106007 | 连续三个交易日内收盘价格跌幅偏离值累计达到20%的证券 |
| 106008 | 连续三个交易日内收盘价格涨幅偏离值累计达到15%的证券 |
| 106009 | 连续三个交易日内收盘价格跌幅偏离值累计达到15%的证券 |
| 106010 | 连续三个交易日内涨幅偏离值累计达到12%的ST证券、*ST证券和未完成股改证券 |
| 106011 | 连续三个交易日内跌幅偏离值累计达到12%的ST证券、*ST证券和未完成股改证券 |
| 106012 | 连续三个交易日的日均换手率与前五个交易日日均换手率的比值到达30倍 |
| 106013 | 单只标的证券的当日融资买入数量达到当日该证券总交易量的50％以上的证券 |
| 106014 | 单只标的证券的当日融券卖出数量达到当日该证券总交易量的50％以上的证券 |
| 106015 | 日价格涨幅达到20%的证券 |
| 106016 | 日价格跌幅达到-15%的证券 |
| 106099 | 其它异常波动的证券 |

**示例**

```python
# 获取2018-08-01的龙虎榜数据
get_billboard_list(stock_list=None, end_date = '2018-08-01', count =1)
```

## 上市公司分红送股（除权除息）数据

```python
from jqdata import finance
finance.run_query(query(finance.STK_XR_XD).filter(finance.STK_XR_XD.code==code).order_by(finance.STK_XR_XD.report_date).limit(n))
```

记录由上市公司年报、中报、一季报、三季报统计出的分红转增情况。

**参数：**

- **query(finance.STK_XR_XD)**：表示从finance.STK_XR_XD这张表中查询上市公司除权除息的数据，还可以指定所要查询的字段名，格式如下：query(库名.表名.字段名1，库名.表名.字段名2），多个字段用英文逗号进行分隔；query函数的更多用法详见：[sqlalchemy.orm.query.Query对象](https://docs.sqlalchemy.org/en/rel_1_0/orm/query.html)
- **finance.STK_XR_XD**：代表除权除息数据表，记录由上市公司年报、中报、一季报、三季报统计出的分红转增情况。表结构和字段信息如下：

| 字段名称 | 中文名称 | 字段类型 | 能否为空 | 含义 |
| --- | --- | --- | --- | --- |
| code | 股票代码 | varchar(12) | N | 加后缀 |
| company_id | 机构ID | int | N |  |
| company_name | 机构名称 | varchar(100) |  |  |
| report_date | 分红报告期 | date | N | 一般为：一季报:YYYY-03-31;中报:YYYY-06-30;三季报:YYYY-09-30;年报:YYYY-12-31同时也可能存在其他日期 |
| bonus_type | 分红类型 | varchar(60) |  | 201102新增,类型如下：年度分红 中期分红 季度分红 特别分红 向公众股东赠送 股改分红 |
| board_plan_pub_date | 董事会预案公告日期 | date |  |  |
| board_plan_bonusnote | 董事会预案分红说明 | varchar(500) |  | 每10股送XX转增XX派XX元 |
| distributed_share_base_board | 分配股本基数（董事会） | decimal(20,4) |  | 单位:万股 |
| shareholders_plan_pub_date | 股东大会预案公告日期 | date |  |  |
| shareholders_plan_bonusnote | 股东大会预案分红说明 | varchar(200) |  |  |
| distributed_share_base_shareholders | 分配股本基数（股东大会） | decimal(20,4) |  | 单位:万股 |
| implementation_pub_date | 实施方案公告日期 | date |  |  |
| implementation_bonusnote | 实施方案分红说明 | varchar(200) |  | 维护规则: 每10股送XX转增XX派XX元 或:不分配不转赠 |
| distributed_share_base_implement | 分配股本基数（实施） |  |  | 单位:万股 (如实施公告未披露则在登记日后1~2周内补充) |
| dividend_ratio | 送股比例 | decimal(20,4) |  | 每10股送XX股 (最新送股比例) |
| transfer_ratio | 转增比例 | decimal(20,4) |  | 每10股转增 XX股 ；(最新转增比例) |
| bonus_ratio_rmb | 派息比例(人民币) | decimal(20,4) |  | 每10股派 XX。说明：这里的比例为最新的分配比例，预案公布的时候，预案的分配基数在此维护，如果股东大会或实施方案发生变化，再次进行修改，保证此处为最新的分配基数 |
| bonus_ratio_usd | 派息比例（美元） | decimal(20,4) |  | 每10股派 XX。说明：这里的比例为最新的分配比例，预案公布的时候，预案的分配基数在此维护，如果股东大会或实施方案发生变化，再次进行修改，保证此处为最新的分配基数 如果这里只告诉了汇率，没有公布具体的外币派息，则要计算出； |
| bonus_ratio_hkd | 派息比例（港币） | decimal(20,4) |  | 每10股派 XX。说明：这里的比例为最新的分配比例，预案公布的时候，预案的分配基数在此维护，如果股东大会或实施方案发生变化，再次进行修改，保证此处为最新的分配基数 如果这里只告诉了汇率，没有公布具体的外币派息，则要计算出； |
| at_bonus_ratio_rmb | 税后派息比例（人民币） | decimal(20,4) |  |  |
| exchange_rate | 汇率 | decimal(20,4) |  | 当日以外币（美元或港币）计价的B股价格兑换成人民币的汇率 |
| dividend_number | 送股数量 | decimal(20,4) |  | 单位：万股 (如实施公告未披露则在登记日后1~2周内补充) |
| transfer_number | 转增数量 | decimal(20,4) |  | 单位：万股 (如实施公告未披露则在登记日后1~2周内补充) |
| bonus_amount_rmb | 派息金额(人民币) | decimal(20,4) |  | 单位：万元 (如实施公告未披露则在登记日后1~2周内补充) |
| a_registration_date | A股股权登记日 | date |  |  |
| b_registration_date | B股股权登记日 | date |  | B股股权登记存在**最后交易日，除权基准日以及股权登记日**三个日期，由于B股实行T+3制度，最后交易日持有的股份需要在3个交易日之后确定股东身份，然后在除权基准日进行除权。 |
| a_xr_date | A股除权日 | date |  |  |
| b_xr_baseday | B股除权基准日 | date |  | 根据B股实行T＋3交收制度,则B股的“股权登记日”是“最后交易日”后的第 三个交易日,直至“股权登记日”这一日为止,B股投资者的股权登记才告完成,也 就意味着B股股份至股权登记日为止,才真正划入B股投资者的名下。 |
| b_final_trade_date | B股最后交易日 | date |  |  |
| a_bonus_date | 派息日(A) | date |  |  |
| b_bonus_date | 派息日(B) | date |  |  |
| dividend_arrival_date | 红股到帐日 | date |  |  |
| a_increment_listing_date | A股新增股份上市日 | date |  |  |
| b_increment_listing_date | B股新增股份上市日 | date |  |  |
| total_capital_before_transfer | 送转前总股本 | decimal(20,4) |  | 单位：万股 |
| total_capital_after_transfer | 送转后总股本 | decimal(20,4) |  | 单位：万股 |
| float_capital_before_transfer | 送转前流通股本 | decimal(20,4) |  | 单位：万股 |
| float_capital_after_transfer | 送转后流通股本 | decimal(20,4) |  | 单位：万股 |
| note | 备注 | varchar(500) |  |  |
| a_transfer_arrival_date | A股转增股份到帐日 | date |  |  |
| b_transfer_arrival_date | B股转增股份到帐日 | date |  |  |
| b_dividend_arrival_date | B股送红股到帐日 | date |  | 20080801新增 |
| note_of_no_dividend | 有关不分配的说明 | varchar(1000) |  |  |
| plan_progress_code | 方案进度编码 | int |  |  |
| plan_progress | 方案进度 | varchar(60) |  | 董事会预案 实施方案 股东大会预案 取消分红 公司预案 延迟实施 |
| bonus_cancel_pub_date | 取消分红公告日期 | date |  |  |

- **filter(finance.STK_XR_XD.report_date==report_date)**：指定筛选条件，通过finance.STK_XR_XD.report_date==report_date可以指定你想要查询的分红报告期；除此之外，还可以对表中其他字段指定筛选条件，如finance.STK_XR_XD.code=='000001.XSHE'，表示筛选股票编码为000001.XSHE的数据； 多个筛选条件用英文逗号分隔。
- **order_by(finance.STK_XR_XD.report_date)**: 将返回结果按分红报告期排序
- **limit(n)**：限制返回的数据条数，n指定返回条数。

**返回结果：**

- 返回一个dataframe，每一行对应数据表中的一条数据，列索引是你所查询的字段名称。

**注意：**

1.  **为了防止返回数据量过大, 我们每次最多返回4000行**
    
2.  不能进行连表查询，即同时查询多张表的数据
    
    **示例：**
    
    ```python
    from jqdata import *
    q=query(finance.STK_XR_XD).filter(finance.STK_XR_XD.report_date>='2015-01-01').limit(10)
    df = finance.run_query(q)
    print(df)
    
     id company_id           company_name               code   report_date     bonus_type  \
    0  19  300000062  广东德美精细化工集团股份有限公司  002054.XSHE  2015-06-30       中期分红
    1  20  300000062  广东德美精细化工集团股份有限公司  002054.XSHE  2015-12-31       年度分红
    2  21  300000062  广东德美精细化工集团股份有限公司  002054.XSHE  2016-06-30       中期分红
    3  22  300000062  广东德美精细化工集团股份有限公司  002054.XSHE  2016-12-31       年度分红
    4  23  300000062  广东德美精细化工集团股份有限公司  002054.XSHE  2017-06-30       中期分红
    5  24  300000062  广东德美精细化工集团股份有限公司  002054.XSHE  2017-12-31       年度分红
    6  43  300000123     深圳市得润电子股份有限公司    002055.XSHE  2015-06-30       中期分红
    7  44  300000123     深圳市得润电子股份有限公司    002055.XSHE  2015-12-31       年度分红
    8  45  300000123     深圳市得润电子股份有限公司    002055.XSHE  2016-06-30       中期分红
    9  46  300000123     深圳市得润电子股份有限公司    002055.XSHE  2016-12-31       年度分红    board_plan_pub_date board_plan_bonusnote     distributed_share_base_board  \
    0          2015-08-29               不分配不转增                          NaN
    1          2016-04-27          10派1.2元(含税)                   41923.0828
    2          2016-08-27               不分配不转增                          NaN
    3          2017-04-25          10派1.2元(含税)                   41923.0828
    4          2017-08-29               不分配不转增                          NaN
    5          2018-04-27         10派0.47元(含税)                   41923.0828
    6          2015-07-25               不分配不转增                          NaN
    7          2016-04-23               不分配不转增                          NaN
    8          2016-08-27               不分配不转增                          NaN
    9          2017-04-29          10派0.2元(含税)                    45051.208    shareholders_plan_pub_date          ...           \
    0                        NaN          ...
    1                 2016-05-18          ...
    2                        NaN          ...
    3                 2017-05-17          ...
    4                        NaN          ...
    5                 2018-05-19          ...
    6                        NaN          ...
    7                 2016-05-14          ...
    8                        NaN          ...
    9                 2017-05-20          ...               float_capital_before_transfer    float_capital_after_transfer note  \
    0                           NaN                          NaN  NaN
    1                           NaN                          NaN  NaN
    2                           NaN                          NaN  NaN
    3                           NaN                          NaN  NaN
    4                           NaN                          NaN  NaN
    5                           NaN                          NaN  NaN
    6                           NaN                          NaN  NaN
    7                           NaN                          NaN  NaN
    8                           NaN                          NaN  NaN
    9                           NaN                          NaN  NaN
    
     a_transfer_arrival_date     b_transfer_arrival_date    b_dividend_arrival_date  \
    0                     NaN                     NaN                     NaN
    1                     NaN                     NaN                     NaN
    2                     NaN                     NaN                     NaN
    3                     NaN                     NaN                     NaN
    4                     NaN                     NaN                     NaN
    5                     NaN                     NaN                     NaN
    6                     NaN                     NaN                     NaN
    7                     NaN                     NaN                     NaN
    8                     NaN                     NaN                     NaN
    9                     NaN                     NaN                     NaN
    
      note_of_no_dividend    plan_progress_code  plan_progress     bonus_cancel_pub_date
    0                 NaN             313001         董事会预案                   NaN
    1                 NaN             313002          实施方案                   NaN
    2                 NaN             313001         董事会预案                   NaN
    3                 NaN             313002          实施方案                   NaN
    4                 NaN             313001         董事会预案                   NaN
    5                 NaN             313002          实施方案                   NaN
    6                 NaN             313001         董事会预案                   NaN
    7                 NaN             313003        股东大会预案                   NaN
    8                 NaN             313001         董事会预案                   NaN
    9                 NaN             313002          实施方案                   NaN
    ```
    

## 沪深市场每日成交概况

```python
from jqdata import finance
finance.run_query(query(finance.STK_EXCHANGE_TRADE_INFO).filter(finance.STK_EXCHANGE_TRADE_INFO.exchange_code==exchange_code).limit(n)
```

记录沪深两市股票交易的成交情况，包括市值、成交量，市盈率等情况。

**参数：**

- **query(finance.STK_EXCHANGE_TRADE_INFO)**：表示从finance.STK_EXCHANGE_TRADE_INFO这张表中查询沪深两市股票交易的成交情况，还可以指定所要查询的字段名，格式如下：query(库名.表名.字段名1，库名.表名.字段名2），多个字段用英文逗号进行分隔；query函数的更多用法详见：[sqlalchemy.orm.query.Query对象](https://docs.sqlalchemy.org/en/rel_1_0/orm/query.html)
- **finance.STK_EXCHANGE_TRADE_INFO**：代表沪深市场每日成交概况表，记录沪深两市股票交易的成交情况，包括市值、成交量，市盈率等情况，表结构和字段信息如下：

| 字段名称 | 中文名称 | 字段类型 | 能否为空 | 含义 |
| --- | --- | --- | --- | --- |
| exchange_code | 市场编码 | varchar(12) | N | 编码规则见下表 |
| exchange_name | 市场名称 | varchar(100) |  | 上海市场，上海A股，上海B股，深圳市场，深市主板，中小企业板，创业板 |
| date | 交易日期 | date | N |  |
| total_market_cap | 市价总值 | decimal(20,8) |  | 单位：亿 |
| circulating_market_cap | 流通市值 | decimal(20,8) |  | 单位：亿 |
| volume | 成交量 | decimal(20,4) |  | 单位：万 |
| money | 成交金额 | decimal(20,8) |  | 单位：亿 |
| deal_number | 成交笔数 | decimal(20,4) |  | 单位：万笔 |
| pe_average | 平均市盈率 | decimal(20,4) |  | 上海市场市盈率计算方法：市盈率＝∑(收盘价×发行数量)/∑(每股收益×发行数量)，统计时剔除亏损及暂停上市的上市公司。 深圳市场市盈率计算方法：市盈率＝∑市价总值/∑(总股本×上年每股利润)，剔除上年利润为负的公司。 |
| turnover_ratio | 换手率 | decimal(10,4) |  | 单位：％ |

市场编码名称对照表

| 市场编码 | 交易市场名称 | 备注 |
| --- | --- | --- |
| 322001 | 上海市场 |  |
| 322002 | 上海A股 |  |
| 322003 | 上海B股 |  |
| 322004 | 深圳市场 | 该市场交易所未公布成交量和成交笔数 |
| 322005 | 深市主板 |  |
| 322006 | 中小企业板 |  |
| 322007 | 创业板 |  |

- **filter(finance.STK_EXCHANGE_TRADE_INFO.date==date)**：指定筛选条件，通过finance.STK_EXCHANGE_TRADE_INFO.date==date可以指定你想要查询的交易日期；除此之外，还可以对表中其他字段指定筛选条件，如finance.STK_EXCHANGE_TRADE_INFO.exchange_code==322001，表示筛选市场编码为322001（上海市场）的数据；多个筛选条件用英文逗号分隔。
    
- **limit(n)**：限制返回的数据条数，n指定返回条数。
    

**返回结果：**

- 返回一个dataframe，每一行对应数据表中的一条数据，列索引是你所查询的字段名称。

**注意：**

1.  **为了防止返回数据量过大, 我们每次最多返回4000行**
    
2.  不能进行连表查询，即同时查询多张表的数据
    
    **示例：**
    

```python
q=query(finance.STK_EXCHANGE_TRADE_INFO).filter(finance.STK_EXCHANGE_TRADE_INFO.date>='2015-01-01').limit(10)
df=finance.run_query(q)
print(df)

      id  exchange_code    exchange_name        date     total_market_cap  \
0  14847         322002          上海A股  2015-01-05     252101.167063
1  14848         322003          上海B股  2015-01-05        883.102583
2  14849         322001          上海市场  2015-01-05     252984.269645
3  14850         322006         中小企业板  2015-01-05      51786.890000
4  14851         322005          深市主板  2015-01-05      57235.450000
5  14852         322004          深圳市场  2015-01-05     130625.770000
6  14853         322007           创业板  2015-01-05      21603.430000
7  14854         322002          上海A股  2015-01-06     252786.779098
8  14855         322003          上海B股  2015-01-06        879.903673
9  14856         322001          上海市场  2015-01-06     253666.682771

   circulating_market_cap        volume        money  deal_number  pe_average  \
0           228118.117416  5.321700e+06  5504.189763    1800.6098      16.576
1              883.102583  7.334709e+03     4.510566       3.7579      15.987
2           229001.219999  5.335211e+06  5511.112029    1804.4529      16.574
3            36548.430000  5.987000e+05   845.890000     381.6300      41.660
4            47395.540000  1.412500e+06  1598.710000     579.6500      26.010
5            96936.140000           NaN  2789.140000          NaN      34.600
6            12992.170000  1.793000e+05   344.530000     140.9500      63.790
7           228171.900720  5.011329e+06  5321.072770    1817.5373      16.581
8              879.903673  6.242410e+03     3.806482       3.0057      15.922
9           229051.804393  5.021845e+06  5328.157451    1820.6523      16.579

   turnover_ratio
0          2.1486
1          0.4856
2          2.1385
3             NaN
4             NaN
5          3.2800
6             NaN
7          2.0226
8          0.4133
9          2.0128
```

## 市场通（沪港通，深港通和港股通）

### 合格证券变动记录

```python
from jqdata import finance
finance.run_query(query(finance.STK_EL_CONST_CHANGE).filter(finance.STK_EL_CONST_CHANGE.code==code).limit(n))
```

记录沪港通、深港通和港股通的成分股的变动情况。

**参数：**

- **query(finance.STK_EL_CONST_CHANGE)**：表示从finance.STK_EL_CONST_CHANGE这张表中查询沪港通、深港通和港股通成分股的变动记录，还可以指定所要查询的字段名，格式如下：query(库名.表名.字段名1，库名.表名.字段名2），多个字段用英文逗号进行分隔；query函数的更多用法详见：[sqlalchemy.orm.query.Query对象](https://docs.sqlalchemy.org/en/rel_1_0/orm/query.html)
    
    **finance.STK_EL_CONST_CHANGE**：记录沪港通、深港通和港股通成分股的变动情况，包括交易类型，变更日期，变更方向等，表结构和字段信息如下：
    

| 字段 | 名称 | 类型 | 备注/示例 |
| --- | --- | --- | --- |
| link_id | 交易类型编码 | int | 同市场通编码 |
| link_name | 交易类型名称 | varchar(12) |  |
| code | 证券代码 | varchar(12) |  |
| name_ch | 中文简称 | varchar(30) |  |
| name_en | 英文简称 | varchar(120) |  |
| exchange | 该股票所在的交易所 | varchar(12) | 上海市场:XSHG/深圳市场:XSHE/香港市场:XHKG |
| change_date | 变更日期 | date |  |
| direction | 变更方向 | varchar(6) | IN/OUT（分别为纳入和剔除） |

- **filter(finance.STK_EL_CONST_CHANGE.code==code)**：指定筛选条件，通过finance.STK_EL_CONST_CHANGE.code==code可以指定你想要查询的股票代码；除此之外，还可以对表中其他字段指定筛选条件，如finance.STK_EL_CONST_CHANGE.change_date>='2015-01-01'，表示筛选变更日期大于等于2015年1月1日之后的数据；多个筛选条件用英文逗号分隔。
- **order_by(finance.STK_EL_CONST_CHANGE.change_date)**: 将返回结果按变更日期排序
- **limit(n)**：限制返回的数据条数，n指定返回条数。

**返回结果：**

- 返回一个 dataframe， 每一行对应数据表中的一条数据， 列索引是你所查询的字段名称

**注意：**

1.  **为了防止返回数据量过大, 我们每次最多返回4000行**
    
2.  不能进行连表查询，即同时查询多张表的数据
    
    **示例：**
    

```python
q=query(finance.STK_EL_CONST_CHANGE).filter(finance.STK_EL_CONST_CHANGE.link_id==310001).order_by(finance.STK_EL_CONST_CHANGE.change_date).limit(10)
df=finance.run_query(q)
print(df)

id link_id link_name         code name_ch name_en exchange change_date  \
0  536  310001       沪股通  600000.XSHG    浦发银行     NaN     XSHG  2014-11-17
1  537  310001       沪股通  600004.XSHG    白云机场     NaN     XSHG  2014-11-17
2  539  310001       沪股通  600007.XSHG    中国国贸     NaN     XSHG  2014-11-17
3  540  310001       沪股通  600008.XSHG    首创股份     NaN     XSHG  2014-11-17
4  541  310001       沪股通  600009.XSHG    上海机场     NaN     XSHG  2014-11-17
5  542  310001       沪股通  600010.XSHG    包钢股份     NaN     XSHG  2014-11-17
6  543  310001       沪股通  600011.XSHG    华能国际     NaN     XSHG  2014-11-17
7  544  310001       沪股通  600012.XSHG    皖通高速     NaN     XSHG  2014-11-17
8  545  310001       沪股通  600015.XSHG    华夏银行     NaN     XSHG  2014-11-17
9  546  310001       沪股通  600016.XSHG    民生银行     NaN     XSHG  2014-11-17
```

### 市场通交易日历

```python
from jqdata import finance
finance.run_query(query(finance.STK_EXCHANGE_LINK_CALENDAR).filter(finance.STK_EXCHANGE_LINK_CALENDAR.day==day).limit(n))
```

记录沪港通、深港通和港股通每天是否开市。

**参数：**

- **query(finance.STK_EXCHANGE_LINK_CALENDAR)**：表示从finance.STK_EXCHANGE_LINK_CALENDAR这张表中查询市场沪港通、深港通和港股通交易日历的信息，还可以指定所要查询的字段名，格式如下：query(库名.表名.字段名1，库名.表名.字段名2），多个字段用英文逗号进行分隔；query函数的更多用法详见：[sqlalchemy.orm.query.Query对象](https://docs.sqlalchemy.org/en/rel_1_0/orm/query.html)
    
    **finance.STK_EXCHANGE_LINK_CALENDAR**：代表了市场通交易日历表，记录沪港通、深港通和港股通每天是否开市，包括交易日期，交易日类型等，表结构和字段信息如下：
    

| 字段 | 名称 | 类型 | 备注/示例 |
| --- | --- | --- | --- |
| day | 交易日期 | date |  |
| link_id | 市场通编码 | int |  |
| link_name | 市场通名称 | varchar(32) | 包括以下四个名称： 沪股通， 深股通， 港股通(沪)， 港股通(深) |
| type_id | 交易日类型编码 | int | 如下 交易日类型编码 |
| type | 交易日类型 | varchar(32) |  |

**附注**

港股通（沪）和港股通（深）的交易日在深港通开展后是一致的。

**交易日类型编码**

| 交易日类型编码 | 交易日类型 |
| --- | --- |
| 312001 | 正常交易日 |
| 312003 | 休市 |

**市场通编码**

| 市场通编码 | 市场通名称 |
| --- | --- |
| 310001 | 沪股通 |
| 310002 | 深股通 |
| 310003 | 港股通（沪） |
| 310004 | 港股通（深） |

- **filter(finance.STK_EXCHANGE_LINK_CALENDAR.day==day)**：指定筛选条件，通过finance.STK_EXCHANGE_LINK_CALENDAR.day==day可以指定你想要查询的日期；除此之外，还可以对表中其他字段指定筛选条件，如finance.STK_EXCHANGE_LINK_CALENDAR.type_id=='312001'，表示筛选交易日类型为正常交易日的数据；多个筛选条件用英文逗号分隔。
- **limit(n)**：限制返回的数据条数，n指定返回条数。

**返回结果：**

- 返回一个 dataframe， 每一行对应数据表中的一条数据， 列索引是你所查询的字段名称

**注意：**

1.  **为了防止返回数据量过大, 我们每次最多返回4000行**
    
2.  不能进行连表查询，即同时查询多张表的数据
    
    **示例：**
    

```python
q=query(finance.STK_EXCHANGE_LINK_CALENDAR).filter(finance.STK_EXCHANGE_LINK_CALENDAR.day>='2015-01-01').limit(10)
df=finance.run_query(q)
print(df)

        id       day   link_id    link_name type_id    type
0  1244830  2015-01-01  310001       沪股通  312003   全天休市
1      145  2015-01-01  310003    港股通(沪)  312003   全天休市
2  1244831  2015-01-02  310001       沪股通  312003   全天休市
3      146  2015-01-02  310003    港股通(沪)  312003   全天休市
4  1244832  2015-01-03  310001       沪股通  312003   全天休市
5      147  2015-01-03  310003    港股通(沪)  312003   全天休市
6  1244833  2015-01-04  310001       沪股通  312003   全天休市
7      148  2015-01-04  310003    港股通(沪)  312003   全天休市
8  1244834  2015-01-05  310001       沪股通  312001  正常交易日
9      149  2015-01-05  310003    港股通(沪)  312001  正常交易日
```

### 市场通十大成交活跃股

```python
from jqdata import finance
finance.run_query(query(finance.STK_EL_TOP_ACTIVATE).filter(finance.STK_EL_TOP_ACTIVATE.code==code).limit(n))
```

统计沪港通、深港通和港股通前十大交易活跃股的交易状况。

**参数：**

- **query(finance.STK_EL_TOP_ACTIVATE)**：表示从finance.STK_EL_TOP_ACTIVATE这张表中查询沪港通、深港通和港股通前十大交易活跃股的交易状况，还可以指定所要查询的字段名，格式如下：query(库名.表名.字段名1，库名.表名.字段名2），多个字段用英文逗号进行分隔；query函数的更多用法详见：[sqlalchemy.orm.query.Query对象](http://docs.sqlalchemy.org/en/rel_1_0/orm/query.html)
    
    **finance.STK_EL_TOP_ACTIVATE**：代表了市场通十大成交活跃股表，统计沪港通、深港通和港股通前十大交易活跃股的交易状况，包括买入金额，卖出金额等，表结构和字段信息如下：
    

| 字段 | 名称 | 类型 | 备注/示例 |
| --- | --- | --- | --- |
| day | 日期 | date |  |
| link_id | 市场通编码 | int |  |
| link_name | 市场通名称 | varchar(32) | 包括以下四个名称： 沪股通， 深股通， 港股通(沪)， 港股通(深) |
| rank | 排名 | int |  |
| code | 股票代码 | varchar(12) |  |
| name | 股票名称 | varchar(100) |  |
| exchange | 交易所名称 | varchar(12) |  |
| buy | 买入金额(元) | decimal(20, 4) | (北向自2024-08-18之后不再披露) |
| sell | 卖出金额(元) | decimal(20, 4) | (北向自2024-08-18之后不再披露) |
| total | 买入及卖出金额(元) | decimal(20, 4) |  |

**市场通编码**

| 市场通编码 | 市场通名称 |
| --- | --- |
| 310001 | 沪股通 |
| 310002 | 深股通 |
| 310003 | 港股通（沪） |
| 310004 | 港股通（深） |

- **filter(finance.STK_EL_TOP_ACTIVATE.code==code)**：指定筛选条件，通过finance.STK_EL_TOP_ACTIVATE.code==code可以指定你想要查询的股票代码；除此之外，还可以对表中其他字段指定筛选条件，如finance.STK_EL_TOP_ACTIVATE.day>='2015-01-01'，表示筛选日期大于等于2015年1月1日之后的数据；多个筛选条件用英文逗号分隔。
- **limit(n)**：限制返回的数据条数，n指定返回条数。

**返回结果：**

- 返回一个 dataframe， 每一行对应数据表中的一条数据， 列索引是你所查询的字段名称

**注意：**

1.  **为了防止返回数据量过大, 我们每次最多返回4000行**
    
2.  不能进行连表查询，即同时查询多张表的数据
    
    **示例：**
    

```python
q=query(finance.STK_EL_TOP_ACTIVATE).filter(finance.STK_EL_TOP_ACTIVATE.code=='000002.XSHE').limit(10)
df=finance.run_query(q)
print(df)

       id         day link_id     link_name rank       code   name     exchange  \
0  323010  2018-01-15  310002       深股通    2  000002.XSHE  万科Ａ      深交所
1  323050  2018-01-16  310002       深股通    2  000002.XSHE  万科Ａ      深交所
2  323089  2018-01-17  310002       深股通    1  000002.XSHE  万科Ａ      深交所
3  323132  2018-01-18  310002       深股通    4  000002.XSHE  万科Ａ      深交所
4  323213  2018-01-23  310002       深股通    6  000002.XSHE  万科Ａ      深交所
5  323254  2018-01-24  310002       深股通    7  000002.XSHE  万科Ａ      深交所
6  341170  2018-01-25  310002       深股通    7  000002.XSHE  万科Ａ      深交所
7  341209  2018-01-26  310002       深股通    6  000002.XSHE  万科Ａ      深交所
8  341248  2018-01-29  310002       深股通    5  000002.XSHE  万科Ａ      深交所
9  341444  2018-01-30  310002       深股通    5  000002.XSHE  万科Ａ      深交所

           buy         sell        total
0  124497968.0  326656496.0  451154464.0
1  127460061.0  465933921.0  593393982.0
2  157676630.0  542617116.0  700293746.0
3  203996076.0  105819761.0  309815837.0
4  141515523.0  190282952.0  331798475.0
5  110052973.0  163321615.0  273374588.0
6  179785644.0  120157651.0  299943295.0
7  166750550.0   78471253.0  245221803.0
8  157899558.0  170790111.0  328689669.0
9  201547219.0  165714289.0  367261508.0
```

### 市场通成交与额度信息

```python
from jqdata import finance
finance.run_query(query(finance.STK_ML_QUOTA).filter(finance.STK_ML_QUOTA.day==day).limit(n))
```

记录沪股通、深股通和港股通每个交易日的成交与额度的控制情况。

**参数：**

- **query(finance.STK_ML_QUOTA)**：表示从finance.STK_ML_QUOTA这张表中查询沪港通、深港通和港股通的成交与额度信息，还可以指定所要查询的字段名，格式如下：query(库名.表名.字段名1，库名.表名.字段名2），多个字段用英文逗号进行分隔；query函数的更多用法详见：[sqlalchemy.orm.query.Query对象](http://docs.sqlalchemy.org/en/rel_1_0/orm/query.html)
- **finance.STK_ML_QUOTA**：代表了市场通成交与额度信息表，记录了沪港通、深港通和港股通成交与额度的信息，包括买入、卖出等，表结构和字段信息如下：

| 字段 | 名称 | 类型 | 备注/示例 |
| --- | --- | --- | --- |
| day | 交易日期 | date |  |
| link_id | 市场通编码 | int |  |
| link_name | 市场通名称 | varchar(32) | 包括以下四个名称： 沪股通，深股通，港股通(沪）,港股通(深）;其中沪股通和深股通属于北向资金，港股通（沪）和港股通（深）属于南向资金。 |
| currency_id | 货币编码 | int |  |
| currency | 货币名称 | varchar(16) |  |
| buy_amount | 买入成交额 | decimal(20,4) | 亿(自2024-08-18之后北向不再披露) |
| buy_volume | 买入成交数 | decimal(20,4) | 笔(自2024-08-18之后北向不再披露) |
| sell_amount | 卖出成交额 | decimal(20,4) | 亿(自2024-08-18之后北向不再披露) |
| sell_volume | 卖出成交数 | decimal(20,4) | 笔(自2024-08-18之后北向不再披露) |
| sum_amount | 累计成交额 | decimal(20,4) | 买入成交额+卖出成交额 |
| sum_volume | 累计成交数目 | decimal(20,4) | 买入成交量+卖出成交量 |
| quota | 总额度 | decimal(20, 4) | 亿（2016-08-16号起，沪港通和深港通不再设总额度限制） |
| quota_balance | 总额度余额 | decimal(20, 4) | 亿 |
| quota_daily | 每日额度 | decimal(20, 4) | 亿 (自2024-08-18之后不再披露) |
| quota_daily_balance | 每日额度余额 | decimal(20, 4) | 亿 (自2024-08-18之后不再披露) |

**货币编码**

| 货币编码 | 货币名称 |
| --- | --- |
| 110001 | 人民币 |
| 110003 | 港元 |

**市场通编码**

| 市场通编码 | 市场通名称 |
| --- | --- |
| 310001 | 沪股通 |
| 310002 | 深股通 |
| 310003 | 港股通（沪） |
| 310004 | 港股通（深） |

- **filter(finance.STK_ML_QUOTA.day==day)**：指定筛选条件，通过finance.STK_ML_QUOTA.day==day可以指定你想要查询的日期；除此之外，还可以对表中其他字段指定筛选条件，如finance.STK_ML_QUOTA.link_id==310001，表示筛选市场通编码为310001（沪股通）的数据；多个筛选条件用英文逗号分隔。
- **limit(n)**：限制返回的数据条数，n指定返回条数。

**返回结果：**

- 返回一个 dataframe， 每一行对应数据表中的一条数据， 列索引是你所查询的字段名称

**注意：**

1.  **为了防止返回数据量过大, 我们每次最多返回4000行**
    
2.  不能进行连表查询，即同时查询多张表的数据
    
    **示例：**
    

```python
q=query(finance.STK_ML_QUOTA).filter(finance.STK_ML_QUOTA.day>='2015-01-01').limit(10)
df=finance.run_query(q)
print(df)

    id         day link_id    link_name     currency_id   currency_name  buy_amount  \
0  183  2015-01-05  310001       沪股通      110001           人民币      40.01
1  271  2015-01-05  310003    港股通(沪)      110003            港元      20.51
2  182  2015-01-06  310001       沪股通      110001           人民币       32.4
3  270  2015-01-06  310003    港股通(沪)      110003            港元      11.15
4  181  2015-01-07  310001       沪股通      110001           人民币      20.43
5  269  2015-01-07  310003    港股通(沪)      110003            港元      10.28
6  180  2015-01-08  310001       沪股通      110001           人民币      22.31
7  268  2015-01-08  310003    港股通(沪)      110003            港元       7.86
8  179  2015-01-09  310001       沪股通      110001           人民币       34.7
9  267  2015-01-09  310003    港股通(沪)      110003            港元      11.16

  buy_volume  sell_amount  sell_volume sum_amount sum_volume quota  \
0    96819.0       19.98     48515.0      59.99   145334.0   NaN
1    33888.0        5.22     12241.0      25.73    46129.0   NaN
2    67392.0       32.64     76188.0      65.04   143580.0   NaN
3    22180.0        2.88      6806.0      14.03    28986.0   NaN
4    62539.0       17.01     39833.0      37.44   102372.0   NaN
5    21663.0        2.85      6296.0      13.13    27959.0   NaN
6    53725.0       21.74     62294.0      44.05   116019.0   NaN
7    15741.0        2.95      7050.0      10.81    22791.0   NaN
8   128236.0       20.17     51436.0      54.87   179672.0   NaN
9    21465.0        4.47      8845.0      15.63    30310.0   NaN

  quota_balance  quota_daily    quota_daily_balance
0           NaN       130.0               83.11
1           NaN       105.0                87.7
2           NaN       130.0              109.09
3           NaN       105.0               95.32
4           NaN       130.0              112.47
5           NaN       105.0               95.91
6           NaN       130.0              119.22
7           NaN       105.0               98.63
8           NaN       130.0              113.83
9           NaN       105.0               96.98
```

### 市场通汇率

```python
from jqdata import finance
finance.run_query(query(finance.STK_EXCHANGE_LINK_RATE).filter(finance.STK_EXCHANGE_LINK_RATE.day==day).limit(n))
```

包含2014年11月起人民币和港币之间的参考汇率/结算汇兑比率信息。

**参数：**

- **query(finance.STK_EXCHANGE_LINK_RATE)**：表示从finance.STK_EXCHANGE_LINK_RATE这张表中查询汇率信息，还可以指定所要查询的字段名，格式如下：query(库名.表名.字段名1，库名.表名.字段名2），多个字段用英文逗号进行分隔；query函数的更多用法详见：[sqlalchemy.orm.query.Query对象](http://docs.sqlalchemy.org/en/rel_1_0/orm/query.html)
    
    **finance.STK_EXCHANGE_LINK_RATE**：代表了市场通汇率表，记录参考汇率/结算汇兑比率信息，包括买入参考/结算汇率、卖出参考/结算汇率等，表结构和字段信息如下：
    

| 字段 | 名称 | 类型 | 备注/示例 |
| --- | --- | --- | --- |
| day | 日期 | Date |  |
| link_id | 市场通编码 | int |  |
| link_name | 市场通名称 | varchar(32) | 以“港股通(沪)”为代表 |
| domestic_currency | 本币 | varchar(12) | RMB |
| foreign_currency | 外币 | varchar(12) | HKD |
| refer_bid_rate | 买入参考汇率 | decimal(10, 5) |  |
| refer_ask_rate | 卖出参考汇率 | decimal(10, 5) |  |
| settle_bid_rate | 买入结算汇率 | decimal(10, 5) |  |
| settle_ask_rate | 卖出结算汇率 | decimal(10, 5) |  |

**市场通编码**

| 市场通编码 | 市场通名称 |
| --- | --- |
| 310003 | 港股通（沪） |
| 310004 | 港股通（深） |

- **filter(finance.STK_EXCHANGE_LINK_RATE.day==day)**：指定筛选条件，通过finance.STK_EXCHANGE_LINK_RATE.day==day可以指定你想要查询的日期；除此之外，还可以对表中其他字段指定筛选条件，如finance.STK_EXCHANGE_LINK_RATE.link_id==310001，表示筛选市场通编码为310001（沪股通）的数据；多个筛选条件用英文逗号分隔。
- **limit(n)**：限制返回的数据条数，n指定返回条数。

**返回结果：**

- 返回一个 dataframe， 每一行对应数据表中的一条数据， 列索引是你所查询的字段名称

**注意：**

1.  **为了防止返回数据量过大, 我们每次最多返回4000行**
    
2.  不能进行连表查询，即同时查询多张表的数据
    
    **示例：**
    

```python
q=query(finance.STK_EXCHANGE_LINK_RATE).filter(finance.STK_EXCHANGE_LINK_RATE.day>='2015-01-01').limit(10)
df=finance.run_query(q)
print(df)

   id         day link_id    link_name        domestic_currency   foreign_currency  \
0  31  2015-01-05  310003    港股通(沪)               RMB              HKD
1  32  2015-01-06  310003    港股通(沪)               RMB              HKD
2  33  2015-01-07  310003    港股通(沪)               RMB              HKD
3  34  2015-01-08  310003    港股通(沪)               RMB              HKD
4  35  2015-01-09  310003    港股通(沪)               RMB              HKD
5  36  2015-01-12  310003    港股通(沪)               RMB              HKD
6  37  2015-01-13  310003    港股通(沪)               RMB              HKD
7  38  2015-01-14  310003    港股通(沪)               RMB              HKD
8  39  2015-01-15  310003    港股通(沪)               RMB              HKD
9  40  2015-01-16  310003    港股通(沪)               RMB              HKD

  refer_bid_rate   refer_ask_rate  settle_bid_rate   settle_ask_rate
0         0.7774         0.8254         0.80317         0.80283
1         0.7785         0.8267         0.80307         0.80213
2         0.7777         0.8259         0.80197         0.80163
3         0.7773         0.8253         0.80116         0.80144
4         0.7776         0.8258           0.802          0.8014
5         0.7771         0.8251         0.80176         0.80044
6         0.7758         0.8238          0.7999          0.7997
7         0.7755         0.8235         0.79973         0.79927
8         0.7752         0.8232         0.79983         0.79857
9         0.7744         0.8222         0.79597         0.80063
```

### 沪深港通持股数据

```
from jqdata import finance
df=finance.run_query(query(finance.STK_HK_HOLD_INFO).filter(finance.STK_HK_HOLD_INFO.link_id==310001))
print(df)
```

记录了北向资金（沪股通、深股通）和南向资金港股通的持股数量和持股比例，数据从2017年3月17号开始至今，一般在盘前6:30左右更新昨日数据。
北向数据自 2024-08-17 开始, 改为按季度披露

**参数：**

- **query(finance.STK_HK_HOLD_INFO)**：表示从finance.STK_HK_HOLD_INFO这张表中查询沪深港通的持股数据，还可以指定所要查询的字段名，格式如下：query(库名.表名.字段名1，库名.表名.字段名2），多个字段用英文逗号分隔进行提取；如query(finance.STK_HK_HOLD_INFO.code)。query函数的更多用法详见：[query简易教程](https://www.joinquant.com/view/community/detail/16411)。
- **finance.STK_HK_HOLD_INFO**：收录了沪深港通每日的持股数量和持股比例数据，表结构和字段信息如下：

| 字段名称 | 中文名称 | 字段类型 | 能否为空 | 注释 |
| --- | --- | --- | --- | --- |
| day | 日期 | date | N | 北向自2024-08-18之后按照季度进行披露 |
| link_id | 市场通编码 | int | N | 三种类型：310001-沪股通，310002-深股通，310005-港股通 |
| link_name | 市场通名称 | varchar(32) | N | 三种类型：沪股通，深股通，港股通 |
| code | 股票代码 | varchar(12) | N |  |
| name | 股票名称 | varchar(100) | N |  |
| share_number | 持股数量 | int |  | 单位：股，于中央结算系统的持股量 |
| share_ratio | 持股比例 | decimal(10,4) |  | 单位：％，沪股通（占流通股百分比）：占于上交所上市及交易的A股总数的百分比；深股通（占总股本百分比）：占于深交所上市及交易的A股总数的百分比；港股通（占总股本百分比）：占已发行股份百分比 |

- **filter(finance.STK_HK_HOLD_INFO.link_id==310001)**：指定筛选条件，通过finance.STK_HK_HOLD_INFO.link_id==310001可以指定查询沪股通的持股数据；除此之外，还可以对表中其他字段指定筛选条件，如finance.STK_HK_HOLD_INFO.day=='2019-03-01'，指定获取2019年3月1日的沪深港通持股数据。
- **limit(n)**：限制返回的数据条数，n指定返回条数。

**返回结果：**

- 返回一个 dataframe，每一行对应数据表中的一条数据， 列索引是您所查询的字段名称

**注意：**

1.  为了防止返回数据量过大, 我们每次最多返回4000行
2.  不能进行连表查询，即同时查询多张表的数据

**示例：**

```python
#获取北向资金沪股通的持股数据
from jqdata import finance
df=finance.run_query(query(finance.STK_HK_HOLD_INFO).filter(finance.STK_HK_HOLD_INFO.link_id==310001).order_by(finance.STK_HK_HOLD_INFO.day.desc()))
print(df)

    id      day        link_id  link_name   code     name    share_number   share_ratio
0    1319365 2019-03-01  310001  沪股通 603997.XSHG 继峰股份    2905091        0.46
1    1319364 2019-03-01  310001  沪股通 603993.XSHG 洛阳钼业    140398591      0.79
2    1319363 2019-03-01  310001  沪股通 603989.XSHG 艾华集团    6574106        1.68
3    1319362 2019-03-01  310001  沪股通 603986.XSHG 兆易创新    1851725        0.89
4    1319361 2019-03-01  310001  沪股通 603979.XSHG 金诚信      191590         0.03
5    1319360 2019-03-01  310001  沪股通 603959.XSHG 百利科技    81666          0.05
6    1319359 2019-03-01  310001  沪股通 603939.XSHG 益丰药房    21973169       6.05
7    1319358 2019-03-01  310001  沪股通 603929.XSHG 亚翔集成    156924         0.16
8    1319357 2019-03-01  310001  沪股通 603899.XSHG 晨光文具    4751149        0.51
9    1319356 2019-03-01  310001  沪股通 603898.XSHG 好莱客      1843470        0.59
10    1319355 2019-03-01  310001  沪股通 603897.XSHG 长城科技    168377          0.37
...
```

## 上市公司概况

### 上市公司基本信息

```python
from jqdata import finance
finance.run_query(query(finance.STK_COMPANY_INFO).filter(finance.STK_COMPANY_INFO.code==code).limit(n))
```

获取上市公司最新公布的基本信息，包含注册资本，主营业务，行业分类等。

**参数：**

- **query(finance.STK_COMPANY_INFO)**：表示从finance.STK_COMPANY_INFO这张表中查询上市公司最新公布的基本信息，还可以指定所要查询的字段名，格式如下：query(库名.表名.字段名1，库名.表名.字段名2），多个字段用英文逗号进行分隔；query函数的更多用法详见：[sqlalchemy.orm.query.Query对象](http://docs.sqlalchemy.org/en/rel_1_0/orm/query.html)
    
    **finance.STK_COMPANY_INFO**：代表上市公司基本信息表，收录了上市公司最新公布的基本信息，表结构和字段信息如下：
    

| 字段名称 | 中文名称 | 字段类型 | 备注/示例 |
| --- | --- | --- | --- |
| company_id | 公司ID | int |  |
| code | 证券代码 | varchar(12) | 多证券代码的优先级：A股>B股 |
| full_name | 公司名称 | varchar(100) |  |
| short_name | 公司简称 | varchar(40) |  |
| a_code | A股股票代码 | varchar(12) |  |
| b_code | B股股票代码 | varchar(12) |  |
| h_code | H股股票代码 | varchar(12) |  |
| fullname_en | 英文名称 | varchar(100) |  |
| shortname_en | 英文简称 | varchar(40) |  |
| legal_representative | 法人代表 | varchar(40) |  |
| register_location | 注册地址 | varchar(100) |  |
| office_address | 办公地址 | varchar(150) |  |
| zipcode | 邮政编码 | varchar(10) |  |
| register_capital | 注册资金 | decimal(20,4) | 单位：万元 |
| currency_id | 货币编码 | int |  |
| currency | 货币名称 | varchar(32) |  |
| establish_date | 成立日期 | date |  |
| website | 机构网址 | varchar(80) |  |
| email | 电子信箱 | varchar(80) |  |
| contact_number | 联系电话 | varchar(60) |  |
| fax_number | 联系传真 | varchar(60) |  |
| main_business | 主营业务 | varchar(500) |  |
| business_scope | 经营范围 | varchar(4000) |  |
| description | 机构简介 | varchar(4000) |  |
| tax_number | 税务登记号 | varchar(50) |  |
| license_number | 法人营业执照号 | varchar(40) |  |
| pub_newspaper | 指定信息披露报刊 | varchar(120) |  |
| pub_website | 指定信息披露网站 | varchar(120) |  |
| secretary | 董事会秘书 | varchar(40) |  |
| secretary_number | 董秘联系电话 | varchar(60) |  |
| secretary_fax | 董秘联系传真 | varchar(60) |  |
| secretary_email | 董秘电子邮箱 | varchar(80) |  |
| security_representative | 证券事务代表 | varchar(40) |  |
| province_id | 所属省份编码 | varchar(12) |  |
| province | 所属省份 | varchar(60) |  |
| city_id | 所属城市编码 | varchar(12) |  |
| city | 所属城市 | varchar(60) |  |
| industry_id | 行业编码 | varchar(12) | 证监会行业分类 |
| industry_1 | 行业一级分类 | varchar(60) |  |
| industry_2 | 行业二级分类 | varchar(60) |  |
| cpafirm | 会计师事务所 | varchar(200) |  |
| lawfirm | 律师事务所 | varchar(200) |  |
| ceo | 总经理 | varchar(100) |  |
| comments | 备注 | varchar(300) |  |

- **filter(finance.STK_COMPANY_INFO.code==code)**：指定筛选条件，通过finance.STK_COMPANY_INFO.code==code可以指定你想要查询的股票代码；除此之外，还可以对表中其他字段指定筛选条件，如finance.STK_COMPANY_INFO.city==’北京市’，表示所属城市为北京市；多个筛选条件用英文逗号分隔。
- **limit(n)**：限制返回的数据条数，n指定返回条数。

**返回结果：**

- 返回一个 dataframe， 每一行对应数据表中的一条数据， 列索引是你所查询的字段名称

**注意：**

1.  **为了防止返回数据量过大, 我们每次最多返回4000行**
2.  不能进行连表查询，即同时查询多张表的数据

**示例：**

```python
# 指定查询对象为恒瑞医药（600276.XSHG)的上市公司基本信息，限定返回条数为10
q=query(finance.STK_COMPANY_INFO).filter(finance.STK_COMPANY_INFO.code=='600276.XSHG').limit(10)
df=finance.run_query(q)
print(df)

     id company_id         code            full_name     short_name  a_code b_code  \
0  2474  420600276  600276.XSHG  江苏恒瑞医药股份有限公司       恒瑞医药  600276    NaN

  h_code                        fullname_en       shortname_en  \
0    NaN  Jiangsu Hengrui Medicine Co., Ltd.  Hengrui Medicine

                         ...                             province city_id  city  \
0                        ...                               江苏  320700  连云港市

  industry_id   industry_1    industry_2                          cpafirm    \
0         C27        制造业      医药制造业  江苏苏亚金诚会计师事务所(特殊普通合伙)

       lawfirm     ceo                                            comments
0  浩天律师事务所  周云曙   公司是国内少有的在研发方面投入较大的企业，现有多个品种在研，不仅在国内建                           立了研究机构，投入较...

[1 rows x 45 columns]
```

### 上市公司状态变动

```python
from jqdata import finance
finance.run_query(query(finance.STK_STATUS_CHANGE).filter(finance.STK_STATUS_CHANGE.code==code).limit(n))
```

获取上市公司已发行未上市、正常上市、实行ST、*ST、暂停上市、终止上市的变动情况等

**参数：**

- **query(finance.STK_STATUS_CHANGE)**：表示从finance.STK_STATUS_CHANGE这张表中查询上市公司的状态变动信息，还可以指定所要查询的字段名，格式如下：query(库名.表名.字段名1，库名.表名.字段名2），多个字段用英文逗号进行分隔；query函数的更多用法详见：[sqlalchemy.orm.query.Query对象](http://docs.sqlalchemy.org/en/rel_1_0/orm/query.html)
    
- **finance.STK_STATUS_CHANGE**：代表上市公司状态变动表，收录了上市公司已发行未上市、正常上市、实行ST、*ST、暂停上市、终止上市的变动情况等，表结构和字段信息如下：
    
    | 字段名称 | 中文名称 | 字段类型 | 备注/示例 |
    | --- | --- | --- | --- |
    | company_id | 机构ID | int |  |
    | code | 股票代码 | varchar(12) |  |
    | name | 股票名称 | varchar(40) |  |
    | pub_date | 公告日期 | date |  |
    | change_date | 变更日期 | date |  |
    | public_status_id | 上市状态编码 | int | 如下[上市状态编码](#list_status) |
    | public_status | 上市状态 | varchar(32) |  |
    | change_reason | 变更原因 | varchar(500) |  |
    | change_type_id | 变更类型编码 | int | 如下[变更类型编码](#change_reason) |
    | change_type | 变更类型 | varchar(60) |  |
    | comments | 备注 | varchar(255) |  |
    
    上市状态编码
    
    | **上市状态编码** | **上市状态** |
    | --- | --- |
    | 301001 | 正常上市 |
    | 301002 | ST |
    | 301003 | *ST |
    | 301004 | 暂停上市 |
    | 301005 | 进入退市整理期 |
    | 301006 | 终止上市 |
    | 301007 | 已发行未上市 |
    | 301008 | 预披露 |
    | 301009 | 未过会 |
    | 301010 | 发行失败 |
    | 301011 | 暂缓发行 |
    | 301012 | 暂缓上市 |
    | 301013 | 停止转让 |
    | 301014 | 正常转让 |
    | 301015 | 实行投资者适当性管理表示 |
    | 301099 | 其他 |
    
    变更类型编码
    
    | **变更类型编码** | **变更类型** |
    | --- | --- |
    | 303001 | 恢复上市 |
    | 303002 | 摘星 |
    | 303003 | 摘帽 |
    | 303004 | 摘星摘帽 |
    | 303005 | 披星 |
    | 303006 | 戴帽 |
    | 303007 | 戴帽披星 |
    | 303008 | 拟上市 |
    | 303009 | 新股上市 |
    | 303010 | 发行失败 |
    | 303011 | 暂停上市 |
    | 303012 | 终止上市 |
    | 303013 | 退市整理 |
    | 303014 | 暂缓发行 |
    | 303015 | 暂缓上市 |
    | 303016 | 实行投资者适当性管理标识 |
    | 303017 | 未过会 |
    | 303018 | 预披露 |
    | 303019 | 正常转让 |
    | 303020 | 停止转让 |
    | 303021 | 重新上市 |
    | 303099 | 其他 |
    
- **filter(finance.STK_STATUS_CHANGE.code==code)**：指定筛选条件，通过finance.STK_STATUS_CHANGE.code==code可以指定你想要查询的股票代码；除此之外，还可以对表中其他字段指定筛选条件，如finance.STK_STATUS_CHANGE.pub_date>='2015-01-01'，表示筛选公告日期大于等于2015年1月1日之后的数据；多个筛选条件用英文逗号分隔。
    
- **limit(n)**：限制返回的数据条数，n指定返回条数。
    

**返回结果：**

- 返回一个 dataframe， 每一行对应数据表中的一条数据， 列索引是你所查询的字段名称

**注意：**

1.  **为了防止返回数据量过大, 我们每次最多返回4000行**
2.  不能进行连表查询，即同时查询多张表的数据

**示例：**

```python
# 指定查询对象为恒瑞医药（600276.XSHG)的上市公司状态变动，限定返回条数为10
q=query(finance.STK_STATUS_CHANGE).filter(finance.STK_STATUS_CHANGE.code=='600276.XSHG').limit(10)
df=finance.run_query(q)
print(df)

     id   company_id         code     name   pub_date    public_status_id  \
0  2840    420600276  600276.XSHG  恒瑞医药  2000-10-18             301001

  public_status   change_date  change_reason  change_type_id   change_type  comments
0       正常上市    2000-10-18            NaN           303009      新股上市      NaN
```

### 股票上市信息

```python
from jqdata import finance
finance.run_query(query(finance.STK_LIST).filter(finance.STK_LIST.code==code).limit(n))
```

获取沪深A股的上市信息，包含上市日期、交易所、发行价格、初始上市数量等

**参数：**

- **query(finance.STK_LIST)**：表示从finance.STK_LIST这张表中查询沪深A股的上市信息，还可以指定所要查询的字段名，格式如下：query(库名.表名.字段名1，库名.表名.字段名2），多个字段用英文逗号进行分隔；query函数的更多用法详见：[sqlalchemy.orm.query.Query对象](http://docs.sqlalchemy.org/en/rel_1_0/orm/query.html)
    
    **finance.STK_LIST**：代表股票上市信息表，收录了沪深A股的上市信息，包含上市日期、交易所、发行价格、初始上市数量等，表结构和字段信息如下：
    

| 字段名称 | 中文名称 | 字段类型 | 备注/示例 |
| --- | --- | --- | --- |
| code | 证券代码 | varchar(12) |  |
| name | 证券简称 | varchar(40) |  |
| short_name | 拼音简称 | varchar(20) |  |
| category | 证券类别 | varchar(4) | A/B |
| exchange | 交易所 | varchar(12) | XSHG/XSHE |
| start_date | 上市日期 | date |  |
| end_date | 终止上市日期 | date |  |
| company_id | 公司ID | int |  |
| company_name | 公司名称 | varchar(100) |  |
| ipo_shares | 初始上市数量 | decimal(20,2) | 股 |
| book_price | 发行价格 | decimal(20,4) | 元 |
| par_value | 面值 | decimal(20,4) | 元 |
| state_id | 上市状态编码 | int |  |
| state | 上市状态 | varchar(32) |  |

- **filter(finance.STK_LIST.code==code)**：指定筛选条件，通过finance.STK_LIST.code==code可以指定你想要查询的股票代码；除此之外，还可以对表中其他字段指定筛选条件，如finance.STK_LIST.start_date>=’2015-01-01’，表示筛选上市日期大于等于2015年1月1日之后的数据；多个筛选条件用英文逗号分隔。
- **limit(n)**：限制返回的数据条数，n指定返回条数。

**返回结果：**

- 返回一个 dataframe， 每一行对应数据表中的一条数据， 列索引是你所查询的字段名称

**注意：**

1.  **为了防止返回数据量过大, 我们每次最多返回4000行**
2.  不能进行连表查询，即同时查询多张表的数据

**示例：**

```python
# 指定查询对象为恒瑞医药（600276.XSHG)的上市信息，限定返回条数为10
q=query(finance.STK_LIST).filter(finance.STK_LIST.code=='600276.XSHG').limit(10)
df=finance.run_query(q)
print(df)

     id         code     name    short_name  category   exchange    start_date   \
0  1364  600276.XSHG   恒瑞医药         HRYY         A       XSHG      2000-10-18

  end_date   company_id         company_name   ipo_shares    book_price   par_value \
0     NaN     420600276  江苏恒瑞医药股份有限公司  40000000.0         11.98         1.0

  state_id      state
0   301001    正常上市
```

### 股票简称变更情况

```python
from jqdata import finance
finance.run_query(query(finance.STK_NAME_HISTORY).filter(finance.STK_NAME_HISTORY.code==code).limit(n))
```

获取在A股市场和B股市场上市的股票简称的变更情况

**参数：**

- **query(finance.STK_NAME_HISTORY)**：表示从finance.STK_NAME_HISTORY这张表中查询股票简称的变更情况，还可以指定所要查询的字段名，格式如下：query(库名.表名.字段名1，库名.表名.字段名2），多个字段用英文逗号进行分隔；query函数的更多用法详见：[sqlalchemy.orm.query.Query对象](http://docs.sqlalchemy.org/en/rel_1_0/orm/query.html)
    
    **finance.STK_NAME_HISTORY**：代表股票简称变更表，收录了在A股市场和B股市场上市的股票简称的变更情况，表结构和字段信息如下：
    

| 字段名称 | 中文名称 | 字段类型 | 备注/示例 |
| --- | --- | --- | --- |
| code | 股票代码 | varchar(12) |  |
| company_id | 公司ID | int |  |
| new_name | 新股票简称 | varchar(40) |  |
| new_spelling | 新英文简称 | varchar(40) |  |
| org_name | 原证券简称 | varchar(40) |  |
| org_spelling | 原证券英文简称 | varchar(40) |  |
| start_date | 开始日期 | date |  |
| pub_date | 公告日期 | date |  |
| reason | 变更原因 | varchar(255) |  |

- **filter(finance.STK_NAME_HISTORY.code==code)**：指定筛选条件，通过finance.STK_NAME_HISTORY.code==code可以指定你想要查询的股票代码；除此之外，还可以对表中其他字段指定筛选条件，如finance.STK_NAME_HISTORY.pub_date>=’2015-01-01’，表示筛选公告日期大于等于2015年1月1日之后的数据；多个筛选条件用英文逗号分隔。
- **limit(n)**：限制返回的数据条数，n指定返回条数。

**返回结果：**

- 返回一个 dataframe， 每一行对应数据表中的一条数据， 列索引是你所查询的字段名称

**注意：**

1.  **为了防止返回数据量过大, 我们每次最多返回4000行**
2.  不能进行连表查询，即同时查询多张表的数据

**示例：**

```python
# 指定查询对象为恒瑞医药（600276.XSHG)的股票简称变更信息，限定返回条数为10
q=query(finance.STK_NAME_HISTORY).filter(finance.STK_NAME_HISTORY.code=='600276.XSHG').limit(10)
df=finance.run_query(q)
print(df)

     id         code company_id     new_name   new_spelling org_name org_spelling  \
0  1459  600276.XSHG  420600276     恒瑞医药         HRYY      NaN          NaN
1  3588  600276.XSHG  420600276      Ｇ恒瑞          ＧHR      NaN          NaN
2  4007  600276.XSHG  420600276     恒瑞医药         HRYY      NaN          NaN

   start_date    pub_date  reason
0  2000-10-18  2000-10-18    NaN
1  2006-06-20  2006-06-15    NaN
2  2006-10-09  2006-09-28    NaN
```

### 上市公司员工情况

```
from jqdata import finance
finance.run_query(query(finance.STK_EMPLOYEE_INFO).filter(finance.STK_EMPLOYEE_INFO.code==code).limit(n))
```

获取上市公司在公告中公布的员工情况，包括员工人数、学历等信息;
更新时间：上市公司定期报告员工情况的维护时效为定期报告披露后一个月内

**参数：**

- **query(finance.STK_EMPLOYEE_INFO)**：表示从finance.STK_EMPLOYEE_INFO这张表中查询上市公司员工情况的字段信息，还可以指定所要查询的字段名，格式如下：query(库名.表名.字段名1，库名.表名.字段名2），多个字段用逗号分隔进行提取；query函数的更多用法详见：[sqlalchemy.orm.query.Query对象](http://docs.sqlalchemy.org/en/rel_1_0/orm/query.html)
    
    **finance.STK_EMPLOYEE_INFO**：代表上市公司员工情况表，收录了上市公司在公告中公布的员工情况，表结构和字段信息如下：
    

| 字段名称 | 中文名称 | 字段类型 | 备注/示例 |
| --- | --- | --- | --- |
| company_id | 公司ID | int |  |
| code | 证券代码 | varchar(12) | ‘600276.XSHG’，’000001.XSHE’ |
| name | 证券名称 | varchar(64) |  |
| end_date | 报告期截止日 | date | 统计截止该报告期的员工信息 |
| pub_date | 公告日期 | date |  |
| employee | 在职员工总数 | int | 人 |
| retirement | 离退休人员 | int | 人 |
| graduate_rate | 研究生以上人员比例 | decimal(10,4) | % |
| college_rate | 大学专科以上人员比例 | decimal(10,4) | % |
| middle_rate | 中专及以下人员比例 | decimal(10,4) | % |

- **filter(finance.STK_EMPLOYEE_INFO.code==code)**：指定筛选条件，通过finance.STK_EMPLOYEE_INFO.code==code可以指定你想要查询的股票代码；除此之外，还可以对表中其他字段指定筛选条件，如finance.STK_EMPLOYEE_INFO.pub_date>=’2015-01-01’，表示公告日期大于2015年1月1日上市公司公布的员工信息；多个筛选条件用英文逗号分隔。
- **limit(n)**：限制返回的数据条数，n指定返回条数。

**返回结果：**

- 返回一个 dataframe， 每一行对应数据表中的一条数据， 列索引是你所查询的字段名称

**注意：**

1.  **为了防止返回数据量过大, 我们每次最多返回3000行**
2.  不能进行连表查询，即同时查询多张表的数据

**示例：**

```python
# 指定查询对象为恒瑞医药（600276.XSHG)的员工信息且公告日期大于2015年1月1日，限定返回条数为10
q=query(finance.STK_EMPLOYEE_INFO).filter(finance.STK_EMPLOYEE_INFO.code=='600276.XSHG',finance.STK_EMPLOYEE_INFO.pub_date>='2015-01-01').limit(10)
df=finance.run_query(q)
print(df)

        id company_id         code  name    end_date    pub_date      employee  \
  0  21542  420600276  600276.XSHG  恒瑞医药  2014-12-31  2015-03-31     8770
  1  21543  420600276  600276.XSHG  恒瑞医药  2015-12-31  2016-04-13    10191
  2  21544  420600276  600276.XSHG  恒瑞医药  2016-12-31  2017-03-11    12653

    retirement graduate_rate college_rate middle_rate
  0        NaN           NaN          NaN         NaN
  1        NaN           NaN          NaN         NaN
  2        NaN           NaN          NaN         NaN
```

## 上市公司股东和股本信息

### 十大股东

```python
from jqdata import finance
finance.run_query(query(finance.STK_SHAREHOLDER_TOP10).filter(finance.STK_SHAREHOLDER_TOP10.code==code).limit(n))
```

获取上市公司前十大股东的持股情况，包括持股数量，所持股份性质，变动原因等。

**参数：**

- **query(finance.STK_SHAREHOLDER_TOP10)**：表示从finance.STK_SHAREHOLDER_TOP10这张表中查询上市公司前十大股东的持股情况，还可以指定所要查询的字段名，格式如下：query(库名.表名.字段名1，库名.表名.字段名2），多个字段用英文逗号进行分隔；query函数的更多用法详见：[sqlalchemy.orm.query.Query对象](http://docs.sqlalchemy.org/en/rel_1_0/orm/query.html)
    
    **finance.STK_SHAREHOLDER_TOP10**：代表上市公司十大股东表，收录了上市公司前十大股东的持股情况，包括持股数量，所持股份性质，变动原因等。表结构和字段信息如下：
    
    | 字段名称 | 中文名称 | 字段类型 | 备注/示例 |
    | --- | --- | --- | --- |
    | company_id | 公司ID | int |  |
    | company_name | 公司名称 | varchar(100) | 在此是指上市公司的名称 |
    | code | 股票代码 | varchar(12) |  |
    | end_date | 截止日期 | date | 公告中统计的十大股东截止到某一日期的更新情况。 |
    | pub_date | 公告日期 | date | 公告中会提到十大股东的更新情况。 |
    | change_reason_id | 变动原因编码 | int |  |
    | change_reason | 变动原因 | varchar(120) |  |
    | shareholder_rank | 股东名次 | int |  |
    | shareholder_name | 股东名称 | varchar(200) |  |
    | shareholder_name_en | 股东名称（英文） | varchar(200) |  |
    | shareholder_id | 股东ID | int |  |
    | shareholder_class_id | 股东类别编码 | int |  |
    | shareholder_class | 股东类别 | varchar(150) | 包括:券商、社保基金、证券投资基金、保险公司、QFII、其它机构、个人等 |
    | share_number | 持股数量 | decimal(10,4) | 股 |
    | share_ratio | 持股比例 | decimal(10,4) | % |
    | sharesnature_id | 股份性质编码 | int |  |
    | sharesnature | 股份性质 | varchar(120) | 包括:国家股、法人股、个人股外资股、流通A股、流通B股、职工股、发起人股、转配股等 |
    | share_pledge_freeze | 股份质押冻结数量 | decimal(10,4) | 如果股份质押数量和股份冻结数量任意一个字段有值，则等于后两者之和 |
    | share_pledge | 股份质押数量 | decimal(10,4) | 股 |
    | share_freeze | 股份冻结数量 | decimal(10,4) | 股 |
    
- **filter(finance.STK_SHAREHOLDER_TOP10.code==code)**：指定筛选条件，通过finance.STK_SHAREHOLDER_TOP10.code==code可以指定你想要查询的股票代码；除此之外，还可以对表中其他字段指定筛选条件，如finance.STK_SHAREHOLDER_TOP10.pub_date>='2015-01-01'，表示筛选公告日期大于等于2015年1月1日之后的数据；多个筛选条件用英文逗号分隔。
    
- **limit(n)**：限制返回的数据条数，n指定返回条数。
    

**返回结果：**

- 返回一个 dataframe， 每一行对应数据表中的一条数据， 列索引是你所查询的字段名称

**注意：**

1.  **为了防止返回数据量过大, 我们每次最多返回4000行**
2.  不能进行连表查询，即同时查询多张表的数据

**示例：**

```python
#指定查询对象为恒瑞医药（600276.XSHG)的十大股东情况，限定返回条数为10条
q=query(finance.STK_SHAREHOLDER_TOP10).filter(finance.STK_SHAREHOLDER_TOP10.code=='600276.XSHG',finance.STK_SHAREHOLDER_TOP10.pub_date>'2015-01-01').limit(10)
df=finance.run_query(q)
print(df)

       id  company_name           company_id         code    end_date    pub_date  \
0  753808  江苏恒瑞医药股份有限公司  420600276  600276.XSHG  2014-12-31  2015-03-31
1  753809  江苏恒瑞医药股份有限公司  420600276  600276.XSHG  2014-12-31  2015-03-31
2  753810  江苏恒瑞医药股份有限公司  420600276  600276.XSHG  2014-12-31  2015-03-31
3  753811  江苏恒瑞医药股份有限公司  420600276  600276.XSHG  2014-12-31  2015-03-31
4  753812  江苏恒瑞医药股份有限公司  420600276  600276.XSHG  2014-12-31  2015-03-31
5  753813  江苏恒瑞医药股份有限公司  420600276  600276.XSHG  2014-12-31  2015-03-31
6  753814  江苏恒瑞医药股份有限公司  420600276  600276.XSHG  2014-12-31  2015-03-31
7  753815  江苏恒瑞医药股份有限公司  420600276  600276.XSHG  2014-12-31  2015-03-31
8  753816  江苏恒瑞医药股份有限公司  420600276  600276.XSHG  2014-12-31  2015-03-31
9  753817  江苏恒瑞医药股份有限公司  420600276  600276.XSHG  2014-12-31  2015-03-31

  change_reason_id change_reason     shareholder_rank  \
0           306019          定期报告                4
1           306019          定期报告                9
2           306019          定期报告               10
3           306019          定期报告                2
4           306019          定期报告                3
5           306019          定期报告                5
6           306019          定期报告                6
7           306019          定期报告                7
8           306019          定期报告                8
9           306019          定期报告                1

                    shareholder_name     ...                   shareholder_id  \
0                         中国医药工业有限公司     ...                  100014895
1               交通银行-博时新兴成长股票型证券投资基金     ...           120050009
2   新华人寿保险股份有限公司-分红-团体分红-018L-FH001沪     ...           100000383
3                         西藏达远投资有限公司     ...                   100097529
4                      连云港恒创医药科技有限公司     ...                100008678
5                         江苏金海投资有限公司     ...                   100008257
6                         香港中央结算有限公司     ...                   100011907
7  中国农业银行股份有限公司-国泰国证医药卫生行业指数分级证券投资基金     ...   120160219
8         兴业银行股份有限公司-兴全趋势投资混合型证券投资基金     ...        120163402
9                       江苏恒瑞医药集团有限公司     ...                   100008682

  shareholder_class_id shareholder_class share_number share_ratio  \
0               307099              其他机构   73000000.0        4.85
1               307003            证券投资基金   10107880.0        0.67
2               307014            保险投资组合    9820232.0        0.65
3               307099              其他机构  240536692.0       15.99
4               307099              其他机构  112278458.0        7.47
5               307099              其他机构   53474244.0        3.56
6               307099              其他机构   30821240.0        2.05
7               307003            证券投资基金   12489920.0        0.83
8               307003            证券投资基金   11999901.0         0.8
9               307099              其他机构  365776169.0       24.32

  sharesnature_id    sharesnature    share_pledge_freeze   share_pledge  share_freeze
0          308007         流通A股                 NaN          NaN          NaN
1          308007         流通A股                 NaN          NaN          NaN
2          308007         流通A股                 NaN          NaN          NaN
3          308007         流通A股                 NaN          NaN          NaN
4          308007         流通A股                 NaN          NaN          NaN
5          308007         流通A股          53474244.0   53474244.0          NaN
6          308007         流通A股                 NaN          NaN          NaN
7          308007         流通A股                 NaN          NaN          NaN
8          308007         流通A股                 NaN          NaN          NaN
9          308007         流通A股                 NaN          NaN          NaN
```

### 十大流通股东

```python
from jqdata import finance
finance.run_query(query(finance.STK_SHAREHOLDER_FLOATING_TOP10).filter(finance.STK_SHAREHOLDER_FLOATING_TOP10.code==code).limit(n))
```

获取上市公司前十大流通股东的持股情况，包括持股数量，所持股份性质，变动原因等。

**参数：**

- **query(finance.STK_SHAREHOLDER_FLOATING_TOP10)**：表示从finance.STK_SHAREHOLDER_FLOATING_TOP10这张表中查询上市公司前十大流通股东的持股情况，还可以指定所要查询的字段名，格式如下：query(库名.表名.字段名1，库名.表名.字段名2），多个字段用英文逗号进行分隔；query函数的更多用法详见：[sqlalchemy.orm.query.Query对象](http://docs.sqlalchemy.org/en/rel_1_0/orm/query.html)
    
    **finance.STK_SHAREHOLDER_FLOATING_TOP10**：代表上市公司十大流通股东表，收录了上市公司前十大流通股东的持股情况，包括持股数量，所持股份性质，变动原因等。表结构和字段信息如下：
    
    | 字段名称 | 中文名称 | 字段类型 | 备注/示例 |
    | --- | --- | --- | --- |
    | company_id | 公司ID | int |  |
    | company_name | 公司名称 | varchar(100) |  |
    | code | 股票代码 | varchar(12) |  |
    | end_date | 截止日期 | date |  |
    | pub_date | 公告日期 | date |  |
    | change_reason_id | 变动原因编码 | int |  |
    | change_reason | 变动原因 | varchar(120) |  |
    | shareholder_rank | 股东名次 | int |  |
    | shareholder_id | 股东ID | int |  |
    | shareholder_name | 股东名称 | varchar(200) |  |
    | shareholder_name_en | 股东名称（英文） | varchar(150) |  |
    | shareholder_class_id | 股东类别编码 | int |  |
    | shareholder_class | 股东类别 | varchar(150) |  |
    | share_number | 持股数量 | int | 股 |
    | share_ratio | 持股比例 | decimal(10,4) | % |
    | sharesnature_id | 股份性质编码 | int |  |
    | sharesnature | 股份性质 | varchar(120) |  |
    
- **filter(finance.STK_SHAREHOLDER_FLOATING_TOP10.code==code)**：指定筛选条件，通过finance.STK_SHAREHOLDER_FLOATING_TOP10.code==code可以指定你想要查询的股票代码；除此之外，还可以对表中其他字段指定筛选条件，如finance.STK_SHAREHOLDER_FLOATING_TOP10.pub_date>='2015-01-01'，表示筛选公告日期大于等于2015年1月1日之后的数据；多个筛选条件用英文逗号分隔。
    
- **limit(n)**：限制返回的数据条数，n指定返回条数。
    

**返回结果：**

- 返回一个 dataframe， 每一行对应数据表中的一条数据， 列索引是你所查询的字段名称

**注意：**

1.  **为了防止返回数据量过大, 我们每次最多返回4000行**
2.  不能进行连表查询，即同时查询多张表的数据

**示例：**

```python
#指定查询对象为恒瑞医药（600276.XSHG)的十大流通股东情况，返回条数为10条
q=query(finance.STK_SHAREHOLDER_FLOATING_TOP10).filter(finance.STK_SHAREHOLDER_FLOATING_TOP10.code=='600276.XSHG',finance.STK_SHAREHOLDER_FLOATING_TOP10.pub_date>'2015-01-01').limit(10)
df=finance.run_query(q)
print(df)

       id company_id  company_name         code    end_date    pub_date  \
0  585806  420600276  江苏恒瑞医药股份有限公司  600276.XSHG  2014-12-31  2015-03-31
1  585807  420600276  江苏恒瑞医药股份有限公司  600276.XSHG  2014-12-31  2015-03-31
2  585808  420600276  江苏恒瑞医药股份有限公司  600276.XSHG  2014-12-31  2015-03-31
3  585809  420600276  江苏恒瑞医药股份有限公司  600276.XSHG  2014-12-31  2015-03-31
4  585810  420600276  江苏恒瑞医药股份有限公司  600276.XSHG  2014-12-31  2015-03-31
5  585811  420600276  江苏恒瑞医药股份有限公司  600276.XSHG  2014-12-31  2015-03-31
6  585812  420600276  江苏恒瑞医药股份有限公司  600276.XSHG  2014-12-31  2015-03-31
7  585813  420600276  江苏恒瑞医药股份有限公司  600276.XSHG  2014-12-31  2015-03-31
8  585814  420600276  江苏恒瑞医药股份有限公司  600276.XSHG  2014-12-31  2015-03-31
9  585815  420600276  江苏恒瑞医药股份有限公司  600276.XSHG  2014-12-31  2015-03-31

  change_reason_id change_reason shareholder_rank shareholder_id  \
0            15019          定期报告                1              0
1            15019          定期报告                2              0
2            15019          定期报告                3              0
3            15019          定期报告                4              0
4            15019          定期报告                5              0
5            15019          定期报告                6              0
6            15019          定期报告                7       77160219
7            15019          定期报告                8       77163402
8            15019          定期报告                9       77050009
9            15019          定期报告               10              0

                    shareholder_name              shareholder_name_en     shareholder_class_id  \
0                       江苏恒瑞医药集团有限公司                 NaN                 3999
1                         西藏达远投资有限公司                 NaN                 3999
2                      连云港恒创医药科技有限公司                 NaN                 3999
3                         中国医药工业有限公司                 NaN                 3999
4                         江苏金海投资有限公司                 NaN                 3999
5                         香港中央结算有限公司                 NaN                 3999
6  中国农业银行股份有限公司-国泰国证医药卫生行业指数分级证券投资基金  NaN                 3003
7         兴业银行股份有限公司-兴全趋势投资混合型证券投资基金        NaN                 3003
8               交通银行-博时新兴成长股票型证券投资基金                 NaN                 3003
9   新华人寿保险股份有限公司-分红-团体分红-018L-FH001沪                 NaN                 3017

  shareholder_class share_number share_ratio sharesnature_id sharesnature
0              其他机构  332523790.0      22.109           25007         流通A股
1              其他机构  229034683.0      15.228           25007         流通A股
2              其他机构  102094053.0       6.788           25007         流通A股
3              其他机构   70203316.0       4.668           25007         流通A股
4              其他机构   50367370.0       3.349           25007         流通A股
5              其他机构   17207872.0       1.144           25007         流通A股
6            证券投资基金   15161505.0       1.008           25007         流通A股
7            证券投资基金   10299800.0       0.685           25007         流通A股
8            证券投资基金    9929500.0        0.66           25007         流通A股
9            保险投资组合    9296487.0       0.618           25007         流通A股
```

### 股东股份质押

```python
from jqdata import finance
finance.run_query(query(finance.STK_SHARES_PLEDGE).filter(finance.STK_SHARES_PLEDGE.code==code).limit(n))
```

获取上市公司股东股份的质押情况。

**参数：**

- **query(finance.STK_SHARES_PLEDGE)**：表示从finance.STK_SHARES_PLEDGE这张表中查询上市公司股东股份的质押情况，还可以指定所要查询的字段名，格式如下：query(库名.表名.字段名1，库名.表名.字段名2），多个字段用英文逗号进行分隔；query函数的更多用法详见：[sqlalchemy.orm.query.Query对象](http://docs.sqlalchemy.org/en/rel_1_0/orm/query.html)
    
    **finance.STK_SHARES_PLEDGE**：代表上市公司股东股份质押表，收录了上市公司股东股份的质押情况。表结构和字段信息如下：
    
    | 字段名称 | 中文名称 | 字段类型 | 备注/示例 |
    | --- | --- | --- | --- |
    | company_id | 公司ID | int |  |
    | company_name | 公司名称 | varchar(100) |  |
    | code | 股票代码 | varchar(12) |  |
    | pub_date | 公告日期 | date |  |
    | pledgor_id | 出质人ID | int |  |
    | pledgor | 出质人 | varchar(100) | 将资产质押出去的人成为出质人 |
    | pledgee | 质权人 | varchar(100) |  |
    | pledge_item | 质押事项 | varchar(500) | 质押原因，记录借款人、借款金额、币种等内容 |
    | pledge_nature_id | 质押股份性质编码 | int |  |
    | pledge_nature | 质押股份性质 | varchar(120) |  |
    | pledge_number | 质押数量 | int | 股 |
    | pledge_total_ratio | 占总股本比例 | decimal(10,4) | % |
    | start_date | 质押起始日 | date |  |
    | end_date | 质押终止日 | date |  |
    | unpledged_date | 质押解除日 | date |  |
    | unpledged_number | 质押解除数量 | int | 股 |
    | unpledged _detail | 解除质押说明 | varchar(1000) |  |
    | is_buy_back | 是否质押式回购交易 | char(1) |  |
    
- **filter(finance.STK_SHARES_PLEDGE.code==code)**：指定筛选条件，通过finance.STK_SHARES_PLEDGE.code==code可以指定你想要查询的股票代码；除此之外，还可以对表中其他字段指定筛选条件，如finance.STK_SHARES_PLEDGE.pub_date>='2015-01-01'，表示筛选公告日期大于等于2015年1月1日之后的数据；多个筛选条件用英文逗号分隔。
    
- **limit(n)**：限制返回的数据条数，n指定返回条数。
    

**返回结果：**

- 返回一个 dataframe， 每一行对应数据表中的一条数据， 列索引是你所查询的字段名称

**注意：**

1.  **为了防止返回数据量过大, 我们每次最多返回4000行**
2.  不能进行连表查询，即同时查询多张表的数据

**示例：**

```python
#指定查询对象为万科（000002.XSHE)的股东股份质押情况，返回条数为10条
q=query(finance.STK_SHARES_PLEDGE).filter(finance.STK_SHARES_PLEDGE.code=='000002.XSHE',finance.STK_SHARES_PLEDGE.pub_date>'2015-01-01').limit(10)
df=finance.run_query(q)
print(df)

      id company_id      company_name         code      pub_date     pledgor_id  \
0  30928  430000002   万科企业股份有限公司  000002.XSHE  2015-11-11        NaN
1  41070  430000002   万科企业股份有限公司  000002.XSHE  2016-07-14        NaN
2  52962  430000002   万科企业股份有限公司  000002.XSHE  2017-03-08        NaN
3  52963  430000002   万科企业股份有限公司  000002.XSHE  2017-03-08        NaN
4  53281  430000002   万科企业股份有限公司  000002.XSHE  2017-03-14        NaN
5  53430  430000002   万科企业股份有限公司  000002.XSHE  2017-03-17        NaN
6  53454  430000002   万科企业股份有限公司  000002.XSHE  2017-03-17        NaN
7  53455  430000002   万科企业股份有限公司  000002.XSHE  2017-03-17        NaN
8  53456  430000002   万科企业股份有限公司  000002.XSHE  2017-03-17        NaN
9  53504  430000002   万科企业股份有限公司  000002.XSHE  2017-03-17        NaN

         pledgor                   pledgee  \
0  深圳市钜盛华股份有限公司  鹏华资产管理（深圳）有限公司
1  深圳市钜盛华股份有限公司    中国银河证券股份有限公司
2  深圳市钜盛华股份有限公司  鹏华资产管理（深圳）有限公司
3  深圳市钜盛华股份有限公司  鹏华资产管理（深圳）有限公司
4  深圳市钜盛华股份有限公司      平安证券股份有限公司
5   广州市凯进投资有限公司      中信证券股份有限公司
6   广州市悦朗投资有限公司      中信证券股份有限公司
7   广州市广域实业有限公司      中信证券股份有限公司
8   广州市启通实业有限公司      中信证券股份有限公司
9   广州市昱博投资有限公司      中信证券股份有限公司

                                         pledge_item pledge_nature_id  \
0  本公司股东深圳市钜盛华股份有限公司将持有的公司728,000,000股无限售流通A股质押给鹏...              NaN
1  本公司股东深圳市钜盛华股份有限公司将持有的本公司37357300股股权质押给中国银河证券股份...         308007.0
2  本公司股东深圳市钜盛华股份有限公司将2015年10月28日质押给鹏华资产管理（深圳）有限公司...         308007.0
3  本公司股东深圳市钜盛华股份有限公司将2015年10月21日质押给鹏华资产管理（深圳）有限公司...         308007.0
4  本公司第一大股东深圳市钜盛华股份有限公司将持有的本公司182000000股流通A股股权质押给...         308007.0
5  本公司股东广州市凯进投资有限公司将持有的本公司50759970股股权质押给中信证券股份有限公...              NaN
6  本公司股东广州市悦朗投资有限公司将持有的本公司205731814股股权质押给中信证券股份有限...              NaN
7  本公司股东广州市广域实业有限公司将持有的本公司86701961股股权质押给中信证券股份有限公...              NaN
8  本公司股东广州市启通实业有限公司将持有的本公司68205047股股权质押给中信证券股份有限公...              NaN
9  本公司股东广州市昱博投资有限公司将持有的本公司210778555股股权质押给中信证券股份有限...              NaN

      pledge_nature pledge_number   pledge_total_ratio  start_date    end_date  \
0           NaN   728000000.0                7.0        2015-10-15         NaN
1          流通A股    37357300.0                NaN     2016-07-12         NaN
2          流通A股           NaN                NaN     2015-10-28  2017-03-03
3          流通A股           NaN                NaN     2015-10-21  2017-03-03
4          流通A股   182000000.0                NaN     2017-03-09         NaN
5           NaN    50759970.0                   NaN  2017-03-16  2018-03-16
6           NaN   205731814.0                   NaN  2017-03-16  2018-03-16
7           NaN    86701961.0                   NaN  2017-03-16  2018-03-16
8           NaN    68205047.0                   NaN  2017-03-16  2018-03-16
9           NaN   210778555.0                   NaN  2017-03-16  2018-03-16

  unpledged_date unpledged_number unpledged_detail is_buy_back
0            NaN              NaN              NaN         NaN
1            NaN              NaN              NaN           1
2     2017-03-03       91000000.0              NaN         NaN
3     2017-03-03       91000000.0              NaN         NaN
4            NaN              NaN              NaN           1
5            NaN              NaN              NaN           1
6            NaN              NaN              NaN           1
7            NaN              NaN              NaN           1
8            NaN              NaN              NaN           1
9            NaN              NaN              NaN           1
```

### 股东股份冻结

```python
from jqdata import finance
finance.run_query(query(finance.STK_SHARES_FROZEN).filter(finance.STK_SHARES_FROZEN.code==code).limit(n))
```

获取上市公司股东股份的冻结情况

**参数：**

- **query(finance.STK_SHARES_FROZEN)**：表示从finance.STK_SHARES_FROZEN这张表中查询股东股份的冻结情况，还可以指定所要查询的字段名，格式如下：query(库名.表名.字段名1，库名.表名.字段名2），多个字段用英文逗号进行分隔；query函数的更多用法详见：[sqlalchemy.orm.query.Query对象](http://docs.sqlalchemy.org/en/rel_1_0/orm/query.html)
    
    **finance.STK_SHARES_FROZEN**：代表上市公司股东股份冻结表，收录了上市公司股东股份的冻结情况，表结构和字段信息如下：
    
    | 字段名称 | 中文名称 | 字段类型 | 含义 |
    | --- | --- | --- | --- |
    | company_id | 公司ID | int |  |
    | company_name | 公司名称 | varchar(100) |  |
    | pub_date | 公告日期 | date |  |
    | code | 股票代码 | varchar(12) |  |
    | frozen_person_id | 被冻结当事人ID | int |  |
    | frozen_person | 被冻结当事人 | varchar(100) |  |
    | frozen_reason | 冻结事项 | varchar(600) |  |
    | frozen_share_nature_id | 被冻结股份性质编码 | int |  |
    | frozen_share_nature | 被冻结股份性质 | varchar(120) | 包括:国家股、法人股、个人股、外资股、流通A股、流通B股、职工股、发起人股、转配股 |
    | frozen_number | 冻结数量 | int | 股 |
    | frozen_total_ratio | 占总股份比例 | decimal(10,4) | % |
    | freeze_applicant | 冻结申请人 | varchar(100) |  |
    | freeze_executor | 冻结执行人 | varchar(100) |  |
    | start_date | 冻结起始日 | date |  |
    | end_date | 冻结终止日 | date |  |
    | unfrozen_date | 解冻日期 | date | 分批解冻的为最近一次解冻日期 |
    | unfrozen_number | 累计解冻数量 | int | 原解冻数量(股) |
    | unfrozen_detail | 解冻处理说明 | varchar(1000) | 冻结过程及结束后的处理结果 |
    
- **filter(finance.STK_SHARES_FROZEN.code==code)**：指定筛选条件，通过finance.STK_SHARES_FROZEN.code==code可以指定你想要查询的股票代码；除此之外，还可以对表中其他字段指定筛选条件，如finance.STK_SHARES_FROZEN.pub_date>='2015-01-01'，表示筛选公告日期大于等于2015年1月1日之后的数据；多个筛选条件用英文逗号分隔。
    
- **limit(n)**：限制返回的数据条数，n指定返回条数。
    

**返回结果：**

- 返回一个 dataframe， 每一行对应数据表中的一条数据， 列索引是你所查询的字段名称

**注意：**

1.  **为了防止返回数据量过大, 我们每次最多返回4000行**
2.  不能进行连表查询，即同时查询多张表的数据

**示例：**

```python
#指定查询对象为文一科技（600520.XSHG)的股东股份冻结情况，返回条数为10条
q=query(finance.STK_SHARES_FROZEN).filter(finance.STK_SHARES_FROZEN.code=='600520.XSHG',finance.STK_SHARES_FROZEN.pub_date>'2015-01-01').limit(10)
df=finance.run_query(q)
print(df)

     id company_id    company_name    pub_date         code frozen_person_id  \
0  4213  420600520  铜陵中发三佳科技股份有限公司  2015-07-11  600520.XSHG              NaN
1  4227  420600520  铜陵中发三佳科技股份有限公司  2015-08-13  600520.XSHG              NaN
2  4261  420600520  铜陵中发三佳科技股份有限公司  2015-09-22  600520.XSHG              NaN
3  4446  420600520  铜陵中发三佳科技股份有限公司  2016-03-24  600520.XSHG              NaN
4  4499  420600520  铜陵中发三佳科技股份有限公司  2016-04-30  600520.XSHG              NaN
5  4509  420600520  铜陵中发三佳科技股份有限公司  2016-05-07  600520.XSHG              NaN
6  4513  420600520  铜陵中发三佳科技股份有限公司  2016-05-21  600520.XSHG              NaN
7  4541  420600520  铜陵中发三佳科技股份有限公司  2016-06-25  600520.XSHG              NaN
8  4542  420600520  铜陵中发三佳科技股份有限公司  2016-06-25  600520.XSHG              NaN
9  4569  420600520  铜陵中发三佳科技股份有限公司  2016-07-09  600520.XSHG              NaN

       frozen_person frozen_reason frozen_share_nature_id frozen_share_nature  \
0  铜陵市三佳电子（集团）有限责任公司           NaN               308001.0               境内法人股
1  铜陵市三佳电子（集团）有限责任公司           NaN               308001.0               境内法人股
2  铜陵市三佳电子（集团）有限责任公司           NaN               308001.0               境内法人股
3  铜陵市三佳电子（集团）有限责任公司           NaN               308001.0               境内法人股
4  铜陵市三佳电子（集团）有限责任公司           NaN               308001.0               境内法人股
5  铜陵市三佳电子（集团）有限责任公司           NaN               308001.0               境内法人股
6  铜陵市三佳电子（集团）有限责任公司           NaN                    NaN                 NaN
7  铜陵市三佳电子（集团）有限责任公司           NaN                    NaN                 NaN
8  铜陵市三佳电子（集团）有限责任公司           NaN                    NaN                 NaN
9  铜陵市三佳电子（集团）有限责任公司           NaN                    NaN                 NaN

        ...       frozen_total_ratio freeze_applicant        freeze_executor  \
0       ...                    17.09              NaN             上海市金山区人民法院
1       ...                    17.09              NaN                    NaN
2       ...                    17.09   中信银行股份有限公司安庆分行                    NaN
3       ...                   17.089              NaN  安庆市宜秀区人民法院及安庆市迎江区人民法院
4       ...                   17.089              NaN            上海市浦东新区人民法院
5       ...                   17.089              NaN            上海市浦东新区人民法院
6       ...                   17.089              NaN          广东省深圳市宝安区人民法院
7       ...                      NaN     上海富汇融资租赁有限公司            上海市浦东新区人民法院
8       ...                   17.089              NaN              铜陵市中级人民法院
9       ...                      NaN              NaN          广东省深圳市宝安区人民法院

  change_reason_id change_reason  start_date    end_date unfrozen_date  \
0              NaN           NaN  2015-07-10         NaN           NaN
1              NaN           NaN         NaN  2015-08-11    2015-08-11
2              NaN           NaN         NaN         NaN           NaN
3              NaN           NaN         NaN  2016-03-16    2016-03-16
4              NaN           NaN  2016-04-27  2019-04-20           NaN
5              NaN           NaN  2016-05-04  2019-05-04           NaN
6              NaN           NaN         NaN         NaN           NaN
7              NaN           NaN         NaN  2016-06-23    2016-06-23
8              NaN           NaN         NaN  2016-06-23    2016-06-23
9              NaN           NaN         NaN  2016-07-07    2016-07-07

  unfrozen_number unfrozen_detail
0             NaN             NaN
1      27073333.0             NaN
2             NaN             NaN
3      27073333.0             NaN
4             NaN             NaN
5             NaN             NaN
6             NaN             NaN
7      27073333.0             NaN
8      27073333.0             NaN
9      27073333.0             NaN

[10 rows x 21 columns]
```

### 股东户数

```python
from jqdata import finance
finance.run_query(query(finance.STK_HOLDER_NUM).filter(finance.STK_HOLDER_NUM.code==code).limit(n))
```

获取上市公司全部股东户数，A股股东、B股股东、H股股东的持股户数

**参数：**

- **query(finance.STK_HOLDER_NUM)**：表示从finance.STK_HOLDER_NUM这张表中查询上市公司的股东户数，还可以指定所要查询的字段名，格式如下：query(库名.表名.字段名1，库名.表名.字段名2），多个字段用英文逗号进行分隔；query函数的更多用法详见：[sqlalchemy.orm.query.Query对象](http://docs.sqlalchemy.org/en/rel_1_0/orm/query.html)
    
    **finance.STK_HOLDER_NUM**：代表上市公司股东户数表，收录了上市公司全部股东户数，A股股东、B股股东、H股股东的持股户数情况，表结构和字段信息如下：
    
    | 字段名称 | 中文名称 | 字段类型 | 备注/示例 |
    | --- | --- | --- | --- |
    | code | 股票代码 | varchar(12) |  |
    | pub_date | 公告日期 | date |  |
    | end_date | 截止日期 | date |  |
    | share_holders | 股东总户数 | int |  |
    | a_share_holders | A股股东总户数 | int |  |
    | b_share_holders | B股股东总户数 | int |  |
    | h_share_holders | H股股东总户数 | int |  |
    
- **filter(finance.STK_HOLDER_NUM.code==code)**：指定筛选条件，通过finance.STK_HOLDER_NUM.code==code可以指定你想要查询的股票代码；除此之外，还可以对表中其他字段指定筛选条件，如finance.STK_HOLDER_NUM.pub_date>='2015-01-01'，表示筛选公布日期大于等于2015年1月1日之后的数据；多个筛选条件用英文逗号分隔。
    
- **limit(n)**：限制返回的数据条数，n指定返回条数。
    

**返回结果：**

- 返回一个 dataframe， 每一行对应数据表中的一条数据， 列索引是你所查询的字段名称

**注意：**

1.  **为了防止返回数据量过大, 我们每次最多返回4000行**
2.  不能进行连表查询，即同时查询多张表的数据

**示例：**

```python
#指定查询对象为万科（000002.XSHE)的股东户数情况，返回条数为10条
q=query(finance.STK_HOLDER_NUM).filter(finance.STK_HOLDER_NUM.code=='000002.XSHE',finance.STK_HOLDER_NUM.pub_date>'2015-01-01').limit(10)
df=finance.run_query(q)
print(df)

    id         code    end_date    pub_date share_holders a_share_holders  \
0  139  000002.XSHE  2014-12-31  2015-03-31        496922          496907
1  140  000002.XSHE  2015-03-24  2015-03-31        586390          586373
2  141  000002.XSHE  2015-03-31  2015-04-27        652130          652113
3  142  000002.XSHE  2015-06-30  2015-08-17        479264          479246
4  143  000002.XSHE  2015-09-30  2015-10-28        332360          332339
5  144  000002.XSHE  2015-12-31  2016-03-14        272370          272350
6  145  000002.XSHE  2016-02-29  2016-03-14        272167          272145
7  146  000002.XSHE  2016-03-31  2016-04-28        272085          272063
8  147  000002.XSHE  2016-06-30  2016-08-25        272027          272006
9  148  000002.XSHE  2016-07-31  2016-08-25        546713          546691

  b_share_holders h_share_holders
0             NaN              15
1             NaN              17
2             NaN              17
3             NaN              18
4             NaN              21
5             NaN              20
6             NaN              22
7             NaN              22
8             NaN              21
9             NaN              22
```

### 大股东增减持

```python
from jqdata import finance
finance.run_query(query(finance.STK_SHAREHOLDERS_SHARE_CHANGE).filter(finance.STK_SHAREHOLDERS_SHARE_CHANGE.code==code).limit(n))
```

获取上市公司大股东的增减持情况。

**参数：**

- **query(finance.STK_SHAREHOLDERS_SHARE_CHANGE)**：表示从finance.STK_SHAREHOLDERS_SHARE_CHANGE这张表中查询上市公司大股东的增减持情况，还可以指定所要查询的字段名，格式如下：query(库名.表名.字段名1，库名.表名.字段名2），多个字段用英文逗号进行分隔；query函数的更多用法详见：[sqlalchemy.orm.query.Query对象](http://docs.sqlalchemy.org/en/rel_1_0/orm/query.html)
    
    **finance.STK_SHAREHOLDERS_SHARE_CHANGE**：代表上市公司大股东增减持情况表，收录了大股东的增减持情况，表结构和字段信息如下：
    
    | 段名称 | 中文名称 | 字段类型 | 备注/示例 |
    | --- | --- | --- | --- |
    | company_id | 公司ID | int |  |
    | company_name | 公司名称 | varchar(100) |  |
    | code | 股票代码 | varchar(12) |  |
    | pub_date | 公告日期 | date |  |
    | end_date | 增（减）持截止日 | date | 变动截止日期 |
    | type | 增（减）持类型 | int | 0--增持;1--减持 |
    | shareholder_id | 股东ID | int |  |
    | shareholder_name | 股东名称 | varchar(100) |  |
    | change_number | 变动数量 | int | 股 |
    | change_ratio | 变动数量占总股本比例 | decimal(10,4) | 录入变动数量后，系统自动计算变动比例，持股比例可以用持股数量除以股本情况表中的总股本 |
    | price_ceiling | 增（减）持价格上限 | varchar(100) | 公告里面一般会给一个增持或者减持的价格区间，上限就是增持价格或减持价格的最高价。如果公告中只披露了平均价，那price_ceiling即为成交均价 |
    | after_change_ratio | 变动后占比 | decimal(10,4) | %，变动后持股数量占总股本比例 |
    
- **filter(finance.STK_SHAREHOLDERS_SHARE_CHANGE.code==code)**：指定筛选条件，通过finance.STK_SHAREHOLDERS_SHARE_CHANGE.code==code可以指定你想要查询的股票代码；除此之外，还可以对表中其他字段指定筛选条件，如finance.STK_SHAREHOLDERS_SHARE_CHANGE.pub_date>='2015-01-01'，表示筛选公布日期大于等于2015年1月1日之后的数据；多个筛选条件用英文逗号分隔。
    
- **limit(n)**：限制返回的数据条数，n指定返回条数。
    

**返回结果：**

- 返回一个 dataframe， 每一行对应数据表中的一条数据， 列索引是你所查询的字段名称

**注意：**

1.  **为了防止返回数据量过大, 我们每次最多返回4000行**
2.  不能进行连表查询，即同时查询多张表的数据

**示例：**

```python
#指定查询对象为万科（000002.XSHE)的大股东增减持情况，返回条数为10条
q=query(finance.STK_SHAREHOLDERS_SHARE_CHANGE).filter(finance.STK_SHAREHOLDERS_SHARE_CHANGE.code=='000002.XSHE',finance.STK_SHAREHOLDERS_SHARE_CHANGE.pub_date>'2015-01-01').limit(10)
df=finance.run_query(q)
print(df)

     id company_id company_name         code    pub_date    end_date type  \
0  1362  430000002   万科企业股份有限公司  000002.XSHE  2015-10-22  2015-10-20    0

  shareholder_id shareholder_name change_number change_ratio price_ceiling  \
0            NaN     深圳市矩盛华股份有限公司   369084217.0         3.34           NaN

  after_change_ratio
0                NaN
```

### 受限股份上市公告日期

```python
from jqdata import finance
finance.run_query(query(finance.STK_LIMITED_SHARES_LIST).filter(finance.STK_LIMITED_SHARES_LIST.code==code).limit(n))
```

获取上市公司受限股份上市公告日期和预计解禁日期。

**参数：**

- **query(finance.STK_LIMITED_SHARES_LIST)**：表示从finance.STK_LIMITED_SHARES_LIST这张表中查询上市公司受限股份上市公告和预计解禁的日期，还可以指定所要查询的字段名，格式如下：query(库名.表名.字段名1，库名.表名.字段名2），多个字段用英文逗号进行分隔；query函数的更多用法详见：[query简单教程](https://www.joinquant.com/view/community/detail/433d0e9ed9fed11fc9f7772eab8d9376)
    
- **finance.STK_LIMITED_SHARES_LIST**：代表受限股份上市公告日期表，收录了上市公司受限股份上市公告和预计解禁的日期，表结构和字段信息如下：
    
    | 字段名称 | 中文名称 | 字段类型 | 含义 |
    | --- | --- | --- | --- |
    | company_id | 公司ID | int |  |
    | company_name | 公司名称 | varchar(100) |  |
    | code | 股票代码 | varchar(12) |  |
    | pub_date | 公告日期 | date | 上市流通方案公布日期 |
    | shareholder_name | 股东名称 | varchar(100) |  |
    | expected_unlimited_date | 预计解除限售日期 | date |  |
    | expected_unlimited_number | 预计解除限售数量 | int | 单位：股 |
    | expected_unlimited_ratio | 预计解除限售比例 | decimal(10,4) | 单位：％；预计解除限售数量占总股本比例 |
    | actual_unlimited_date | 实际解除限售日期 | date |  |
    | actual_unlimited_number | 实际解除限售数量 | int | 单位：股 |
    | actual_unlimited_ratio | 实际解除限售比例 | decimal(10,4) | 单位：％；实际解除限售数量占总股本比例 |
    | limited_reason_id | 限售原因编码 | int | 如下 限售原因编码 |
    | limited_reason | 限售原因 | varchar(60) | 用户选择：股改限售；发行限售 |
    | trade_condition | 上市交易条件 | varchar(500) | 股份上市交易的条件限制 |
    
- **filter(finance.STK_LIMITED_SHARES_LIST.code==code)**：指定筛选条件，通过finance.STK_LIMITED_SHARES_LIST.code==code可以指定你想要查询的股票代码；除此之外，还可以对表中其他字段指定筛选条件，如finance.STK_LIMITED_SHARES_LIST.pub_date>='2015-01-01'，表示筛选公布日期大于等于2015年1月1日之后的数据；多个筛选条件用英文逗号分隔。
    
- **limit(n)**：限制返回的数据条数，n指定返回条数。
    

**返回结果：**

- 返回一个 dataframe， 每一行对应数据表中的一条数据， 列索引是你所查询的字段名称

**注意：**

1.  **为了防止返回数据量过大, 我们每次最多返回4000行**
2.  不能进行连表查询，即同时查询多张表的数据

**示例：**

```python
#指定查询对象为华泰证券（600276.XSHG)的受限股份上市公告日期，返回条数为10条
q=query(finance.STK_LIMITED_SHARES_LIST).filter(finance.STK_LIMITED_SHARES_LIST.code=='601688.XSHG',finance.STK_LIMITED_SHARES_LIST.pub_date>'2018-01-01').limit(10)
df=finance.run_query(q)
print(df)

      id  company_id company_name         code    pub_date   shareholder_name  \
0  34395   460000161   华泰证券股份有限公司  601688.XSHG  2018-08-04  阿里巴巴（中国）网络技术有限公司等

  expected_unlimited_date  expected_unlimited_number expected_unlimited_ratio  \
0              2019-08-02               1.088731e+09                     None

  actual_unlimited_date actual_unlimited_number actual_unlimited_ratio  \
0                  None                    None                   None

   limited_reason_id limited_reason trade_condition
0             309008        非公开发行限售            None
```

### 受限股份实际解禁日期

```python
from jqdata import finance
finance.run_query(query(finance.STK_LIMITED_SHARES_UNLIMIT).filter(finance.STK_LIMITED_SHARES_UNLIMIT.code==code).limit(n))
```

获取公司已上市的受限股份实际解禁的日期。

**参数：**

- **query(finance.STK_LIMITED_SHARES_UNLIMIT)**：表示从finance.STK_LIMITED_SHARES_UNLIMIT这张表中查询上市公司受限股份实际解禁的日期，还可以指定所要查询的字段名，格式如下：query(库名.表名.字段名1，库名.表名.字段名2），多个字段用英文逗号进行分隔；query函数的更多用法详见：[sqlalchemy.orm.query.Query对象](http://docs.sqlalchemy.org/en/rel_1_0/orm/query.html)
    
    **finance.STK_LIMITED_SHARES_UNLIMIT**：代表上市公司受限股份实际解禁表，收录了上市公司受限股份实际解禁的日期信息，表结构和字段信息如下：
    
    | 字段名称 | 中文名称 | 字段类型 | 含义 |
    | --- | --- | --- | --- |
    | company_id | 公司ID | int |  |
    | company_name | 公司名称 | varchar(100) |  |
    | code | 股票代码 | varchar(12) |  |
    | pub_date | 公告日期 | date |  |
    | shareholder_name | 股东名称 | varchar(100) |  |
    | actual_unlimited_date | 实际解除限售日期 | date |  |
    | actual_unlimited_number | 实际解除限售数量 | int | 股 |
    | actual_unlimited_ratio | 本次解禁实际可流通比例 | decimal(10,4) | 本次解禁实际可流通数量/总股本，单位% |
    | limited_reason_id | 限售原因编码 | int |  |
    | limited_reason | 限售原因 | varchar(60) |  |
    | actual_trade_number | 实际可流通数量 | int | 股 |
    
- **filter(finance.STK_LIMITED_SHARES_UNLIMIT.code==code)**：指定筛选条件，通过finance.STK_LIMITED_SHARES_UNLIMIT.code==code可以指定你想要查询的股票代码；除此之外，还可以对表中其他字段指定筛选条件，如finance.STK_LIMITED_SHARES_UNLIMIT.pub_date>='2015-01-01'，表示筛选公布日期大于等于2015年1月1日之后的数据；多个筛选条件用英文逗号分隔。
    
- **limit(n)**：限制返回的数据条数，n指定返回条数。
    

**返回结果：**

- 返回一个 dataframe， 每一行对应数据表中的一条数据，列索引是你所查询的字段名称

**注意：**

1.  **为了防止返回数据量过大, 我们每次最多返回4000行**
2.  不能进行连表查询，即同时查询多张表的数据

**示例：**

```python
#指定查询对象为恒瑞医药（600276.XSHG)的受限股份实际解禁日期，返回条数为10条
q=query(finance.STK_LIMITED_SHARES_UNLIMIT).filter(finance.STK_LIMITED_SHARES_UNLIMIT.code=='600276.XSHG',finance.STK_LIMITED_SHARES_UNLIMIT.pub_date>'2015-01-01').limit(10)
df=finance.run_query(q)
print(df)

      id company_id  company_name         code    pub_date shareholder_name  \
0  11252  420600276  江苏恒瑞医药股份有限公司  600276.XSHG  2015-07-14             蒋素梅等
1  11889  420600276  江苏恒瑞医药股份有限公司  600276.XSHG  2016-01-16             周云曙等
2  12613  420600276  江苏恒瑞医药股份有限公司  600276.XSHG  2016-07-14             蒋素梅等
3  13335  420600276  江苏恒瑞医药股份有限公司  600276.XSHG  2017-01-10             周云曙等
4  14162  420600276  江苏恒瑞医药股份有限公司  600276.XSHG  2017-07-20             蒋素梅等
5  15291  420600276  江苏恒瑞医药股份有限公司  600276.XSHG  2018-01-26             周云曙等

  actual_unlimited_date actual_unlimited_number actual_unlimited_ratio  \
0            2015-07-17               4021160.0                 0.1672
1            2016-01-21                531960.0                 0.0068
2            2016-07-19               3488285.0                 0.1486
3            2017-01-16                478764.0                 0.0051
4            2017-07-25               4024089.0                 0.1167
5            2018-01-31                574517.0                 0.0051

  limited_reason_id limited_reason actual_trade_number
0            309004           股权激励           3270410.0
1            309004           股权激励            132990.0
2            309004           股权激励           3488285.0
3            309004           股权激励            119691.0
4            309004           股权激励           3287409.0
5            309004           股权激励            143628.0
```

### 上市公司股本变动

```python
from jqdata import finance
finance.run_query(query(finance.STK_CAPITAL_CHANGE).filter(finance.STK_CAPITAL_CHANGE.code==code).limit(n))
```

获取上市公司的股本变动情况

**参数：**

- **query(finance.STK_CAPITAL_CHANGE)**：表示从finance.STK_CAPITAL_CHANGE这张表中查询股票简称的变更情况，还可以指定所要查询的字段名，格式如下：query(库名.表名.字段名1，库名.表名.字段名2)，多个字段用英文逗号进行分隔；query函数的更多用法详见：[sqlalchemy.orm.query.Query对象](http://docs.sqlalchemy.org/en/rel_1_0/orm/query.html)
    
    **finance.STK_CAPITAL_CHANGE**：代表上市公司的股本变动表，收录了上市公司发生上市、增发、配股，转增等时间带来的股本变动情况。表结构和字段信息如下：
    
    | 字段名称 | 中文名称 | 字段类型 | 含义 |
    | --- | --- | --- | --- |
    | company_id | 公司ID | int |  |
    | company_name | 公司名称 | varchar(100) |  |
    | code | 股票代码 | varchar(12) |  |
    | change_date | 变动日期 | date |  |
    | pub_date | 公告日期 | date |  |
    | change_reason_id | 变动原因编码 | int |  |
    | change_reason | 变动原因 | varchar(120) |  |
    | share_total | 总股本 | decimal(20,4) | 未流通股份+已流通股份，单位：万股 |
    | share_non_trade | 未流通股份 | decimal(20,4) | 发起人股份 + 募集法人股份 + 内部职工股 + 优先股+转配股+其他未流通股+配售法人股+已发行未上市股份 |
    | share_start | 发起人股份 | decimal(20,4) | 国家持股 +国有法人持股+境内法人持股 + 境外法人持股 + 自然人持股 |
    | share_nation | 国家持股 | decimal(20,4) | 单位：万股 |
    | share_nation_legal | 国有法人持股 | decimal(20,4) | 单位：万股 |
    | share_instate_legal | 境内法人持股 | decimal(20,4) | 单位：万股 |
    | share_outstate_legal | 境外法人持股 | decimal(20,4) | 单位：万股 |
    | share_natural | 自然人持股 | decimal(20,4) | 单位：万股 |
    | share_raised | 募集法人股 | decimal(20,4) | 单位：万股 |
    | share_inside | 内部职工股 | decimal(20,4) | 单位：万股 |
    | share_convert | 转配股 | decimal(20,4) | 单位：万股 |
    | share_perferred | 优先股 | decimal(20,4) | 单位：万股 |
    | share_other_nontrade | 其他未流通股 | decimal(20,4) | 单位：万股 |
    | share_limited | 流通受限股份 | decimal(20,4) | 单位：万股 |
    | share_legal_issue | 配售法人股 | decimal(20,4) | 战略投资配售股份+证券投资基金配售股份+一般法人配售股份(万股) |
    | share_strategic_investor | 战略投资者持股 | decimal(20,4) | 单位：万股 |
    | share_fund | 证券投资基金持股 | decimal(20,4) | 单位：万股 |
    | share_normal_legal | 一般法人持股 | decimal(20,4) | 单位：万股 |
    | share_other_limited | 其他流通受限股份 | decimal(20,4) | 单位：万股 |
    | share_nation_limited | 国家持股（受限） | decimal(20,4) | 单位：万股 |
    | share_nation_legal_limited | 国有法人持股（受限） | decimal(20,4) | 单位：万股 |
    | other_instate_limited | 其他内资持股（受限） | decimal(20,4) | 单位：万股 |
    | legal of other_instate_limited | 其他内资持股（受限）中的境内法人持股 | decimal(20,4) | 单位：万股 |
    | natural of other_instate_limited | 其他内资持股（受限）中的境内自然人持股 | decimal(20,4) | 单位：万股 |
    | outstate_limited | 外资持股（受限） | decimal(20,4) | 单位：万股 |
    | legal of outstate_limited | 外资持股（受限）中的境外法人持股 | decimal(20,4) | 单位：万股 |
    | natural of outstate_limited | 外资持股（受限）境外自然人持股 | decimal(20,4) | 单位：万股 |
    | share_trade_total | 已流通股份 | decimal(20,4) | 人民币普通股 + 境内上市外资股（B股）+ 境外上市外资股（H股）+高管股+ 其他流通股 |
    | share_rmb | 人民币普通股 | decimal(20,4) | 单位：万股 |
    | share_b | 境内上市外资股（B股） | decimal(20,4) | 单位：万股 |
    | share_b_limited | 限售B股 | decimal（20,4） | 单位：万股 |
    | share_h | 境外上市外资股（H股） | decimal(20,4) | 单位：万股 |
    | share_h_limited | 限售H股 | decimal(20,4) | 单位：万股 |
    | share_management | 高管股 | decimal(20,4) | 单位：万股 |
    | share_management_limited | 限售高管股 | decimal(20,4) | 单位：万股 |
    | share_other_trade | 其他流通股 | decimal(20,4) | 单位：万股 |
    | control_shareholder_limited | 控股股东、实际控制人(受限) | decimal(20,4) | 单位：万股 |
    | core_employee_limited | 核心员工(受限) | decimal(20,4) | 单位：万股 |
    | individual_fund_limited | 个人或基金(受限) | decimal(20,4) | 单位：万股 |
    | other_legal_limited | 其他法人(受限) | decimal(20,4) | 单位：万股 |
    | other_limited | 其他(受限) | decimal(20,4) | 单位：万股 |
    
- **filter(finance.STK_CAPITAL_CHANGE.code==code)**：指定筛选条件，通过finance.STK_CAPITAL_CHANGE.code==code可以指定你想要查询的股票代码；除此之外，还可以对表中其他字段指定筛选条件，如finance.STK_CAPITAL_CHANGE.pub_date>='2015-01-01'，表示筛选公布日期大于等于2015年1月1日之后的数据；多个筛选条件用英文逗号分隔。
    
- **limit(n)**：限制返回的数据条数，n指定返回条数。
    

**返回结果：**

- 返回一个 dataframe， 每一行对应数据表中的一条数据， 列索引是你所查询的字段名称

**注意：**

1.  **为了防止返回数据量过大, 我们每次最多返回4000行**
2.  不能进行连表查询，即同时查询多张表的数据

**示例：**

```python
#指定查询对象为恒瑞医药（600276.XSHG)的股本变动情况，返回条数为10条
q=query(finance.STK_CAPITAL_CHANGE).filter(finance.STK_CAPITAL_CHANGE.code=='600276.XSHG',finance.STK_CAPITAL_CHANGE.pub_date>'2015-01-01').limit(10)
df=finance.run_query(q)
print(df)

      id company_id  company_name         code change_date    pub_date  \
0    107  420600276  江苏恒瑞医药股份有限公司  600276.XSHG  2017-01-16  2017-01-10
1   3506  420600276  江苏恒瑞医药股份有限公司  600276.XSHG  2017-05-31  2017-05-22
2   4130  420600276  江苏恒瑞医药股份有限公司  600276.XSHG  2017-06-29  2017-06-29
3   4417  420600276  江苏恒瑞医药股份有限公司  600276.XSHG  2017-07-25  2017-07-20
4   7659  420600276  江苏恒瑞医药股份有限公司  600276.XSHG  2017-06-30  2017-08-30
5   8432  420600276  江苏恒瑞医药股份有限公司  600276.XSHG  2017-09-22  2017-09-22
6   9839  420600276  江苏恒瑞医药股份有限公司  600276.XSHG  2018-01-18  2018-01-20
7   9911  420600276  江苏恒瑞医药股份有限公司  600276.XSHG  2018-01-31  2018-01-26
8  12261  420600276  江苏恒瑞医药股份有限公司  600276.XSHG  2017-12-31  2018-04-16

  change_reason_id change_reason  share_total share_non_trade      ...       \
0           306037        激励股份上市  234745.9674             0.0      ...
1           306010            送股  281695.1609             0.0      ...
2           306016          股份回购  281688.9833             0.0      ...
3           306037        激励股份上市  281688.9833             0.0      ...
4           306019          定期报告  281688.9833             0.0      ...
5           306016          股份回购  281688.3038             0.0      ...
6           306004        增发新股上市  283264.8038             0.0      ...
7           306037        激励股份上市  283264.8038             0.0      ...
8           306019          定期报告  281688.3038             0.0      ...

  share_h share_h_limited share_management share_management_limited  \
0     0.0             NaN              0.0                      NaN
1     0.0             NaN              0.0                      NaN
2     0.0             NaN              0.0                      NaN
3     0.0             NaN              0.0                      NaN
4     0.0             NaN              0.0                      NaN
5     0.0             NaN              0.0                      NaN
6     0.0             NaN              0.0                      NaN
7     0.0             NaN              0.0                      NaN
8     0.0             NaN              0.0                      NaN

  share_other_trade control_shareholder_limited core_employee_limited  \
0               0.0                         NaN                   NaN
1               0.0                         NaN                   NaN
2               0.0                         NaN                   NaN
3               0.0                         NaN                   NaN
4               0.0                         NaN                   NaN
5               0.0                         NaN                   NaN
6               0.0                         NaN                   NaN
7               0.0                         NaN                   NaN
8               0.0                         NaN                   NaN

  individual_fund_limited other_legal_limited other_limited
0                     NaN                 NaN           NaN
1                     NaN                 NaN           NaN
2                     NaN                 NaN           NaN
3                     NaN                 NaN           NaN
4                     NaN                 NaN           NaN
5                     NaN                 NaN           NaN
6                     NaN                 NaN           NaN
7                     NaN                 NaN           NaN
8                     NaN                 NaN           NaN

[9 rows x 49 columns]
```

## 获取单季度/年度财务数据

查询股票的**市值数据、资产负债数据、现金流数据、利润数据、财务指标数据**. 详情通过[财务数据列表](https://www.joinquant.com/help/api/help?name=Stock#%E8%B4%A2%E5%8A%A1%E6%95%B0%E6%8D%AE%E5%88%97%E8%A1%A8)查看! 可通过以下api进行查询 :

名称 描述

get_fundamentals 查询财务数据

```python
get_fundamentals(query_object, date=None, statDate=None)
```

查询财务数据，详细的财务数据表及字段描述请点击[财务数据文档](https://www.joinquant.com/help/api/help?name=Stock#%E8%8E%B7%E5%8F%96%E5%8D%95%E5%AD%A3%E5%BA%A6%E5%B9%B4%E5%BA%A6%E8%B4%A2%E5%8A%A1%E6%95%B0%E6%8D%AE)查看，Query 对象的使用方法请参考[Query的简单教程](https://www.joinquant.com/view/community/detail/433d0e9ed9fed11fc9f7772eab8d9376) date和statDate参数只能传入一个: - 传入date时, 查询**指定日期date收盘后所能看到的最近(对市值表来说, 最近一天, 对其他表来说, 最近一个季度)的数据**, 默认我们会查找上市公司在当前日期之前发布的数据, 不会有未来函数.不要传递当天的日期取获取估值表,pe/市值等依赖收盘价的指标是盘后更新的。 - 传入statDate时, 查询 **statDate 指定的季度或者年份的财务数据**. 注意: 1. 由于公司发布财报不及时, 一般是看不到当季度或年份的财务报表的, 回测中使用这个数据可能会有未来函数, 请注意规避. 2. 由于估值表每天更新, 当按季度或者年份查询时, 返回季度或者年份最后一天的数据 3. 由于“资产负债数据”这个表是存量性质的， 查询年度数据是返回第四季度的数据。 4. 银行业、券商、保险专项数据只有年报数据，需传入statDate参数，当传入 date 参数 或 statDate 传入季度时返回空，请自行避免未来函数。 当 date 和 statDate 都不传入时, 相当于使用 date 参数, date 的默认值下面会描述. **参数** - query_object: 一个[sqlalchemy.orm.query.Query对象](https://docs.sqlalchemy.org/en/rel_1_0/orm/query.html), 可以通过全局的 query 函数获取 Query 对象,[Query对象的简单使用教程](https://www.joinquant.com/view/community/detail/433d0e9ed9fed11fc9f7772eab8d9376) - date: 查询日期, 一个字符串(格式类似'2015-10-15')或者[datetime.date]/[datetime.datetime]对象, 可以是None, 使用默认日期. 这个默认日期在回测和研究模块上有点差别: 1. 回测模块: 默认值会随着回测日期变化而变化, 等于 context.current_dt 的前一天(实际生活中我们只能看到前一天的财报和市值数据, 所以要用前一天) 2. 研究模块: 使用平台财务数据的最新日期, 一般是昨天. - statDate: 财报统计的季度或者年份, 一个字符串, 有两种格式: 1. 季度: 格式是: **年 + 'q' + 季度序号**, 例如: '2015q1', '2013q4'. 2. 年份: 格式就是年份的数字, 例如: '2015', '2016'. **返回** 返回一个 [pandas.DataFrame], 每一行对应数据库返回的每一行(可能是几个表的联合查询结果的一行), 列索引是你查询的所有字段 注意： 1. 为了防止返回数据量过大, 我们每次最多返回5000行 2. 当相关股票上市前、退市后，财务数据返回各字段为空 **示例**

```python
# 查询'000001.XSHE'的所有市值数据, 时间是2015-10-15
q = query(
    valuation
).filter(
    valuation.code == '000001.XSHE'
)
df = get_fundamentals(q, '2015-10-15')
# 打印出总市值
log.info(df['market_cap'][0])
```

```python
# 获取多只股票在某一日期的市值, 利润
df = get_fundamentals(query(
        valuation, income
    ).filter(
        # 这里不能使用 in 操作, 要使用in_()函数
        valuation.code.in_(['000001.XSHE', '600000.XSHG'])
    ), date='2015-10-15')
```

```python
# 选出所有的总市值大于1000亿元, 市盈率小于10, 营业总收入大于200亿元的股票
df = get_fundamentals(query(
        valuation.code, valuation.market_cap, valuation.pe_ratio, income.total_operating_revenue
    ).filter(
        valuation.market_cap > 1000,
        valuation.pe_ratio < 10,
        income.total_operating_revenue > 2e10
    ).order_by(
        # 按市值降序排列
        valuation.market_cap.desc()
    ).limit(
        # 最多返回100个
        100
    ), date='2015-10-15')
```

```python
# 使用 or_ 函数: 查询总市值大于1000亿元 **或者** 市盈率小于10的股票
from sqlalchemy.sql.expression import or_
get_fundamentals(query(
        valuation.code
    ).filter(
        or_(
            valuation.market_cap > 1000,
            valuation.pe_ratio < 10
        )
    ))
```

```python
# 查询平安银行2014年四个季度的季报, 放到数组中
q = query(
        income.statDate,
        income.code,
        income.basic_eps,
        balance.cash_equivalents,
        cash_flow.goods_sale_and_service_render_cash
    ).filter(
        income.code == '000001.XSHE',
    )

rets = [get_fundamentals(q, statDate='2014q'+str(i)) for i in range(1, 5)]
```

```python
# 查询平安银行2014年的年报
q = query(
        income.statDate,
        income.code,
        income.basic_eps,
        cash_flow.goods_sale_and_service_render_cash
    ).filter(
        income.code == '000001.XSHE',
    )

ret = get_fundamentals(q, statDate='2014')
```

get_fundamentals_continuously 查询多日的财务数据

```python
get_fundamentals_continuously(query_object, end_date=None,count=None, panel=True)
```

查询多日财务数据，详细的财务数据表及字段描述请点击[财务数据文档](https://www.joinquant.com/help/api/help?name=Stock#%E8%8E%B7%E5%8F%96%E5%8D%95%E5%AD%A3%E5%BA%A6%E5%B9%B4%E5%BA%A6%E8%B4%A2%E5%8A%A1%E6%95%B0%E6%8D%AE)查看，Query 对象的使用方法请参考[Query的简单教程](https://www.joinquant.com/view/community/detail/433d0e9ed9fed11fc9f7772eab8d9376) **参数** - query_object: 一个[sqlalchemy.orm.query.Query对象](https://docs.sqlalchemy.org/en/rel_1_0/orm/query.html), 可以通过全局的 query 函数获取 Query 对象,[Query对象的简单使用教程](https://www.joinquant.com/view/community/detail/433d0e9ed9fed11fc9f7772eab8d9376) - end_date: 查询日期, 一个字符串(格式类似'2015-10-15')或者[datetime.date]/[datetime.datetime]对象, 可以是None, 使用默认日期. 这个默认日期在回测和研究模块上有点差别: 1. 回测模块: 默认值会随着回测日期变化而变化, 等于 context.current_dt 的前一天(实际生活中我们只能看到前一天的财报和市值数据, 所以要用前一天) 2. 研究模块: 使用平台财务数据的最新日期, 一般是昨天. - count: 获取 end_date 前 count 个日期的数据 - panel：在pandas 0.24版后，panel被彻底移除。获取多标的数据时建议设置panel为False，返回等效的dataframe **返回** - 默认panel=True，返回一个 pandas.Panel； - 建议设置panel为False，返回等效的dataframe； **出于性能方面考虑，我们做出了返回总条数不超过5000条的限制。 也就是说：查询的股票数量\*count 要小于5000。 否则，返回的数据会不完整。** **示例**

```python
>>> q = query(valuation.turnover_ratio,
              valuation.market_cap,
              indicator.eps
            ).filter(valuation.code.in_(['000001.XSHE', '600000.XSHG']))

>>> panel = get_fundamentals_continuously(q, end_date='2018-01-01', count=5)

>>> panel

\<class 'pandas.core.panel.Panel'\>
Dimensions: 3 (items) x 5 (major_axis) x 2 (minor_axis)
Items axis: turnover_ratio to eps
Major_axis axis: 2017-12-25 to 2017-12-29
Minor_axis axis: 000001.XSHE to 600000.XSHG

>>> panel.minor_xs('600000.XSHG')

turnover_ratio  market_cap  eps
day
2017-12-25  0.0687  3695.4270   0.48
2017-12-26  0.0542  3710.1030   0.48
2017-12-27  0.1165  3704.2324   0.48
2017-12-28  0.0849  3680.7510   0.48
2017-12-29  0.0582  3695.4270   0.48


>>> panel.major_xs('2017-12-25')

turnover_ratio  market_cap  eps
code
000001.XSHE 0.9372  2275.0796   0.38
600000.XSHG 0.0687  3695.4270   0.48

>>> panel.xs('turnover_ratio',axis=0)
# axis=0 表示 items axis; axis=1 表示 major axis; axis=2 表示 minor axis

code    000001.XSHE 600000.XSHG
day
2017-12-25  0.9372  0.0687
2017-12-26  0.6642  0.0542
2017-12-27  0.8078  0.1165
2017-12-28  0.9180  0.0849
2017-12-29  0.5810  0.0582
```

get_history_fundamentals 获取多个季度/年度的历史财务数据

获取多个季度/年度的三大财务报表和财务指标数据. 可指定单季度数据, 也可以指定年度数据。可以指定观察日期, 也可以指定最后一个报告期的结束日期

```python
get_history_fundamentals(security, fields, watch_date=None, stat_date=None, count=1, interval='1q', stat_by_year=False)
```

##### **参数** - security：股票代码或者股票代码列表。 - fields：要查询的财务数据的列表, 季度数据和年度数据可选择的列不同。示例： [balance.cash_equivalents, cash_flow.net_deposit_increase, income.total_operating_revenue] - watch_date：观察日期, 如果指定, 将返回 watch_date 日期前(包含该日期)发布的报表数据 - stat_date：统计日期, 可以是 '2019'/'2019q1'/'2018q4' 格式, 如果指定, 将返回 stat_date 对应报告期及之前的历史报告期的报表数据 - watch_date 和 stat_date 只能指定一个, 而且必须指定一个 - 如果没有 stat_date 指定报告期的数据, 则该数据会缺失一行. - count：查询历史的多个报告期时, 指定的报告期数量. 如果股票历史报告期的数量小于 count, 则该股票返回的数据行数将小于 count - interval：查询多个报告期数据时, 指定报告期间隔, 可选值: '1q'/'1y', 表示间隔一季度或者一年, 举例说明: - stat_date='2019q1', interval='1q', count=4, 将返回 2018q2,2018q3,2018q4,2019q1 的数据 - stat_date='2019q1', interval='1y', count=4, 将返回 2016q1,2017q1,2018q1,2019q1 的数据 - stat_by_year=True, stat_date='2018', interval='1y', count=4 将返回 2015/2016/2017/2018 年度的年报数据 - stat_by_year：bool, 是否返回年度数据. 默认返回的按季度统计的数据(比如income表中只有单个季度的利润). - 如果是True： - interval必须是 '1y' - 如果指定了 stat_date 的话, stat_date 必须是一个代表年份整数、字符串, 表明统计的年份，比如2019, "2019"。但不能是"20191q"这种格式。 - fields 可以选择 balance/income/cash_flow/indicator/bank_indicator/security_indicator/insurance_indicator 表中的列 - 如果是False： fields只能选择balance/income/cash_flow/indicator 表中的列 ##### **返回值** pandas.DataFrame, 数据库查询结果. 数据格式同 get_fundamentals. 每个股票每个报告期(一季度或者一年)的数据占用一行. ##### **注意** - 不支持valuation市值表 - 推荐用户对结果使用pandas的[groupby](https://pandas.pydata.org/pandas-docs/version/0.22/generated/pandas.DataFrame.groupby.html)方法来进行分组分析数据 - 每次最多返回50000条数据，更多数据需要根据标的或者时间分多次获取 ##### **示例**

```
from jqdata import *
security = ['000001.XSHE', '600000.XSHG']
df = get_history_fundamentals(security, fields=[balance.cash_equivalents,
        cash_flow.net_deposit_increase, income.total_operating_revenue],
        watch_date=None, stat_date='2019q1', count=5, interval='1q', stat_by_year=False)
print(df)
print(df.groupby('code').mean())
```

get_valuation 获取多个标的在指定交易日范围内的市值表数据

```python
from jqdata import *
get_valuation(security, start_date=None, end_date=None, fields=None, count=None)
```

获取多个标的在指定交易日范围内的市值表数据 ##### **参数** - security: 标的code字符串列表或者单个标的字符串 - end_date: 查询结束时间 - start_date: 查询开始时间，不能与count共用 - count: 表示往前查询每一个标的count个交易日的数据，如果期间标的停牌，则该标的返回的市值数据数量小于count - fields: 财务数据中市值表的字段，返回结果中总会包含code、day字段，可用字段如下： |code| 股票代码 带后缀.XSHE/.XSHG| |day |日期 取数据的日期| | capitalization |总股本(万股)| |circulating_cap| 流通股本(万股)| |market_cap |总市值(亿元)| |circulating_market_cap| 流通市值(亿元)| |turnover_ratio |换手率(%)| |pe_ratio |市盈率(PE, TTM)| |pe_ratio_lyr |市盈率(PE)| |pb_ratio |市净率(PB)| | ps_ratio| 市销率(PS, TTM)| |pcf_ratio| 市现率(PCF, 现金净流量TTM)| ##### **返回值** - 返回一个dataframe，索引默认是pandas的整数索引，返回的结果中总会包含code、day字段。 #### **注意** - 每次最多返回5000条数据，更多数据需要根据标的或者时间分多次获取 - 不要获取当天的估值数据,pe/市值等依赖收盘价的指标是盘后更新的。 ##### **示例**

```python
from jqdata import *
# 传入单个标的
df1 = get_valuation('000001.XSHE', end_date="2019-11-18", count=3, fields=['capitalization', 'market_cap'])
print(df1)

# 传入多个标的
df2 = get_valuation(['000001.XSHE', '000002.XSHE'], end_date="2019-11-18", count=3, fields=['capitalization', 'market_cap'])
print(df2)
```

### 财务数据列表

#### 市值数据

每天更新(总股本，流通股本会在早盘前预先填充 ,其他涉及收盘价的指标盘后更新)

表名: valuation

| 列名 | 列的含义 | 解释 | 公式 |
| --- | --- | --- | --- |
| code | 股票代码 | 带后缀.XSHE/.XSHG |  |
| day | 日期 | 取数据的日期 |  |
| capitalization | 总股本(万股) | 公司已发行的普通股股份总数(包含A股，B股和H股的总股本)，当天盘前会根据最新已知的股本数据进行填充 |  |
| circulating_cap | 流通股本(万股) | 公司已发行的境内上市流通、以人民币兑换的股份总数(A股市场的流通股本)，当天盘前会根据最新已知的流通股本数据进行填充 |  |
| market_cap | 总市值(亿元) | A股收盘价*已发行股票总股本（A股+B股+H股） |  |
| circulating_market_cap | 流通市值(亿元) | 流通市值指在某特定时间内当时可交易的流通股股数乘以当时股价得出的流通股票总价值。 | A股市场的收盘价*A股市场的流通股数 |
| turnover_ratio | 换手率(%) | 指在一定时间内市场中股票转手买卖的频率，是反映股票流通性强弱的指标之一。 | 换手率=[指定交易日成交量(手)×100/截至该日股票的流通股本(股)]×100% |
| pe_ratio | 市盈率(PE, TTM) | 每股市价为每股收益的倍数，反映投资人对每元净利润所愿支付的价格，用来估计股票的投资报酬和风险 | 市盈率（PE，TTM）=（股票在指定交易日期的收盘价 * 截止当日公司总股本）/归属于母公司股东的净利润TTM。 |
| pe_ratio_lyr | 市盈率(PE) | 以上一年度每股盈利计算的静态市盈率. 股价/最近年度报告EPS | 市盈率（PE）=（股票在指定交易日期的收盘价 * 截至当日公司总股本）/归属母公司股东的净利润。 |
| pb_ratio | 市净率(PB) | 每股股价与每股净资产的比率 | 市净率=（股票在指定交易日期的收盘价 * 截至当日公司总股本）/(归属母公司股东的权益MRQ-其他权益工具)。 |
| ps_ratio | 市销率(PS, TTM) | 市销率为股票价格与每股销售收入之比，市销率越小，通常被认为投资价值越高。 | 市销率TTM=（股票在指定交易日期的收盘价 * 截至当日公司总股本）/营业总收入TTM |
| pcf_ratio | 市现率(PCF, 现金净流量TTM) | 每股市价为每股现金净流量的倍数 | 市现率=（股票在指定交易日期的收盘价 * 截至当日公司总股本）/现金及现金等价物净增加额TTM |

#### 资产负债数据

按季度更新, 统计周期是一季度。可以使用get_fundamentals() 的statDate参数查询年度数据。 由于这个表是存量性质的， 查询年度数据是返回第四季度的数据。

表名: balance

| 列名 | 列的含义 | 解释 |
| --- | --- | --- |
| code | 股票代码 | 带后缀.XSHE/.XSHG |
| pubDate | 日期 | 公司发布财报的日期 |
| statDate | 日期 | 财报统计的季度的最后一天, 比如2015-03-31, 2015-06-30 |
| cash_equivalents | 货币资金(元) | 货币资金是指在企业生产经营过程中处于货币形态的那部分资金，按其形态和用途不同可分为包括库存现金、银行存款和其他货币资金。它是企业中最活跃的资金，流动性强，是企业的重要支付手段和流通手段，因而是流动资产的审查重点。货币资金：又称为货币资产，是指在企业生产经营过程中处于货币形态的资产。是指可以立即投入流通，用以购买商品或劳务或用以偿还债务的交换媒介物。 |
| settlement_provi | 结算备付金(元) | 结算备付金是指结算参与人根据规定，存放在其资金交收账户中用于证券交易及非交易结算的资金。资金交收账户即结算备付金账户。 |
| lend_capital | 拆出资金(元) | 企业（金融）拆借给境内、境外其他金融机构的款项。 |
| trading_assets | 交易性金融资产(元) | 交易性金融资产是指：企业为了近期内出售而持有的金融资产。通常情况下，以赚取差价为目的从二级市场购入的股票、债券和基金等，应分类为交易性金融资产，故长期股权投资不会被分类转入交易性金融资产及其直接指定为以公允价值计量且其变动计入当期损益的金融资产进行核算。 |
| bill_receivable | 应收票据(元) | 应收票据是指企业持有的还没有到期、尚未兑现的票据。应收票据是企业未来收取货款的权利，这种权利和将来应收取的货款金额以书面文件形式约定下来，因此它受到法律的保护，具有法律上的约束力。是一种债权凭证。根据我国现行法律的规定，商业汇票的期限不得超过6个月，因而我国的商业汇票是一种流动资产。在我国应收票据、应付票据通常是指“商业汇票”，包括“银行承兑汇票”和“商业承兑汇票”两种，是远期票据，付款期一般在1个月以上，6个月以内。其他的银行票据(支票、本票、汇票}等，都是作为货币资金来核算的，而不作为应收应付票据 |
| account_receivable | 应收账款(元) | 应收账款是指企业在正常的经营过程中因销售商品、产品、提供劳务等业务，应向购买单位收取的款项，包括应由购买单位或接受劳务单位负担的税金、代购买方垫付的各种运杂费等。 |
| advance_payment | 预付款项(元) | 预付款项，包括预付货款和预付工程款等，通常属于流动资产。预付账款与应收账款都属于公司的债权，但两者产生的原因不同，应收账款是公司应收的销货款，通常是用货币清偿的，而预付账款是预付给供货单位的购货款或预付给施工单位的工程价款和材料款，通常是用商品、劳务或完工工程来清偿的。 |
| insurance_receivables | 应收保费(元) | 保险公司按照合同约定应向投保人收取但尚未收到的保费收入。 |
| reinsurance_receivables | 应收分保账款(元) | 指公司开展分保业务而发生的各种应收款项。 |
| reinsurance_contract_reserves_receivable | 应收分保合同准备金(元) | 是用于核算企业（再保险分出人）从事再保险业务确认的应收分保未到期责任准备金，以及应向再保险接受人摊回的保险责任准备金。 |
| interest_receivable | 应收利息(元) | 应收利息是指：短期债券投资实际支付的价款中包含的已到付息期但尚未领取的债券利息。这部分应收利息不计入短期债券投资初始投资成本中。但实际支付的价款中包含尚未到期的债券利息，则计入短期债券投资初始投资成本中（不需要单独核算）。 |
| dividend_receivable | 应收股利(元) | 应收股利是指企业因股权投资而应收取的现金股利以及应收其他单位的利润，包括企业购入股票实际支付的款项中所包括的已宣告发放但尚未领取的现金股利和企业因对外投资应分得的现金股利或利润等，但不包括应收的股票股利。 |
| other_receivable | 其他应收款(元) | 其他应收款是企业应收款项的另一重要组成部分。是企业除应收票据、应收账款和预付账款以外的各种应收暂付款项。其他应收款通常包括暂付款，是指企业在商品交易业务以外发生的各种应收、暂付款项。 |
| bought_sellback_assets | 买入返售金融资产(元) | 指公司按返售协议约定先买入再按固定价格返售的证券等金融资产所融出的资金。 |
| inventories | 存货(元) | 是指企业在日常活动中持有的以备出售的产成品或商品、处在生产过程中的在产品、在生产过程或提供劳务过程中耗用的材料和物料等。 |
| non_current_asset_in_one_year | 一年内到期的非流动资产(元) | 一年内到期的非流动资产反映企业将于一年内到期的非流动资产项目金额。包括一年内到期的持有至到期投资、长期待摊费用和一年内可收回的长期应收款。应根据有关科目的期末余额填列。执行企业会计制度的企业根据“一年内到期的长期债权投资”等科目填列。 |
| other_current_assets | 其他流动资产(元) | 其他流动资产，是指除货币资金、短期投资、应收票据、应收账款、其他应收款、存货等流动资产以外的流动资产 |
| total_current_assets | 流动资产合计(元) | 指在一年内或者超过一年的一个营业周期内变现或者耗用的资产，包括货币资金、短期投资、应收票据、应收账款、坏账准备、应收账款净额、预付账款、其他应收款、存货、待转其他业务支出、待摊费用、待处理流动资产净损失、一年内到期的长期债券投资、其他流动资产等项。 |
| loan_and_advance | 发放委托贷款及垫款(元) | 委托贷款是指由委托人提供合法来源的资金转入委托银行一般委存账户，委托银行根据委托人确定的贷款对象、用途、金额、期限、利率等代为发放、监督使用并协助收回的贷款业务。垫款是指银行在客户无力支付到期款项的情况下，被迫以自有资金代为支付的行为。 |
| hold_for_sale_assets | 可供出售金融资产(元) | 可供出售金融资产指初始确认时即被指定为可供出售的非衍生金融资产，以及下列各类资产之外的非衍生金融资产：（一）贷款和应收款项；（二）持有至到期投资；（三）交易性金融资产。 |
| hold_to_maturity_investments | 持有至到期投资(元) | 持有至到期投资指企业有明确意图并有能力持有至到期，到期日固定、回收金额固定或可确定的非衍生金融资产。以下非衍生金融资产不应划分为持有至到期投资：（一）初始确认时划分为交易性非衍生金融资产；（二）初始确认时被指定为可供出售非衍生金融资产；（三）符合贷款和应收款项定义的非衍生金融资产。 |
| longterm_receivable_account | 长期应收款(元) | 长期应收款是根据长期应收款的账户余额减去未确认融资收益还有一年内到期的长期应收款。 |
| longterm_equity_invest | 长期股权投资(元) | 长期股权投资是指企业持有的对其子公司、合营企业及联营企业的权益性投资以及企业持有的对被投资单位不具有控制、共同控制或重大影响，且在活跃市场中没有报价、公允价值不能可靠计量的权益性投资。 |
| investment_property | 投资性房地产(元) | 投资性房地产是指为赚取租金或资本增值，或两者兼有而持有的房地产。投资性房地产应当能够单独计量和出售。 |
| fixed_assets | 固定资产(元) | 固定资产是指企业为生产商品、提供劳务、出租或经营管理而持有的、使用寿命超过一个会计年度的有形资产。属于产品生产过程中用来改变或者影响劳动对象的劳动资料，是固定资本的实物形态。固定资产在生产过程中可以长期发挥作用，长期保持原有的实物形态，但其价值则随着企业生产经营活动而逐渐地转移到产品成本中去，并构成产品价值的一个组成部分。 |
| constru_in_process | 在建工程(元) | 在建工程是指企业固定资产的新建、改建、扩建，或技术改造、设备更新和大修理工程等尚未完工的工程支出。在建工程通常有”自营”和”出包”两种方式。自营在建工程指企业自行购买工程用料、自行施工并进行管理的工程；出包在建工程是指企业通过签订合同，由其它工程队或单位承包建造的工程。 |
| construction_materials | 工程物资(元) | 工程物资是指用于固定资产建造的建筑材料（如钢材、水泥、玻璃等），企业（民用航空运输）的高价周转件（例如飞机的引擎）等。买回来要再次加工建设的资产。在资产负债表中列示为非流动资产。 |
| fixed_assets_liquidation | 固定资产清理(元) | 固定资产清理是指企业因出售、报废和毁损等原因转入清理的固定资产价值及其在清理过程中所发生的清理费用和清理收入等。 |
| biological_assets | 生产性生物资产(元) | 生产性生物资产是指为产出农产品、提供劳务或出租等目的而持有的生物资产，包括经济林、薪炭林、产畜和役畜等。 |
| oil_gas_assets | 油气资产(元) | 重要资产，其价值在总资产中占有较大比重。油气资产是指油气开采企业所拥有或控制的井及相关设施和矿区权益。油气资产属于递耗资产。递耗资产是通过开掘、采伐、利用而逐渐耗竭，以致无法恢复或难以恢复、更新或按原样重置的自然资源，如矿藏、原始森林等。油气资产是油气生产企业的重要资产，其价值在总资产中占有较大比重。 |
| intangible_assets | 无形资产(元) | 无形资产是指企业拥有或者控制的没有实物形态的可辨认非货币性资产。资产满足下列条件之一的，符合无形资产定义中的可辨认性标准：　1、能够从企业中分离或者划分出来，并能够单独或者与相关合同、资产或负债一起，用于出售、转移、授予许可、租赁或者交换。　2、源自合同性权利或其他法定权利，无论这些权利是否可以从企业或其他权利和义务中转移或者分离。无形资产主要包括专利权、非专利技术、商标权、著作权、土地使用权、特许权等。商誉的存在无法与企业自身分离，不具有可辨认性，不属于本章所指无形资产。 |
| development_expenditure | 开发支出(元) | 开发支出项目是反映企业开发无形资产过程中能够资本化形成无形资产成本的支出部分。开发支出项目应当根据”研发支出”科目中所属的”资本化支出”明细科目期末余额填列。 |
| good_will | 商誉(元) | 商誉是指能在未来期间为企业经营带来超额利润的潜在经济价值，或一家企业预期的获利能力超过可辨认资产正常获利能力（如社会平均投资回报率）的资本化价值。商誉是企业整体价值的组成部分。在企业合并时，它是购买企业投资成本超过被并企业净资产公允价值的差额。 |
| long_deferred_expense | 长期待摊费用(元) | 长期待摊费用是指企业已经支出，但摊销期限在1年以上(不含1年)的各项费用，包括开办费、租入固定资产的改良支出及摊销期在1年以上的固定资产大修理支出、股票发行费用等。应由本期负担的借款利息、租金等，不得作为长期待摊费用。 |
| deferred_tax_assets | 递延所得税资产(元) | 指对于可抵扣暂时性差异，以未来期间很可能取得用来抵扣可抵扣暂时性差异的应纳税所得额为限确认的一项资产。而对于所有应纳税暂时性差异均应确认为一项递延所得税负债，但某些特殊情况除外。递延所得税资产和递延所得税负债是和暂时性差异相对应的，可抵减暂时性差异是将来可用来抵税的部分，是应该收回的资产，所以对应递延所得税资产递延所得税负债是由应纳税暂时性差异产生的，对于影响利润的暂时性差异，确认的递延所得税负债应该调整“所得税费用”。例如会计折旧小于税法折旧，导致资产的账面价值大于计税基础，如果产品已经对外销售了，就会影响利润，所以递延所得税负债应该调整当期的所得税费用。如果暂时性差异不影响利润，而是直接计入所有者权益的，则确认的递延所得税负债应该调整资本公积。例如可供出售金融资产是按照公允价值来计量的，公允价值产升高了，会计上调增了可供出售金融资产的账面价值，并确认的资本公积，因为不影响利润，所以确认的递延所得税负债不能调整所得税费用，而应该调整资本公积。 |
| other_non_current_assets | 其他非流动资产(元) | 贷款是指贷款人(我国的商业银行等金融机构)对借款人提供的并按约定的利率和期限还本付息的货币资金。贷款币可以是人民币，也可以是外币。 |
| total_non_current_assets | 非流动资产合计(元) | 公式：非流动资产合计=所有的非流动资产项目之和—一年内到期的非流动资产=固定资产—累计折旧—固定资产减值准备—一年内到期的非流动资产。 |
| total_assets | 资产总计(元) | 资产总计是指企业拥有或可控制的能以货币计量的经济资源，包括各种财产、债权和其他权利。企业的资产按其流动性划分为：流动资产、长期投资、固定资产、无形资产及递延资产、其他资产等，即为企业资产负债表的资产总计项。所谓流动性是指企业资产的变现能力和支付能力。该指标根据会计“资产负债表”中“资产总计”项的年末数填列。资产总计=流动资产+长期投资+固定资产+无形及递延资产+其他资产。 |
| shortterm_loan | 短期借款(元) | 短期借款企业用来维持正常的生产经营所需的资金或为抵偿某项债务而向银行或其他金融机构等外单位借入的、还款期限在一年以下或者一年的一个经营周期内的各种借款。 |
| borrowing_from_centralbank | 向中央银行借款(元) | 向中央银行借款的形式有两种，一种是直接借款，也称再贷款;另一种为间接借款，即所谓的再贴现。 |
| deposit_in_interbank | 吸收存款及同业存放(元) | 吸收存款是负债类科目，它核算企业（银行）吸收的除了同业存放款项以外的其他各种存款，即：收到的除金融机构以外的企业或者个人、组织的存款，包括单位存款（企业、事业单位、机关、社会团体等）、个人存款、信用卡存款、特种存款、转贷款资金和财政性存款等。同业存放，也称同业存款，全称是同业及其金融机构存入款项，是指因支付清算和业务合作等的需要，由其他金融机构存放于商业银行的款项。 |
| borrowing_capital | 拆入资金(元) | 拆入资金，是指信托投资公司向银行或其他金融机构借入的资金。拆入资金应按实际借入的金额入账。 |
| trading_liability | 交易性金融负债(元) | 交易性金融负债是指企业采用短期获利模式进行融资所形成的负债，比如短期借款、长期借款、应付债券。作为交易双方来说，甲方的金融债权就是乙方的金融负债，由于融资方需要支付利息，因比，就形成了金融负债。交易性金融负债是企业承担的交易性金融负债的公允价值。 |
| notes_payable | 应付票据(元) | 应付票据是指企业购买材料、商品和接受劳务供应等而开出、承兑的商业汇票，包括商业承兑汇票和银行承兑汇票。在我国应收票据、应付票据仅指“商业汇票”，包括“银行承兑汇票”和“商业承兑汇票”两种，属于远期票据，付款期一般在1个月以上，6个月以内。其他的银行票据（支票、本票、汇票）等，都是作为货币资金来核算的，而不作为应收应付票据。 |
| accounts_payable | 应付账款(元) | 应付账款是指因购买材料、商品或接受劳务供应等而发生的债务，这是买卖双方在购销活动中由于取得物资与支付贷款在时间上不一致而产生的负债。 |
| advance_peceipts | 预收款项(元) | 预收款项是在企业销售交易成立以前，预先收取的部分货款。 |
| sold_buyback_secu_proceeds | 卖出回购金融资产款(元) | 卖出回购金融资产款是用于核算企业（金融）按回购协议卖出票据、证券、贷款等金融资产所融入的资金。 |
| commission_payable | 应付手续费及佣金(元) | 是会计科目的一种，用以核算企业因购买材料、商品和接受劳务供应等经营活动应支付的款项。通常是指因购买材料、商品或接受劳务供应等而发生的债务，这是买卖双方在购销活动中由于取得物资与支付贷款在时间上不一致而产生的负债。 |
| salaries_payable | 应付职工薪酬(元) | 应付职工薪酬是指企业为获得职工提供的服务而给予各种形式的报酬以及其他相关支出。职工薪酬包括：职工工资、奖金、津贴和补贴；职工福利费；医疗保险费、养老保险费、失业保险费、工伤保险费和生育保险费等社会保险费；住房公积金；工会经费和职工教育经费；非货币性福利；因解除与职工的劳动关系给予的补偿；其他与获得职工提供的服务相关的支出。原“应付工资”和“应付福利费”取消，换成“应付职工薪酬”。 |
| taxs_payable | 应交税费(元) | 应交税费是指企业根据在一定时期内取得的营业收入、实现的利润等，按照现行税法规定，采用一定的计税方法计提的应交纳的各种税费。应交税费包括企业依法交纳的增值税、消费税、营业税、所得税、资源税、土地增值税、城市维护建设税、房产税、土地使用税、车船税、教育费附加、矿产资源补偿费等税费，以及在上缴国家之前，由企业代收代缴的个人所得税等。 |
| interest_payable | 应付利息(元) | 应付利息是指金融企业根据存款或债券金额及其存续期限和规定的利率，按期计提应支付给单位和个人的利息。应付利息应按已计但尚未支付的金额入账。应付利息包括分期付息到期还本的长期借款、企业债券等应支付的利息。应付利息与应计利息的区别：应付利息属于借款,应计利息属于企业存款。 |
| dividend_payable | 应付股利(元) | 应付股利是指企业根据年度利润分配方案，确定分配的股利。是企业经董事会或股东大会，或类似机构决议确定分配的现金股利或利润。企业分配的股票股利，不通过“应付股利”科目核算。确定时借记“未分配利润”帐户，贷记“应付股利”帐户；实际支付时借记“应付股利”帐户，贷记“银行存款”帐户。 |
| other_payable | 其他应付款(元) | 其他应付款是财务会计中的一个往来科目，通常情况下，该科目只核算企业应付其他单位或个人的零星款项，如应付经营租入固定资产和包装物的租金、存入保证金、应付统筹退休金等。 |
| reinsurance_payables | 应付分保账款(元) | 应付分保账款表示债务，这样一来，债权、债务关系更加一目了然。另外，财产保险公司应收分保账款是指本公司与其他保险公司之间开展分保业务发生的各种应收款项。 |
| insurance_contract_reserves | 保险合同准备金(元) | 险准备金是指保险人为保证其如约履行保险赔偿或给付义务，根据政府有关法律规定或业务特定需要，从保费收入或盈余中提取的与其所承担的保险责任相对应的一定数量的基金。 |
| proxy_secu_proceeds | 代理买卖证券款(元) | 代理买卖证券款是指公司接受客户委托，代理客户买卖股票、债券和基金等有价证券而收到的款项，包括公司代理客户认购新股的款项、代理客户领取的现金股利和债券利息，代客户向证券交易所支付的配股款等。 |
| receivings_from_vicariously_sold_securities | 代理承销证券款(元) | 代理承销证券款是指公司接受委托，采用承购包销方式或代销方式承销证券所形成的、应付证券发行人的承销资金。 |
| non_current_liability_in_one_year | 一年内到期的非流动负债(元) | 是反映企业各种非流动负债在一年之内到期的金额，包括一年内到期的长期借款、长期应付款和应付债券。本项目应根据上述账户分析计算后填列。计入(收录)流动负债中。 |
| other_current_liability | 其他流动负债(元) | 其他流动负债是指不能归属于短期借款，应付短期债券券，应付票据，应付帐款，应付所得税，其他应付款，预收账款这七款项目的流动负债。但以上各款流动负债，其金额未超过流动负债合计金额百分之五者，得并入其他流动负债内。 |
| total_current_liability | 流动负债合计(元) | 流动负债合计是指企业在一年内或超过一年的一个营业周期内需要偿还的债务，包括短期借款、应付帐款、其他应付款、应付工资、应付福利费、未交税金和未付利润、其他应付款、预提费用等。 |
| longterm_loan | 长期借款(元) | 长期借款是指企业从银行或其他金融机构借入的期限在一年以上(不含一年)的借款。我国股份制企业的长期借款主要是向金融机构借人的各项长期性借款，如从各专业银行、商业银行取得的贷款；除此之外，还包括向财务公司、投资公司等金融企业借人的款项。 |
| bonds_payable | 应付债券(元) | 应付债券是指企业为筹集资金而对外发行的期限在一年以上的长期借款性质的书面证明，约定在一定期限内还本付息的一种书面承诺。 |
| longterm_account_payable | 长期应付款(元) | 长期应付款是指企业除了长期借款和应付债券以外的长期负债，包括应付引进设备款、应付融资租入固定资产的租赁费等。 |
| specific_account_payable | 专项应付款(元) | 专项应付款是企业接受国家拨入的具有专门用途的款项所形成的不需要以资产或增加其他负债偿还的负债。专项应付款指企业接受国家拨入的具有专门用途的拨款，如新产品试制费拨款、中间试验费拨款和重要科学研究补助费拨款等科技三项拨款等。 |
| estimate_liability | 预计负债(元) | 预计负债是因或有事项可能产生的负债。根据或有事项准则的规定，与或有事项相关的义务同时符合以下三个条件的，企业应将其确认为负债：一是该义务是企业承担的现时义务；二是该义务的履行很可能导致经济利益流出企业，这里的“很可能”指发生的可能性为“大于50%，但小于或等于95%”；三是该义务的金额能够可靠地计量。 |
| deferred_tax_liability | 递延所得税负债(元) | 递延所得税负债是指根据应纳税暂时性差异计算的未来期间应付所得税的金额；递延所得税资产和递延所得税负债是和暂时性差异相对应的，可抵减暂时性差异是将来可用来抵税的部分，是应该收回的资产，所以对应递延所得税资产；递延所得税负债是由应纳税暂时性差异产生的，对于影响利润的暂时性差异，确认的递延所得税负债应该调整“所得税费用”。 |
| other_non_current_liability | 其他非流动负债(元) | 其他非流动负债项目是反映企业除长期借款、应付债券等项目以外的其他非流动负债。其他非流动负债项目应根据有关科目的期末余额填列。其他非流动负债项目应根据有关科目期末余额减去将于一年内(含一年)到期偿还数后的余额填列。非流动负债各项目中将于一年内(含一年)到期的非流动负债，应在”一年内到期的非流动负债”项目内单独反映。 |
| total_non_current_liability | 非流动负债合计(元) | 非流动负债合计指企业在偿还期在一年以上的债务，包括长期借款、应付债券和长期应付款。 |
| total_liability | 负债合计(元) | 负债合计是指企业所承担的能以，将以资产或劳务偿还的债务，偿还形式包括货币、资产或提供劳务。 |
| paidin_capital | 实收资本(或股本)(元) | 实收资本是指企业的投资者按照企业章程或合同、协议的约定，实际投入企业的资本。我国实行的是注册资本制，因而，在投资者足额缴纳资本之后，企业的实收资本应该等于企业的注册资本。“实收资本”科目用于核算企业实际收到的投资人投入的资本。 |
| capital_reserve_fund | 资本公积金(元) | 资本公积金是在公司的生产经营之外，由资本、资产本身及其他原因形成的股东权益收入。股份公司的资本公积金，主要来源于的股票发行的溢价收入、接受的赠与、资产增值、因合并而接受其他公司资产净额等。其中，股票发行溢价是上市公司最常见、是最主要的资本公积金来源。 |
| treasury_stock | 库存股(元) | 指股份有限公司已发行的股票，由于公司的重新回购或其他原因且不是为了注销的目的而由公司持有的股票。 |
| specific_reserves | 专项储备(元) | 专项储备用于核算高危行业企业按照规定提取的安全生产费以及维持简单再生产费用等具有类似性质的费用。 |
| surplus_reserve_fund | 盈余公积金(元) | 盈余公积是指企业按照规定从净利润中提取的各种积累资金。 |
| ordinary_risk_reserve_fund | 一般风险准备(元) | 指从事证券业务的金融企业按规定从 净利润中提取，用于弥补亏损的 风险准备。 |
| retained_profit | 未分配利润(元) | 未分配利润是企业未作分配的利润。它在以后年度可继续进行分配，在未进行分配之前，属于所有者权益的组成部分。 |
| foreign_currency_report_conv_diff | 外币报表折算差额(元) | 是指在编制合并财务报表时，把国外子公司或分支机构以所在国家货币编制的财务报表折算成以记账本位币表达的财务报表时，由于报表项目采用不同汇率折算而形成的汇兑损益。 |
| equities_parent_company_owners | 归属于母公司股东权益合计(元) | 母公司股东权益反映的是母公司所持股份部分的所有者权益数，所有者权益合计是反映的是所有的股东包括母公司与少数股东一起100%的股东所持股份的总体所有者权益合计数。即所有者权益合计＝母公司股东权益合计母＋少数股东权益合计。 |
| minority_interests | 少数股东权益(元) | 少数股东权益简称少数股权,是反映除母公司以外的其他投资者在子公司中的权益，表示其他投资者在子公司所有者权益中所拥有的份额。在控股合并形式下，子公司股东权益中未被母公司持有部分。在母公司拥有子公司股份不足100%，即只拥有子公司净资产的部分产权时，子公司股东权益的一部分属于母公司所有，即多数股权，其余部分仍属外界其他股东所有，由于后者在子公司全部股权中不足半数，对子公司没有控制能力，故被称为少数股权。 |
| total_owner_equities | 股东权益合计(元) | 指股本、资本公积、盈余公积、未分配利润的之和，代表了股东对企业的所有权，反映了股东在企业资产中享有的经济利益。 |
| total_sheet_owner_equities | 负债和股东权益合计 | 负债和股东权益总计是等于负债总额加上股东权益总额，也等于资产总额。 |

#### 现金流数据

按季度更新, 统计周期是一季度。可以使用get_fundamentals() 的 statDate 参数查询年度数据。

表名: cash_flow

| 列名 | 列的含义 | 解释 |
| --- | --- | --- |
| code | 股票代码 | 带后缀.XSHE/.XSHG |
| pubDate | 日期 | 公司发布财报日期 |
| statDate | 日期 | 财报统计的季度的最后一天, 比如2015-03-31, 2015-06-30 |
| goods_sale_and_service_render_cash | 销售商品、提供劳务收到的现金(元) | 反映企业本期销售商品、提供劳务收到的现金，以及前期销售商品、提供劳务本期收到的现金（包括销售收入和应向购买者收取的增值税销项税额）和本期预收的款项，减去本期销售本期退回的商品和前期销售本期退回的商品支付的现金。企业销售材料和代购代销业务收到的现金，也在本项目反映。 |
| net_deposit_increase | 客户存款和同业存放款项净增加额(元) | 客户存款和同业存款净增加额=客户存款和同业存款期末余额－客户存款和同业存款期初余额。 |
| net_borrowing_from_central_bank | 向中央银行借款净增加额(元) | 向中央银行借款净增加额=向中央银行借款期末余额－向中央银行借款期初余额。 |
| net_borrowing_from_finance_co | 向其他金融机构拆入资金净增加额(元) | 向其他金融机构拆入资金净增加额=向其他金融机构拆入资金期末余额－向其他金融机构拆入资金期初余额。 |
| net_original_insurance_cash | 收到原保险合同保费取得的现金(元) | 收到原保险合同保费取得的现金 |
| net_cash_received_from_reinsurance_business | 收到再保险业务现金净额(元) | 再保险是指一个保险人，分出一定的保险金额给另一个保险人。 |
| net_insurer_deposit_investment | 保户储金及投资款净增加额(元) | 保户储金，是指保险公司以储金利息作为保费的保险业务，收到保户缴存的储金。投资款是收到股东的款项。 |
| net_deal_trading_assets | 处置交易性金融资产净增加额(元) | 交易性金融资产是指企业为了近期内出售而持有的债券投资、股票投资和基金投资。 |
| interest_and_commission_cashin | 收取利息、手续费及佣金的现金(元) | 收取利息、手续费及佣金的现金 |
| net_increase_in_placements | 拆入资金净增加额(元) | 拆入资金净增加额=拆入资金期末余额－拆入资金期初余额。 |
| net_buyback | 回购业务资金净增加额(元) | 回购交易是质押贷款的一种方式，通常用在政府债券上。债券经纪人向投资者临时出售一定的债券，同时签约在一定的时间内以稍高价格买回来。债券经纪人从中取得资金再用来投资，而投资者从价格差中得利。 |
| tax_levy_refund | 收到的税费返还(元) | 反映企业收到返还的增值税、营业税、所得税、消费税、关税和教育费附加返还款等各种税费。 |
| other_cashin_related_operate | 收到其他与经营活动有关的现金(元) | 反映企业收到的罚款收入、经营租赁收到的租金等其他与经营活动有关的现金流入，金额较大的应当单独列示。 |
| subtotal_operate_cash_inflow | 经营活动现金流入小计(元) | 销售商品、提供劳务+收到的现金收到的税费返还+收到其他与经营活动有关的现金。 |
| goods_and_services_cash_paid | 购买商品、接受劳务支付的现金(元) | 反映企业本期购买商品、接受劳务实际支付的现金（包括增值税进项税额），以及本期支付前期购买商品、接受劳务的未付款项和本期预付款项，减去本期发生的购货退回收到的现金。 |
| net_loan_and_advance_increase | 客户贷款及垫款净增加额(元) | 客户贷款是科目核算信托项目管理运用、处分信托财产而持有的各项贷款。垫款是指银行在客户无力支付到期款项的情况下，被迫以自有资金代为支付的行为。 |
| net_deposit_in_cb_and_ib | 存放中央银行和同业款项净增加额(元) | 存放中央银行款项是指各金融企业在中央银行开户而存入的用于支付清算、调拨款项、提取及缴存现金、往来资金结算以及按吸收存款的一定比例缴存于中央银行的款项和其他需要缴存的款项。存放同业是指商业银行存放在其他银行和非银行金融机构的存款。 |
| original_compensation_paid | 支付原保险合同赔付款项的现金(元) | 赔付支出主要指核算企业（保险）支付的原保险合同赔付款项和再保险合同赔付款项。原保险即是区别于再保险的名词。 |
| handling_charges_and_commission | 支付利息、手续费及佣金的现金(元) | 一般是指涉及到贷款利息，银行扣缴的手续费及佣金等现金的流出，用在利息指出，或者银行手续费支出，佣金支出等业务上。 |
| policy_dividend_cash_paid | 支付保单红利的现金(元) | 保单红利支出是根据原保险合同的约定，按照分红保险产品的红利分配方法及有关精算结果而估算，支付给保单持有人的红利。 |
| staff_behalf_paid | 支付给职工以及为职工支付的现金(元) | 这个项目反映企业实际支付给职工的现金以及为职工支付的现金，包括本期实际支付给职工的工资、奖金、各种津贴和补贴等，以及为职工支付的其他费用。不包括支付的离退休人员的各项费用和支付给在建工程人员的工资等。 |
| tax_payments | 支付的各项税费(元) | 反映企业本期发生并支付的、本期支付以前各期发生的以及预交的教育费附加、矿产资源补偿费、印花税、房产税、土地增值税、车船使用税、预交的营业税等税费，计入固定资产价值、实际支付的耕地占用税、本期退回的增值税、所得税等除外。 |
| other_operate_cash_paid | 支付其他与经营活动有关的现金(元) | 反映企业支付的罚款支出、支付的差旅费、业务招待费、保险费、经营租赁支付的现金等其他与经营活动有关的现金流出，金额较大的应当单独列示。 |
| subtotal_operate_cash_outflow | 经营活动现金流出小计(元) | 购买商品、接受劳务支付的现金+支付给职工以及为职工支付的现金+支付的各项税费+支付其他与经营活动有关的现金。 |
| net_operate_cash_flow | 经营活动产生的现金流量净额(元) | 公式: 经营活动产生的现金流量净额 |
| invest_withdrawal_cash | 收回投资收到的现金(元) | 反映企业出售、转让或到期收回除现金等价物以外的交易性金融资产、长期股权投资而收到的现金，以及收回长期债权投资本金而收到的现金，但长期债权投资收回的利息除外。 |
| invest_proceeds | 取得投资收益收到的现金(元) | 反映企业因股权性投资而分得的现金股利，从子公司、联营企业或合营企业分回利润而收到的现金，以及因债权性投资而取得的现金利息收入，但股票股利除外。 |
| fix_intan_other_asset_dispo_cash | 处置固定资产、无形资产和其他长期资产收回的现金净额(元) | 反映企业出售、报废固定资产、无形资产和其他长期资产所取得的现金（包括因资产毁损而收到的保险赔偿收入），减去为处置这些资产而支付的有关费用后的净额，但现金净额为负数的除外。 |
| net_cash_deal_subcompany | 处置子公司及其他营业单位收到的现金净额(元) | 反映企业处置子公司及其他营业单位所取得的现金减去相关处置费用后的净额。 |
| other_cash_from_invest_act | 收到其他与投资活动有关的现金(元) | 反映企业除上述各项目外收到或支付的其他与投资活动有关的现金流入或流出，金额较大的应当单独列示。 |
| subtotal_invest_cash_inflow | 投资活动现金流入小计(元) | 取得投资收益收到的现金+处置固定资产、无形资产和其他长期资产收回的现金净额+处置子公司及其他营业单位收到的现金净额+收到其他与投资活动有关的现金。 |
| fix_intan_other_asset_acqui_cash | 购建固定资产、无形资产和其他长期资产支付的现金(元) | 反映企业购买、建造固定资产、取得无形资产和其他长期资产所支付的现金及增值税款、支付的应由在建工程和无形资产负担的职工薪酬现金支出，但为购建固定资产而发生的借款利息资本化部分、融资租入固定资产所支付的租赁费除外。 |
| invest_cash_paid | 投资支付的现金(元) | 反映企业取得的除现金等价物以外的权益性投资和债权性投资所支付的现金以及支付的佣金、手续费等附加费用。 |
| impawned_loan_net_increase | 质押贷款净增加额(元) | 质押贷款是指贷款人按《担保法》规定的质押方式以借款人或第三人的动产或权利为质押物发放的贷款。 |
| net_cash_from_sub_company | 取得子公司及其他营业单位支付的现金净额(元) | 反映企业购买子公司及其他营业单位购买出价中以现金支付的部分，减去子公司或其他营业单位持有的现金和现金等价物后的净额。 |
| other_cash_to_invest_act | 支付其他与投资活动有关的现金(元) | 现金流量表科目。 |
| subtotal_invest_cash_outflow | 投资活动现金流出小计(元) | 购建固定资产、无形资产和其他长期资产支付的现金+投资支付的现金+取得子公司及其他营业单位支付的现金净额+支付其他与投资活动有关的现金。 |
| net_invest_cash_flow | 投资活动产生的现金流量净额(元) | 现金流量表科目。 |
| cash_from_invest | 吸收投资收到的现金(元) | 反映企业以发行股票、债券等方式筹集资金实际收到的款项，减去直接支付给金融企业的佣金、手续费、宣传费、咨询费、印刷费等发行费用后的净额。 |
| cash_from_mino_s_invest_sub | 子公司吸收少数股东投资收到的现金(元) | 《企业会计准则第33 号——合并财务报表》合并现金流量表科目。具体核算范围和方法参见上市公司定期报告。 |
| cash_from_borrowing | 取得借款收到的现金(元) | 反映企业举借各种短期、长期借款而收到的现金。 |
| cash_from_bonds_issue | 发行债券收到的现金(元) | 反映商业银行本期发行债券收到的本金。 |
| other_finance_act_cash | 收到其他与筹资活动有关的现金(元) | 反映企业除上述项目外，收到或支付的其他与筹资活动有关的现金流入或流出，包括以发行股票、债券等方式筹集资金而由企业直接支付的审计和咨询等费用、为购建固定资产而发生的借款利息资本化部分、融资租入固定资产所支付的租赁费、以分期付款方式购建固定资产以后各期支付的现金等。 |
| subtotal_finance_cash_inflow | 筹资活动现金流入小计(元) | 吸收投资收到的现金+取得借款收到的现金+收到其他与筹资活动有关的现金+发行债券收到的现金。 |
| borrowing_repayment | 偿还债务支付的现金(元) | 反映企业以现金偿还债务的本金。 |
| dividend_interest_payment | 分配股利、利润或偿付利息支付的现金(元) | 反映企业实际支付的现金股利、支付给其他投资单位的利润或用现金支付的借款利息、债券利息。 |
| proceeds_from_sub_to_mino_s | 子公司支付给少数股东的股利、利润(元) | 一般企业现金流量表科目。 |
| other_finance_act_payment | 支付其他与筹资活动有关的现金(元) | 包括：筹资费用所支付的现金，融资租赁所支付的现金，减少注册资本所支付的现金（收购本公司股票、退还联营单位的联营投资等）企业以分期付款方式构建固定资产除首期付款支付的现金以外的其他各期所支付的现金。 |
| subtotal_finance_cash_outflow | 筹资活动现金流出小计(元) | 现金流量表科目。 |
| net_finance_cash_flow | 筹资活动产生的现金流量净额(元) | 现金流量表科目。 |
| exchange_rate_change_effect | 汇率变动对现金及现金等价物的影响 | 指企业外币现金流量及境外子公司的现金流量折算成记账本位币时，所采用的是现金流量发生日的汇率或即期汇率的近似汇率。 |
| cash_equivalent_increase | 现金及现金等价物净增加额 | 中外币现金净增加额按期末汇率折算的金额。 |
| cash_equivalents_at_beginning | 期初现金及现金等价物余额(元) | 现金流量表科目。 |
| cash_and_equivalents_at_end | 期末现金及现金等价物余额(元) | 现金流量表科目。 |

#### 利润数据

按季度更新, 统计周期是一季度。可以使用get_fundamentals() 的statDate参数查询年度数据。

表名: income

| 列名 | 列的含义 | 解释 |
| --- | --- | --- |
| code | 股票代码 | 带后缀.XSHE/.XSHG |
| pubDate | 日期 | 公司发布财报日期 |
| statDate | 日期 | 财报统计的季度的最后一天, 比如2015-03-31, 2015-06-30 |
| total_operating_revenue | 营业总收入(元) | 具体核算范围和方法参见上市公司定期报告 |
| operating_revenue | 营业收入(元) | 具体核算范围和方法参见上市公司定期报告 |
| interest_income | 利息收入(元) | 利息收入是指纳税人购买各种债券等有价证券的利息，外单位欠款付给的利息以及其他利息收入。包括：购买各种债券等有价证券的利息，如购买国库券，重点企业建设债券、国家保值公债以及政府部门和企业发放的各类有价证券；企业各项存款所取得的利息外单位欠本企业款而取得的利息；其他利息收入等。 |
| premiums_earned | 已赚保费(元) | 已赚保费是指保险起期已经预先缴付的保险费,过去的保险期间的保费就成为已赚的保费。 |
| commission_income | 手续费及佣金收入(元) | 手续费及佣金收入是指公司为客户办理各种业务收取的手续费及佣金收入，包括办理咨询业务、担保业务、代保管等代理业务以及办理投资业务等取得的手续费及佣金，如业务代办手续费收入、咨询服务收入、担保收入、资产管理收入、代保管收入，代理买卖证券、代理承销证券、代理兑付证券、代理保管证券等代理业务以及其他相关服务实现的手续费及佣金收入等。 |
| total_operating_cost | 营业总成本(元) | 营业总成本=主营业务成本+其他业务成本+利息支出+手续费及佣金支出+退保金+赔付支出净额+提取保险合同准备金净额+保单红利支出+分保费用+营业税金及附加+销售费用+管理费用+财务费用+资产减值损失+其他 |
| operating_cost | 营业成本(元) | 营业成本，也称运营成本。是指企业所销售商品或者提供劳务的成本。营业成本应当与所销售商品或者所提供劳务而取得的收入进行配比。 |
| interest_expense | 利息支出(元) | 利息支出是指临时借款的利息支出。在以收付实现制作为记帐基础的前提条件下，所谓支出应以实际支付为标准，即资金流出，标志着现金、银行存款的减少。就利息支出而言、给个人帐户计息，其资金并没有流出，现金、银行存款并没有减少，因此，给个人计息不应作为利息支出列支。 |
| commission_expense | 手续费及佣金支出(元) | 手续费及佣金支出，本科目主要核算企业（金融）发生的与其经营活动相关的各项手续费、佣金等支出。 |
| refunded_premiums | 退保金(元) | 退保金是指公司经营的长期人身保险业务中，投保人办理退保时，按保险条款规定支付给投保人的金额。 |
| net_pay_insurance_claims | 赔付支出净额(元) | 赔付支出主要指核算企业（保险）支付的原保险合同赔付款项和再保险合同赔付款项。企业（保险）可以单独设置“赔款支出”、“满期给付”、“年金给付”、“死伤医疗给付”、“分保赔付支出”等科目。可按保险合同和险种进行明细核算。 |
| withdraw_insurance_contract_reserve | 提取保险合同准备金净额(元) | 保险准备金是指保险人为保证其如约履行保险赔偿或给付义务，根据政府有关法律规定或业务特定需要，从保费收入或盈余中提取的与其所承担的保险责任相对应的一定数量的基金。 |
| policy_dividend_payout | 保单红利支出(元) | 保单红利支出是根据原保险合同的约定，按照分红保险产品的红利分配方法及有关精算结果而估算，支付给保单持有人的红利。 |
| reinsurance_cost | 分保费用(元) | 分保费用，是办理初保业务的保险公司向其他保险公司分保保险业务，在向对方支付分保费的同时，向对方收取的一定费用，用以弥补初保人的费用支出。 |
| operating_tax_surcharges | 营业税金及附加(元) | 反映企业经营主要业务应负担的营业税、消费税、城市维护建设税、资源税和教育费附加等。填报此项指标时应注意，实行新税制后，会计上规定应交增值税不再计入“主营业务税金及附加”项，无论是一般纳税企业还是小规模纳税企业均应在“应交增值税明细表”中单独反映。根据企业会计“利润表”中对应指标的本年累计数填列。 |
| sale_expense | 销售费用(元) | 销售费用是指企业在销售产品、自制半成品和提供劳务等过程中发生的各项费用。包括由企业负担的包装费、运输费、广告费、装卸费、保险费、委托代销手续费、展览费、租赁费（不含融资租赁费)和销售服务费、销售部门人员工资、职工福利费、差旅费、折旧费、修理费、物料消耗、低值易耗品摊销以及其他经费等。与销售有关的差旅费应计入销售费用。 |
| administration_expense | 管理费用(元) | 管理费用是指 企业行政管理部门为组织和管理生产经营活动而发生的各项费用。管理费用属于期间费用，在发生的当期就计入当期的损失或是利益。 |
| financial_expense | 财务费用(元) | 财务费用指企业在生产经营过程中为筹集资金而发生的筹资费用。包括企业生产经营期间发生的利息支出（减利息收入）、汇兑损益（有的企业如商品流通企业、保险企业进行单独核算，不包括在财务费用）、金融机构手续费，企业发生的现金折扣或收到的现金折扣等。但在企业筹建期间发生的利息支出，应计入开办费；为购建或生产满足资本化条件的资产发生的应予以资本化的借款费用，在“在建工程”、“制造费用”等账户核算。 |
| asset_impairment_loss | 资产减值损失(元) | 资产减值损失是指因资产的账面价值高于其可收回金额而造成的损失。 新会计准则规定资产减值范围主要是固定资产、无形资产以及除特别规定外的其他资产减值的处理。《资产减值》准则改变了固定资产、无形资产等的减值准备计提后可以转回的做法，资产减值损失一经确认，在以后会期间不得转回，消除了一些企业通过计提秘密准备来调节利润的可能，限制了利润的人为波动。资产减值损失在会计核算中属于损益类科目。 |
| fair_value_variable_income | 公允价值变动收益(元) | “公允价值变动收益” 这个科目，是“以公允价值计量且其变动计入当期损益的交易性金融资产”的一个科目。在资产负债表日，“交易性金融资产”的公允价值高于其账面价值的差额，应借记“交易性金融资产－公允价值变动”，贷记“公允价值变动损益”，公允价值低于其账面价值的差额，则做相反的分录。 |
| investment_income | 投资收益(元) | 投资收益是对外投资所取得的利润、股利和债券利息等收入减去投资损失后的净收益。严格地讲，所谓投资收益是指以项目为边界的货币收入等。 |
| invest_income_associates | 对联营企业和合营企业的投资收益(元) | 持有的对联营企业及合营企业的投资，按照《企业会计准则第2号——长期股权投资》的规定，应当采用权益法核算，在按持股比例等计算确认应享有或应分担被投资单位的净损益时，应当考虑以下因素：投资企业与联营企业及合营企业之间发生的内部交易损益按照持股比例计算归属于投资企业的部分，应当予以抵销，在此基础上确认投资损益。
投资企业与被投资单位发生的内部交易损失，按照《企业会计准则第8号———资产减值》等规定属于资产减值损失的，应当全额确认。
投资企业对于纳入其合并范围的子公司与其联营企业及合营企业之间发生的内部交易损益，也应当按照上述原则进行抵销，在此基础上确认投资损益。
投资企业对于首次执行日之前已经持有的对联营企业及合营企业的长期股权投资，如存在与该投资相关的股权投资借方差额，还应扣除按原剩余期限直线摊销的股权投资借方差额，确认投资损益。
投资企业在被投资单位宣告发放现金股利或利润时，按照规定计算应分得的部分确认应收股利，同时冲减长期股权投资的账面价值。 |
| exchange_income | 汇兑收益(元) | 汇兑收益，是指用记账本位币，按照不同的汇率报告相同数量的外币而产生的差额。简单地说，就是公司的外币货币性项目和非货币性项目因汇率变动，在折算成本币时造成损益。而这部分汇兑差额作为财务费用，计入当期损益，从而影响公司利润。 |
| operating_profit | 营业利润(元) | 营业利润是企业最基本经营活动的成果，也是企业一定时期获得利润中最主要、最稳定的来源。2006年财政部颁布的新企业会计准则-30号财务报表列报中已对营业利润进行了调整，将投资收益调入营业利润，同时取消了主营业务利润和其他业务利润的提法，补贴收入被并入营业外收入，营业利润减营业外收支调整即得到利润总额。 |
| non_operating_revenue | 营业外收入(元) | 营业外收入是指企业确认与企业生产经营活动没有直接关系的各种收入。 |
| non_operating_expense | 营业外支出(元) | 营业外支出是企业发生的与其日常活动无直接关系的各项损失，主要包括非流动资产处置损失、公益性捐赠支出、盘亏损失、非常损失、罚款支出等。 |
| disposal_loss_non_current_liability | 非流动资产处置净损失(元) | “非流动资产处置损失”属于损益类的科目，在编制利润表时这些科目如果有本期发生额，要填在利润表中。“非流动资产处置损失”是营业外支出的明细科目，在损益表中计入“营业外支出”，“营业外支出”下方会单独列示“非流动资产处置损失”，但是包括在“营业外支出”项目中。 |
| total_profit | 利润总额(元) | 利润总额指企业在生产经营过程中各种收入扣除各种耗费后的盈余，反映企业在报告期内实现的盈亏总额。 |
| income_tax_expense | 所得税费用(元) | 所得税费用是指企业经营利润应交纳的所得税。“所得税费用”，核算企业负担的所得税，是损益类科目；这一般不等于当期应交所得税，因为可能存在“暂时性差异”。如果只有永久性差异，则等于当期应交所得税。 |
| net_profit | 净利润(元) | 净利润（收益）是指在利润总额中按规定交纳了所得税后公司的利润留成，一般也称为税后利润或净利润。净利润的计算公式为：净利润=利润总额-所得税费用.净利润是一个企业经营的最终成果，净利润多，企业的经营效益就好；净利润少，企业的经营效益就差，它是衡量一个企业经营效益的主要指标。 |
| np_parent_company_owners | 归属于母公司股东的净利润(元) | 准确来讲应称之为“归属于上市公司股东的净利润”，这是因为净利润都归属于股东，只是在合并报表中的净利润有一部分是归属于子公司的其它股东的，这些子公司的其它股东也依法按比例享有子公司的净利润。 |
| minority_profit | 少数股东损益(元) | 少数股东损益是一个流量概念，是指公司合并报表的子公司其它非控股股东享有的损益，需要在利润表中予以扣除。利润表的“净利润”项下可以分“归属于母公司所有者的净利润”和“少数股东损益”。其对应的存量概念是“少数股东权益”。 |
| basic_eps | 基本每股收益(元) | 理论算法：归属于普通股股东的当期净利润/(当期实际发行在外的普通股加权平均数=∑(发行在外普通股股数×发行在外月份数)／12) |
| diluted_eps | 稀释每股收益(元) | 理论算法：归属于普通股股东的当期净利润(扣除当期已确认为费用的稀释性潜在普通股的利息、稀释性潜在普通股转换时将产生的收益或费用、相关所得税的影响)/假设稀释性潜在普通股于当期期初(或发行日)已经全部转换为普通股，于此计算的普通股股数的加权平均数。 |
| other_composite_income | 其他综合收益(元) | 其他综合收益是指企业根据企业会计准则规定未在损益中确认的各项利得和损失扣除所得税影响后的净额。企业在计算利润表中的其他综合收益时，应当扣除所得税影响；在计算合并利润表中的其他综合收益时，除了扣除所得税影响以外，还需要分别计算归属于母公司所有者的其他综合收益和归属于少数股东的其他综合收益。 |
| total_composite_income | 综合收益总额(元) | 综合收益总额项目，反映企业净利润与其他综合收益的合计金额。综合收益，包括其他综合收益和综合收益总额。其中，其他综合收益反映企业根据企业会计准则规定未在损益中确认的各项利得和损失扣除所得税影响后的净额；综合收益总额是企业净利润与其他综合收益的合计金额。 |
| ci_parent_company_owners | 归属于母公司所有者的综合收益总额(元) | 综合收益是指除所有者的出资额和各种为第三方或客户代收的款项以外的各种收入。根据美国财务会计准则委员会（FASB）1980年在第3号财务会计概念公告(SFAC3）（企业财务报表的要素）（后为1985年发布的SFAC6所取代）的解释，综合收益是指“一个主体在某一期间与非业主方面进行交易或发生其他事项和情况所引起的权益（净资产）变动。它包括这一期间内除业主投资和派给业主款外，一切权益上的变动。” |
| ci_minority_owners | 归属于少数股东的综合收益总额(元) | 综合收益是指除所有者的出资额和各种为第三方或客户代收的款项以外的各种收入。根据美国财务会计准则委员会（FASB）1980年在第3号财务会计概念公告(SFAC3）（企业财务报表的要素）（后为1985年发布的SFAC6所取代）的解释，综合收益是指“一个主体在某一期间与非业主方面进行交易或发生其他事项和情况所引起的权益（净资产）变动。它包括这一期间内除业主投资和派给业主款外，一切权益上的变动。” |

#### 财务指标数据

按季度更新, 统计周期是一季度。可以使用get_fundamentals() 的statDate参数查询年度数据。

表名: indicator

| 列名 | 列的含义 | 解释 |
| --- | --- | --- |
| code | 股票代码 | 带后缀.XSHE/.XSHG |
| pubDate | 日期 | 公司发布财报日期 |
| statDate | 日期 | 财报统计的季度的最后一天, 比如2015-03-31, 2015-06-30 |
| eps | 每股收益EPS(元) | 每股收益(摊薄)＝净利润/期末股本；分子从单季利润表取值，分母取季度末报告期股本值；净利润指归属于母公司股东的净利润(元) |
| adjusted_profit | 扣除非经常损益后的净利润(元) | 非经常性损益这一概念是证监会在1999年首次提出的，当时将其定义为：公司正常经营损益之外的一次性或偶发性损益。《问答第1号》则指出：非经常性损益是公司发生的与经营业务无直接关系的收支；以及虽与经营业务相关，但由于其性质、金额或发生频率等方面的原因，影响了真实公允地反映公司正常盈利能力的各项收入。 |
| operating_profit | 经营活动净收益(元) | 营业总收入-营业总成本 |
| value_change_profit | 价值变动净收益(元) | 公允价值变动净收益+投资净收益+汇兑净收益 |
| roe | 净资产收益率ROE(%) | 归属于母公司股东的净利润*2/（期初归属于母公司股东的净资产+期末归属于母公司股东的净资产） |
| inc_return | 净资产收益率(扣除非经常损益)(%) | 扣除非经常损益后的净利润（不含少数股东损益）*2/（期初归属于母公司股东的净资产+期末归属于母公司股东的净资产） |
| roa | 总资产净利率ROA(%) | 净利润*2/（期初总资产+期末总资产） |
| net_profit_margin | 销售净利率(%) | 净利润/营业收入 |
| gross_profit_margin | 销售毛利率(%) | 毛利/营业收入 |
| expense_to_total_revenue | 营业总成本/营业总收入(%) | 营业总成本/营业总收入(%) |
| operation_profit_to_total_revenue | 营业利润/营业总收入(%) | 营业利润/营业总收入(%) |
| net_profit_to_total_revenue | 净利润/营业总收入(%) | 净利润/营业总收入(%) |
| operating_expense_to_total_revenue | 营业费用/营业总收入(%) | 营业费用/营业总收入(%) |
| ga_expense_to_total_revenue | 管理费用/营业总收入(%) | 管理费用/营业总收入(%) |
| financing_expense_to_total_revenue | 财务费用/营业总收入(%) | 财务费用/营业总收入(%) |
| operating_profit_to_profit | 经营活动净收益/利润总额(%) | 经营活动净收益/利润总额(%) |
| invesment_profit_to_profit | 价值变动净收益/利润总额(%) | 价值变动净收益/利润总额(%) |
| adjusted_profit_to_profit | 扣除非经常损益后的净利润/净利润(%) | 扣除非经常损益后的净利润/净利润(%) |
| goods_sale_and_service_to_revenue | 销售商品提供劳务收到的现金/营业收入(%) | 销售商品提供劳务收到的现金/营业收入(%) |
| ocf_to_revenue | 经营活动产生的现金流量净额/营业收入(%) | 经营活动产生的现金流量净额/营业收入(%) |
| ocf_to_operating_profit | 经营活动产生的现金流量净额/经营活动净收益(%) | 经营活动产生的现金流量净额/经营活动净收益(%) |
| inc_total_revenue_year_on_year | 营业总收入同比增长率(%) | 营业总收入同比增长率是企业在一定期间内取得的营业总收入与其上年同期营业总收入的增长的百分比，以反映企业在此期间内营业总收入的增长或下降等情况。 |
| inc_total_revenue_annual | 营业总收入环比增长率(%) | 营业收入是指企业在从事销售商品，提供劳务和让渡资产使用权等日常经营业务过程中所形成的经济利益的总流入。环比增长率=（本期的某个指标的值-上一期这个指标的值）/上一期这个指标的值*100%。 |
| inc_revenue_year_on_year | 营业收入同比增长率(%) | 营业收入,是指公司在从事销售商品、提供劳务和让渡资产使用权等日常经营业务过程中所形成的经济利益的总流入，而营业收入同比增长率，则是检验上市公司去年一年挣钱能力是否提高的标准，营业收入同比增长,说明公司在上一年度挣钱的能力加强了，营业收入同比下降，则说明公司的挣钱能力稍逊于往年。 |
| inc_revenue_annual | 营业收入环比增长率(%) | 环比增长率=（本期的某个指标的值-上一期这个指标的值）/上一期这个指标的值*100%。 |
| inc_operation_profit_year_on_year | 营业利润同比增长率(%) | 同比增长率就是指公司当年期的营业利润和上月同期、上年同期的营业利润比较。（当期的营业利润-上月（上年）当期的营业利润）/上月（上年）当期的营业利润绝对值=利润同比增长率。 |
| inc_operation_profit_annual | 营业利润环比增长率(%) | 环比增长率=（本期的某个指标的值-上一期这个指标的值）/上一期这个指标的值*100%。 |
| inc_net_profit_year_on_year | 净利润同比增长率(%) | （当期的净利润-上月（上年）当期的净利润）/上月（上年）当期的净利润绝对值=净利润同比增长率。 |
| inc_net_profit_annual | 净利润环比增长率(%) | 环比增长率=（本期的某个指标的值-上一期这个指标的值）/上一期这个指标的值*100%。 |
| inc_net_profit_to_shareholders_year_on_year | 归属母公司股东的净利润同比增长率(%) | 归属于母公司股东净利润是指全部归属于母公司股东的净利润，包括母公司实现的净利润和下属子公司实现的净利润；同比增长率，一般是指和去年同期相比较的增长率。同比增长 和上一时期、上一年度或历史相比的增长（幅度）。 |
| inc_net_profit_to_shareholders_annual | 归属母公司股东的净利润环比增长率(%) | 环比增长率=（本期的某个指标的值-上一期这个指标的值）/上一期这个指标的值*100%。 |

## 获取报告期财务数据

报告期财务数据是上市公司定期公告中按照报告期统计的财务数据，使用run_query()方法进行查询，各类型报表的使用方法如下。
报告期的数据单位为元

### 审计意见(新上线数据)

```python
from jqdata import finance
finance.run_query(query(finance.STK_AUDIT_OPINION).filter(finance.STK_AUDIT_OPINION.code==code).limit(n))
```

获取上市公司定期报告及审计报告中出具的审计意见

**参数：**

- **query(finance.STK_AUDIT_OPINION)**：表示从finance.STK_AUDIT_OPINION这张表中查询上市公司审计意见的所有字段信息，还可以指定所要查询的字段名，格式如下：query(库名.表名.字段名1，库名.表名.字段名2），多个字段用逗号分隔进行提取；query函数的更多用法详见：[sqlalchemy.orm.query.Query对象](http://docs.sqlalchemy.org/en/rel_1_0/orm/query.html)
    
- 表结构和字段信息如下：
    

| 字段 | 名称 | 类型 | 注释 |
| --- | --- | --- | --- |
| pub_date | 公告日期 | DATE |  |
| end_date | 报告日期 | DATE |  |
| report_type | 审计报告类型 | TINYINT(4) | 0(财务报表审计报告), 1(内部控制审计报告) |
| accounting_firm | 会计师事务所 | VARCHAR(100) |  |
| accountant | 会计师 | VARCHAR(100) |  |
| opinion_type_id | 审计意见类型id | INTEGER(11) |  |
| opinion_type | 审计意见类型 | VARCHAR(20) |  |

**审计意见类型编码**

| 审计意见类型编码 | 审计意见类型 |
| --- | --- |
| 1 | 无保留 |
| 2 | 无保留带解释性说明 |
| 3 | 保留意见 |
| 4 | 拒绝/无法表示意见 |
| 5 | 否定意见 |
| 6 | 未经审计 |
| 7 | 保留带解释性说明 |
| 10 | 经审计（不确定具体意见类型） |
| 11 | 无保留带持续经营重大不确定性 |

- **filter(finance.STK_AUDIT_OPINION.code==code)**：指定筛选条件，通过finance.STK_AUDIT_OPINION.code==code可以指定你想要查询的股票代码；除此之外，还可以对表中其他字段指定筛选条件，如finance.STK_AUDIT_OPINION.pub_date>='2015-01-01'，表示公告日期在2015年1月1日之后发布的数据；多个筛选条件用英文逗号分隔。
    
- **limit(n)**：限制返回的数据条数，n指定返回条数。
    

**返回结果：**

- 返回一个 dataframe，每一行对应数据表中的一条数据， 列索引是你所查询的字段名称

**注意：**

1.  **为了防止返回数据量过大, 我们每次最多返回4000行**
2.  不能进行连表查询，即同时查询多张表的数据

**示例：**

```python
#查询贵州茅台2015年之后公布的审计意见信息，限定返回条数为10条
from jqdata import finance
q=query(finance.STK_AUDIT_OPINION).filter(finance.STK_AUDIT_OPINION.code=='600519.XSHG',finance.STK_AUDIT_OPINION.pub_date>='2015-01-01').limit(10)
df=finance.run_query(q)
print(df)

      id         code    pub_date    end_date  report_type   accounting_firm  \
0  91458  600519.XSHG  2015-04-21  2014-12-31            0  立信会计师事务所(特殊普通合伙)
1  91459  600519.XSHG  2015-04-21  2015-03-31            0              None
2  91460  600519.XSHG  2015-08-28  2015-06-30            0              None
3  91461  600519.XSHG  2015-10-23  2015-09-30            0              None
4  91462  600519.XSHG  2016-03-24  2015-12-31            0  立信会计师事务所(特殊普通合伙)
5  91463  600519.XSHG  2016-04-21  2016-03-31            0              None
6  91464  600519.XSHG  2016-08-27  2016-06-30            0              None
7  91465  600519.XSHG  2016-10-29  2016-09-30            0              None
8  91466  600519.XSHG  2017-04-15  2016-12-31            0  立信会计师事务所(特殊普通合伙)
9  91467  600519.XSHG  2017-04-15  2016-12-31            1  立信会计师事务所(特殊普通合伙)

  accountant  opinion_type_id opinion_type
0      杨雄、江山                1          无保留
1       None                6         未经审计
2       None                6         未经审计
3       None                6         未经审计
4     江山、王晓明                1          无保留
5       None                6         未经审计
6       None                6         未经审计
7       None                6         未经审计
8     江山、王晓明                1          无保留
9     江山、王晓明                1          无保留
```

### 定期报告预约披露时间表(新上线数据)

```python
from jqdata import finance
finance.run_query(query(finance.STK_REPORT_DISCLOSURE).filter(finance.STK_REPORT_DISCLOSURE.code==code).limit(n))
```

获取上市公司定期报告预约披露及实际披露日期

**参数：**

- **query(finance.STK_REPORT_DISCLOSURE)**：表示从finance.STK_REPORT_DISCLOSURE这张表中查询所有字段信息，还可以指定所要查询的字段名，格式如下：query(库名.表名.字段名1，库名.表名.字段名2），多个字段用逗号分隔进行提取；query函数的更多用法详见：[sqlalchemy.orm.query.Query对象](http://docs.sqlalchemy.org/en/rel_1_0/orm/query.html)
    
- 表结构和字段信息如下：
    

| 字段 | 名称 | 类型 | 注释 |
| --- | --- | --- | --- |
| code | 公司代码 | VARCHAR(12) |  |
| end_date | 截止日期 | DATE |  |
| appoint_date | 预约披露日 | DATE |  |
| first_date | 首次变更日 | DATE |  |
| second_date | 二次变更日 | DATE |  |
| third_date | 三次变更日 | DATE |  |
| pub_date | 实际披露日 | DATE |  |

- **filter(finance.STK_REPORT_DISCLOSURE.code==code)**：指定筛选条件，通过finance.STK_REPORT_DISCLOSURE.code==code可以指定你想要查询的股票代码；除此之外，还可以对表中其他字段指定筛选条件，如finance.STK_REPORT_DISCLOSURE.pub_date>='2015-01-01'，表示公告日期在2015年1月1日之后发布的数据；多个筛选条件用英文逗号分隔。
    
- **limit(n)**：限制返回的数据条数，n指定返回条数。
    

**返回结果：**

- 返回一个 dataframe，每一行对应数据表中的一条数据， 列索引是你所查询的字段名称

**注意：**

1.  **为了防止返回数据量过大, 我们每次最多返回4000行**
2.  不能进行连表查询，即同时查询多张表的数据

**示例：**

```python
#查询贵州茅台2019年之后的数据，限定返回条数为10条
from jqdata import finance
q=query(finance.STK_REPORT_DISCLOSURE).filter(finance.STK_REPORT_DISCLOSURE.code=='600519.XSHG',
                                              finance.STK_REPORT_DISCLOSURE.end_date>='2019-01-01').limit(10)
df=finance.run_query(q)
print(df)

       id         code    end_date appoint_date  first_date second_date  \
0  143825  600519.XSHG  2019-03-31   2019-04-25        None        None
1  140169  600519.XSHG  2019-06-30   2019-08-08  2019-07-18        None
2  136468  600519.XSHG  2019-09-30   2019-10-16        None        None
3  132661  600519.XSHG  2019-12-31   2020-03-25  2020-04-22        None
4  159688  600519.XSHG  2020-03-31   2020-04-28        None        None
5  155757  600519.XSHG  2020-06-30   2020-07-29        None        None
6  151704  600519.XSHG  2020-09-30   2020-10-26        None        None
7  147459  600519.XSHG  2020-12-31   2021-03-31        None        None
8  177187  600519.XSHG  2021-03-31   2021-04-28        None        None
9  172783  600519.XSHG  2021-06-30   2021-07-31        None        None

  third_date    pub_date
0       None  2019-04-25
1       None  2019-07-18
2       None  2019-10-16
3       None  2020-04-22
4       None  2020-04-28
5       None  2020-07-29
6       None  2020-10-26
7       None  2021-03-31
8       None  2021-04-28
9       None  2021-07-31
```

### 业绩预告

```python
from jqdata import finance
finance.run_query(query(finance.STK_FIN_FORCAST).filter(finance.STK_FIN_FORCAST.code==code).limit(n))
```

获取上市公司业绩预告等信息

**参数：**

- **query(finance.STK_FIN_FORCAST)**：表示从finance.STK_FIN_FORCAST这张表中查询上市公司业绩报告的字段信息，还可以指定所要查询的字段名，格式如下：query(库名.表名.字段名1，库名.表名.字段名2），多个字段用逗号分隔进行提取；query函数的更多用法详见：[sqlalchemy.orm.query.Query对象](http://docs.sqlalchemy.org/en/rel_1_0/orm/query.html)
    
- 以下"净利润" 一般披露为归母净利润
    
- **finance.STK_FIN_FORCAST**：代表上市公司业绩预告表，收录了上市公司的业绩预告信息，表结构和字段信息如下：
    
    | 字段 | 名称 | 类型 | 注释 |
    | --- | --- | --- | --- |
    | company_id | 公司ID | int |  |
    | code | 股票代码 | varchar(12) |  |
    | name | 公司名称 | varchar(64) |  |
    | end_date | 报告期 | date |  |
    | report_type_id | 预告期类型编码 | int | 如下 [预告期类型编码](#type1) |
    | report_type | 预告期类型 | varchar(32) |  |
    | pub_date | 公布日期 | date |  |
    | type_id | 预告类型编码 | int | 如下 [业绩类型编码](#type2) |
    | type | 预告类型 | varchar(32) |  |
    | profit_min | 预告净利润（下限） | decimal(22,6) |  |
    | profit_max | 预告净利润（上限） | decimal(22,6) |  |
    | profit_last | 去年同期净利润 | decimal(22,6) |  |
    | profit_ratio_min | 预告净利润变动幅度(下限) | decimal(10,4) | 单位：% |
    | profit_ratio_max | 预告净利润变动幅度(上限) | decimal(10,4) | 单位：% |
    | content | 预告内容 | varchar(2048) |  |
    
    **预告期类型编码**
    
    | 预告期编码 | 预告期类型 |
    | --- | --- |
    | 304001 | 一季度预告 |
    | 304002 | 中报预告 |
    | 304003 | 三季度预告 |
    | 304004 | 四季度预告 |
    
    **业绩类型编码**
    
    | 业绩类型编码 | 业绩类型 |
    | --- | --- |
    | 305001 | 业绩大幅上升(50%以上) |
    | 305002 | 业绩预增 |
    | 305003 | 业绩预盈 |
    | 305004 | 预计扭亏 |
    | 305005 | 业绩持平 |
    | 305006 | 无大幅变动 |
    | 305007 | 业绩预亏 |
    | 305008 | 业绩大幅下降(50%以上) |
    | 305009 | 大幅减亏 |
    | 305010 | 业绩预降 |
    | 305011 | 预计减亏 |
    | 305012 | 不确定 |
    | 305013 | 取消预测 |
    
- **filter(finance.STK_FIN_FORCAST.code==code)**：指定筛选条件，通过finance.STK_FIN_FORCAST.code==code可以指定你想要查询的股票代码；除此之外，还可以对表中其他字段指定筛选条件，如finance.STK_FIN_FORCAST.pub_date>='2015-01-01'，表示公告日期在2015年1月1日之后发布的业绩预告；多个筛选条件用英文逗号分隔。
    
- **limit(n)**：限制返回的数据条数，n指定返回条数。
    

**返回结果：**

- 返回一个 dataframe，每一行对应数据表中的一条数据， 列索引是你所查询的字段名称

**注意：**

1.  **为了防止返回数据量过大, 我们每次最多返回4000行**
2.  不能进行连表查询，即同时查询多张表的数据

**示例：**

```python
#查询贵州茅台2015年之后公布的业绩预告信息，限定返回条数为10条
from jqdata import finance
q=query(finance.STK_FIN_FORCAST).filter(finance.STK_FIN_FORCAST.code=='600519.XSHG',finance.STK_FIN_FORCAST.pub_date>='2015-01-01').limit(10)
df=finance.run_query(q)
print(df)

       id  company_id         code         name           end_date  report_type_id  \
0  138256   420600519  600519.XSHG  贵州茅台酒股份有限公司  2017-12-31          304004

     report_type    pub_date  type_id    type      profit_min profit_max  \
0       四季度预告  2018-01-31   305001  业绩大幅上升       None       None

    profit_last  profit_ratio_min  profit_ratio_max  \
0  1.671836e+10                58                58

                                     content
0  预计公司2017年01-12月归属于上市公司股东的净利润与上年同期相比增长58%。
```

### 业绩快报(新上线数据)

```python
from jqdata import finance
finance.run_query(query(finance.STK_PERFORMANCE_LETTERS).filter(finance.STK_PERFORMANCE_LETTERS.code==code).limit(n))
```

获取上市公司业绩快报信息

**参数：**

- **query(finance.STK_PERFORMANCE_LETTERS)**：表示从finance.STK_PERFORMANCE_LETTERS这张表中查询上市公司业绩报告的字段信息，还可以指定所要查询的字段名，格式如下：query(库名.表名.字段名1，库名.表名.字段名2），多个字段用逗号分隔进行提取；query函数的更多用法详见：[sqlalchemy.orm.query.Query对象](http://docs.sqlalchemy.org/en/rel_1_0/orm/query.html)
    
- **finance.STK_PERFORMANCE_LETTERS**：代表上市公司业绩预告表，收录了上市公司的业绩预告信息，表结构和字段信息如下：
    

| 字段 | 名称 | 类型 | 注释 |
| --- | --- | --- | --- |
| company_id | 机构ID | INTEGER(11) |  |
| company_name | 公司名称 | VARCHAR(100) |  |
| code | 股票代码 | VARCHAR(12) |  |
| name | 股票简称 | VARCHAR(12) |  |
| pub_date | 公布日期 | DATE |  |
| start_date | 开始日期 | DATE |  |
| end_date | 截至日期 | DATE |  |
| report_date | 报告期 | DATE |  |
| report_type | 报告期类型 | int | 0：本期，1：上期 |
| total_operating_revenue | 营业总收入 | DECIMAL(20, 4) |  |
| operating_revenue | 营业收入 | DECIMAL(20, 4) |  |
| operating_profit | 营业利润 | DECIMAL(20, 4) |  |
| total_profit | 利润总额 | DECIMAL(20, 4) |  |
| np_parent_company_owners | 归属于母公司所有者的净利润 | DECIMAL(20, 4) |  |
| total_assets | 总资产 | DECIMAL(20, 4) |  |
| equities_parent_company_owners | 归属于上市公司股东的所有者权益 | DECIMAL(20, 4) |  |
| basic_eps | 基本每股收益 | DECIMAL(20, 4) |  |
| weight_roe | 净资产收益(加权) | DECIMAL(20, 4) | 披露值 |

- **filter(finance.STK_PERFORMANCE_LETTERS.code==code)**：指定筛选条件，通过finance.STK_PERFORMANCE_LETTERS.code==code可以指定你想要查询的股票代码；除此之外，还可以对表中其他字段指定筛选条件，如finance.STK_PERFORMANCE_LETTERS.pub_date>='2015-01-01'，表示公告日期在2015年1月1日之后发布的业绩快报；多个筛选条件用英文逗号分隔。
    
- **limit(n)**：限制返回的数据条数，n指定返回条数。
    

**返回结果：**

- 返回一个 dataframe，每一行对应数据表中的一条数据， 列索引是你所查询的字段名称

**注意：**

1.  **为了防止返回数据量过大, 我们每次最多返回4000行**
2.  不能进行连表查询，即同时查询多张表的数据

**示例：**

```python
from jqdata import *
a=finance.run_query(query(finance.STK_PERFORMANCE_LETTERS).filter(finance.STK_PERFORMANCE_LETTERS.code=='000001.XSHE').limit(3))
print(a)

   id  company_id company_name         code  name    pub_date  start_date  \
0   1   430000001   平安银行股份有限公司  000001.XSHE  平安银行  2019-01-04  2018-01-01
1   2   430000001   平安银行股份有限公司  000001.XSHE  平安银行  2019-01-04  2017-01-01
2   3   430000001   平安银行股份有限公司  000001.XSHE  平安银行  2020-01-14  2019-01-01

     end_date report_date  report_type total_operating_revenue  \
0  2018-12-31  2018-12-31            0                    None
1  2017-12-31  2018-12-31            1                    None
2  2019-12-31  2019-12-31            0                    None

   operating_revenue  operating_profit  total_profit  \
0       1.167160e+11      3.230500e+10  3.223100e+10
1       1.057860e+11      3.022300e+10  3.015700e+10
2       1.379580e+11      3.628900e+10  3.624000e+10

   np_parent_company_owners  total_assets  equities_parent_company_owners  \
0              2.481800e+10  3.420753e+12                             NaN
1              2.318900e+10  3.248474e+12                             NaN
2              2.819500e+10  3.939070e+12                    3.129830e+11

   basic_eps  weight_roe
0        NaN       11.49
1        NaN       11.62
2    16.1282       11.30
```

### 合并利润表

```
from jqdata import finance
finance.run_query(query(finance.STK_INCOME_STATEMENT).filter(finance.STK_INCOME_STATEMENT.code==code).limit(n))
```

获取上市公司定期公告中公布的合并利润表数据（2007版）

**参数：**

- **query(finance.STK_INCOME_STATEMENT)**：表示从finance.STK_INCOME_STATEMENT这张表中查询上市公司定期公告中公布的合并利润表信息，还可以指定所要查询的字段名，格式如下：query(库名.表名.字段名1，库名.表名.字段名2），多个字段用逗号分隔进行提取；query函数的更多用法详见：[sqlalchemy.orm.query.Query对象](http://docs.sqlalchemy.org/en/rel_1_0/orm/query.html)
    
- **finance.STK_INCOME_STATEMENT**：代表上市公司合并利润表，收录了上市公司定期公告中公布的合并利润表数据，表结构和字段信息如下：
    
    | 字段名称 | 中文名称 | 字段类型 | 含义 |
    | --- | --- | --- | --- |
    | company_id | 公司ID | int |  |
    | company_name | 公司名称 | varchar(100) |  |
    | code | 股票代码 | varchar(12) |  |
    | a_code | A股代码 | varchar(12) |  |
    | b_code | B股代码 | varchar(12) |  |
    | h_code | H股代码 | varchar(12) |  |
    | pub_date | 公告日期 | date |  |
    | start_date | 开始日期 | date |  |
    | end_date | 截止日期 | date |  |
    | report_date | 报告期 | date |  |
    | report_type | 报告期类型 | int | 0：本期，1：上期 |
    | source_id | 报表来源编码 | int | 如下 [报表来源编码](#source1) |
    | source | 报表来源 | varchar(60) | 选择时程序自动填入 |
    | total_operating_revenue | 营业总收入 | decimal(20,4) |  |
    | operating_revenue | 营业收入 | decimal(20,4) |  |
    | total_operating_cost | 营业总成本 | decimal(20,4) |  |
    | operating_cost | 营业成本 | decimal(20,4) |  |
    | operating_tax_surcharges | 营业税金及附加 | decimal(20,4) |  |
    | sale_expense | 销售费用 | decimal(20,4) |  |
    | administration_expense | 管理费用 | decimal(20,4) |  |
    | exploration_expense | 堪探费用 | decimal(20,4) | 勘探费用用于核算企业（石油天然气开采）核算的油气勘探过程中发生的地质调查、物理化学勘探各项支出和非成功探井等支出。 |
    | financial_expense | 财务费用 | decimal(20,4) |  |
    | asset_impairment_loss | 资产减值损失 | decimal(20,4) |  |
    | fair_value_variable_income | 公允价值变动净收益 | decimal(20,4) |  |
    | investment_income | 投资收益 | decimal(20,4) |  |
    | invest_income_associates | 对联营企业和合营企业的投资收益 | decimal(20,4) |  |
    | exchange_income | 汇兑收益 | decimal(20,4) |  |
    | other_items_influenced_income | 影响营业利润的其他科目 | decimal(20,4) |  |
    | operating_profit | 营业利润 | decimal(20,4) |  |
    | subsidy_income | 补贴收入 | decimal(20,4) |  |
    | non_operating_revenue | 营业外收入 | decimal(20,4) |  |
    | non_operating_expense | 营业外支出 | decimal(20,4) |  |
    | disposal_loss_non_current_liability | 非流动资产处置净损失 | decimal(20,4) |  |
    | other_items_influenced_profit | 影响利润总额的其他科目 | decimal(20,4) |  |
    | total_profit | 利润总额 | decimal(20,4) |  |
    | income_tax | 所得税 | decimal(20,4) |  |
    | other_items_influenced_net_profit | 影响净利润的其他科目 | decimal(20,4) |  |
    | net_profit | 净利润 | decimal(20,4) |  |
    | np_parent_company_owners | 归属于母公司所有者的净利润 | decimal(20,4) |  |
    | minority_profit | 少数股东损益 | decimal(20,4) |  |
    | eps | 每股收益 | decimal(20,4) |  |
    | basic_eps | 基本每股收益 | decimal(20,4) |  |
    | diluted_eps | 稀释每股收益 | decimal(20,4) |  |
    | other_composite_income | 其他综合收益 | decimal(20,4) |  |
    | total_composite_income | 综合收益总额 | decimal(20,4) |  |
    | ci_parent_company_owners | 归属于母公司所有者的综合收益总额 | decimal(20,4) |  |
    | ci_minority_owners | 归属于少数股东的综合收益总额 | decimal(20,4) |  |
    | interest_income | 利息收入 | decimal(20,4) |  |
    | premiums_earned | 已赚保费 | decimal(20,4) |  |
    | commission_income | 手续费及佣金收入 | decimal(20,4) |  |
    | interest_expense | 利息支出 | decimal(20,4) |  |
    | commission_expense | 手续费及佣金支出 | decimal(20,4) |  |
    | refunded_premiums | 退保金 | decimal(20,4) |  |
    | net_pay_insurance_claims | 赔付支出净额 | decimal(20,4) |  |
    | withdraw_insurance_contract_reserve | 提取保险合同准备金净额 | decimal(20,4) |  |
    | policy_dividend_payout | 保单红利支出 | decimal(20,4) |  |
    | reinsurance_cost | 分保费用 | decimal(20,4) |  |
    | non_current_asset_disposed | 非流动资产处置利得 | decimal(20,4) |  |
    | other_earnings | 其他收益 | decimal(20,4) |  |
    | asset_deal_income | 资产处置收益 | decimal(20,4) |  |
    | sust_operate_net_profit | 持续经营净利润 | decimal(20,4) |  |
    | discon_operate_net_profit | 终止经营净利润 | decimal(20,4) |  |
    | credit_impairment_loss | 信用减值损失 | decimal(20,4) |  |
    | net_open_hedge_income | 净敞口套期收益 | decimal(20,4) |  |
    | interest_cost_fin | 财务费用-利息费用 | decimal(20,4) |  |
    | interest_income_fin | 财务费用-利息收入 | decimal(20,4) |  |
    | rd_expenses | 研发费用 | decimal(20,4) |  |
    
    **报表来源编码**
    
    | 编码 | 名称 |
    | --- | --- |
    | 321001 | 招募说明书 |
    | 321002 | 上市公告书 |
    | 321003 | 定期报告 |
    | 321004 | 预披露公告 |
    | 321005 | 换股报告书 |
    | 321099 | 其他 |
    
- **filter(finance.STK_INCOME_STATEMENT.code==code)**：指定筛选条件，通过finance.STK_INCOME_STATEMENT.code==code可以指定你想要查询的股票代码；除此之外，还可以对表中其他字段指定筛选条件，如finance.STK_INCOME_STATEMENT.pub_date>='2015-01-01'，表示公告日期大于2015年1月1日上市公司公布的合并利润表信息；多个筛选条件用英文逗号分隔。
    
- **limit(n)**：限制返回的数据条数，n指定返回条数。
    

**返回结果：**

- 返回一个 dataframe，每一行对应数据表中的一条数据， 列索引是你所查询的字段名称

**注意：**

1.  **为了防止返回数据量过大, 我们每次最多返回4000行**
2.  不能进行连表查询，即同时查询多张表的数据

**示例：**

```python
#查询贵州茅台2015年之后公告的合并利润表数据，取出合并利润表中本期的营业总收入，归属于母公司的净利润
from jqdata import finance
q=query(finance.STK_INCOME_STATEMENT.company_name,
        finance.STK_INCOME_STATEMENT.code,
        finance.STK_INCOME_STATEMENT.pub_date,
        finance.STK_INCOME_STATEMENT.start_date,
        finance.STK_INCOME_STATEMENT.end_date,
        finance.STK_INCOME_STATEMENT.total_operating_revenue,
finance.STK_INCOME_STATEMENT.np_parent_company_owners).filter(finance.STK_INCOME_STATEMENT.code=='600519.XSHG',finance.STK_INCOME_STATEMENT.pub_date>='2015-01-01',finance.STK_INCOME_STATEMENT.report_type==0).limit(20)
df=finance.run_query(q)
print(df)

   company_name         code    pub_date  start_date    end_date  \
0   贵州茅台酒股份有限公司  600519.XSHG  2015-04-21  2014-01-01  2014-12-31
1   贵州茅台酒股份有限公司  600519.XSHG  2015-04-21  2015-01-01  2015-03-31
2   贵州茅台酒股份有限公司  600519.XSHG  2015-08-28  2015-01-01  2015-06-30
3   贵州茅台酒股份有限公司  600519.XSHG  2015-10-23  2015-01-01  2015-09-30
4   贵州茅台酒股份有限公司  600519.XSHG  2016-03-24  2015-01-01  2015-12-31
5   贵州茅台酒股份有限公司  600519.XSHG  2016-04-21  2016-01-01  2016-03-31
6   贵州茅台酒股份有限公司  600519.XSHG  2016-08-27  2016-01-01  2016-06-30
7   贵州茅台酒股份有限公司  600519.XSHG  2016-10-29  2016-01-01  2016-09-30
8   贵州茅台酒股份有限公司  600519.XSHG  2017-04-15  2016-01-01  2016-12-31
9   贵州茅台酒股份有限公司  600519.XSHG  2017-04-25  2017-01-01  2017-03-31
10  贵州茅台酒股份有限公司  600519.XSHG  2017-07-28  2017-01-01  2017-06-30
11  贵州茅台酒股份有限公司  600519.XSHG  2017-10-26  2017-01-01  2017-09-30
12  贵州茅台酒股份有限公司  600519.XSHG  2018-03-28  2017-01-01  2017-12-31
13  贵州茅台酒股份有限公司  600519.XSHG  2018-04-28  2018-01-01  2018-03-31
14  贵州茅台酒股份有限公司  600519.XSHG  2018-08-02  2018-01-01  2018-06-30

    total_operating_revenue  np_parent_company_owners
0              3.221721e+10              1.534980e+10
1              8.760368e+09              4.364902e+09
2              1.618565e+10              7.888232e+09
3              2.373432e+10              1.142464e+10
4              3.344686e+10              1.550309e+10
5              1.025087e+10              4.889272e+09
6              1.873762e+10              8.802637e+09
7              2.753274e+10              1.246558e+10
8              4.015508e+10              1.671836e+10
9              1.391341e+10              6.123119e+09
10             2.549390e+10              1.125086e+10
11             4.448737e+10              1.998385e+10
12             6.106276e+10              2.707936e+10
13             1.839526e+10              8.506907e+09
14             3.525146e+10              1.576419e+10
```

### 母公司利润表

#### 上市公司母公司利润表

```
from jqdata import finance
finance.run_query(query(finance.STK_INCOME_STATEMENT_PARENT).filter(finance.STK_INCOME_STATEMENT_PARENT.code==code).limit(n))
```

获取上市公司母公司利润的信息（2007版）

**参数：**

- **query(finance.STK_INCOME_STATEMENT_PARENT)**：表示从finance.STK_INCOME_STATEMENT_PARENT这张表中查询上市公司母公司利润表的字段信息，还可以指定所要查询的字段名，格式如下：query(库名.表名.字段名1，库名.表名.字段名2），多个字段用逗号分隔进行提取；query函数的更多用法详见：[sqlalchemy.orm.query.Query对象](http://docs.sqlalchemy.org/en/rel_1_0/orm/query.html)
    
- **finance.STK_INCOME_STATEMENT_PARENT**：代表上市公司母公司利润表，收录了上市公司母公司的利润信息，表结构和字段信息如下：
    
    | 字段名称 | 中文名称 | 字段类型 | 含义 |
    | --- | --- | --- | --- |
    | company_id | 公司ID | int |  |
    | company_name | 公司名称 | varchar(100) |  |
    | code | 股票代码 | varchar(12) |  |
    | a_code | A股代码 | varchar(12) |  |
    | b_code | B股代码 | varchar(12) |  |
    | h_code | H股代码 | varchar(12) |  |
    | pub_date | 公告日期 | date |  |
    | start_date | 开始日期 | date |  |
    | end_date | 截止日期 | date |  |
    | report_date | 报告期 | date |  |
    | report_type | 报告期类型 | int | 0本期，1上期 |
    | source_id | 报表来源编码 | int | 如下[报表来源编码](#source2) |
    | source | 报表来源 | varchar(60) |  |
    | total_operating_revenue | 营业总收入 | decimal(20,4) |  |
    | operating_revenue | 营业收入 | decimal(20,4) |  |
    | total_operating_cost | 营业总成本 | decimal(20,4) |  |
    | operating_cost | 营业成本 | decimal(20,4) |  |
    | operating_tax_surcharges | 营业税金及附加 | decimal(20,4) |  |
    | sale_expense | 销售费用 | decimal(20,4) |  |
    | administration_expense | 管理费用 | decimal(20,4) |  |
    | exploration_expense | 堪探费用 | decimal(20,4) | 勘探费用用于核算企业（石油天然气开采）核算的油气勘探过程中发生的地质调查、物理化学勘探各项支出和非成功探井等支出。 |
    | financial_expense | 财务费用 | decimal(20,4) |  |
    | asset_impairment_loss | 资产减值损失 | decimal(20,4) |  |
    | fair_value_variable_income | 公允价值变动净收益 | decimal(20,4) |  |
    | investment_income | 投资收益 | decimal(20,4) |  |
    | invest_income_associates | 对联营企业和合营企业的投资收益 | decimal(20,4) |  |
    | exchange_income | 汇兑收益 | decimal(20,4) |  |
    | other_items_influenced_income | 影响营业利润的其他科目 | decimal(20,4) |  |
    | operating_profit | 营业利润 | decimal(20,4) |  |
    | subsidy_income | 补贴收入 | decimal(20,4) |  |
    | non_operating_revenue | 营业外收入 | decimal(20,4) |  |
    | non_operating_expense | 营业外支出 | decimal(20,4) |  |
    | disposal_loss_non_current_liability | 非流动资产处置净损失 | decimal(20,4) |  |
    | other_items_influenced_profit | 影响利润总额的其他科目 | decimal(20,4) |  |
    | total_profit | 利润总额 | decimal(20,4) |  |
    | income_tax | 所得税 | decimal(20,4) |  |
    | other_items_influenced_net_profit | 影响净利润的其他科目 | decimal(20,4) |  |
    | net_profit | 净利润 | decimal(20,4) |  |
    | np_parent_company_owners | 归属于母公司所有者的净利润 | decimal(20,4) |  |
    | minority_profit | 少数股东损益 | decimal(20,4) |  |
    | eps | 每股收益 | decimal(20,4) |  |
    | basic_eps | 基本每股收益 | decimal(20,4) |  |
    | diluted_eps | 稀释每股收益 | decimal(20,4) |  |
    | other_composite_income | 其他综合收益 | decimal(20,4) |  |
    | total_composite_income | 综合收益总额 | decimal(20,4) |  |
    | ci_parent_company_owners | 归属于母公司所有者的综合收益总额 | decimal(20,4) |  |
    | ci_minority_owners | 归属于少数股东的综合收益总额 | decimal(20,4) |  |
    | interest_income | 利息收入 | decimal(20,4) |  |
    | premiums_earned | 已赚保费 | decimal(20,4) |  |
    | commission_income | 手续费及佣金收入 | decimal(20,4) |  |
    | interest_expense | 利息支出 | decimal(20,4) |  |
    | commission_expense | 手续费及佣金支出 | decimal(20,4) |  |
    | refunded_premiums | 退保金 | decimal(20,4) |  |
    | net_pay_insurance_claims | 赔付支出净额 | decimal(20,4) |  |
    | withdraw_insurance_contract_reserve | 提取保险合同准备金净额 | decimal(20,4) |  |
    | policy_dividend_payout | 保单红利支出 | decimal(20,4) |  |
    | reinsurance_cost | 分保费用 | decimal(20,4) |  |
    | non_current_asset_disposed | 非流动资产处置利得 | decimal(20,4) |  |
    | other_earnings | 其他收益 | decimal(20,4) |  |
    | asset_deal_income | 资产处置收益 | decimal(20,4) |  |
    | sust_operate_net_profit | 持续经营净利润 | decimal(20,4) |  |
    | discon_operate_net_profit | 终止经营净利润 | decimal(20,4) |  |
    | credit_impairment_loss | 信用减值损失 | decimal(20,4) |  |
    | net_open_hedge_income | 净敞口套期收益 | decimal(20,4) |  |
    | interest_cost_fin | 财务费用-利息费用 | decimal(20,4) |  |
    | interest_income_fin | 财务费用-利息收入 | decimal(20,4) |  |
    | rd_expenses | 研发费用 | decimal(20,4) |  |
    
    **报表来源编码**
    
    | 编码 | 名称 |
    | --- | --- |
    | 321001 | 招募说明书 |
    | 321002 | 上市公告书 |
    | 321003 | 定期报告 |
    | 321004 | 预披露公告 |
    | 321005 | 换股报告书 |
    | 321099 | 其他 |
    
- **filter(finance.STK_INCOME_STATEMENT_PARENT.code==code)**：指定筛选条件，通过finance.STK_INCOME_STATEMENT_PARENT.code==code可以指定你想要查询的股票代码；除此之外，还可以对表中其他字段指定筛选条件，如finance.STK_INCOME_STATEMENT_PARENT.pub_date>='2015-01-01'，表示公告日期大于2015年1月1日上市公司公布的母公司利润表信息；多个筛选条件用英文逗号分隔。
    
- **limit(n)**：限制返回的数据条数，n指定返回条数。
    

**返回结果：**

- 返回一个 dataframe，每一行对应数据表中的一条数据， 列索引是你所查询的字段名称

**注意：**

1.  **为了防止返回数据量过大, 我们每次最多返回4000行**
2.  不能进行连表查询，即同时查询多张表的数据

**示例：**

```python
#查询贵州茅台2015年之后公告的母公司利润表数据，取出母公司利润表中本期的营业总收入，归属于母公司所有者的净利润
from jqdata import finance
q=query(finance.STK_INCOME_STATEMENT_PARENT.company_name,
        finance.STK_INCOME_STATEMENT_PARENT.code,
        finance.STK_INCOME_STATEMENT_PARENT.pub_date,
        finance.STK_INCOME_STATEMENT_PARENT.start_date,
        finance.STK_INCOME_STATEMENT_PARENT.end_date,
        finance.STK_INCOME_STATEMENT_PARENT.total_operating_revenue,
finance.STK_INCOME_STATEMENT_PARENT.np_parent_company_owners).filter(finance.STK_INCOME_STATEMENT_PARENT.code=='600519.XSHG',finance.STK_INCOME_STATEMENT_PARENT.pub_date>='2015-01-01',finance.STK_INCOME_STATEMENT_PARENT.report_type==0).limit(20)
df=finance.run_query(q)
print(df)

   company_name         code    pub_date  start_date    end_date  \
0   贵州茅台酒股份有限公司  600519.XSHG  2015-04-21  2014-01-01  2014-12-31
1   贵州茅台酒股份有限公司  600519.XSHG  2015-04-21  2015-01-01  2015-03-31
2   贵州茅台酒股份有限公司  600519.XSHG  2015-08-28  2015-01-01  2015-06-30
3   贵州茅台酒股份有限公司  600519.XSHG  2015-10-23  2015-01-01  2015-09-30
4   贵州茅台酒股份有限公司  600519.XSHG  2016-03-24  2015-01-01  2015-12-31
5   贵州茅台酒股份有限公司  600519.XSHG  2016-04-21  2016-01-01  2016-03-31
6   贵州茅台酒股份有限公司  600519.XSHG  2016-08-27  2016-01-01  2016-06-30
7   贵州茅台酒股份有限公司  600519.XSHG  2016-10-29  2016-01-01  2016-09-30
8   贵州茅台酒股份有限公司  600519.XSHG  2017-04-15  2016-01-01  2016-12-31
9   贵州茅台酒股份有限公司  600519.XSHG  2017-04-25  2017-01-01  2017-03-31
10  贵州茅台酒股份有限公司  600519.XSHG  2017-07-28  2017-01-01  2017-06-30
11  贵州茅台酒股份有限公司  600519.XSHG  2017-10-26  2017-01-01  2017-09-30
12  贵州茅台酒股份有限公司  600519.XSHG  2018-03-28  2017-01-01  2017-12-31
13  贵州茅台酒股份有限公司  600519.XSHG  2018-04-28  2018-01-01  2018-03-31
14  贵州茅台酒股份有限公司  600519.XSHG  2018-08-02  2018-01-01  2018-06-30

    total_operating_revenue  np_parent_company_owners
0              6.878165e+09              1.028603e+10
1              1.886084e+09             -5.773331e+07
2              3.571872e+09             -1.556184e+08
3              5.411957e+09              9.476542e+09
4              8.843334e+09              9.611173e+09
5              1.507658e+09              8.850591e+09
6              3.608903e+09              8.733012e+09
7              5.430884e+09              8.002128e+09
8              1.289781e+10              9.251255e+09
9              4.992937e+09              1.023919e+09
10             9.310346e+09              8.967873e+09
11             1.720851e+10              1.074275e+10
12             2.192229e+10              1.079946e+10
13             6.005294e+09              9.480740e+08
14             1.162651e+10              5.081753e+10
```

### 合并现金流量表

```python
from jqdata import finance
finance.run_query(query(finance.STK_CASHFLOW_STATEMENT).filter(finance.STK_CASHFLOW_STATEMENT.code==code).limit(n))
```

获取上市公司定期公告中公布的合并现金流量表数据（2007版）

**参数：**

- **query(finance.STK_CASHFLOW_STATEMENT)**：表示从finance.STK_CASHFLOW_STATEMENT这张表中查询上市公司定期公告中公布的合并现金流量表信息，还可以指定所要查询的字段名，格式如下：query(库名.表名.字段名1，库名.表名.字段名2），多个字段用逗号分隔进行提取；query函数的更多用法详见：[sqlalchemy.orm.query.Query对象](http://docs.sqlalchemy.org/en/rel_1_0/orm/query.html)
    
- **finance.STK_CASHFLOW_STATEMENT**：代表上市公司合并现金流量表，收录了上市公司定期公告中公布的合并现金流量表数据，表结构和字段信息如下：
    
    | 字段名称 | 中文名称 | 字段类型 | 含义 |
    | --- | --- | --- | --- |
    | company_id | 公司ID | int |  |
    | company_name | 公司名称 | varchar(100) |  |
    | code | 股票主证券代码 | varchar(12) |  |
    | a_code | A股代码 | varchar(12) |  |
    | b_code | B股代码 | varchar(12) |  |
    | h_code | H股代码 | varchar(12) |  |
    | pub_date | 公告日期 | date |  |
    | start_date | 开始日期 | date |  |
    | end_date | 截止日期 | date |  |
    | report_date | 报告期 | date |  |
    | report_type | 报告期类型 | int | 0本期，1上期 |
    | source_id | 报表来源编码 | int | 如下[报表来源编码](#source3) |
    | source | 报表来源 | varchar(60) |  |
    | goods_sale_and_service_render_cash | 销售商品、提供劳务收到的现金 | decimal(20,4) |  |
    | tax_levy_refund | 收到的税费返还 | decimal(20,4) |  |
    | subtotal_operate_cash_inflow | 经营活动现金流入小计 | decimal(20,4) |  |
    | goods_and_services_cash_paid | 购买商品、接受劳务支付的现金 | decimal(20,4) |  |
    | staff_behalf_paid | 支付给职工以及为职工支付的现金 | decimal(20,4) |  |
    | tax_payments | 支付的各项税费 | decimal(20,4) |  |
    | subtotal_operate_cash_outflow | 经营活动现金流出小计 | decimal(20,4) |  |
    | net_operate_cash_flow | 经营活动现金流量净额 | decimal(20,4) |  |
    | invest_withdrawal_cash | 收回投资收到的现金 | decimal(20,4) |  |
    | invest_proceeds | 取得投资收益收到的现金 | decimal(20,4) |  |
    | fix_intan_other_asset_dispo_cash | 处置固定资产、无形资产和其他长期资产收回的现金净额 | decimal(20,4) |  |
    | net_cash_deal_subcompany | 处置子公司及其他营业单位收到的现金净额 | decimal(20,4) |  |
    | subtotal_invest_cash_inflow | 投资活动现金流入小计 | decimal(20,4) |  |
    | fix_intan_other_asset_acqui_cash | 购建固定资产、无形资产和其他长期资产支付的现金 | decimal(20,4) |  |
    | invest_cash_paid | 投资支付的现金 | decimal(20,4) |  |
    | impawned_loan_net_increase | 质押贷款净增加额 | decimal(20,4) |  |
    | net_cash_from_sub_company | 取得子公司及其他营业单位支付的现金净额 | decimal(20,4) |  |
    | subtotal_invest_cash_outflow | 投资活动现金流出小计 | decimal(20,4) |  |
    | net_invest_cash_flow | 投资活动现金流量净额 | decimal(20,4) |  |
    | cash_from_invest | 吸收投资收到的现金 | decimal(20,4) |  |
    | cash_from_borrowing | 取得借款收到的现金 | decimal(20,4) |  |
    | cash_from_bonds_issue | 发行债券收到的现金 | decimal(20,4) |  |
    | subtotal_finance_cash_inflow | 筹资活动现金流入小计 | decimal(20,4) |  |
    | borrowing_repayment | 偿还债务支付的现金 | decimal(20,4) |  |
    | dividend_interest_payment | 分配股利、利润或偿付利息支付的现金 | decimal(20,4) |  |
    | subtotal_finance_cash_outflow | 筹资活动现金流出小计 | decimal(20,4) |  |
    | net_finance_cash_flow | 筹资活动现金流量净额 | decimal(20,4) |  |
    | exchange_rate_change_effect | 汇率变动对现金的影响 | decimal(20,4) |  |
    | other_reason_effect_cash | 其他原因对现金的影响 | decimal(20,4) |  |
    | cash_equivalent_increase | 现金及现金等价物净增加额 | decimal(20,4) |  |
    | cash_equivalents_at_beginning | 期初现金及现金等价物余额 | decimal(20,4) |  |
    | cash_and_equivalents_at_end | 期末现金及现金等价物余额 | decimal(20,4) |  |
    | net_profit | 净利润 | decimal(20,4) |  |
    | assets_depreciation_reserves | 资产减值准备 | decimal(20,4) |  |
    | fixed_assets_depreciation | 固定资产折旧、油气资产折耗、生产性生物资产折旧 | decimal(20,4) |  |
    | intangible_assets_amortization | 无形资产摊销 | decimal(20,4) |  |
    | defferred_expense_amortization | 长期待摊费用摊销 | decimal(20,4) |  |
    | fix_intan_other_asset_dispo_loss | 处置固定资产、无形资产和其他长期资产的损失 | decimal(20,4) |  |
    | fixed_asset_scrap_loss | 固定资产报废损失 | decimal(20,4) |  |
    | fair_value_change_loss | 公允价值变动损失 | decimal(20,4) |  |
    | financial_cost | 财务费用 | decimal(20,4) |  |
    | invest_loss | 投资损失 | decimal(20,4) |  |
    | deffered_tax_asset_decrease | 递延所得税资产减少 | decimal(20,4) |  |
    | deffered_tax_liability_increase | 递延所得税负债增加 | decimal(20,4) |  |
    | inventory_decrease | 存货的减少 | decimal(20,4) |  |
    | operate_receivables_decrease | 经营性应收项目的减少 | decimal(20,4) |  |
    | operate_payable_increase | 经营性应付项目的增加 | decimal(20,4) |  |
    | others | 其他 | decimal(20,4) |  |
    | net_operate_cash_flow_indirect | 经营活动现金流量净额_间接法 | decimal(20,4) |  |
    | debt_to_capital | 债务转为资本 | decimal(20,4) |  |
    | cbs_expiring_in_one_year | 一年内到期的可转换公司债券 | decimal(20,4) |  |
    | financial_lease_fixed_assets | 融资租入固定资产 | decimal(20,4) |  |
    | cash_at_end | 现金的期末余额 | decimal(20,4) |  |
    | cash_at_beginning | 现金的期初余额 | decimal(20,4) |  |
    | equivalents_at_end | 现金等价物的期末余额 | decimal(20,4) |  |
    | equivalents_at_beginning | 现金等价物的期初余额 | decimal(20,4) |  |
    | other_reason_effect_cash_indirect | 其他原因对现金的影响_间接法 | decimal(20,4) |  |
    | cash_equivalent_increase_indirect | 现金及现金等价物净增加额_间接法 | decimal(20,4) |  |
    | net_deposit_increase | 客户存款和同业存放款项净增加额 | decimal(20,4) |  |
    | net_borrowing_from_central_bank | 向中央银行借款净增加额 | decimal(20,4) |  |
    | net_borrowing_from_finance_co | 向其他金融机构拆入资金净增加额 | decimal(20,4) |  |
    | net_original_insurance_cash | 收到原保险合同保费取得的现金 | decimal(20,4) |  |
    | net_cash_received_from_reinsurance_business | 收到再保险业务现金净额 | decimal(20,4) |  |
    | net_insurer_deposit_investment | 保户储金及投资款净增加额 | decimal(20,4) |  |
    | net_deal_trading_assets | 处置以公允价值计量且其变动计入当期损益的金融资产净增加额 | decimal(20,4) |  |
    | interest_and_commission_cashin | 收取利息、手续费及佣金的现金 | decimal(20,4) |  |
    | net_increase_in_placements | 拆入资金净增加额 | decimal(20,4) |  |
    | net_buyback | 回购业务资金净增加额 | decimal(20,4) |  |
    | net_loan_and_advance_increase | 客户贷款及垫款净增加额 | decimal(20,4) |  |
    | net_deposit_in_cb_and_ib | 存放中央银行和同业款项净增加额 | decimal(20,4) |  |
    | original_compensation_paid | 支付原保险合同赔付款项的现金 | decimal(20,4) |  |
    | handling_charges_and_commission | 支付利息、手续费及佣金的现金 | decimal(20,4) |  |
    | policy_dividend_cash_paid | 支付保单红利的现金 | decimal(20,4) |  |
    | cash_from_mino_s_invest_sub | 子公司吸收少数股东投资收到的现金 | decimal(20,4) |  |
    | proceeds_from_sub_to_mino_s | 子公司支付给少数股东的股利、利润 | decimal(20,4) |  |
    | investment_property_depreciation | 投资性房地产的折旧及摊销 | decimal(20,4) |  |
    | credit_impairment_loss | 信用减值损失(现金流量表补充科目) | decimal(20,4) |  |
    
    **报表来源编码**
    
    | 编码 | 名称 |
    | --- | --- |
    | 321001 | 招募说明书 |
    | 321002 | 上市公告书 |
    | 321003 | 定期报告 |
    | 321004 | 预披露公告 |
    | 321005 | 换股报告书 |
    | 321099 | 其他 |
    
- **filter(finance.STK_CASHFLOW_STATEMENT.code==code)**：指定筛选条件，通过finance.STK_CASHFLOW_STATEMENT.code==code可以指定你想要查询的股票代码；除此之外，还可以对表中其他字段指定筛选条件，如finance.STK_CASHFLOW_STATEMENT.pub_date>='2015-01-01'，表示公告日期大于2015年1月1日上市公司合并现金流量表数据；多个筛选条件用英文逗号分隔。
    
- **limit(n)**：限制返回的数据条数，n指定返回条数。
    

**返回结果：**

- 返回一个 dataframe，每一行对应数据表中的一条数据， 列索引是你所查询的字段名称

**注意：**

1.  **为了防止返回数据量过大, 我们每次最多返回4000行**
2.  不能进行连表查询，即同时查询多张表的数据

**示例：**

```python
#查询贵州茅台2015年之后公告的合并现金流量表数据，取出本期的经营活动现金流量净额，投资活动现金流量净额，以及筹资活动现金流量净额
from jqdata import *
q=query(finance.STK_CASHFLOW_STATEMENT.company_name,
        finance.STK_CASHFLOW_STATEMENT.code,
        finance.STK_CASHFLOW_STATEMENT.pub_date,
        finance.STK_CASHFLOW_STATEMENT.start_date,
        finance.STK_CASHFLOW_STATEMENT.end_date,
        finance.STK_CASHFLOW_STATEMENT.net_operate_cash_flow,
        finance.STK_CASHFLOW_STATEMENT.net_invest_cash_flow,
finance.STK_CASHFLOW_STATEMENT.net_finance_cash_flow).filter(finance.STK_CASHFLOW_STATEMENT.code=='600519.XSHG',finance.STK_CASHFLOW_STATEMENT.pub_date>='2015-01-01',finance.STK_CASHFLOW_STATEMENT.report_type==0).limit(20)
df=finance.run_query(q)
print(df)

   company_name         code    pub_date  start_date    end_date  \
0   贵州茅台酒股份有限公司  600519.XSHG  2015-04-21  2014-01-01  2014-12-31
1   贵州茅台酒股份有限公司  600519.XSHG  2015-04-21  2015-01-01  2015-03-31
2   贵州茅台酒股份有限公司  600519.XSHG  2015-08-28  2015-01-01  2015-06-30
3   贵州茅台酒股份有限公司  600519.XSHG  2015-10-23  2015-01-01  2015-09-30
4   贵州茅台酒股份有限公司  600519.XSHG  2016-03-24  2015-01-01  2015-12-31
5   贵州茅台酒股份有限公司  600519.XSHG  2016-04-21  2016-01-01  2016-03-31
6   贵州茅台酒股份有限公司  600519.XSHG  2016-08-27  2016-01-01  2016-06-30
7   贵州茅台酒股份有限公司  600519.XSHG  2016-10-29  2016-01-01  2016-09-30
8   贵州茅台酒股份有限公司  600519.XSHG  2017-04-15  2016-01-01  2016-12-31
9   贵州茅台酒股份有限公司  600519.XSHG  2017-04-25  2017-01-01  2017-03-31
10  贵州茅台酒股份有限公司  600519.XSHG  2017-07-28  2017-01-01  2017-06-30
11  贵州茅台酒股份有限公司  600519.XSHG  2017-10-26  2017-01-01  2017-09-30
12  贵州茅台酒股份有限公司  600519.XSHG  2018-03-28  2017-01-01  2017-12-31
13  贵州茅台酒股份有限公司  600519.XSHG  2018-04-28  2018-01-01  2018-03-31
14  贵州茅台酒股份有限公司  600519.XSHG  2018-08-02  2018-01-01  2018-06-30

    net_operate_cash_flow  net_invest_cash_flow  net_finance_cash_flow
0            1.263252e+10         -4.580160e+09          -5.041427e+09
1            2.111634e+09         -8.540453e+08          -3.464185e+07
2            4.901688e+09         -1.290715e+09          -3.494246e+07
3            1.142339e+10         -1.782995e+09          -5.587555e+09
4            1.743634e+10         -2.048790e+09          -5.588020e+09
5            7.436044e+09         -4.213453e+08          -5.085073e+08
6            1.360396e+10         -5.555078e+08          -3.283074e+09
7            3.253533e+10         -7.734874e+08          -8.284064e+09
8            3.745125e+10         -1.102501e+09          -8.334512e+09
9            6.108975e+09         -3.003397e+08                    NaN
10           6.935360e+09         -4.706886e+08          -3.640000e+08
11           2.278677e+10         -7.477752e+08          -8.893178e+09
12           2.215304e+10         -1.120645e+09          -8.899178e+09
13           4.935501e+09         -5.919110e+08                    NaN
14           1.773503e+10         -7.397817e+08          -1.385492e+10
```

### 母公司现金流量表

```
from jqdata import finance
finance.run_query(query(finance.STK_CASHFLOW_STATEMENT_PARENT).filter(finance.STK_CASHFLOW_STATEMENT_PARENT.code==code).limit(n))
```

获取上市公司定期公告中公布的母公司现金流量表（2007版）

**参数：**

- **query(finance.STK_CASHFLOW_STATEMENT_PARENT)**：表示从finance.STK_CASHFLOW_STATEMENT_PARENT这张表中查询上市公司定期公告中公布的母公司现金流量表信息，还可以指定所要查询的字段名，格式如下：query(库名.表名.字段名1，库名.表名.字段名2），多个字段用逗号分隔进行提取；query函数的更多用法详见：[sqlalchemy.orm.query.Query对象](http://docs.sqlalchemy.org/en/rel_1_0/orm/query.html)
    
- **finance.STK_CASHFLOW_STATEMENT_PARENT**：代表上市公司母公司现金流量表，收录了上市公司定期公告中公布的母公司现金流量表数据，表结构和字段信息如下：
    
    | 字段名称 | 中文名称 | 字段类型 | 含义 |
    | --- | --- | --- | --- |
    | company_id | 公司ID | int |  |
    | company_name | 公司名称 | varchar(100) |  |
    | code | 股票主证券代码 | varchar(12) |  |
    | a_code | A股代码 | varchar(12) |  |
    | b_code | B股代码 | varchar(12) |  |
    | h_code | H股代码 | varchar(12) |  |
    | pub_date | 公告日期 | date |  |
    | start_date | 开始日期 | date |  |
    | end_date | 截止日期 | date |  |
    | report_date | 报告期 | date |  |
    | report_type | 报告期类型 | int | 0本期，1上期 |
    | source_id | 报表来源编码 | int | 如下[报表来源编码](#source4) |
    | source | 报表来源 | varchar(60) |  |
    | goods_sale_and_service_render_cash | 销售商品、提供劳务收到的现金 | decimal(20,4) |  |
    | tax_levy_refund | 收到的税费返还 | decimal(20,4) |  |
    | subtotal_operate_cash_inflow | 经营活动现金流入小计 | decimal(20,4) |  |
    | goods_and_services_cash_paid | 购买商品、接受劳务支付的现金 | decimal(20,4) |  |
    | staff_behalf_paid | 支付给职工以及为职工支付的现金 | decimal(20,4) |  |
    | tax_payments | 支付的各项税费 | decimal(20,4) |  |
    | subtotal_operate_cash_outflow | 经营活动现金流出小计 | decimal(20,4) |  |
    | net_operate_cash_flow | 经营活动现金流量净额 | decimal(20,4) |  |
    | invest_withdrawal_cash | 收回投资收到的现金 | decimal(20,4) |  |
    | invest_proceeds | 取得投资收益收到的现金 | decimal(20,4) |  |
    | fix_intan_other_asset_dispo_cash | 处置固定资产、无形资产和其他长期资产收回的现金净额 | decimal(20,4) |  |
    | net_cash_deal_subcompany | 处置子公司及其他营业单位收到的现金净额 | decimal(20,4) |  |
    | subtotal_invest_cash_inflow | 投资活动现金流入小计 | decimal(20,4) |  |
    | fix_intan_other_asset_acqui_cash | 购建固定资产、无形资产和其他长期资产支付的现金 | decimal(20,4) |  |
    | invest_cash_paid | 投资支付的现金 | decimal(20,4) |  |
    | impawned_loan_net_increase | 质押贷款净增加额 | decimal(20,4) |  |
    | net_cash_from_sub_company | 取得子公司及其他营业单位支付的现金净额 | decimal(20,4) |  |
    | subtotal_invest_cash_outflow | 投资活动现金流出小计 | decimal(20,4) |  |
    | net_invest_cash_flow | 投资活动现金流量净额 | decimal(20,4) |  |
    | cash_from_invest | 吸收投资收到的现金 | decimal(20,4) |  |
    | cash_from_borrowing | 取得借款收到的现金 | decimal(20,4) |  |
    | cash_from_bonds_issue | 发行债券收到的现金 | decimal(20,4) |  |
    | subtotal_finance_cash_inflow | 筹资活动现金流入小计 | decimal(20,4) |  |
    | borrowing_repayment | 偿还债务支付的现金 | decimal(20,4) |  |
    | dividend_interest_payment | 分配股利、利润或偿付利息支付的现金 | decimal(20,4) |  |
    | subtotal_finance_cash_outflow | 筹资活动现金流出小计 | decimal(20,4) |  |
    | net_finance_cash_flow | 筹资活动现金流量净额 | decimal(20,4) |  |
    | exchange_rate_change_effect | 汇率变动对现金的影响 | decimal(20,4) |  |
    | other_reason_effect_cash | 其他原因对现金的影响 | decimal(20,4) |  |
    | cash_equivalent_increase | 现金及现金等价物净增加额 | decimal(20,4) |  |
    | cash_equivalents_at_beginning | 期初现金及现金等价物余额 | decimal(20,4) |  |
    | cash_and_equivalents_at_end | 期末现金及现金等价物余额 | decimal(20,4) |  |
    | net_profit | 净利润 | decimal(20,4) |  |
    | assets_depreciation_reserves | 资产减值准备 | decimal(20,4) |  |
    | fixed_assets_depreciation | 固定资产折旧、油气资产折耗、生产性生物资产折旧 | decimal(20,4) |  |
    | intangible_assets_amortization | 无形资产摊销 | decimal(20,4) |  |
    | defferred_expense_amortization | 长期待摊费用摊销 | decimal(20,4) |  |
    | fix_intan_other_asset_dispo_loss | 处置固定资产、无形资产和其他长期资产的损失 | decimal(20,4) |  |
    | fixed_asset_scrap_loss | 固定资产报废损失 | decimal(20,4) |  |
    | fair_value_change_loss | 公允价值变动损失 | decimal(20,4) |  |
    | financial_cost | 财务费用 | decimal(20,4) |  |
    | invest_loss | 投资损失 | decimal(20,4) |  |
    | deffered_tax_asset_decrease | 递延所得税资产减少 | decimal(20,4) |  |
    | deffered_tax_liability_increase | 递延所得税负债增加 | decimal(20,4) |  |
    | inventory_decrease | 存货的减少 | decimal(20,4) |  |
    | operate_receivables_decrease | 经营性应收项目的减少 | decimal(20,4) |  |
    | operate_payable_increase | 经营性应付项目的增加 | decimal(20,4) |  |
    | others | 其他 | decimal(20,4) |  |
    | net_operate_cash_flow_indirect | 经营活动现金流量净额_间接法 | decimal(20,4) |  |
    | debt_to_capital | 债务转为资本 | decimal(20,4) |  |
    | cbs_expiring_in_one_year | 一年内到期的可转换公司债券 | decimal(20,4) |  |
    | financial_lease_fixed_assets | 融资租入固定资产 | decimal(20,4) |  |
    | cash_at_end | 现金的期末余额 | decimal(20,4) |  |
    | cash_at_beginning | 现金的期初余额 | decimal(20,4) |  |
    | equivalents_at_end | 现金等价物的期末余额 | decimal(20,4) |  |
    | equivalents_at_beginning | 现金等价物的期初余额 | decimal(20,4) |  |
    | other_reason_effect_cash_indirect | 其他原因对现金的影响_间接法 | decimal(20,4) |  |
    | cash_equivalent_increase_indirect | 现金及现金等价物净增加额_间接法 | decimal(20,4) |  |
    | net_deposit_increase | 客户存款和同业存放款项净增加额 | decimal(20,4) |  |
    | net_borrowing_from_central_bank | 向中央银行借款净增加额 | decimal(20,4) |  |
    | net_borrowing_from_finance_co | 向其他金融机构拆入资金净增加额 | decimal(20,4) |  |
    | net_original_insurance_cash | 收到原保险合同保费取得的现金 | decimal(20,4) |  |
    | net_cash_received_from_reinsurance_business | 收到再保险业务现金净额 | decimal(20,4) |  |
    | net_insurer_deposit_investment | 保户储金及投资款净增加额 | decimal(20,4) |  |
    | net_deal_trading_assets | 处置以公允价值计量且其变动计入当期损益的金融资产净增加额 | decimal(20,4) |  |
    | interest_and_commission_cashin | 收取利息、手续费及佣金的现金 | decimal(20,4) |  |
    | net_increase_in_placements | 拆入资金净增加额 | decimal(20,4) |  |
    | net_buyback | 回购业务资金净增加额 | decimal(20,4) |  |
    | net_loan_and_advance_increase | 客户贷款及垫款净增加额 | decimal(20,4) |  |
    | net_deposit_in_cb_and_ib | 存放中央银行和同业款项净增加额 | decimal(20,4) |  |
    | original_compensation_paid | 支付原保险合同赔付款项的现金 | decimal(20,4) |  |
    | handling_charges_and_commission | 支付利息、手续费及佣金的现金 | decimal(20,4) |  |
    | policy_dividend_cash_paid | 支付保单红利的现金 | decimal(20,4) |  |
    | cash_from_mino_s_invest_sub | 子公司吸收少数股东投资收到的现金 | decimal(20,4) |  |
    | proceeds_from_sub_to_mino_s | 子公司支付给少数股东的股利、利润 | decimal(20,4) |  |
    | investment_property_depreciation | 投资性房地产的折旧及摊销 | decimal(20,4) |  |
    | credit_impairment_loss | 信用减值损失(现金流量表补充科目) | decimal(20,4) |  |
    
    **报表来源编码**
    
    | 编码 | 名称 |
    | --- | --- |
    | 321001 | 招募说明书 |
    | 321002 | 上市公告书 |
    | 321003 | 定期报告 |
    | 321004 | 预披露公告 |
    | 321005 | 换股报告书 |
    | 321099 | 其他 |
    
- filter(finance.STK_CASHFLOW_STATEMENT_PARENT.code==code)**：指定筛选条件，通过finance.STK_CASHFLOW_STATEMENT_PARENT.code==code可以指定你想要查询的股票代码；除此之外，还可以对表中其他字段指定筛选条件，如finance.STK_CASHFLOW_STATEMENT_PARENT.pub_date>='2015-01-01'，表示公告日期大于2015年1月1日上市公司公布的母公司现金流量表信息；多个筛选条件用英文逗号分隔。
    
- **limit(n)**：限制返回的数据条数，n指定返回条数。
    

**返回结果：**

- 返回一个 dataframe，每一行对应数据表中的一条数据， 列索引是你所查询的字段名称

**注意：**

1.  **为了防止返回数据量过大, 我们每次最多返回4000行**
2.  不能进行连表查询，即同时查询多张表的数据

**示例：**

```python
#查询贵州茅台2015年之后公告的母公司现金流量表数据，取出本期的经营活动现金流量净额，投资活动现金流量净额，以及筹资活动现金流量净额
from jqdata import *
q=query(finance.STK_CASHFLOW_STATEMENT_PARENT.company_name,
        finance.STK_CASHFLOW_STATEMENT_PARENT.code,
        finance.STK_CASHFLOW_STATEMENT_PARENT.pub_date,
        finance.STK_CASHFLOW_STATEMENT_PARENT.start_date,
        finance.STK_CASHFLOW_STATEMENT_PARENT.end_date,
        finance.STK_CASHFLOW_STATEMENT_PARENT.net_operate_cash_flow,
        finance.STK_CASHFLOW_STATEMENT_PARENT.net_invest_cash_flow,
finance.STK_CASHFLOW_STATEMENT_PARENT.net_finance_cash_flow).filter(finance.STK_CASHFLOW_STATEMENT_PARENT.code=='600519.XSHG',finance.STK_CASHFLOW_STATEMENT_PARENT.pub_date>='2015-01-01',finance.STK_CASHFLOW_STATEMENT_PARENT.report_type==0).limit(20)
df=finance.run_query(q)
print(df)

   company_name         code    pub_date  start_date    end_date  \
0   贵州茅台酒股份有限公司  600519.XSHG  2015-04-21  2014-01-01  2014-12-31
1   贵州茅台酒股份有限公司  600519.XSHG  2015-04-21  2015-01-01  2015-03-31
2   贵州茅台酒股份有限公司  600519.XSHG  2015-08-28  2015-01-01  2015-06-30
3   贵州茅台酒股份有限公司  600519.XSHG  2015-10-23  2015-01-01  2015-09-30
4   贵州茅台酒股份有限公司  600519.XSHG  2016-03-24  2015-01-01  2015-12-31
5   贵州茅台酒股份有限公司  600519.XSHG  2016-04-21  2016-01-01  2016-03-31
6   贵州茅台酒股份有限公司  600519.XSHG  2016-08-27  2016-01-01  2016-06-30
7   贵州茅台酒股份有限公司  600519.XSHG  2016-10-29  2016-01-01  2016-09-30
8   贵州茅台酒股份有限公司  600519.XSHG  2017-04-15  2016-01-01  2016-12-31
9   贵州茅台酒股份有限公司  600519.XSHG  2017-04-25  2017-01-01  2017-03-31
10  贵州茅台酒股份有限公司  600519.XSHG  2017-07-28  2017-01-01  2017-06-30
11  贵州茅台酒股份有限公司  600519.XSHG  2017-10-26  2017-01-01  2017-09-30
12  贵州茅台酒股份有限公司  600519.XSHG  2018-03-28  2017-01-01  2017-12-31
13  贵州茅台酒股份有限公司  600519.XSHG  2018-04-28  2018-01-01  2018-03-31
14  贵州茅台酒股份有限公司  600519.XSHG  2018-08-02  2018-01-01  2018-06-30

    net_operate_cash_flow  net_invest_cash_flow  net_finance_cash_flow
0           -2.713989e+09          6.192758e+09          -4.562999e+09
1            2.082144e+09         -1.135273e+09           2.200000e+07
2            3.259594e+09         -1.568552e+09           2.200000e+07
3            2.284079e+09          8.054632e+08          -5.040068e+09
4            1.975006e+09          7.412721e+09          -5.018068e+09
5            6.073286e+08          8.692869e+07                    NaN
6           -7.648020e+08          7.468597e+09          -2.774566e+09
7           -7.797669e+08          8.882256e+09          -7.751997e+09
8            7.157030e+08          8.562947e+09          -7.818445e+09
9           -2.124767e+09         -3.119164e+08                    NaN
10          -1.473598e+09         -4.806175e+08                    NaN
11           8.751075e+08          6.337564e+09          -8.525814e+09
12           1.565579e+09          5.981627e+09          -8.525814e+09
13          -2.814955e+08         -5.779401e+08                    NaN
14          -2.121182e+09          1.535743e+10          -1.381692e+10
```

### 合并资产负债表

```
from jqdata import finance
finance.run_query(query(finance.STK_BALANCE_SHEET).filter(finance.STK_BALANCE_SHEET.code==code).limit(n))
```

获取上市公司定期公告中公布的合并资产负债表（2007版）

**参数：**

- **query(finance.STK_BALANCE_SHEET)**：表示从finance.STK_BALANCE_SHEET这张表中查询上市公司定期公告中公布的合并资产负债表信息，还可以指定所要查询的字段名，格式如下：query(库名.表名.字段名1，库名.表名.字段名2），多个字段用逗号分隔进行提取；query函数的更多用法详见：[sqlalchemy.orm.query.Query对象](http://docs.sqlalchemy.org/en/rel_1_0/orm/query.html)
    
- **finance.STK_BALANCE_SHEET**：代表上市公司合并资产负债表信息，收录了上市公司定期公告中公布的合并资产负债表数据，表结构和字段信息如下：
    
    | 字段名称 | 中文名称 | 字段类型 | 含义 |
    | --- | --- | --- | --- |
    | company_id | 公司ID | int |  |
    | company_name | 公司名称 | varchar(100) |  |
    | code | 股票代码 | varchar(12) |  |
    | a_code | A股代码 | varchar(12) |  |
    | b_code | B股代码 | varchar(12) |  |
    | h_code | H股代码 | varchar(12) |  |
    | pub_date | 公告日期 | date |  |
    | start_date | 开始日期 | date |  |
    | end_date | 截止日期 | date |  |
    | report_date | 报告期 | date |  |
    | report_type | 报告期类型 | int | 0本期，1上期 |
    | source_id | 报表来源编码 | int | 如下 [报表来源编码](#source5) |
    | source | 报表来源 | varchar(60) |  |
    | cash_equivalents | 货币资金 | decimal(20,4) |  |
    | trading_assets | 交易性金融资产 | decimal(20,4) |  |
    | bill_receivable | 应收票据 | decimal(20,4) |  |
    | account_receivable | 应收账款 | decimal(20,4) |  |
    | advance_payment | 预付款项 | decimal(20,4) |  |
    | other_receivable | 其他应收款 | decimal(20,4) |  |
    | affiliated_company_receivable | 应收关联公司款 | decimal(20,4) |  |
    | interest_receivable | 应收利息 | decimal(20,4) |  |
    | dividend_receivable | 应收股利 | decimal(20,4) |  |
    | inventories | 存货 | decimal(20,4) |  |
    | expendable_biological_asset | 消耗性生物资产 | decimal(20,4) | 消耗性生物资产，是指为出售而持有的、或在将来收获为农产品的生物资产，包括生长中的大田作物、蔬菜、用材林，以及存栏代售的牲畜等 |
    | non_current_asset_in_one_year | 一年内到期的非流动资产 | decimal(20,4) |  |
    | total_current_assets | 流动资产合计 | decimal(20,4) |  |
    | hold_for_sale_assets | 可供出售金融资产 | decimal(20,4) |  |
    | hold_to_maturity_investments | 持有至到期投资 | decimal(20,4) |  |
    | longterm_receivable_account | 长期应收款 | decimal(20,4) |  |
    | longterm_equity_invest | 长期股权投资 | decimal(20,4) |  |
    | investment_property | 投资性房地产 | decimal(20,4) |  |
    | fixed_assets | 固定资产 | decimal(20,4) |  |
    | constru_in_process | 在建工程 | decimal(20,4) |  |
    | construction_materials | 工程物资 | decimal(20,4) |  |
    | fixed_assets_liquidation | 固定资产清理 | decimal(20,4) |  |
    | biological_assets | 生产性生物资产 | decimal(20,4) |  |
    | oil_gas_assets | 油气资产 | decimal(20,4) |  |
    | intangible_assets | 无形资产 | decimal(20,4) |  |
    | development_expenditure | 开发支出 | decimal(20,4) |  |
    | good_will | 商誉 | decimal(20,4) |  |
    | long_deferred_expense | 长期待摊费用 | decimal(20,4) |  |
    | deferred_tax_assets | 递延所得税资产 | decimal(20,4) |  |
    | total_non_current_assets | 非流动资产合计 | decimal(20,4) |  |
    | total_assets | 资产总计 | decimal(20,4) |  |
    | shortterm_loan | 短期借款 | decimal(20,4) |  |
    | trading_liability | 交易性金融负债 | decimal(20,4) |  |
    | notes_payable | 应付票据 | decimal(20,4) |  |
    | accounts_payable | 应付账款 | decimal(20,4) |  |
    | advance_peceipts | 预收款项 | decimal(20,4) |  |
    | salaries_payable | 应付职工薪酬 | decimal(20,4) |  |
    | taxs_payable | 应交税费 | decimal(20,4) |  |
    | interest_payable | 应付利息 | decimal(20,4) |  |
    | dividend_payable | 应付股利 | decimal(20,4) |  |
    | other_payable | 其他应付款 | decimal(20,4) |  |
    | affiliated_company_payable | 应付关联公司款 | decimal(20,4) |  |
    | non_current_liability_in_one_year | 一年内到期的非流动负债 | decimal(20,4) |  |
    | total_current_liability | 流动负债合计 | decimal(20,4) |  |
    | longterm_loan | 长期借款 | decimal(20,4) |  |
    | bonds_payable | 应付债券 | decimal(20,4) |  |
    | longterm_account_payable | 长期应付款 | decimal(20,4) |  |
    | specific_account_payable | 专项应付款 | decimal(20,4) |  |
    | estimate_liability | 预计负债 | decimal(20,4) |  |
    | deferred_tax_liability | 递延所得税负债 | decimal(20,4) |  |
    | total_non_current_liability | 非流动负债合计 | decimal(20,4) |  |
    | total_liability | 负债合计 | decimal(20,4) |  |
    | paidin_capital | 实收资本（或股本） | decimal(20,4) |  |
    | capital_reserve_fund | 资本公积 | decimal(20,4) |  |
    | specific_reserves | 专项储备 | decimal(20,4) |  |
    | surplus_reserve_fund | 盈余公积 | decimal(20,4) |  |
    | treasury_stock | 库存股 | decimal(20,4) |  |
    | retained_profit | 未分配利润 | decimal(20,4) |  |
    | equities_parent_company_owners | 归属于母公司所有者权益 | decimal(20,4) |  |
    | minority_interests | 少数股东权益 | decimal(20,4) |  |
    | foreign_currency_report_conv_diff | 外币报表折算价差 | decimal(20,4) |  |
    | irregular_item_adjustment | 非正常经营项目收益调整 | decimal(20,4) |  |
    | total_owner_equities | 所有者权益（或股东权益）合计 | decimal(20,4) |  |
    | total_sheet_owner_equities | 负债和所有者权益（或股东权益）合计 | decimal(20,4) |  |
    | other_comprehensive_income | 其他综合收益 | decimal(20,4) |  |
    | deferred_earning | 递延收益-非流动负债 | decimal(20,4) |  |
    | settlement_provi | 结算备付金 | decimal(20,4) |  |
    | lend_capital | 拆出资金 | decimal(20,4) |  |
    | loan_and_advance_current_assets | 发放贷款及垫款-流动资产 | decimal(20,4) |  |
    | derivative_financial_asset | 衍生金融资产 | decimal(20,4) |  |
    | insurance_receivables | 应收保费 | decimal(20,4) |  |
    | reinsurance_receivables | 应收分保账款 | decimal(20,4) |  |
    | reinsurance_contract_reserves_receivable | 应收分保合同准备金 | decimal(20,4) |  |
    | bought_sellback_assets | 买入返售金融资产 | decimal(20,4) |  |
    | hold_sale_asset | 划分为持有待售的资产 | decimal(20,4) |  |
    | loan_and_advance_noncurrent_assets | 发放贷款及垫款-非流动资产 | decimal(20,4) |  |
    | borrowing_from_centralbank | 向中央银行借款 | decimal(20,4) |  |
    | deposit_in_interbank | 吸收存款及同业存放 | decimal(20,4) |  |
    | borrowing_capital | 拆入资金 | decimal(20,4) |  |
    | derivative_financial_liability | 衍生金融负债 | decimal(20,4) |  |
    | sold_buyback_secu_proceeds | 卖出回购金融资产款 | decimal(20,4) |  |
    | commission_payable | 应付手续费及佣金 | decimal(20,4) |  |
    | reinsurance_payables | 应付分保账款 | decimal(20,4) |  |
    | insurance_contract_reserves | 保险合同准备金 | decimal(20,4) |  |
    | proxy_secu_proceeds | 代理买卖证券款 | decimal(20,4) |  |
    | receivings_from_vicariously_sold_securities | 代理承销证券款 | decimal(20,4) |  |
    | hold_sale_liability | 划分为持有待售的负债 | decimal(20,4) |  |
    | estimate_liability_current | 预计负债-流动负债 | decimal(20,4) |  |
    | deferred_earning_current | 递延收益-流动负债 | decimal(20,4) |  |
    | preferred_shares_noncurrent | 优先股-非流动负债 | decimal(20,4) |  |
    | pepertual_liability_noncurrent | 永续债-非流动负债 | decimal(20,4) |  |
    | longterm_salaries_payable | 长期应付职工薪酬 | decimal(20,4) |  |
    | other_equity_tools | 其他权益工具 | decimal(20,4) |  |
    | preferred_shares_equity | 其中：优先股-所有者权益 | decimal(20,4) |  |
    | pepertual_liability_equity | 永续债-所有者权益 | decimal(20,4) |  |
    | other_current_assets | 其他流动资产 | decimal(20,4) |  |
    | other_non_current_assets | 其他非流动资产 | decimal(20,4) |  |
    | other_current_liability | 其他流动负债 | decimal(20,4) |  |
    | other_non_current_liability | 其他非流动负债 | decimal(20,4) |  |
    | ordinary_risk_reserve_fund | 一般风险准备 | decimal(20,4) |  |
    | contract_assets | 合同资产 | decimal(20,4) |  |
    | bond_invest | 债权投资 | decimal(20,4) |  |
    | other_bond_invest | 其他债权投资 | decimal(20,4) |  |
    | other_equity_tools_invest | 其他权益工具投资 | decimal(20,4) |  |
    | other_non_current_financial_assets | 其他非流动金融资产 | decimal(20,4) |  |
    | contract_liability | 合同负债 | decimal(20,4) |  |
    | receivable_fin | 应收款项融资 | decimal(20,4) |  |
    | usufruct_assets | 使用权资产 | decimal(20,4) |  |
    | bill_and_account_payable | 应付票据及应付账款 | decimal(20,4) |  |
    | bill_and_account_receivable | 应收票据及应收账款 | decimal(20,4) |  |
    | lease_liability | 租赁负债 | decimal(20,4) |  |
    
- **报表来源编码**
    
    | 编码 | 名称 |
    | --- | --- |
    | 321001 | 招募说明书 |
    | 321002 | 上市公告书 |
    | 321003 | 定期报告 |
    | 321004 | 预披露公告 |
    | 321005 | 换股报告书 |
    | 321099 | 其他 |
    
- **filter(finance.STK_BALANCE_SHEET.code==code)**：指定筛选条件，通过finance.STK_BALANCE_SHEET.code==code可以指定你想要查询的股票代码；除此之外，还可以对表中其他字段指定筛选条件，如finance.STK_BALANCE_SHEET.pub_date>='2015-01-01'，表示公告日期大于2015年1月1日上市公司公布的合并资产负债表信息；多个筛选条件用英文逗号分隔。
    
- **limit(n)**：限制返回的数据条数，n指定返回条数。
    

**返回结果：**

- 返回一个 dataframe，每一行对应数据表中的一条数据， 列索引是你所查询的字段名称

**注意：**

1.  **为了防止返回数据量过大, 我们每次最多返回4000行**
2.  不能进行连表查询，即同时查询多张表的数据

**示例：**

```python
#查询贵州茅台2015年之后公告的合并资产负债表数据，取出本期的货币资金，总资产和总负债
from jqdata import *
q=query(finance.STK_BALANCE_SHEET.company_name,
        finance.STK_BALANCE_SHEET.code,
        finance.STK_BALANCE_SHEET.pub_date,
        finance.STK_BALANCE_SHEET.start_date,
        finance.STK_BALANCE_SHEET.end_date,
        finance.STK_BALANCE_SHEET.cash_equivalents,
        finance.STK_BALANCE_SHEET.total_assets,
        finance.STK_BALANCE_SHEET.total_liability
).filter(finance.STK_BALANCE_SHEET.code=='600519.XSHG',finance.STK_BALANCE_SHEET.pub_date>='2015-01-01',finance.STK_BALANCE_SHEET.report_type==0).limit(20)
df=finance.run_query(q)
print(df)

   company_name         code    pub_date  start_date    end_date  \
0   贵州茅台酒股份有限公司  600519.XSHG  2015-04-21  2014-01-01  2014-12-31
1   贵州茅台酒股份有限公司  600519.XSHG  2015-04-21  2015-01-01  2015-03-31
2   贵州茅台酒股份有限公司  600519.XSHG  2015-08-28  2015-01-01  2015-06-30
3   贵州茅台酒股份有限公司  600519.XSHG  2015-10-23  2015-01-01  2015-09-30
4   贵州茅台酒股份有限公司  600519.XSHG  2016-03-24  2015-01-01  2015-12-31
5   贵州茅台酒股份有限公司  600519.XSHG  2016-04-21  2016-01-01  2016-03-31
6   贵州茅台酒股份有限公司  600519.XSHG  2016-08-27  2016-01-01  2016-06-30
7   贵州茅台酒股份有限公司  600519.XSHG  2016-10-29  2016-01-01  2016-09-30
8   贵州茅台酒股份有限公司  600519.XSHG  2017-04-15  2016-01-01  2016-12-31
9   贵州茅台酒股份有限公司  600519.XSHG  2017-04-25  2017-01-01  2017-03-31
10  贵州茅台酒股份有限公司  600519.XSHG  2017-07-28  2017-01-01  2017-06-30
11  贵州茅台酒股份有限公司  600519.XSHG  2017-10-26  2017-01-01  2017-09-30
12  贵州茅台酒股份有限公司  600519.XSHG  2018-03-28  2017-01-01  2017-12-31
13  贵州茅台酒股份有限公司  600519.XSHG  2018-04-28  2018-01-01  2018-03-31
14  贵州茅台酒股份有限公司  600519.XSHG  2018-08-02  2018-01-01  2018-06-30

    cash_equivalents  total_assets  total_liability
0       2.771072e+10  6.587317e+10     1.056161e+10
1       2.842068e+10  6.876902e+10     8.838873e+09
2       3.023650e+10  7.233774e+10     8.675962e+09
3       3.053612e+10  7.755903e+10     1.564019e+10
4       3.680075e+10  8.630146e+10     2.006729e+10
5       4.377574e+10  9.069045e+10     1.974919e+10
6       4.752806e+10  9.554650e+10     2.819334e+10
7       6.199974e+10  1.051460e+11     3.386253e+10
8       6.685496e+10  1.129345e+11     3.703600e+10
9       7.270833e+10  1.189787e+11     3.652483e+10
10      7.363535e+10  1.203827e+11     4.131949e+10
11      8.096468e+10  1.277800e+11     3.939919e+10
12      8.786887e+10  1.346101e+11     3.859049e+10
13      8.721137e+10  1.344049e+11     2.925526e+10
14      8.366017e+10  1.299148e+11     3.341036e+10
```

### 母公司资产负债表

```
from jqdata import finance
finance.run_query(query(finance.STK_BALANCE_SHEET_PARENT).filter(finance.STK_BALANCE_SHEET_PARENT.code==code).limit(n))
```

获取上市公司定期公告中公布的母公司资产负债表（2007版）

**参数：**

- **query(finance.STK_BALANCE_SHEET_PARENT)**：表示从finance.STK_BALANCE_SHEET_PARENT这张表中查询上市公司定期公告中公布的母公司资产负债表信息，还可以指定所要查询的字段名，格式如下：query(库名.表名.字段名1，库名.表名.字段名2），多个字段用逗号分隔进行提取；query函数的更多用法详见：[sqlalchemy.orm.query.Query对象](http://docs.sqlalchemy.org/en/rel_1_0/orm/query.html)
    
- **finance.STK_BALANCE_SHEET_PARENT**：代表上市公司母公司资产负债表信息，收录了上市公司定期公告中公布的母公司资产负债表数据，表结构和字段信息如下：
    
    | 字段名称 | 中文名称 | 字段类型 | 含义 |
    | --- | --- | --- | --- |
    | company_id | 公司ID | int |  |
    | company_name | 公司名称 | varchar(100) |  |
    | code | 股票代码 | varchar(12) |  |
    | a_code | A股代码 | varchar(12) |  |
    | b_code | B股代码 | varchar(12) |  |
    | h_code | H股代码 | varchar(12) |  |
    | pub_date | 公告日期 | date |  |
    | end_date | 截止日期 | date |  |
    | report_date | 报告期 | date |  |
    | report_type | 报告期类型 | int | 0本期，1上期 |
    | source_id | 报表来源编码 | int | 如下[报表来源编码](#source6) |
    | source | 报表来源 | varchar(60) |  |
    | cash_equivalents | 货币资金 | decimal(20,4) |  |
    | trading_assets | 交易性金融资产 | decimal(20,4) |  |
    | bill_receivable | 应收票据 | decimal(20,4) |  |
    | account_receivable | 应收账款 | decimal(20,4) |  |
    | advance_payment | 预付款项 | decimal(20,4) |  |
    | other_receivable | 其他应收款 | decimal(20,4) |  |
    | affiliated_company_receivable | 应收关联公司款 | decimal(20,4) |  |
    | interest_receivable | 应收利息 | decimal(20,4) |  |
    | dividend_receivable | 应收股利 | decimal(20,4) |  |
    | inventories | 存货 | decimal(20,4) |  |
    | expendable_biological_asset | 消耗性生物资产 | decimal(20,4) | 消耗性生物资产，是指为出售而持有的、或在将来收获为农产品的[生物资产](http://wiki.mbalib.com/wiki/%E7%94%9F%E7%89%A9%E8%B5%84%E4%BA%A7)，包括生长中的大田作物、蔬菜、[用材林](http://wiki.mbalib.com/wiki/%E7%94%A8%E6%9D%90%E6%9E%97)以及存栏代售的牲畜等 |
    | non_current_asset_in_one_year | 一年内到期的非流动资产 | decimal(20,4) |  |
    | total_current_assets | 流动资产合计 | decimal(20,4) |  |
    | hold_for_sale_assets | 可供出售金融资产 | decimal(20,4) |  |
    | hold_to_maturity_investments | 持有至到期投资 | decimal(20,4) |  |
    | longterm_receivable_account | 长期应收款 | decimal(20,4) |  |
    | longterm_equity_invest | 长期股权投资 | decimal(20,4) |  |
    | investment_property | 投资性房地产 | decimal(20,4) |  |
    | fixed_assets | 固定资产 | decimal(20,4) |  |
    | constru_in_process | 在建工程 | decimal(20,4) |  |
    | construction_materials | 工程物资 | decimal(20,4) |  |
    | fixed_assets_liquidation | 固定资产清理 | decimal(20,4) |  |
    | biological_assets | 生产性生物资产 | decimal(20,4) |  |
    | oil_gas_assets | 油气资产 | decimal(20,4) |  |
    | intangible_assets | 无形资产 | decimal(20,4) |  |
    | development_expenditure | 开发支出 | decimal(20,4) |  |
    | good_will | 商誉 | decimal(20,4) |  |
    | long_deferred_expense | 长期待摊费用 | decimal(20,4) |  |
    | deferred_tax_assets | 递延所得税资产 | decimal(20,4) |  |
    | total_non_current_assets | 非流动资产合计 | decimal(20,4) |  |
    | total_assets | 资产总计 | decimal(20,4) |  |
    | shortterm_loan | 短期借款 | decimal(20,4) |  |
    | trading_liability | 交易性金融负债 | decimal(20,4) |  |
    | notes_payable | 应付票据 | decimal(20,4) |  |
    | accounts_payable | 应付账款 | decimal(20,4) |  |
    | advance_peceipts | 预收款项 | decimal(20,4) |  |
    | salaries_payable | 应付职工薪酬 | decimal(20,4) |  |
    | taxs_payable | 应交税费 | decimal(20,4) |  |
    | interest_payable | 应付利息 | decimal(20,4) |  |
    | dividend_payable | 应付股利 | decimal(20,4) |  |
    | other_payable | 其他应付款 | decimal(20,4) |  |
    | affiliated_company_payable | 应付关联公司款 | decimal(20,4) |  |
    | non_current_liability_in_one_year | 一年内到期的非流动负债 | decimal(20,4) |  |
    | total_current_liability | 流动负债合计 | decimal(20,4) |  |
    | longterm_loan | 长期借款 | decimal(20,4) |  |
    | bonds_payable | 应付债券 | decimal(20,4) |  |
    | longterm_account_payable | 长期应付款 | decimal(20,4) |  |
    | specific_account_payable | 专项应付款 | decimal(20,4) |  |
    | estimate_liability | 预计负债 | decimal(20,4) |  |
    | deferred_tax_liability | 递延所得税负债 | decimal(20,4) |  |
    | total_non_current_liability | 非流动负债合计 | decimal(20,4) |  |
    | total_liability | 负债合计 | decimal(20,4) |  |
    | paidin_capital | 实收资本（或股本） | decimal(20,4) |  |
    | capital_reserve_fund | 资本公积 | decimal(20,4) |  |
    | specific_reserves | 专项储备 | decimal(20,4) |  |
    | surplus_reserve_fund | 盈余公积 | decimal(20,4) |  |
    | treasury_stock | 库存股 | decimal(20,4) |  |
    | retained_profit | 未分配利润 | decimal(20,4) |  |
    | equities_parent_company_owners | 归属于母公司所有者权益 | decimal(20,4) |  |
    | minority_interests | 少数股东权益 | decimal(20,4) |  |
    | foreign_currency_report_conv_diff | 外币报表折算价差 | decimal(20,4) |  |
    | irregular_item_adjustment | 非正常经营项目收益调整 | decimal(20,4) |  |
    | total_owner_equities | 所有者权益（或股东权益）合计 | decimal(20,4) |  |
    | total_sheet_owner_equities | 负债和所有者权益（或股东权益）合计 | decimal(20,4) |  |
    | other_comprehensive_income | 其他综合收益 | decimal(20,4) |  |
    | deferred_earning | 递延收益-非流动负债 | decimal(20,4) |  |
    | settlement_provi | 结算备付金 | decimal(20,4) |  |
    | lend_capital | 拆出资金 | decimal(20,4) |  |
    | loan_and_advance_current_assets | 发放贷款及垫款-流动资产 | decimal(20,4) |  |
    | derivative_financial_asset | 衍生金融资产 | decimal(20,4) |  |
    | insurance_receivables | 应收保费 | decimal(20,4) |  |
    | reinsurance_receivables | 应收分保账款 | decimal(20,4) |  |
    | reinsurance_contract_reserves_receivable | 应收分保合同准备金 | decimal(20,4) |  |
    | bought_sellback_assets | 买入返售金融资产 | decimal(20,4) |  |
    | hold_sale_asset | 划分为持有待售的资产 | decimal(20,4) |  |
    | loan_and_advance_noncurrent_assets | 发放贷款及垫款-非流动资产 | decimal(20,4) |  |
    | borrowing_from_centralbank | 向中央银行借款 | decimal(20,4) |  |
    | deposit_in_interbank | 吸收存款及同业存放 | decimal(20,4) |  |
    | borrowing_capital | 拆入资金 | decimal(20,4) |  |
    | derivative_financial_liability | 衍生金融负债 | decimal(20,4) |  |
    | sold_buyback_secu_proceeds | 卖出回购金融资产款 | decimal(20,4) |  |
    | commission_payable | 应付手续费及佣金 | decimal(20,4) |  |
    | reinsurance_payables | 应付分保账款 | decimal(20,4) |  |
    | insurance_contract_reserves | 保险合同准备金 | decimal(20,4) |  |
    | proxy_secu_proceeds | 代理买卖证券款 | decimal(20,4) |  |
    | receivings_from_vicariously_sold_securities | 代理承销证券款 | decimal(20,4) |  |
    | hold_sale_liability | 划分为持有待售的负债 | decimal(20,4) |  |
    | estimate_liability_current | 预计负债-流动负债 | decimal(20,4) |  |
    | deferred_earning_current | 递延收益-流动负债 | decimal(20,4) |  |
    | preferred_shares_noncurrent | 优先股-非流动负债 | decimal(20,4) |  |
    | pepertual_liability_noncurrent | 永续债-非流动负债 | decimal(20,4) |  |
    | longterm_salaries_payable | 长期应付职工薪酬 | decimal(20,4) |  |
    | other_equity_tools | 其他权益工具 | decimal(20,4) |  |
    | preferred_shares_equity | 其中：优先股-所有者权益 | decimal(20,4) |  |
    | pepertual_liability_equity | 永续债-所有者权益 | decimal(20,4) |  |
    | other_current_assets | 其他流动资产 | decimal(20,4) |  |
    | other_non_current_assets | 其他非流动资产 | decimal(20,4) |  |
    | other_current_liability | 其他流动负债 | decimal(20,4) |  |
    | other_non_current_liability | 其他非流动负债 | decimal(20,4) |  |
    | ordinary_risk_reserve_fund | 一般风险准备 | decimal(20,4) |  |
    | contract_assets | 合同资产 | decimal(20,4) |  |
    | bond_invest | 债权投资 | decimal(20,4) |  |
    | other_bond_invest | 其他债权投资 | decimal(20,4) |  |
    | other_equity_tools_invest | 其他权益工具投资 | decimal(20,4) |  |
    | other_non_current_financial_assets | 其他非流动金融资产 | decimal(20,4) |  |
    | contract_liability | 合同负债 | decimal(20,4) |  |
    | receivable_fin | 应收款项融资 | decimal(20,4) |  |
    | usufruct_assets | 使用权资产 | decimal(20,4) |  |
    | bill_and_account_payable | 应付票据及应付账款 | decimal(20,4) |  |
    | bill_and_account_receivable | 应收票据及应收账款 | decimal(20,4) |  |
    | lease_liability | 租赁负债 | decimal(20,4) |  |
    
- **报表来源编码**
    
    | 编码 | 名称 |
    | --- | --- |
    | 321001 | 招募说明书 |
    | 321002 | 上市公告书 |
    | 321003 | 定期报告 |
    | 321004 | 预披露公告 |
    | 321005 | 换股报告书 |
    | 321099 | 其他 |
    
- **filter(finance.STK_BALANCE_SHEET_PARENT.code==code)**：指定筛选条件，通过finance.STK_BALANCE_SHEET_PARENT.code==code可以指定你想要查询的股票代码；除此之外，还可以对表中其他字段指定筛选条件，如finance.STK_BALANCE_SHEET_PARENT.pub_date>='2015-01-01'，表示公告日期大于2015年1月1日上市公司公布的母公司资产负债表信息；多个筛选条件用英文逗号分隔。
    
- **limit(n)**：限制返回的数据条数，n指定返回条数。
    

**返回结果：**

- 返回一个 dataframe，每一行对应数据表中的一条数据， 列索引是你所查询的字段名称

**注意：**

1.  **为了防止返回数据量过大, 我们每次最多返回4000行**
2.  不能进行连表查询，即同时查询多张表的数据

**示例：**

```python
#查询贵州茅台2015年之后公告的母公司资产负债表数据，取出本期的货币资金，总资产和总负债
from jqdata import *
q=query(finance.STK_BALANCE_SHEET_PARENT.company_name,
        finance.STK_BALANCE_SHEET_PARENT.code,
        finance.STK_BALANCE_SHEET_PARENT.pub_date,
        finance.STK_BALANCE_SHEET_PARENT.start_date,
        finance.STK_BALANCE_SHEET_PARENT.end_date,
        finance.STK_BALANCE_SHEET_PARENT.cash_equivalents,
        finance.STK_BALANCE_SHEET_PARENT.total_assets,
        finance.STK_BALANCE_SHEET_PARENT.total_liability
).filter(finance.STK_BALANCE_SHEET_PARENT.code=='600519.XSHG',finance.STK_BALANCE_SHEET_PARENT.pub_date>='2015-01-01',finance.STK_BALANCE_SHEET_PARENT.report_type==0).limit(20)
df=finance.run_query(q)
print(df)

   company_name         code    pub_date  start_date    end_date  \
0   贵州茅台酒股份有限公司  600519.XSHG  2015-04-21  2014-01-01  2014-12-31
1   贵州茅台酒股份有限公司  600519.XSHG  2015-04-21  2015-01-01  2015-03-31
2   贵州茅台酒股份有限公司  600519.XSHG  2015-08-28  2015-01-01  2015-06-30
3   贵州茅台酒股份有限公司  600519.XSHG  2015-10-23  2015-01-01  2015-09-30
4   贵州茅台酒股份有限公司  600519.XSHG  2016-03-24  2015-01-01  2015-12-31
5   贵州茅台酒股份有限公司  600519.XSHG  2016-04-21  2016-01-01  2016-03-31
6   贵州茅台酒股份有限公司  600519.XSHG  2016-08-27  2016-01-01  2016-06-30
7   贵州茅台酒股份有限公司  600519.XSHG  2016-10-29  2016-01-01  2016-09-30
8   贵州茅台酒股份有限公司  600519.XSHG  2017-04-15  2016-01-01  2016-12-31
9   贵州茅台酒股份有限公司  600519.XSHG  2017-04-25  2017-01-01  2017-03-31
10  贵州茅台酒股份有限公司  600519.XSHG  2017-07-28  2017-01-01  2017-06-30
11  贵州茅台酒股份有限公司  600519.XSHG  2017-10-26  2017-01-01  2017-09-30
12  贵州茅台酒股份有限公司  600519.XSHG  2018-03-28  2017-01-01  2017-12-31
13  贵州茅台酒股份有限公司  600519.XSHG  2018-04-28  2018-01-01  2018-03-31
14  贵州茅台酒股份有限公司  600519.XSHG  2018-08-02  2018-01-01  2018-06-30

    cash_equivalents  total_assets  total_liability
0       1.070530e+10  4.662489e+10     1.693767e+10
1       1.165218e+10  4.903731e+10     1.940782e+10
2       1.239635e+10  5.079041e+10     2.125881e+10
3       8.754779e+09  5.396424e+10     1.979558e+10
4       1.505296e+10  5.512518e+10     2.082189e+10
5       1.574722e+10  6.608276e+10     2.292887e+10
6       1.898219e+10  6.186466e+10     2.658035e+10
7       1.540346e+10  5.697338e+10     2.241995e+10
8       1.651317e+10  5.966072e+10     2.385817e+10
9       1.407649e+10  5.863382e+10     2.180735e+10
10      1.455895e+10  6.757545e+10     3.133084e+10
11      1.520003e+10  6.220742e+10     2.418794e+10
12      1.553456e+10  6.507375e+10     2.699755e+10
13      1.467512e+10  6.102503e+10     2.200076e+10
14      1.495389e+10  7.800655e+10     2.929751e+09
```

### 金融类合并利润表

#### 金融类合并利润表2007版

```
from jqdata import finance
finance.run_query(query(finance.FINANCE_INCOME_STATEMENT).filter(finance.FINANCE_INCOME_STATEMENT.code==code).limit(n))
```

获取金融类上市公司的合并利润表信息

**参数：**

- **query(finance.FINANCE_INCOME_STATEMENT)**：表示从finance.FINANCE_INCOME_STATEMENT这张表中查询金融类上市公司合并利润表的字段信息，还可以指定所要查询的字段名，格式如下：query(库名.表名.字段名1，库名.表名.字段名2），多个字段用逗号分隔进行提取；query函数的更多用法详见：[sqlalchemy.orm.query.Query对象](http://docs.sqlalchemy.org/en/rel_1_0/orm/query.html)
    
- **finance.FINANCE_INCOME_STATEMENT**：代表金融类上市公司合并利润表，收录了金融类上市公司的合并利润表，表结构和字段信息如下：
    
    | 字段名称 | 中文名称 | 字段类型 | 含义 |
    | --- | --- | --- | --- |
    | company_id | 公司ID | int |  |
    | company_name | 公司名称 | varchar(100) |  |
    | code | 公司主证券代码 | varchar(12) |  |
    | a_code | A股代码 | varchar(12) |  |
    | b_code | B股代码 | varchar(12) |  |
    | h_code | H股代码 | varchar(12) |  |
    | pub_date | 公告日期 | date |  |
    | start_date | 开始日期 | date |  |
    | end_date | 截止日期 | date |  |
    | report_date | 报告期 | date |  |
    | report_type | 报告期类型 | int | 0本期，1上期 |
    | source_id | 报表来源编码 | int | 如下[报表来源编码](#source7) |
    | source | 报表来源 | varchar(60) |  |
    | operating_revenue | 营业收入 | decimal(20,4) |  |
    | interest_net_revenue | 利息净收入 | decimal(20,4) |  |
    | interest_income | 利息收入 | decimal(20,4) |  |
    | interest_expense | 利息支出 | decimal(20,4) |  |
    | commission_net_income | 手续费及佣金净收入 | decimal(20,4) |  |
    | commission_income | 手续费及佣金收入 | decimal(20,4) |  |
    | commission_expense | 手续费及佣金支出 | decimal(20,4) |  |
    | agent_security_income | 代理买卖证券业务净收入 | decimal(20,4) |  |
    | sell_security_income | 证券承销业务净收入 | decimal(20,4) |  |
    | manage_income | 委托客户管理资产业务净收入 | decimal(20,4) |  |
    | premiums_earned | 已赚保费 | decimal(20,4) |  |
    | assurance_income | 保险业务收入 | decimal(20,4) |  |
    | premiums_income | 分保费收入 | decimal(20,4) |  |
    | premiums_expense | 分出保费 | decimal(20,4) |  |
    | prepare_money | 提取未到期责任准备金 | decimal(20,4) |  |
    | investment_income | 投资收益 | decimal(20,4) |  |
    | invest_income_associates | 对联营企业和合营企业的投资收益 | decimal(20,4) |  |
    | fair_value_variable_income | 公允价值变动收益 | decimal(20,4) |  |
    | exchange_income | 汇兑收益 | decimal(20,4) |  |
    | other_income | 其他业务收入 | decimal(20,4) |  |
    | operation_expense | 营业支出 | decimal(20,4) |  |
    | refunded_premiums | 退保金 | decimal(20,4) |  |
    | compensate_loss | 赔付支出 | decimal(20,4) |  |
    | compensation_back | 摊回赔付支出 | decimal(20,4) |  |
    | insurance_reserve | 提取保险责任准备金 | decimal(20,4) |  |
    | insurance_reserve_back | 摊回保险责任准备金 | decimal(20,4) |  |
    | policy_dividend_payout | 保单红利支出 | decimal(20,4) |  |
    | reinsurance_cost | 分保费用 | decimal(20,4) |  |
    | operating_tax_surcharges | 营业税金及附加 | decimal(20,4) |  |
    | commission_expense2 | 手续费及佣金支出(保险专用) | decimal(20,4) |  |
    | operation_manage_fee | 业务及管理费 | decimal(20,4) |  |
    | separate_fee | 摊回分保费用 | decimal(20,4) |  |
    | asset_impairment_loss | 资产减值损失 | decimal(20,4) |  |
    | other_cost | 其他业务成本 | decimal(20,4) |  |
    | operating_profit | 营业利润 | decimal(20,4) |  |
    | subsidy_income | 补贴收入 | decimal(20,4) |  |
    | non_operating_revenue | 营业外收入 | decimal(20,4) |  |
    | non_operating_expense | 营业外支出 | decimal(20,4) |  |
    | other_items_influenced_profit | 影响利润总额的其他科目 | decimal(20,4) |  |
    | total_profit | 利润总额 | decimal(20,4) |  |
    | income_tax_expense | 所得税费用 | decimal(20,4) |  |
    | other_influence_net_profit | 影响净利润的其他科目 | decimal(20,4) |  |
    | net_profit | 净利润 | decimal(20,4) |  |
    | np_parent_company_owners | 归属于母公司股东的净利润 | decimal(20,4) |  |
    | minority_profit | 少数股东损益 | decimal(20,4) |  |
    | eps | 每股收益 | decimal(20,4) |  |
    | basic_eps | 基本每股收益 | decimal(20,4) |  |
    | diluted_eps | 稀释每股收益 | decimal(20,4) |  |
    | other_composite_income | 其他综合收益 | decimal(20,4) |  |
    | total_composite_income | 综合收益总额 | decimal(20,4) |  |
    | ci_parent_company_owners | 归属于母公司的综合收益 | decimal(20,4) |  |
    | ci_minority_owners | 归属于少数股东的综合收益 | decimal(20,4) |  |
    | other_earnings | 其他收益 | decimal(20,4) |  |
    | asset_deal_income | 资产处置收益 | decimal(20,4) |  |
    | sust_operate_net_profit | 持续经营净利润 | decimal(20,4) |  |
    | discon_operate_net_profit | 终止经营净利润 | decimal(20,4) |  |
    | credit_impairment_loss | 信用减值损失 | decimal(20,4) |  |
    
- **报表来源编码**
    
    | 编码 | 名称 |
    | --- | --- |
    | 321001 | 招募说明书 |
    | 321002 | 上市公告书 |
    | 321003 | 定期报告 |
    | 321004 | 预披露公告 |
    | 321005 | 换股报告书 |
    | 321099 | 其他 |
    
- filter(finance.FINANCE_INCOME_STATEMENT.code==code)**：指定筛选条件，通过finance.FINANCE_INCOME_STATEMENT.code==code可以指定你想要查询的股票代码；除此之外，还可以对表中其他字段指定筛选条件，如finance.FINANCE_INCOME_STATEMENT.pub_date>='2015-01-01'，表示公告日期大于2015年1月1日金融类上市公司公布的合并利润表信息；多个筛选条件用英文逗号分隔。
    
- **limit(n)**：限制返回的数据条数，n指定返回条数。
    

**返回结果：**

- 返回一个 dataframe，每一行对应数据表中的一条数据， 列索引是你所查询的字段名称

**注意：**

1.  **为了防止返回数据量过大, 我们每次最多返回4000行**
2.  不能进行连表查询，即同时查询多张表的数据

**示例：**

```
#查询中国平安2015年之后公告的合并利润表数据,指定只取出本期数据
from jqdata import finance
q=query(finance.FINANCE_INCOME_STATEMENT).filter(finance.FINANCE_INCOME_STATEMENT.code=='601318.XSHG',finance.FINANCE_INCOME_STATEMENT.pub_date>='2015-01-01',finance.FINANCE_INCOME_STATEMENT.report_type==0).limit(10)
df=finance.run_query(q)
print(df)

      id  company_id      company_name         code  a_code b_code h_code  \
0    246   300002221  中国平安保险(集团)股份有限公司  601318.XSHG  601318   None  02318
1    248   300002221  中国平安保险(集团)股份有限公司  601318.XSHG  601318   None  02318
2    250   300002221  中国平安保险(集团)股份有限公司  601318.XSHG  601318   None  02318
3    252   300002221  中国平安保险(集团)股份有限公司  601318.XSHG  601318   None  02318
4    254   300002221  中国平安保险(集团)股份有限公司  601318.XSHG  601318   None  02318
5    256   300002221  中国平安保险(集团)股份有限公司  601318.XSHG  601318   None  02318
6    258   300002221  中国平安保险(集团)股份有限公司  601318.XSHG  601318   None  02318
7    260   300002221  中国平安保险(集团)股份有限公司  601318.XSHG  601318   None  02318
8    262   300002221  中国平安保险(集团)股份有限公司  601318.XSHG  601318   None  02318
9    264   300002221  中国平安保险(集团)股份有限公司  601318.XSHG  601318   None  02318
10   265   300002221  中国平安保险(集团)股份有限公司  601318.XSHG  601318   None  02318
11   266   300002221  中国平安保险(集团)股份有限公司  601318.XSHG  601318   None  02318
12   267   300002221  中国平安保险(集团)股份有限公司  601318.XSHG  601318   None  02318
13  4189   300002221  中国平安保险(集团)股份有限公司  601318.XSHG  601318   None  02318
14  4333   300002221  中国平安保险(集团)股份有限公司  601318.XSHG  601318   None  02318

      pub_date  start_date    end_date         ...           net_profit  \
0   2015-03-20  2014-01-01  2014-12-31         ...          47930000000
1   2015-04-30  2015-01-01  2015-03-31         ...          22436000000
2   2015-08-21  2015-01-01  2015-06-30         ...          39911000000
3   2015-10-28  2015-01-01  2015-09-30         ...          56405000000
4   2016-03-16  2015-01-01  2015-12-31         ...          65178000000
5   2016-04-27  2016-01-01  2016-03-31         ...          23389000000
6   2016-08-18  2016-01-01  2016-06-30         ...          46308000000
7   2016-10-28  2016-01-01  2016-09-30         ...          64813000000
8   2017-03-23  2016-01-01  2016-12-31         ...          72368000000
9   2017-04-28  2017-01-01  2017-03-31         ...          25740000000
10  2017-08-18  2017-01-01  2017-06-30         ...          49093000000
11  2017-10-28  2017-01-01  2017-09-30         ...          75219000000
12  2018-03-21  2017-01-01  2017-12-31         ...          99978000000
13  2018-04-27  2018-01-01  2018-03-31         ...          28951000000
14  2018-08-22  2018-01-01  2018-06-30         ...          64770000000

    np_parent_company_owners  minority_profit  eps  basic_eps  diluted_eps  \
0                39279000000       8651000000  NaN       4.93         4.68
1                19964000000       2472000000  NaN       2.19         2.19
2                34649000000       5262000000  NaN       1.90         1.90
3                48276000000       8129000000  NaN       2.64         2.64
4                54203000000      10975000000  NaN       2.98         2.98
5                20700000000       2689000000  NaN       1.16         1.16
6                40776000000       5532000000  NaN       2.28         2.28
7                56508000000       8305000000  NaN       3.17         3.16
8                62394000000       9974000000  NaN       3.50         3.49
9                23053000000       2687000000  NaN       1.29         1.29
10               43427000000       5666000000  NaN       2.43         2.43
11               66318000000       8901000000  NaN       3.72         3.71
12               89088000000      10890000000  NaN       4.99         4.99
13               25702000000       3249000000  NaN       1.44         1.44
14               58095000000       6675000000  NaN       3.26         3.25

    other_composite_income  total_composite_income  ci_parent_company_owners  \
0              30774000000            7.870400e+10              6.959000e+10
1              -3572000000            1.886400e+10              1.633600e+10
2                 71000000            3.998200e+10              3.450800e+10
3             -13161000000            4.324400e+10              3.488100e+10
4                752000000            6.593000e+10              5.456500e+10
5             -11246000000            1.214300e+10              9.509000e+09
6              -9129000000            3.717900e+10              3.167900e+10
7              -5917000000            5.889600e+10              5.050300e+10
8              -7567000000            6.480100e+10              5.471000e+10
9               6311000000            3.205100e+10              2.923600e+10
10              9927000000            5.902000e+10              5.315300e+10
11             17846000000            9.306500e+10              8.369900e+10
12             21881000000            1.218590e+11              1.106720e+11
13              -658000000            2.829300e+10              2.481100e+10
14               130000000            6.490000e+10              5.787400e+10

    ci_minority_owners
0           9114000000
1           2528000000
2           5474000000
3           8363000000
4          11365000000
5           2634000000
6           5500000000
7           8393000000
8          10091000000
9           2815000000
10          5867000000
11          9366000000
12         11187000000
13          3482000000
14          7026000000

[15 rows x 66 columns]
```

### 金融类母公司利润表

```
from jqdata import finance
finance.run_query(query(finance.FINANCE_INCOME_STATEMENT_PARENT).filter(finance.FINANCE_INCOME_STATEMENT_PARENT.code==code).limit(n))
```

获取金融类上市公司的母公司利润表信息

**参数：**

- **query(finance.FINANCE_INCOME_STATEMENT_PARENT)**：表示从finance.FINANCE_INCOME_STATEMENT_PARENT这张表中查询金融类上市公司母公司利润表的字段信息，还可以指定所要查询的字段名，格式如下：query(库名.表名.字段名1，库名.表名.字段名2），多个字段用逗号分隔进行提取；query函数的更多用法详见：[sqlalchemy.orm.query.Query对象](http://docs.sqlalchemy.org/en/rel_1_0/orm/query.html)
    
- **finance.FINANCE_INCOME_STATEMENT_PARENT**：代表金融类上市公司母公司利润表，收录了金融类上市公司的母公司利润表，表结构和字段信息如下：
    
    | 字段名称 | 中文名称 | 字段类型 | 含义 |
    | --- | --- | --- | --- |
    | company_id | 公司ID | int |  |
    | company_name | 公司名称 | varchar(100) |  |
    | code | 公司主证券代码 | varchar(12) |  |
    | a_code | A股代码 | varchar(12) |  |
    | b_code | B股代码 | varchar(12) |  |
    | h_code | H股代码 | varchar(12) |  |
    | pub_date | 公告日期 | date |  |
    | start_date | 开始日期 | date |  |
    | end_date | 截止日期 | date |  |
    | report_date | 报告期 | date |  |
    | report_type | 报告期类型 | int | 0本期，1上期 |
    | source_id | 报表来源编码 | int | 如下[报表来源编码](#source8) |
    | source | 报表来源 | varchar(60) |  |
    | operating_revenue | 营业收入 | decimal(20,4) |  |
    | interest_net_revenue | 利息净收入 | decimal(20,4) |  |
    | interest_income | 利息收入 | decimal(20,4) |  |
    | interest_expense | 利息支出 | decimal(20,4) |  |
    | commission_net_income | 手续费及佣金净收入 | decimal(20,4) |  |
    | commission_income | 手续费及佣金收入 | decimal(20,4) |  |
    | commission_expense | 手续费及佣金支出 | decimal(20,4) |  |
    | agent_security_income | 代理买卖证券业务净收入 | decimal(20,4) |  |
    | sell_security_income | 证券承销业务净收入 | decimal(20,4) |  |
    | manage_income | 委托客户管理资产业务净收入 | decimal(20,4) |  |
    | premiums_earned | 已赚保费 | decimal(20,4) |  |
    | assurance_income | 保险业务收入 | decimal(20,4) |  |
    | premiums_income | 分保费收入 | decimal(20,4) |  |
    | premiums_expense | 分出保费 | decimal(20,4) |  |
    | prepare_money | 提取未到期责任准备金 | decimal(20,4) |  |
    | investment_income | 投资收益 | decimal(20,4) |  |
    | invest_income_associates | 对联营企业和合营企业的投资收益 | decimal(20,4) |  |
    | fair_value_variable_income | 公允价值变动收益 | decimal(20,4) |  |
    | exchange_income | 汇兑收益 | decimal(20,4) |  |
    | other_income | 其他业务收入 | decimal(20,4) |  |
    | operation_expense | 营业支出 | decimal(20,4) |  |
    | refunded_premiums | 退保金 | decimal(20,4) |  |
    | compensate_loss | 赔付支出 | decimal(20,4) |  |
    | compensation_back | 摊回赔付支出 | decimal(20,4) |  |
    | insurance_reserve | 提取保险责任准备金 | decimal(20,4) |  |
    | insurance_reserve_back | 摊回保险责任准备金 | decimal(20,4) |  |
    | policy_dividend_payout | 保单红利支出 | decimal(20,4) |  |
    | reinsurance_cost | 分保费用 | decimal(20,4) |  |
    | operating_tax_surcharges | 营业税金及附加 | decimal(20,4) |  |
    | commission_expense2 | 手续费及佣金支出(保险专用) | decimal(20,4) |  |
    | operation_manage_fee | 业务及管理费 | decimal(20,4) |  |
    | separate_fee | 摊回分保费用 | decimal(20,4) |  |
    | asset_impairment_loss | 资产减值损失 | decimal(20,4) |  |
    | other_cost | 其他业务成本 | decimal(20,4) |  |
    | operating_profit | 营业利润 | decimal(20,4) |  |
    | subsidy_income | 补贴收入 | decimal(20,4) |  |
    | non_operating_revenue | 营业外收入 | decimal(20,4) |  |
    | non_operating_expense | 营业外支出 | decimal(20,4) |  |
    | other_items_influenced_profit | 影响利润总额的其他科目 | decimal(20,4) |  |
    | total_profit | 利润总额 | decimal(20,4) |  |
    | income_tax_expense | 所得税费用 | decimal(20,4) |  |
    | other_influence_net_profit | 影响净利润的其他科目 | decimal(20,4) |  |
    | net_profit | 净利润 | decimal(20,4) |  |
    | np_parent_company_owners | 归属于母公司股东的净利润 | decimal(20,4) |  |
    | minority_profit | 少数股东损益 | decimal(20,4) |  |
    | eps | 每股收益 | decimal(20,4) |  |
    | basic_eps | 基本每股收益 | decimal(20,4) |  |
    | diluted_eps | 稀释每股收益 | decimal(20,4) |  |
    | other_composite_income | 其他综合收益 | decimal(20,4) |  |
    | total_composite_income | 综合收益总额 | decimal(20,4) |  |
    | ci_parent_company_owners | 归属于母公司的综合收益 | decimal(20,4) |  |
    | ci_minority_owners | 归属于少数股东的综合收益 | decimal(20,4) |  |
    | other_earnings | 其他收益 | decimal(20,4) |  |
    | asset_deal_income | 资产处置收益 | decimal(20,4) |  |
    | sust_operate_net_profit | 持续经营净利润 | decimal(20,4) |  |
    | discon_operate_net_profit | 终止经营净利润 | decimal(20,4) |  |
    | credit_impairment_loss | 信用减值损失 | decimal(20,4) |  |
    
- **报表来源编码**
    
    | 编码 | 名称 |
    | --- | --- |
    | 321001 | 招募说明书 |
    | 321002 | 上市公告书 |
    | 321003 | 定期报告 |
    | 321004 | 预披露公告 |
    | 321005 | 换股报告书 |
    | 321099 | 其他 |
    
- filter(finance.FINANCE_INCOME_STATEMENT_PARENT.code==code)**：指定筛选条件，通过finance.FINANCE_INCOME_STATEMENT_PARENT.code==code可以指定你想要查询的股票代码；除此之外，还可以对表中其他字段指定筛选条件，如finance.FINANCE_INCOME_STATEMENT_PARENT.pub_date>='2015-01-01'，表示公告日期大于2015年1月1日金融类上市公司公布的母公司利润表信息；多个筛选条件用英文逗号分隔。
    
- **limit(n)**：限制返回的数据条数，n指定返回条数。
    

**返回结果：**

- 返回一个 dataframe，每一行对应数据表中的一条数据， 列索引是你所查询的字段名称

**注意：**

1.  **为了防止返回数据量过大, 我们每次最多返回4000行**
2.  不能进行连表查询，即同时查询多张表的数据

**示例：**

```
#查询中国平安2015年之后公告的母公司利润表数据,指定只取出本期数据
from jqdata import finance
q=query(finance.FINANCE_INCOME_STATEMENT_PARENT).filter(finance.FINANCE_INCOME_STATEMENT_PARENT.code=='601318.XSHG',                                        finance.FINANCE_INCOME_STATEMENT_PARENT.pub_date>='2015-01-01',                         finance.FINANCE_INCOME_STATEMENT_PARENT.report_type==0).limit(20)
df=finance.run_query(q)
print(df)

      id  company_id      company_name         code  a_code b_code h_code  \
0    214   300002221  中国平安保险(集团)股份有限公司  601318.XSHG  601318   None  02318
1    216   300002221  中国平安保险(集团)股份有限公司  601318.XSHG  601318   None  02318
2    218   300002221  中国平安保险(集团)股份有限公司  601318.XSHG  601318   None  02318
3    220   300002221  中国平安保险(集团)股份有限公司  601318.XSHG  601318   None  02318
4    222   300002221  中国平安保险(集团)股份有限公司  601318.XSHG  601318   None  02318
5    224   300002221  中国平安保险(集团)股份有限公司  601318.XSHG  601318   None  02318
6    226   300002221  中国平安保险(集团)股份有限公司  601318.XSHG  601318   None  02318
7    228   300002221  中国平安保险(集团)股份有限公司  601318.XSHG  601318   None  02318
8    230   300002221  中国平安保险(集团)股份有限公司  601318.XSHG  601318   None  02318
9    232   300002221  中国平安保险(集团)股份有限公司  601318.XSHG  601318   None  02318
10   233   300002221  中国平安保险(集团)股份有限公司  601318.XSHG  601318   None  02318
11   234   300002221  中国平安保险(集团)股份有限公司  601318.XSHG  601318   None  02318
12   235   300002221  中国平安保险(集团)股份有限公司  601318.XSHG  601318   None  02318
13  3508   300002221  中国平安保险(集团)股份有限公司  601318.XSHG  601318   None  02318
14  3638   300002221  中国平安保险(集团)股份有限公司  601318.XSHG  601318   None  02318

      pub_date  start_date    end_date        ...           net_profit  \
0   2015-03-20  2014-01-01  2014-12-31        ...           7214000000
1   2015-04-30  2015-01-01  2015-03-31        ...            316000000
2   2015-08-21  2015-01-01  2015-06-30        ...           8390000000
3   2015-10-28  2015-01-01  2015-09-30        ...           8969000000
4   2016-03-16  2015-01-01  2015-12-31        ...          10280000000
5   2016-04-27  2016-01-01  2016-03-31        ...            181000000
6   2016-08-18  2016-01-01  2016-06-30        ...          13850000000
7   2016-10-28  2016-01-01  2016-09-30        ...          13747000000
8   2017-03-23  2016-01-01  2016-12-31        ...          28678000000
9   2017-04-28  2017-01-01  2017-03-31        ...              2000000
10  2017-08-18  2017-01-01  2017-06-30        ...          12068000000
11  2017-10-28  2017-01-01  2017-09-30        ...          14439000000
12  2018-03-21  2017-01-01  2017-12-31        ...          29238000000
13  2018-04-27  2018-01-01  2018-03-31        ...           -214000000
14  2018-08-22  2018-01-01  2018-06-30        ...          21911000000

    np_parent_company_owners  minority_profit  eps  basic_eps diluted_eps  \
0                 7214000000              NaN  NaN        NaN         NaN
1                  316000000              NaN  NaN        NaN         NaN
2                 8390000000              NaN  NaN        NaN         NaN
3                 8969000000              NaN  NaN        NaN         NaN
4                10280000000              NaN  NaN        NaN         NaN
5                  181000000              NaN  NaN        NaN         NaN
6                13850000000              NaN  NaN        NaN         NaN
7                13747000000              NaN  NaN        NaN         NaN
8                28678000000              NaN  NaN        NaN         NaN
9                    2000000              NaN  NaN        NaN         NaN
10               12068000000              NaN  NaN        NaN         NaN
11               14439000000              NaN  NaN        NaN         NaN
12               29238000000              NaN  NaN        NaN         NaN
13                -214000000              NaN  NaN        NaN         NaN
14               21911000000              NaN  NaN        NaN         NaN

   other_composite_income total_composite_income ci_parent_company_owners  \
0               235000000             7449000000                      NaN
1               -47000000              269000000                      NaN
2                85000000             8475000000                      NaN
3               191000000             9160000000                      NaN
4               436000000            10716000000                      NaN
5               -38000000              143000000                      NaN
6               -48000000            13802000000              13802000000
7                 7000000            13754000000              13754000000
8              -285000000            28393000000              28393000000
9                -9000000               -7000000                      NaN
10                7000000            12075000000              12075000000
11               41000000            14480000000              14480000000
12             -172000000            29066000000              29066000000
13               52000000             -162000000               -162000000
14               84000000            21995000000              21995000000

   ci_minority_owners
0                 NaN
1                 NaN
2                 NaN
3                 NaN
4                 NaN
5                 NaN
6                 NaN
7                 NaN
8                 NaN
9                 NaN
10                NaN
11                NaN
12                NaN
13                NaN
14                NaN

[15 rows x 66 columns]
```

### 金融类合并现金流量表

#### 金融类合并现金流量表2007版

```python
from jqdata import finance
finance.run_query(query(finance.FINANCE_CASHFLOW_STATEMENT).filter(finance.FINANCE_CASHFLOW_STATEMENT.code==code).limit(n))
```

获取金融类上市公司的合并现金流量表信息

**参数：**

- **query(finance.FINANCE_CASHFLOW_STATEMENT)**：表示从finance.FINANCE_CASHFLOW_STATEMENT这张表中查询金融类上市公司合并现金流量的字段信息，还可以指定所要查询的字段名，格式如下：query(库名.表名.字段名1，库名.表名.字段名2），多个字段用逗号分隔进行提取；query函数的更多用法详见：[sqlalchemy.orm.query.Query对象](http://docs.sqlalchemy.org/en/rel_1_0/orm/query.html)
    
- **finance.FINANCE_CASHFLOW_STATEMENT**：代表金融类上市公司合并现金流量表，收录了金融类上市公司的合并现金流量，表结构和字段信息如下：
    
    | 字段名称 | 中文名称 | 字段类型 | 含义 |
    | --- | --- | --- | --- |
    | company_id | 公司ID | int |  |
    | company_name | 公司名称 | varchar(100) |  |
    | code | 公司主证券代码 | varchar(12) |  |
    | a_code | A股代码 | varchar(12) |  |
    | b_code | B股代码 | varchar(12) |  |
    | h_code | H股代码 | varchar(12) |  |
    | pub_date | 公告日期 | date |  |
    | start_date | 开始日期 | date |  |
    | end_date | 截止日期 | date |  |
    | report_date | 报告期 | date |  |
    | report_type | 报告期类型 | int | 0本期，1上期 |
    | source_id | 报表来源编码 | int | 如下[报表来源编码](#source9) |
    | source | 报表来源 | varchar(60) |  |
    | operate_cash_flow | 经营活动产生的现金流量 | decimal(20,4) |  |
    | net_loan_and_advance_decrease | 客户贷款及垫款净减少额 | decimal(20,4) |  |
    | net_deposit_increase | 客户存款和同业存放款项净增加额 | decimal(20,4) |  |
    | net_borrowing_from_central_bank | 向中央银行借款净增加额 | decimal(20,4) |  |
    | net_deposit_in_cb_and_ib_de | 存放中央银行和同业款项净减少额 | decimal(20,4) |  |
    | net_borrowing_from_finance_co | 向其他金融机构拆入资金净增加额 | decimal(20,4) |  |
    | interest_and_commission_cashin | 收取利息、手续费及佣金的现金 | decimal(20,4) |  |
    | trade_asset_increase | 处置交易性金融资产净增加额 | decimal(20,4) |  |
    | net_increase_in_placements | 拆入资金净增加额 | decimal(20,4) |  |
    | net_buyback | 回购业务资金净增加额 | decimal(20,4) |  |
    | goods_sale_and_service_render_cash | 销售商品、提供劳务收到的现金 | decimal(20,4) |  |
    | tax_levy_refund | 收到的税费返还 | decimal(20,4) |  |
    | net_original_insurance_cash | 收到原保险合同保费取得的现金 | decimal(20,4) |  |
    | insurance_cash_amount | 收到再保业务现金净额 | decimal(20,4) |  |
    | net_insurer_deposit_investment | 保户储金及投资款净增加额 | decimal(20,4) |  |
    | subtotal_operate_cash_inflow | 经营活动现金流入小计 | decimal(20,4) |  |
    | net_loan_and_advance_increase | 客户贷款及垫款净增加额 | decimal(20,4) |  |
    | saving_clients_decrease_amount | 客户存放及同业存放款项净减少额 | decimal(20,4) |  |
    | net_deposit_in_cb_and_ib | 存放中央银行和同业款项净增加额 | decimal(20,4) |  |
    | central_borrowing_decrease | 向中央银行借款净减少额 | decimal(20,4) |  |
    | other_money_increase | 向其他金融机构拆出资金净增加额 | decimal(20,4) |  |
    | purchase_trade_asset_increase | 购入交易性金融资产净增加额 | decimal(20,4) |  |
    | repurchase_decrease | 回购业务资金净减少额 | decimal(20,4) |  |
    | handling_charges_and_commission | 支付利息、手续费及佣金的现金 | decimal(20,4) |  |
    | goods_and_services_cash_paid | 购买商品、提供劳务支付的现金 | decimal(20,4) |  |
    | net_cash_re_insurance | 支付再保业务现金净额 | decimal(20,4) |  |
    | reserve_investment_decrease | 保户储金及投资款净减少额 | decimal(20,4) |  |
    | original_compensation_paid | 支付原保险合同赔付款项的现金 | decimal(20,4) |  |
    | policy_dividend_cash_paid | 支付保单红利的现金 | decimal(20,4) |  |
    | staff_behalf_paid | 支付给职工以及为职工支付的现金 | decimal(20,4) |  |
    | tax_payments | 支付的各项税费 | decimal(20,4) |  |
    | subtotal_operate_cash_outflow | 经营活动现金流出小计 | decimal(20,4) |  |
    | net_operate_cash_flow | 经营活动现金流量净额 | decimal(20,4) |  |
    | invest_cash_flow | 投资活动产生的现金流量 | decimal(20,4) |  |
    | invest_withdrawal_cash | 收回投资收到的现金 | decimal(20,4) |  |
    | invest_proceeds | 取得投资收益收到的现金 | decimal(20,4) |  |
    | gain_from_disposal | 处置固定资产、无形资产和其他长期资产所收回的现金 | decimal(20,4) |  |
    | subtotal_invest_cash_inflow | 投资活动现金流入小计 | decimal(20,4) |  |
    | invest_cash_paid | 投资支付的现金 | decimal(20,4) |  |
    | impawned_loan_net_increase | 质押贷款净增加额 | decimal(20,4) |  |
    | fix_intan_other_asset_acqui_cash | 购建固定资产、无形资产和其他长期资产支付的现金 | decimal(20,4) |  |
    | subtotal_invest_cash_outflow | 投资活动现金流出小计 | decimal(20,4) |  |
    | net_invest_cash_flow | 投资活动现金流量净额 | decimal(20,4) |  |
    | finance_cash_flow | 筹资活动产生的现金流量 | decimal(20,4) |  |
    | cash_from_invest | 吸收投资收到的现金 | decimal(20,4) |  |
    | cash_from_bonds_issue | 发行债券收到的现金 | decimal(20,4) |  |
    | cash_from_borrowing | 取得借款收到的现金 | decimal(20,4) |  |
    | subtotal_finance_cash_inflow | 筹资活动现金流入小计 | decimal(20,4) |  |
    | borrowing_repayment | 偿还债务支付的现金 | decimal(20,4) |  |
    | dividend_interest_payment | 分配股利、利润或偿付利息支付的现金 | decimal(20,4) |  |
    | subtotal_finance_cash_outflow | 筹资活动现金流出小计 | decimal(20,4) |  |
    | net_finance_cash_flow | 筹资活动产生的现金流量净额 | decimal(20,4) |  |
    | exchange_rate_change_effect | 汇率变动对现金的影响 | decimal(20,4) |  |
    | other_reason_effect_cash | 其他原因对现金的影响 | decimal(20,4) |  |
    | cash_equivalent_increase | 现金及现金等价物净增加额 | decimal(20,4) |  |
    | cash_equivalents_at_beginning | 期初现金及现金等价物余额 | decimal(20,4) |  |
    | cash_and_equivalents_at_end | 期末现金及现金等价物余额 | decimal(20,4) |  |
    | net_profit_cashflow_adjustment | 将净利润调节为经营活动现金流量 | decimal(20,4) |  |
    | net_profit | 净利润 | decimal(20,4) |  |
    | assets_depreciation_reserves | 资产减值准备 | decimal(20,4) |  |
    | fixed_assets_depreciation | 固定资产折旧、油气资产折耗、生产性生物资产折旧 | decimal(20,4) |  |
    | intangible_assets_amortization | 无形资产摊销 | decimal(20,4) |  |
    | defferred_expense_amortization | 长期待摊费用摊销 | decimal(20,4) |  |
    | fix_intan_other_asset_dispo_loss | 处置固定资产、无形资产和其他长期资产的损失 | decimal(20,4) |  |
    | fixed_asset_scrap_loss | 固定资产报废损失 | decimal(20,4) |  |
    | fair_value_change_loss | 公允价值变动损失 | decimal(20,4) |  |
    | financial_cost | 财务费用 | decimal(20,4) |  |
    | invest_loss | 投资损失 | decimal(20,4) |  |
    | deffered_tax_asset_decrease | 递延所得税资产减少 | decimal(20,4) |  |
    | deffered_tax_liability_increase | 递延所得税负债增加 | decimal(20,4) |  |
    | inventory_decrease | 存货的减少 | decimal(20,4) |  |
    | operate_receivables_decrease | 经营性应收项目的减少 | decimal(20,4) |  |
    | operate_payable_increase | 经营性应付项目的增加 | decimal(20,4) |  |
    | others | 其他 | decimal(20,4) |  |
    | net_operate_cash_flow2 | 经营活动产生的现金流量净额_间接法 | decimal(20,4) |  |
    | activities_not_relate_major | 不涉及现金收支的重大投资和筹资活动 | decimal(20,4) |  |
    | debt_to_capital | 债务转为资本 | decimal(20,4) |  |
    | cbs_expiring_in_one_year | 一年内到期的可转换公司债券 | decimal(20,4) |  |
    | financial_lease_fixed_assets | 融资租入固定资产 | decimal(20,4) |  |
    | change_info_cash | 现金及现金等价物净变动情况 | decimal(20,4) |  |
    | cash_at_end | 现金的期末余额 | decimal(20,4) |  |
    | cash_at_beginning | 现金的期初余额 | decimal(20,4) |  |
    | equivalents_at_end | 现金等价物的期末余额 | decimal(20,4) |  |
    | equivalents_at_beginning | 现金等价物的期初余额 | decimal(20,4) |  |
    | other_influence2 | 其他原因对现金的影响2 | decimal(20,4) |  |
    | cash_equivalent_increase2 | 现金及现金等价物净增加额2 | decimal(20,4) |  |
    | investment_property_depreciation | 投资性房地产的折旧及摊销 | decimal(20,4) |  |
    | net_dec_finance_out | 融出资金净减少额 | decimal(20,4) |  |
    | net_cash_received_from_proxy_secu | 代理买卖证券收到的现金净额 | decimal(20,4) |  |
    | net_inc_finance_out | 融出资金净增加额 | decimal(20,4) |  |
    | net_cash_paid_to_proxy_secu | 代理买卖证券支付的现金净额 | decimal(20,4) |  |
    | net_dec_in_placements | 拆入资金净减少额 | decimal(20,4) |  |
    | credit_impairment_loss | 信用减值损失(现金流量表补充科目) | decimal(20,4) |  |
    
- **报表来源编码**
    
    | 编码 | 名称 |
    | --- | --- |
    | 321001 | 招募说明书 |
    | 321002 | 上市公告书 |
    | 321003 | 定期报告 |
    | 321004 | 预披露公告 |
    | 321005 | 换股报告书 |
    | 321099 | 其他 |
    
- **filter(finance.FINANCE_CASHFLOW_STATEMENT.code==code)**：指定筛选条件，通过finance.FINANCE_CASHFLOW_STATEMENT.code==code可以指定你想要查询的股票代码；除此之外，还可以对表中其他字段指定筛选条件，如finance.FINANCE_CASHFLOW_STATEMENT.pub_date>='2015-01-01'，表示公告日期大于2015年1月1日金融类上市公司公布的合并现金流量信息；多个筛选条件用英文逗号分隔。
    
- **limit(n)**：限制返回的数据条数，n指定返回条数。
    

**返回结果：**

- 返回一个 dataframe，每一行对应数据表中的一条数据， 列索引是你所查询的字段名称

**注意：**

1.  **为了防止返回数据量过大, 我们每次最多返回4000行**
2.  不能进行连表查询，即同时查询多张表的数据

**示例：**

```
#查询中国平安2015年之后公告的合并现金流量表数据，指定只取出本期数据经营活动现金流量净额，投资活动现金流量净额，以及筹资活动现金流量净额
from jqdata import *
q=query(finance.FINANCE_CASHFLOW_STATEMENT.company_name,
        finance.FINANCE_CASHFLOW_STATEMENT.code,
        finance.FINANCE_CASHFLOW_STATEMENT.pub_date,
        finance.FINANCE_CASHFLOW_STATEMENT.start_date,
        finance.FINANCE_CASHFLOW_STATEMENT.end_date,
        finance.FINANCE_CASHFLOW_STATEMENT.net_operate_cash_flow,
        finance.FINANCE_CASHFLOW_STATEMENT.net_invest_cash_flow,
finance.FINANCE_CASHFLOW_STATEMENT.net_finance_cash_flow).filter(finance.FINANCE_CASHFLOW_STATEMENT.code=='601318.XSHG',finance.FINANCE_CASHFLOW_STATEMENT.pub_date>='2015-01-01',finance.FINANCE_CASHFLOW_STATEMENT.report_type==0).limit(20)
df=finance.run_query(q)
print(df)

        company_name         code    pub_date  start_date    end_date  \
0   中国平安保险(集团)股份有限公司  601318.XSHG  2015-03-20  2014-01-01  2014-12-31
1   中国平安保险(集团)股份有限公司  601318.XSHG  2015-04-30  2015-01-01  2015-03-31
2   中国平安保险(集团)股份有限公司  601318.XSHG  2015-08-21  2015-01-01  2015-06-30
3   中国平安保险(集团)股份有限公司  601318.XSHG  2015-10-28  2015-01-01  2015-09-30
4   中国平安保险(集团)股份有限公司  601318.XSHG  2016-03-16  2015-01-01  2015-12-31
5   中国平安保险(集团)股份有限公司  601318.XSHG  2016-04-27  2016-01-01  2016-03-31
6   中国平安保险(集团)股份有限公司  601318.XSHG  2016-08-18  2016-01-01  2016-06-30
7   中国平安保险(集团)股份有限公司  601318.XSHG  2016-10-28  2016-01-01  2016-09-30
8   中国平安保险(集团)股份有限公司  601318.XSHG  2017-03-23  2016-01-01  2016-12-31
9   中国平安保险(集团)股份有限公司  601318.XSHG  2017-04-28  2017-01-01  2017-03-31
10  中国平安保险(集团)股份有限公司  601318.XSHG  2017-08-18  2017-01-01  2017-06-30
11  中国平安保险(集团)股份有限公司  601318.XSHG  2017-10-28  2017-01-01  2017-09-30
12  中国平安保险(集团)股份有限公司  601318.XSHG  2018-03-21  2017-01-01  2017-12-31
13  中国平安保险(集团)股份有限公司  601318.XSHG  2018-04-27  2018-01-01  2018-03-31
14  中国平安保险(集团)股份有限公司  601318.XSHG  2018-08-22  2018-01-01  2018-06-30

    net_operate_cash_flow  net_invest_cash_flow  net_finance_cash_flow
0            1.702600e+11         -2.368890e+11           8.536800e+10
1            6.114900e+10         -4.478700e+10           1.996200e+10
2            2.478960e+11         -1.355150e+11           1.059350e+11
3            1.710670e+11         -1.442380e+11           1.675280e+11
4            1.356180e+11         -2.737320e+11           2.049760e+11
5            1.192720e+11         -1.241580e+11           5.367100e+10
6            6.599800e+10         -2.663960e+11           1.714720e+11
7           -1.702500e+10         -1.942610e+11           1.291400e+11
8            2.278210e+11         -3.306160e+11           1.330040e+11
9           -4.168500e+10         -9.311700e+10           5.026700e+10
10          -1.397500e+10         -2.399940e+11           1.139460e+11
11           7.821000e+09         -2.805420e+11           1.511410e+11
12           1.212830e+11         -3.547670e+11           1.785880e+11
13           1.398670e+11         -8.252000e+10          -1.837000e+09
14           1.616070e+11         -6.376100e+10          -3.634900e+10
```

### 金融类母公司现金流量表

```
from jqdata import finance
finance.run_query(query(finance.FINANCE_CASHFLOW_STATEMENT_PARENT).filter(finance.FINANCE_CASHFLOW_STATEMENT_PARENT.code==code).limit(n))
```

获取金融类上市公司的母公司现金流量表信息

**参数：**

- **query(finance.FINANCE_CASHFLOW_STATEMENT_PARENT)**：表示从finance.FINANCE_CASHFLOW_STATEMENT_PARENT这张表中查询金融类上市公司母公司现金流量的字段信息，还可以指定所要查询的字段名，格式如下：query(库名.表名.字段名1，库名.表名.字段名2），多个字段用逗号分隔进行提取；query函数的更多用法详见：[sqlalchemy.orm.query.Query对象](http://docs.sqlalchemy.org/en/rel_1_0/orm/query.html)
    
- **finance.FINANCE_CASHFLOW_STATEMENT_PARENT**：代表金融类上市公司母公司现金流量表，收录了金融类上市公司的母公司现金流量，表结构和字段信息如下：
    
    | 字段名称 | 中文名称 | 字段类型 | 含义 |
    | --- | --- | --- | --- |
    | company_id | 公司ID | int |  |
    | company_name | 公司名称 | varchar(100) |  |
    | code | 公司主证券代码 | varchar(12) |  |
    | a_code | A股代码 | varchar(12) |  |
    | b_code | B股代码 | varchar(12) |  |
    | h_code | H股代码 | varchar(12) |  |
    | pub_date | 公告日期 | date |  |
    | start_date | 开始日期 | date |  |
    | end_date | 截止日期 | date |  |
    | report_date | 报告期 | date |  |
    | report_type | 报告期类型 | int | 0本期，1上期 |
    | source_id | 报表来源编码 | int | 如下[报表来源编码](#source10) |
    | source | 报表来源 | varchar(60) |  |
    | operate_cash_flow | 经营活动产生的现金流量 | decimal(20,4) |  |
    | net_loan_and_advance_decrease | 客户贷款及垫款净减少额 | decimal(20,4) |  |
    | net_deposit_increase | 客户存款和同业存放款项净增加额 | decimal(20,4) |  |
    | net_borrowing_from_central_bank | 向中央银行借款净增加额 | decimal(20,4) |  |
    | net_deposit_in_cb_and_ib_de | 存放中央银行和同业款项净减少额 | decimal(20,4) |  |
    | net_borrowing_from_finance_co | 向其他金融机构拆入资金净增加额 | decimal(20,4) |  |
    | interest_and_commission_cashin | 收取利息、手续费及佣金的现金 | decimal(20,4) |  |
    | trade_asset_increase | 处置交易性金融资产净增加额 | decimal(20,4) |  |
    | net_increase_in_placements | 拆入资金净增加额 | decimal(20,4) |  |
    | net_buyback | 回购业务资金净增加额 | decimal(20,4) |  |
    | goods_sale_and_service_render_cash | 销售商品、提供劳务收到的现金 | decimal(20,4) |  |
    | tax_levy_refund | 收到的税费返还 | decimal(20,4) |  |
    | net_original_insurance_cash | 收到原保险合同保费取得的现金 | decimal(20,4) |  |
    | insurance_cash_amount | 收到再保业务现金净额 | decimal(20,4) |  |
    | net_insurer_deposit_investment | 保户储金及投资款净增加额 | decimal(20,4) |  |
    | subtotal_operate_cash_inflow | 经营活动现金流入小计 | decimal(20,4) |  |
    | net_loan_and_advance_increase | 客户贷款及垫款净增加额 | decimal(20,4) |  |
    | saving_clients_decrease_amount | 客户存放及同业存放款项净减少额 | decimal(20,4) |  |
    | net_deposit_in_cb_and_ib | 存放中央银行和同业款项净增加额 | decimal(20,4) |  |
    | central_borrowing_decrease | 向中央银行借款净减少额 | decimal(20,4) |  |
    | other_money_increase | 向其他金融机构拆出资金净增加额 | decimal(20,4) |  |
    | purchase_trade_asset_increase | 购入交易性金融资产净增加额 | decimal(20,4) |  |
    | repurchase_decrease | 回购业务资金净减少额 | decimal(20,4) |  |
    | handling_charges_and_commission | 支付利息、手续费及佣金的现金 | decimal(20,4) |  |
    | goods_and_services_cash_paid | 购买商品、提供劳务支付的现金 | decimal(20,4) |  |
    | net_cash_re_insurance | 支付再保业务现金净额 | decimal(20,4) |  |
    | reserve_investment_decrease | 保户储金及投资款净减少额 | decimal(20,4) |  |
    | original_compensation_paid | 支付原保险合同赔付款项的现金 | decimal(20,4) |  |
    | policy_dividend_cash_paid | 支付保单红利的现金 | decimal(20,4) |  |
    | staff_behalf_paid | 支付给职工以及为职工支付的现金 | decimal(20,4) |  |
    | tax_payments | 支付的各项税费 | decimal(20,4) |  |
    | subtotal_operate_cash_outflow | 经营活动现金流出小计 | decimal(20,4) |  |
    | net_operate_cash_flow | 经营活动现金流量净额 | decimal(20,4) |  |
    | invest_cash_flow | 投资活动产生的现金流量 | decimal(20,4) |  |
    | invest_withdrawal_cash | 收回投资收到的现金 | decimal(20,4) |  |
    | invest_proceeds | 取得投资收益收到的现金 | decimal(20,4) |  |
    | gain_from_disposal | 处置固定资产、无形资产和其他长期资产所收回的现金 | decimal(20,4) |  |
    | subtotal_invest_cash_inflow | 投资活动现金流入小计 | decimal(20,4) |  |
    | invest_cash_paid | 投资支付的现金 | decimal(20,4) |  |
    | impawned_loan_net_increase | 质押贷款净增加额 | decimal(20,4) |  |
    | fix_intan_other_asset_acqui_cash | 购建固定资产、无形资产和其他长期资产支付的现金 | decimal(20,4) |  |
    | subtotal_invest_cash_outflow | 投资活动现金流出小计 | decimal(20,4) |  |
    | net_invest_cash_flow | 投资活动现金流量净额 | decimal(20,4) |  |
    | finance_cash_flow | 筹资活动产生的现金流量 | decimal(20,4) |  |
    | cash_from_invest | 吸收投资收到的现金 | decimal(20,4) |  |
    | cash_from_bonds_issue | 发行债券收到的现金 | decimal(20,4) |  |
    | cash_from_borrowing | 取得借款收到的现金 | decimal(20,4) |  |
    | subtotal_finance_cash_inflow | 筹资活动现金流入小计 | decimal(20,4) |  |
    | borrowing_repayment | 偿还债务支付的现金 | decimal(20,4) |  |
    | dividend_interest_payment | 分配股利、利润或偿付利息支付的现金 | decimal(20,4) |  |
    | subtotal_finance_cash_outflow | 筹资活动现金流出小计 | decimal(20,4) |  |
    | net_finance_cash_flow | 筹资活动产生的现金流量净额 | decimal(20,4) |  |
    | exchange_rate_change_effect | 汇率变动对现金的影响 | decimal(20,4) |  |
    | other_reason_effect_cash | 其他原因对现金的影响 | decimal(20,4) |  |
    | cash_equivalent_increase | 现金及现金等价物净增加额 | decimal(20,4) |  |
    | cash_equivalents_at_beginning | 期初现金及现金等价物余额 | decimal(20,4) |  |
    | cash_and_equivalents_at_end | 期末现金及现金等价物余额 | decimal(20,4) |  |
    | net_profit_cashflow_adjustment | 将净利润调节为经营活动现金流量 | decimal(20,4) |  |
    | net_profit | 净利润 | decimal(20,4) |  |
    | assets_depreciation_reserves | 资产减值准备 | decimal(20,4) |  |
    | fixed_assets_depreciation | 固定资产折旧、油气资产折耗、生产性生物资产折旧 | decimal(20,4) |  |
    | intangible_assets_amortization | 无形资产摊销 | decimal(20,4) |  |
    | defferred_expense_amortization | 长期待摊费用摊销 | decimal(20,4) |  |
    | fix_intan_other_asset_dispo_loss | 处置固定资产、无形资产和其他长期资产的损失 | decimal(20,4) |  |
    | fixed_asset_scrap_loss | 固定资产报废损失 | decimal(20,4) |  |
    | fair_value_change_loss | 公允价值变动损失 | decimal(20,4) |  |
    | financial_cost | 财务费用 | decimal(20,4) |  |
    | invest_loss | 投资损失 | decimal(20,4) |  |
    | deffered_tax_asset_decrease | 递延所得税资产减少 | decimal(20,4) |  |
    | deffered_tax_liability_increase | 递延所得税负债增加 | decimal(20,4) |  |
    | inventory_decrease | 存货的减少 | decimal(20,4) |  |
    | operate_receivables_decrease | 经营性应收项目的减少 | decimal(20,4) |  |
    | operate_payable_increase | 经营性应付项目的增加 | decimal(20,4) |  |
    | others | 其他 | decimal(20,4) |  |
    | net_operate_cash_flow2 | 经营活动产生的现金流量净额_间接法 | decimal(20,4) |  |
    | activities_not_relate_major | 不涉及现金收支的重大投资和筹资活动 | decimal(20,4) |  |
    | debt_to_capital | 债务转为资本 | decimal(20,4) |  |
    | cbs_expiring_in_one_year | 一年内到期的可转换公司债券 | decimal(20,4) |  |
    | financial_lease_fixed_assets | 融资租入固定资产 | decimal(20,4) |  |
    | change_info_cash | 现金及现金等价物净变动情况 | decimal(20,4) |  |
    | cash_at_end | 现金的期末余额 | decimal(20,4) |  |
    | cash_at_beginning | 现金的期初余额 | decimal(20,4) |  |
    | equivalents_at_end | 现金等价物的期末余额 | decimal(20,4) |  |
    | equivalents_at_beginning | 现金等价物的期初余额 | decimal(20,4) |  |
    | other_influence2 | 其他原因对现金的影响2 | decimal(20,4) |  |
    | cash_equivalent_increase2 | 现金及现金等价物净增加额2 | decimal(20,4) |  |
    | investment_property_depreciation | 投资性房地产的折旧及摊销 | decimal(20,4) |  |
    | net_dec_finance_out | 融出资金净减少额 | decimal(20,4) |  |
    | net_cash_received_from_proxy_secu | 代理买卖证券收到的现金净额 | decimal(20,4) |  |
    | net_inc_finance_out | 融出资金净增加额 | decimal(20,4) |  |
    | net_cash_paid_to_proxy_secu | 代理买卖证券支付的现金净额 | decimal(20,4) |  |
    | net_dec_in_placements | 拆入资金净减少额 | decimal(20,4) |  |
    | credit_impairment_loss | 信用减值损失(现金流量表补充科目) | decimal(20,4) |  |
    
- **报表来源编码**
    
    | 编码 | 名称 |
    | --- | --- |
    | 321001 | 招募说明书 |
    | 321002 | 上市公告书 |
    | 321003 | 定期报告 |
    | 321004 | 预披露公告 |
    | 321005 | 换股报告书 |
    | 321099 | 其他 |
    
- **filter(finance.FINANCE_CASHFLOW_STATEMENT_PARENT.code==code)**：指定筛选条件，通过finance.FINANCE_CASHFLOW_STATEMENT_PARENT.code==code可以指定你想要查询的股票代码；除此之外，还可以对表中其他字段指定筛选条件，如finance.FINANCE_CASHFLOW_STATEMENT_PARENT.pub_date>='2015-01-01'，表示公告日期大于2015年1月1日金融类上市公司公布的母公司现金流量信息；多个筛选条件用英文逗号分隔。
    
- **limit(n)**：限制返回的数据条数，n指定返回条数。
    

**返回结果：**

- 返回一个 dataframe，每一行对应数据表中的一条数据， 列索引是你所查询的字段名称

**注意：**

1.  **为了防止返回数据量过大, 我们每次最多返回4000行**
2.  不能进行连表查询，即同时查询多张表的数据

**示例：**

```python
#查询中国平安2015年之后公告的母公司现金流量表数据，指定只取出本期经营活动现金流量净额，投资活动现金流量净额，以及筹资活动现金流量净额
from jqdata import *
q=query(finance.FINANCE_CASHFLOW_STATEMENT_PARENT.company_name,
        finance.FINANCE_CASHFLOW_STATEMENT_PARENT.code,
        finance.FINANCE_CASHFLOW_STATEMENT_PARENT.pub_date,
        finance.FINANCE_CASHFLOW_STATEMENT_PARENT.start_date,
        finance.FINANCE_CASHFLOW_STATEMENT_PARENT.end_date,
        finance.FINANCE_CASHFLOW_STATEMENT_PARENT.net_operate_cash_flow,
        finance.FINANCE_CASHFLOW_STATEMENT_PARENT.net_invest_cash_flow,
finance.FINANCE_CASHFLOW_STATEMENT_PARENT.net_finance_cash_flow).filter(finance.FINANCE_CASHFLOW_STATEMENT_PARENT.code=='601318.XSHG',finance.FINANCE_CASHFLOW_STATEMENT_PARENT.pub_date>='2015-01-01',finance.FINANCE_CASHFLOW_STATEMENT_PARENT.report_type==0).limit(20)
df=finance.run_query(q)
print(df)

       company_name         code    pub_date  start_date    end_date  \
0   中国平安保险(集团)股份有限公司  601318.XSHG  2015-03-20  2014-01-01  2014-12-31
1   中国平安保险(集团)股份有限公司  601318.XSHG  2015-04-30  2015-01-01  2015-03-31
2   中国平安保险(集团)股份有限公司  601318.XSHG  2015-08-21  2015-01-01  2015-06-30
3   中国平安保险(集团)股份有限公司  601318.XSHG  2015-10-28  2015-01-01  2015-09-30
4   中国平安保险(集团)股份有限公司  601318.XSHG  2016-03-16  2015-01-01  2015-12-31
5   中国平安保险(集团)股份有限公司  601318.XSHG  2016-04-27  2016-01-01  2016-03-31
6   中国平安保险(集团)股份有限公司  601318.XSHG  2016-08-18  2016-01-01  2016-06-30
7   中国平安保险(集团)股份有限公司  601318.XSHG  2016-10-28  2016-01-01  2016-09-30
8   中国平安保险(集团)股份有限公司  601318.XSHG  2017-03-23  2016-01-01  2016-12-31
9   中国平安保险(集团)股份有限公司  601318.XSHG  2017-04-28  2017-01-01  2017-03-31
10  中国平安保险(集团)股份有限公司  601318.XSHG  2017-08-18  2017-01-01  2017-06-30
11  中国平安保险(集团)股份有限公司  601318.XSHG  2017-10-28  2017-01-01  2017-09-30
12  中国平安保险(集团)股份有限公司  601318.XSHG  2018-03-21  2017-01-01  2017-12-31
13  中国平安保险(集团)股份有限公司  601318.XSHG  2018-04-27  2018-01-01  2018-03-31
14  中国平安保险(集团)股份有限公司  601318.XSHG  2018-08-22  2018-01-01  2018-06-30

    net_operate_cash_flow  net_invest_cash_flow  net_finance_cash_flow
0               -88000000          -14333000000            23543000000
1              -202000000            -718000000              691000000
2               -88000000           -8063000000             3010000000
3               -25000000          -11168000000            -7130000000
4              -203000000          -10990000000            -5711000000
5              -533000000             456000000             -300000000
6              -236000000            3237000000            -1620000000
7              -418000000           10895000000           -10390000000
8              -639000000           15006000000           -11895000000
9              -259000000            -912000000            -1994000000
10             -165000000            5139000000            -3376000000
11             -647000000           13784000000           -12390000000
12             -310000000           22612000000           -15924000000
13             -211000000             246000000              470000000
14             -188000000           15464000000           -12487000000
```

### 金融类合并资产负债表

```
from jqdata import finance
finance.run_query(query(finance.FINANCE_BALANCE_SHEET).filter(finance.FINANCE_BALANCE_SHEET.code==code).limit(n))
```

获取金融类上市公司的合并资产负债表信息

**参数：**

- **query(finance.FINANCE_BALANCE_SHEET)**：表示从finance.FINANCE_BALANCE_SHEET这张表中查询金融类上市公司合并资产负债的字段信息，还可以指定所要查询的字段名，格式如下：query(库名.表名.字段名1，库名.表名.字段名2），多个字段用逗号分隔进行提取；query函数的更多用法详见：[sqlalchemy.orm.query.Query对象](http://docs.sqlalchemy.org/en/rel_1_0/orm/query.html)
    
- **finance.FINANCE_BALANCE_SHEET**：代表金融类上市公司合并资产负债表，收录了金融类上市公司的合并资产负债，表结构和字段信息如下：
    
    | 字段名称 | 中文名称 | 字段类型 | 含义 |
    | --- | --- | --- | --- |
    | company_id | 公司ID | int |  |
    | company_name | 公司名称 | varchar(100) |  |
    | code | 公司主证券代码 | varchar(12) |  |
    | a_code | A股代码 | varchar(12) |  |
    | b_code | B股代码 | varchar(12) |  |
    | h_code | H股代码 | varchar(12) |  |
    | pub_date | 公告日期 | date |  |
    | start_date | 开始日期 | date |  |
    | end_date | 截止日期 | date |  |
    | report_date | 报告期 | date |  |
    | report_type | 报告期类型 | int | 0本期，1上期 |
    | source_id | 报表来源编码 | int | 如下[报表编码表](#source11) |
    | source | 报表来源 | varchar(60) |  |
    | deposit_in_ib | 存放同业款项 | decimal(20,4) |  |
    | cash_equivalents | 货币资金 | decimal(20,4) |  |
    | deposit_client | 客户资金存款 | decimal(20,4) |  |
    | cash_in_cb | 现金及存放中央银行款项 | decimal(20,4) |  |
    | settlement_provi | 结算备付金 | decimal(20,4) |  |
    | settlement_provi_client | 客户备付金 | decimal(20,4) |  |
    | metal | 贵金属 | decimal(20,4) |  |
    | lend_capital | 拆出资金 | decimal(20,4) |  |
    | fairvalue_fianancial_asset | 以公允价值计量且其变动计入当期损益的金融资产 | decimal(20,4) |  |
    | other_grow_asset | 衍生金融资产 | decimal(20,4) |  |
    | bought_sellback_assets | 买入返售金融资产 | decimal(20,4) |  |
    | interest_receivable | 应收利息 | decimal(20,4) |  |
    | insurance_receivables | 应收保费 | decimal(20,4) |  |
    | recover_receivable | 应收代位追偿款 | decimal(20,4) |  |
    | separate_receivable | 应收分保帐款 | decimal(20,4) |  |
    | not_time_fund | 应收分保未到期责任准备金 | decimal(20,4) |  |
    | not_decide_fund | 应收分保未决赔款准备金 | decimal(20,4) |  |
    | response_fund | 应收分保寿险责任准备金 | decimal(20,4) |  |
    | health_fund | 应收分保长期健康险责任准备金 | decimal(20,4) |  |
    | margin_loan | 保户质押贷款 | decimal(20,4) |  |
    | deposit_period | 定期存款 | decimal(20,4) |  |
    | loan_and_advance | 发放贷款及垫款 | decimal(20,4) |  |
    | margin_out | 存出保证金 | decimal(20,4) |  |
    | agent_asset | 代理业务资产 | decimal(20,4) |  |
    | investment_reveiable | 应收款项类投资 | decimal(20,4) |  |
    | advance_payment | 预付款项 | decimal(20,4) |  |
    | hold_for_sale_assets | 可供出售金融资产 | decimal(20,4) |  |
    | hold_to_maturity_investments | 持有至到期投资 | decimal(20,4) |  |
    | longterm_equity_invest | 长期股权投资 | decimal(20,4) |  |
    | finance_out | 融出资金 | decimal(20,4) |  |
    | capital_margin_out | 存出资本保证金 | decimal(20,4) |  |
    | investment_property | 投资性房地产 | decimal(20,4) |  |
    | inventories | 存货 | decimal(20,4) |  |
    | fixed_assets | 固定资产 | decimal(20,4) |  |
    | constru_in_process | 在建工程 | decimal(20,4) |  |
    | intangible_assets | 无形资产 | decimal(20,4) |  |
    | trade_fee | 交易席位费 | decimal(20,4) |  |
    | long_deferred_expense | 长期待摊费用 | decimal(20,4) |  |
    | fixed_assets_liquidation | 固定资产清理 | decimal(20,4) |  |
    | independent_account_asset | 独立帐户资产 | decimal(20,4) |  |
    | deferred_tax_assets | 递延所得税资产 | decimal(20,4) |  |
    | other_asset | 其他资产 | decimal(20,4) |  |
    | total_assets | 资产总计 | decimal(20,4) |  |
    | borrowing_from_centralbank | 向中央银行借款 | decimal(20,4) |  |
    | deposit_in_ib_and_other | 同业及其他金融机构存放款项 | decimal(20,4) |  |
    | shortterm_loan | 短期借款 | decimal(20,4) |  |
    | loan_pledge | 其中：质押借款 | decimal(20,4) |  |
    | borrowing_capital | 拆入资金 | decimal(20,4) |  |
    | fairvalue_financial_liability | 以公允价值计量且其变动计入当期损益的金融负债 | decimal(20,4) |  |
    | derivative_financial_liability | 衍生金融负债 | decimal(20,4) |  |
    | sold_buyback_secu_proceeds | 卖出回购金融资产款 | decimal(20,4) |  |
    | deposit_absorb | 吸收存款 | decimal(20,4) |  |
    | proxy_secu_proceeds | 代理买卖证券款 | decimal(20,4) |  |
    | proxy_sell_proceeds | 代理承销证券款 | decimal(20,4) |  |
    | accounts_payable | 应付账款 | decimal(20,4) |  |
    | notes_payable | 应付票据 | decimal(20,4) |  |
    | advance_peceipts | 预收款项 | decimal(20,4) |  |
    | insurance_receive_early | 预收保费 | decimal(20,4) |  |
    | commission_payable | 应付手续费及佣金 | decimal(20,4) |  |
    | insurance_payable | 应付分保帐款 | decimal(20,4) |  |
    | salaries_payable | 应付职工薪酬 | decimal(20,4) |  |
    | taxs_payable | 应交税费 | decimal(20,4) |  |
    | interest_payable | 应付利息 | decimal(20,4) |  |
    | proxy_liability | 代理业务负债 | decimal(20,4) |  |
    | estimate_liability | 预计负债 | decimal(20,4) |  |
    | compensation_payable | 应付赔付款 | decimal(20,4) |  |
    | interest_insurance_payable | 应付保单红利 | decimal(20,4) |  |
    | investment_money | 保户储金及投资款 | decimal(20,4) |  |
    | not_time_reserve | 未到期责任准备金 | decimal(20,4) |  |
    | not_decide_reserve | 未决赔款准备金 | decimal(20,4) |  |
    | live_reserve | 寿险责任准备金 | decimal(20,4) |  |
    | longterm_reserve | 长期健康险责任准备金 | decimal(20,4) |  |
    | longterm_loan | 长期借款 | decimal(20,4) |  |
    | bonds_payable | 应付债券 | decimal(20,4) |  |
    | independent_account | 独立帐户负债 | decimal(20,4) |  |
    | deferred_tax_liability | 递延所得税负债 | decimal(20,4) |  |
    | other_liability | 其他负债 | decimal(20,4) |  |
    | total_liability | 负债合计 | decimal(20,4) |  |
    | paidin_capital | 实收资本(或股本) | decimal(20,4) |  |
    | capital_reserve_fund | 资本公积 | decimal(20,4) |  |
    | treasury_stock | 减：库存股 | decimal(20,4) |  |
    | surplus_reserve_fund | 盈余公积 | decimal(20,4) |  |
    | equities_parent_company_owners | 归属于母公司所有者权益 | decimal(20,4) |  |
    | retained_profit | 未分配利润 | decimal(20,4) |  |
    | minority_interests | 少数股东权益 | decimal(20,4) |  |
    | currency_mis | 外币报表折算差额 | decimal(20,4) |  |
    | total_owner_equities | 所有者权益合计 | decimal(20,4) |  |
    | total_liability_equity | 负债和所有者权益总计 | decimal(20,4) |  |
    | perferred_share_liability | 优先股-负债 | decimal(20,4) |  |
    | account_receivable | 应收账款 | decimal(20,4) |  |
    | other_equity_tools | 其他权益工具 | decimal(20,4) |  |
    | perferred_share_equity | 优先股-权益 | decimal(20,4) |  |
    | pep_debt_equity | 永续债-权益 | decimal(20,4) |  |
    | other_comprehensive_income | 其他综合收益 | decimal(20,4) |  |
    | good_will | 商誉 | decimal(20,4) |  |
    | shortterm_loan_payable | 应付短期融资款 | decimal(20,4) |  |
    | accounts_payable | 应付账款 | decimal(20,4) |  |
    | other_operate_cash_paid | 支付其他与经营活动有关的现金(元) | decimal(20, 4) |  |
    | subtotal_operate_cash_outflow | 经营活动现金流出小计(元) | decimal(20, 4) |  |
    | net_operate_cash_flow | 经营活动现金流量净额(元) | decimal(20, 4) |  |
    | invest_cash_flow | 投资活动产生的现金流量(元) | decimal(20, 4) |  |
    | invest_withdrawal_cash | 收回投资收到的现金(元) | decimal(20, 4) |  |
    | invest_proceeds | 取得投资收益收到的现金(元) | decimal(20, 4) |  |
    | other_cash_from_invest_act | 收到其他与投资活动有关的现金(元) | decimal(20, 4) |  |
    | gain_from_disposal | 处置固定资产、无形资产和其他长期资产所收回的现金(元) | decimal(20, 4) |  |
    | subtotal_invest_cash_inflow | 投资活动现金流入小计(元) | decimal(20, 4) |  |
    | long_deferred_expense | 长期待摊费用(元) | decimal(20, 4) |  |
    | contract_assets | 合同资产 | decimal(20,4) |  |
    | hold_sale_asset | 持有待售资产 | decimal(20,4) |  |
    | bond_invest | 债权投资 | decimal(20,4) |  |
    | other_bond_invest | 其他债权投资 | decimal(20,4) |  |
    | other_equity_tools_invest | 其他权益工具投资 | decimal(20,4) |  |
    | contract_liability | 合同负债 | decimal(20,4) |  |
    | usufruct_assets | 使用权资产 | decimal(20,4) |  |
    | liease_liability | 租赁负债 | decimal(20,4) |  |
    | ordinary_risk_reserve_fund | 一般风险准备 | decimal(20,4) |  |
    
- **报表来源编码**
    
    | 编码 | 名称 |
    | --- | --- |
    | 321001 | 招募说明书 |
    | 321002 | 上市公告书 |
    | 321003 | 定期报告 |
    | 321004 | 预披露公告 |
    | 321005 | 换股报告书 |
    | 321099 | 其他 |
    
- **filter(finance.FINANCE_BALANCE_SHEET.code==code)**：指定筛选条件，通过finance.FINANCE_BALANCE_SHEET.code==code可以指定你想要查询的股票代码；除此之外，还可以对表中其他字段指定筛选条件，如finance.FINANCE_BALANCE_SHEET.pub_date>='2015-01-01'，表示公告日期大于2015年1月1日金融类上市公司公布的合并资产负债信息；多个筛选条件用英文逗号分隔。
    
- **limit(n)**：限制返回的数据条数，n指定返回条数。
    

**返回结果：**

- 返回一个 dataframe，每一行对应数据表中的一条数据， 列索引是你所查询的字段名称

**注意：**

1.  **为了防止返回数据量过大, 我们每次最多返回4000行**
2.  不能进行连表查询，即同时查询多张表的数据

**示例：**

```python
#查询中国平安2015年之后公告的合并资产负债表数据，取出本期的货币资金，总资产和总负债
from jqdata import finance
q=query(finance.FINANCE_BALANCE_SHEET.company_name,
        finance.FINANCE_BALANCE_SHEET.code,
        finance.FINANCE_BALANCE_SHEET.pub_date,
        finance.FINANCE_BALANCE_SHEET.start_date,
        finance.FINANCE_BALANCE_SHEET.end_date,
        finance.FINANCE_BALANCE_SHEET.cash_equivalents,
        finance.FINANCE_BALANCE_SHEET.total_assets,
        finance.FINANCE_BALANCE_SHEET.total_liability
).filter(finance.FINANCE_BALANCE_SHEET.code=='601318.XSHG',finance.FINANCE_BALANCE_SHEET.pub_date>='2015-01-01',finance.FINANCE_BALANCE_SHEET.report_type==0).limit(20)
df=finance.run_query(q)
print(df)

        company_name         code    pub_date  start_date    end_date  \
0   中国平安保险(集团)股份有限公司  601318.XSHG  2015-03-20  2014-01-01  2014-12-31
1   中国平安保险(集团)股份有限公司  601318.XSHG  2015-04-30  2015-01-01  2015-03-31
2   中国平安保险(集团)股份有限公司  601318.XSHG  2015-08-21  2015-01-01  2015-06-30
3   中国平安保险(集团)股份有限公司  601318.XSHG  2015-10-28  2015-01-01  2015-09-30
4   中国平安保险(集团)股份有限公司  601318.XSHG  2016-03-16  2015-01-01  2015-12-31
5   中国平安保险(集团)股份有限公司  601318.XSHG  2016-04-27  2016-01-01  2016-03-31
6   中国平安保险(集团)股份有限公司  601318.XSHG  2016-08-18  2016-01-01  2016-06-30
7   中国平安保险(集团)股份有限公司  601318.XSHG  2016-10-28  2016-01-01  2016-09-30
8   中国平安保险(集团)股份有限公司  601318.XSHG  2017-03-23  2016-01-01  2016-12-31
9   中国平安保险(集团)股份有限公司  601318.XSHG  2017-04-28  2017-01-01  2017-03-31
10  中国平安保险(集团)股份有限公司  601318.XSHG  2017-08-18  2017-01-01  2017-06-30
11  中国平安保险(集团)股份有限公司  601318.XSHG  2017-10-28  2017-01-01  2017-09-30
12  中国平安保险(集团)股份有限公司  601318.XSHG  2018-03-21  2017-01-01  2017-12-31
13  中国平安保险(集团)股份有限公司  601318.XSHG  2018-04-27  2018-01-01  2018-03-31
14  中国平安保险(集团)股份有限公司  601318.XSHG  2018-08-22  2018-01-01  2018-06-30

    cash_equivalents  total_assets  total_liability
0       4.427070e+11  4.005911e+12     3.652095e+12
1       4.131880e+11  4.215240e+12     3.833842e+12
2       4.510800e+11  4.632287e+12     4.227789e+12
3       4.654240e+11  4.667113e+12     4.262293e+12
4       4.750570e+11  4.765159e+12     4.351588e+12
5       5.668130e+11  5.006993e+12     4.566653e+12
6       5.210790e+11  5.219782e+12     4.757190e+12
7       5.230110e+11  5.296564e+12     4.815950e+12
8       5.696830e+11  5.576903e+12     5.090442e+12
9       5.415870e+11  5.773318e+12     5.254793e+12
10      5.559020e+11  5.978688e+12     5.445990e+12
11      5.396110e+11  6.168516e+12     5.609576e+12
12      5.683990e+11  6.493075e+12     5.905158e+12
13      5.091390e+11  6.725766e+12     6.108353e+12
14      5.300420e+11  6.851431e+12     6.216339e+12
```

### 金融类母公司资产负债表

```
from jqdata import finance
finance.run_query(query(finance.FINANCE_BALANCE_SHEET_PARENT).filter(finance.FINANCE_BALANCE_SHEET_PARENT.code==code).limit(n))
```

获取金融类上市公司的母公司资产负债表信息

**参数：**

- **query(finance.FINANCE_BALANCE_SHEET_PARENT)**：表示从finance.FINANCE_BALANCE_SHEET_PARENT这张表中查询金融类上市公司母公司资产负债的字段信息，还可以指定所要查询的字段名，格式如下：query(库名.表名.字段名1，库名.表名.字段名2），多个字段用逗号分隔进行提取；query函数的更多用法详见：[sqlalchemy.orm.query.Query对象](http://docs.sqlalchemy.org/en/rel_1_0/orm/query.html)
    
- **finance.FINANCE_BALANCE_SHEET_PARENT**：代表金融类上市公司母公司资产负债表，收录了金融类上市公司的母公司资产负债，表结构和字段信息如下：
    
    | 字段名称 | 中文名称 | 字段类型 | 含义 |
    | --- | --- | --- | --- |
    | company_id | 公司ID | int |  |
    | company_name | 公司名称 | varchar(100) |  |
    | code | 公司主证券代码 | varchar(12) |  |
    | a_code | A股代码 | varchar(12) |  |
    | b_code | B股代码 | varchar(12) |  |
    | h_code | H股代码 | varchar(12) |  |
    | pub_date | 公告日期 | date |  |
    | start_date | 开始日期 | date |  |
    | end_date | 截止日期 | date |  |
    | report_date | 报告期 | date |  |
    | report_type | 报告期类型 | int | 0本期，1上期 |
    | source_id | 报表来源编码 | int | 如下[报表来源编码](#source12) |
    | source | 报表来源 | varchar(60) |  |
    | deposit_in_ib | 存放同业款项 | decimal(20,4) |  |
    | cash_equivalents | 货币资金 | decimal(20,4) |  |
    | deposit_client | 客户资金存款 | decimal(20,4) |  |
    | cash_in_cb | 现金及存放中央银行款项 | decimal(20,4) |  |
    | settlement_provi | 结算备付金 | decimal(20,4) |  |
    | settlement_provi_client | 客户备付金 | decimal(20,4) |  |
    | metal | 贵金属 | decimal(20,4) |  |
    | lend_capital | 拆出资金 | decimal(20,4) |  |
    | fairvalue_fianancial_asset | 以公允价值计量且其变动计入当期损益的金融资产 | decimal(20,4) |  |
    | other_grow_asset | 衍生金融资产 | decimal(20,4) |  |
    | bought_sellback_assets | 买入返售金融资产 | decimal(20,4) |  |
    | interest_receivable | 应收利息 | decimal(20,4) |  |
    | insurance_receivables | 应收保费 | decimal(20,4) |  |
    | recover_receivable | 应收代位追偿款 | decimal(20,4) |  |
    | separate_receivable | 应收分保帐款 | decimal(20,4) |  |
    | not_time_fund | 应收分保未到期责任准备金 | decimal(20,4) |  |
    | not_decide_fund | 应收分保未决赔款准备金 | decimal(20,4) |  |
    | response_fund | 应收分保寿险责任准备金 | decimal(20,4) |  |
    | health_fund | 应收分保长期健康险责任准备金 | decimal(20,4) |  |
    | margin_loan | 保户质押贷款 | decimal(20,4) |  |
    | deposit_period | 定期存款 | decimal(20,4) |  |
    | loan_and_advance | 发放贷款及垫款 | decimal(20,4) |  |
    | margin_out | 存出保证金 | decimal(20,4) |  |
    | agent_asset | 代理业务资产 | decimal(20,4) |  |
    | investment_reveiable | 应收款项类投资 | decimal(20,4) |  |
    | advance_payment | 预付款项 | decimal(20,4) |  |
    | hold_for_sale_assets | 可供出售金融资产 | decimal(20,4) |  |
    | hold_to_maturity_investments | 持有至到期投资 | decimal(20,4) |  |
    | longterm_equity_invest | 长期股权投资 | decimal(20,4) |  |
    | finance_out | 融出资金 | decimal(20,4) |  |
    | capital_margin_out | 存出资本保证金 | decimal(20,4) |  |
    | investment_property | 投资性房地产 | decimal(20,4) |  |
    | inventories | 存货 | decimal(20,4) |  |
    | fixed_assets | 固定资产 | decimal(20,4) |  |
    | constru_in_process | 在建工程 | decimal(20,4) |  |
    | intangible_assets | 无形资产 | decimal(20,4) |  |
    | trade_fee | 交易席位费 | decimal(20,4) |  |
    | long_deferred_expense | 长期待摊费用 | decimal(20,4) |  |
    | fixed_assets_liquidation | 固定资产清理 | decimal(20,4) |  |
    | independent_account_asset | 独立帐户资产 | decimal(20,4) |  |
    | deferred_tax_assets | 递延所得税资产 | decimal(20,4) |  |
    | other_asset | 其他资产 | decimal(20,4) |  |
    | total_assets | 资产总计 | decimal(20,4) |  |
    | borrowing_from_centralbank | 向中央银行借款 | decimal(20,4) |  |
    | deposit_in_ib_and_other | 同业及其他金融机构存放款项 | decimal(20,4) |  |
    | shortterm_loan | 短期借款 | decimal(20,4) |  |
    | loan_pledge | 其中：质押借款 | decimal(20,4) |  |
    | borrowing_capital | 拆入资金 | decimal(20,4) |  |
    | fairvalue_financial_liability | 以公允价值计量且其变动计入当期损益的金融负债 | decimal(20,4) |  |
    | derivative_financial_liability | 衍生金融负债 | decimal(20,4) |  |
    | sold_buyback_secu_proceeds | 卖出回购金融资产款 | decimal(20,4) |  |
    | deposit_absorb | 吸收存款 | decimal(20,4) |  |
    | proxy_secu_proceeds | 代理买卖证券款 | decimal(20,4) |  |
    | proxy_sell_proceeds | 代理承销证券款 | decimal(20,4) |  |
    | accounts_payable | 应付账款 | decimal(20,4) |  |
    | notes_payable | 应付票据 | decimal(20,4) |  |
    | advance_peceipts | 预收款项 | decimal(20,4) |  |
    | insurance_receive_early | 预收保费 | decimal(20,4) |  |
    | commission_payable | 应付手续费及佣金 | decimal(20,4) |  |
    | insurance_payable | 应付分保帐款 | decimal(20,4) |  |
    | salaries_payable | 应付职工薪酬 | decimal(20,4) |  |
    | taxs_payable | 应交税费 | decimal(20,4) |  |
    | interest_payable | 应付利息 | decimal(20,4) |  |
    | proxy_liability | 代理业务负债 | decimal(20,4) |  |
    | estimate_liability | 预计负债 | decimal(20,4) |  |
    | compensation_payable | 应付赔付款 | decimal(20,4) |  |
    | interest_insurance_payable | 应付保单红利 | decimal(20,4) |  |
    | investment_money | 保户储金及投资款 | decimal(20,4) |  |
    | not_time_reserve | 未到期责任准备金 | decimal(20,4) |  |
    | not_decide_reserve | 未决赔款准备金 | decimal(20,4) |  |
    | live_reserve | 寿险责任准备金 | decimal(20,4) |  |
    | longterm_reserve | 长期健康险责任准备金 | decimal(20,4) |  |
    | longterm_loan | 长期借款 | decimal(20,4) |  |
    | bonds_payable | 应付债券 | decimal(20,4) |  |
    | independent_account | 独立帐户负债 | decimal(20,4) |  |
    | deferred_tax_liability | 递延所得税负债 | decimal(20,4) |  |
    | other_liability | 其他负债 | decimal(20,4) |  |
    | total_liability | 负债合计 | decimal(20,4) |  |
    | paidin_capital | 实收资本(或股本) | decimal(20,4) |  |
    | capital_reserve_fund | 资本公积 | decimal(20,4) |  |
    | treasury_stock | 减：库存股 | decimal(20,4) |  |
    | surplus_reserve_fund | 盈余公积 | decimal(20,4) |  |
    | equities_parent_company_owners | 归属于母公司所有者权益 | decimal(20,4) |  |
    | retained_profit | 未分配利润 | decimal(20,4) |  |
    | minority_interests | 少数股东权益 | decimal(20,4) |  |
    | currency_mis | 外币报表折算差额 | decimal(20,4) |  |
    | total_owner_equities | 所有者权益合计 | decimal(20,4) |  |
    | total_liability_equity | 负债和所有者权益总计 | decimal(20,4) |  |
    | perferred_share_liability | 优先股-负债 | decimal(20,4) |  |
    | account_receivable | 应收账款 | decimal(20,4) |  |
    | other_equity_tools | 其他权益工具 | decimal(20,4) |  |
    | perferred_share_equity | 优先股-权益 | decimal(20,4) |  |
    | pep_debt_equity | 永续债-权益 | decimal(20,4) |  |
    | other_comprehensive_income | 其他综合收益 | decimal(20,4) |  |
    | good_will | 商誉 | decimal(20,4) |  |
    | shortterm_loan_payable | 应付短期融资款 | decimal(20,4) |  |
    | accounts_payable | 应付账款 | decimal(20,4) |  |
    | other_operate_cash_paid | 支付其他与经营活动有关的现金(元) | decimal(20, 4) |  |
    | subtotal_operate_cash_outflow | 经营活动现金流出小计(元) | decimal(20, 4) |  |
    | net_operate_cash_flow | 经营活动现金流量净额(元) | decimal(20, 4) |  |
    | invest_cash_flow | 投资活动产生的现金流量(元) | decimal(20, 4) |  |
    | invest_withdrawal_cash | 收回投资收到的现金(元) | decimal(20, 4) |  |
    | invest_proceeds | 取得投资收益收到的现金(元) | decimal(20, 4) |  |
    | other_cash_from_invest_act | 收到其他与投资活动有关的现金(元) | decimal(20, 4) |  |
    | gain_from_disposal | 处置固定资产、无形资产和其他长期资产所收回的现金(元) | decimal(20, 4) |  |
    | subtotal_invest_cash_inflow | 投资活动现金流入小计(元) | decimal(20, 4) |  |
    | long_deferred_expense | 长期待摊费用(元) | decimal(20, 4) |  |
    | contract_assets | 合同资产 | decimal(20,4) |  |
    | hold_sale_asset | 持有待售资产 | decimal(20,4) |  |
    | bond_invest | 债权投资 | decimal(20,4) |  |
    | other_bond_invest | 其他债权投资 | decimal(20,4) |  |
    | other_equity_tools_invest | 其他权益工具投资 | decimal(20,4) |  |
    | contract_liability | 合同负债 | decimal(20,4) |  |
    | usufruct_assets | 使用权资产 | decimal(20,4) |  |
    | liease_liability | 租赁负债 | decimal(20,4) |  |
    | ordinary_risk_reserve_fund | 一般风险准备 | decimal(20,4) |  |
    
- **报表来源编码**
    
    | 编码 | 名称 |
    | --- | --- |
    | 321001 | 招募说明书 |
    | 321002 | 上市公告书 |
    | 321003 | 定期报告 |
    | 321004 | 预披露公告 |
    | 321005 | 换股报告书 |
    | 321099 | 其他 |
    
- **filter(finance.FINANCE_BALANCE_SHEET_PARENT.code==code)**：指定筛选条件，通过finance.FINANCE_BALANCE_SHEET_PARENT.code==code可以指定你想要查询的股票代码；除此之外，还可以对表中其他字段指定筛选条件，如finance.FINANCE_BALANCE_SHEET_PARENT.pub_date>='2015-01-01'，表示公告日期大于2015年1月1日金融类上市公司公布的母公司资产负债信息；多个筛选条件用英文逗号分隔。
    
- **limit(n)**：限制返回的数据条数，n指定返回条数。
    

**返回结果：**

- 返回一个 dataframe，每一行对应数据表中的一条数据， 列索引是你所查询的字段名称

**注意：**

1.  **为了防止返回数据量过大, 我们每次最多返回4000行**
2.  不能进行连表查询，即同时查询多张表的数据

**示例：**

```python
#查询中国平安2015年之后公告的母公司资产负债表数据，取出本期的货币资金，总资产和总负债
from jqdata import finance
q=query(finance.FINANCE_BALANCE_SHEET_PARENT.company_name,
        finance.FINANCE_BALANCE_SHEET_PARENT.code,
        finance.FINANCE_BALANCE_SHEET_PARENT.pub_date,
        finance.FINANCE_BALANCE_SHEET_PARENT.start_date,
        finance.FINANCE_BALANCE_SHEET_PARENT.end_date,
        finance.FINANCE_BALANCE_SHEET_PARENT.cash_equivalents,
        finance.FINANCE_BALANCE_SHEET_PARENT.total_assets,
        finance.FINANCE_BALANCE_SHEET_PARENT.total_liability
).filter(finance.FINANCE_BALANCE_SHEET_PARENT.code=='601318.XSHG',finance.FINANCE_BALANCE_SHEET_PARENT.pub_date>='2015-01-01',finance.FINANCE_BALANCE_SHEET_PARENT.report_type==0).limit(20)
df=finance.run_query(q)
print(df)

       company_name         code    pub_date  start_date    end_date  \
0   中国平安保险(集团)股份有限公司  601318.XSHG  2015-03-20  2014-01-01  2014-12-31
1   中国平安保险(集团)股份有限公司  601318.XSHG  2015-04-30  2015-01-01  2015-03-31
2   中国平安保险(集团)股份有限公司  601318.XSHG  2015-08-21  2015-01-01  2015-06-30
3   中国平安保险(集团)股份有限公司  601318.XSHG  2015-10-28  2015-01-01  2015-09-30
4   中国平安保险(集团)股份有限公司  601318.XSHG  2016-03-16  2015-01-01  2015-12-31
5   中国平安保险(集团)股份有限公司  601318.XSHG  2016-04-27  2016-01-01  2016-03-31
6   中国平安保险(集团)股份有限公司  601318.XSHG  2016-08-18  2016-01-01  2016-06-30
7   中国平安保险(集团)股份有限公司  601318.XSHG  2016-10-28  2016-01-01  2016-09-30
8   中国平安保险(集团)股份有限公司  601318.XSHG  2017-03-23  2016-01-01  2016-12-31
9   中国平安保险(集团)股份有限公司  601318.XSHG  2017-04-28  2017-01-01  2017-03-31
10  中国平安保险(集团)股份有限公司  601318.XSHG  2017-08-18  2017-01-01  2017-06-30
11  中国平安保险(集团)股份有限公司  601318.XSHG  2017-10-28  2017-01-01  2017-09-30
12  中国平安保险(集团)股份有限公司  601318.XSHG  2018-03-21  2017-01-01  2017-12-31
13  中国平安保险(集团)股份有限公司  601318.XSHG  2018-04-27  2018-01-01  2018-03-31
14  中国平安保险(集团)股份有限公司  601318.XSHG  2018-08-22  2018-01-01  2018-06-30

    cash_equivalents  total_assets  total_liability
0        26214000000  1.970230e+11      17331000000
1        25899000000  1.980580e+11       8930000000
2        20809000000  2.096090e+11      16105000000
3         8815000000  2.004830e+11       9538000000
4        10179000000  2.033480e+11      10805000000
5         9906000000  2.031290e+11      10349000000
6        10234000000  2.155980e+11      15577000000
7        10453000000  2.069940e+11      10585000000
8        10028000000  2.203310e+11       9205000000
9         8923000000  2.183790e+11       7200000000
10       14429000000  2.291570e+11      15987000000
11       11133000000  2.264570e+11      19084000000
12       19039000000  2.351180e+11      12990000000
13       18961000000  2.356310e+11      13536000000
14       15981000000  2.454330e+11      23082000000
```