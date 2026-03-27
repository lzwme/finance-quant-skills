---
name: akquant
description: 生成 akquant 框架的可执行量化策略代码，涵盖数据接口、事件驱动、风控与优化；当用户需要开发 akquant量化策略 时使用
metadata: {"clawdbot":{"emoji":"📈","requires":{"bins":["python", "uv"],"os":"win32"}}}
---

# AKQuant 量化策略开发指南

## 任务目标

本 Skill 用于辅助 AI 编程智能体生成符合 akquant 框架规范的可执行量化策略代码。能力包括策略设计、回测配置、订单管理、风控规则、参数优化与横截面策略实现。

## 核心能力清单

- 策略类生成：继承 Strategy 基类，实现生命周期钩子
- 数据接口配置：准备 DataFrame 数据、设置预热期、访问历史数据
- 事件驱动机制：on_bar/on_tick/on_order/on_trade 等回调
- 订单管理：市价单/限价单/目标仓位/OCO/Bracket/Trailing Stop
- 风控规则：持仓限制/回撤熔断/止损阈值/行业集中度
- 参数优化：网格搜索与滚动优化（Walk-Forward）
- 多策略编排：slot 映射与策略级风控

## 触发条件

当用户表达以下意图时触发：
- 开发量化交易策略
- 配置回测环境与参数
- 设置风险控制规则
- 进行参数优化与调优
- 实现横截面或轮动策略
- 排查策略运行错误

## 策略开发工作流

### 阶段一：理解需求

1. 识别策略类型：趋势跟踪、均值回归、横截面轮动、套利等
2. 确定数据需求：时间周期、标的范围、字段要求
3. 明确风控约束：持仓上限、止损止盈、回撤限制

### 阶段二：设计策略结构

参考 [strategy-patterns.md](references/strategy-patterns.md) 选择范式：
- 类风格（推荐）：继承 Strategy，封装状态与逻辑
- 函数风格：initialize + on_bar，快速原型

关键决策点：
- 预热期设置：根据指标窗口长度计算
- 历史数据访问：get_history (numpy) 或 get_history_df (DataFrame)
- 执行模式：NextOpen（下一 Bar 开盘）或 CurrentClose（当前 Bar 收盘）

### 阶段三：编写策略代码

使用 [assets/strategy-template.py](assets/strategy-template.py) 作为起点：

```python
from akquant import Strategy, Bar

class MyStrategy(Strategy):
    warmup_period = 20  # 预热数据长度

    def __init__(self, param1=10):
        self.param1 = param1

    def on_start(self):
        self.subscribe("600000")

    def on_bar(self, bar: Bar):
        # 核心交易逻辑
        history = self.get_history(self.param1, bar.symbol, "close")
        if len(history) < self.param1:
            return

        import numpy as np
        ma = np.mean(history)
        pos = self.get_position(bar.symbol)

        if bar.close > ma and pos == 0:
            self.buy(bar.symbol, 100)
        elif bar.close < ma and pos > 0:
            self.sell(bar.symbol, 100)
```

### 阶段四：配置回测环境

参考 [api-reference.md](references/api-reference.md) 设置参数：

```python
from akquant import run_backtest

result = run_backtest(
    strategy=MyStrategy,
    data=df,
    symbol="600000",
    initial_cash=500_000.0,
    commission_rate=0.0003,
    stamp_tax_rate=0.001,
    t_plus_one=True,  # A 股 T+1 规则
    warmup_period=20,
    execution_mode="NextOpen",
)
```

### 阶段五：设置风控规则

参考 [risk-management.md](references/risk-management.md) 配置：

```python
from akquant.config import RiskConfig

result = run_backtest(
    ...,
    risk_config=RiskConfig(
        max_position_pct=0.10,  # 单标的持仓不超过 10%
        max_account_drawdown=0.20,  # 最大回撤 20%
        max_daily_loss=0.05,  # 单日亏损 5%
    ),
)
```

### 阶段六：参数优化

