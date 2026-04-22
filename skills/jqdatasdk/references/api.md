# jqdatasdk API 参考文档

本文档提供 jqdatasdk 所有 API 的详细说明和参数定义。

## 目录

1. [认证与配置](#认证与配置)
2. [行情数据](#行情数据)
3. [财务数据](#财务数据)
4. [标的信息](#标的信息)
5. [行业与概念](#行业与概念)
6. [资金流向](#资金流向)
7. [融资融券](#融资融券)
8. [期货数据](#期货数据)
9. [因子数据](#因子数据)
10. [Alpha因子](#alpha因子)
11. [其他接口](#其他接口)
12. [错误处理](#错误处理)

---

## 认证与配置

### jq.auth()

账号密码认证。

```python
jq.auth(username, password, host=None, port=None)
```

**参数:**
- `username` (str): 聚宽账号用户名
- `password` (str): 聚宽账号密码
- `host` (str, optional): 服务器地址，默认 None
- `port` (int, optional): 服务器端口，默认 None

**示例:**
```python
jq.auth('your_username', 'your_password')
```

### jq.auth_by_token()

使用 Token 认证。

```python
jq.auth_by_token(token, host=None, port=None)
```

**参数:**
- `token` (str): 聚宽 Token
- `host` (str, optional): 服务器地址
- `port` (int, optional): 服务器端口

**示例:**
```python
jq.auth_by_token('your_token')
```

### jq.logout()

退出登录。

```python
jq.logout()
```

### jq.is_auth()

检查认证状态。

```python
jq.is_auth() -> bool
```

**返回:** bool - 是否已认证

### jq.set_params()

设置请求参数。

```python
jq.set_params(**params)
```

**参数:**
- `request_timeout` (int): 请求超时时间(秒)，默认300
- `request_attempt_count` (int): 请求重试次数，默认3
- `request_username` (str): 请求用户名
- `request_password` (str): 请求密码
- `request_host` (str): 请求服务器地址
- `request_port` (int): 请求服务器端口
- `enable_auth_prompt` (bool): 是否输出登录提示，默认True

---

## 行情数据

### get_price()

获取一支或多支证券的行情数据（K线）。

```python
get_price(security, start_date=None, end_date=None, frequency='daily', 
          fields=None, skip_paused=False, fq='pre', count=None, 
          panel=True, fill_paused=True, round=True)
```

**参数:**
- `security` (str/list): 证券代码或代码列表，格式为 `XXXXXX.XSHG`（上海）或 `XXXXXX.XSHE`（深圳）
- `start_date` (str/datetime, optional): 开始日期，格式 `YYYY-MM-DD`
- `end_date` (str/datetime, optional): 结束日期，默认 '2015-12-31'
- `frequency` (str): 时间频率
  - 分钟线：`1min`, `5min`, `15min`, `30min`, `60min`, `120min`
  - 日线：`daily`（默认）
  - 周线：`weekly`
  - 月线：`monthly`
- `fields` (list, optional): 返回字段列表
  - `open`: 开盘价
  - `close`: 收盘价
  - `high`: 最高价
  - `low`: 最低价
  - `volume`: 成交量
  - `money`: 成交额
- `skip_paused` (bool): 是否跳过停牌日期，默认 False
- `fq` (str): 复权类型，`'pre'`前复权, `'post'`后复权, None不复权
- `count` (int, optional): 返回数据条数，与 start_date 二选一
- `panel` (bool): 是否返回 panel 对象，默认 True
- `fill_paused` (bool): 停牌时是否用收盘价填充，默认 True
- `round` (bool): 是否四舍五入，默认 True

**返回:** DataFrame 或 Panel

**示例:**
```python
# 获取单只股票日线数据
df = jq.get_price('000001.XSHE', start_date='2024-01-01', end_date='2024-12-31')

# 获取多只股票分钟数据
df = jq.get_price(['000001.XSHE', '600519.XSHG'], 
                   start_date='2024-01-01', frequency='5m')

# 指定字段
df = jq.get_price('000001.XSHE',
                  start_date='2024-01-01',
                  end_date='2024-01-31',
                  frequency='daily',
                  fields=['open', 'close', 'high', 'low', 'volume'])
```

### get_bars()

获取历史K线数据。

```python
get_bars(security, count=None, unit="1d", 
         fields=("date", "open", "high", "low", "close"),
         include_now=False, end_dt=None, fq_ref_date=None, df=True,
         start_dt=None, skip_paused=True)
```

**参数:**
- `security` (str/list): 证券代码
- `count` (int): 返回数据条数
- `unit` (str): 时间单位，支持 `'1m'`, `'5m'`, `'15m'`, `'30m'`, `'60m'`, `'120m'`, `'1d'`, `'1w'`, `'1M'`
- `fields` (tuple/list): 返回字段
- `include_now` (bool): 是否包含当前bar
- `end_dt` (str/datetime, optional): 截止时间
- `fq_ref_date` (str/datetime, optional): 复权基准日期
- `df` (bool): 是否返回 DataFrame
- `start_dt` (str/datetime, optional): 开始时间
- `skip_paused` (bool): 是否跳过停牌

### get_ticks()

获取 Tick 逐笔数据。

```python
get_ticks(security, start_dt=None, end_dt=None, count=None, 
          fields=None, skip=True, df=True)
```

**参数:**
- `security` (str): 股票或期货代码
- `start_dt` (str/datetime, optional): 开始时间，格式 `YYYY-MM-DD HH:MM:SS`
- `end_dt` (str/datetime, optional): 截止时间
- `count` (int, optional): 数据条数
- `fields` (list, optional): 字段列表
- `skip` (bool): 是否过滤无成交tick
- `df` (bool): 是否返回 DataFrame

**返回:** DataFrame，包含：
- `time`: 时间
- `price`: 价格
- `volume`: 成交量
- `amount`: 成交额
- `direction`: 买卖方向

**示例:**
```python
ticks = jq.get_ticks(security='000001.XSHE',
                     start_dt='2024-01-01 09:30:00',
                     end_dt='2024-01-01 15:00:00')
```

### get_current_tick()

获取最新Tick数据。

```python
get_current_tick(security) -> DataFrame
```

**参数:**
- `security` (str/list): 证券代码

### get_current_data()

获取实时数据快照。

**参数:** 无

**返回:** dict，键为证券代码，值为包含实时数据的对象
- `last_price`: 最新价
- `time`: 时间
- `day_open`: 日开盘价
- `day_high`: 日最高价
- `day_low`: 日最低价
- `volume`: 成交量
- `money`: 成交额

**示例:**
```python
data = jq.get_current_data()
if '000001.XSHE' in data:
    print(data['000001.XSHE'].last_price)
```

### get_order_book()

获取委托数据（买卖五档）。

```python
get_order_book(security, start_dt, end_dt)
```

**参数:**
- `security` (str): 证券代码
- `start_dt` (str): 开始日期时间
- `end_dt` (str): 结束日期时间

**返回:** list，包含买卖五档委托数据

**示例:**
```python
orders = jq.get_order_book(security='000001.XSHE',
                           start_dt='2024-01-01 09:30:00',
                           end_dt='2024-01-01 09:35:00')
```

### get_extras()

获取额外数据。

```python
get_extras(info, security_list, start_date=None, end_date=None, df=True, count=None)
```

**参数:**
- `info` (str): 数据类型
  - `'is_st'`: 是否ST
  - `'acc_net_value'`: 累计净值
  - `'unit_net_value'`: 单位净值
  - `'futures_sett_price'`: 期货结算价
  - `'futures_positions'`: 期货持仓
- `security_list` (list): 证券列表
- `start_date` (str/datetime, optional): 开始日期
- `end_date` (str/datetime, optional): 结束日期
- `df` (bool): 是否返回 DataFrame
- `count` (int, optional): 数据条数

---

## 财务数据

### get_fundamentals()

查询财务数据。

```python
get_fundamentals(query_object, date=None, statDate=None) -> DataFrame
```

**参数:**
- `query_object` (Query): SQLAlchemy Query 对象
- `date` (str/datetime, optional): 查询日期
- `statDate` (str, optional): 财报统计季度，如 `'2024q1'`

**返回:** DataFrame

**示例:**
```python
from jqdatasdk import finance

q = jq.query(
    finance.indicator.code,
    finance.indicator.pub_date,
    finance.indicator.eps,
    finance.indicator.net_profits,
    finance.indicator.roe
).filter(
    finance.indicator.code == '000001.XSHE'
)

df = jq.get_fundamentals(q, date='2024-12-31')
```

### get_fundamentals_continuously()

连续查询财务数据。

```python
get_fundamentals_continuously(query_object, end_date=None, count=1, panel=True)
```

**参数:**
- `query_object` (Query): SQLAlchemy Query 对象
- `end_date` (str/datetime, optional): 截止日期
- `count` (int): 查询的日期数量
- `panel` (bool): 是否返回 Panel

### finance.run_query()

通过 ORM 执行财务数据查询。

**财务数据表：**

1. **资产负债表 (finance.STK_BALANCE_SHEET)**
   - `code`: 股票代码
   - `statDate`: 报告期
   - `total_assets`: 总资产
   - `total_liability`: 总负债
   - `total_owner_equities`: 股东权益

2. **利润表 (finance.STK_INCOME_STATEMENT)**
   - `code`: 股票代码
   - `statDate`: 报告期
   - `total_operating_revenue`: 营业总收入
   - `operating_cost`: 营业成本
   - `net_profit`: 净利润

3. **现金流量表 (finance.STK_CASH_FLOW_STATEMENT)**
   - `code`: 股票代码
   - `statDate`: 报告期
   - `net_operate_cash_flow`: 经营活动现金流
   - `net_invest_cash_flow`: 投资活动现金流

4. **指标数据 (finance.indicator)**
   - `code`: 股票代码
   - `statDate`: 报告期
   - `roe`: 净资产收益率
   - `inc_return`: 投资回报率
   - `inc_revenue_year_on_year`: 营业收入同比增长率
   - `net_profit_growth_rate`: 净利润增长率
   - `roe_yearly`: 年化净资产收益率

5. **估值数据 (finance.valuation)**
   - `code`: 股票代码
   - `day`: 日期
   - `market_cap`: 总市值
   - `circulating_market_cap`: 流通市值
   - `pe_ratio`: 市盈率
   - `pb_ratio`: 市净率
   - `ps_ratio`: 市销率
   - `pcf_ratio`: 市现率
   - `turnover_ratio`: 换手率

**查询示例:**
```python
from jqdatasdk import finance, query

# 查询资产负债表
q = query(finance.STK_BALANCE_SHEET.code,
          finance.STK_BALANCE_SHEET.statDate,
          finance.STK_BALANCE_SHEET.total_assets)
q = q.filter(finance.STK_BALANCE_SHEET.code == '000001.XSHE')
q = q.filter(finance.STK_BALANCE_SHEET.statDate == '2023')
df = finance.run_query(q)

# 查询指标数据
q = query(finance.indicator.code,
          finance.indicator.statDate,
          finance.indicator.roe,
          finance.indicator.pe_ratio)
q = q.filter(finance.indicator.code.in_(['000001.XSHE', '600000.XSHG']))
df = finance.run_query(q)

# 查询估值数据
q = query(finance.valuation.code,
          finance.valuation.day,
          finance.valuation.market_cap,
          finance.valuation.pe_ratio,
          finance.valuation.pb_ratio)
q = q.filter(finance.valuation.code == '000001.XSHE')
q = q.filter(finance.valuation.day >= '2024-01-01')
df = finance.run_query(q)
```

### get_valuation()

获取市值数据。

```python
get_valuation(security_list, start_date=None, end_date=None, fields=None, count=None)
```

**参数:**
- `security_list` (str/list): 证券代码列表
- `start_date` (str/datetime, optional): 开始日期
- `end_date` (str/datetime, optional): 结束日期
- `fields` (list, optional): 返回字段
- `count` (int, optional): 数据条数

**可用字段:**
- `code` - 股票代码
- `day` - 日期
- `pe_ratio` - 市盈率(PE, TTM)
- `turnover_ratio` - 换手率(%)
- `pb_ratio` - 市净率(PB)
- `ps_ratio` - 市销率(PS, TTM)
- `pcf_ratio` - 市现率(PCF)
- `capitalization` - 总股本(万股)
- `market_cap` - 总市值(亿元)
- `circulating_cap` - 流通股本(万股)
- `circulating_market_cap` - 流通市值(亿元)

### get_history_fundamentals()

获取历史财报数据。

```python
get_history_fundamentals(security, fields, watch_date=None, stat_date=None,
                         count=1, interval='1q', stat_by_year=False)
```

**参数:**
- `security` (str/list): 股票代码
- `fields` (list): 要查询的字段列表
- `watch_date` (str/datetime, optional): 观察日期
- `stat_date` (str, optional): 统计日期，如 `'2024q1'`
- `count` (int): 查询的历史报告期数量
- `interval` (str): 间隔，`'1q'` 或 `'1y'`
- `stat_by_year` (bool): 是否返回年度数据

---

## 标的信息

### get_all_securities()

获取所有证券信息。

```python
get_all_securities(types=[], date=None) -> DataFrame
```

**参数:**
- `types` (list, optional): 证券类型过滤
  - `'stock'`: 股票
  - `'fund'`: 基金
  - `'index'`: 指数
  - `'futures'`: 期货
  - `'etf'`: ETF
  - `'lof'`: LOF
  - `'bond'`: 债券
- `date` (str/datetime, optional): 查询日期

**示例:**
```python
# 获取所有股票
stocks = jq.get_all_securities(['stock'])

# 获取所有基金
funds = jq.get_all_securities(['fund'])

# 获取所有指数
indices = jq.get_all_securities(['index'])
```

### get_security_info()

获取证券详细信息。

```python
get_security_info(code, date=None) -> Security
```

**参数:**
- `code` (str): 证券代码
- `date` (str/datetime, optional): 查询日期

**返回:** object，包含：
- `code`: 证券代码
- `display_name`: 显示名称
- `name`: 简称
- `start_date`: 上市日期
- `end_date`: 退市日期（如有）
- `type`: 类型
- `parent`: 母证券（适用于基金等）

**示例:**
```python
info = jq.get_security_info('000001.XSHE')
print(info.display_name)
print(info.start_date)
```

### get_index_stocks()

获取指数成分股。

```python
get_index_stocks(index_symbol, date=today()) -> list
```

**参数:**
- `index_symbol` (str): 指数代码
  - `'000300.XSHG'`: 沪深300
  - `'000905.XSHG'`: 中证500
  - `'000852.XSHG'`: 中证1000
- `date` (str/datetime, optional): 查询日期

**示例:**
```python
hs300_stocks = jq.get_index_stocks('000300.XSHG')
zz500_stocks = jq.get_index_stocks('000905.XSHG')
zz1000_stocks = jq.get_index_stocks('000852.XSHG')
```

---

## 行业与概念

### get_industries()

获取行业列表。

```python
get_industries(name='zjw', date=None) -> DataFrame
```

**参数:**
- `name` (str): 行业分类代码
  - `'zjw'`: 聚宽一级行业
  - `'sw_l1'`: 申万一级行业
  - `'sw_l2'`: 申万二级行业
- `date` (str/datetime, optional): 查询日期

### get_industry_stocks()

获取行业股票列表。

```python
get_industry_stocks(industry_code, date=today()) -> list
```

**参数:**
- `industry_code` (str): 行业代码
- `date` (str/datetime, optional): 查询日期

### get_concepts()

获取概念板块列表。

```python
get_concepts() -> DataFrame
```

### get_concept_stocks()

获取概念板块股票列表。

```python
get_concept_stocks(concept_code, date=today()) -> list
```

**参数:**
- `concept_code` (str): 概念板块代码
- `date` (str/datetime, optional): 查询日期

### get_concept()

获取股票所属概念。

```python
get_concept(security, date) -> dict
```

### get_industry()

获取股票所属行业。

```python
get_industry(security, date=None, df=False)
```

---

## 资金流向

### get_money_flow()

获取资金流向数据。

```python
get_money_flow(security_list, start_date=None, end_date=None, 
               fields=None, count=None) -> DataFrame
```

**参数:**
- `security_list` (str/list): 证券代码
- `start_date` (str/datetime, optional): 开始日期
- `end_date` (str/datetime, optional): 结束日期
- `fields` (list, optional): 返回字段
- `count` (int, optional): 数据条数

**可用字段:**
- `date` - 日期
- `sec_code` - 股票代码
- `net_amount_main` - 主力净流入
- `net_pct_main` - 主力净流入占比
- `net_amount_xl` - 超大单净流入
- `net_amount_l` - 大单净流入
- `net_amount_m` - 中单净流入
- `net_amount_s` - 小单净流入

### get_money_flow_pro()

获取专业资金流向数据。

```python
get_money_flow_pro(security_list, start_date=None, end_date=None,
                   frequency='daily', fields=None, count=None, data_type='money')
```

**参数:**
- `frequency` (str): `'daily'` 或 `'minutes'`
- `data_type` (str): `'money'`, `'volume'`, 或 `'deal'`

---

## 融资融券

### get_mtss()

获取融资融券数据。

```python
get_mtss(security_list, start_date=None, end_date=None, fields=None, count=None)
```

### get_margincash_stocks()

获取可融资标的列表。

```python
get_margincash_stocks(date=None) -> list
```

### get_marginsec_stocks()

获取可融券标的列表。

```python
get_marginsec_stocks(date=None) -> list
```

---

## 期货数据

### get_future_contracts()

获取期货合约列表。

```python
get_future_contracts(underlying_symbol, date=None) -> list
```

**参数:**
- `underlying_symbol` (str): 期货品种，如 `'IF'`, `'IC'`, `'IH'`, `'AG'`, `'AU'`
- `date` (str/datetime, optional): 查询日期

### get_dominant_future()

获取主力合约。

```python
get_dominant_future(underlying_symbol=None, date=None, end_date=None)
```

### get_order_future_bar()

获取连续合约行情。

```python
get_order_future_bar(symbol, future_type, start_dt, end_dt,
                     unit='1d', fields=None, include_now=True)
```

**参数:**
- `symbol` (str): 品种代码
- `future_type` (str): 合约类型，`'0'`当月, `'1'`次月, `'0q'`当季, `'1q'`次季

---

## 因子数据

### 因子分类

聚宽提供多种类型的因子数据：

1. **估值因子**
   - 市值（market_cap, circulating_market_cap）
   - 估值比率（pe_ratio, pb_ratio, ps_ratio, pcf_ratio）

2. **技术因子**
   - 均线（MA）
   - 动量（Momentum）
   - 波动率（Volatility）
   - 振幅（Amplitude）

3. **成长因子**
   - 营业收入增长率（inc_revenue_year_on_year）
   - 净利润增长率（net_profit_growth_rate）
   - ROE增长率（roe_yearly）

4. **情绪因子**
   - 换手率（turnover_ratio）
   - 量比

5. **规模因子**
   - 总市值
   - 流通市值

### get_factor_values()

获取因子数据。

```python
get_factor_values(securities, factors, start_date=None, end_date=None, count=None)
```

**参数:**
- `securities` (str/list): 证券代码
- `factors` (list): 因子名称列表
- `start_date` (str/datetime, optional): 开始日期
- `end_date` (str/datetime, optional): 结束日期
- `count` (int, optional): 数据条数

**返回:** dict，key为因子名，value为DataFrame

### get_all_factors()

获取所有可用因子。

```python
get_all_factors() -> DataFrame
```

### get_factor_kanban_values()

获取因子面板数据。

```python
get_factor_kanban_values(universe=None, bt_cycle=None, category=None, model='long_only', **kwargs)
```

**参数:**
- `universe` (str): 股票池，`'hs300'`, `'zz500'`, `'zz800'`, `'zz1000'`, `'zzqz'`
- `bt_cycle` (str): 周期，`'month_3'`, `'year_1'`, `'year_3'`, `'year_10'`
- `category` (str): 分类，`'basics'`, `'quality'`, `'emotion'`, `'growth'`, `'risk'`, `'technical'`, `'momentum'`
- `model` (str): `'long_only'` 或 `'long_short'`

### get_factor_style_returns()

获取风格因子暴露收益率。

```python
get_factor_style_returns(factors=None, start_date=None, end_date=None, 
                        count=None, universe=None, industry='sw_l1')
```

### get_factor_stats()

获取因子历史收益统计。

```python
get_factor_stats(factor_names=None, universe_type='hs300',
                 start_date=None, end_date=None, count=None,
                 skip_paused=False, commision_fee=0.0)
```

### 因子数据获取示例

```python
from jqdatasdk import finance, query

# 获取估值因子
q = query(finance.valuation.code,
          finance.valuation.day,
          finance.valuation.market_cap,
          finance.valuation.pe_ratio,
          finance.valuation.pb_ratio)
q = q.filter(finance.valuation.code == '000001.XSHE')
q = q.filter(finance.valuation.day >= '2024-01-01')
df = finance.run_query(q)

# 获取成长因子
q = query(finance.indicator.code,
          finance.indicator.statDate,
          finance.indicator.inc_revenue_year_on_year,
          finance.indicator.roe)
q = q.filter(finance.indicator.code == '000001.XSHE')
df = finance.run_query(q)
```

### 自定义因子计算

对于聚宽未直接提供的因子，可以通过基础数据计算：

```python
import pandas as pd
import jqdatasdk as jq

# 获取价格数据
df = jq.get_price('000001.XSHE',
                  start_date='2024-01-01',
                  end_date='2024-03-31',
                  frequency='daily')

# 计算动量因子
df = df.reset_index()
df['momentum_20'] = df['close'].pct_change(20) * 100
df['momentum_60'] = df['close'].pct_change(60) * 100

# 计算波动率因子
df['volatility_20'] = df['close'].pct_change().rolling(window=20).std() * 100

# 计算RSI指标
def calculate_rsi(series, period=14):
    delta = series.diff()
    gain = (delta.where(delta > 0, 0)).rolling(window=period).mean()
    loss = (-delta.where(delta < 0, 0)).rolling(window=period).mean()
    rs = gain / loss
    rsi = 100 - (100 / (1 + rs))
    return rsi

df['rsi_14'] = calculate_rsi(df['close'])
```

---

## Alpha因子

### get_all_alpha_101()

获取 Alpha101 因子。

```python
get_all_alpha_101(date, code=None, alpha=None) -> DataFrame
```

### get_all_alpha_191()

获取 Alpha191 因子。

```python
get_all_alpha_191(date, code=None, alpha=None) -> DataFrame
```

---

## 其他接口

### get_trade_days()

获取交易日列表。

```python
get_trade_days(start_date=None, end_date=None, count=None) -> ndarray
```

**示例:**
```python
trade_days = jq.get_trade_days(start_date='2024-01-01', end_date='2024-12-31')
```

### get_all_trade_days()

获取所有交易日。

```python
get_all_trade_days() -> ndarray
```

### get_billboard_list()

获取龙虎榜数据。

```python
get_billboard_list(stock_list=None, start_date=None, end_date=None, count=None)
```

### get_locked_shares()

获取限售股解禁数据。

```python
get_locked_shares(stock_list=None, start_date=None, end_date=None, forward_count=None)
```

### get_table_info()

查询数据表字段信息。

```python
get_table_info(table) -> DataFrame
```

**参数:**
- `table` (str/ORM): 表名或 ORM 对象

### get_preopen_infos()

获取盘前交易信息。

```python
get_preopen_infos(security, fields=("paused", "factor", "high_limit", "low_limit"))
```

### get_query_count()

查询剩余请求条数。

```python
get_query_count(field=None)
```

**参数:**
- `field` (str, optional): `'total'` 或 `'spare'`

**示例:**
```python
count_info = jq.get_query_count()
print(f"已用: {count_info['spare']}")
print(f"总计: {count_info['total']}")
print(f"剩余: {count_info['total'] - count_info['spare']}")
```

---

## 财务表字段参考

### finance.indicator (财务指标表)

| 字段 | 说明 |
|------|------|
| code | 股票代码 |
| pub_date | 发布日期 |
| end_date | 报告期结束日期 |
| eps | 每股收益 |
| eps_yoy | 每股收益同比(%) |
| bvps | 每股净资产 |
| roe | 净资产收益率(%) |
| roe_yoy | 净资产收益率同比(%) |
| net_profits | 净利润(万元) |
| net_profits_yoy | 净利润同比(%) |
| revenue | 营业收入(万元) |
| revenue_yoy | 营业收入同比(%) |
| total_assets | 总资产(万元) |
| total_liab | 总负债(万元) |
| gross_profit | 毛利率(%) |
| net_profit_margin | 净利率(%) |

### finance.balance (资产负债表)

| 字段 | 说明 |
|------|------|
| code | 股票代码 |
| end_date | 报告期结束日期 |
| total_assets | 资产总计 |
| total_liab | 负债合计 |
| total_hldr_eqy_excl_min_int_shares | 归属于母公司股东权益 |
| total_hldr_eqy | 股东权益合计 |

### finance.income (利润表)

| 字段 | 说明 |
|------|------|
| code | 股票代码 |
| end_date | 报告期结束日期 |
| total_revenue | 营业收入 |
| oper_cost | 营业成本 |
| total_operate_income | 营业利润 |
| net_profit | 净利润 |

### finance.cash_flow (现金流量表)

| 字段 | 说明 |
|------|------|
| code | 股票代码 |
| end_date | 报告期结束日期 |
| oper_cash_flow | 经营活动产生的现金流量净额 |
| invest_cash_flow | 投资活动产生的现金流量净额 |
| fin_cash_flow | 筹资活动产生的现金流量净额 |

---

## 错误处理

### 常见错误

| 错误类型 | 说明 | 解决方法 |
|---------|------|---------|
| AuthError | 认证失败 | 检查 Token 或账号密码是否正确 |
| QueryCountExceeded | 调用次数超限 | 查看剩余次数，减少请求 |
| InvalidSecurity | 证券代码无效 | 检查代码格式（如 `000001.XSHE`） |
| NoData | 无数据 | 检查日期范围和代码 |

### 错误处理示例

```python
from jqdatasdk import AuthError

try:
    jq.auth('你的Token', '你的Token')
    df = jq.get_price('000001.XSHE',
                      start_date='2024-01-01',
                      end_date='2024-01-31')
except AuthError:
    print("认证失败，请检查 Token")
except Exception as e:
    print(f"错误: {e}")
```
