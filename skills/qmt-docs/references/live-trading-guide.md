# QMT 实盘交易完全指南

## 🎯 实盘交易概述

**实盘交易**是指在盘中接收最新的动态行情，即时发送买卖信号到交易所，判断委托状态，进行实时交易的过程。

### 实盘与回测的核心差异

| 维度 | 回测 | 实盘 |
|------|------|------|
| **数据源** | 本地历史数据 | 实时行情推送 |
| **触发方式** | K线驱动 | 分笔驱动 |
| **执行速度** | 批量处理 | 实时处理 |
| **交易对手** | 虚拟账户 | 真实交易所 |
| **撮合规则** | QMT模拟 | 交易所规则 |
| **风险** | 无风险 | 真实风险 |

---

## 🛠️ 第一步：配置账号

### 账号类型

QMT支持两种账号类型：

#### 1. 真实柜台账号（实盘账号）
- **特点**：连接交易所真实柜台
- **用途**：真实资金交易
- **风险**：真实亏损可能
- **获取**：联系券商或购买投研端账号

#### 2. 模拟柜台账号（模拟账号）
- **特点**：QMT提供的虚拟柜台
- **用途**：模拟环境测试
- **风险**：无风险
- **获取**：购买QMT模拟柜台撮合服务

### 账号配置步骤

1. **选择账号类型**
   ```
   我的界面 → 账号设置 → 选择账号类型
   ```

2. **配置账户信息**
   ```
   账户名称: 账号ID（如 888888）
   账户类型: stock（股票）或 credit（两融）
   登录状态: 需要确保账户已登录
   ```

3. **启用账号**
   ```
   模型交易界面 → 新建策略交易 → 选择账号
   ```

4. **验证账号连接**
   ```python
   # 在 init 函数中测试
   account = get_trade_detail_data('账号名称', 'stock', 'account')
   if account:
       print("账号已连接")
   else:
       print("账号连接失败")
   ```

---

## 📋 第二步：基础信息配置

### 策略参数设置

在模型交易界面配置以下信息：

#### 1. 基本信息

```
策略名称: 双均线实盘策略
描述: 基于快慢均线的实盘交易策略
创建日期: 自动生成
```

#### 2. 品种配置

```
主图品种: 要交易的股票代码（如 600000.SH）
默认周期: K线周期（1d、1w、5m等）
市场: 上海(SH) 或 深圳(SZ)
```

#### 3. 账号配置

```python
# 在代码中获取当前账号信息
account = account  # 模型交易界面选择的账号
accountType = accountType  # 账号类型（STOCK/CREDIT）
```

#### 4. 资金管理

```
初始现金: 账号的可用现金（自动获取）
单笔交易额: 固定金额或百分比
最大持仓: 最多持有多少手
```

### 风险管理设置

```python
# 在 init 中设置风险参数
class RiskControl:
    def __init__(self):
        self.max_loss_per_day = 0.05    # 每日最大亏损 5%
        self.max_position_size = 10000  # 最大持仓 10000 股
        self.max_single_trade = 5000    # 单笔最大 5000 股
        self.stop_loss_pct = 0.03       # 止损幅度 3%

risk = RiskControl()
```

---

## 🚀 第三步：两种交易模式

### 交易模式概览

QMT系统支持两种委托和交易模式：

| 模式 | 参数值 | 特点 | 适用场景 |
|------|------|------|--------|
| **逐K线模式** | quicktrade=0 | 等待K线完成 | 中期策略 |
| **立即下单模式** | quicktrade=2 | 立刻执行 | 高频策略 |

---

## 🔄 模式一：逐K线模式（quicktrade=0）

### 工作原理

```
盘中时段
  ↓
每个分笔数据到达（通常3秒一次）
  ↓
触发 handlebar 函数
  ↓
handlebar 中产生交易信号
  ↓
系统暂存交易信号（不立刻发出）
  ↓
3秒后下一个分笔到达
  ↓
检查是否为新K线的首个分笔
  ├─→ 是：发送暂存的交易信号
  └─→ 否：丢弃暂存的交易信号
```

### 代码实现

