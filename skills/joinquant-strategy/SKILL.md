---
name: joinquant-strategy
description: 聚宽（JoinQuant）官网策略开发指南，涵盖回测、模拟交易、数据 API、交易函数、因子与技术指标。当用户编写聚宽策略、回测、模拟盘，排查模拟盘改代码不生效/替换代码，查询聚宽 API、get_price/order/run_daily、Alpha 因子、技术指标，或提及 joinquant、聚宽、jqdata 策略时使用。本地数据获取请用 jqdatasdk 技能。
metadata: {"openclaw":{"emoji":"📚","requires":{"bins":["python"]}}}
---

# 聚宽策略开发

基于本目录离线文档，为聚宽官网（回测 / 模拟 / 研究）编写 Python 策略。回答 API 问题时**必须先查阅本地文档**，不得凭记忆编造函数签名或参数。查不到时明确说「本地文档未覆盖」，附官网链接 <https://www.joinquant.com/help/api/help>，不要推测参数默认值。

> **与 jqdatasdk 的区别**：`jqdata` 在官网策略环境使用；`jqdatasdk` 是本地 Python 库，API 略有不同，且不能在官网回测/模拟/研究中使用。

## 文档查阅流程

1. **确定问题类型**，按下表定位文件（完整文件清单见 [reference.md](reference.md)）
2. **用 Grep/Read 搜索**目标函数名或中文关键词（如 `get_price`、`order_target`、`市盈率`）
3. **交叉验证**：API 行为查 `api.md`，字段/表结构查 `data/*.md`，踩坑查 `faq.md`
4. **给出答案时**引用文档中的调用方法、参数、返回值与示例代码

| 意图 | 首读 | 深入 |
|------|------|------|
| 编写策略 / 需要完整骨架 | `strategy_template.md` | `api.md`「策略程序架构」 |
| 查行情与历史数据 | `api.md`「数据获取函数」 | `data/Stock.md` |
| 下单 / 持仓 / 账户对象 | `api.md`「交易函数」「对象」 | — |
| 财务 / 估值选股 | `data/Stock.md` | `api.md` get_fundamentals |
| 指数成分股 | `data/index.md` | `api.md` get_index_stocks |
| 行业 / 概念轮动 | `data/plateData.md` | `api.md` get_industry_stocks |
| 期货策略 | `data/Future.md` | `api.md`「期货策略专用函数」 |
| 期权策略 | `data/Option.md` | `api.md` 期权相关 |
| 基金 / ETF | `data/fund.md` | `data/OTCfund.md` |
| 可转债 | `data/bond.md` | — |
| 宏观数据 | `data/macroData.md` | — |
| 技术指标 | `data/technicalanalysis.md` | `jqlib.technical_analysis` |
| Alpha 因子 | `data/Alpha101.md`、`data/Alpha191.md` | — |
| 自定义因子 | `factor.md` | `data/Alpha101.md` |
| 因子看板数据 | `data/factor_values.md` | `factor.md` |
| 融资融券 | `data/Stock.md` 融资融券章节 | `api.md` 融资融券专用函数 |
| 模拟盘改代码 / 参数不生效 | `simulation.md`（先读再答） | `faq.md`、`api.md`「模拟盘注意事项」 |
| 报错 / 数据疑问 | `faq.md` | `api.md`「注意事项」 |

### 交付前自检

- [ ] 每个参数、返回值都能在 `api.md` 或 `data/*.md` 中找到出处
- [ ] 标明适用环境（回测 / 模拟 / 研究）；标 ♠ 的 API 仅回测/模拟可用，研究模块不可调用
- [ ] 示例代码含必要 import（`from jqdata import *`），可直接粘贴运行
- [ ] 选股与取数检查是否传了历史时点的 `date=`，确认未引入未来数据

## 策略骨架

最小可运行结构：

