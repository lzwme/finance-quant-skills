---
name: akshare-docs
description: AKShare 开源金融数据接口库，提供股票、期货、期权、基金、外汇、债券、指数、加密货币等金融产品的基本面数据、实时和历史行情数据、衍生数据。
version: 1.0.0
homepage: https://akshare.akfamily.xyz
metadata:
  {
    "openclaw":
      {
        "emoji": "📈",
        "requires": { "pip": ["akshare>=1.12", "pandas>=1.5"] },
        "install":
          [
            {
              "id": "pip-install",
              "kind": "pip",
              "packages": ["akshare>=1.12", "pandas>=1.5"],
              "label": "安装AKShare依赖"
            }
          ]
      }
  }
keywords:
  - 股票
  - 财经
  - 行情
  - 加密货币
  - 宏观经济
  - AKShare
---

# AKShare财经数据获取 API

## 快速开始

```bash
# 安装依赖
pip install akshare pandas --upgrade

# 测试安装
python -c "import akshare; print(akshare.__version__)"
```

需要 Python 3.9+

## 基本用法

```python
import akshare as ak

# 获取平安银行日K线数据
df = ak.stock_zh_a_hist(symbol="000001", period="daily", start_date="20240101", end_date="20240630")
print(df)
```

### 函数命名规则

```
{asset_type}_{market}_{data_type}_{data_source}
```

- **Asset type**: `stock` (stocks), `futures` (futures), `fund` (funds), `bond` (bonds), `forex` (foreign exchange), `option` (options), `macro` (macroeconomics), `index` (indices)
- **Market**: `zh` (China), `us` (United States), `hk` (Hong Kong), or exchange codes
- **Data type**: `spot` (real-time), `hist` (historical), `daily` (daily bars), `minute` (minute bars)
- **Data source**: `em` (East Money), `sina` (Sina Finance), exchange abbreviations

### 输出格式

默认返回Pandas DataFrame，可直接处理：

```python
df = ak.stock_zh_a_spot_em()
print(df.head())  # 查看前5行
print(df.columns)  # 查看列名
df.to_csv("data.csv")  # 保存CSV
```


## 股票数据（A股）

### 实时行情 — 全部A股

```python
import akshare as ak

# 获取全部A股实时行情
df = ak.stock_zh_a_spot_em()
# 返回字段: 序号、代码、名称、最新价、涨跌幅、涨跌额、成交量、成交额、振幅、最高、最低、今开、昨收、量比、换手率、市盈率、市净率 ...
```

### 历史K线数据

```python
# 获取指定股票历史日K线数据
df = ak.stock_zh_a_hist(
    symbol="000001",       # 股票代码（不带前缀）
    period="daily",        # 周期: "daily"(日), "weekly"(周), "monthly"(月)
    start_date="20240101", # 开始日期，格式YYYYMMDD
    end_date="20240630",   # 结束日期
    adjust=""              # 复权: ""(不复权), "qfq"(前复权), "hfq"(后复权)
)
# 返回字段: 日期、开盘、收盘、最高、最低、成交量、成交额、振幅、涨跌幅、涨跌额、换手率
```

### 分钟级K线数据

```python
# 获取分钟级K线数据
df = ak.stock_zh_a_hist_min_em(
    symbol="000001",
    period="5",            # 分钟间隔: "1", "5", "15", "30", "60"
    start_date="2024-01-02 09:30:00",
    end_date="2024-01-02 15:00:00",
    adjust=""              # 复权类型
)
```

### 个股基本信息

```python
# 获取个股基本信息
df = ak.stock_individual_info_em(symbol="000001")
# 返回字段: 总市值、流通市值、行业、上市时间、股票代码、股票简称、总股本、流通股 ...
```

## 港股数据

```python
# 港股实时行情
df = ak.stock_hk_spot_em()

# 港股历史K线数据
df = ak.stock_hk_hist(
    symbol="00700",        # 腾讯控股
    period="daily",        # 日线
    start_date="20240101",
    end_date="20240630",
    adjust="qfq"           # 前复权
)
```

## 美股数据

```python
# 美股日线数据
df = ak.stock_us_daily(symbol="AAPL", adjust="qfq")

# 美股实时行情
df = ak.stock_us_spot_em()
```

## 指数数据

