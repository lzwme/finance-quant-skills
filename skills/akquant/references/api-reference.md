# API 速查手册

本文档提供 akquant 核心 API 的快速参考，涵盖回测入口、策略基类、交易对象与配置类。

## 目录

- [回测入口](#回测入口)
- [策略基类](#策略基类)
- [交易对象](#交易对象)
- [配置类](#配置类)
- [数据对象](#数据对象)

---

## 回测入口

### run_backtest

最常用的回测入口函数，封装了引擎的初始化和配置过程。

```python
from akquant import run_backtest

result = run_backtest(
    strategy=MyStrategy,          # 策略类或实例
    data=df,                      # DataFrame 或 Dict[str, DataFrame]
    symbol="600000",              # 标的代码或列表
    initial_cash=500_000.0,       # 初始资金
    commission_rate=0.0003,       # 佣金率
    stamp_tax_rate=0.001,         # 印花税率
    transfer_fee_rate=0.00002,    # 过户费率
    min_commission=5.0,           # 最低佣金
    slippage=0.0001,              # 滑点
    volume_limit_pct=0.25,        # 成交量限制
    execution_mode="NextOpen",    # 执行模式
    t_plus_one=False,             # T+1 规则
    warmup_period=20,             # 预热期
    start_time="2023-01-01",      # 开始时间
    end_time="2023-12-31",        # 结束时间
    risk_config=RiskConfig(...),  # 风控配置
)
```

**关键参数说明**：

| 参数 | 类型 | 默认值 | 说明 |
|------|------|--------|------|
| `strategy` | Type[Strategy] / Strategy / Callable | 必填 | 策略类、实例或函数式 on_bar |
| `data` | DataFrame / Dict[str, DataFrame] / List[Bar] | 必填 | 回测数据 |
| `symbol` | str / List[str] | "BENCHMARK" | 标的代码或列表 |
| `initial_cash` | float | 1,000,000.0 | 初始资金 |
| `execution_mode` | ExecutionMode / str | "NextOpen" | 执行模式：NextOpen 或 CurrentClose |
| `t_plus_one` | bool | False | 是否启用 T+1 规则 |
| `warmup_period` | int | 0 | 预热数据长度（Bar 数量） |
| `slippage` | float | 0.0 | 滑点（百分比，如 0.0001 = 1bp） |
| `volume_limit_pct` | float | 0.25 | 单笔成交不超过 Bar 成交量的百分比 |

**执行模式说明**：
- `NextOpen`：信号触发后在下一 Bar 开盘价成交（默认）
- `CurrentClose`：信号触发后在当前 Bar 收盘价成交

### run_grid_search

网格搜索参数优化。

```python
from akquant import run_grid_search

results = run_grid_search(
    strategy=MyStrategy,
    param_grid={"ma_window": [10, 20, 30], "stop_loss": [0.03, 0.05]},
    data=df,
    sort_by="sharpe_ratio",
    ascending=False,
    timeout=60.0,  # 单次任务超时（秒）
    result_filter=lambda m: m["trade_count"] >= 50,  # 结果筛选
)
```

### run_walk_forward

滚动优化（Walk-Forward Optimization）。

```python
from akquant import run_walk_forward

wfo_results = run_walk_forward(
    strategy=MyStrategy,
    param_grid={"ma_window": [10, 20, 30]},
    data=df,
    train_period=250,   # 训练窗口长度
    test_period=60,     # 测试窗口长度
    metric="sharpe_ratio",
)
```

---

## 策略基类

### Strategy

策略基类，用户应继承此类并重写回调方法。

#### 生命周期钩子

| 方法 | 触发时机 | 用途 |
|------|----------|------|
| `__init__` | 对象初始化 | 定义参数 |
| `on_start()` | 策略启动时 | 订阅数据、注册指标 |
| `on_resume()` | 热启动恢复时 | 处理快照恢复逻辑 |
| `on_bar(bar: Bar)` | K 线闭合时 | 核心交易逻辑 |
| `on_tick(tick: Tick)` | Tick 到达时 | 高频/盘口策略 |
| `on_order(order: Order)` | 订单状态变化时 | 监控订单状态 |
| `on_trade(trade: Trade)` | 成交回报时 | 记录成交信息 |
| `on_reject(order: Order)` | 订单被拒绝时 | 处理拒单逻辑 |
| `on_timer(payload: str)` | 定时器触发时 | 定时调仓 |
| `on_session_start` | 会话开始时 | 交易日切换 |
| `on_session_end` | 会话结束时 | 日终处理 |
| `before_trading` | 交易日开始时 | 日前准备 |
| `after_trading` | 交易日结束时 | 日后清理 |
| `on_portfolio_update` | 账户快照变化时 | 监控资产变化 |
| `on_error` | 用户回调抛异常时 | 错误处理 |
| `on_stop()` | 策略停止时 | 资源清理 |

#### 属性访问

| 属性 | 说明 |
|------|------|
| `self.symbol` | 当前标的代码 |
| `self.close` | 当前最新价 |
| `self.open` | 当前开盘价 |
| `self.high` | 当前最高价 |
| `self.low` | 当前最低价 |
| `self.volume` | 当前成交量 |
| `self.now` | 当前回测时间（pd.Timestamp） |
| `self.position` | 当前标的持仓辅助对象（Position） |

#### 交易方法

```python
# 市价单
self.buy(symbol, quantity)
self.sell(symbol, quantity)

# 限价单
self.buy(symbol, quantity, price=10.5)
self.sell(symbol, quantity, price=10.5)

# 止损/止盈单
self.buy(symbol, quantity, trigger_price=9.5)  # 价格跌破 9.5 时买入

# 目标仓位
self.order_target(target=100, symbol="AAPL")  # 调整持仓至 100 股
self.order_target_percent(0.5, symbol="AAPL")  # 调整持仓至总资产 50%
self.order_target_value(10000, symbol="AAPL")  # 调整持仓至 10000 元

# 多标的权重调仓
self.order_target_weights(
    target_weights={"AAPL": 0.4, "MSFT": 0.3},
    liquidate_unmentioned=True,  # 平掉未提及的持仓
    rebalance_tolerance=0.01,    # 容忍小偏差
)

# 撤单
self.cancel_order(order_id)
self.cancel_all_orders(symbol)

# OCO 订单组
self.create_oco_order_group(first_order_id, second_order_id)

# Bracket 订单
self.place_bracket_order(
    symbol=bar.symbol,
    quantity=100,
    stop_trigger_price=bar.close * 0.98,
    take_profit_price=bar.close * 1.04,
)

# 跟踪止损
self.place_trailing_stop(
    symbol=bar.symbol,
    quantity=100,
    trail_offset=1.5,  # 跟踪偏移
    side="Sell",
)
```

#### 数据查询方法

```python
# 获取历史数据（numpy array）
history = self.get_history(count=20, symbol="AAPL", field="close")

# 获取历史数据（DataFrame）
df = self.get_history_df(count=20, symbol="AAPL")

# 获取持仓
position = self.get_position(symbol)  # 总持仓
available = self.get_available_position(symbol)  # 可用持仓（T+1）

# 获取所有持仓
positions = self.get_positions()  # Dict[str, float]

# 获取账户信息
cash = self.get_cash()
account = self.get_account()  # {"cash": ..., "equity": ..., "market_value": ...}

# 获取订单与成交
order = self.get_order(order_id)
open_orders = self.get_open_orders(symbol)
trades = self.get_trades()
```

#### 工具方法

```python
# 日志记录
self.log("信号触发", level=logging.INFO)

# 定时任务
self.add_daily_timer("14:55:00", "rebalance")  # 每日定时
self.schedule("2023-01-01 09:30:00", "special")  # 单次定时

# 订阅数据
self.subscribe("AAPL")

# 时间转换
local_time = self.to_local_time(timestamp)
time_str = self.format_time(timestamp, "%Y-%m-%d %H:%M:%S")
```

---

## 交易对象

### Order

```python
@dataclass
class Order:
    id: str                        # 订单 ID
    symbol: str                    # 标的代码
    side: OrderSide                # Buy / Sell
    order_type: OrderType          # Market / Limit / StopMarket
    status: OrderStatus            # New / Filled / Cancelled / Rejected
    quantity: float                # 委托数量
    filled_quantity: float         # 已成交数量
    price: Optional[float]         # 委托价格
    average_filled_price: float    # 成交均价
    trigger_price: Optional[float] # 触发价格
    time_in_force: TimeInForce     # GTC / IOC / FOK / Day
    created_at: int                # 创建时间戳（纳秒）
    updated_at: int                # 更新时间戳
    tag: str                       # 标签
    reject_reason: str             # 拒绝原因
```

### Trade

单次成交记录（一个订单可能对应多次成交）。

```python
@dataclass
class Trade:
    id: str           # 成交 ID
    order_id: str     # 对应订单 ID
    symbol: str       # 标的代码
    side: OrderSide   # 方向
    quantity: float   # 成交数量
    price: float      # 成交价格
    commission: float # 手续费
    timestamp: int    # 成交时间戳
```

### ClosedTrade

已平仓交易记录（开仓+平仓完整周期）。

```python
@dataclass
class ClosedTrade:
    entry_time: int       # 开仓时间
    exit_time: int        # 平仓时间
    entry_price: float    # 开仓价格
    exit_price: float     # 平仓价格
    quantity: float       # 数量
    pnl: float            # 盈亏金额
    return_pct: float     # 收益率
    duration: int         # 持仓时间（秒）
    mae: float            # 最大不利变动
    mfe: float            # 最大有利变动
```

---

## 配置类

### BacktestConfig

```python
from akquant import BacktestConfig, StrategyConfig

config = BacktestConfig(
    strategy_config=StrategyConfig(
        initial_cash=500_000.0,
        commission_rate=0.0003,
        t_plus_one=True,
    ),
    start_time="2023-01-01",
    end_time="2023-12-31",
    instruments=["600000"],
    show_progress=True,
)
```

### StrategyConfig

```python
from akquant import StrategyConfig

strategy_config = StrategyConfig(
    initial_cash=500_000.0,
    commission_rate=0.0003,
    stamp_tax_rate=0.001,
    slippage=0.0001,
    volume_limit_pct=0.25,
    t_plus_one=True,
    max_long_positions=10,
    risk=RiskConfig(
        max_position_pct=0.10,
        max_account_drawdown=0.20,
    ),
)
```

### RiskConfig

```python
from akquant.config import RiskConfig

risk_config = RiskConfig(
    active=True,
    safety_margin=0.0001,
    max_order_size=10000,           # 单笔最大委托数量
    max_order_value=100_000.0,      # 单笔最大委托金额
    max_position_size=50000,        # 单标的最大持仓数量
    max_position_pct=0.10,          # 单标的持仓上限（占总权益）
    sector_concentration=0.20,      # 行业集中度限制
    max_account_drawdown=0.20,      # 账户最大回撤
    max_daily_loss=0.05,            # 单日最大亏损
    stop_loss_threshold=0.80,       # 账户净值止损阈值
)
```

### InstrumentConfig

```python
from akquant import InstrumentConfig

# 股票配置
stock_config = InstrumentConfig(
    symbol="600000",
    asset_type="STOCK",
    lot_size=100,
)

# 期货配置
futures_config = InstrumentConfig(
    symbol="IF2312",
    asset_type="FUTURES",
    multiplier=300.0,      # 合约乘数
    margin_ratio=0.12,     # 保证金率
    tick_size=0.2,         # 最小变动价位
)

# 期权配置
option_config = InstrumentConfig(
    symbol="10003720",
    asset_type="OPTION",
    option_type="CALL",
    strike_price=3.0,
    expiry_date="2023-12-27",
    underlying_symbol="510050",
)
```

---

## 数据对象

### Bar

K 线数据对象。

```python
@dataclass
class Bar:
    timestamp: int               # Unix 时间戳（纳秒）
    open: float                  # 开盘价
    high: float                  # 最高价
    low: float                   # 最低价
    close: float                 # 收盘价
    volume: float                # 成交量
    symbol: str                  # 标的代码
    extra: Dict[str, float]      # 扩展数据字典
    
    @property
    def timestamp_str(self) -> str:
        """时间字符串"""
        ...
```

### Tick

Tick 数据对象。

```python
@dataclass
class Tick:
    timestamp: int     # Unix 时间戳（纳秒）
    price: float       # 最新价
    volume: float      # 成交量
    symbol: str        # 标的代码
```

---

## BacktestResult

回测结果对象。

```python
@dataclass
class BacktestResult:
    metrics_df: pd.DataFrame       # 绩效指标表
    trades_df: pd.DataFrame        # 平仓交易表
    orders_df: pd.DataFrame        # 委托记录表
    executions_df: pd.DataFrame    # 成交流水表
    positions_df: pd.DataFrame     # 每日持仓表
    equity_curve: List[Tuple]      # 权益曲线
    
    # 方法
    def exposure_df(self, freq="D") -> pd.DataFrame:
        """组合暴露分解"""
        ...
    
    def attribution_df(self, by="symbol") -> pd.DataFrame:
        """归因分析"""
        ...
    
    def capacity_df(self, freq="D") -> pd.DataFrame:
        """容量代理指标"""
        ...
```

**常用指标**：

| 指标 | 字段名 | 说明 |
|------|--------|------|
| 总收益率 | `total_return_pct` | 策略总收益百分比 |
| 年化收益率 | `annual_return_pct` | 年化收益百分比 |
| 夏普比率 | `sharpe_ratio` | 风险调整后收益 |
| 最大回撤 | `max_drawdown_pct` | 最大回撤百分比 |
| 卡玛比率 | `calmar_ratio` | 年化收益 / 最大回撤 |
| 胜率 | `win_rate` | 盈利交易占比 |
| 盈亏比 | `profit_loss_ratio` | 平均盈利 / 平均亏损 |
| 交易次数 | `trade_count` | 总交易次数 |