```python
#coding:gbk

import pandas as pd
import numpy as np
import datetime

class TradeState:
    """保存策略状态"""
    def __init__(self):
        self.stock = None
        self.acct = None
        self.acct_type = None
        self.amount = 10000              # 单笔买入金额
        self.line1 = 17                  # 快线周期
        self.line2 = 27                  # 慢线周期
        self.buy_code = 23               # 买入代码
        self.sell_code = 24              # 卖出代码
        self.waiting_list = []           # 未查到委托列表

A = TradeState()

def init(C):
    """初始化函数"""
    # 获取策略参数
    A.stock = C.stockcode + '.' + C.market
    A.acct = account                     # 模型交易界面选择
    A.acct_type = accountType            # 账号类型
    
    # 设置均线参数
    A.line1 = 17   # 快线周期
    A.line2 = 27   # 慢线周期
    
    # 设置下单代码
    if A.acct_type == 'STOCK':
        A.buy_code = 23
        A.sell_code = 24
    else:  # CREDIT
        A.buy_code = 33
        A.sell_code = 34
    
    print(f'双均线实盘 {A.stock} {A.acct} 单笔{A.amount}元')

def handlebar(C):
    """K线处理函数 - 逐K线生效"""
    
    # 1. 跳过历史K线（只在盘中交易）
    if not C.is_last_bar():
        return
    
    # 2. 检查交易时间
    now = datetime.datetime.now()
    now_time = now.strftime('%H%M%S')
    
    # 只在交易时间段执行（9:30-15:00）
    if now_time < '093000' or now_time > '150000':
        return
    
    # 3. 获取账户信息
    account = get_trade_detail_data(A.acct, A.acct_type, 'account')
    if len(account) == 0:
        print(f'账号 {A.acct} 未登录')
        return
    
    account = account[0]
    available_cash = int(account.m_dAvailable)
    
    # 4. 处理未查到的委托
    if A.waiting_list:
        # 查询成交记录
        deals = get_trade_detail_data(A.acct, A.acct_type, 'deal')
        found_list = []
        
        for deal in deals:
            if deal.m_strRemark in A.waiting_list:
                found_list.append(deal.m_strRemark)
        
        # 清理已成交的委托
        A.waiting_list = [i for i in A.waiting_list if i not in found_list]
    
    # 如果还有未查到的委托，暂停报单
    if A.waiting_list:
        print(f"有未查到委托 {A.waiting_list} 暂停报单")
        return
    
    # 5. 获取持仓信息
    holdings = get_trade_detail_data(A.acct, A.acct_type, 'position')
    holdings_dict = {
        f'{i.m_strInstrumentID}.{i.m_strExchangeID}': i.m_nCanUseVolume 
        for i in holdings
    }
    holding_vol = holdings_dict.get(A.stock, 0)
    
    # 6. 获取行情数据
    data = C.get_market_data_ex(
        ['close'],
        [A.stock],
        period='1d',
        count=max(A.line1, A.line2) + 1
    )
    
    close_list = list(data[A.stock].values.flatten())
    
    if len(close_list) < max(A.line1, A.line2) + 1:
        print('行情长度不足')
        return
    
    # 7. 计算均线
    pre_line1 = np.mean(close_list[-A.line1-1:-1])
    pre_line2 = np.mean(close_list[-A.line2-1:-1])
    current_line1 = np.mean(close_list[-A.line1:])
    current_line2 = np.mean(close_list[-A.line2:])
    
    # 8. 交易逻辑
    vol = int(A.amount / close_list[-1] / 100) * 100  # 买入数量
    
    # 买入信号：快线上穿慢线 并且 无持仓
    if (A.amount < available_cash and 
        vol >= 100 and 
        A.stock not in holdings_dict and 
        pre_line1 < pre_line2 and 
        current_line1 > current_line2):
        
        msg = f"双均线实盘 {A.stock} 上穿均线 买入{vol}股"
        passorder(
            A.buy_code,           # 买卖代码
            1101,                 # 价格类型（1101=市价）
            A.acct,               # 账号
            A.stock,              # 品种
            14,                   # 订单类型
            -1,                   # 止价
            vol,                  # 数量
            '双均线实盘',         # 策略名称
            0,                    # 逐K线模式 ← 关键参数
            msg,                  # 备注
            C                     # ContextInfo对象
        )
        print(msg)
        A.waiting_list.append(msg)
    
    # 卖出信号：快线下穿慢线 并且 有持仓
    if (A.stock in holdings_dict and 
        holdings_dict[A.stock] > 0 and 
        pre_line1 > pre_line2 and 
        current_line1 < current_line2):
        
        msg = f"双均线实盘 {A.stock} 下穿均线 卖出{holdings_dict[A.stock]}股"
        passorder(
            A.sell_code,
            1101,
            A.acct,
            A.stock,
            14,
            -1,
            holdings_dict[A.stock],
            '双均线实盘',
            0,                    # 逐K线模式 ← 关键参数
            msg,
            C
        )
        print(msg)
        A.waiting_list.append(msg)
```

