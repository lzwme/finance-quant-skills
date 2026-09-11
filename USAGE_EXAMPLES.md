# Skills 使用示例

本项目共包含 **13 个 Skills**，按功能分为三大类：**数据获取**、**回测框架**、**策略开发与文档**。安装后，直接向 AI 助手描述需求即可自动触发对应 Skill。

---

## 📈 数据获取

### 1. 获取 A 股历史 K 线（BaoStock — 免费、无需注册）

> 帮我用 baostock 获取贵州茅台 2025 年全年的日 K 线数据，前复权

- **适用场景**：A 股历史行情、财务报表、指数成分股、交易日历
- **关键参数**：代码格式 `sh.600519` / `sz.000001`，支持 `--adjust 2`（前复权）

### 2. 获取全品类金融数据（AKShare — 免费、无需注册）

> 帮我用 akshare 查看沪深 300 ETF（510300）的实时行情
> 帮我用 akshare 获取中国 2025 年 GDP 宏观数据
> 帮我用 akshare 查询 BTC/USDT 的加密货币价格

- **适用场景**：股票/期货/期权/基金/外汇/债券/加密货币/宏观经济
- **关键参数**：`python scripts/stock_data.py --type hist --symbol 600519 --start 20250101`

### 3. 自然语言选股查询（PyWenCai — 同花顺问财）

> 帮我用问财查询"市盈率小于 20 且 ROE 大于 15% 的股票"

- **适用场景**：用中文自然语言筛选 A 股/指数/基金/港股/可转债
- **前置要求**：需配置问财 Cookie（环境变量 `WENCAI_COOKIE`）

### 4. 通达信量化数据（TdxQuant — 需客户端）

> 帮我用通达信查看贵州茅台的实时行情和 K 线数据
> 帮我用通达信执行 MACD 公式，参数 12,26,9

- **适用场景**：A 股行情快照、K 线、专业财务、板块成分股、新股/可转债、通达信公式执行、交易下单
- **前置要求**：需安装并启动通达信金融终端（支持 TQ 策略功能）
- **关键参数**：代码格式 `600519.SH`，财务字段如 `--fields fn193,fn197`

### 5. MiniQMT 行情与交易（XtQuant — 需客户端）

> 帮我用 miniqmt 订阅贵州茅台的实时行情
> 帮我用 miniqmt 查询持仓并下单买入 100 股平安银行

- **适用场景**：实时行情订阅、K 线数据、财务数据、股票/期货/期权交易下单及撤单
- **前置要求**：需安装并启动迅投 MiniQMT 客户端
- **关键参数**：代码格式 `600519.SH`，周期 `1d`/`1m`/`tick`

### 6. 聚宽数据（JQData — 需 Token）

> 帮我用聚宽获取招商银行 2025 年的财务指标和估值因子

- **适用场景**：本地 Python 环境获取 A 股行情、财务指标、因子数据（估值/动量/质量等）
- **前置要求**：需注册聚宽账号并配置 Token（环境变量 `JQDATA_TOKEN`）
- **关键参数**：代码格式 `600036.XSHG`（上海）/ `000001.XSHE`（深圳）
- **与 joinquant-strategy 的区别**：`jqdatasdk` 用于财经数据拉取；`joinquant-strategy` 用于官网策略编写与 API 查阅

### 7. Tushare 数据（需 Token）

> 帮我用 tushare 获取上证指数 2025 上半年的日线数据和宏观数据

- **适用场景**：A 股行情、财务报表（利润表/资产负债表/现金流）、指数、Shibor 等宏观数据
- **前置要求**：需注册 Tushare Pro 并配置 Token（环境变量 `TUSHARE_TOKEN`）
- **关键参数**：代码格式 `000001.SZ` / `600036.SH`

---

## 🔬 策略回测框架

### 8. Backtrader 回测（开源、纯 Python）

> 帮我用 backtrader 写一个双均线交叉策略，回测贵州茅台 2025 年数据，计算夏普比率和最大回撤

- **适用场景**：事件驱动回测、内置 100+ 技术指标、参数优化（网格搜索）、绩效分析
- **核心概念**：Cerebro（引擎）、Strategy（策略）、Analyzer（分析器）、指标在 `__init__` 中定义，交易逻辑在 `next` 中编写
- **组合使用**：可配合 baostock/akshare Skill 先获取数据，再回测

