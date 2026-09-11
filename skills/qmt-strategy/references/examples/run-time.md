# 定时任务示例：run_time 定时运行

## 使用场景

基于**固定时间间隔**触发函数执行，适合：
- 定时监控市场状态
- 固定时间调整持仓
- 定期检查风险
- 市场加权分析

## 完整代码示例

### 示例1：市场加权涨幅监控

```python
#coding:gbk

import time
import datetime

class MarketState:
    def __init__(self):
        self.hsa = []              # 沪深A股列表
        self.vol_dict = {}         # 成交量字典
        self.bought_list = []      # 已买入列表

A = MarketState()

def init(C):
    """初始化函数"""
    
    print("初始化市场监控策略")
    
    # 1. 获取沪深A股股票列表
    A.hsa = C.get_stock_list_in_sector('沪深A股')
    print(f"获得沪深A股股票 {len(A.hsa)} 只")
    
    # 2. 初始化每只股票的成交量
    for stock in A.hsa:
        A.vol_dict[stock] = C.get_last_volume(stock)
    
    # 3. 启动定时任务
    # 每秒执行一次 market_monitor 函数
    # 从2024-03-13 09:30:00 开始
    C.run_time("market_monitor", "1nSecond", "09:30:00")
    
    print("定时任务已启动")


def market_monitor(C):
    """
    定时执行的监控函数
    这个函数每秒触发一次
    """
    
    # 记录执行时间
    t0 = time.time()
    now = datetime.datetime.now()
    
    # 获取所有股票的最新行情
    full_tick = C.get_full_tick(A.hsa)
    
    total_market_value = 0
    total_ratio = 0
    count = 0
    
    # 遍历所有股票
    for stock in A.hsa:
        try:
            current_price = full_tick[stock]['lastPrice']
            last_close = full_tick[stock]['lastClose']
            
            # 计算涨幅（百分比）
            ratio = current_price / last_close - 1
            
            # 如果涨幅>9% 且 未买入，则买入
            if ratio > 0.09 and stock not in A.bought_list:
                msg = f"{now} {stock} {C.get_stock_name(stock)} 涨幅{ratio*100:.2f}% 买入100股"
                print(msg)
                
                # 这里可以加入实际下单逻辑（暂时注释）
                # passorder(23, 1101, account, stock, 14, -1, 100, 
                #          '定时监控', 2, msg, C)
                
                A.bought_list.append(stock)
            
            # 计算加权涨幅
            market_value = current_price * A.vol_dict[stock]
            total_ratio += ratio * market_value
            total_market_value += market_value
            count += 1
        
        except Exception as e:
            # 某些股票可能无法获取行情（停牌、新上市等）
            continue
    
    # 计算市场加权涨幅
    if total_market_value > 0:
        weighted_ratio = total_ratio / total_market_value * 100
    else:
        weighted_ratio = 0
    
    # 输出市场加权涨幅
    elapsed = round(time.time() - t0, 5)
    print(f'{now} 市场加权涨幅 {weighted_ratio:.2f}% 处理{count}只股票 耗时{elapsed}秒')
```

### 示例2：定时检查持仓