### 关键要点

✅ **逐K线模式的特点**：
- 等待K线完成再发单
- 避免频繁报撤
- 适合中期策略

⚠️ **重要参数**：
```python
passorder(..., quicktrade=0)  # ← 0 表示逐K线模式
```

---

## ⚡ 模式二：立即下单模式（quicktrade=2）

### 工作原理

```
handlebar 触发
  ↓
产生交易信号
  ↓
立刻发出委托（无需等待）
  ↓
委托直接到交易所
```

### 代码实现

```python
#coding:gbk

class TradeState:
    """使用全局变量保存状态"""
    def __init__(self):
        self.pending_orders = []    # 待处理委托
        self.executed_orders = []   # 已执行委托

A = TradeState()

def init(C):
    pass

def handlebar(C):
    """立即下单模式"""
    
    # 获取账户信息
    account = get_trade_detail_data('账号', 'STOCK', 'account')
    if not account:
        return
    
    # 交易逻辑
    if buy_signal:
        # 立刻下单
        passorder(
            23,
            1101,
            'account',
            '600000.SH',
            14,
            -1,
            100,
            '立即下单策略',
            2,                # ← 2 表示立即下单模式
            'buy signal',
            C
        )
        
        # 使用全局变量管理状态
        A.pending_orders.append({
            'stock': '600000.SH',
            'side': 'BUY',
            'size': 100
        })
```

### 关键要点

⚠️ **立即下单模式的特点**：
- 立刻发出委托
- 无需等待K线完成
- 频繁报撤可能产生成本

⚠️ **状态管理**：
```python
# ❌ 错误：不能使用 ContextInfo 保存状态
C.order_list = []

# ✅ 正确：使用全局变量保存状态
class TradeState:
    def __init__(self):
        self.order_list = []

A = TradeState()
```

---

## 🔍 第四步：委托管理与查询

### 查询账户状态

```python
def check_account_status(acct, acct_type):
    """查询账户信息"""
    
    # 账户基本信息
    account = get_trade_detail_data(acct, acct_type, 'account')
    if account:
        acc = account[0]
        print(f"可用现金: {acc.m_dAvailable}")
        print(f"总资产: {acc.m_dTotalAsset}")
        print(f"浮动盈亏: {acc.m_dFloatProfit}")
    
    # 持仓信息
    positions = get_trade_detail_data(acct, acct_type, 'position')
    for pos in positions:
        print(f"股票: {pos.m_strInstrumentID}")
        print(f"数量: {pos.m_nVolume}")
        print(f"可用: {pos.m_nCanUseVolume}")
        print(f"成本价: {pos.m_dOpenPrice}")
        print(f"盈亏: {pos.m_dProfit}")
    
    # 委托信息
    orders = get_trade_detail_data(acct, acct_type, 'order')
    for order in orders:
        print(f"委托编号: {order.m_strOrderID}")
        print(f"状态: {order.m_nOrderStatus}")
        print(f"数量: {order.m_nOrderVolume}")
    
    # 成交记录
    deals = get_trade_detail_data(acct, acct_type, 'deal')
    for deal in deals[-10:]:  # 取最后10条
        print(f"成交时间: {deal.m_strTradeTime}")
        print(f"成交价: {deal.m_dTradePrice}")
        print(f"成交量: {deal.m_nTradeVolume}")
    
    return account, positions, orders, deals
```

### 委托状态码

| 状态码 | 说明 |
|------|------|
| 0 | 未报 |
| 1 | 待报 |
| 2 | 已报 |
| 3 | 已撤 |
| 4 | 部成 |
| 5 | 已成 |
| 6 | 废单 |
| 7 | 待撤 |

### 成交查询

```python
def check_trades(acct, acct_type, max_records=20):
    """查询最近的成交记录"""
    
    deals = get_trade_detail_data(acct, acct_type, 'deal')
    
    print(f"最近 {max_records} 笔成交:")
    for deal in deals[-max_records:]:
        print(f"""
        时间: {deal.m_strTradeTime}
        股票: {deal.m_strInstrumentID}.{deal.m_strExchangeID}
        方向: {'买' if deal.m_nTradeDir == 0 else '卖'}
        成交价: {deal.m_dTradePrice}
        成交量: {deal.m_nTradeVolume}
        成交额: {deal.m_nTradeVolume * deal.m_dTradePrice}
        费用: {deal.m_dCommission}
        """)
```