### 9. RQAlpha 回测（米筐开源、模块化）

> 帮我用 rqalpha 写一个期货双均线 CTA 策略，回测沪深 300 期货 IF2401

- **适用场景**：A 股和期货回测、Mod 插件系统扩展、内置数据包 `download-bundle`
- **核心概念**：`init`（初始化）、`handle_bar`（K 线触发）、scheduler 定时调度
- **特色**：支持代码格式 `IF2401.CCFX`，期货专用下单函数 `buy_open` / `sell_close`

---

## 🛠 策略开发与文档

### 10. AKQuant 策略开发框架

> 帮我用 akquant 写一个横截面动量轮动策略，在沪深 300 成分股中每月调仓

- **适用场景**：量化策略开发（事件驱动）、风控规则配置、参数优化（Walk-Forward）、横截面策略
- **核心概念**：Strategy 基类、`on_bar`/`on_timer` 回调、RiskConfig 风控
- **环境要求**：Python 3.10+ / Windows，推荐使用 `uv` 管理项目环境

### 11. QMT 策略开发文档

> 帮我查看 QMT 的交易 API 参考文档
> 帮我用 QMT 写一个 handlebar 驱动的双均线策略

- **适用场景**：查阅 QMT（迅投极速策略交易系统）完整开发指南、API 参考、代码示例
- **核心内容**：系统概述、回测/实盘指南、行情/交易 API、数据字典、聚宽迁移指南
- **执行机制**：handlebar（K 线驱动）、subscribe（事件驱动）、run_time（定时触发）

### 12. 聚宽策略开发文档

> 帮我用聚宽写一个沪深 300 成分股均线轮动策略
> 帮我查聚宽 get_fundamentals 怎么按市盈率筛选股票

- **适用场景**：聚宽官网策略编写、回测、模拟交易、API 与数据字典查阅
- **核心内容**：策略骨架（initialize/run_daily）、交易函数、财务查询、行业/概念选股、Alpha 因子、技术指标
- **文档来源**：离线同步聚宽官方 API 文档（`api.md`、`data/*.md`、`faq.md` 等）
- **关键参数**：代码格式 `600519.XSHG` / `000001.XSHE`，建议 `set_option('use_real_price', True)`

### 13. 机构级投研报告生成（Equity Researcher）

> 帮我用 equity-researcher 分析贵州茅台，出一份投资速览
> 帮我看看比亚迪的深度研报

- **适用场景**：A 股/港股/美股上市公司的机构级投研报告生成、投资逻辑梳理、财务建模
- **输出模式**：
  - **投资速览（Tear Sheet）**：3-5 页，含公司概览、核心财务指标、估值倍数、投资逻辑与风险因素
  - **深度研报（Equity Report）**：≥25 页，含行业分析、产业链图谱、三表模型、DCF 估值、情景分析与敏感性测试
- **来源**：
  - 同步自 Kimi 官方技能，详情见 https://www.kimi.com/extensions?tab=skill
  - https://github.com/haomingz/kimi-skills/blob/master/skills/equity-researcher/

---

## 💡 典型组合使用场景

| 场景 | 推荐 Skills 搭配 |
|------|----------------|
| **数据获取 + 回测研究** | baostock / akshare → backtrader / rqalpha |
| **数据获取 + QMT 实盘** | baostock / akshare → qmt-strategy（策略开发）→ miniqmt（实盘交易） |
| **聚宽策略开发** | joinquant-strategy（API/策略编写）→ jqdatasdk（本地数据验证） |
| **聚宽迁移至 QMT** | joinquant-strategy（理解聚宽 API）→ qmt-strategy（joinquant-migration 迁移指南） |
| **选股 + 回测验证** | pywencai（筛选标的）→ backtrader（回测策略） |
| **通达信公式 + 实盘交易** | tdxquant（公式计算/选股）→ miniqmt / QMT（下单） |
| **全品类数据采集** | akshare（股票/期货/加密货币/宏观） |
| **投研报告 + 数据验证** | equity-researcher（生成研报）→ baostock / akshare（数据验证） |