```python
#coding:gbk

import datetime

class PortfolioState:
    def __init__(self):
        self.account = 'testaccount'
        self.account_type = 'STOCK'

P = PortfolioState()

def init(C):
    """初始化"""
    
    # 每分钟检查一次持仓
    C.run_time("check_portfolio", "1nMinute", "09:30:00")
    
    # 每个小时检查一次止损
    C.run_time("check_stoploss", "1nHour", "10:00:00")


def check_portfolio(C):
    """定时检查持仓"""
    
    now = datetime.datetime.now()
    
    # 获取账户信息
    account = get_trade_detail_data(P.account, P.account_type, 'account')
    if not account:
        print(f"[{now}] 账户未登录")
        return
    
    acc = account[0]
    
    # 获取持仓
    positions = get_trade_detail_data(P.account, P.account_type, 'position')
    
    # 输出持仓信息
    print(f"[{now}] ========== 持仓检查 ==========")
    print(f"可用现金: {acc.m_dAvailable / 100:.2f} 元")
    print(f"总资产: {acc.m_dTotalAsset / 100:.2f} 元")
    print(f"浮动盈亏: {acc.m_dFloatProfit / 100:.2f} 元")
    print()
    
    if not positions:
        print("当前无持仓")
    else:
        print("当前持仓:")
        for pos in positions:
            stock = f"{pos.m_strInstrumentID}.{pos.m_strExchangeID}"
            profit_ratio = pos.m_dProfitRatio * 100
            
            print(f"  {stock}: {pos.m_nVolume}股 成本{pos.m_dOpenPrice:.2f} "
                  f"现价{pos.m_dLastPrice:.2f} 盈亏{pos.m_dProfit:.2f} "
                  f"收益率{profit_ratio:.2f}%")


def check_stoploss(C):
    """定时检查止损"""
    
    now = datetime.datetime.now()
    stop_loss_pct = -0.05  # 5%止损
    
    positions = get_trade_detail_data(P.account, P.account_type, 'position')
    
    if not positions:
        return
    
    print(f"[{now}] 检查止损...")
    
    for pos in positions:
        stock = f"{pos.m_strInstrumentID}.{pos.m_strExchangeID}"
        profit_ratio = pos.m_dProfitRatio
        
        # 如果盈亏比超过止损线，执行止损
        if profit_ratio < stop_loss_pct:
            print(f"[{now}] ★ 止损信号: {stock} 亏损{abs(profit_ratio)*100:.2f}%")
            
            # 这里可以加入卖出逻辑
            # passorder(24, 1101, P.account, stock, 14, -1, 
            #          pos.m_nCanUseVolume, '止损', 2, f'{stock}止损卖出', C)
```

### 示例3：交易时段控制

```python
#coding:gbk

import datetime

class TradeControl:
    def __init__(self):
        self.status = False  # 是否允许交易
        self.start_time = '09:30:00'
        self.end_time = '15:00:00'

TC = TradeControl()

def init(C):
    """初始化"""
    
    # 开盘时启用交易
    C.run_time("open_market", "1nSecond", "09:30:00")
    
    # 收盘时禁用交易
    C.run_time("close_market", "1nSecond", "15:00:00")
    
    # 每30秒输出一次市场状态
    C.run_time("check_status", "30nSecond", "09:30:00")


def open_market(C):
    """开盘处理"""
    now = datetime.datetime.now()
    TC.status = True
    print(f"[{now}] ★ 市场开盘 - 允许交易")


def close_market(C):
    """收盘处理"""
    now = datetime.datetime.now()
    TC.status = False
    print(f"[{now}] ★ 市场收盘 - 禁止交易")


def check_status(C):
    """状态检查"""
    now = datetime.datetime.now()
    status_text = "允许交易" if TC.status else "禁止交易"
    print(f"[{now}] 交易状态: {status_text}")
```

---

## run_time 详解

### 函数签名

```python
C.run_time(
    function_name,      # 要执行的函数名称
    time_interval,      # 时间间隔
    start_time         # 起始时间
)
```

### 时间间隔类型

```python
"1nSecond"      # 每1秒执行一次
"5nSecond"      # 每5秒执行一次
"10nSecond"     # 每10秒执行一次
"30nSecond"     # 每30秒执行一次
"60nSecond"     # 每60秒（1分钟）执行一次
"1nMinute"      # 每1分钟执行一次
"5nMinute"      # 每5分钟执行一次
"30nMinute"     # 每30分钟执行一次
"1nHour"        # 每1小时执行一次
```

### 起始时间格式

```python
# 绝对时间（每天的固定时间）
"09:30:00"          # 每天9:30启动
"13:00:00"          # 每天13:00启动
"14:00:00"          # 每天14:00启动

# 立即启动
""                  # 立即启动（推荐用于市场中段）
```

### 常见配置

```python
# 每天开盘时启动
C.run_time("init_func", "1nSecond", "09:30:00")

# 每个交易时段启动
C.run_time("monitor_func", "1nMinute", "09:30:00")

# 盘后定时任务
C.run_time("report_func", "1nSecond", "15:00:00")

# 午间定时任务
C.run_time("lunch_func", "1nSecond", "12:00:00")
```

