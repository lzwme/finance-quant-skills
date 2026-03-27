# 实盘示例：双均线策略

## 完整的实盘交易代码示例

### 策略描述

这是一个基于双均线的实盘交易策略：
- **运行方式**：逐K线模式（handlebar）
- **委托模式**：逐K线生效（quicktrade=0）
- **交易时间**：09:30-15:00
- **风险管理**：未查到的委托会暂停后续报单

### 完整代码

```python
#coding:gbk

import pandas as pd
import numpy as np
import datetime

# ===== 全局变量 =====
class TradeState:
    """交易状态管理（仅限于逐K线模式）"""
    def __init__(self):
        self.stock = None
        self.acct = None                    # 账号
        self.acct_type = None               # 账户类型
        self.amount = 10000                 # 单笔买入金额
        self.line1 = 17                     # 快线周期
        self.line2 = 27                     # 慢线周期
        self.waiting_list = []              # 未查到成交的委托列表
        self.buy_code = 23                  # 买入代码
        self.sell_code = 24                 # 卖出代码

A = TradeState()


# ===== 初始化函数 =====
def init(C):
    """
    策略初始化函数
    参数 C: ContextInfo 对象
    """
    
    # 获取策略参数
    A.stock = C.stockcode + '.' + C.market         # 交易品种
    A.acct = account                               # 模型交易界面选择的账号
    A.acct_type = accountType                      # 账户类型（STOCK/CREDIT）
    
    # 设置策略参数
    A.line1 = 17    # 快线周期
    A.line2 = 27    # 慢线周期
    
    # 设置买卖代码（区分股票和两融账户）
    if A.acct_type == 'STOCK':
        A.buy_code = 23
        A.sell_code = 24
    else:  # CREDIT
        A.buy_code = 33
        A.sell_code = 34
    
    print(f"双均线实盘策略初始化")
    print(f"  品种: {A.stock}")
    print(f"  账号: {A.acct}")
    print(f"  账户类型: {A.acct_type}")
    print(f"  单笔金额: {A.amount} 元")


# ===== K线处理函数 =====
def handlebar(C):
    """
    K线处理函数 - 逐K线模式
    
    实盘中：
    1. 历史K线遍历一遍
    2. 盘中时：主图每个分笔触发一次
    3. 新K线首笔时，发送前一个K线暂存的委托
    """
    
    # ========== 1. 跳过历史K线 ==========
    # 只处理最后一根K线（盘中当前K线）
    if not C.is_last_bar():
        return
    
    # ========== 2. 检查交易时间 ==========
    now = datetime.datetime.now()
    now_time = now.strftime('%H%M%S')
    
    # 只在交易时间段执行（9:30-15:00）
    if now_time < '093000' or now_time > '150000':
        print(f"[{now}] 非交易时间，跳过")
        return
    
    # ========== 3. 获取账户信息 ==========
    account = get_trade_detail_data(A.acct, A.acct_type, 'account')
    if len(account) == 0:
        print(f"[{now}] 错误：账号 {A.acct} 未登录")
        return
    
    account = account[0]
    available_cash = int(account.m_dAvailable)
    
    # ========== 4. 处理未查到的委托 ==========
    if A.waiting_list:
        # 查询最新的成交记录
        deals = get_trade_detail_data(A.acct, A.acct_type, 'deal')
        found_list = []
        
        # 找出已成交的委托
        for deal in deals:
            if deal.m_strRemark in A.waiting_list:
                found_list.append(deal.m_strRemark)
        
        # 从待查列表中移除已成交的
        A.waiting_list = [i for i in A.waiting_list if i not in found_list]
    
    # 如果还有未查到的委托，暂停报单
    if A.waiting_list:
        print(f"[{now}] 有未查到的委托 {A.waiting_list} - 暂停报单")
        return
    
    # ========== 5. 获取持仓信息 ==========
    holdings = get_trade_detail_data(A.acct, A.acct_type, 'position')
    holdings_dict = {}
    for pos in holdings:
        stock_code = f'{pos.m_strInstrumentID}.{pos.m_strExchangeID}'
        holdings_dict[stock_code] = pos.m_nCanUseVolume
    
    holding_vol = holdings_dict.get(A.stock, 0)
    
    # ========== 6. 获取行情数据 ==========
    # 实盘使用 subscribe=True 获取实时数据
    data = C.get_market_data_ex(
        ['close'],
        [A.stock],
        period='1d',
        count=max(A.line1, A.line2) + 1,
        subscribe=True  # ← 实盘使用 True
    )
    
    close_list = list(data[A.stock].values.flatten())
    
    # 检查数据长度
    if len(close_list) < max(A.line1, A.line2) + 1:
        print(f"[{now}] 行情长度不足（新上市或停牌）")
        return
    
    # ========== 7. 计算均线 ==========
    # 前一个K线的均线
    pre_line1 = np.mean(close_list[-A.line1-1:-1])
    pre_line2 = np.mean(close_list[-A.line2-1:-1])
    
    # 当前K线的均线
    current_line1 = np.mean(close_list[-A.line1:])
    current_line2 = np.mean(close_list[-A.line2:])
    
    current_price = close_list[-1]
    
    # ========== 8. 计算买入数量 ==========
    vol = int(A.amount / current_price / 100) * 100  # 向下取整到100的倍数
    
    # ========== 9. 买入信号 - 金叉 ==========
    # 条件：前期快线<慢线，当前快线>慢线（金叉），并且未持仓
    if (A.amount < available_cash and 
        vol >= 100 and 
        A.stock not in holdings_dict and 
        pre_line1 < pre_line2 and 
        current_line1 > current_line2):
        
        msg = f"双均线实盘 {A.stock} 上穿均线 买入{vol}股"
        print(f"[{now}] ★ 买入信号: {msg}")
        
        # 下单 - 逐K线模式（quicktrade=0）
        passorder(
            A.buy_code,                     # 买入代码
            1101,                           # 市价单
            A.acct,                         # 账号
            A.stock,                        # 品种
            14,                             # 订单类型
            -1,                             # 止价
            vol,                            # 数量
            '双均线实盘',                   # 策略名称
            0,                              # ← 逐K线模式（等待K线完成）
            msg,                            # 备注
            C                               # ContextInfo
        )
        
        # 加入待查询列表
        A.waiting_list.append(msg)
    
    # ========== 10. 卖出信号 - 死叉 ==========
    # 条件：前期快线>慢线，当前快线<慢线（死叉），并且有持仓
    if (A.stock in holdings_dict and 
        holdings_dict[A.stock] > 0 and 
        pre_line1 > pre_line2 and 
        current_line1 < current_line2):
        
        msg = f"双均线实盘 {A.stock} 下穿均线 卖出{holdings_dict[A.stock]}股"
        print(f"[{now}] ★ 卖出信号: {msg}")
        
        # 下单 - 逐K线模式（quicktrade=0）
        passorder(
            A.sell_code,                    # 卖出代码
            1101,                           # 市价单
            A.acct,                         # 账号
            A.stock,                        # 品种
            14,                             # 订单类型
            -1,                             # 止价
            holdings_dict[A.stock],         # 数量
            '双均线实盘',                   # 策略名称
            0,                              # ← 逐K线模式
            msg,                            # 备注
            C                               # ContextInfo
        )
        
        # 加入待查询列表
        A.waiting_list.append(msg)
```

