---
name: joinquant-docs
description: 聚宽（JoinQuant）官网策略开发指南，涵盖回测、模拟交易、数据 API、交易函数、因子与技术指标。当用户编写聚宽策略、回测、模拟盘、查询聚宽 API、get_price/order/run_daily、Alpha 因子、技术指标，或提及 joinquant、聚宽、jqdata 策略时使用。本地数据获取请用 jqdatasdk 技能。
---

# 聚宽策略开发

基于本目录离线文档，为聚宽官网（回测 / 模拟 / 研究）编写 Python 策略。回答 API 问题时**必须先查阅本地文档**，不得凭记忆编造函数签名或参数。

> **与 jqdatasdk 的区别**：`jqdata` 在官网策略环境使用；`jqdatasdk` 是本地 Python 库，API 略有不同，且不能在官网回测/模拟/研究中使用。

## 文档查阅流程

1. **确定问题类型**，按 [reference.md](reference.md) 定位文件
2. **用 Grep/Read 搜索**目标函数名或中文关键词（如 `get_price`、`order_target`、`市盈率`）
3. **交叉验证**：API 行为查 `api.md`，字段/表结构查 `data/*.md`，踩坑查 `faq.md`
4. **给出答案时**引用文档中的调用方法、参数、返回值与示例代码

```
需要写策略框架？     → api.md「开始写策略」「策略程序架构」
需要查数据 API？      → api.md「数据获取函数」+ data/ 对应品种文档
需要下单/持仓？      → api.md「交易函数」「对象」
需要财务/估值数据？  → data/Stock.md（run_query + valuation/fundamentals 表）
需要行业/概念选股？  → data/plateData.md + api.md get_industry_stocks 等
需要技术指标？       → data/technicalanalysis.md（from jqlib.technical_analysis import *）
需要 Alpha 因子？    → data/Alpha101.md、data/Alpha191.md
需要自定义因子？     → fator.md（jqfactor.Factor、calc_factors）
需要因子看板数据？   → data/factor_values.md
```

## 策略骨架

最小可运行结构：

```python
# 导入聚宽函数库
import jqdata

def initialize(context):
    g.security = '000001.XSHE'
    set_benchmark('000300.XSHG')
    set_option('use_real_price', True)  # 开启动态复权（真实价格），建议开启
    run_daily(trade, time='open')       # 或 time='every_bar' / '9:30'

def trade(context):
    security = g.security
    close_data = attribute_history(security, 5, '1d', ['close'])
    MA5 = close_data['close'].mean()
    current_price = close_data['close'][-1]
    cash = context.portfolio.available_cash

    if current_price > 1.01 * MA5:
        order_value(security, cash)
    elif current_price < MA5 and context.portfolio.positions[security].closeable_amount > 0:
        order_target(security, 0)
```

### 生命周期函数

| 函数 | 说明 |
|------|------|
| `initialize(context)` | 全局初始化，仅运行一次；用 `g` 存全局变量 |
| `run_daily/weekly/monthly(func, ...)` | 定时任务；`func` 必须是**全局函数**，不能是类方法 |
| `handle_data(context, data)` | 按回测频率驱动；**不建议与 run_daily 混用** |
| `before_trading_start` | 开盘前（9:00） |
| `after_trading_end` | 收盘后（15:30） |

带 ♠ 标识的 API 仅支持**回测/模拟**，不能在研究模块调用。`jqdata` 模块在研究与回测环境均可使用。

## 证券代码规范

| 市场 | 后缀 | 示例 |
|------|------|------|
| 上海证券交易所 | `.XSHG` | `600519.XSHG` |
| 深圳证券交易所 | `.XSHE` | `000001.XSHE` |
| 中金所 | `.CCFX` | `IC9999.CCFX` |
| 大商所 | `.XDCE` | `A9999.XDCE` |
| 上期所 | `.XSGE` | `AU9999.XSGE` |
| 郑商所 | `.XZCE` | `CY8888.XZCE` |
| 场外基金 | `.OF` | `519671.OF` |

期货策略需将 `run_daily` 的 `reference_security` 设为对应主力合约（如 `IF9999.CCFX`），以匹配夜盘开盘时间。

## 常用 API 速查

### 行情与历史

```python
get_price(security, start_date, end_date, frequency='daily', fields=None, fq='pre')
attribute_history(security, count, unit, fields)  # 回测环境，不含当天
history(count, unit, field, security_list, df=True)
get_bars(security, count, unit, fields, include_now=True)
```

### 标的池与板块

