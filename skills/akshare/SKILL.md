---
name: akshare
description: AKShare 开源金融数据接口库，提供股票、期货、期权、基金、外汇、债券、指数、加密货币等全品类金融数据；当用户需要获取各类金融市场数据时使用
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
  - 期货
  - 期权
  - 基金
  - 外汇
  - 债券
  - 指数
  - 加密货币
  - 宏观经济
  - AKShare
---

# AKShare 金融数据获取

## 任务目标
- 本 Skill 用于：通过 AKShare 接口获取全品类金融市场数据
- 能力包含：股票、期货、期权、基金、外汇、债券、指数、加密货币、宏观经济等数据
- 触发条件：用户提及 AKShare 或需要获取各类金融数据时

## 前置准备
- 依赖说明：安装 akshare 库（已包含在 dependency 中）
- 凭证配置：AKShare 无需注册或 API Key，直接调用即可使用
- 环境要求：Python 3.9+，建议定期更新 `pip install akshare --upgrade`

## 操作步骤
- 标准流程：
  1. 确定数据需求 — 智能体理解用户意图（股票/期货/基金/外汇等）
  2. 调用对应脚本 — 根据数据类型选择脚本
  3. 解析结果 — 智能体分析返回的 JSON 格式数据
- 脚本调用映射：
  - 股票数据 → `python scripts/stock_data.py --type hist --symbol 000001 --start 20240101 --end 20240131`
  - 期货数据 → `python scripts/futures_data.py --type daily --exchange CFFEX --start 20240101 --end 20240131`
  - 基金数据 → `python scripts/fund_data.py --type etf --symbol 510300`
  - 外汇数据 → `python scripts/forex_data.py --type spot --symbol usd`
  - 宏观经济 → `python scripts/macro_data.py --type gdp`
  - 加密货币 → `python scripts/crypto_data.py --type price --symbol BTC/USDT`
- 可选分支：
  - 当需要多只标的：使用逗号分隔多个代码
  - 当需要指定周期：使用 `--period` 参数（daily/weekly/monthly）
  - 当需要复权数据：使用 `--adjust` 参数（qfq/hfq/空值）

## 使用示例
- 示例1：获取股票历史K线
  - 场景/输入：用户说"获取贵州茅台2024年的日K线数据"
  - 预期产出：返回日期、开盘价、最高价、最低价、收盘价、成交量等OHLCV数据
  - 关键要点：调用 `python scripts/stock_data.py --type hist --symbol 600519 --start 20240101 --end 20241231 --period daily --adjust qfq`
- 示例2：获取期货数据
  - 场景/输入：用户说"查看沪深300股指期货数据"
  - 预期产出：返回期货合约的K线数据、持仓量、成交量等信息
  - 关键要点：调用 `python scripts/futures_data.py --type daily --symbol IF2406 --start 20240101 --end 20240131`
- 示例3：获取基金数据
  - 场景/输入：用户说"查询沪深300ETF的行情"
  - 预期产出：返回ETF的实时行情或历史净值数据
  - 关键要点：调用 `python scripts/fund_data.py --type etf --symbol 510300`
- 示例4：获取宏观经济数据
  - 场景/输入：用户说"查看中国GDP数据"
  - 预期产出：返回GDP历史数据和最新值
  - 关键要点：调用 `python scripts/macro_data.py --type gdp`

## 数据分类详解

### 股票数据（A股/港股/美股）
- **实时行情**：`ak.stock_zh_a_spot_em()` - 全部A股实时行情
- **历史K线**：`ak.stock_zh_a_hist(symbol, period, start_date, end_date, adjust)`
- **分钟K线**：`ak.stock_zh_a_hist_min_em(symbol, period, start_date, end_date)`
- **个股信息**：`ak.stock_individual_info_em(symbol)` - 基本信息、市值、行业等
- **财务数据**：`ak.stock_fundamental(symbol)` - 基本面数据
- **估值指标**：`ak.stock_valuation(symbol)` - PE、PB等
- **港股数据**：`ak.stock_hk_spot_em()`, `ak.stock_hk_hist()`
- **美股数据**：`ak.stock_us_daily(symbol)`, `ak.stock_us_spot_em()`

### 期货数据
- **期货行情**：`ak.futures_zh_spot()` - 实时行情
- **期货K线**：`get_futures_daily(start_date, end_date, market)` - 按交易所
- **库存数据**：`ak.futures_inventory_99(symbol)` - 期货库存

### 基金数据
- **ETF行情**：`ak.fund_etf_spot_em()` - ETF实时行情
- **ETF历史**：`ak.fund_etf_hist_em(symbol, period, start_date, end_date, adjust)`
- **开放式基金**：`ak.fund_open_fund_daily_em(symbol)` - 每日净值
- **基金评级**：`ak.fund_rating_all()` - 基金评级信息

### 期权数据
- **期权历史**：`ak.option_hist_dce(symbol)` - 交易所期权数据
- **ETF期权**：`ak.option_sse_spot_price(symbol)` - 上证50ETF期权

### 债券数据
- **可转债**：`ak.bond_zh_cov()` - 可转债列表
- **可转债K线**：`ak.bond_zh_hs_cov_daily(symbol)` - 可转债历史数据
- **债券报价**：`ak.bond_spot_quote()` - 中国债券现货报价

