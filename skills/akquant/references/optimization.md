# 参数优化指南

本文档详细说明 akquant 框架的参数优化方法，包括网格搜索、滚动优化与参数模型驱动。

## 目录

- [优化方法对比](#优化方法对比)
- [网格搜索](#网格搜索)
- [滚动优化](#滚动优化)
- [参数模型驱动](#参数模型驱动)
- [最佳实践](#最佳实践)

---

## 优化方法对比

| 特性 | 网格搜索 | 滚动优化 |
|------|----------|----------|
| **数据使用** | 全部数据一次性优化 | 数据滚动切分，训练/测试严格分离 |
| **参数结果** | 1 组全局静态参数 | 多组动态变化的参数 |
| **过拟合风险** | **极高**（看着答案找最优解） | **低**（模拟真实未知环境） |
| **核心目的** | 探索参数敏感性，找"理论上限" | 验证策略稳健性，评估"实战预期" |
| **API** | `run_grid_search` | `run_walk_forward` |

**推荐**：生产策略必须使用滚动优化验证稳健性。

---

## 网格搜索

### 基本用法

```python
from akquant import run_grid_search

# 定义参数网格
param_grid = {
    "ma_window": [10, 20, 30],
    "stop_loss": [0.03, 0.05, 0.08],
}

# 运行网格搜索
results = run_grid_search(
    strategy=MyStrategy,
    param_grid=param_grid,
    data=df,
    sort_by="sharpe_ratio",
    ascending=False,
)

# 查看结果
print(results.head())
```

### 多目标排序

```python
results = run_grid_search(
    strategy=MyStrategy,
    param_grid=param_grid,
    data=df,
    sort_by=["sharpe_ratio", "total_return"],  # 优先夏普，其次收益
    ascending=[False, False],
)
```

### 结果筛选

```python
def result_filter(metrics):
    return (
        metrics.get("trade_count", 0) >= 50 and        # 交易次数 >= 50
        metrics.get("sharpe_ratio", 0) > 1.0 and       # 夏普 > 1.0
        metrics.get("max_drawdown_pct", 1.0) < 0.2     # 最大回撤 < 20%
    )

results = run_grid_search(
    strategy=MyStrategy,
    param_grid=param_grid,
    data=df,
    result_filter=result_filter,
)
```

### 动态预热期

```python
def warmup_calc(params):
    # 预热期 = 指标窗口 + 缓冲
    return params["ma_window"] + 5

results = run_grid_search(
    strategy=MyStrategy,
    param_grid=param_grid,
    data=df,
    warmup_calc=warmup_calc,
)
```

### 参数约束

```python
def param_constraint(params):
    # 短期均线 < 长期均线
    return params["fast_window"] < params["slow_window"]

results = run_grid_search(
    strategy=MyStrategy,
    param_grid={
        "fast_window": [5, 10, 15],
        "slow_window": [20, 30, 60],
    },
    constraint=param_constraint,
)
```

### 资源控制

```python
results = run_grid_search(
    strategy=MyStrategy,
    param_grid=param_grid,
    data=df,
    timeout=60.0,            # 单次任务超时 60 秒
    max_tasks_per_child=1,   # 每次任务重启进程
)
```

### 断点续传

```python
results = run_grid_search(
    strategy=MyStrategy,
    param_grid=param_grid,
    data=df,
    db_path="optimization.db",  # 持久化到 SQLite
)
```

**特性**：
- 实时保存：每完成一个组合立即写入数据库
- 断点续传：程序中断后自动跳过已完成的组合
- 结果复用：可从数据库读取历史结果

---

## 滚动优化

### 原理

滚动优化（Walk-Forward Optimization, WFO）模拟真实的时间流逝，将数据切分为多个 `[训练集 | 测试集]` 窗口：

```
窗口 1: [训练 1-3 月] → [测试 4 月]
窗口 2: [训练 2-4 月] → [测试 5 月]
窗口 3: [训练 3-5 月] → [测试 6 月]
...
最终: 拼接所有测试段结果
```

**核心思想**：永远只用过去的数据来决定现在的参数。

### 基本用法

```python
from akquant import run_walk_forward

wfo_results = run_walk_forward(
    strategy=MyStrategy,
    param_grid=param_grid,
    data=df,
    train_period=250,      # 训练窗口长度（Bar 数量）
    test_period=60,        # 测试窗口长度（Bar 数量）
    metric="sharpe_ratio", # 优化目标
    ascending=False,
)

print(wfo_results)
```

### 多目标优化

```python
wfo_results = run_walk_forward(
    strategy=MyStrategy,
    param_grid=param_grid,
    data=df,
    train_period=250,
    test_period=60,
    metric=["sharpe_ratio", "total_return"],  # 多目标
    ascending=[False, False],
)
```

### 完整示例

```python
from akquant import Strategy, run_walk_forward
import numpy as np

class MAStrategy(Strategy):
    def __init__(self, fast=10, slow=20):
        self.fast = fast
        self.slow = slow
        self.warmup_period = slow + 1
    
    def on_bar(self, bar):
        fast_ma = np.mean(self.get_history(self.fast, bar.symbol, "close"))
        slow_ma = np.mean(self.get_history(self.slow, bar.symbol, "close"))
        
        pos = self.get_position(bar.symbol)
        if fast_ma > slow_ma and pos == 0:
            self.buy(bar.symbol, 100)
        elif fast_ma < slow_ma and pos > 0:
            self.sell(bar.symbol, pos)

# 定义参数网格
param_grid = {
    "fast": [5, 10, 15],
    "slow": [20, 30, 60],
}

# 参数约束
def constraint(params):
    return params["fast"] < params["slow"]

# 动态预热期
def warmup_calc(params):
    return params["slow"] + 1

# 运行滚动优化
wfo_results = run_walk_forward(
    strategy=MAStrategy,
    param_grid=param_grid,
    data=df,
    train_period=250,
    test_period=60,
    metric="sharpe_ratio",
    constraint=constraint,
    warmup_calc=warmup_calc,
    initial_cash=500_000.0,
)
```

### 参数选择

| 参数 | 建议 | 说明 |
|------|------|------|
| `train_period` | 180-250 | 日频数据约 1 年；窗口越长参数越稳定 |
| `test_period` | 20-60 | 日频数据约 1-3 个月；滚动步长 |
| `metric` | `"sharpe_ratio"` | 推荐夏普比率；也可用 `"total_return"` |

---

## 参数模型驱动

### 定义参数模型

```python
from akquant import ParamModel, IntParam, FloatParam

class StrategyParams(ParamModel):
    fast_period: int = IntParam(10, ge=2, le=200, title="快线周期")
    slow_period: int = IntParam(30, ge=3, le=500, title="慢线周期")
    stop_loss: float = FloatParam(0.05, ge=0.01, le=0.20, title="止损比例")
```

### 策略类声明

```python
from akquant import Strategy

class MyStrategy(Strategy):
    PARAM_MODEL = StrategyParams
    
    def __init__(self, fast_period=10, slow_period=30, stop_loss=0.05):
        self.fast_period = fast_period
        self.slow_period = slow_period
        self.stop_loss = stop_loss
        self.warmup_period = slow_period + 1
```

### 导出 Schema

```python
from akquant import get_strategy_param_schema

schema = get_strategy_param_schema(MyStrategy)
# 返回 JSON Schema，用于前端表单生成
```

### 校验参数

```python
from akquant import validate_strategy_params

# 校验用户输入
params = validate_strategy_params(
    MyStrategy,
    {"fast_period": 12, "slow_period": 36, "stop_loss": 0.08},
)

# 校验失败会抛出异常
try:
    validate_strategy_params(
        MyStrategy,
        {"fast_period": 300, "slow_period": 20},  # fast > max, fast > slow
    )
except Exception as e:
    print(f"参数校验失败: {e}")
```

### 与网格搜索结合

```python
# PARAM_MODEL 用于单次回测校验
# param_grid 用于网格搜索

results = run_grid_search(
    strategy=MyStrategy,
    param_grid={
        "fast_period": [5, 10, 15],
        "slow_period": [20, 30, 60],
    },
    data=df,
)
```

---

## 最佳实践

### 1. 避免过拟合

```python
# ❌ 错误：直接使用网格搜索最优参数
results = run_grid_search(...)
best_params = results.iloc[0].to_dict()
# 在生产中使用 best_params → 可能是过拟合的产物

# ✅ 正确：使用滚动优化验证稳健性
wfo_results = run_walk_forward(...)
# 如果 WFO 结果稳定，说明参数具有稳健性
```

### 2. 设置合理的筛选条件

```python
def result_filter(metrics):
    return (
        metrics.get("trade_count", 0) >= 30 and        # 交易次数足够
        metrics.get("sharpe_ratio", 0) > 0.5 and       # 夏普为正
        metrics.get("max_drawdown_pct", 1.0) < 0.3 and # 回撤可控
        metrics.get("win_rate", 0) > 0.4               # 胜率合理
    )
```

### 3. 使用参数约束减少无效组合

```python
def constraint(params):
    # 逻辑约束
    if params["fast"] >= params["slow"]:
        return False
    
    # 合理性约束
    if params["stop_loss"] > params["take_profit"]:
        return False
    
    return True
```

### 4. 动态预热期避免数据不足

```python
def warmup_calc(params):
    # 预热期 = 最大指标窗口 + 缓冲
    max_window = max(params["fast"], params["slow"], params["rsi_period"])
    return max_window + 10
```

### 5. 分析参数稳定性

```python
# 网格搜索后分析参数敏感性
results = run_grid_search(...)

# 查看同一参数不同值的表现
for ma in [10, 20, 30]:
    subset = results[results["ma_window"] == ma]
    print(f"MA={ma}: 平均夏普={subset['sharpe_ratio'].mean():.2f}")

# 如果某参数值的表现在显著优于其他，可能过拟合
```

### 6. 分阶段验证

```python
# 阶段 1：网格搜索探索参数空间
grid_results = run_grid_search(
    strategy=MyStrategy,
    param_grid={"ma": range(5, 50, 5)},  # 粗粒度
    data=df_train,
)

# 阶段 2：在候选范围内细粒度搜索
top_ma = grid_results.iloc[0]["ma"]
fine_results = run_grid_search(
    strategy=MyStrategy,
    param_grid={"ma": range(top_ma - 5, top_ma + 6, 1)},  # 细粒度
    data=df_validate,
)

# 阶段 3：滚动优化最终验证
wfo_results = run_walk_forward(
    strategy=MyStrategy,
    param_grid={"ma": [top_ma - 2, top_ma, top_ma + 2]},
    data=df_test,
)
```

---

## 完整示例

```python
from akquant import (
    Strategy,
    run_grid_search,
    run_walk_forward,
    ParamModel,
    IntParam,
    FloatParam,
    validate_strategy_params,
)
import numpy as np

# 1. 定义参数模型
class TrendParams(ParamModel):
    fast: int = IntParam(10, ge=2, le=100, title="快线")
    slow: int = IntParam(30, ge=5, le=200, title="慢线")
    stop_loss: float = FloatParam(0.05, ge=0.01, le=0.20, title="止损")

# 2. 定义策略
class TrendStrategy(Strategy):
    PARAM_MODEL = TrendParams
    
    def __init__(self, fast=10, slow=30, stop_loss=0.05):
        self.fast = fast
        self.slow = slow
        self.stop_loss = stop_loss
        self.warmup_period = slow + 1
        self.entry_price = None
    
    def on_bar(self, bar):
        # 指标计算
        fast_ma = np.mean(self.get_history(self.fast, bar.symbol, "close"))
        slow_ma = np.mean(self.get_history(self.slow, bar.symbol, "close"))
        
        pos = self.get_position(bar.symbol)
        
        # 开仓
        if fast_ma > slow_ma and pos == 0:
            self.buy(bar.symbol, 100)
            self.entry_price = bar.close
        
        # 止损
        elif pos > 0 and self.entry_price:
            pnl = (bar.close - self.entry_price) / self.entry_price
            if pnl < -self.stop_loss:
                self.sell(bar.symbol, pos)
                self.entry_price = None
        
        # 平仓
        elif fast_ma < slow_ma and pos > 0:
            self.sell(bar.symbol, pos)
            self.entry_price = None

# 3. 参数约束
def constraint(params):
    return params["fast"] < params["slow"]

# 4. 动态预热期
def warmup_calc(params):
    return params["slow"] + 5

# 5. 结果筛选
def result_filter(metrics):
    return (
        metrics.get("trade_count", 0) >= 20 and
        metrics.get("sharpe_ratio", 0) > 0.5
    )

# 6. 网格搜索（探索阶段）
param_grid = {
    "fast": [5, 10, 15, 20],
    "slow": [30, 40, 50, 60],
    "stop_loss": [0.03, 0.05, 0.08],
}

grid_results = run_grid_search(
    strategy=TrendStrategy,
    param_grid=param_grid,
    data=df,
    constraint=constraint,
    warmup_calc=warmup_calc,
    result_filter=result_filter,
    sort_by="sharpe_ratio",
    db_path="optimization.db",
)

print("网格搜索结果 Top 5:")
print(grid_results.head())

# 7. 滚动优化（验证阶段）
wfo_results = run_walk_forward(
    strategy=TrendStrategy,
    param_grid={
        "fast": [10, 15],
        "slow": [30, 40],
        "stop_loss": [0.05],
    },
    data=df,
    train_period=250,
    test_period=60,
    metric="sharpe_ratio",
    constraint=constraint,
    warmup_calc=warmup_calc,
)

print("\n滚动优化结果:")
print(wfo_results)
```