参考 [optimization.md](references/optimization.md) 执行：

```python
from akquant import run_grid_search, run_walk_forward

# 网格搜索
results = run_grid_search(
    strategy=MyStrategy,
    param_grid={"param1": [10, 20, 30]},
    data=df,
    sort_by="sharpe_ratio",
)

# 滚动优化（推荐）
wfo_results = run_walk_forward(
    strategy=MyStrategy,
    param_grid={"param1": [10, 20, 30]},
    data=df,
    train_period=250,
    test_period=60,
    metric="sharpe_ratio",
)
```

## 横截面策略开发

参考 [cross-section-guide.md](references/cross-section-guide.md) 实现多标的轮动：

**推荐范式**：使用 on_timer 统一触发调仓

```python
class CrossSectionStrategy(Strategy):
    def __init__(self):
        self.universe = ["sh600519", "sz000858", "sh601318"]

    def on_start(self):
        self.add_daily_timer("14:55:00", "rebalance")

    def on_timer(self, payload):
        if payload != "rebalance":
            return

        # 计算所有标分数
        scores = {}
        for symbol in self.universe:
            history = self.get_history(20, symbol, "close")
            scores[symbol] = (history[-1] - history[0]) / history[0]

        # 选出最佳标的并调仓
        best = max(scores, key=scores.get)
        self.order_target_percent(0.95, symbol=best)
```

## 资源索引

| 资源 | 用途 | 何时读取 |
|------|------|----------|
| [api-reference.md](references/api-reference.md) | API 速查 | 查询函数签名与参数 |
| [strategy-patterns.md](references/strategy-patterns.md) | 策略范式 | 设计策略结构 |
| [risk-management.md](references/risk-management.md) | 风控配置 | 设置风控规则 |
| [optimization.md](references/optimization.md) | 参数优化 | 调优策略参数 |
| [cross-section-guide.md](references/cross-section-guide.md) | 横截面策略 | 实现多标的轮动 |
| [strategy-template.py](assets/strategy-template.py) | 策略模板 | 快速生成代码骨架 |
## 环境准备与依赖管理

### 使用 uv 管理项目环境（推荐）

由于 akquant 依赖 `pandas>=3.0.0`，全局安装可能与现有项目存在版本冲突。推荐使用 **uv** 创建隔离环境：

#### 1. 安装 uv：若已安装则跳过

```bash
# macOS
brew install uv

# Linux
curl -LsSf https://astral.sh/uv/install.sh | sh

# Windows (PowerShell)
powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
```

#### 2. 创建项目并初始化环境

```bash
# 创建项目目录
mkdir my-quant-strategy
cd my-quant-strategy

# 初始化项目（创建 pyproject.toml）
uv init

# 创建虚拟环境并安装依赖
uv venv
uv add akquant pandas numpy
```

#### 3. 运行策略脚本

```bash
# 方式一：使用 uv run（推荐）
uv run python my_strategy.py

# 方式二：激活虚拟环境后运行
source .venv/bin/activate  # macOS/Linux
# .venv\Scripts\activate   # Windows
python my_strategy.py
```

#### 4. 依赖版本锁定

uv 会自动生成 `uv.lock` 文件，确保团队依赖一致：

```bash
# 安装精确版本（从 lock 文件）
uv sync

# 添加新依赖
uv add scipy  # 自动更新 lock 文件
```

#### 5. 项目结构建议

```
my-quant-strategy/
├── .venv/              # 虚拟环境（uv 自动创建）
├── pyproject.toml      # 项目配置
├── uv.lock             # 依赖锁定文件
├── strategies/         # 策略脚本
│   ├── ma_strategy.py
│   └── cross_section.py
└── data/               # 数据文件
    └── stock_data.csv
```

### 快速启动命令