```python
get_all_securities(types=['stock'], date=None)   # date 防未来函数
get_index_stocks('000300.XSHG', date=None)
get_industry_stocks('C15', date=None)
get_concept_stocks('GN036', date=None)
set_universe([...])  # 设置后 history 可不传 security_list
```

### 财务数据（SQL 查询）

```python
from jqdata import *
q = query(valuation).filter(valuation.code == '000001.XSHE')
df = get_fundamentals(q, date='2015-10-15')

# 或 run_query（单次最多 4000 行，不可连表）
df = finance.run_query(query(finance.STK_XXX).filter(...).limit(4000))
```

### 交易

```python
order(security, amount)              # 按股数，正买负卖
order_value(security, value)       # 按金额
order_target(security, amount)       # 调到目标股数
order_target_value(security, value)  # 调到目标市值
order_target_percent(security, percent)  # 调到目标仓位比例
```

A 股买入数量须为 100 整数倍（科创板 200 起）；卖光持仓时不受限。每日最多 10000 笔订单。

### 技术指标

```python
from jqlib.technical_analysis import *
# check_date 策略中建议用 context.current_dt，避免盘中取当日收盘指标产生未来数据
result = MACD(security_list, check_date=context.current_dt, SHORT=12, LONG=26, MID=9)
```

### 自定义因子

```python
from jqfactor import Factor, calc_factors

class MyFactor(Factor):
    name = 'my_factor'
    max_window = 5
    dependencies = ['close']
    def calc(self, data):
        return data['close'].mean()

factors = calc_factors(securities, [MyFactor()], start_date, end_date)
```

详见 `fator.md` 与 `data/Alpha101.md`、`data/Alpha191.md`。

## 关键注意事项

### 防止未来函数

- `get_all_securities(date=...)`、`get_index_stocks(..., date=...)` 等必须传入**历史时点**的 `date`，不能用未来日期
- `history` / `attribute_history` 取天数据时**不包含当天**；要当天数据需取分钟级
- 技术指标 `check_date` 只精确到日期时返回收盘值，盘中调用当天会产生未来数据
- 财务数据默认按公告日期处理，注意 `get_fundamentals` 的 `date` 参数含义

### 运行频率

- 优先使用 `run_daily`，避免与 `handle_data` 混用
- `run_daily(func, time='every_bar')` 频率与回测设置一致
- `run_weekly/monthly` 的 `force=False` 可避免晚注册时的就近执行

### 数据查询限制

- `run_query` / `get_fundamentals` 单次最多返回 **4000 行**
- `run_query` **不支持连表查询**
- 默认行情为**前复权**；`fq=None` 为不复权

### 环境与产品区分

| 产品 | 使用场景 |
|------|----------|
| `jqdata`（官网） | 回测、模拟、研究 |
| `jqdatasdk`（本地） | 本地量化研究，**不能**在官网策略中 import |

## 按场景选文档

| 场景 | 首先阅读 | 深入查阅 |
|------|----------|----------|
| 新手写第一个策略 | `api.md`「开始写策略」 | `api.md`「策略程序架构」 |
| 股票选股 + 财务 | `data/Stock.md` | `api.md` get_fundamentals |
| 指数成分股策略 | `data/index.md` | `api.md` get_index_stocks |
| 行业/概念轮动 | `data/plateData.md` | `api.md` get_industry_stocks |
| 期货策略 | `data/Future.md` | `api.md`「期货策略专用函数」 |
| 期权策略 | `data/Option.md` | `api.md` 期权相关 |
| 基金/ETF | `data/fund.md` | `data/OTCfund.md` |
| 可转债 | `data/bond.md` | — |
| 宏观数据 | `data/macroData.md` | — |
| 技术分析指标 | `data/technicalanalysis.md` | — |
| 因子选股 | `fator.md` + `data/factor_values.md` | `data/Alpha101.md` |
| 融资融券 | `data/Stock.md` 融资融券章节 | `api.md` 融资融券专用函数 |
| 报错/数据疑问 | `faq.md` | `api.md`「注意事项」 |

## 策略示例

完整示例见 `api.md` 末尾「策略示例」：均线策略、多股票持仓、追涨策略、万圣节效应等。

## 文档更新

本地数据字典由脚本从官网同步：

```bash
bun scripts/get-joinquant-docs.ts
# 强制覆盖已有 md：FORCE_UPDATE=1 bun scripts/get-joinquant-docs.ts
```

## 附加资源

- 完整文档索引：[reference.md](reference.md)
- 平台 API 全文：[api.md](api.md)
- 常见问题：[faq.md](faq.md)
- 因子分析：[fator.md](fator.md)