```python
# A股指数历史数据 (e.g., Shanghai Composite Index 000001)
df = ak.stock_zh_index_daily_em(symbol="sh000001")

# 指数成分股 (e.g., CSI 300)
df = ak.index_stock_cons_csindex(symbol="000300")
```


## 基金数据

```python
# ETF实时行情
df = ak.fund_etf_spot_em()

# ETF历史K线数据
df = ak.fund_etf_hist_em(
    symbol="510300",       # 沪深300ETF
    period="daily",
    start_date="20240101",
    end_date="20240630",
    adjust="qfq"
)

# 开放式基金每日净值
df = ak.fund_open_fund_daily_em(symbol="000001")

# 基金评级
df = ak.fund_rating_all()
```


## 期货数据

```python
# 期货日线数据（按交易所汇总）
from akshare import get_futures_daily
df = get_futures_daily(start_date="20240101", end_date="20240102", market="CFFEX")
# 交易所选项: "CFFEX"(中金所), "SHFE"(上期所), "DCE"(大商所), "CZCE"(郑商所), "INE"(上海国际能源交易中心), "GFEX"(广期所)

# 期货实时行情
df = ak.futures_zh_spot()

# 期货库存数据
df = ak.futures_inventory_99(symbol="豆一")
```


## 期权数据

```python
# 交易所期权历史数据
df = ak.option_hist_dce(symbol="豆粕期权")

# 上证50ETF期权
df = ak.option_sse_spot_price(symbol="510050")
```


## 债券数据

```python
# 可转债列表
df = ak.bond_zh_cov()

# 可转债历史K线数据
df = ak.bond_zh_hs_cov_daily(symbol="sz123456")

# 中国债券现货报价
df = ak.bond_spot_quote()
```


## 外汇贵金属

```python
# 外汇实时行情（东方财富）
df = ak.forex_spot_em()

# 外汇即期报价（中国外汇交易中心）
df = ak.fx_spot_quote()

# 外汇掉期报价
df = ak.fx_swap_quote()

# 外汇汇率
df = ak.forex_usd_cny()  # 美元兑人民币

# 贵金属
df = ak.metals_shibor()  # 上海银行间拆借利率

# 金银价格
df = ak.metals_gold()  # 国际金价
```


## 财务数据

```python
# 股票基本面
ak.stock_fundamental(symbol="000001")  # 基本面数据

# 估值指标
ak.stock_valuation(symbol="000001")  # PE、PB等

# 盈利能力
ak.stock_profit_em(symbol="000001")
```


## 加密货币

```python
# 币种列表
ak.crypto_binance_symbols()  # 币安交易对

# 实时价格
ak.crypto_binance_btc_usdt_spot()  # BTC/USDT

# K线数据
ak.crypto_binance_btc_usdt_kline(period="daily")
```


## 宏观经济

```python
# 中国CPI年度数据
df = ak.macro_china_cpi_yearly()

# 中国GDP
df = ak.macro_china_gdp()
# 中国GDP年度数据
df = ak.macro_china_gdp_yearly()

# 中国PMI数据
df = ak.macro_china_pmi()

# 美国非农就业数据
df = ak.macro_usa_non_farm()

# 美国CPI月度数据
df = ak.macro_usa_cpi_monthly()
```

## 新闻与舆情

```python
# 个股财经新闻（东方财富）
df = ak.stock_news_em(symbol="000001")

# 央视新闻
df = ak.news_cctv(date="20240101")
```

## 完整示例：下载数据并绘制K线图

```python
import akshare as ak
import pandas as pd
import mplfinance as mpf  # pip install mplfinance

# 获取贵州茅台前复权日K线数据
df = ak.stock_zh_a_hist(
    symbol="600519",
    period="daily",
    start_date="20240101",
    end_date="20240630",
    adjust="qfq"
)

# 设置日期索引并重命名列为英文（mplfinance要求）
df.index = pd.to_datetime(df["日期"])  # 设置日期为索引
df.rename(columns={
    "开盘": "Open",    # 开盘价
    "收盘": "Close",   # 收盘价
    "最高": "High",    # 最高价
    "最低": "Low",     # 最低价
    "成交量": "Volume" # 成交量
}, inplace=True)

# 绘制K线图（含5/10/20日均线和成交量）
mpf.plot(df, type="candle", mav=(5, 10, 20), volume=True)
```


## 使用技巧

