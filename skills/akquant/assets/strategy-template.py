"""
AKQuant 策略模板

本模板提供策略类的基本结构，包含常用生命周期钩子和交易方法示例。
使用时根据实际需求修改参数和逻辑。

使用方法：
1. 复制此文件并重命名（如 my_strategy.py）
2. 修改策略类名和参数
3. 实现 on_bar 中的核心交易逻辑
4. 根据需要启用其他生命周期钩子

环境准备（使用 uv 管理依赖）：
    # 创建项目
    mkdir my-quant-strategy && cd my-quant-strategy
    uv init
    uv venv
    uv add akquant pandas numpy
    
    # 运行策略
    uv run python my_strategy.py
"""

from akquant import Strategy, Bar, Order, Trade
import numpy as np


class TemplateStrategy(Strategy):
    """
    策略模板类
    
    参数说明：
    - param1: 参数1描述
    - param2: 参数2描述
    """
    
    # 预热数据长度（Bar 数量）
    # 根据指标所需的最大窗口长度设置
    warmup_period = 20
    
    def __init__(self, param1=10, param2=0.05):
        """
        初始化策略参数
        
        注意：不要在这里调用交易 API，策略尚未启动
        """
        self.param1 = param1
        self.param2 = param2
        
        # 动态设置预热期（可选）
        self.warmup_period = param1 + 5
        
        # 策略内部状态
        self.entry_price = None
        self.trade_count = 0
    
    def on_start(self):
        """
        策略启动时调用
        
        必须在此处订阅数据，否则 on_bar 不会触发
        """
        # 订阅标的（必填）
        self.subscribe("600000")
        
        # 可选：注册定时器
        # self.add_daily_timer("14:55:00", "rebalance")
        
        self.log("策略启动")
    
    def on_resume(self):
        """
        热启动时调用（在 on_start 之前）
        
        用于处理从快照恢复后的特殊逻辑
        """
        if self.is_restored:
            self.log("从快照恢复")
    
    def on_bar(self, bar: Bar):
        """
        K 线闭合时触发（核心交易逻辑）
        
        参数：
        - bar: 当前 K 线数据对象
        """
        # 1. 获取历史数据
        closes = self.get_history(self.param1, bar.symbol, "close")
        
        # 2. 检查数据是否足够
        if len(closes) < self.param1:
            return
        
        # 3. 计算指标
        ma = np.mean(closes)
        std = np.std(closes)
        
        # 4. 获取当前持仓
        pos = self.get_position(bar.symbol)
        
        # 5. 交易逻辑
        # 开仓条件
        if bar.close > ma * 1.02 and pos == 0:
            self.buy(bar.symbol, 100)
            self.entry_price = bar.close
            self.log(f"开仓: {bar.symbol} @ {bar.close}")
        
        # 平仓条件
        elif bar.close < ma * 0.98 and pos > 0:
            self.sell(bar.symbol, pos)
            self.entry_price = None
            self.log(f"平仓: {bar.symbol} @ {bar.close}")
        
        # 止损逻辑
        elif pos > 0 and self.entry_price:
            pnl_pct = (bar.close - self.entry_price) / self.entry_price
            if pnl_pct < -self.param2:
                self.sell(bar.symbol, pos)
                self.entry_price = None
                self.log(f"止损: {bar.symbol} @ {bar.close}, PnL: {pnl_pct:.2%}")
    
    def on_tick(self, tick):
        """
        Tick 数据到达时触发（高频/盘口策略）
        
        仅在使用 Tick 数据时启用
        """
        pass
    
    def on_order(self, order: Order):
        """
        订单状态变化时触发
        
        注意：先于 on_bar 触发
        """
        if order.status.name == "Filled":
            self.log(f"订单成交: {order.symbol} {order.side.name} {order.filled_quantity}@{order.average_filled_price}")
        elif order.status.name == "Rejected":
            self.log(f"订单被拒: {order.reject_reason}", level=40)
    
    def on_trade(self, trade: Trade):
        """
        成交回报时触发
        """
        self.trade_count += 1
        self.log(f"成交: {trade.symbol} {trade.quantity}@{trade.price}")
    
    def on_reject(self, order: Order):
        """
        订单被拒绝时触发（每个订单仅触发一次）
        """
        self.log(f"订单被拒: {order.symbol} {order.reject_reason}", level=40)
    
    def on_timer(self, payload: str):
        """
        定时器触发时调用
        
        用于定时调仓（横截面策略推荐使用）
        """
        if payload == "rebalance":
            self.log("执行定时调仓")
            # 实现调仓逻辑
    
    def on_session_start(self, session, timestamp):
        """会话开始时触发"""
        pass
    
    def on_session_end(self, session, timestamp):
        """会话结束时触发"""
        pass
    
    def before_trading(self, trading_date, timestamp):
        """每个交易日开始时触发"""
        self.log(f"交易日开始: {trading_date}")
    
    def after_trading(self, trading_date, timestamp):
        """每个交易日结束时触发"""
        self.log(f"交易日结束: {trading_date}")
    
    def on_portfolio_update(self, snapshot):
        """账户快照变化时触发"""
        # equity = snapshot.equity
        # cash = snapshot.cash
        pass
    
    def on_error(self, error, source, payload=None):
        """
        用户回调抛异常时触发
        
        可通过 self.error_mode 控制行为：
        - "raise": 继续抛出异常（默认）
        - "continue": 记录日志后继续运行
        """
        self.log(f"策略错误: {error}", level=40)
    
    def on_stop(self):
        """策略停止时调用"""
        self.log(f"策略停止，总交易次数: {self.trade_count}")


