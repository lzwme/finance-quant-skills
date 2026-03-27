---
name: "qmt-docs"
type: skill
description: "QMT完整的策略开发指南、API参考和代码示例。当需要开发QMT策略时，请参考本指南。"
tags: ["QMT", "策略开发", "Python", "回测", "实盘交易", "量化交易"]
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

# QMT Python策略开发知识库

完整的 QMT（迅投极速策略交易系统）Python 开发指南，包含系统概述、执行机制、回测实盘指南、API 参考和代码示例。

## 📚 模块导航

### 基础
- **[系统概述](references/overview.md)** - QMT 架构、两种交易模式、场景选择
- **[执行机制](references/execution-mechanisms.md)** - handlebar、subscribe、run_time

### 指南
- **[回测指南](references/backtesting-guide.md)** - 历史数据回测完整流程
- **[实盘指南](references/live-trading-guide.md)** - 实时交易部署与风险管理

### API 参考
- **[行情数据 API](references/market-data-api.md)** - 数据获取函数
- **[交易 API](references/trading-api.md)** - 下单、查询函数

### 其他
- **[最佳实践](references/best-practices.md)** - 编码规范、性能优化
- **[聚宽迁移](references/joinquant-migration.md)** - 聚宽策略移植指南

### 代码示例
| 示例 | 机制 | 文件 |
|------|------|------|
| 双均线回测 | handlebar | [examples/backtest.md](references/examples/backtest.md) |
| 双均线实盘 | handlebar | [examples/live-trading.md](references/examples/live-trading.md) |
| 事件驱动 | subscribe | [examples/subscribe.md](references/examples/subscribe.md) |
| 定时任务 | run_time | [examples/run-time.md](references/examples/run-time.md) |

## 🔧 关键速查

### 编码规范
```python
#coding:gbk  # 必须在第一行
```

### 核心概念
| 概念 | 说明 |
|------|------|
| handlebar | K线驱动（回测推荐） |
| subscribe | 事件驱动（仅实盘，高频） |
| run_time | 定时触发（监控场景） |
| quicktrade | 0=等待K线完成, 2=立即执行 |
| 最小单位 | 100 股 |

### 常用代码
```python
# 获取数据
data = C.get_market_data_ex(['close'], [stock], count=100, subscribe=False)

# 下单买入
passorder(23, 1101, account, stock, 5, -1, 100, C)

# 查询持仓
holds = get_trade_detail_data(account, 'stock', 'position')
```

## 📖 使用建议

1. **新手**：从 [overview.md](references/overview.md) 开始
2. **查找**：使用 [INDEX.md](references/INDEX.md) 导航
3. **回测**：阅读 [backtesting-guide.md](references/backtesting-guide.md)
4. **实盘**：阅读 [live-trading-guide.md](references/live-trading-guide.md)
