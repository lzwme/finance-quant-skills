## 获取期权数据

**注意**

- 目前只提供期权数据，暂时还不支持期权的回测、模拟及实盘。
- query函数的更多用法详见：[Query的简单教程](https://www.joinquant.com/view/community/detail/433d0e9ed9fed11fc9f7772eab8d9376)
- [期权数据获取教程>>>](https://www.joinquant.com/view/community/detail/c0f06b43c15a2f46939cf1239a6274db?type=1)
- 有关目前提供的300ETF期权数据说明：（1）行情数据：上交所和中金所有天、分钟和tick频率的，深交所目前只有天频率的（OPT_DAILY_PRICE）；（2）OPT_TRADE_RANK_STK：上交所和深交所；OPT_DAILY_PREOPEN：上交所；OPT_DAILY_PRICE： 全部；OPT_RISK_INDICATOR：全部；OPT_CONTRACT_INFO：全部；OPT_ADJUSTMENT：上交所；OPT_EXERCISE_INFO：上交所；

### 获取期权合约资料

```python
from jqdata import *
opt.run_query(query(opt.OPT_CONTRACT_INFO).filter(opt.OPT_CONTRACT_INFO.code==code).limit(n))
```

描述：记录ETF期权，300股指期权，铜期权，白糖期权、豆粕期权等自上市以来的所有合约资料，包括合约代码，挂牌日期，开盘参考价等，为回测研究提供最基础的合约信息

**参数：**

- **query(opt.OPT_CONTRACT_INFO)**：表示从opt.OPT_CONTRACT_INFO这张表中查询期权基本资料数据，还可以指定所要查询的字段名，格式如下：query(库名.表名.字段名1，库名.表名.字段名2），多个字段用逗号分隔进行提取；query函数的更多用法详见：[sqlalchemy.orm.query.Query对象](http://docs.sqlalchemy.org/en/rel_1_0/orm/query.html)
- **opt.OPT_CONTRACT_INFO**：收录了期权基本资料数据，表结构和字段信息如下：

**字段设计**

| **名称** | **类型** | **描述** | **示例** | **备注** |
| --- | --- | --- | --- | --- |
| code | str | 合约代码 | 10001313.XSHG；CU1901C46000.XSGE；SR903C4700.XZCE；M1707-C-2400.XDCE | 注意合约代码使用大写字母 |
| trading_code | str | 合约交易代码 | 510050C1810M02800 | 合约调整会产生新的交易代码 |
| name | str | 合约简称 | 50ETF购10月2800豆粕购7月2400 | 合约调整会产生新的合约简称 |
| contract_type | str | 合约类型。CO-认购期权，PO-认沽期权 | CO |  |
| exchange_code | str | 证券市场编码，XSHG：上海证券交易所；XSGE：上海期货交易所；XZCE：郑州商品交易所；XDCE：大连商品交易所；CCFX：中国金融期货交易所 | XSHG |  |
| currency_id | str | 货币代码CNY-人民币 | CNY |  |
| underlying_symbol | str | 标的代码 | 510050.XSHG |  |
| underlying_name | str | 标的简称 | 华夏上证50ETF |  |
| underlying_exchange | str | 标的交易市场 | XSHG |  |
| underlying_type | str | 标的品种类别。ETF-交易型开放式指数基金FUTURE-期货 | ETF |  |
| exercise_price | float | 行权价格 | 2.8 | 合约调整会产生新的行权价格 |
| contract_unit | int | 合约单位 | 10000 | 合约调整会产生新的合约单位 |
| contract_status | str | 合约状态：LIST-上市、DELIST-退市。SUSPEND-停牌 | DELIST | 新期权上市由交易所公布LIST：挂牌日期<=当前日期<=最后交易日DELIST：当前日期>最后交易日 |
| list_date | str | 挂牌日期 | 2018-09-25 |  |
| list_reason | str | 合约挂牌原因 |  |  |
| list_price | decimal(20,4) | 开盘参考价 |  | 合约挂牌当天交易所会公布 |
| high_limit | decimal(20,4) | 挂牌涨停价 |  | 合约挂牌当天交易所会公布 |
| low_limit | decimal(20,4) | 挂牌跌停价 |  | 合约上市当天交易所会公布 |
| expire_date | str | 到期日 | 2018/10/24 |  |
| last_trade_date | str | 最后交易日 | 2018/10/24 |  |
| exercise_date | str | 行权日 | 2018/10/24 | 50ETF，铜期权是欧式期权，行权日固定。白糖期权和豆粕期权是美式期权，到期日之前都可以行权，行权日不固定，可为空。 |
| delivery_date | str | 交收日期 | 2018/10/25 |  |
| is_adjust | int | 是否调整 |  | 原合约调整为新的合约会发生合约资料的变化1-是，0-否 |
| delist_date | str | 摘牌日期 | 2018/10/24 |  |
| delist_reason | str | 合约摘牌原因 |  |  |

- **filter(opt.OPT_CONTRACT_INFO.code==code)**：指定筛选条件，通过opt.OPT_CONTRACT_INFO.code==code可以指定你想要查询的合约代码；除此之外，还可以对表中其他字段指定筛选条件；多个筛选条件用英文逗号分隔。
- **limit(n)**：限制返回的数据条数，n指定返回条数。

**返回结果：**

- 返回一个 dataframe，每一行对应数据表中的一条数据， 列索引是您所查询的字段名称

**注意：**

1.  **为了防止返回数据量过大, 我们每次最多返回3000行**
2.  不能进行连表查询，即同时查询多张表的数据

**示例：**

```
# 查询当前可交易的50ETF期权合约信息
# 回测/模拟交易中将datetime.now()换成context.current_dt

from jqdata import *
from datetime import datetime
opt.run_query(query(opt.OPT_CONTRACT_INFO).filter((opt.OPT_CONTRACT_INFO.underlying_symbol == "510050.XSHG") & (opt.OPT_CONTRACT_INFO.last_trade_date > datetime.now())))
```

```python
#查询("10001313.XSHG ")最新的期权基本资料数据。
from jqdata import *
q=query(opt.OPT_CONTRACT_INFO).filter(opt.OPT_CONTRACT_INFO.code=='10001313.XSHG')
df=opt.run_query(q)
print(df)

     id           code       trading_code            name contract_type  \
0  2435  10001313.XSHG  510050C1812A02500  50ETF购12月2450A            CO

  exchange_code currency_id underlying_symbol underlying_name  \
0          XSHG         CNY       510050.XSHG           50ETF

  underlying_exchange      ...      list_price  high_limit  low_limit  \
0                XSHG      ...          0.3523      0.6216      0.083

  expire_date last_trade_date exercise_date  delivery_date  is_adjust  \
0  2018-12-26      2018-12-26    2018-12-26     2018-12-27          1

   delist_date delist_reason
0         None          None
```

### 获取期权合约调整记录

```python
from jqdata  import *
opt.run_query(query(opt.OPT_ADJUSTMENT).filter(opt.OPT_ADJUSTMENT.code==code).limit(n))
```

描述：记录ETF期权因分红除息所带来的期权交易代码，合约简称，合约单位，行权价格的变化

**参数：**

- **query(opt.OPT_ADJUSTMENT)**：表示从opt.OPT_ADJUSTMENT这张表中查询期权合约调整数据，还可以指定所要查询的字段名，格式如下：query(库名.表名.字段名1，库名.表名.字段名2），多个字段用逗号分隔进行提取；query函数的更多用法详见：[sqlalchemy.orm.query.Query对象](http://docs.sqlalchemy.org/en/rel_1_0/orm/query.html)
- **opt.OPT_ADJUSTMENT**：收录了期权合约调整数据，表结构和字段信息如下：

**字段设计**

| **名称** | **类型** | **描述** | **示例** | **备注** |
| --- | --- | --- | --- | --- |
| code | str | 合约代码 | 10001313.XSHG; |  |
| adj_date | date | 调整日期 |  |  |
| contract_type | str | 合约类型。CO-认购期权，PO-认沽期权 | CO |  |
| ex_trading_code | str | 原交易代码 | 510050C1812M02500 | 合约调整会产生新的交易代码 |
| ex_name | str | 原合约简称 | 50ETF购10月2800豆粕购7月2400 | 合约调整会产生新的合约简称 |
| ex_exercise_price | float | 原行权价 |  |  |
| ex_contract_unit | int | 原合约单位 |  |  |
| new_trading_code | str | 新交易代码 | 510050C1812A02500 |  |
| new_name | str | 新合约简称 |  |  |
| new_exercise_price | float | 新行权价 |  |  |
| new_contract_unit | int | 新合约单位 |  |  |
| adj_reason | str | 调整原因 |  |  |
| expire_date | str | 到期日 | 2018/10/24 |  |
| last_trade_date | str | 最后交易日 | 2018/10/24 |  |
| exercise_date | str | 行权日 | 2018/10/24 | 50ETF期权是欧式期权，行权日固定 |
| delivery_date | str | 交收日期 | 2018/10/25 |  |
| position | int | 合约持仓 |  |  |

- **filter(opt.OPT_ADJUSTMENT.code==code)**：指定筛选条件，通过opt.OPT_ADJUSTMENT.code==code可以指定你想要查询的合约代码；除此之外，还可以对表中其他字段指定筛选条件；多个筛选条件用英文逗号分隔。
- **limit(n)**：限制返回的数据条数，n指定返回条数。

**返回结果：**

- 返回一个 dataframe，每一行对应数据表中的一条数据， 列索引是您所查询的字段名称

**注意：**

1.  **为了防止返回数据量过大, 我们每次最多返回3000行**
2.  不能进行连表查询，即同时查询多张表的数据

**示例：**

```python
#查询("10001313.XSHG ")最新的期权合约调整记录。
from jqdata import *
q=query(opt.OPT_ADJUSTMENT).filter(opt.OPT_ADJUSTMENT.code=='10001313.XSHG')
df=opt.run_query(q)
print(df)

   id           code    adj_date contract_type    ex_trading_code  \
0  70  10001313.XSHG  2018-12-03            CO  510050C1812M02500

         ex_name  ex_exercise_price  ex_contract_unit   new_trading_code  \
0  50ETF购12月2500                2.5             10000  510050C1812A02500

         new_name  new_exercise_price  new_contract_unit adj_reason  \
0  50ETF购12月2450A                2.45              10202         除息

  expire_date last_trade_date exercise_date delivery_date  position
0  2018-12-26      2018-12-26    2018-12-26    2018-12-27    107928
```

### 获取期权每日盘前静态文件

```python
from jqdata import *
opt.run_query(query(opt.OPT_DAILY_PREOPEN).filter(opt.OPT_DAILY_PREOPEN.code==code).limit(n))
```

描述：提供ETF期权每日交易的基本参数，包含合约单位，行权价格，持仓量，涨跌停价等数据

**参数：**

- **query(opt.OPT_DAILY_PREOPEN)**：表示从opt.OPT_DAILY_PREOPEN这张表中查询期权每日盘前静态数据，还可以指定所要查询的字段名，格式如下：query(库名.表名.字段名1，库名.表名.字段名2），多个字段用逗号分隔进行提取；query函数的更多用法详见：[sqlalchemy.orm.query.Query对象](http://docs.sqlalchemy.org/en/rel_1_0/orm/query.html)
- **opt.OPT_DAILY_PREOPEN**：收录了期权每日盘前静态数据，表结构和字段信息如下：

**字段设计**

| **名称** | **类型** | **描述** | **示例** | **备注** |
| --- | --- | --- | --- | --- |
| date | str | 交易日期 | 2018-11-09 |  |
| code | str | 合约代码 | 10001313.XSHG |  |
| trading_code | str | 合约交易代码 | 510050C1812M02500 | 保留，每个交易日仍然存在一 一对应关系 |
| name | str | 合约简称 | 50ETF购12月2500 | 保留，每个交易日仍然存在一 一对应关系 |
| exchange_code | str | 证券市场编码XSHG:上海证券交易所 | XSHG |  |
| underlying_symbol | str | 标的代码 | 510050.XSHG |  |
| underlying_name | str | 标的名称 | 50ETF |  |
| underlying_exchange | str | 标的交易市场 | XSHG |  |
| underlying_type | str | 标的品种类别，STOCK：股票；ETF：交易型开放式指数基金；FUTURE：期货 | F |  |
| exercise_type | str | 期权履约方式:A 美式;E 欧式 | E |  |
| contract_type | str | 合约类型。CO-认购期权，PO-认沽期权 | CO |  |
| contract_unit | int | 合约单位 | 10000 |  |
| exercise_price | float | 行权价格 | 2.5 |  |
| list_date | str | 挂牌日期 | 2018/4/26 |  |
| last_trade_date | str | 最后交易日 | 2018/12/26 |  |
| exercise_date | str | 行权日 | 2018/12/26 |  |
| delivery_date | str | 交收日期 | 2018/12/27 |  |
| expire_date | str | 到期日 | 2018/12/26 |  |
| contract_version | str | 合约版本号 | 0 |  |
| position | int | 持仓量 | 13630 |  |
| pre_close | float | 前收盘价 | 0.1391 |  |
| pre_settle | float | 前结算价 | 0.1391 |  |
| pre_close_underlying | float | 标的证券前收盘 | 2.537 |  |
| is_limit | str | 涨跌幅限类型，“N”为有涨跌幅限制,深交所无此字段 | N |  |
| high_limit | float | 涨停价 | 0.3928 |  |
| low_limit | float | 跌停价 | 0.0001 |  |
| margin_unit | float | 单位保证金 | 4435.4 |  |
| margin_ratio_1 | float | 保证金计算比例参数一 | 12 |  |
| margin_ratio_2 | float | 保证金计算比例参数二 | 7 |  |
| round_lot | int | 整手数 | 1 |  |
| limit_order_min | int | 单笔限价申报下限,深交所无此字段 | 1 |  |
| limit_order_max | int | 单笔限价申报上限,深交所无此字段 | 30 |  |
| market_order_min | int | 单笔市价申报下限,深交所无此字段 | 1 |  |
| market_order_max | int | 单笔市价申报上限,深交所无此字段 | 10 |  |
| quote_change_min | float | 最小报价变动(数值) | 0.0001 |  |
| contract_status | str | 合约状态信息,深交所无此字段 | 0000E | 该字段为8位字符串，左起每位表示特定的含义，无定义则填空格。第1位：‘0’表示可开仓，‘1’表示限制卖出开仓（不.包括备兑开仓）和买入开仓。第2位：‘0’表示未连续停牌，‘1’表示连续停牌。（预留，暂填0）第3位：‘0’表示未临近到期日，‘1’表示距离到期日不足5个交易日。第4位：‘0’表示近期未做调整，‘1’表示最近5个交易日内合约发生过调整。第5位：‘A’表示当日新挂牌的合约，‘E’表示存续的合约 |

- **filter(opt.OPT_DAILY_PREOPEN.code==code)**：指定筛选条件，通过opt.OPT_DAILY_PREOPEN.code==code可以指定你想要查询的合约代码；除此之外，还可以对表中其他字段指定筛选条件；多个筛选条件用英文逗号分隔。
- **limit(n)**：限制返回的数据条数，n指定返回条数。

**返回结果：**

- 返回一个 dataframe，每一行对应数据表中的一条数据， 列索引是您所查询的字段名称

**注意：**

1.  **为了防止返回数据量过大, 我们每次最多返回3000行**
2.  不能进行连表查询，即同时查询多张表的数据

**示例：**

```python
#查询("10001313.XSHG ")最新的期权每日盘前静态数据。
from jqdata import *
q=query(opt.OPT_DAILY_PREOPEN.code,
        opt.OPT_DAILY_PREOPEN.trading_code,
        opt.OPT_DAILY_PREOPEN.name,
opt.OPT_DAILY_PREOPEN.exercise_date,).filter(opt.OPT_DAILY_PREOPEN.code=='10001313.XSHG').order_by(opt.OPT_DAILY_PREOPEN.date.desc()).limit(10)
df=opt.run_query(q)
print(df)

               code       trading_code              name exercise_date
0   10001313.XSHG  510050C1812A02500    50ETF购12月2450A    2018-12-26
1   10001313.XSHG  510050C1812A02500    50ETF购12月2450A    2018-12-26
2   10001313.XSHG  510050C1812A02500    50ETF购12月2450A    2018-12-26
3   10001313.XSHG  510050C1812A02500  XD50ETF购12月2450A    2018-12-26
4   10001313.XSHG  510050C1812M02500     50ETF购12月2500    2018-12-26
5   10001313.XSHG  510050C1812M02500     50ETF购12月2500    2018-12-26
6   10001313.XSHG  510050C1812M02500     50ETF购12月2500    2018-12-26
7   10001313.XSHG  510050C1812M02500     50ETF购12月2500    2018-12-26
8   10001313.XSHG  510050C1812M02500     50ETF购12月2500    2018-12-26
9   10001313.XSHG  510050C1812M02500     50ETF购12月2500    2018-12-26
```

### 获取期权日行情数据

```python
from jqdata import *
opt.run_query(query(opt.OPT_DAILY_PRICE).filter(opt.OPT_DAILY_PRICE.code==code).limit(n))
```

描述：提供期权每日开盘价，收盘价，最高价，最低价，成交量，成交额，涨跌幅，持仓量等日行情数据。

**参数：**

- **query(opt.OPT_DAILY_PRICE)**：表示从opt.OPT_DAILY_PRICE这张表中查询期权日行情数据，还可以指定所要查询的字段名，格式如下：query(库名.表名.字段名1，库名.表名.字段名2），多个字段用逗号分隔进行提取；query函数的更多用法详见：[sqlalchemy.orm.query.Query对象](http://docs.sqlalchemy.org/en/rel_1_0/orm/query.html)
- **opt.OPT_DAILY_PRICE**：收录了期权日行情数据，表结构和字段信息如下：

**字段设计**

| **名称** | **类型** | **描述** | **示例** | **备注** |
| --- | --- | --- | --- | --- |
| code | str | 合约代码 | 10001313.XSHG；CU1901C46000.XSGE；SR903C4700.XZCE；M1707-C-2400.XDCE | 合约代码使用大写字母 |
| exchange_code | str | 证券市场编码，XSHG：上海证券交易所；XSGE：上海期货交易所；XZCE：郑州商品交易所；XDCE：大连商品交易所 | XSHG |  |
| date | str | 交易日期 | 2018/10/25 |  |
| pre_settle | float | 前结算价 | 0.1997 |  |
| pre_close | float | 前收价 | 0.1997 |  |
| open | float | 今开盘 | 0.1683 |  |
| high | float | 最高价 | 0.2072 |  |
| low | float | 最低价 | 0.1517 |  |
| close | float | 收盘价 | 0.2035 |  |
| change_pct_close | float | 收盘价涨跌幅(%） |  | 收盘价/前结算价 |
| settle_price | float | 结算价 | 0.204 | 收盘价是一天交易的最后一个价,它是由于收盘前1分钟所有买卖盘集中撮合而成 ；结算价：原则上，期权合约的结算价格为该合约当日收盘集合竞价的成交价格。但是，如果当日收盘集合竞价未形成成交价格，或者成交价格明显不合理（比如价格倒挂），那么上交所就会考虑期权交易的多重影响因素，另行计算合约的结算价格。即根据同标的、同到期日、同类型其他行权价的期权合约隐含波动率，推算该合约隐含波动率，并以此计算该合约结算价。 |
| change_pct_settle | float | 结算价涨跌幅(%) |  | 结算价/前结算价 |
| volume | float | 成交量（张） | 3126 |  |
| money | float | 成交金额（元） | 5620827 |  |
| position | int | 持仓量 | 5095 |  |

- **filter(opt.OPT_DAILY_PRICE.code==code)**：指定筛选条件，通过opt.OPT_DAILY_PRICE.code==code可以指定你想要查询的合约代码；除此之外，还可以对表中其他字段指定筛选条件；多个筛选条件用英文逗号分隔。
- **limit(n)**：限制返回的数据条数，n指定返回条数。

**返回结果：**

- 返回一个 dataframe，每一行对应数据表中的一条数据， 列索引是您所查询的字段名称

**注意：**

1.  **为了防止返回数据量过大, 我们每次最多返回3000行**
2.  不能进行连表查询，即同时查询多张表的数据

**示例：**

```python
#查询上证50ETF期权（'10001313.XSHG')最近10个交易日的日行情数据。
from jqdata import *
q=query(opt.OPT_DAILY_PRICE).filter(opt.OPT_DAILY_PRICE.code=='10001313.XSHG').order_by(opt.OPT_DAILY_PRICE.date.desc()).limit(10)
df=opt.run_query(q)
print(df)

      id           code exchange_code        date  pre_settle  pre_close  \
0  321643  10001313.XSHG          XSHG  2018-12-05      0.0797     0.0797
1  320840  10001313.XSHG          XSHG  2018-12-04      0.0788     0.0788
2  320046  10001313.XSHG          XSHG  2018-12-03      0.0592     0.0604
3  319315  10001313.XSHG          XSHG  2018-11-30      0.0510     0.0510
4  318593  10001313.XSHG          XSHG  2018-11-29      0.0550     0.0550
5  317860  10001313.XSHG          XSHG  2018-11-28      0.0468     0.0468
6  317132  10001313.XSHG          XSHG  2018-11-27      0.0553     0.0553
7  316364  10001313.XSHG          XSHG  2018-11-26      0.0595     0.0595
8  315590  10001313.XSHG          XSHG  2018-11-23      0.0783     0.0783
9  314816  10001313.XSHG          XSHG  2018-11-22      0.0892     0.0892

     open    high     low   close  change_pct_close  settle_price  \
0  0.0673  0.0785  0.0664  0.0716          -10.1631        0.0716
1  0.0780  0.0821  0.0701  0.0797            1.1421        0.0797
2  0.0880  0.0919  0.0749  0.0788           33.1081        0.0788
3  0.0500  0.0620  0.0497  0.0604           18.4314        0.0604
4  0.0613  0.0629  0.0480  0.0510           -7.2727        0.0510
5  0.0468  0.0577  0.0460  0.0550           17.5214        0.0550
6  0.0589  0.0603  0.0455  0.0468          -15.3707        0.0468
7  0.0612  0.0676  0.0506  0.0553           -7.0588        0.0553
8  0.0784  0.0799  0.0589  0.0595          -24.0102        0.0595
9  0.0923  0.0931  0.0718  0.0783          -12.2197        0.0783

   change_pct_settle    volume       money  position
0           -10.1631   44938.0  33451080.0     72717
1             1.1421   55720.0  43805151.0     74468
2            33.1081  106122.0  90415448.0     81186
3            18.4314  146824.0  82267433.0    107928
4            -7.2727  139922.0  78418357.0    122002
5            17.5214   94165.0  49885293.0     97160
6           -15.3707   83460.0  44309064.0     96531
7            -7.0588   78105.0  46594632.0     75401
8           -24.0102   63644.0  42066470.0     64213
9           -12.2197   41977.0  33248317.0     46825
```

### 获取期权分钟行情(仅本地数据提供)

```python
get_price(security, start_date=None, end_date=None, frequency='daily', fields=None, skip_paused=False, count=None)
```

获取期权的历史行情, 按天或者按分钟，这里在使用时注意 end_date 的设置，不要引入未来的数据；其中50ETF期权从2017-01-01开始，商品期权从2019-12-02开始。 **注意**

- 仅[本地数据](https://www.joinquant.com/help/api/doc?name=JQDatadoc)提供

**参数**

- security: 期权合约代码；如security='10001979.XSHG' #50ETF期权，上海证券交易所；security='CU2001C42000.XSGE'#铜期权，上海期货交易所； security='SR003C5600.XZCE' #白糖期权，郑州商品交易所； security='M2005-P-2400.XDCE' #豆粕期权，大连商品交易所；
    
- count: **与 start_date 二选一，不可同时使用**. 数量, 返回的结果集的行数, 即表示获取 end_date 之前几个 frequency 的数据
    
- start_date: **与 count 二选一，不可同时使用**. 字符串或者 [datetime.datetime]/[datetime.date] 对象, 开始时间.
    
    -   如果 count 和 start_date 参数都没有, 则 start_date 生效, 值是 '2015-01-01'. 注意:
    -   当取分钟数据时, 时间可以精确到分钟, 比如: 传入 `datetime.datetime(2015, 1, 1, 10, 0, 0)` 或者 `'2015-01-01 10:00:00'`.
    -   当取分钟数据时, 如果只传入日期, 则日内时间是当日的 00:00:00.
    -   当取天数据时, 传入的日内时间会被忽略
- end_date: 格式同上, 结束时间, 默认是'2015-12-31', 包含此日期. **注意: 当取分钟数据时, 如果 end_date 只有日期, 则日内时间等同于 00:00:00, 所以返回的数据是不包括 end_date 这一天的**.
    
- frequency: 单位时间长度, 几天或者几分钟, 现在支持'Xd','Xm', 'daily'(等同于'1d'), 'minute'(等同于'1m'), X是一个正整数, 分别表示X天和X分钟(不论是按天还是按分钟回测都能拿到这两种单位的数据), 注意, 当X > 1时, fields只支持['open', 'close', 'high', 'low', 'volume', 'money']这几个标准字段. 默认值是daily
    
- fields: 字符串list, 选择要获取的行情数据字段, 默认是None(表示['open', 'close', 'high', 'low', 'volume', 'money']这几个标准字段), 支持SecurityUnitData里面的所有基本属性,，包含：['open', ' close', 'low', 'high', 'volume', 'money', 'high_limit',' low_limit', 'avg', ' pre_close', 'open_interest'(持仓量)]
    
- skip_paused: 是否跳过不交易日期(包括停牌, 未上市或者退市后的日期). 如果不跳过, 停牌时会使用停牌前的数据填充(具体请看SecurityUnitData的paused属性), 上市前或者退市后数据都为 nan, 但要注意:
    
    -   默认为 False
    -   当 skip_paused 是 True 时, 只能取一只期权的信息 **关于停牌**: 因为此API可以获取多只期权的数据, 可能有的期权停牌有的没有, 为了保持时间轴的一致,我们默认没有跳过停牌的日期, 停牌时使用停牌前的数据填充(请看 SecurityUnitData 的 paused 属性). 如想跳过, 请使用 skip_paused=True 参数, 同时只取一只期权的信息

**返回结果** 返回pandas.DataFrame对象, 行索引是datetime.datetime对象, 列索引是行情字段名字

- **示例**

```python
# 获取10001313.XSHG期权合约的分钟行情
p=get_price('10001313.XSHG','2018-12-21 09:00:00','2018-12-21 12:00:00','1m')
print(p)

                       open   close    high     low  volume     money
2018-12-21 09:31:00  0.0038  0.0034  0.0040  0.0034   310.0  11407.88
2018-12-21 09:32:00  0.0034  0.0032  0.0034  0.0032   169.0   5760.05
2018-12-21 09:33:00  0.0032  0.0033  0.0034  0.0032   228.0   7647.41
2018-12-21 09:34:00  0.0033  0.0031  0.0033  0.0031   446.0  14496.03
2018-12-21 09:35:00  0.0031  0.0031  0.0031  0.0030   340.0  10581.51
2018-12-21 09:36:00  0.0028  0.0030  0.0030  0.0028   611.0  18203.43
2018-12-21 09:37:00  0.0028  0.0031  0.0031  0.0028   528.0  15954.91
2018-12-21 09:38:00  0.0031  0.0031  0.0033  0.0031   409.0  13138.13
...
2018-12-21 11:15:00  0.0023  0.0023  0.0023  0.0023   134.0   3157.52
2018-12-21 11:16:00  0.0023  0.0022  0.0023  0.0020   181.0   3969.59
2018-12-21 11:17:00  0.0021  0.0021  0.0022  0.0021    99.0   2128.14
2018-12-21 11:18:00  0.0022  0.0022  0.0022  0.0022     8.0    179.56
2018-12-21 11:19:00  0.0022  0.0023  0.0023  0.0022    62.0   1442.56
2018-12-21 11:20:00  0.0023  0.0025  0.0025  0.0023    87.0   2210.77
2018-12-21 11:21:00  0.0025  0.0026  0.0026  0.0025    12.0    307.08
2018-12-21 11:22:00  0.0025  0.0025  0.0025  0.0025    25.0    637.63
2018-12-21 11:23:00  0.0026  0.0025  0.0026  0.0025    62.0   1627.22
2018-12-21 11:24:00  0.0025  0.0025  0.0025  0.0025    45.0   1147.72
2018-12-21 11:25:00  0.0023  0.0025  0.0025  0.0023    15.0    372.37
2018-12-21 11:26:00  0.0023  0.0023  0.0025  0.0023   127.0   3122.84
2018-12-21 11:27:00  0.0023  0.0025  0.0025  0.0023    19.0    473.37
2018-12-21 11:28:00  0.0025  0.0023  0.0025  0.0023    40.0   1018.16
2018-12-21 11:29:00  0.0025  0.0025  0.0025  0.0025    43.0   1096.71
2018-12-21 11:30:00  0.0023  0.0023  0.0023  0.0023    48.0   1175.27
```

### 获取指定时间周期的期权行情(仅本地数据提供)

```python
get_bars(security, count, unit='1d',
         fields=['date','open','high','low','close'],
         include_now=False, end_dt=None)
```

获取各种时间周期的bar数据，bar的分割方式与主流行情软件相同， 同时还支持返回当前时刻所在 bar 的数据。其中50ETF期权从2017-01-01开始，商品期权从2019-12-02开始。 **注意**

- 仅[本地数据](https://www.joinquant.com/help/api/doc?name=JQDatadoc)提供

**参数**

- security: 期权合约代码；如security='10001979.XSHG' #50ETF期权，上海证券交易所；security='CU2001C42000.XSGE'#铜期权，上海期货交易所； security='SR003C5600.XZCE' #白糖期权，郑州商品交易所； security='M2005-P-2400.XDCE' #豆粕期权，大连商品交易所；
- count: 大于0的整数，表示获取bar的个数。如果行情数据的bar不足count个，返回的长度则小于count个数。
- unit: bar的时间单位, 支持如下周期：'1m', '5m', '15m', '30m', '60m', '120m', '1d', '1w', '1M'。其中m表示分钟，d表示天，w表示周，M表示月。
- fields: 获取数据的字段， 支持如下值：'date', 'open', 'close', 'high', 'low', 'volume', 'money'。
- include_now: 取值True 或者False。 表示是否包含当前bar, 比如策略时间是9:33，unit参数为5m， 如果 include_now=True,则返回9:30-9:33这个分钟 bar。
- end_dt：查询的截止时间，支持的类型为datetime.datetime或None，默认为datetime.now()。

**返回**

返回一个pandas.dataframe对象，可以按任意周期返回期权合约的开盘价、收盘价、最高价、最低价，同时也可以利用date数据查看所返回的数据是什么时刻的。

**示例**

```python
#获取指定时间周期为5m的期权行情数据
df = get_bars('10001313.XSHG',10,'5m',fields=['date','open','high','low','close'],end_dt='2018-12-21 15:00:00')
print(df)

                 date    open    high     low   close
0 2018-12-21 14:10:00  0.0019  0.0022  0.0018  0.0021
1 2018-12-21 14:15:00  0.0022  0.0023  0.0019  0.0019
2 2018-12-21 14:20:00  0.0019  0.0022  0.0019  0.0022
3 2018-12-21 14:25:00  0.0022  0.0022  0.0020  0.0020
4 2018-12-21 14:30:00  0.0021  0.0021  0.0020  0.0020
5 2018-12-21 14:35:00  0.0021  0.0023  0.0021  0.0022
6 2018-12-21 14:40:00  0.0021  0.0022  0.0019  0.0020
7 2018-12-21 14:45:00  0.0020  0.0021  0.0018  0.0019
8 2018-12-21 14:50:00  0.0019  0.0020  0.0018  0.0019
9 2018-12-21 14:55:00  0.0018  0.0019  0.0017  0.0018
```

### 获取期权的tick行情(仅本地数据提供)

```python
get_ticks(security, start_dt, end_dt, count, fields , skip , df)
```

**期权部分**，支持期权tick数据，其中50ETF期权从2017-01-01开始，提供买卖五档；商品期权从2019-12-02开始，提供买卖一档。

**注意**：

- 仅[本地数据](https://www.joinquant.com/help/api/doc?name=JQDatadoc)提供

**参数**：

- security: 期权代码，如security='10001979.XSHG' #50ETF期权，上海证券交易所；security='CU2001C42000.XSGE'#铜期权，上海期货交易所； security='SR003C5600.XZCE' #白糖期权，郑州商品交易所； security='M2005-P-2400.XDCE' #豆粕期权，大连商品交易所；
    
- start_dt: 开始日期
    
- end_dt: 结束日期
    
- count: 取出指定时间区间内前多少条的tick数据;
    
- fields: 选择要获取的行情数据字段，默认为None;
    
- skip:默认为True，过滤掉无成交变化的tick数据；当指定skip=False时，返回的tick数据会保留无成交有盘口变化的tick数据
    
- df:默认为False，返回numpy.ndarray格式的tick数据；df=True的时候，返回pandas.Dataframe格式的数据。
    
- **期权tick返回结果：**
    

| 字段名 | 说明 | 字段类型 |
| --- | --- | --- |
| time | 时间 | datetime |
| current | 当前价 | float |
| high | 当日最高价 | float |
| low | 当日最低价 | float |
| volume | 累计成交量（张） | float |
| money | 累计成交额（元） | float |
| position | 持仓量（张） | float |
| a1_p | 一档卖价 | float |
| a1_v | 一档卖量 | float |
| … |  |  |
| a5_p | 五档卖价 | float |
| a5_v | 五档卖量 | float |
| b1_p | 一档买价 | float |
| b1_v | 一档买量 | float |
| … |  |  |
| b5_p | 五档买价 | float |
| b5_v | 五档买量 | float |

**期权tick数据示例**：

```python
# fields中的字段可以自己添加，下面只是示例
df = get_ticks('10001313.XSHG',start_dt='2018-12-20 09:00:00',end_dt='2018-12-20 10:00:00', fields=['time', 'current', 'volume', 'a1_p', 'b1_p'])
print(df)

[(20181220092500.0, 0.006, 30.0, 0.006, 0.0059)
 (20181220092500.0, 0.006, 0.0, 0.006, 0.0059)
 (20181220092520.0, 0.006, 0.0, 0.006, 0.0059) ...,
 (20181220095959.0, 0.0042, 0.0, 0.0043, 0.0042)
 (20181220100000.0, 0.0043, 2.0, 0.0043, 0.0042)
 (20181220100000.0, 0.0043, 0.0, 0.0043, 0.0042)]
```

### 获取ETF期权交易和持仓排名统计

```python
from jqdata import *
opt.run_query(query(opt.OPT_TRADE_RANK_STK).filter(opt.OPT_TRADE_RANK_STK.underlying_symbol==underlying_symbol).limit(n))
```

描述：统计沪深ETF期权，每日最活跃三个合约的交易排名和持仓量最大三个合约的持仓排名情况

**参数：**

- **query(opt.OPT_TRADE_RANK_STK)**：表示从opt.OPT_TRADE_RANK_STK这张表中查询股票期权交易和持仓排名统计数据，还可以指定所要查询的字段名，格式如下：query(库名.表名.字段名1，库名.表名.字段名2），多个字段用逗号分隔进行提取；query函数的更多用法详见：[sqlalchemy.orm.query.Query对象](http://docs.sqlalchemy.org/en/rel_1_0/orm/query.html)
- **opt.OPT_TRADE_RANK_STK**：收录了股票期权交易和持仓排名统计数据，表结构和字段信息如下：

**字段设计**

| **名称** | **类型** | **描述** | **示例** |
| --- | --- | --- | --- |
| underlying_symbol | str | 标的代码 | 510050.XSHG |
| underlying_name | str | 标的简称 | 华夏上证50ETF |
| underlying_exchange | str | 证券市场编码：XSHG-上海证券交易所； | XSHG |
| date | str | 交易日期 | 2018-10-25 |
| rank | int | 排名 | 1 |
| volume | int | 数量(张） | 184891 |
| option_agency | str | 期权经营机构 | 华泰证券 |
| rank_type | str | 排名统计类型，601001：最活跃三个合约的认购交易排名；601002：最活跃三个合约的认沽交易排名；601003：持仓最大3个合约的认购持仓量排名；601004：持仓最大3个合约的认沽持仓量排名 | 601001 |

- **filter(opt.OPT_TRADE_RANK_STK.underlying_symbol==underlying_symbol)**：指定筛选条件，通过opt.OPT_TRADE_RANK_STK.underlying_symbol==underlying_symbol可以指定你想要查询的标的代码；除此之外，还可以对表中其他字段指定筛选条件；多个筛选条件用英文逗号分隔。
- **limit(n)**：限制返回的数据条数，n指定返回条数。

**返回结果：**

- 返回一个 dataframe，每一行对应数据表中的一条数据， 列索引是您所查询的字段名称

**注意：**

1.  **为了防止返回数据量过大, 我们每次最多返回3000行**
2.  不能进行连表查询，即同时查询多张表的数据

**示例：**

```python
#查询最活跃三个合约的认购交易排名（601001）
from jqdata import *
q=query(opt.OPT_TRADE_RANK_STK).filter(opt.OPT_TRADE_RANK_STK.rank_type==601001).order_by(opt.OPT_TRADE_RANK_STK.date.desc()).limit(10)
df=opt.run_query(q)
print(df)

      id underlying_symbol underlying_name underlying_exchange        date  \
0  18641       510050.XSHG           50ETF                XSHG  2018-12-05
1  18642       510050.XSHG           50ETF                XSHG  2018-12-05
2  18643       510050.XSHG           50ETF                XSHG  2018-12-05
3  18644       510050.XSHG           50ETF                XSHG  2018-12-05
4  18645       510050.XSHG           50ETF                XSHG  2018-12-05
5  18621       510050.XSHG           50ETF                XSHG  2018-12-04
6  18622       510050.XSHG           50ETF                XSHG  2018-12-04
7  18623       510050.XSHG           50ETF                XSHG  2018-12-04
8  18624       510050.XSHG           50ETF                XSHG  2018-12-04
9  18625       510050.XSHG           50ETF                XSHG  2018-12-04

   rank  volume option_agency rank_type
0     2   78610          中信证券    601001
1     5   56171          海通证券    601001
2     3   66600          招商证券    601001
3     1   79627          中泰证券    601001
4     4   62392          华泰证券    601001
5     1   89718          中信证券    601001
6     4   69276          国泰君安    601001
7     5   61900          招商证券    601001
8     2   75760          中泰证券    601001
9     3   72447          华泰证券    601001
```

### 获取期权风险指标数据

```python
from jqdata import *
opt.run_query(query(opt.OPT_RISK_INDICATOR).filter(opt.OPT_RISK_INDICATOR.code==code).limit(n))
```

描述：统计各期权合约每日的风险指标，帮助用户更科学的衡量期权合约的价值变动

**参数：**

- **query(opt.OPT_RISK_INDICATOR)**：表示从opt.OPT_RISK_INDICATOR这张表中查询期权风险指标数据，还可以指定所要查询的字段名，格式如下：query(库名.表名.字段名1，库名.表名.字段名2），多个字段用逗号分隔进行提取；query函数的更多用法详见：[sqlalchemy.orm.query.Query对象](http://docs.sqlalchemy.org/en/rel_1_0/orm/query.html)
- **opt.OPT_RISK_INDICATOR**：收录了期权风险指标数据，表结构和字段信息如下：

**字段设计**

| **名称** | **类型** | **描述** | **示例** | **备注** |
| --- | --- | --- | --- | --- |
| code | str | 合约代码 | 10001313.XSHG；CU1901C46000.XSGE；SR903C4700.XZCE；M1707-C-2400.XDCE | 合约代码使用大写字母 |
| exchange_code | str | 证券市场编码 | XSHG |  |
| date | str | 交易日期 | 2018-10-19 |  |
| delta | float | DELTA | 0.906 | **Delta=期权价格变化/****期货****变化** |
| theta | float | THETA | -0.249 | **Theta＝期权价格的变化／距离到期日时间的变化** |
| gamma | float | GAMMA | 0.669 | **Gamma=delta的变化／期货价格的变化** |
| vega | float | VEGA | 0.138 | **Vega=期权价格变化/波动率的变化** |
| rho | float | RHO | 0.213 | **Rho=期权价格的变化／****无风险利率****的变化** |

- **filter(opt.OPT_RISK_INDICATOR.code==code)**：指定筛选条件，通过opt.OPT_RISK_INDICATOR.code==code可以指定你想要查询的合约代码；除此之外，还可以对表中其他字段指定筛选条件；多个筛选条件用英文逗号分隔。
- **limit(n)**：限制返回的数据条数，n指定返回条数。

**返回结果：**

- 返回一个 dataframe，每一行对应数据表中的一条数据， 列索引是您所查询的字段名称

**注意：**

1.  **为了防止返回数据量过大, 我们每次最多返回3000行**
2.  不能进行连表查询，即同时查询多张表的数据

**示例：**

```python
#查询('10001313.XSHG')最新的期权风险指标数据。
from jqdata import *
q=query(opt.OPT_RISK_INDICATOR).filter(opt.OPT_RISK_INDICATOR.code=='10001313.XSHG').order_by(opt.OPT_RISK_INDICATOR.date.desc()).limit(10)
df=opt.run_query(q)
print(df)

       id           code exchange_code        date  delta  theta  gamma  \
0  320797  10001313.XSHG          XSHG  2018-12-05  0.609 -0.488  2.875
1   83541  10001313.XSHG          XSHG  2018-12-04  0.638 -0.471  2.730
2   83540  10001313.XSHG          XSHG  2018-12-03  0.610 -0.490  2.607
3   83539  10001313.XSHG          XSHG  2018-11-30  0.467 -0.519  2.278
4   83538  10001313.XSHG          XSHG  2018-11-29  0.419 -0.484  2.266
5   83537  10001313.XSHG          XSHG  2018-11-28  0.447 -0.466  2.341
6   83536  10001313.XSHG          XSHG  2018-11-27  0.391 -0.449  2.198
7   83535  10001313.XSHG          XSHG  2018-11-26  0.422 -0.470  2.108
8   83534  10001313.XSHG          XSHG  2018-11-23  0.418 -0.468  1.917
9   83533  10001313.XSHG          XSHG  2018-11-22  0.497 -0.477  1.929

    vega    rho
0  0.228  0.083
1  0.229  0.091
2  0.239  0.090
3  0.263  0.078
4  0.261  0.072
5  0.270  0.080
6  0.264  0.072
7  0.275  0.080
8  0.287  0.087
9  0.302  0.108
```

### 获取期权行权交收信息

```python
from jqdata import *
opt.run_query(query(opt.OPT_EXERCISE_INFO).filter(opt.OPT_EXERCISE_INFO.underlying_symbol==underlying_symbol).limit(n))
```

描述：统计ETF期权在各个行权日的交收情况，一定程度上也代表了用户对当前市场的风险偏好

**参数：**

- **query(opt.OPT_EXERCISE_INFO)**：表示从opt.OPT_EXERCISE_INFO这张表中查询期权行权交收信息数据，还可以指定所要查询的字段名，格式如下：query(库名.表名.字段名1，库名.表名.字段名2），多个字段用逗号分隔进行提取；query函数的更多用法详见：[sqlalchemy.orm.query.Query对象](http://docs.sqlalchemy.org/en/rel_1_0/orm/query.html)
- **opt.OPT_EXERCISE_INFO**：收录了期权行权交收信息数据，表结构和字段信息如下：

**字段设计**

| **名称** | **类型** | **描述** | **示例** | **备注** |  |
| --- | --- | --- | --- | --- | --- |
| underlying_symbol | str | 标的代码 | 510050.XSHG |  |  |
| underlying_name | str | 标的名称 |  |  |  |
| exercise_date | str | 行权日 | 2018-10-24 |  |  |
| constract_type | str | 合约类型，CO-认购期权，PO-认沽期权 | CO |  |  |
| exercise_number | int | 行权数量 | 12520 |  |  |

- **filter(opt.OPT_EXERCISE_INFO.underlying_symbol==underlying_symbol)**：指定筛选条件，通过opt.OPT_EXERCISE_INFO.underlying_symbol==underlying_symbol可以指定你想要查询的标的代码；除此之外，还可以对表中其他字段指定筛选条件；多个筛选条件用英文逗号分隔。
- **limit(n)**：限制返回的数据条数，n指定返回条数。

**返回结果：**

- 返回一个 dataframe，每一行对应数据表中的一条数据， 列索引是您所查询的字段名称

**注意：**

1.  **为了防止返回数据量过大, 我们每次最多返回3000行**
2.  不能进行连表查询，即同时查询多张表的数据

**示例：**

```python
#查询华夏上证50ETF("510050.XSHG")最新的期权行权交收信息数据。
from jqdata import *
q=query(opt.OPT_EXERCISE_INFO).filter(opt.OPT_EXERCISE_INFO.underlying_symbol=='510050.XSHG').order_by(opt.OPT_EXERCISE_INFO.exercise_date.desc()).limit(10)
df=opt.run_query(q)
print(df)

      id underlying_symbol underlying_name exercise_date contract_type  exercise_number
0   86       510050.XSHG           50ETF    2018-11-28            PO            14419
1   85       510050.XSHG           50ETF    2018-11-28            CO            17330
2   84       510050.XSHG           50ETF    2018-10-24            PO            21933
3   83       510050.XSHG           50ETF    2018-10-24            CO            12520
4   82       510050.XSHG           50ETF    2018-09-26            PO             9550
5   81       510050.XSHG           50ETF    2018-09-26            CO            20286
6   80       510050.XSHG           50ETF    2018-08-22            PO            10228
7   79       510050.XSHG           50ETF    2018-08-22            CO            10208
8   78       510050.XSHG           50ETF    2018-07-25            PO             5754
9   77       510050.XSHG           50ETF    2018-07-25            CO            19632
```

## 期权列表

文档更新可能存在滞后，请直接查询[期权合约资料表](https://www.joinquant.com/help/api/help#Option:%E8%8E%B7%E5%8F%96%E6%9C%9F%E6%9D%83%E5%90%88%E7%BA%A6%E8%B5%84%E6%96%99)获取

| 上市日期 | 品种名称 | 交易所 | 示例合约代码 | 示例合约名称 | 示例合约标的物 | 示例合约标的物名称 | 合约规格 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 2015-02-09 | 50ETF期权 | XSHG | 10000001.XSHG | 50ETF购3月2200 | 510050.XSHG | 50ETF | [50ETF期权合约规格](http://www.sse.com.cn/assortment/options/contract/c/c_20230303_5717359.shtml) |
| 2017-03-31 | 豆粕期权 | XDCE | M1712-P-2650.XDCE | 豆粕沽12月2650 | M1712.XDCE | 连豆粕1712合约 | [豆粕期权合约规格](http://m.dce.com.cn/dalianshangpinmobile/pzzx90/dpqq95/hyygz49/6216504/index.html) |
| 2017-04-19 | 白糖期权 | XZCE | SR807P6900.XZCE | 白糖沽7月6900 | SR1807.XZCE | 郑白糖807合约 | [白糖期权合约规格](http://www.czce.com.cn/cn/sspz/bt/H770204index_1.htm) |
| 2018-09-21 | 铜期权 | XSGE | CU1906P48000.XSGE | 铜沽6月48000 | CU1906.XSGE | 沪铜1906合约 | [铜期权合约规格](https://www.shfe.com.cn/products/cuQ/standard/) |
| 2019-01-28 | 棉花期权 | XZCE | CF905P16400.XZCE | 棉花沽5月16400 | CF1905.XZCE | 郑棉花905合约 | [棉花期权合约规格](http://www.czce.com.cn/cn/sspz/mh/H770203index_1.htm) |
| 2019-01-28 | 天胶期权 | XSGE | RU1907C10750.XSGE | 天胶购7月10750 | RU1907.XSGE | 沪天胶1907合约 | [天胶期权合约规格](https://www.shfe.com.cn/products/ruQ/standard/) |
| 2019-01-28 | 玉米期权 | XDCE | C2001-P-2040.XDCE | 玉米沽1月2040 | C2001.XDCE | 连玉米2001合约 | [玉米期权合约规格](http://www.dce.com.cn/dalianshangpin/sspz/ymqq/hyygz63/6216478/index.html) |
| 2019-12-09 | 铁矿石期权 | XDCE | I2009-C-520.XDCE | 铁矿石购9月520 | I2009.XDCE | 连铁矿石2009合约 | [铁矿石期权合约规格](http://www.dce.com.cn/dalianshangpin/sspz/tksqq21/hyygz11/6216456/index.html) |
| 2019-12-16 | 甲醇期权 | XZCE | MA003P2100.XZCE | 甲醇沽3月2100 | MA2003.XZCE | 郑甲醇003合约 | [甲醇期权合约规格](http://www.czce.com.cn/cn/sspz/jc/H770208index_1.htm) |
| 2019-12-16 | PTA期权 | XZCE | TA004C4900.XZCE | PTA购4月4900 | TA2004.XZCE | 郑精对苯二甲酸004合约 | [PTA期权合约规格](http://www.czce.com.cn/cn/sspz/pta/H770205index_1.htm) |
| 2019-12-20 | 黄金期权 | XSGE | AU2010C348.XSGE | 黄金购10月348 | AU2010.XSGE | 沪黄金2010合约 | [黄金期权合约规格](https://www.shfe.com.cn/products/auQ/standard/) |
| 2019-12-23 | 沪深300期权 | CCFX | IO2012-P-4500.CCFX | 沪深300沽12月4500 | 000300.XSHG | 沪深300指数 | [沪深300期权合约规格](http://www.cffex.com.cn/hs300gzqq/) |
| 2019-12-23 | 300ETF期权 | XSHE | 90000034.XSHE | 300ETF沽2月4300 | 159919.XSHE | 嘉实沪深300ETF | [300ETF期权合约规格](http://www.szse.cn/lawrules/rule/derivative/t20191219_572722.html) |
| 2019-12-23 | 300ETF期权 | XSHG | 10002160.XSHG | 300ETF购3月4300 | 510300.XSHG | 华泰柏瑞沪深300ETF | [300ETF期权合约规格](http://www.sse.com.cn/assortment/options/contract/c/c_20230303_5717360.shtml) |
| 2020-01-16 | 菜籽粕期权 | XZCE | RM009C2175.XZCE | 菜籽粕购9月2175 | RM2009.XZCE | 郑菜籽粕009合约 | [菜籽粕期权合约规格](http://www.czce.com.cn/cn/sspz/czy/H770206index_1.htm) |
| 2020-03-31 | 液化石油气期权 | XDCE | PG2103-P-2700.XDCE | 液化石油气沽3月2700 | PG2103.XDCE | 连液化石油气2103合约 | [液化石油气期权合约规格](http://www.dce.com.cn/dalianshangpin/sspz/yhsyqqq/hyygz73/6210761/index.html) |
| 2020-06-30 | 动力煤期权 | XZCE | ZC010P500.XZCE | 动力煤沽10月500 | ZC2010.XZCE | 郑动力煤010合约 | [动力煤期权合约规格](http://www.czce.com.cn/cn/sspz/dlm/H770212index_1.htm) |
| 2020-07-06 | 乙烯期权 | XDCE | L2101-P-6700.XDCE | 乙烯沽1月6700 | L2101.XDCE | 连乙烯2101合约 | [乙烯期权合约规格](http://www.dce.com.cn/dalianshangpin/sspz/6226615/hyygz184/6227275/index.html) |
| 2020-07-06 | 聚氯乙烯期权 | XDCE | V2104-C-5900.XDCE | 聚氯乙烯购4月5900 | V2104.XDCE | 连聚氯乙烯2104合约 | [聚氯乙烯期权合约规格](http://www.dce.com.cn/dalianshangpin/sspz/6226619/hyygz9/6227280/index.html) |
| 2020-07-06 | 聚丙烯期权 | XDCE | PP2105-P-6800.XDCE | 聚丙烯沽5月6800 | PP2105.XDCE | 连聚丙烯2105合约 | [聚丙烯期权合约规格](http://www.dce.com.cn/dalianshangpin/sspz/6226623/hyygz75/6227284/index.html) |
| 2020-08-10 | 锌期权 | XSGE | ZN2010C19600.XSGE | 锌购10月19600 | ZN2010.XSGE | 沪锌2010合约 | [锌期权合约规格](https://www.shfe.com.cn/products/znQ/standard/) |
| 2020-08-10 | 铝期权 | XSGE | AL2101P15600.XSGE | 铝沽1月15600 | AL2101.XSGE | 沪铝2101合约 | [铝期权合约规格](https://www.shfe.com.cn/products/alQ/standard/) |
| 2021-06-18 | 棕油期权 | XDCE | P2203-P-6800.XDCE | 棕油沽3月6800 | P2203.XDCE | 连棕油2203合约 | [棕油期权合约规格](http://www.dce.com.cn/dalianshangpin/sspz/6282422/6282423/6282591/index.html) |
| 2021-06-21 | 原油期权 | XINE | SC2110P510.XINE | 原油沽10月510 | SC2110.XINE | 沪原油2110合约 | [原油期权合约规格](https://www.ine.cn/products/scQ/) |
| 2022-07-22 | 中证1000期权 | CCFX | MO2212-C-7600.CCFX | 中证1000购12月7600 | 000852.XSHG | 中证1000指数 | [中证1000期权合约规格](http://www.cffex.com.cn/zz1000gzqq/) |
| 2022-08-08 | 黄大豆2号期权 | XDCE | B2307-P-4100.XDCE | 黄大豆2号沽7月4100 | B2307.XDCE | 连黄大豆2号2307合约 | [黄大豆2号期权合约规格](http://www.dce.com.cn/dalianshangpin/sspz/hdd2hqq/hyygz64/8509657/index.html) |
| 2022-08-08 | 黄大豆1号期权 | XDCE | A2305-P-6400.XDCE | 黄大豆1号沽5月6400 | A2305.XDCE | 连黄大豆1号2305合约 | [黄大豆1号期权合约规格](http://www.dce.com.cn/dalianshangpin/sspz/hdd1hqq/hyygz4/8509653/index.html) |
| 2022-08-08 | 豆油期权 | XDCE | Y2211-C-8600.XDCE | 豆油购11月8600 | Y2211.XDCE | 连豆油2211合约 | [豆油期权合约规格](http://www.dce.com.cn/dalianshangpin/sspz/dyqq/hyygz2/8509701/index.html) |
| 2022-08-26 | 花生期权 | XZCE | PK212P11200.XZCE | 花生沽12月11200 | PK2212.XZCE | 郑花生212合约 | [花生期权合约规格](http://www.czce.com.cn/cn/sspz/hsqh/H770226index_1.htm) |
| 2022-08-26 | 菜籽油期权 | XZCE | OI305P9900.XZCE | 菜籽油沽5月9900 | OI2305.XZCE | 郑菜籽油305合约 | [菜籽油期权合约规格](http://www.czce.com.cn/cn/sspz/czy/H770206index_1.htm) |
| 2022-09-19 | 500ETF期权 | XSHG | 10004510.XSHG | 500ETF沽10月6000 | 510500.XSHG | 南方中证500ETF | [500ETF期权合约规格](http://www.sse.com.cn/assortment/options/contract/c/c_20230303_5717361.shtml) |
| 2022-09-19 | 中证500ETF期权 | XSHE | 90001345.XSHE | 中证500ETF购3月5000 | 159922.XSHE | 嘉实中证500ETF | [中证500ETF期权合约规格](http://www.szse.cn/disclosure/notice/general/t20220916_595888.html) |
| 2022-09-19 | 创业板ETF期权 | XSHE | 90001228.XSHE | 创业板ETF沽10月2100 | 159915.XSHE | 易方达创业板ETF | [创业板ETF期权合约规格](http://www.szse.cn/disclosure/notice/general/t20220916_595887.html) |
| 2022-12-12 | 深证100ETF期权 | XSHE | 90001612.XSHE | 深证100ETF沽1月3000 | 159901.XSHE | 易方达深证100ETF | [深证100ETF期权合约规格](http://www.szse.cn/disclosure/notice/general/t20221209_597760.html) |
| 2022-12-19 | 上证50期权 | CCFX | HO2303-P-2500.CCFX | 上证50沽3月2500 | 000016.XSHG | 上证50指数 | [上证50期权合约规格](http://www.cffex.com.cn/sz50gzqq/) |
| 2022-12-23 | 工业硅期权 | GFEX | SI2311-C-19600.GFEX | 工业硅购11月19600 | SI2311.GFEX | 粤工业硅2311合约 | [工业硅期权合约规格](http://www.gfex.com.cn/gfex/gyeg/sspz.shtml) |
| 2022-12-26 | 螺钢期权 | XSGE | RB2310C3750.XSGE | 螺钢购10月3750 | RB2310.XSGE | 沪螺钢2310合约 | [螺钢期权合约规格](https://www.shfe.com.cn/products/rbQ/standard/) |
| 2022-12-26 | 白银期权 | XSGE | AG2306P5600.XSGE | 白银沽6月5600 | AG2306.XSGE | 沪白银2306合约 | [白银期权合约规格](https://www.shfe.com.cn/products/agQ/standard/) |
| 2023-05-15 | 乙二醇期权 | XDCE | EG2310-P-4500.XDCE | 乙二醇沽10月4500 | EG2310.XDCE | 连乙二醇2310合约 | [乙二醇期权合约规格](http://www.dce.com.cn/dalianshangpin/sspz/yecqq/hyygz99/8543272/index.html) |
| 2023-05-15 | 苯乙烯期权 | XDCE | EB2309-C-8400.XDCE | 苯乙烯购9月8400 | EB2309.XDCE | 连苯乙烯2309合约 | [苯乙烯期权合约规格](http://www.dce.com.cn/dalianshangpin/sspz/byxqq/hyygz7/8543277/index.html) |
| 2023-06-05 | 科创板50期权 | XSHG | 10005558.XSHG | 科创板50沽6月900 | 588080.XSHG | 科创板50 | [科创板50期权合约规格](http://www.sse.com.cn/assortment/options/contract/c/c_20230602_5722082.shtml) |
| 2023-06-05 | 科创50期权 | XSHG | 10005533.XSHG | 科创50购12月1000 | 588000.XSHG | 科创50 | [科创50期权合约规格](http://www.sse.com.cn/assortment/options/contract/c/c_20230602_5722081.shtml) |
| 2023-07-24 | 碳酸锂期权 | GFEX | LC2406-P-180000.GFEX | 碳酸锂沽06月180000 | LC2406.GFEX | 粤碳酸锂2406合约 | [碳酸锂期权合约规格](http://www.gfex.com.cn/gfex/tsl/sspz.shtml) |
| 2023-07-31 | 丁二烯橡胶期权 | XSGE | BR2402C11800.XSGE | 丁二烯橡胶购2月11800 | BR2402.XSGE | 沪丁二烯橡胶2402合约 | [丁二烯橡胶期权合约规格](https://www.shfe.com.cn/products/br/standard/text/) |
| 2023-09-18 | 对二甲苯期权 | XZCE | PX406C9100.XZCE | 对二甲苯购6月9100 | PX2406.XZCE | 郑对二甲苯406合约 | [对二甲苯期权合约规格](http://www.czce.com.cn/cn/sspz/dejbqhqq/H770227index_1.htm) |
| 2023-09-18 | 烧碱期权 | XZCE | SH405C3240.XZCE | 烧碱购5月3240 | SH2405.XZCE | 郑烧碱405合约 | [烧碱期权合约规格](http://www.czce.com.cn/cn/sspz/sjqhqq/H770228index_1.htm) |
| 2023-10-20 | 涤纶短纤期权 | XZCE | PF401P6600.XZCE | 涤纶短纤沽1月6600 | PF2401.XZCE | 郑涤纶短纤401合约 | [涤纶短纤期权合约规格](http://www.czce.com.cn/cn/sspz/dxqh/H770225index_1.htm) |
| 2023-10-20 | 纯碱期权 | XZCE | SA404P1660.XZCE | 纯碱沽4月1660 | SA2404.XZCE | 郑纯碱404合约 | [纯碱期权合约规格](http://www.czce.com.cn/cn/sspz/cjqh/H770224index_1.htm) |
| 2023-10-20 | 硅铁期权 | XZCE | SF402P6400.XZCE | 硅铁沽2月6400 | SF2402.XZCE | 郑硅铁402合约 | [硅铁期权合约规格](http://www.czce.com.cn/cn/sspz/gt/H770217index_1.htm) |
| 2023-10-20 | 锰硅期权 | XZCE | SM403P7600.XZCE | 锰硅沽3月7600 | SM2403.XZCE | 郑锰硅403合约 | [锰硅期权合约规格](http://www.czce.com.cn/cn/sspz/meng/H770220index_1.htm) |
| 2023-10-20 | 鲜苹果期权 | XZCE | AP405C9000.XZCE | 鲜苹果购5月9000 | AP2405.XZCE | 郑鲜苹果405合约 | [鲜苹果期权合约规格](http://www.czce.com.cn/cn/sspz/pg/H770221index_1.htm) |
| 2023-10-20 | 尿素期权 | XZCE | UR401C2080.XZCE | 尿素购1月2080 | UR2401.XZCE | 郑尿素401合约 | [尿素期权合约规格](http://www.czce.com.cn/cn/sspz/nsqh/H770223index_1.htm) |
| 2024-06-21 | 干制红枣期权 | XZCE | CJ501P11400.XZCE | 干制红枣沽1月11400 | CJ2501.XZCE | 郑干制红枣501合约 | [干制红枣期权合约规格](http://www.czce.com.cn/cn/sspz/hzqh/H770222index_1.htm#tabs-4) |
| 2024-06-21 | 平板玻璃期权 | XZCE | FG409P1360.XZCE | 平板玻璃沽9月1360 | FG2409.XZCE | 郑平板玻璃409合约 | [平板玻璃期权合约规格](http://www.czce.com.cn/cn/sspz/bl/H770209index_1.htm#tabs-4) |
| 2024-08-23 | 玉米淀粉期权 | XDCE | CS2507-P-2900.XDCE | 玉米淀粉沽7月2900 | CS2507.XDCE | 连玉米淀粉2507合约 | [玉米淀粉期权合约规格](http://www.dce.com.cn/dalianshangpin/sspz/8606077/8606078/8608200/index.html) |
| 2024-08-23 | 生猪期权 | XDCE | LH2505-P-14400.XDCE | 生猪沽5月14400 | LH2505.XDCE | 连生猪2505合约 | [生猪期权合约规格](http://www.dce.com.cn/dalianshangpin/sspz/8606123/8606124/8608208/index.html) |
| 2024-08-23 | 鸡蛋期权 | XDCE | JD2501-P-3250.XDCE | 鸡蛋沽1月3250 | JD2501.XDCE | 连鸡蛋2501合约 | [鸡蛋期权合约规格](http://www.dce.com.cn/dalianshangpin/sspz/8606105/8606106/8607940/index.html) |
| 2024-09-02 | 铅期权 | XSGE | PB2412C15400.XSGE | 铅购12月15400 | PB2412.XSGE | 沪铅2412合约 | [铅期权合约规格](https://www.shfe.com.cn/products/option/nonferrousmetal/pb_o/) |
| 2024-09-02 | 镍期权 | XSGE | NI2501P116000.XSGE | 镍沽1月116000 | NI2501.XSGE | 沪镍2501合约 | [镍期权合约规格](https://www.shfe.com.cn/products/option/nonferrousmetal/ni_o/) |
| 2024-09-02 | 锡期权 | XSGE | SN2412P245000.XSGE | 锡沽12月245000 | SN2412.XSGE | 沪锡2412合约 | [锡期权合约规格](https://www.shfe.com.cn/products/option/nonferrousmetal/sn_o/) |
| 2024-09-02 | 氧化铝期权 | XSGE | AO2501P3450.XSGE | 氧化铝沽1月3450 | AO2501.XSGE | 沪氧化铝2501合约 | [氧化铝期权合约规格](https://www.shfe.com.cn/products/option/nonferrousmetal/ao_o/) |
| 2024-11-19 | 原木期权 | XDCE | LG2511-C-750.XDCE | 原木购11月750 | LG2511.XDCE | 连原木2511合约 | [原木期权合约规格](http://www.dce.com.cn/dalianshangpin/sspz/8621129/8621130/8622207/index.html) |
| 2024-12-27 | 多晶硅期权 | GFEX | PS2512-P-47000.GFEX | 多晶硅沽12月47000 | PS2512.GFEX | 粤多晶硅2512合约 | [多晶硅期权合约规格](http://www.gfex.com.cn/gfex/djg/sspz.shtml) |
| 2024-12-27 | 瓶级聚酯切片期权 | XZCE | PR503C5800.XZCE | 瓶级聚酯切片购3月5800 | PR2503.XZCE | 郑瓶级聚酯切片503合约 | [瓶级聚酯切片期权合约规格](http://www.czce.com.cn/cn/sspz/ppqh/H770229index_1.htm#tabs-4) |