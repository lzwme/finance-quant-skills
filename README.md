# Finance Quant Skills

一个面向金融量化交易领域的 Claude Skills 技能维护仓库，基于 [Agent Skills](https://agentskills.io) 标准构建。

## 目录结构

本仓库维护金融量化交易相关的 Skills，涵盖量化策略开发、金融数据分析、交易框架文档查询等场景。每个 Skill 位于独立文件夹中，包含 `SKILL.md` 指令等文件。

```
quant-finance-skills/
├── skills/          # 量化交易相关的 Skills 集合
├── template/        # Skill 模板
└── .claude-plugin/  # Claude Code 插件配置
```

## 安装使用

### 让 AI Agent 帮助安装

以对话的形式告诉 Agent 智能体，如 `OpenClaw`：

> 帮我安装这个 skills 仓库中的所有技能: https://github.com/lzwme/quant-finance-skills
>
> 帮我安装这个 skills 仓库中的 qmt-docs 技能: https://github.com/lzwme/quant-finance-skills

### 在 Claude Code 中安装使用

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

### 使用 `npx skills` 工具为智能体安装技能

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

### 在代码仓库中安装并支持多编程智能体工具的技巧

不同编程智能体的 skills 目录规范有所不同。当我们会在多个编程工具之间切换使用时，则需要配置多个 skills 目录。

通过软连接和 `.gitignore` 配置，可以将 skills 目录链接到多个编程工具的 skills 目录中：

```bash
# 假若在 agents/skills 中维护 skills
# 创建 .cluade、.cursor 的 skills 软连接

# macOS/Linux 下
ln -s agents/skills .cluade/skills
ln -s agents/skills .cursor/skills

# windows powershell 下（需管理员权限。也可将 SymbolicLink 改为 Junction，则无需管理员权限）
New-Item -ItemType SymbolicLink -Path .cluade/.cursor/skills -Target <绝对路径>/agents/skills
New-Item -ItemType SymbolicLink -Path .cursor/skills -Target <绝对路径>/agents/skills
```

## 创建新的 Skill

在 `skills/` 目录下新建文件夹，创建 `SKILL.md` 文件即可：

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

## 相关资源及参考

### 什么是 Skills？

Skills 是由指令、脚本和资源组成的文件夹，Claude 会动态加载它们以提升在专业任务上的表现。Skills 教会 Claude 如何以可重复的方式完成特定任务——例如按照量化策略流程编写交易程序、分析金融数据、自动化研报处理等。

- [什么是 Skills？](https://support.claude.com/en/articles/12512176-what-are-skills)
- [在 Claude 中使用 Skills](https://support.claude.com/en/articles/12512180-using-skills-in-claude)
- [如何创建自定义 Skills](https://support.claude.com/en/articles/12512198-creating-custom-skills)
- [Equipping agents for the real world with Agent Skills](https://anthropic.com/engineering/equipping-agents-for-the-real-world-with-agent-skills)

### 量化金融相关 Skills 参考

- 东方财富妙想：
    - https://ai.eastmoney.com/mxClaw
    - https://clawhub.ai/u/Financial-AI-Analyst
- 量化相关集合：
    - https://github.com/openclaw/skills/tree/main/skills/coderwpf
    - https://clawhub.ai/u/coderwpf
- 基于富途 OpenAPI 的股票行情 Skill：https://clawhub.ai/shuizhengqi1/futu-stock

**Skills 资源或参考：**

- [anthropics/skills](https://github.com/anthropics/skills)
- [The open agent skills tool - npx skills](https://github.com/vercel-labs/skills)
- [https://skills.sh](https://skills.sh) Vercel 推出的 Skills 聚合站，包含大量开源 Skills，能够按 24 小时热度、官方认证等多种方式快速检索。
- [http://clawhub.ai](http://clawhub.ai) OpenClaw 官方 Skills 集合站。

### 量化交易平台及资源

- [Awesome Quant](AWESOME-QUANT.md) 涉及学习和使用的一些量化交易平台及资源列表

## License

This project is released under the MIT license.

This project is developed and maintained by [Zhiwen Studio](https://lzw.me).