### 如何运行此策略

#### 1. 准备工作

- ✅ 确保账户已登录
- ✅ 选择交易品种作为主图
- ✅ 确保有足够的资金

#### 2. 配置策略

在模型交易界面：

| 设置 | 值 |
|------|-----|
| 策略选择 | 选择这个代码文件 |
| 品种 | 选择要交易的股票 |
| 账号 | 选择已用账号（如模拟账号） |
| 运行模式 | 先选"模拟信号"测试，再选"实盘"交易 |

#### 3. 模拟信号模式（推荐先试）

```
模型交易 → 新建策略 → 选择策略和账号
→ 运行模式选择"模拟信号模式"
→ 点击"启动"
```

效果：显示交易信号但不实际下单，用于验证逻辑

#### 4. 实盘模式（验证无误后）

```
模型交易 → 选择同一个策略
→ 运行模式选择"实盘交易模式"
→ 点击"启动"
```

效果：实际发送委托到交易所

### 实盘运行示例输出

```
双均线实盘策略初始化
  品种: 600000.SH
  账号: 888888
  账户类型: STOCK
  单笔金额: 10000 元

[2024-03-13 10:30:15] 非交易时间，跳过
...
[2024-03-13 09:30:15] ★ 买入信号: 双均线实盘 600000.SH 上穿均线 买入1049股
...
[2024-03-13 13:45:30] ★ 卖出信号: 双均线实盘 600000.SH 下穿均线 卖出1049股
```

### 关键要点

#### 1. 逐K线模式的特点

- ✅ 等待K线完成再发单
- ✅ 避免频繁报撤
- ✅ 与回测逻辑一致

#### 2. 状态管理

- ✅ 使用全局变量管理状态（TradeState类）
- ✅ 记录待查询的委托（waiting_list）
- ✅ 新K线首笔时发送前一个K线的信号

#### 3. 风险管理

- ✅ 只在交易时间段执行
- ✅ 检查账户是否登录
- ✅ 检查资金是否足够
- ✅ 检查持仓是否足够

### 参数优化

#### 增加止损

```python
# 添加止损价格检查
stop_loss_pct = 0.03  # 3%止损

if holding_vol > 0:
    current_price = close_list[-1]
    # 获取持仓成本价
    pos_cost = ...  # 从持仓信息获取
    
    if current_price < pos_cost * (1 - stop_loss_pct):
        # 执行止损
        passorder(A.sell_code, 1101, A.acct, A.stock, 14, -1, holding_vol, ...)
```

#### 调整资金管理

```python
# 改为按可用资金的百分比
volume_pct = 0.8  # 使用80%的资金
vol = int(available_cash * volume_pct / current_price / 100) * 100
```

### 常见问题

#### Q: 为什么没有委托信号出现？

**A**: 检查：
1. 是否在交易时间段（09:30-15:00）
2. 账户是否已登录
3. 是否进入了金叉/死叉条件
4. C.is_last_bar() 是否返回 True

#### Q: 委托为什么一直没成交？

**A**: 可能原因：
1. 价格超出2%笼子
2. 数量不是100的倍数
3. 账户无可用现金或持仓

#### Q: 如何在逐K线模式下停止策略？

**A**: 操作步骤：
1. 点击"停止"按钮
2. 等待当前委托完成
3. 关闭策略

---

## 与回测的对比

| 维度 | 回测 | 实盘 |
|------|------|------|
| subscribe | False | True |
| is_last_bar() | 无需检查 | 需要检查 |
| 交易时间 | 无限制 | 09:30-15:00 |
| 账户 | 虚拟 | 真实/模拟 |
| 委托等待 | 无 | 需要 |
| 成交查询 | 自动 | 需要手动查询 |

---

## 下一步

- 📖 了解逐K线模式：[运行机制详解](../execution-mechanisms.md)
- 🔧 优化策略：[最佳实践](../best-practices.md)
- 📊 学习事件驱动：[事件驱动示例](./subscribe.md)

