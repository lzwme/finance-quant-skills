# QMT Python SKILL 索引

## 📚 模块列表

| 模块 | 说明 | 适合场景 |
|------|------|---------|
| [overview.md](./overview.md) | 系统概述 | 所有新手必读 |
| [execution-mechanisms.md](./execution-mechanisms.md) | 三种运行机制详解 | 选择运行方式 |
| [backtesting-guide.md](./backtesting-guide.md) | 回测完整指南 | 历史数据验证 |
| [live-trading-guide.md](./live-trading-guide.md) | 实盘交易指南 | 真实交易部署 |
| [market-data-api.md](./market-data-api.md) | 行情数据 API | 数据获取查询 |
| [trading-api.md](./trading-api.md) | 交易函数 API | 下单交易查询 |
| [best-practices.md](./best-practices.md) | 最佳实践 | 代码质量优化 |
| [joinquant-migration.md](./joinquant-migration.md) | 聚宽迁移指南 | 从聚宽迁移 |

## 📁 代码示例

| 文件 | 类型 | 难度 |
|------|------|------|
| [examples/backtest.md](./examples/backtest.md) | 双均线回测 | ⭐⭐ |
| [examples/live-trading.md](./examples/live-trading.md) | 双均线实盘 | ⭐⭐⭐ |
| [examples/subscribe.md](./examples/subscribe.md) | 事件驱动 | ⭐⭐⭐ |
| [examples/run-time.md](./examples/run-time.md) | 定时任务 | ⭐⭐ |

## 🚀 学习路径

### 路径 1：回测验证
```
overview.md → execution-mechanisms.md → backtesting-guide.md → examples/backtest.md
```

### 路径 2：实盘交易
```
overview.md → execution-mechanisms.md → live-trading-guide.md → examples/live-trading.md
```

### 路径 3：高频策略
```
overview.md → execution-mechanisms.md → examples/subscribe.md
```

### 路径 4：定时监控
```
overview.md → execution-mechanisms.md → examples/run-time.md
```

## ⚠️ 关键注意

| 项目 | 要求 |
|------|------|
| 编码 | 文件首行必须 `#coding:gbk` |
| 数量 | 最小 100 股 |
| 回测参数 | `subscribe=False` |
| 实盘参数 | `subscribe=True` |

## 🔗 相关链接

- [迅投 QMT 官网](http://www.thinktrader.net/)
- [官方知识库](https://dict.thinktrader.net/)
- [迅投社区](https://xuntou.net/)
