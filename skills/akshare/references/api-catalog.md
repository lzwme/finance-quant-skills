# AKShare API 函数速查表

## 股票数据（A股/港股/美股）

- **实时行情**：`ak.stock_zh_a_spot_em()` - 全部A股实时行情
- **历史K线**：`ak.stock_zh_a_hist(symbol, period, start_date, end_date, adjust)`
- **分钟K线**：`ak.stock_zh_a_hist_min_em(symbol, period, start_date, end_date)`
- **个股信息**：`ak.stock_individual_info_em(symbol)` - 基本信息、市值、行业等
- **财务数据**：`ak.stock_fundamental(symbol)` - 基本面数据
- **估值指标**：`ak.stock_valuation(symbol)` - PE、PB等
- **港股数据**：`ak.stock_hk_spot_em()`, `ak.stock_hk_hist()`
- **美股数据**：`ak.stock_us_daily(symbol)`, `ak.stock_us_spot_em()`

## 期货数据

- **期货行情**：`ak.futures_zh_spot()` - 实时行情
- **期货K线**：`ak.get_futures_daily(start_date, end_date, market)` - 按交易所
- **库存数据**：`ak.futures_inventory_99(symbol)` - 期货库存

## 基金数据

- **ETF行情**：`ak.fund_etf_spot_em()` - ETF实时行情
- **ETF历史**：`ak.fund_etf_hist_em(symbol, period, start_date, end_date, adjust)`
- **开放式基金**：`ak.fund_open_fund_daily_em(symbol)` - 每日净值
- **基金评级**：`ak.fund_rating_all()` - 基金评级信息

## 期权数据

- **期权历史**：`ak.option_hist_dce(symbol)` - 交易所期权数据
- **ETF期权**：`ak.option_sse_spot_price(symbol)` - 上证50ETF期权

## 债券数据

- **可转债**：`ak.bond_zh_cov()` - 可转债列表
- **可转债K线**：`ak.bond_zh_hs_cov_daily(symbol)` - 可转债历史数据
- **债券报价**：`ak.bond_spot_quote()` - 中国债券现货报价

## 外汇贵金属

- **外汇行情**：`ak.forex_spot_em()` - 外汇实时行情
- **汇率数据**：`ak.forex_usd_cny()` - 美元兑人民币
- **贵金属**：`ak.metals_gold()` - 国际金价

## 指数数据

- **A股指数**：`ak.stock_zh_index_daily_em(symbol)` - 指数历史数据
- **指数成分**：`ak.index_stock_cons_csindex(symbol)` - 指数成分股

## 加密货币

- **币种列表**：`ak.crypto_binance_symbols()` - 币安交易对
- **实时价格**：`ak.crypto_binance_btc_usdt_spot()` - BTC/USDT价格
- **K线数据**：`ak.crypto_binance_btc_usdt_kline(period)` - 加密货币K线

## 宏观经济

- **中国GDP**：`ak.macro_china_gdp()`, `ak.macro_china_gdp_yearly()`
- **CPI数据**：`ak.macro_china_cpi_yearly()`, `ak.macro_china_cpi()`
- **PMI数据**：`ak.macro_china_pmi()`
- **美国数据**：`ak.macro_usa_non_farm()`, `ak.macro_usa_cpi_monthly()`

## 特色数据

- **龙虎榜**：`ak.stock_lhb_detail_em(start_date, end_date)` - 龙虎榜详情
- **融资融券**：`ak.stock_margin_sse(start_date, end_date)` - 融资融券数据
- **北向资金**：`ak.stock_hsgt_hist_em(symbol)` - 陆港通数据
- **股东数据**：`ak.stock_gdfx_top_10_em(symbol, date)` - 前十大股东
- **板块行情**：`ak.stock_board_industry_name_em()` - 行业板块
- **限售解禁**：`ak.stock_restricted_release_queue_em(symbol)` - 限售解禁
- **资金流向**：`ak.stock_market_fund_flow()` - 市场资金流向
