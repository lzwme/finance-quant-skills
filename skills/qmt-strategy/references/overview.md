# QMT 系统概述

QMT（极速策略交易系统）是迅投推出的内置 Python 3.6 环境的量化交易平台，提供**行情数据获取**与**交易下单**两大核心功能。

## 核心特性

| 特性 | 说明 |
|------|------|
| Python 版本 | 3.6 |
| 常用库 | pandas、numpy、talib 等 |
| 编码要求 | **GBK**（文件首行必须 `#coding:gbk`） |
| 股票最小单位 | 100 股 |
| 应用场景 | 指标计算、策略编写、回测、实盘 |

## 两种交易模式

| 维度 | 回测模式 | 实盘模式 |
|------|---------|---------|
| 数据源 | 本地历史数据 | 实时推送 |
| subscribe 参数 | `False` | `True` |
| 撮合 | QMT虚拟撮合 | 真实交易所 |
| 账号 | 任意字符串 | 真实/模拟账号 |
| 风险 | 无风险 | 真实风险 |

**回测撮合规则：**
- 指定价格在 K 线高低点间 → 按指定价格
- 超出高低点范围 → 按收盘价
- 数量大于可用 → 按可用数量

**实盘撮合规则：**
- 价格不能超过当前价 2%（价格笼子）
- 数量超过可用 → 废单

## 三种运行机制

| 机制 | 触发方式 | 回测 | 实盘 | 典型场景 |
|------|---------|:----:|:----:|---------|
| **handlebar** | 逐 K 线驱动 | ✅ | ✅ | 回测、盘中模拟 K 线 |
| **subscribe** | 事件驱动（分笔推送） | ❌ | ✅ | 分笔高频交易 |
| **run_time** | 定时触发 | ❌ | ✅ | 定时监控 |

> 详细机制说明（含流程图、代码模板、quicktrade 对比）→ [execution-mechanisms.md](./execution-mechanisms.md)

## 场景选择指南

| 需求 | 推荐机制 | 数据源 | 下单模式 |
|------|---------|--------|---------|
| 历史回测 | handlebar | 本地数据 | quicktrade=0 |
| 盘中模拟 K 线 | handlebar | 实时分笔 | quicktrade=0 |
| 分笔高频交易 | subscribe | 实时推送 | quicktrade=2 |
| 定时监控 | run_time | 定时查询 | quicktrade=2 |

## 开发入门路径

```
新手上路:
  overview.md (本文) → execution-mechanisms.md → quick-reference.md → 代码示例

开发回测:
  backtesting-guide.md → examples/backtest.md

开发实盘:
  live-trading-guide.md → examples/live-trading.md

查找 API:
  quick-reference.md (速查) → python-innerApi/ (完整文档)
```

## 📚 文档体系说明

| 层级 | 目录 | 定位 |
|------|------|------|
| **教程/指南** | `references/*.md`（本文同级） | 实践导向，含代码模板和场景说明 |
| **API 参考** | `references/python-innerApi/*.md` | 完整官方 API 文档，含所有参数和数据结构 |
| **数据字典** | `references/dict/*.md` | 各品种数据字段说明 |
| **代码示例** | `references/examples/*.md` | 完整可运行策略代码 |

## 下一步

- 📖 了解运行机制 → [execution-mechanisms.md](./execution-mechanisms.md)
- 🔧 查看 API 速查 → [quick-reference.md](./quick-reference.md)
- 🧪 开始回测 → [backtesting-guide.md](./backtesting-guide.md)
- 💹 进行实盘 → [live-trading-guide.md](./live-trading-guide.md)
- 📋 完整 API → [python-innerApi/start_now.md](./python-innerApi/start_now.md)
- 🌐 官方知识库 → [dict.thinktrader.net](https://dict.thinktrader.net)
