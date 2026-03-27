---
name: baostock
description: BaoStock A股数据平台，免费开源，支持股票行情、K线、财务数据、行业分类、指数成分股查询；当用户需要获取A股历史行情、财务报表、交易日历等数据时使用。
metadata: {"clawdbot":{"emoji":"📈","requires":{"bins":["python3"]}}}
---

# BaoStock

[BaoStock](https://www.baostock.com) 是一个免费的开源中国A股证券数据平台。无需注册或API Key，返回 `pandas.DataFrame`。数据覆盖范围：A股自1990年至今。

## 安装

```bash
pip install baostock --upgrade
```

验证安装：

```bash
python -c "import baostock as bs; lg = bs.login(); print(lg.error_msg); bs.logout()"
```

预期输出：`login success!`。

## 基本用法

每个会话必须以 `bs.login()` 开始，以 `bs.logout()` 结束：

```python
import baostock as bs
import pandas as pd

# 登录系统
lg = bs.login()

# ... 在此执行数据查询 ...

# 登出系统
bs.logout()
```

使用 `.get_data()` 从查询结果中获取DataFrame：

```python
rs = bs.query_all_stock()
df = rs.get_data()
```

## 股票代码格式

- 上海证券交易所: `sh.600000`, `sh.601398`
- 深圳证券交易所: `sz.000001`, `sz.300750`
- 北京证券交易所: `bj.430047`
- 指数: `sh.000001`（上证综指）, `sh.000300`（沪深300）

## 核心API

### 1. query_all_stock — 获取全部证券列表

获取指定交易日的全部股票/指数代码。

```python
# 获取指定日期所有证券代码
rs = bs.query_all_stock(day="2024-01-02")
df = rs.get_data()
# 返回字段: code(证券代码), tradeStatus(交易状态), code_name(证券名称)
```

- **day** — 日期字符串 `YYYY-MM-DD`（默认今天）。非交易日返回空DataFrame。

### 2. query_history_k_data_plus — K线数据

获取历史K线数据（开高低收量 + 指标）。

```python
# 获取工商银行日K线数据
rs = bs.query_history_k_data_plus(
    "sh.601398",
    "date,code,open,high,low,close,volume,amount,pctChg",
    start_date="2024-01-01",
    end_date="2024-06-30",
    frequency="d",       # 频率: d(日线), w(周线), m(月线), 5/15/30/60(分钟线)
    adjustflag="3"       # 复权: 1(后复权), 2(前复权), 3(不复权，默认)
)
df = rs.get_data()
```

**参数说明：**

- **code** — 股票代码，格式 `sh.600000` 或 `sz.000001`
- **fields** — 逗号分隔的字段名（见下方）
- **start_date / end_date** — `YYYY-MM-DD` 格式
- **frequency** — `d`(日线), `w`(周线), `m`(月线), `5`/`15`/`30`/`60`(分钟线)。指数无分钟级数据。
- **adjustflag** — `1`(后复权), `2`(前复权), `3`(不复权，默认)

**日线可用字段：**

`date`(日期), `code`(证券代码), `open`(开盘价), `high`(最高价), `low`(最低价), `close`(收盘价), `preclose`(昨收价), `volume`(成交量), `amount`(成交额), `adjustflag`(复权标志), `turn`(换手率), `tradestatus`(交易状态), `pctChg`(涨跌幅), `peTTM`(滚动市盈率), `pbMRQ`(市净率), `psTTM`(滚动市销率), `pcfNcfTTM`(滚动市现率), `isST`(是否ST)

**分钟线可用字段：**

`date`(日期), `time`(时间), `code`(证券代码), `open`(开盘价), `high`(最高价), `low`(最低价), `close`(收盘价), `volume`(成交量), `amount`(成交额), `adjustflag`(复权标志)

### 3. query_trade_dates — 交易日历

```python
# 获取指定范围的交易日历
rs = bs.query_trade_dates(start_date="2024-01-01", end_date="2024-12-31")
df = rs.get_data()
# 返回字段: calendar_date(日历日期), is_trading_day(是否交易日)
```

### 4. query_stock_industry — 行业分类

```python
# 获取全部股票行业分类
rs = bs.query_stock_industry()
df = rs.get_data()
# 返回字段: updateDate(更新日期), code(证券代码), code_name(证券名称), industry(行业), industryClassification(行业分类)
```

### 5. query_stock_basic — 股票基本信息

```python
# 获取指定股票基本信息
rs = bs.query_stock_basic(code="sh.601398")
df = rs.get_data()
# 返回字段: code(证券代码), code_name(证券名称), ipoDate(上市日期), outDate(退市日期), type(类型), status(状态)
```

- **type** — `1` 股票, `2` 指数, `3` 其他
- **status** — `1` 上市, `0` 退市

### 6. query_dividend_data — 分红信息

```python
# 获取指定股票分红数据
rs = bs.query_dividend_data(code="sh.601398", year="2023", yearType="report")
df = rs.get_data()
```

- **yearType** — `report`(报告期) 或 `operate`(实施期)

### 7. 财务数据（季度）

#### 盈利能力

```python
# 获取盈利能力指标（ROE、净利润率、毛利率等）
rs = bs.query_profit_data(code="sh.601398", year=2023, quarter=4)
df = rs.get_data()
```

#### 营运能力

```python
# 获取营运能力指标（存货周转率、应收账款周转率等）
rs = bs.query_operation_data(code="sh.601398", year=2023, quarter=4)
df = rs.get_data()
```

#### 成长能力

```python
# 获取成长能力指标（营收同比增长、净利润同比增长等）
rs = bs.query_growth_data(code="sh.601398", year=2023, quarter=4)
df = rs.get_data()
```

#### 偿债能力

```python
# 获取偿债能力指标（流动比率、速动比率等）
rs = bs.query_balance_data(code="sh.601398", year=2023, quarter=4)
df = rs.get_data()
```

#### 现金流

```python
# 获取现金流数据
rs = bs.query_cash_flow_data(code="sh.601398", year=2023, quarter=4)
df = rs.get_data()
```

#### 杜邦分析

```python
# 获取杜邦分析数据（ROE分解：利润率×资产周转率×权益乘数）
rs = bs.query_dupont_data(code="sh.601398", year=2023, quarter=4)
df = rs.get_data()
```

### 8. 指数数据

#### 指数成分股

```python
# 获取沪深300成分股
rs = bs.query_hs300_stocks()
df = rs.get_data()

# 获取上证50成分股
rs = bs.query_sz50_stocks()
df = rs.get_data()

# 获取中证500成分股
rs = bs.query_zz500_stocks()
df = rs.get_data()
```

## 使用示例

### 下载单只股票数据并保存

```python
import baostock as bs
import pandas as pd

bs.login()

# 获取贵州茅台2024年日K线数据（后复权）
rs = bs.query_history_k_data_plus(
    "sh.600519",
    "date,code,open,high,low,close,volume,amount,pctChg,peTTM",
    start_date="2024-01-01",
    end_date="2024-12-31",
    frequency="d",
    adjustflag="2"  # 后复权
)
df = rs.get_data()

# 保存到CSV文件
df.to_csv("kweichow_moutai_2024.csv", index=False)
print(df.head())

bs.logout()
```

### 批量下载多只股票数据

```python
import baostock as bs
import pandas as pd

bs.login()

# 定义要下载的股票列表
stock_list = ["sh.600519", "sh.601398", "sz.000001", "sz.300750", "sh.601318"]

all_data = []
for code in stock_list:
    # 获取日K线数据（前复权）
    rs = bs.query_history_k_data_plus(
        code,
        "date,code,open,high,low,close,volume,amount,pctChg,turn,peTTM,pbMRQ",
        start_date="2024-01-01",
        end_date="2024-06-30",
        frequency="d",
        adjustflag="1"  # 前复权
    )
    df = rs.get_data()
    all_data.append(df)
    print(f"已下载 {code}，共 {len(df)} 条记录")

# 合并所有数据
combined = pd.concat(all_data, ignore_index=True)
combined.to_csv("multi_stock_baostock.csv", index=False)
print(f"合并总记录数: {len(combined)}")

bs.logout()
```

### 获取全市场股票列表并筛选

```python
import baostock as bs
import pandas as pd

bs.login()

# 获取指定日期所有证券
rs = bs.query_all_stock(day="2024-06-28")
df = rs.get_data()

# 筛选正常交易的股票（排除指数和停牌股）
stocks = df[df["tradeStatus"] == "1"]
# 筛选上海A股（sh.6开头）
sh_stocks = stocks[stocks["code"].str.startswith("sh.6")]
print(f"沪市A股: {len(sh_stocks)} 只")

# 筛选深圳主板（sz.00开头）
sz_main = stocks[stocks["code"].str.startswith("sz.00")]
print(f"深圳主板: {len(sz_main)} 只")

# 筛选创业板（sz.30开头）
gem = stocks[stocks["code"].str.startswith("sz.30")]
print(f"创业板: {len(gem)} 只")

bs.logout()
```

### 获取沪深300成分股并下载数据

```python
import baostock as bs
import pandas as pd

bs.login()

# 获取沪深300成分股
rs = bs.query_hs300_stocks()
hs300 = rs.get_data()
print(f"沪深300共 {len(hs300)} 只成分股")

# 下载前10只成分股的日K线数据
for _, row in hs300.head(10).iterrows():
    code = row["code"]
    name = row["code_name"]
    rs = bs.query_history_k_data_plus(
        code,
        "date,code,close,pctChg,turn",
        start_date="2024-06-01",
        end_date="2024-06-30",
        frequency="d",
        adjustflag="1"
    )
    df = rs.get_data()
    print(f"{name}({code}): {len(df)} 条记录")

bs.logout()
```

### 获取财务数据并分析

```python
import baostock as bs
import pandas as pd

bs.login()

# 获取多只银行股的盈利能力数据
bank_codes = ["sh.601398", "sh.601939", "sh.601288", "sh.600036", "sh.601166"]
profit_data = []

for code in bank_codes:
    rs = bs.query_profit_data(code=code, year=2023, quarter=4)
    df = rs.get_data()
    if not df.empty:
        profit_data.append(df.iloc[0])

profit_df = pd.DataFrame(profit_data)
# 查看ROE和净利润率
print(profit_df[["code", "roeAvg", "npMargin", "gpMargin"]])

# 获取成长能力数据
growth_data = []
for code in bank_codes:
    rs = bs.query_growth_data(code=code, year=2023, quarter=4)
    df = rs.get_data()
    if not df.empty:
        growth_data.append(df.iloc[0])

growth_df = pd.DataFrame(growth_data)
# 查看营收增长率和净利润增长率
print(growth_df[["code", "YOYEquity", "YOYAsset", "YOYNI"]])

bs.logout()
```

### 配合回测框架使用

baostock 获取的数据可直接传入 backtrader 或 rqalpha 进行回测：

```python
import baostock as bs
import pandas as pd

bs.login()

# 获取数据
rs = bs.query_history_k_data_plus(
    "sh.600000",
    "date,open,high,low,close,volume",
    start_date="2023-01-01", end_date="2024-01-01",
    frequency="d", adjustflag="2"  # 后复权
)
df = rs.get_data()
bs.logout()

# 转换为 backtrader 所需格式
df['date'] = pd.to_datetime(df['date'])
df.set_index('date', inplace=True)
for col in ['open', 'high', 'low', 'close', 'volume']:
    df[col] = df[col].astype(float)

# 传入 backtrader
# import backtrader as bt
# data = bt.feeds.PandasData(dataname=df)
# cerebro.adddata(data)
```

## 常见错误处理

| 错误 | 原因 | 解决方法 |
|------|------|----------|
| `login success!` 后查询返回空 | 非交易日或代码错误 | 确认日期为交易日，检查代码格式 |
| 数据全部为空字符串 | fields 参数未指定或格式错误 | 明确指定所需的 fields 字段列表 |
| 会话超时 | 长时间未活动 | 重新调用 `bs.login()` |
| 并行查询报错 | baostock 非线程安全 | 使用 `multiprocessing`（多进程）替代 `threading` |
| K线数据字段类型为字符串 | 默认返回字符串类型 | 使用 `.astype(float)` 转换数值字段 |

## 使用技巧

- **无需注册或API Key** — 直接调用 `bs.login()` 即可开始。
- 长时间不活动会话可能超时 — 重新调用 `bs.login()` 即可。
- **非线程安全** — 并行下载请使用 `multiprocessing`（多进程），而非 threading（多线程）。
- 财务数据按季度提供，报告期结束后约有2个月的延迟。
- 文档：http://baostock.com/baostock/index.php/Python_API%E6%96%87%E6%A1%A3

## 规则

- 使用此 Skill 前，确认用户需要的是**A股历史数据获取**。若用户需要进行策略回测，应引导配合 backtrader/rqalpha 等回测框架 Skill 使用。
- baostock 仅负责数据获取，不要在此 Skill 中实现回测逻辑或技术指标计算（应引导用户使用对应框架）。
- 每个会话必须以 `bs.login()` 开始、`bs.logout()` 结束。
- 注意 K线数据默认返回字符串类型，传入回测框架前需用 `.astype(float)` 转换数值字段。
- 股票代码格式为 `sh.XXXXXX` 或 `sz.XXXXXX`，不要使用纯数字格式。
