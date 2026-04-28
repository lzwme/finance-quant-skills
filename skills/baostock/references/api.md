# BaoStock API 参考文档

本文档提供 BaoStock 所有 API 的详细说明和参数定义。

## 目录

1. [认证与配置](#认证与配置)
2. [行情数据](#行情数据)
3. [财务数据](#财务数据)
4. [股票信息](#股票信息)
5. [行业与指数](#行业与指数)
6. [错误处理](#错误处理)

---

## 认证与配置

### bs.login()

登录 BaoStock 系统。每个会话必须以 `login` 开始。

```python
lg = bs.login()
```

**返回:** LoginResult 对象
- `error_code`: 错误代码，"0" 表示成功
- `error_msg`: 错误信息

**示例:**
```python
import baostock as bs

lg = bs.login()
if lg.error_code == "0":
    print("登录成功")
else:
    print(f"登录失败: {lg.error_msg}")
```

### bs.logout()

登出 BaoStock 系统。每个会话应以 `logout` 结束。

```python
bs.logout()
```

### 自定义服务器配置

支持通过环境变量或代码方式自定义服务器地址：

```python
import os
import baostock as bs
import baostock.common.contants as cons

# 方式1：环境变量
os.environ['BAOSTOCK_SERVER_IP'] = 'your.server.ip'
os.environ['BAOSTOCK_SERVER_PORT'] = '10030'

# 方式2：代码设置
cons.BAOSTOCK_SERVER_IP = 'your.server.ip'
cons.BAOSTOCK_SERVER_PORT = 10030

# 然后登录
lg = bs.login()
```

---

## 行情数据

### query_history_k_data_plus()

获取历史 K 线数据（主要行情接口）。

```python
rs = bs.query_history_k_data_plus(
    code,
    fields,
    start_date=None,
    end_date=None,
    frequency='d',
    adjustflag='3'
)
```

**参数:**

| 参数 | 类型 | 必填 | 说明 |
|------|------|------|------|
| code | str | 是 | 股票代码，如 `sh.600000`、`sz.000001` |
| fields | str | 是 | 字段列表，逗号分隔 |
| start_date | str | 否 | 开始日期，格式 `YYYY-MM-DD` |
| end_date | str | 否 | 结束日期，格式 `YYYY-MM-DD` |
| frequency | str | 否 | 频率：`d`(日线)、`w`(周线)、`m`(月线)、`5`/`15`/`30`/`60`(分钟线)，默认 `d` |
| adjustflag | str | 否 | 复权类型：`1`(后复权)、`2`(前复权)、`3`(不复权)，默认 `3` |

**日线可用字段:**

| 字段 | 说明 |
|------|------|
| date | 日期 |
| code | 证券代码 |
| open | 开盘价 |
| high | 最高价 |
| low | 最低价 |
| close | 收盘价 |
| preclose | 昨收价 |
| volume | 成交量（股） |
| amount | 成交额（元） |
| adjustflag | 复权标志 |
| turn | 换手率（%） |
| tradestatus | 交易状态：0=停牌，1=正常交易 |
| pctChg | 涨跌幅（%） |
| peTTM | 滚动市盈率 |
| pbMRQ | 市净率 |
| psTTM | 滚动市销率 |
| pcfNcfTTM | 滚动市现率 |
| isST | 是否ST：0=否，1=是 |

**分钟线可用字段:**

| 字段 | 说明 |
|------|------|
| date | 日期 |
| time | 时间（格式：HHMMSS） |
| code | 证券代码 |
| open | 开盘价 |
| high | 最高价 |
| low | 最低价 |
| close | 收盘价 |
| volume | 成交量 |
| amount | 成交额 |
| adjustflag | 复权标志 |

**返回:** QueryResult 对象
- `error_code`: 错误代码
- `error_msg`: 错误信息
- `fields`: 字段名列表
- `next()`: 获取下一行数据
- `get_row_data()`: 获取当前行数据列表

**示例:**
```python
# 获取贵州茅台2024年日K线（前复权）
rs = bs.query_history_k_data_plus(
    "sh.600519",
    "date,code,open,high,low,close,volume,amount,pctChg",
    start_date="2024-01-01",
    end_date="2024-12-31",
    frequency="d",
    adjustflag="2"
)

data = []
while rs.next():
    data.append(rs.get_row_data())
df = pd.DataFrame(data, columns=rs.fields)
```

---

## 财务数据

### query_profit_data()

获取盈利能力数据。

```python
rs = bs.query_profit_data(code, year, quarter)
```

**参数:**
- `code` (str): 股票代码
- `year` (int): 年份，如 2023
- `quarter` (int): 季度，1/2/3/4

**返回字段:**

| 字段 | 说明 |
|------|------|
| code | 股票代码 |
| pubDate | 发布日期 |
| statDate | 统计日期 |
| roeAvg | 净资产收益率（平均） |
| npMargin | 销售净利率 |
| gpMargin | 销售毛利率 |
| netProfit | 净利润（万元） |
| epsTTM | 每股收益（TTM） |
| MBRevenue | 主营营业收入（万元） |
| totalShare | 总股本（万股） |
| liqaShare | 流通股本（万股） |

### query_operation_data()

获取营运能力数据。

```python
rs = bs.query_operation_data(code, year, quarter)
```

**返回字段:**

| 字段 | 说明 |
|------|------|
| code | 股票代码 |
| pubDate | 发布日期 |
| statDate | 统计日期 |
| NRTurnRatio | 应收账款周转率（次） |
| NRTurnDays | 应收账款周转天数（天） |
| INVTurnRatio | 存货周转率（次） |
| INVTurnDays | 存货周转天数（天） |
| CATurnRatio | 流动资产周转率（次） |
| AssetTurnRatio | 总资产周转率（次） |

### query_growth_data()

获取成长能力数据。

```python
rs = bs.query_growth_data(code, year, quarter)
```

**返回字段:**

| 字段 | 说明 |
|------|------|
| code | 股票代码 |
| pubDate | 发布日期 |
| statDate | 统计日期 |
| YOYEquity | 净资产同比增长率 |
| YOYAsset | 总资产同比增长率 |
| YOYNI | 净利润同比增长率 |
| YOYEPSBasic | 基本每股收益同比增长率 |
| YOYEPSDiluted | 稀释每股收益同比增长率 |

### query_balance_data()

获取偿债能力数据。

```python
rs = bs.query_balance_data(code, year, quarter)
```

**返回字段:**

| 字段 | 说明 |
|------|------|
| code | 股票代码 |
| pubDate | 发布日期 |
| statDate | 统计日期 |
| currentRatio | 流动比率 |
| quickRatio | 速动比率 |
| cashRatio | 现金比率 |
| YOYLiability | 总负债同比增长率 |
| liabilityToAsset | 资产负债率 |
| assetToEquity | 权益乘数 |

### query_cash_flow_data()

获取现金流量数据。

```python
rs = bs.query_cash_flow_data(code, year, quarter)
```

**返回字段:**

| 字段 | 说明 |
|------|------|
| code | 股票代码 |
| pubDate | 发布日期 |
| statDate | 统计日期 |
| CAToAsset | 流动资产占比 |
| NCAToAsset | 非流动资产占比 |
| tangibleAssetToAsset | 有形资产占比 |
| ebitToInterest | 已获利息倍数 |
| CFOToOR | 经营活动现金净流量与营业收入比率 |
| CFOToNP | 经营性现金净流量与净利润比率 |
| CFOToGr | 经营性现金净流量与营业总收入比率 |

### query_dupont_data()

获取杜邦分析数据。

```python
rs = bs.query_dupont_data(code, year, quarter)
```

**返回字段:**

| 字段 | 说明 |
|------|------|
| code | 股票代码 |
| pubDate | 发布日期 |
| statDate | 统计日期 |
| dupontROE | 净资产收益率（杜邦分析） |
| dupontAssetStoEquity | 权益乘数 |
| dupontAssetTurn | 总资产周转率 |
| dupontPalm | 主营业务利润率 |
| dupontNetPalm | 销售净利率 |
| dupontTaxBurden | 税收负担率 |
| dupontIntBurden | 利息负担率 |
| dupontEBITToOR | 主营业务利润与营业收入比率 |

---

## 股票信息

### query_all_stock()

获取全部证券列表。

```python
rs = bs.query_all_stock(day=None)
```

**参数:**
- `day` (str): 查询日期，格式 `YYYY-MM-DD`，默认今天

**返回字段:**
- `code`: 证券代码
- `tradeStatus`: 交易状态（0=停牌，1=正常）
- `code_name`: 证券名称

### query_stock_basic()

获取股票基本信息。

```python
rs = bs.query_stock_basic(code=None)
```

**参数:**
- `code` (str): 股票代码，不传则返回全部

**返回字段:**
- `code`: 股票代码
- `code_name`: 股票名称
- `ipoDate`: 上市日期
- `outDate`: 退市日期（如有）
- `type`: 类型（1=股票，2=指数，3=其他）
- `status`: 状态（0=退市，1=上市）

### query_trade_dates()

获取交易日历。

```python
rs = bs.query_trade_dates(start_date, end_date)
```

**参数:**
- `start_date` (str): 开始日期 `YYYY-MM-DD`
- `end_date` (str): 结束日期 `YYYY-MM-DD`

**返回字段:**
- `calendar_date`: 日历日期
- `is_trading_day`: 是否交易日（0=否，1=是）

### query_dividend_data()

获取分红信息。

```python
rs = bs.query_dividend_data(code, year, yearType="report")
```

**参数:**
- `code` (str): 股票代码
- `year` (str): 年份，如 "2023"
- `yearType` (str): 类型，`report`(报告期) 或 `operate`(实施期)

---

## 行业与指数

### query_stock_industry()

获取行业分类数据。

```python
rs = bs.query_stock_industry()
```

**返回字段:**
- `updateDate`: 更新日期
- `code`: 证券代码
- `code_name`: 证券名称
- `industry`: 所属行业
- `industryClassification`: 行业分类标准

### query_hs300_stocks()

获取沪深300成分股。

```python
rs = bs.query_hs300_stocks()
```

**返回字段:**
- `code`: 证券代码
- `code_name`: 证券名称

### query_sz50_stocks()

获取上证50成分股。

```python
rs = bs.query_sz50_stocks()
```

### query_zz500_stocks()

获取中证500成分股。

```python
rs = bs.query_zz500_stocks()
```

---

## 股票代码格式

| 市场 | 格式示例 | 说明 |
|------|----------|------|
| 上海证券交易所 | `sh.600000` | A股：sh.6xxxxx |
| 深圳证券交易所 | `sz.000001` | 主板：sz.00xxxx |
| 深圳证券交易所 | `sz.300750` | 创业板：sz.30xxxx |
| 北京证券交易所 | `bj.430047` | 北交所：bj.xxxxxx |
| 上证指数 | `sh.000001` | 上证综指 |
| 沪深300 | `sh.000300` | 沪深300指数 |
| 上证50 | `sh.000016` | 上证50指数 |

---

## 错误处理

### 常见错误代码

| 错误代码 | 说明 | 解决方法 |
|----------|------|----------|
| 0 | 成功 | - |
| 10001011 | IP 已加入黑名单 | 联系 BaoStock 官方解除 |
| -1 | 网络错误 | 检查网络连接 |
| -2 | 参数错误 | 检查参数格式和取值范围 |
| -3 | 无数据 | 检查日期范围和股票代码 |

### 错误处理示例

```python
import baostock as bs

lg = bs.login()
if lg.error_code != "0":
    if lg.error_code == "10001011":
        print("IP 已被加入黑名单，请联系官方")
    else:
        print(f"登录失败: {lg.error_msg} ({lg.error_code})")
    sys.exit(1)

# 查询数据
rs = bs.query_history_k_data_plus("sh.600000", "date,close")
if rs.error_code != '0':
    print(f"查询失败: {rs.error_msg}")
else:
    # 处理数据
    pass

bs.logout()
```

### 使用技巧

1. **数据类型转换**: K线数据默认返回字符串，数值计算前需转换
   ```python
   df['close'] = df['close'].astype(float)
   ```

2. **非线程安全**: 并行下载请使用多进程而非多线程
   ```python
   from multiprocessing import Pool
   # 使用 Pool 进行并行下载
   ```

3. **财务数据延迟**: 季度报告发布后约2个月才能在 BaoStock 获取

4. **分钟线限制**: 指数无分钟级数据，仅股票支持

5. **复权选择**: 
   - 前复权（2）：适用于分析历史走势
   - 后复权（1）：适用于计算收益率
   - 不复权（3）：原始数据
