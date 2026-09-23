# Finance Quant Skills

一个面向金融量化交易领域的 Claude Skills 技能维护仓库，基于 [Agent Skills](https://agentskills.io) 标准构建。

## 一、目录结构

本仓库维护金融量化交易相关的 Skills，涵盖量化策略开发、金融数据分析、交易框架文档查询等场景。每个 Skill 位于独立文件夹中，包含 `SKILL.md` 指令等文件。

```
finance-quant-skills/
├── skills/              # 量化交易相关的 Skills 集合
│   ├── akquant/         # AKQuant 框架量化策略开发（事件驱动、风控与优化）
│   ├── akshare/    # AKShare 开源金融数据接口（股票/期货/基金/加密货币等）
│   ├── backtrader/      # Backtrader 开源量化回测框架
│   ├── baostock/        # BaoStock A股数据平台（免费行情、K线、财务数据）
│   ├── jqdatasdk/       # 聚宽数据接口（A股行情、财务、因子数据）
│   ├── joinquant-strategy/ # 聚宽官网策略开发文档（回测/模拟/API/因子/技术指标）
│   ├── miniqmt/         # MiniQMT 迅投量化交易接口（XtQuant，支持交易下单）
│   ├── pywencai/        # 同花顺问财数据查询（中文自然语言查询）
│   ├── qmt-strategy/    # QMT 客户端策略开发指南与 API 参考文档
│   ├── rqalpha/         # RQAlpha 米筐开源回测框架（A股/期货）
│   ├── equity-researcher/ # 机构级投研报告生成（Kimi 官方技能）
│   ├── tdxquant/        # 通达信量化数据获取（行情/K线/财务/板块/公式执行）
│   └── tushare/         # Tushare 数据接口（A股行情、财务、宏观数据）
├── template/            # Skill 模板
├── .claude-plugin/      # Claude Code 插件配置
└── .codex-plugin/       # Codex 插件配置（marketplace 索引见 .agents/plugins/）
```

## 二、Skills 安装

请根据你的使用场景选择合适的安装方式：

### 2.1 方式一：让 AI Agent 帮助安装

以对话的形式告诉 Agent 智能体，如 `OpenClaw`：

> 帮我安装这个 skills 仓库中的所有技能: https://github.com/lzwme/finance-quant-skills
>
> 帮我安装这个 skills 仓库中的 qmt-strategy 技能: https://github.com/lzwme/finance-quant-skills

### 2.2 方式二：在 Claude Code 中安装使用

将该仓库注册为 Claude Code Plugin marketplace：

```bash
/plugin marketplace add lzwme/finance-quant-skills
```

然后安装指定的 Skills 插件：

```bash
/plugin install quant-skills@finance-quant-skills
/plugin install quant-docs@finance-quant-skills
```

也可以通过界面操作：选择 `Browse and install plugins` → `finance-quant-skills` → 选择插件 → `Install now`。

安装后，直接描述需求即可触发对应 Skill，例如："使用 QMT 文档 Skill 查询如何通过 Python 调用交易接口"。

### 2.3 方式三（推荐）：使用 `npx skills` 工具为智能体安装技能

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
npx skills add lzwme/finance-quant-skills
```

### 2.4 方式四：在 Codex CLI 中安装使用

本仓库同时提供了 Codex 插件清单（`.codex-plugin/plugin.json`），可将本仓库注册为 Codex 插件 marketplace 后安装：

```bash
codex plugin marketplace add lzwme/finance-quant-skills
```

然后在 Codex 会话中输入 `/plugins`，进入插件界面选择 `finance-quant-skills` 安装即可。安装后会加载全部技能，直接用自然语言描述需求即可触发。

### 2.5 安装技巧：以软连接形式支持多编程智能体工具

不同编程智能体的 skills 目录规范有所不同。当我们在多个编程工具之间切换使用时，需要配置多个 skills 目录。

通过软连接和 `.gitignore` 配置，可以将 skills 目录链接到多个编程工具的 skills 目录中，如此则仅在源目录维护更新文件即可。

创建软连接的命令示例如下：

```bash
# 假若在 agents/skills 中维护 skills
# 创建 .cluade、.cursor、.codex 的 skills 软连接

# macOS/Linux 下
ln -s agents/skills .cluade/skills
ln -s agents/skills .cursor/skills
ln -s agents/skills .codex/skills

# windows powershell 下（其中的 Junction 也可换为 SymbolicLink，但需管理员权限执行）
New-Item -ItemType Junction -Path .cluade/skills -Target <绝对路径>/agents/skills
New-Item -ItemType Junction -Path .cursor/skills -Target <绝对路径>/agents/skills
New-Item -ItemType Junction -Path .codex/skills -Target <绝对路径>/agents/skills
```

`.gitignore` 配置示例如下：

```
# 假若仅在 .agents/skills 中维护 skills
# 忽略 .cluade、.cursor、.codex 等目录下的 skills 软连接
.cluade/skills
.cursor/skills
.codex/skills
.codebuddy/skills
```

## 三、Skills 使用示例

Skills 的详细使用示例见 [USAGE_EXAMPLES.md](./USAGE_EXAMPLES.md)，涵盖数据获取、策略回测、策略开发与文档三大类共 13 个 Skills 的调用场景。

### 3.1 Skills 一览

| 分类 | 名称 | 说明 | 接入方式 |
|------|------|------|---------|
| 数据获取 | **baostock** | A 股历史 K 线、财务报表、指数成分股 | 免费，无需注册 |
| 数据获取 | **akshare** | 股票/期货/加密货币/宏观等全品类金融数据 | 免费，无需注册 |
| 数据获取 | **pywencai** | 同花顺问财自然语言选股查询 | 需配置 Cookie |
| 数据获取 | **tdxquant** | 通达信行情快照、K 线、财务、公式执行 | 需客户端 |
| 数据获取 | **miniqmt** | MiniQMT（xtquant 库）实时行情订阅、K 线、交易下单 | 需客户端 |
| 数据获取 | **jqdatasdk** | 聚宽数据：行情、财务、因子数据 | 需 Token |
| 数据获取 | **tushare** | Tushare Pro：A 股行情、财务、宏观数据 | 需 Token |
| 回测框架 | **backtrader** | 事件驱动回测，内置 100+ 指标 | 开源 Python |
| 回测框架 | **rqalpha** | 米筐回测，支持 A 股/期货 | 开源 Python |
| 策略开发 | **akquant** | 事件驱动策略框架，支持风控、优化 | 开源 Python |
| 策略开发 | **qmt-strategy** | QMT 客户端策略开发指南与 API 参考 | 文档查阅 |
| 策略开发 | **joinquant-strategy** | 聚宽官网策略编写与 API 文档 | 文档查阅 |
| 投研报告 | **equity-researcher** | 机构级投研报告生成（投资速览/深度研报） | Kimi 官方技能 |

详见 [USAGE_EXAMPLES.md](./USAGE_EXAMPLES.md) 获取具体使用场景与参数说明。


## 四、开发

### 4.1 什么是 Skills？

Skills 是由指令、脚本和资源组成的文件夹，Claude 会动态加载它们以提升在专业任务上的表现。Skills 教会 Claude 如何以可重复的方式完成特定任务——例如按照量化策略流程编写交易程序、分析金融数据、自动化研报处理等。

- [什么是 Skills？](https://support.claude.com/en/articles/12512176-what-are-skills)
- [在 Claude 中使用 Skills](https://support.claude.com/en/articles/12512180-using-skills-in-claude)
- [如何创建自定义 Skills](https://support.claude.com/en/articles/12512198-creating-custom-skills)
- [Equipping agents for the real world with Agent Skills](https://anthropic.com/engineering/equipping-agents-for-the-real-world-with-agent-skills)

### 4.2 创建新的 Skill

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

## 五、量化金融相关资源参考

### 5.1 量化金融相关 Skills

- 东方财富妙想：
    - https://ai.eastmoney.com/mxClaw
    - https://clawhub.ai/u/Financial-AI-Analyst
- 量化相关 Skill 集合：
    - https://github.com/openclaw/skills/tree/main/skills/coderwpf
    - https://clawhub.ai/u/coderwpf
- 聚宽策略开发 Skill：https://clawhub.ai/daidaotian/joinquant-strategy
- 基于富途 OpenAPI 的股票行情 Skill：https://clawhub.ai/shuizhengqi1/futu-stock
- [quantskills](https://github.com/quantskills) 由 [PandaAI](https://www.pandaaiquant.com/login?invite=1C91)发起的 AI Agent 时代的开放量化社区， 聚焦 Quant Skills（量化技能） 和 Agents（智能体） 两类资产。

**优质 Skills 资源：**

- [anthropics/skills](https://github.com/anthropics/skills)
- [The open agent skills tool - npx skills](https://github.com/vercel-labs/skills)
- [https://skills.sh](https://skills.sh) Vercel 推出的 Skills 聚合站，包含大量开源 Skills，能够按 24 小时热度、官方认证等多种方式快速检索。
- [http://clawhub.ai](http://clawhub.ai) OpenClaw 官方 Skills 集合站。

### 5.2 量化交易资源列表

- [Awesome Quant](AWESOME-QUANT.md) 收集整理学习和使用涉及的高质量量化交易资源列表，以便于快速索引查找。

## License

This project is released under the MIT license.

This project is developed and maintained by [Zhiwen Studio](https://lzw.me).
