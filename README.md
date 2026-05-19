# Finance Quant Skills

一个面向金融量化交易领域的 Claude Skills 技能维护仓库，基于 [Agent Skills](https://agentskills.io) 标准构建。

## 目录结构

本仓库维护金融量化交易相关的 Skills，涵盖量化策略开发、金融数据分析、交易框架文档查询等场景。每个 Skill 位于独立文件夹中，包含 `SKILL.md` 指令等文件。

```
quant-finance-skills/
├── skills/              # 量化交易相关的 Skills 集合
│   ├── akquant/         # AKQuant 框架量化策略开发（事件驱动、风控与优化）
│   ├── akshare-docs/    # AKShare 开源金融数据接口（股票/期货/基金/加密货币等）
│   ├── backtrader/      # Backtrader 开源量化回测框架
│   ├── baostock/        # BaoStock A股数据平台（免费行情、K线、财务数据）
│   ├── jqdatasdk/       # 聚宽数据接口（A股行情、财务、因子数据）
│   ├── miniqmt/         # MiniQMT 迅投量化交易接口（XtQuant，支持交易下单）
│   ├── pywencai/        # 同花顺问财数据查询（中文自然语言查询）
│   ├── qmt-docs/        # QMT 策略开发指南与 API 参考文档
│   ├── rqalpha/         # RQAlpha 米筐开源回测框架（A股/期货）
│   ├── tdxquant/        # 通达信量化数据获取（行情/K线/财务/板块/公式执行）
│   └── tushare/         # Tushare 数据接口（A股行情、财务、宏观数据）
├── template/            # Skill 模板
└── .claude-plugin/      # Claude Code 插件配置
```

## Skills 安装

请根据你的使用场景选择合适的安装方式：

### 方式一：让 AI Agent 帮助安装

以对话的形式告诉 Agent 智能体，如 `OpenClaw`：

> 帮我安装这个 skills 仓库中的所有技能: https://github.com/lzwme/quant-finance-skills
>
> 帮我安装这个 skills 仓库中的 qmt-docs 技能: https://github.com/lzwme/quant-finance-skills

### 方式二：在 Claude Code 中安装使用

将该仓库注册为 Claude Code Plugin marketplace：

```bash
/plugin marketplace add lzwme/quant-finance-skills
```

然后安装指定的 Skills 插件：

```bash
/plugin install quant-skills@finance-quant-skills
/plugin install quant-docs@finance-quant-skills
```

也可以通过界面操作：选择 `Browse and install plugins` → `finance-quant-skills` → 选择插件 → `Install now`。

安装后，直接描述需求即可触发对应 Skill，例如："使用 QMT 文档 Skill 查询如何通过 Python 调用交易接口"。

### 方式三（推荐）：使用 `npx skills` 工具为智能体安装技能

```bash
# 查看帮助
npx skills --help

# 查看当前项目下已安装的技能
npx skills list
# 查看已全局安装的技能
npx skills list -g
# 更新已安装的技能
npx skills update

# 安装当前仓库技能
npx skills add lzwme/quant-finance-skills
```

### 安装技巧：以软连接形式安装支持多编程智能体工具

不同编程智能体的 skills 目录规范有所不同。当我们会在多个编程工具之间切换使用时，则需要配置多个 skills 目录。

通过软连接和 `.gitignore` 配置，可以将 skills 目录链接到多个编程工具的 skills 目录中：

```bash
# 假若在 agents/skills 中维护 skills
# 创建 .cluade、.cursor 的 skills 软连接

# macOS/Linux 下
ln -s agents/skills .cluade/skills
ln -s agents/skills .cursor/skills

# windows powershell 下（其中的 Junction 也可换为 SymbolicLink，但需管理员权限执行）
New-Item -ItemType Junction -Path .cluade/skills -Target <绝对路径>/agents/skills
New-Item -ItemType Junction -Path .cursor/skills -Target <绝对路径>/agents/skills
```

## Skills 使用示例

本项目共包含 **11 个 Skills**，按功能分为三大类：**数据获取**、**回测框架**、**策略开发与文档**。安装后，直接向 AI 助手描述需求即可自动触发对应 Skill。

### 📊 数据获取

#### 1. 获取 A 股历史 K 线（BaoStock — 免费、无需注册）

> 帮我用 baostock 获取贵州茅台 2024 年全年的日 K 线数据，前复权

- **适用场景**：A 股历史行情、财务报表、指数成分股、交易日历
- **关键参数**：代码格式 `sh.600519` / `sz.000001`，支持 `--adjust 2`（前复权）

#### 2. 获取全品类金融数据（AKShare — 免费、无需注册）

> 帮我用 akshare 查看沪深 300 ETF（510300）的实时行情
> 帮我用 akshare 获取中国 2024 年 GDP 宏观数据
> 帮我用 akshare 查询 BTC/USDT 的加密货币价格

- **适用场景**：股票/期货/期权/基金/外汇/债券/加密货币/宏观经济
- **关键参数**：`python scripts/stock_data.py --type hist --symbol 600519 --start 20240101`

#### 3. 自然语言选股查询（PyWenCai — 同花顺问财）

> 帮我用问财查询"市盈率小于 20 且 ROE 大于 15% 的股票"

- **适用场景**：用中文自然语言筛选 A 股/指数/基金/港股/可转债
- **前置要求**：需配置问财 Cookie（环境变量 `WENCAI_COOKIE`）

#### 4. 通达信量化数据（TdxQuant — 需客户端）

> 帮我用通达信查看贵州茅台的实时行情和 K 线数据
> 帮我用通达信执行 MACD 公式，参数 12,26,9

- **适用场景**：A 股行情快照、K 线、专业财务、板块成分股、新股/可转债、通达信公式执行、交易下单
- **前置要求**：需安装并启动通达信金融终端（支持 TQ 策略功能）
- **关键参数**：代码格式 `600519.SH`，财务字段如 `--fields fn193,fn197`

#### 5. MiniQMT 行情与交易（XtQuant — 需客户端）

> 帮我用 miniqmt 订阅贵州茅台的实时行情
> 帮我用 miniqmt 查询持仓并下单买入 100 股平安银行

- **适用场景**：实时行情订阅、K 线数据、财务数据、股票/期货/期权交易下单及撤单
- **前置要求**：需安装并启动迅投 MiniQMT 客户端
- **关键参数**：代码格式 `600519.SH`，周期 `1d`/`1m`/`tick`

#### 6. 聚宽数据（JQData — 需 Token）

> 帮我用聚宽获取招商银行 2024 年的财务指标和估值因子

- **适用场景**：A 股行情、财务指标、因子数据（估值/动量/质量等）
- **前置要求**：需注册聚宽账号并配置 Token（环境变量 `JQDATA_TOKEN`）
- **关键参数**：代码格式 `600036.XSHG`（上海）/ `000001.XSHE`（深圳）

#### 7. Tushare 数据（需 Token）

> 帮我用 tushare 获取上证指数 2024 上半年的日线数据和宏观数据

- **适用场景**：A 股行情、财务报表（利润表/资产负债表/现金流）、指数、Shibor 等宏观数据
- **前置要求**：需注册 Tushare Pro 并配置 Token（环境变量 `TUSHARE_TOKEN`）
- **关键参数**：代码格式 `000001.SZ` / `600036.SH`

---

### 🔬 策略回测框架

#### 8. Backtrader 回测（开源、纯 Python）

> 帮我用 backtrader 写一个双均线交叉策略，回测贵州茅台 2024 年数据，计算夏普比率和最大回撤

- **适用场景**：事件驱动回测、内置 100+ 技术指标、参数优化（网格搜索）、绩效分析
- **核心概念**：Cerebro（引擎）、Strategy（策略）、Analyzer（分析器）、指标在 `__init__` 中定义，交易逻辑在 `next` 中编写
- **组合使用**：可配合 baostock/akshare Skill 先获取数据，再回测

#### 9. RQAlpha 回测（米筐开源、模块化）

> 帮我用 rqalpha 写一个期货双均线 CTA 策略，回测沪深 300 期货 IF2401

- **适用场景**：A 股和期货回测、Mod 插件系统扩展、内置数据包 `download-bundle`
- **核心概念**：`init`（初始化）、`handle_bar`（K 线触发）、scheduler 定时调度
- **特色**：支持代码格式 `IF2401.CCFX`，期货专用下单函数 `buy_open` / `sell_close`

---

### 🛠 策略开发与文档

#### 10. AKQuant 策略开发框架

> 帮我用 akquant 写一个横截面动量轮动策略，在沪深 300 成分股中每月调仓

- **适用场景**：量化策略开发（事件驱动）、风控规则配置、参数优化（Walk-Forward）、横截面策略
- **核心概念**：Strategy 基类、`on_bar`/`on_timer` 回调、RiskConfig 风控
- **环境要求**：Python 3.10+ / Windows，推荐使用 `uv` 管理项目环境

#### 11. QMT 策略开发文档

> 帮我查看 QMT 的交易 API 参考文档
> 帮我用 QMT 写一个 handlebar 驱动的双均线策略

- **适用场景**：查阅 QMT（迅投极速策略交易系统）完整开发指南、API 参考、代码示例
- **核心内容**：系统概述、回测/实盘指南、行情/交易 API、数据字典、聚宽迁移指南
- **执行机制**：handlebar（K 线驱动）、subscribe（事件驱动）、run_time（定时触发）

---

### 💡 典型组合使用场景

| 场景 | 推荐 Skills 搭配 |
|------|----------------|
| **数据获取 + 回测研究** | baostock / akshare → backtrader / rqalpha |
| **数据获取 + QMT 实盘** | baostock / akshare → qmt-docs（策略开发）→ miniqmt（实盘交易） |
| **选股 + 回测验证** | pywencai（筛选标的）→ backtrader（回测策略） |
| **通达信公式 + 实盘交易** | tdxquant（公式计算/选股）→ miniqmt / QMT（下单） |
| **全品类数据采集** | akshare（股票/期货/加密货币/宏观） |


## 开发

### 什么是 Skills？

Skills 是由指令、脚本和资源组成的文件夹，Claude 会动态加载它们以提升在专业任务上的表现。Skills 教会 Claude 如何以可重复的方式完成特定任务——例如按照量化策略流程编写交易程序、分析金融数据、自动化研报处理等。

- [什么是 Skills？](https://support.claude.com/en/articles/12512176-what-are-skills)
- [在 Claude 中使用 Skills](https://support.claude.com/en/articles/12512180-using-skills-in-claude)
- [如何创建自定义 Skills](https://support.claude.com/en/articles/12512198-creating-custom-skills)
- [Equipping agents for the real world with Agent Skills](https://anthropic.com/engineering/equipping-agents-for-the-real-world-with-agent-skills)

### 创建新的 Skill

在 `skills/` 目录下新建文件夹，创建 `SKILL.md` 及相关文档或资源文件即可。模板示例：

```markdown
---
name: my-quant-skill
description: 描述该 Skill 的功能及适用场景
---

# 技能名称

[在此编写 Claude 激活该 Skill 时应遵循的指令]

## 示例
- 示例用法 1
- 示例用法 2

## 规则
- 规则 1
- 规则 2
```

Frontmatter 必填字段：
- `name` — 唯一标识符（小写，用连字符分隔）
- `description` — 功能描述，说明该 Skill 做什么以及何时使用

## 量化金融相关资源参考

### 金融相关 Skills

- 东方财富妙想：
    - https://ai.eastmoney.com/mxClaw
    - https://clawhub.ai/u/Financial-AI-Analyst
- 量化相关集合：
    - https://github.com/openclaw/skills/tree/main/skills/coderwpf
    - https://clawhub.ai/u/coderwpf
- 基于富途 OpenAPI 的股票行情 Skill：https://clawhub.ai/shuizhengqi1/futu-stock

**优质 Skills 资源：**

- [anthropics/skills](https://github.com/anthropics/skills)
- [The open agent skills tool - npx skills](https://github.com/vercel-labs/skills)
- [https://skills.sh](https://skills.sh) Vercel 推出的 Skills 聚合站，包含大量开源 Skills，能够按 24 小时热度、官方认证等多种方式快速检索。
- [http://clawhub.ai](http://clawhub.ai) OpenClaw 官方 Skills 集合站。

### 量化交易资源列表

- [Awesome Quant](AWESOME-QUANT.md) 收集整理学习和使用涉及的高质量量化交易资源列表，以便于快速索引查找。

## License

This project is released under the MIT license.

This project is developed and maintained by [Zhiwen Studio](https://lzw.me).