### 外汇贵金属
- **外汇行情**：`ak.forex_spot_em()` - 外汇实时行情
- **汇率数据**：`ak.forex_usd_cny()` - 美元兑人民币
- **贵金属**：`ak.metals_gold()` - 国际金价

### 指数数据
- **A股指数**：`ak.stock_zh_index_daily_em(symbol)` - 指数历史数据
- **指数成分**：`ak.index_stock_cons_csindex(symbol)` - 指数成分股

### 加密货币
- **币种列表**：`ak.crypto_binance_symbols()` - 币安交易对
- **实时价格**：`ak.crypto_binance_btc_usdt_spot()` - BTC/USDT价格
- **K线数据**：`ak.crypto_binance_btc_usdt_kline(period)` - 加密货币K线

### 宏观经济
- **中国GDP**：`ak.macro_china_gdp()`, `ak.macro_china_gdp_yearly()`
- **CPI数据**：`ak.macro_china_cpi_yearly()`, `ak.macro_china_cpi()`
- **PMI数据**：`ak.macro_china_pmi()`
- **美国数据**：`ak.macro_usa_non_farm()`, `ak.macro_usa_cpi_monthly()`

### 特色数据
- **龙虎榜**：`ak.stock_lhb_detail_em(start_date, end_date)` - 龙虎榜详情
- **融资融券**：`ak.stock_margin_sse(start_date, end_date)` - 融资融券数据
- **北向资金**：`ak.stock_hsgt_hist_em(symbol)` - 陆港通数据
- **股东数据**：`ak.stock_gdfx_top_10_em(symbol, date)` - 前十大股东
- **板块行情**：`ak.stock_board_industry_name_em()` - 行业板块
- **限售解禁**：`ak.stock_restricted_release_queue_em(symbol)` - 限售解禁
- **资金流向**：`ak.stock_market_fund_flow()` - 市场资金流向

## 资源索引
### 脚本：
- [scripts/stock_data.py](scripts/stock_data.py)（用途与参数：获取股票K线/行情/财务数据，支持 --type/--symbol/--start/--end/--period/--adjust）
- [scripts/futures_data.py](scripts/futures_data.py)（用途与参数：获取期货数据，支持 --type/--symbol/--exchange/--start/--end）
- [scripts/fund_data.py](scripts/fund_data.py)（用途与参数：获取基金数据，支持 --type/--symbol/--start/--end）
- [scripts/forex_data.py](scripts/forex_data.py)（用途与参数：获取外汇贵金属数据，支持 --type/--symbol）
- [scripts/macro_data.py](scripts/macro_data.py)（用途与参数：获取宏观经济数据，支持 --type）
- [scripts/crypto_data.py](scripts/crypto_data.py)（用途与参数：获取加密货币数据，支持 --type/--symbol/--period）
- [scripts/index_data.py](scripts/index_data.py)（用途与参数：获取指数数据，支持 --type/--symbol/--start/--end）
- [scripts/option_data.py](scripts/option_data.py)（用途与参数：获取期权数据，支持 --type/--symbol）
- [scripts/bond_data.py](scripts/bond_data.py)（用途与参数：获取债券数据，支持 --type/--symbol）
- [scripts/special_data.py](scripts/special_data.py)（用途与参数：获取龙虎榜/融资融券/北向资金等特色数据，支持 --type/--symbol/--start/--end）

### 参考文档：
- [股票数据文档](references/stock.md)（何时读取：需要查看股票相关API参数说明时）
- [期货数据文档](references/futures.md)（何时读取：需要查看期货相关API参数说明时）
- [基金数据文档](references/fund.md)（何时读取：需要查看基金相关API参数说明时）
- [宏观经济文档](references/macro.md)（何时读取：需要查看宏观数据API参数说明时）
- [AKShare官方文档](https://akshare.akfamily.xyz)（何时读取：需要查看最新API文档时）

## 注意事项
- AKShare 无需注册或 API Key，直接调用即可使用
- A股股票代码格式：纯数字代码（如 000001、600519），不带市场前缀
- 港股股票代码格式：纯数字代码（如 00700）
- 美股股票代码格式：英文代码（如 AAPL、TSLA）
- 数据列名：A股数据为中文列名，美股/港股数据为英文列名
- 建议定期更新AKShare版本：`pip install akshare --upgrade`
- 由于上游数据源变化，接口更新频繁，遇到错误时可先尝试更新版本
- 脚本返回 JSON 格式数据，智能体负责解析并转换为用户友好的展示
- 非Python用户可使用 AKTools HTTP API封装
- 数据仅供学术研究使用，不构成投资建议

## 快速参考
### 函数命名规则
```
{asset_type}_{market}_{data_type}_{data_source}
```
- **Asset type**: `stock`（股票）, `futures`（期货）, `fund`（基金）, `bond`（债券）, `forex`（外汇）, `option`（期权）, `macro`（宏观）, `index`（指数）
- **Market**: `zh`（中国）, `us`（美国）, `hk`（香港）, 或交易所代码
- **Data type**: `spot`（实时）, `hist`（历史）, `daily`（日线）, `minute`（分钟）
- **Data source**: `em`（东方财富）, `sina`（新浪财经）, 交易所缩写

### 复权类型
- `""` - 不复权
- `"qfq"` - 前复权
- `"hfq"` - 后复权

### 周期类型
- `"daily"` - 日线
- `"weekly"` - 周线
- `"monthly"` - 月线
- `"1"`, `"5"`, `"15"`, `"30"`, `"60"` - 分钟线