```py
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

完整可运行骨架（配置集中、盘前选池、先卖后买、热更新入口）见 [strategy_template.md](strategy_template.md)；模拟盘热更新机制见 [simulation.md](simulation.md)。

### 生命周期函数

| 函数 | 说明 |
|------|------|
| `initialize(context)` | 全局初始化，仅运行一次；用 `g` 存全局变量 |
| `run_daily/weekly/monthly(func, ...)` | 定时任务；`func` 必须是**全局函数**，不能是类方法 |
| `handle_data(context, data)` | 按回测频率驱动；**不建议与 run_daily 混用** |
| `before_trading_start` | 开盘前（9:00） |
| `after_trading_end` | 收盘后（15:30） |
| `after_code_changed(context)` | 模拟盘**替换代码后**触发；此时 `initialize` 不会重跑 |
| `process_initialize(context)` | 每次进程重启都执行；重建不可序列化对象（如 `query`） |

`jqdata` 模块在研究与回测环境均可使用。

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

```py
get_price(security, start_date, end_date, frequency='daily', fields=None, fq='pre')
attribute_history(security, count, unit, fields)  # 回测环境，不含当天
history(count, unit, field, security_list, df=True)
get_bars(security, count, unit, fields, include_now=True)
```

### 标的池与板块

```py
get_all_securities(types=['stock'], date=None)   # date 防未来函数
get_index_stocks('000300.XSHG', date=None)
get_industry_stocks('C15', date=None)
get_concept_stocks('GN036', date=None)
set_universe([...])  # 设置后 history 可不传 security_list
```

### 财务数据（SQL 查询）

```py
from jqdata import *
q = query(valuation).filter(valuation.code == '000001.XSHE')
df = get_fundamentals(q, date='2015-10-15')

# 或 run_query（单次最多 4000 行，不可连表）
df = finance.run_query(query(finance.STK_XXX).filter(...).limit(4000))
```

### 交易

```py
order(security, amount)              # 按股数，正买负卖
order_value(security, value)       # 按金额
order_target(security, amount)       # 调到目标股数
order_target_value(security, value)  # 调到目标市值
order_target_percent(security, percent)  # 调到目标仓位比例
```

A 股买入数量须为 100 整数倍（科创板 200 股起）；卖光持仓时不受限。每日最多 10000 笔订单。

### 技术指标

```py
from jqlib.technical_analysis import *
# check_date 策略中建议用 context.current_dt，避免盘中取当日收盘指标产生未来数据
result = MACD(security_list, check_date=context.current_dt, SHORT=12, LONG=26, MID=9)
```

### 自定义因子

```py
from jqfactor import Factor, calc_factors

class MyFactor(Factor):
    name = 'my_factor'
    max_window = 5
    dependencies = ['close']
    def calc(self, data):
        return data['close'].mean()

factors = calc_factors(securities, [MyFactor()], start_date, end_date)
```

详见 `factor.md` 与 `data/Alpha101.md`、`data/Alpha191.md`。

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

### 模拟盘：改了代码不生效

模拟盘持有独立的代码副本、`initialize` 不会重跑，回测里正常的改动常在模拟盘失效。回答此类问题前先读 [simulation.md](simulation.md)：内含断点定位、`apply_settings` 迁移模板、诊断模板与误判清单。

### 数据查询限制

- `run_query` / `get_fundamentals` 单次最多返回 **4000 行**
- `run_query` **不支持连表查询**
- 默认行情为**前复权**；`fq=None` 为不复权

### 环境与产品区分

| 产品 | 使用场景 |
|------|----------|
| `jqdata`（官网） | 回测、模拟、研究 |
| `jqdatasdk`（本地） | 本地量化研究，**不能**在官网策略中 import |

## 策略示例

完整示例见 `api.md` 末尾「策略示例」：均线策略、多股票持仓、追涨策略、万圣节效应等。

## 附加资源

- 完整文件清单、`api.md` 章节索引、文档同步脚本用法：[reference.md](reference.md)
- 可直接运行的策略骨架：[strategy_template.md](strategy_template.md)
- 模拟盘热更新与排查：[simulation.md](simulation.md)

> `api.md` / `faq.md` / `data/*.md` 由脚本从官网同步，切勿手改；`reference.md`、`simulation.md`、`strategy_template.md` 手工维护。
