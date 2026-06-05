# 聚宽文档索引

本目录文档从 [聚宽官方 API 文档](https://www.joinquant.com/help/api/help) 离线同步，供策略开发时精确查阅。

## 根目录文档

| 文件 | 内容 | 何时查阅 |
|------|------|----------|
| [api.md](api.md) | 策略 API 全文：initialize、run_daily、数据获取、交易、对象、示例 | 查任意官网 API 签名、参数、返回值 |
| [faq.md](faq.md) | 常见问题：数据更新频率、代码后缀、复权、财务差异、期货主力合约 | 数据异常、环境差异、概念澄清 |
| [fator.md](fator.md) | 因子分析：Factor 定义、calc_factors、因子看板、多因子框架 | 自定义因子、因子回测分析 |

## 数据字典（data/）

| 文件 | 内容 | 关键 API / 表 |
|------|------|---------------|
| [data/Stock.md](data/Stock.md) | 股票数据：概况、行情、财务、估值、融资融券、龙虎榜等 | `get_security_info`、`get_price`、`get_fundamentals`、`valuation`、`indicator`、`balance` |
| [data/index.md](data/index.md) | 沪深指数：成分股、权重、行情字段 | `get_index_stocks`、`get_index_weights`、`get_price` |
| [data/plateData.md](data/plateData.md) | 行业/概念板块代码列表 | `get_industry_stocks`、`get_concept_stocks`、`get_industries` |
| [data/Future.md](data/Future.md) | 期货：合约、行情、主力连续、交割 | `get_price`、`get_dominant_future`、`normalize_code` |
| [data/Option.md](data/Option.md) | 期权：合约资料、行情、希腊字母 | `get_price`、期权专用表 |
| [data/fund.md](data/fund.md) | 场内基金：ETF、LOF、分级基金 | `get_price`、`get_extras` |
| [data/OTCfund.md](data/OTCfund.md) | 场外基金：净值、持仓 | `finance.run_query` |
| [data/bond.md](data/bond.md) | 可转债：行情、转股、赎回 | `get_price`、可转债相关表 |
| [data/macroData.md](data/macroData.md) | 宏观经济指标 | `macro.run_query` |
| [data/Public.md](data/Public.md) | 公共数据：新闻联播文本等 | `finance.CCTV_NEWS` |
| [data/technicalanalysis.md](data/technicalanalysis.md) | 技术分析指标（MACD、KDJ、BOLL 等） | `jqlib.technical_analysis.*` |
| [data/Alpha101.md](data/Alpha101.md) | WorldQuant 101 Alphas 因子 | `jqlib.alpha101.*` |
| [data/Alpha191.md](data/Alpha191.md) | 短周期价量 191 Alphas | `jqlib.alpha191.*` |
| [data/factor_values.md](data/factor_values.md) | 因子看板：风险模型、基本面、量价因子列表 | `get_factor_values`、`get_factor_kanban_values` |

## api.md 主要章节

便于 Grep 定位：

| 章节 | 内容 |
|------|------|
| 开始写策略 | 最小示例、均线策略模板 |
| 策略引擎介绍 | 运行频率、撮合、滑点、税费、回测/模拟差异 |
| 策略程序架构 ♠ | initialize、run_daily/weekly/monthly、handle_data |
| 策略设置函数 | set_benchmark、set_order_cost、set_slippage、set_option |
| 数据获取函数 | get_price、history、get_fundamentals、get_index_stocks 等 |
| 交易函数 | order、order_value、order_target、order_target_percent |
| 对象 ♠ | Context、Portfolio、Position、Order |
| 融资融券专用函数 | margincash_open/close 等 |
| 期货策略专用函数 | 换月、交割相关 |
| 策略示例 | 均线、多股、追涨、万圣节效应 |

## 搜索技巧

```bash
# 在 api.md 中搜索函数
rg "def get_price|get_price\(" skills/joinquant-docs/api.md

# 在数据字典中搜索字段
rg "market_cap|市盈率" skills/joinquant-docs/data/Stock.md

# 搜索技术指标
rg "^### MACD" skills/joinquant-docs/data/technicalanalysis.md
```

## 原始 HTML 缓存

`data/local/*.html` 为官网原始 HTML，仅在需要对比转换质量时参考。日常查 API 请读 `.md` 文件。