# ============================================================
# 回测配置示例
# ============================================================

if __name__ == "__main__":
    import pandas as pd
    from akquant import run_backtest
    from akquant.config import RiskConfig
    
    # 1. 准备数据
    def generate_data():
        dates = pd.date_range(start="2023-01-01", end="2023-12-31")
        n = len(dates)
        price = 100 * np.cumprod(1 + np.random.normal(0.0005, 0.02, n))
        return pd.DataFrame({
            "date": dates,
            "open": price,
            "high": price * 1.01,
            "low": price * 0.99,
            "close": price,
            "volume": 10000,
            "symbol": "600000",
        })
    
    df = generate_data()
    
    # 2. 运行回测
    result = run_backtest(
        strategy=TemplateStrategy,
        data=df,
        symbol="600000",
        initial_cash=500_000.0,
        commission_rate=0.0003,
        stamp_tax_rate=0.001,
        t_plus_one=True,
        warmup_period=20,
        execution_mode="NextOpen",
        risk_config=RiskConfig(
            max_position_pct=0.20,
            max_account_drawdown=0.15,
        ),
    )
    
    # 3. 查看结果
    print(f"总收益率: {result.metrics.total_return_pct:.2f}%")
    print(f"夏普比率: {result.metrics.sharpe_ratio:.2f}")
    print(f"最大回撤: {result.metrics.max_drawdown_pct:.2f}%")
    print(f"交易次数: {result.metrics.trade_count}")
    
    # 4. 查看详细数据
    # print(result.metrics_df)
    # print(result.trades_df)
    # print(result.orders_df)


# ============================================================
# 使用 uv 运行策略的完整示例
# ============================================================
"""
# 步骤 1: 创建项目目录
mkdir my-quant-strategy
cd my-quant-strategy

# 步骤 2: 初始化 uv 项目
uv init

# 步骤 3: 创建虚拟环境
uv venv

# 步骤 4: 安装依赖（akquant 需要 pandas>=3.0.0）
uv add akquant pandas numpy

# 步骤 5: 创建策略文件（复制本模板）
cp /path/to/strategy-template.py strategy.py

# 步骤 6: 运行策略
uv run python strategy.py

# 可选: 激活虚拟环境后直接运行
source .venv/bin/activate  # macOS/Linux
# .venv\Scripts\activate   # Windows
python strategy.py

# 项目结构:
# my-quant-strategy/
# ├── .venv/
# ├── pyproject.toml
# ├── uv.lock
# ├── strategy.py
# └── data/
#     └── stock_data.csv
"""