---

## run_time vs handlebar vs subscribe

| 比较项 | handlebar | subscribe | run_time |
|--------|-----------|-----------|----------|
| **触发条件** | K线完成 | 分笔推送 | 时间到达 |
| **触发频率** | 低（K线周期） | 高（分笔） | 固定（秒/分/小时） |
| **数据粒度** | K线 | 分笔 | 任意 |
| **回测支持** | ✅ | ❌ | ❌ |
| **适用场景** | 中期策略 | 高频交易 | 定时监控 |

### 使用场景对应表

```
需要回测？
├─ 是 → handlebar
└─ 否 → 需要什么频率？
       ├─ 分笔级别 → subscribe
       ├─ K线级别 → handlebar
       └─ 固定间隔 → run_time
```

---

## 性能优化

### 1. 合理设置间隔

```python
# ❌ 间隔太短（系统负担重）
C.run_time("func", "1nSecond", "09:30:00")  # 每秒执行，过于频繁

# ✅ 合理的间隔
C.run_time("func", "5nSecond", "09:30:00")   # 每5秒执行
C.run_time("check", "1nMinute", "09:30:00")  # 每分钟执行
C.run_time("report", "5nMinute", "09:30:00") # 每5分钟执行
```

### 2. 不要在回调中进行阻塞操作

```python
# ❌ 阻塞操作
def slow_monitor(C):
    for i in range(1000000):  # 大量计算
        sqrt(i)
    # 这会导致后续任务延迟

# ✅ 快速返回
def fast_monitor(C):
    # 快速处理
    result = calculate_fast()
    return
```

### 3. 缓存计算结果

```python
class Cache:
    def __init__(self):
        self.stock_list = None
        self.last_update = 0

cache = Cache()

def init(C):
    # 初始化时获取一次
    cache.stock_list = C.get_stock_list_in_sector('沪深A股')


def monitor(C):
    # 使用缓存的列表，无需每次重新获取
    for stock in cache.stock_list:
        pass
```

---

## 常见问题

### Q: 为什么定时任务没有执行？

**A**: 检查：
1. 起始时间是否已到达
2. 函数名称是否正确
3. 时间间隔是否合理
4. 策略是否还在运行

### Q: 如何在交易时间内启动定时任务？

**A**: 
```python
# 方式1：指定开市时间
C.run_time("func", "1nMinute", "09:30:00")

# 方式2：立即启动
C.run_time("func", "1nMinute", "")
```

### Q: 定时任务执行了，但没有看到输出？

**A**: 可能原因：
1. 输出被缓冲
2. 运行在后台线程
3. 需要加 `print()` 并及时刷新

### Q: 能否设置多个定时任务？

**A**: 可以，示例：
```python
def init(C):
    C.run_time("task1", "1nSecond", "09:30:00")
    C.run_time("task2", "5nMinute", "09:30:00")
    C.run_time("task3", "1nHour", "10:00:00")
```

---

## 实战建议

### ✅ 定时任务的最佳用途

- 市场监控（涨幅、跌幅统计）
- 风险管理（定时止损检查）
- 交易时段控制（开盘/收盘处理）
- 性能分析（定时输出统计）
- 重新平衡（定时调整仓位）

### ❌ 不适合用定时任务的场景

- 需要K线聚合的交易
- 需要分笔级别的高频交易
- 需要历史回测
- 需要实时响应的策略

### 💡 组合应用示例

```python
def init(C):
    # handlebar：主要交易逻辑
    # run_time：定时监控
    # subscribe：重要行情监控
    
    # 定时监控宏观指标
    C.run_time("monitor_market", "5nMinute", "09:30:00")
    
    # K线制造交易信号
    handlebar_logic()
    
    # 订阅关键品种
    C.subscribe_quote('000001.SZ', callback=important_callback)
```

---

## 下一步

- 📖 了解 handlebar：[执行机制详解](../execution-mechanisms.md)
- 🔧 了解 subscribe：[事件驱动示例](./subscribe.md)
- 📊 学习最佳实践：[编码规范](../best-practices.md)

