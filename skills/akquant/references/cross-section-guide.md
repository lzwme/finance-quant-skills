# 横截面策略指南

本文档详细说明 akquant 框架中横截面策略的开发方法，包括触发机制、数据准备、调仓逻辑与常见陷阱。

## 目录

- [横截面策略概述](#横截面策略概述)
- [推荐范式：on_timer](#推荐范式on-timer)
- [备选方案：timestamp 收齐](#备选方案timestamp-收齐)
- [实战清单](#实战清单)
- [常见陷阱](#常见陷阱)

---

## 横截面策略概述

### 什么是横截面策略？

横截面策略是在同一时间点对多个标的进行比较、排序或打分，然后根据结果进行调仓。常见应用场景：
- 行业轮动：选择强势行业
- 因子选股：根据因子得分选股
- 动量轮动：选择近期表现最好的标的

### 核心特点

- **同时点比较**：必须在同一时间点对多个标的进行评估
- **相对排名**：关注的是标的之间的相对表现，而非绝对收益
- **定期调仓**：通常在固定时点触发调仓

### 关键挑战

1. **触发时机**：如何确保所有标的数据就绪后再执行
2. **数据同步**：处理停牌、缺失数据等情况
3. **调仓效率**：先卖后买，避免资金占用问题

---

## 推荐范式：on_timer

### 设计思路

使用 `on_timer` 在固定时点统一触发调仓，确保：
- 所有标的在同一时刻被评估
- 调仓逻辑集中在一个地方，易于管理
- 避免 `on_bar` 逐条触发导致的状态不一致

### 基本结构

```python
from akquant import Strategy
import numpy as np

class CrossSectionStrategy(Strategy):
    def __init__(self, lookback=20):
        self.lookback = lookback
        self.universe = ["sh600519", "sz000858", "sh601318"]
        self.warmup_period = lookback + 1
    
    def on_start(self):
        # 订阅所有标的
        for symbol in self.universe:
            self.subscribe(symbol)
        
        # 注册每日定时器
        self.add_daily_timer("14:55:00", "rebalance")
    
    def on_timer(self, payload):
        if payload != "rebalance":
            return
        
        # 1. 计算所有标分数
        scores = {}
        for symbol in self.universe:
            closes = self.get_history(self.lookback, symbol, "close")
            if len(closes) < self.lookback:
                return  # 数据不足，跳过本次调仓
            scores[symbol] = (closes[-1] - closes[0]) / closes[0]
        
        # 2. 选出最佳标的
        best = max(scores, key=scores.get)
        
        # 3. 调仓
        self.order_target_percent(0.95, symbol=best)
```

### 完整示例：动量轮动

```python
from akquant import Strategy, run_backtest
import numpy as np

class MomentumRotation(Strategy):
    """
    动量轮动策略：
    - 每日收盘前计算所有标的的动量分数
    - 持有分数最高的标的
    """
    
    def __init__(self, lookback=20, top_k=1):
        self.lookback = lookback
        self.top_k = top_k
        self.universe = ["sh600519", "sz000858", "sh601318", "sh601166"]
        self.warmup_period = lookback + 1
    
    def on_start(self):
        # 订阅所有标的
        for symbol in self.universe:
            self.subscribe(symbol)
        
        # 每日 14:55 触发调仓
        self.add_daily_timer("14:55:00", "rebalance")
    
    def on_timer(self, payload):
        if payload != "rebalance":
            return
        
        # 计算动量分数
        scores = {}
        for symbol in self.universe:
            closes = self.get_history(self.lookback, symbol, "close")
            
            # 数据不足则跳过
            if len(closes) < self.lookback:
                self.log(f"{symbol} 数据不足，跳过本次调仓")
                return
            
            # 动量 = (最新价 - N日前价格) / N日前价格
            momentum = (closes[-1] - closes[0]) / closes[0]
            scores[symbol] = momentum
        
        # 选出 Top K 标的
        sorted_symbols = sorted(scores, key=scores.get, reverse=True)
        selected = sorted_symbols[:self.top_k]
        
        # 计算目标权重（等权）
        weight_per_stock = 0.95 / self.top_k
        target_weights = {s: weight_per_stock for s in selected}
        
        # 调仓
        self.order_target_weights(
            target_weights=target_weights,
            liquidate_unmentioned=True,  # 平掉未选中的持仓
            rebalance_tolerance=0.01,    # 容忍 1% 偏差
        )
        
        self.log(f"调仓完成: {selected}")

# 运行回测
result = run_backtest(
    strategy=MomentumRotation,
    data=data_dict,  # Dict[str, DataFrame]
    symbol=list(data_dict.keys()),
    initial_cash=1_000_000.0,
    commission_rate=0.0003,
    t_plus_one=True,
)
```

### 多因子打分

```python
class MultiFactorStrategy(Strategy):
    def __init__(self):
        self.universe = ["sh600519", "sz000858", "sh601318"]
        self.warmup_period = 30
    
    def on_start(self):
        for symbol in self.universe:
            self.subscribe(symbol)
        self.add_daily_timer("14:55:00", "rebalance")
    
    def on_timer(self, payload):
        if payload != "rebalance":
            return
        
        scores = {}
        for symbol in self.universe:
            # 因子 1：动量
            closes = self.get_history(20, symbol, "close")
            if len(closes) < 20:
                return
            momentum = (closes[-1] - closes[0]) / closes[0]
            
            # 因子 2：波动率（反向）
            returns = np.diff(closes) / closes[:-1]
            volatility = np.std(returns)
            
            # 因子 3：成交量相对变化
            volumes = self.get_history(20, symbol, "volume")
            if len(volumes) < 20:
                return
            vol_ratio = volumes[-1] / np.mean(volumes)
            
            # 综合得分
            score = (
                momentum * 0.5 -           # 动量权重 50%
                volatility * 10 +          # 波动率权重（负向）
                vol_ratio * 0.3            # 成交量权重 30%
            )
            scores[symbol] = score
        
        # 选出最佳标的
        best = max(scores, key=scores.get)
        self.order_target_percent(0.95, symbol=best)
```

---

## 备选方案：timestamp 收齐

### 适用场景

当策略没有固定调仓时点（无法使用 `on_timer`）时，可在 `on_bar` 中缓存同一时间片的标的数据，收齐后再执行横截面逻辑。

### 实现方式

```python
from collections import defaultdict

class BucketStrategy(Strategy):
    def __init__(self, lookback=20):
        self.lookback = lookback
        self.universe = ["sh600519", "sz000858", "sh601318"]
        self.warmup_period = lookback + 1
        self.pending = defaultdict(set)  # timestamp -> set of symbols
    
    def on_bar(self, bar):
        # 1. 记录当前时间片已到达的标的
        self.pending[bar.timestamp].add(bar.symbol)
        
        # 2. 检查是否所有标的都已到达
        if len(self.pending[bar.timestamp]) < len(self.universe):
            return  # 未收齐，等待
        
        # 3. 收齐后执行横截面逻辑
        self.pending.pop(bar.timestamp, None)
        
        scores = {}
        for symbol in self.universe:
            closes = self.get_history(self.lookback, symbol, "close")
            if len(closes) < self.lookback:
                return
            scores[symbol] = (closes[-1] - closes[0]) / closes[0]
        
        best = max(scores, key=scores.get)
        self.order_target_percent(0.95, symbol=best)
```

### 方案对比

| 维度 | 方案 A：on_timer | 方案 B：timestamp 收齐 |
|------|------------------|------------------------|
| 触发方式 | 固定时点触发 | 事件驱动，时间片收齐触发 |
| 稳健性 | 高，不依赖到达顺序 | 中，需维护缓存并处理缺失 |
| 实现复杂度 | 低，逻辑集中 | 中，需管理 timestamp 缓存 |
| 适用场景 | 日频/定时调仓 | 无固定调仓时点的横截面策略 |
| 常见风险 | 定时器时间与数据频率不匹配 | 某些标的缺失导致不触发 |

**推荐**：优先使用 `on_timer`；只有在无法定义稳定调仓时点时再采用 timestamp 收齐方案。

---

## 实战清单

### 设计阶段

- [ ] 明确横截面触发机制：优先 `on_timer`，无固定时点再考虑时间片收齐方案
- [ ] 明确信号时点与成交时点关系：特别是 `execution_mode="next_open"` 的跨 Bar 成交
- [ ] 固定并版本化 `universe` 来源，记录成分生效日期与调仓周期
- [ ] 定义持仓约束：单标的上限、行业集中度、现金留存、最小交易单位

### 数据阶段

- [ ] 统一时区、交易日历和缺失值策略，避免横截面混入异步样本
- [ ] 评分前校验窗口长度，跳过历史不足样本并统计样本覆盖率
- [ ] 对停牌/复牌、涨跌停、成交量异常设置可追踪的降级处理
- [ ] 固化数据快照和拉取参数，保证回测可复现

### 执行阶段

- [ ] 采用目标仓位接口进行调仓，减少先卖后买导致的仓位漂移
- [ ] 设置调仓容忍区间，避免小幅分数波动引发高换手
- [ ] 对订单拒绝进行集中监控，重点关注 `orders_df.reject_reason`
- [ ] 定期二次收敛仓位，处理一次调仓未完全达到目标的问题

### 风控阶段

- [ ] 启用账户级风控：`max_account_drawdown`、`max_daily_loss`、`stop_loss_threshold`
- [ ] 结合策略特性设置限额：`max_position_pct`、`max_order_value` 等
- [ ] 建立风控触发后的策略行为约定：降仓、暂停、仅平仓
- [ ] 保留风控触发日志，便于复盘和参数迭代

### 验证阶段

- [ ] 做时序切分验证（滚动窗口/分阶段）而不是只看全样本结果
- [ ] 观察关键稳定性指标：换手率、持仓集中度、滑点敏感性、容量约束
- [ ] 对比不同执行模式与调仓频率，确认收益来源稳定
- [ ] 将参数与结果快照写入实验记录，便于回溯

### 上线前检查

- [ ] 清单通过：触发、数据、执行、风控、验证五项全部打勾
- [ ] 演练异常场景：缺行情、拒单、延迟触发、交易日切换
- [ ] 固定运行配置与依赖版本，避免环境漂移
- [ ] 准备回滚方案：参数回滚、策略停用、版本回退

---

## 常见陷阱

### 1. 停牌/缺失数据导致不触发

```python
# ❌ 问题：某标的停牌，on_timer 仍能触发，但该标的数据缺失
def on_timer(self, payload):
    for symbol in self.universe:
        closes = self.get_history(20, symbol, "close")
        # 如果某标的停牌，closes 长度可能不足
        if len(closes) < 20:
            return  # 直接返回，导致所有标的都无法调仓

# ✅ 解决：跳过缺失标的，继续处理其他标的
def on_timer(self, payload):
    scores = {}
    for symbol in self.universe:
        closes = self.get_history(20, symbol, "close")
        if len(closes) < 20:
            self.log(f"{symbol} 数据不足，跳过")
            continue  # 跳过，继续处理其他标的
        scores[symbol] = (closes[-1] - closes[0]) / closes[0]
    
    if len(scores) < len(self.universe) * 0.8:  # 有效样本 < 80%
        return  # 样本不足，跳过本次调仓
    
    # 正常调仓
    best = max(scores, key=scores.get)
    self.order_target_percent(0.95, symbol=best)
```

### 2. Universe 漂移

```python
# ❌ 问题：使用硬编码的 universe，未考虑成分调整
self.universe = ["sh600519", "sz000858", "sh601318"]

# ✅ 解决：定期刷新 universe 并记录生效日期
def on_start(self):
    self.load_universe()  # 从文件或数据库加载
    self.add_daily_timer("09:30:00", "refresh_universe")

def on_timer(self, payload):
    if payload == "refresh_universe":
        self.load_universe()
```

### 3. 调仓时点与执行模式错配

```python
# ❌ 问题：14:55 触发调仓，但使用 NextOpen 模式
# 实际成交在次日开盘，信号与成交时点不一致
self.add_daily_timer("14:55:00", "rebalance")

# ✅ 解决：明确记录信号时点与成交时点
def on_timer(self, payload):
    self.log(f"信号时点: {self.now}")
    # NextOpen 模式下，实际成交在次日开盘
    self.order_target_percent(...)
```

### 4. 历史长度不足

```python
# ❌ 问题：新上市或停牌恢复标的数据窗口不完整
def on_timer(self, payload):
    for symbol in self.universe:
        closes = self.get_history(20, symbol, "close")
        score = (closes[-1] - closes[0]) / closes[0]  # 可能只有 10 根数据

# ✅ 解决：统一做长度检查
def on_timer(self, payload):
    for symbol in self.universe:
        closes = self.get_history(20, symbol, "close")
        if len(closes) < 20:
            continue  # 跳过不足样本
        score = (closes[-1] - closes[0]) / closes[0]
```

### 5. 仓位未收敛

```python
# ❌ 问题：多标的先卖后买，资金未及时释放，导致买入不足
def on_timer(self, payload):
    for symbol in self.universe:
        self.order_target_percent(0.25, symbol)  # 每个标的 25%

# ✅ 解决：使用 order_target_weights 统一调仓
def on_timer(self, payload):
    weights = {s: 0.25 for s in self.universe}
    self.order_target_weights(
        target_weights=weights,
        liquidate_unmentioned=True,
        rebalance_tolerance=0.01,  # 容忍小偏差
    )
```

### 6. timestamp 收齐方案中的缺失问题

```python
# ❌ 问题：某标的永远缺失，pending 永远无法收齐
self.pending[bar.timestamp].add(bar.symbol)
if len(self.pending[bar.timestamp]) < len(self.universe):
    return  # 永远等待

# ✅ 解决：设置超时或降级阈值
def on_bar(self, bar):
    self.pending[bar.timestamp].add(bar.symbol)
    
    # 超时检查：如果下一个 timestamp 已到达，强制处理上一个
    if len(self.pending) > 1:
        old_ts = min(self.pending.keys())
        symbols = self.pending.pop(old_ts)
        if len(symbols) >= len(self.universe) * 0.8:  # 80% 到达即可执行
            self.execute_cross_section(old_ts)
```

---

## 最佳实践

1. **触发机制**：优先使用 `on_timer`，确保同一时点统一决策
2. **数据检查**：每次评分前检查历史数据长度，跳过不足样本
3. **样本阈值**：设置有效样本率阈值（如 80%），避免数据缺失导致决策偏差
4. **调仓接口**：使用 `order_target_weights` 统一调仓，避免先卖后买问题
5. **风控集成**：横截面策略必须配置风控，防止单一标的过度集中
6. **日志记录**：记录每次调仓的信号、决策与成交，便于复盘
7. **异常演练**：测试停牌、涨跌停、拒单等异常场景的表现