```bash
# 一键创建并运行策略项目
mkdir quant-project && cd quant-project
uv init
uv venv
uv add akquant pandas numpy

# 创建策略文件（使用模板）
cat > strategy.py << 'EOF'
from akquant import Strategy, Bar, run_backtest
import pandas as pd
import numpy as np

class MyStrategy(Strategy):
    warmup_period = 20

    def on_bar(self, bar: Bar):
        closes = self.get_history(20, bar.symbol, "close")
        if len(closes) < 20:
            return
        ma = np.mean(closes)
        pos = self.get_position(bar.symbol)
        if bar.close > ma and pos == 0:
            self.buy(bar.symbol, 100)
        elif bar.close < ma and pos > 0:
            self.sell(bar.symbol, pos)

# 准备数据并运行回测
# result = run_backtest(strategy=MyStrategy, data=df, symbol="600000")
EOF

# 运行策略
uv run python strategy.py
```

## 注意事项

1. **预热期计算**：确保 warmup_period >= 指标所需的最大窗口长度
2. **T+1 规则**：A 股策略需设置 t_plus_one=True，并区分总持仓与可用持仓
3. **风控优先级**：显式参数 > 配置对象 > 默认值
4. **数据格式**：DataFrame 必须包含 date/open/high/low/close/volume/symbol 字段
5. **横截面触发**：优先使用 on_timer，无固定时点再考虑 timestamp 收齐方案
6. **优化风险**：网格搜索易过拟合，推荐使用滚动优化验证稳健性

## 使用示例

### 示例 1：双均线策略

```python
from akquant import Strategy, Bar
import numpy as np

class DualMAStrategy(Strategy):
    warmup_period = 30

    def __init__(self, fast=10, slow=20):
        self.fast = fast
        self.slow = slow
        self.warmup_period = slow + 1

    def on_bar(self, bar: Bar):
        fast_ma = np.mean(self.get_history(self.fast, bar.symbol, "close"))
        slow_ma = np.mean(self.get_history(self.slow, bar.symbol, "close"))

        pos = self.get_position(bar.symbol)
        if fast_ma > slow_ma and pos == 0:
            self.buy(bar.symbol, 100)
        elif fast_ma < slow_ma and pos > 0:
            self.sell(bar.symbol, pos)
```

### 示例 2：带风控的趋势策略

```python
from akquant import Strategy, Bar, run_backtest
from akquant.config import RiskConfig
import numpy as np

class TrendStrategy(Strategy):
    warmup_period = 20

    def __init__(self, ma_window=20, stop_loss=0.05):
        self.ma_window = ma_window
        self.stop_loss = stop_loss

    def on_bar(self, bar: Bar):
        ma = np.mean(self.get_history(self.ma_window, bar.symbol, "close"))
        pos = self.get_position(bar.symbol)

        if bar.close > ma * 1.02 and pos == 0:
            self.buy(bar.symbol, 100)
        elif bar.close < ma * 0.98 and pos > 0:
            self.sell(bar.symbol, pos)

# 运行回测
result = run_backtest(
    strategy=TrendStrategy,
    data=df,
    symbol="600000",
    initial_cash=1_000_000.0,
    risk_config=RiskConfig(
        max_position_pct=0.20,
        max_account_drawdown=0.15,
        stop_loss_threshold=0.85,
    ),
)
```

### 示例 3：横截面动量轮动

```python
from akquant import Strategy, run_backtest
import numpy as np

class MomentumRotation(Strategy):
    def __init__(self, lookback=20):
        self.lookback = lookback
        self.universe = ["sh600519", "sz000858", "sh601318"]
        self.warmup_period = lookback + 1

    def on_start(self):
        for symbol in self.universe:
            self.subscribe(symbol)
        self.add_daily_timer("14:55:00", "rebalance")

    def on_timer(self, payload):
        if payload != "rebalance":
            return

        scores = {}
        for symbol in self.universe:
            closes = self.get_history(self.lookback, symbol, "close")
            if len(closes) < self.lookback:
                return
            scores[symbol] = (closes[-1] - closes[0]) / closes[0]

        # 选出最佳标的，持仓 95%
        best = max(scores, key=scores.get)
        self.order_target_percent(0.95, symbol=best)
```
