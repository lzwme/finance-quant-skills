---
name: "qmt-docs"
type: skill
description: "QMT（迅投极速策略交易系统）Python 策略开发完整指南。涵盖策略编写、回测、实盘交易、API参考和代码示例。当需要开发QMT量化策略或查询QMT API时使用本技能。"
tags: ["QMT", "迅投", "策略开发", "Python", "回测", "实盘交易", "量化交易"]
metadata:
  {
    "openclaw": {
      "emoji": "📚",
      "requires": {
        "bins": ["python3", "pip3"]
      }
    }
  }
---

# QMT Python 策略开发知识库

为 QMT（迅投极速策略交易系统）提供完整的 Python 开发参考，分为**教程指南**和 **API 参考**两层。

## 📖 文档结构

```
教程/指南（实践导向）
├── overview.md              系统概述、模式选择、入门路径
├── execution-mechanisms.md  三种运行机制详解（含流程图和代码模板）
├── backtesting-guide.md     回测完整流程（数据准备→参数设置→运行→分析）
├── live-trading-guide.md    实盘交易指南（账号配置→委托管理→风险控制）
├── quick-reference.md       ★ 常用 API 速查卡片
├── best-practices.md        编码规范、性能优化、风险管理、调试技巧
├── joinquant-migration.md   聚宽策略迁移至 QMT 指南
└── examples/                代码示例（backtest / live-trading / subscribe / run-time）

API 参考（官方完整文档）
└── python-innerApi/
    ├── start_now.md          快速开始（回测/实盘概览 + 三种机制示例）
    ├── data_function.md      行情与数据函数（get_market_data_ex 等完整参数）
    ├── trading_function.md   交易函数（passorder、get_trade_detail_data 等）
    ├── system_function.md    系统函数（ContextInfo 方法、定时器等）
    ├── callback_function.md  回调函数（account/order/deal/position 主推）
    ├── quote_function.md     引用函数（扩展数据、因子、VBA调用）
    ├── drawing_function.md   绘图函数
    ├── interface_operation.md 界面操作说明
    ├── data_structure.md     数据结构定义（Bar/Tick/Order/Position 等对象字段）
    ├── enum_constants.md     枚举常量（opType、orderType、委托状态等）
    ├── variable_convention.md 变量约定
    ├── code_examples.md      完整代码示例合集
    ├── user_attention.md     用户注意事项
    └── question_answer.md    常见问题

数据字典
└── dict/                    各品种数据字段（stock / indexes / future / option 等）
```

## 🚀 使用引导

### 按场景选择入口

| 场景 | 首先阅读 | 然后查阅 |
|------|---------|---------|
| **新手入门** | `overview.md` → `execution-mechanisms.md` | `quick-reference.md` |
| **编写回测策略** | `backtesting-guide.md` | `examples/backtest.md` |
| **编写实盘策略** | `live-trading-guide.md` | `examples/live-trading.md` |
| **查询 API 用法** | `quick-reference.md`（速查） | `python-innerApi/data_function.md` 等（完整参数） |
| **从聚宽迁移** | `joinquant-migration.md` | `overview.md` |
| **代码质量优化** | `best-practices.md` | `examples/` |
| **数据结构查询** | `python-innerApi/data_structure.md` | `python-innerApi/enum_constants.md` |

### 快速查找路径

```
需要看函数怎么用？
  → quick-reference.md（常用函数精简版）
  → python-innerApi/data_function.md（数据获取类完整文档）
  → python-innerApi/trading_function.md（交易类完整文档）
  → python-innerApi/system_function.md（系统/ContextInfo 方法）

需要看完整代码？
  → python-innerApi/code_examples.md（官方示例合集）
  → examples/（精选示例）

需要查字段含义？
  → python-innerApi/data_structure.md（数据结构定义）
  → dict/（各品种数据字典）

遇到报错/问题？
  → python-innerApi/question_answer.md（官方FAQ）
  → python-innerApi/user_attention.md（注意事项）
```

## 🔧 关键速查

### 编码规范
```python
#coding:gbk  # 必须在文件第一行
```

### 核心概念
| 概念 | 说明 |
|------|------|
| handlebar | K线驱动（回测推荐） |
| subscribe | 事件驱动（仅实盘，高频） |
| run_time | 定时触发（监控场景） |
| quicktrade=0 | 等待K线完成再下单（逐K线模式） |
| quicktrade=2 | 立即下单（不需要等待） |
| 最小单位 | 100 股 |

### 最常用代码
```python
# 获取历史行情数据（回测用 subscribe=False，实盘用 subscribe=True）
data = C.get_market_data_ex(['close'], [stock], end_time=bar_date,
                              period='1d', count=100, subscribe=False)
close_list = list(data[stock].iloc[:, 0])

# 获取全推实时行情
tick = C.get_full_tick(['600000.SH'])
price = tick['600000.SH']['lastPrice']

# 下单买入（23=买入, 1101=按股数, quicktrade=0 逐K线模式）
passorder(23, 1101, account, stock, 5, -1, 100, C)

# 下单买入（quicktrade=2 立即下单模式）
passorder(23, 1101, account, stock, 5, -1, 100, '策略名', 2, '备注', C)

# 查询持仓
holds = get_trade_detail_data(account, 'stock', 'position')
holds_dict = {f'{p.m_strInstrumentID}.{p.m_strExchangeID}': p.m_nVolume for p in holds}

# 查询账户可用资金（单位：分）
cash = get_trade_detail_data(account, 'stock', 'account')[0].m_dAvailable
```

## ⚠️ 使用注意事项

1. **编码声明**：文件首行必须是 `#coding:gbk`，不可省略
2. **位置参数**：`get_market_data_ex` 的前两个参数 `fields` 和 `stocks` 必须用位置参数，不能用 `fields=` 或 `stocks=`
3. **subscribe 参数**：回测必须 `False`，实盘使用 `True`
4. **账号类型**：`get_trade_detail_data` 的第二个参数：股票用 `'stock'`，两融用 `'credit'`
5. **金额单位**：`m_dAvailable` 等金额字段单位是**分**，需 `/100` 转换为元
6. **数量单位**：股票交易必须是 100 的整数倍
7. **实盘限制**：`subscribe` 和 `run_time` 仅支持实盘，不支持回测
