# Quant Finance Skills

一个面向金融量化交易领域的 Claude Skills 技能维护仓库，基于 [Agent Skills](https://agentskills.io) 标准构建。

## 什么是 Skills？

Skills 是由指令、脚本和资源组成的文件夹，Claude 会动态加载它们以提升在专业任务上的表现。Skills 教会 Claude 如何以可重复的方式完成特定任务——例如按照量化策略流程编写交易程序、分析金融数据、自动化研报处理等。

- [什么是 Skills？](https://support.claude.com/en/articles/12512176-what-are-skills)
- [在 Claude 中使用 Skills](https://support.claude.com/en/articles/12512180-using-skills-in-claude)
- [如何创建自定义 Skills](https://support.claude.com/en/articles/12512198-creating-custom-skills)
- [Equipping agents for the real world with Agent Skills](https://anthropic.com/engineering/equipping-agents-for-the-real-world-with-agent-skills)

## 仓库说明

本仓库维护金融量化交易相关的 Skills，涵盖量化策略开发、金融数据分析、交易框架文档查询等场景。每个 Skill 位于独立文件夹中，包含 `SKILL.md` 指令文件，Claude 会根据该文件中的指令和元数据执行对应任务。

## 目录结构

```
quant-finance-skills/
├── skills/          # 量化交易相关的 Skills 集合
├── template/        # Skill 模板
└── .claude-plugin/  # Claude Code 插件配置
```

## 在 Claude Code 中使用

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

## 使用 `npx skills` 工具为智能体安装技能

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

## 许可证

本项目基于 Apache 2.0 许可证开源。