---

## ⚠️ 实盘交易注意事项

### 1. 撮合规则

#### 价格限制
```
股票品种撮合规则：
- 价格不能超过当前价的 2% → 否则废单
- 有涨跌停限制约束
```

#### 数量限制
```
- 委托数量大于可用数量 → 废单
- 必须是100的整数倍（A股规则）
```

### 2. 交易时间

```python
# 股票交易时间
TRADING_HOURS = {
    '沪深A股': ['09:30-11:30', '13:00-15:00'],
    '科创板': ['09:30-11:30', '13:00-15:00'],
    '期货': ['09:00-11:30', '13:00-15:00', '21:00-23:00'],
}

# 需要在交易时间内下单
now_time = datetime.datetime.now().strftime('%H%M%S')
if now_time < '093000' or now_time > '150000':
    print("非交易时间，不下单")
    return
```

### 3. 风险管理

```python
# 设置止损
def set_stop_loss(stock, entry_price, stop_loss_pct):
    """设置止损"""
    stop_price = entry_price * (1 - stop_loss_pct)
    return stop_price

# 设置止盈
def set_take_profit(stock, entry_price, take_profit_pct):
    """设置止盈"""
    profit_price = entry_price * (1 + take_profit_pct)
    return profit_price

# 检查账户风险
def check_daily_loss(initial_cash, current_profit):
    """检查日亏损比例"""
    daily_loss_pct = -current_profit / initial_cash
    if daily_loss_pct > 0.05:  # 亏损超过5%
        print("日亏损超限，停止交易")
        return False
    return True
```

### 4. 委托管理最佳实践

```python
class TradeManager:
    def __init__(self):
        self.pending = []       # 待成交
        self.executed = []      # 已成交
        
    def submit_order(self, passorder_params):
        """提交订单"""
        self.pending.append(passorder_params)
    
    def sync_orders(self, acct, acct_type):
        """同步委托状态"""
        deals = get_trade_detail_data(acct, acct_type, 'deal')
        deal_remarks = [d.m_strRemark for d in deals]
        
        # 从待成交移除已成交
        self.executed = [p for p in self.pending if p in deal_remarks]
        self.pending = [p for p in self.pending if p not in deal_remarks]
    
    def cancel_all(self):
        """取消所有待成交"""
        self.pending = []

tm = TradeManager()
```

---

## 🎯 运行策略

### 在模型交易界面运行

1. **新建策略交易**
   - 点击"新建策略交易"
   - 选择策略文件
   - 选择账号

2. **选择运行模式**
   - **模拟信号模式**：只显示信号，不实际下单
   - **实盘交易模式**：实际发出委托到交易所

3. **启动策略**
   - 检查参数是否正确
   - 点击"启动"或"运行"按钮
   - 监控实时交易

### 监控运行

```
实时显示：
- 交易信号
- 当前持仓
- 可用资金
- 浮动盈亏
- 委托状态
- 成交记录
```

### 停止策略

```
1. 点击"停止"按钮
2. 等待当前委托完成
3. 平仓或持仓至下一个交易日
4. 关闭策略
```

---

## 📊 实盘回顾与优化

### 交易评估

```python
def evaluate_trades(deals):
    """评估交易结果"""
    
    total_trades = len(deals)
    winning_trades = len([d for d in deals if d.m_dProfit > 0])
    win_rate = winning_trades / total_trades if total_trades > 0 else 0
    
    total_profit = sum([d.m_dProfit for d in deals])
    avg_profit = total_profit / total_trades if total_trades > 0 else 0
    
    print(f"总交易数: {total_trades}")
    print(f"胜率: {win_rate*100:.2f}%")
    print(f"总利润: {total_profit:.2f}")
    print(f"平均利润: {avg_profit:.2f}")
```

### 策略改进

```
1. 分析失败交易的原因
2. 调整参数或加入新限制
3. 在模拟模式测试
4. 确认后回到实盘
```

---

## 📚 相关资源

- ✅ [系统概述](./overview.md) - QMT基础
- ✅ [运行机制](./execution-mechanisms.md) - handlebar详解
- ✅ [市场数据API](./market-data-api.md) - 行情函数
- ✅ [交易API](./trading-api.md) - 下单函数  
- ✅ [实盘示例](./examples/live-trading.md) - 完整示例