- 所有函数返回 **pandas DataFrame** — 可直接用于分析、导出和可视化。
- A股数据列名为**中文**；美股/港股数据列名为英文。
- 使用 `--upgrade` 保持akshare最新版 — 由于上游数据源变化，接口更新频繁。
- 非Python用户可使用 [AKTools](https://aktools.readthedocs.io/) HTTP API封装。
- 数据仅供**学术研究**使用 — 不构成投资建议。
- 完整API参考：https://akshare.akfamily.xyz/data/index.html


## 进阶示例

### 市场概览

```python
# A股大盘
index_zh_a_spot()  # 大盘指数

# 涨跌幅排行
stock_zh_a_spot_em()[['代码', '名称', '涨跌幅']].sort_values('涨跌幅', ascending=False)
```

### 批量下载多只股票

```python
import akshare as ak
import pandas as pd

# 定义要下载的股票列表
stock_list = ["000001", "600519", "300750", "601318", "000858"]

all_data = {}
for symbol in stock_list:
    # 下载每只股票的前复权日K线数据
    df = ak.stock_zh_a_hist(
        symbol=symbol,
        period="daily",
        start_date="20240101",
        end_date="20240630",
        adjust="qfq"
    )
    df["股票代码"] = symbol  # 添加股票代码列，便于后续合并
    all_data[symbol] = df
    print(f"已下载 {symbol}，共 {len(df)} 条记录")

# 合并所有股票数据为一个大的DataFrame
combined = pd.concat(all_data.values(), ignore_index=True)
combined.to_csv("multi_stock_data.csv", index=False)
print(f"合并总计: {len(combined)} 条记录")
```

### 计算技术指标（均线、MACD、RSI）

```python
import akshare as ak
import pandas as pd
import numpy as np

# 获取贵州茅台前复权日K线数据
df = ak.stock_zh_a_hist(symbol="600519", period="daily",
                         start_date="20240101", end_date="20241231", adjust="qfq")

# 将收盘价转换为浮点数 (收盘 = close price)
df["收盘"] = df["收盘"].astype(float)

# 计算均线
df["MA5"] = df["收盘"].rolling(window=5).mean()    # 5日均线
df["MA10"] = df["收盘"].rolling(window=10).mean()   # 10日均线
df["MA20"] = df["收盘"].rolling(window=20).mean()   # 20日均线
df["MA60"] = df["收盘"].rolling(window=60).mean()   # 60日均线

# 计算MACD指标
ema12 = df["收盘"].ewm(span=12, adjust=False).mean()  # 12日指数移动平均
ema26 = df["收盘"].ewm(span=26, adjust=False).mean()  # 26日指数移动平均
df["DIF"] = ema12 - ema26                              # 快线（DIF）
df["DEA"] = df["DIF"].ewm(span=9, adjust=False).mean() # 慢线（DEA）
df["MACD"] = 2 * (df["DIF"] - df["DEA"])               # MACD柱

# 计算RSI指标（14日）
delta = df["收盘"].diff()
gain = delta.where(delta > 0, 0)       # 上涨幅度
loss = -delta.where(delta < 0, 0)      # 下跌幅度
avg_gain = gain.rolling(window=14).mean()
avg_loss = loss.rolling(window=14).mean()
rs = avg_gain / avg_loss
df["RSI14"] = 100 - (100 / (1 + rs))   # RSI值

# 计算布林带（20日）
df["BOLL_MID"] = df["收盘"].rolling(window=20).mean()           # 中轨
df["BOLL_UP"] = df["BOLL_MID"] + 2 * df["收盘"].rolling(window=20).std()  # 上轨
df["BOLL_DN"] = df["BOLL_MID"] - 2 * df["收盘"].rolling(window=20).std()  # 下轨

# 展示：日期、收盘价及各技术指标
print(df[["日期", "收盘", "MA5", "MA20", "DIF", "DEA", "MACD", "RSI14"]].tail(10))
```

### 筛选涨停股

```python
import akshare as ak

# 获取全部A股实时行情
df = ak.stock_zh_a_spot_em()

# 筛选涨幅>9.5%的股票（接近涨停）
df["涨跌幅"] = df["涨跌幅"].astype(float)  # 涨跌幅 = change percentage
limit_up = df[df["涨跌幅"] >= 9.5].sort_values("涨跌幅", ascending=False)
print(f"今日涨停/接近涨停股票: 共 {len(limit_up)} 只")
# 展示：代码、名称、最新价、涨跌幅、成交额、换手率
print(limit_up[["代码", "名称", "最新价", "涨跌幅", "成交额", "换手率"]].head(20))
```

### 获取龙虎榜数据

```python
import akshare as ak

# 获取龙虎榜详细数据
df = ak.stock_lhb_detail_em(start_date="20240101", end_date="20240131")
print(df.head())

# 获取龙虎榜营业部排名
df_dept = ak.stock_lhb_hyyyb_em(start_date="20240101", end_date="20240131")
print(df_dept.head())
```

### 获取融资融券数据

```python
import akshare as ak

# 获取沪深融资融券汇总数据
df = ak.stock_margin_sse(start_date="20240101", end_date="20240630")
print(df.head())

# 获取个股融资融券明细
df_detail = ak.stock_margin_detail_sse(date="20240102")
print(df_detail.head())
```

### 获取北向资金（陆港通）数据

```python
import akshare as ak

# 获取北向资金历史数据
df = ak.stock_hsgt_hist_em(symbol="北向资金")  # 北向资金 = Northbound capital
print(df.tail(10))

# 获取北向资金持股明细
df_hold = ak.stock_hsgt_hold_stock_em(market="北向", indicator="今日排行")  # 北向 = Northbound, 今日排行 = Today's ranking
print(df_hold.head(20))
```

### 获取股东数据

```python
import akshare as ak

# 获取前十大股东
df = ak.stock_gdfx_top_10_em(symbol="600519", date="20231231")
print(df)

# 获取前十大流通股东
df_float = ak.stock_gdfx_free_top_10_em(symbol="600519", date="20231231")
print(df_float)
```

### 获取板块行情数据

```python
import akshare as ak

# 获取行业板块行情
df_industry = ak.stock_board_industry_name_em()
print(df_industry.head(20))

# 获取概念板块行情
df_concept = ak.stock_board_concept_name_em()
print(df_concept.head(20))

# 获取特定板块成分股
df_stocks = ak.stock_board_industry_cons_em(symbol="银行")  # 银行 = Banking
print(df_stocks)
```

### 获取限售解禁数据

```python
import akshare as ak

# 获取限售解禁数据
df = ak.stock_restricted_release_queue_em(symbol="全部A股")  # 全部A股 = All A-shares
print(df.head(20))
```

### 获取市场资金流向

```python
import akshare as ak

# 获取大盘资金流向
df = ak.stock_market_fund_flow()
print(df.tail(10))

# 获取个股资金流向
df_stock = ak.stock_individual_fund_flow(stock="000001", market="sz")
print(df_stock.tail(10))
```

### 完整示例：多因子选股

```python
import akshare as ak
import pandas as pd

# 步骤1：获取全部A股实时行情
df = ak.stock_zh_a_spot_em()

# 步骤2：转换数据类型
for col in ["市盈率-动态", "市净率", "换手率", "涨跌幅", "成交额"]:
    df[col] = pd.to_numeric(df[col], errors="coerce")

# 步骤3：多因子筛选
# 条件1：PE 在5-30之间（排除亏损和高估值）
# 条件2：PB 在0.5-5之间
# 条件3：换手率 > 1%（合理流动性）
# 条件4：涨跌幅在-3%到3%之间（排除异常波动）
filtered = df[
    (df["市盈率-动态"] > 5) & (df["市盈率-动态"] < 30) &
    (df["市净率"] > 0.5) & (df["市净率"] < 5) &
    (df["换手率"] > 1) &
    (df["涨跌幅"] > -3) & (df["涨跌幅"] < 3)
].copy()

# 步骤4：按PE排序，选取最低PE的前20只股票
result = filtered.sort_values("市盈率-动态").head(20)
print(f"筛选出 {len(result)} 只股票:")
print(result[["代码", "名称", "最新价", "市盈率-动态", "市净率", "换手率", "涨跌幅"]])
```

## 其他代码参考示例

- [获取加密货币价格和K线数据](./scripts/crypto_price.py)
- [获取宏观经济概览](./scripts/macro_data.py)
- [获取股票实时价格和K线数据](./scripts/stock_price.py)


## 参考文档

- AKShare文档: https://akshare.akfamily.xyz
- GitHub: https://github.com/akfamily/akshare
