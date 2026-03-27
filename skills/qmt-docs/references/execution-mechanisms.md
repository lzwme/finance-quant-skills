# QMT 运行机制详解

## 📌 三种运行机制概览

QMT系统支持三种运行机制来驱动策略执行：

| 机制 | 驱动方式 | 触发事件 | 主要场景 |
|------|--------|--------|--------|
| **handlebar** | 逐K线驱动 | K线生成 | 回测、盘中模拟K线 |
| **subscribe** | 事件驱动 | 分笔推送 | 实盘分笔交易 |
| **run_time** | 定时任务 | 时间触发 | 定时监控交易 |

---

## 🔄 一、逐K线驱动：handlebar

### 定义与特点

**handlebar** 是主图历史K线加盘中订阅推送的组合。系统会在K线完成时触发 `handlebar` 函数。

### 运行流程

#### 回测模式
```
程序启动
  ↓
执行 init(C) 初始化
  ↓
遍历历史K线（从左向右）
  ↓
每根K线触发一次 handlebar(C)
  ↓
所有K线遍历完成
  ↓
得到回测报告
```

#### 实盘模式
```
程序启动
  ↓
执行 init(C) 初始化
  ↓
历史K线遍历（从左向右）
  ↓
|
+─→ 每根历史K线触发 handlebar(C)
|
+─→ 盘中交易时段
        ↓
      主图品种每个新分笔到达
        ↓
      判断是否形成新K线
        ↓
      新K线首个分笔到达时触发 handlebar(C)
```

### 回测工作原理

#### 时间流转
```
K线完成的定义：
- 分笔时间流转到下一个K线周期的第一个分笔时
- 则判定前一个分笔所在K线已完成
```

#### 撮合规则
```python
# 指定价格在当前K线高低点间
# → 按指定价格撮合

if order_price >= kline_low and order_price <= kline_high:
    execute_price = order_price
    
# 指定价格超过高低点范围
# → 按当前K线收盘价撮合
else:
    execute_price = kline_close

# 委托数量大于可用数量
# → 按可用数量撮合
if order_vol > available:
    final_vol = available
```

### 实盘工作原理

#### 逐K线模式（逐k线生效）

**委托模式参数**：`passorder(..., quicktrade=0)` 或 `quicktrade`不填

**工作流程**：
```
盘中时段（如15:00收盘）
  ↓
主图每个分笔（3秒一次）触发 handlebar
  ↓
handlebar 内产生交易信号
  ↓
系统暂存本次交易信号
  ↓
3秒后下一个分笔到达
  ↓
判断是否为新K线的首个分笔？

─→ 是：前一个分笔为前一根K线最后分笔
    ↓
    将暂存的交易信号发送到交易所
    ↓
    完成交易

─→ 否：当前K线未完成
    ↓
    丢弃暂存的交易信号
    ↓
    继续等待
```

**示例**（1分钟K线）：
```
每根1分钟K线内有20个分笔（每个分笔3秒）
  ↓
前19个分笔产生的信号 → 被丢弃
  ↓
最后（第20个）分笔的信号 → 在下一个K线首笔时延迟3秒发出
```

#### 立即下单模式（立刻执行）

**委托模式参数**：`passorder(..., quicktrade=2)`

**工作流程**：
```
handlebar 内产生交易信号
  ↓
立刻发出委托到交易所
  ↓
无需等待K线完成
  ↓
无需保存在 ContextInfo
```

**状态管理**：
- ❌ 不能使用 `ContextInfo` 的属性保存状态
- ✅ 使用全局变量（全局 Class 或 dict）保存委托状态

### 代码模板

```python
#coding:gbk

def init(C):
    # 初始化策略参数
    C.stock = C.stockcode + '.' + C.market  # 主图品种
    C.period = '1d'                         # 周期
    C.line1 = 10                            # 快线参数
    C.line2 = 20                            # 慢线参数
    C.accountid = "test_account"            # 账号

def handlebar(C):
    # 获取当前K线时间
    bar_date = timetag_to_datetime(C.get_bar_timetag(C.barpos), '%Y%m%d%H%M%S')
    
    # 获取历史行情数据（回测用 subscribe=False，实盘用 subscribe=True）
    local_data = C.get_market_data_ex(
        ['close'],
        [C.stock],
        end_time=bar_date,
        period=C.period,
        count=max(C.line1, C.line2),
        subscribe=False  # 回测使用False
    )
    
    # 处理数据
    close_list = list(local_data[C.stock].iloc[:, 0])
    
    if len(close_list) < max(C.line1, C.line2):
        print(bar_date, '行情不足')
        return
    
    # 计算指标
    line1_mean = round(np.mean(close_list[-C.line1:]), 2)
    line2_mean = round(np.mean(close_list[-C.line2:]), 2)
    
    # 交易逻辑
    if line1_mean > line2_mean:
        # 生成买入信号
        passorder(23, 1101, C.accountid, C.stock, 5, -1, 100, C)
    elif line1_mean < line2_mean:
        # 生成卖出信号
        passorder(24, 1101, C.accountid, C.stock, 5, -1, 100, C)
```

---

## 📮 二、事件驱动：subscribe 订阅推送

### 定义与特点

**subscribe** 是盘中订阅指定品种的分笔数据，当新分笔到达时，触发指定的回调函数。

### 运行流程

```
程序启动
  ↓
执行 init(C) 初始化
  ↓
订阅指定品种（C.subscribe_quote）
  ↓
盘中新分笔到达
  ↓
触发回调函数（callback_func）
  ↓
回调函数内进行交易判断
  ↓
执行下单操作
```

### 特点与限制

✅ **优点**
- 分笔级别的实时反应
- 适合高频或需要分笔的策略
- 推送驱动，无需轮询

❌ **限制**
- 只支持实盘（不支持回测）
- 无法模拟历史K线

### 回调函数工作原理

#### 数据结构
```python
def callback_func(data):
    """
    data: 字典类型
    {
        '600000.SH': {
            'close': 10.5,
            'preClose': 10.4,
            'high': 10.6,
            'low': 10.3,
            ...
        },
        '000001.SZ': {
            ...
        }
    }
    """
    for stock in data:
        current_price = data[stock]['close']
        pre_price = data[stock]['preClose']
        # 处理交易逻辑
```

### 代码模板

```python
#coding:gbk

class TradeState:
    def __init__(self):
        self.bought_list = []

A = TradeState()

def init(C):
    def callback_func(data):
        """每个分笔数据到达时触发"""
        for stock in data:
            current_price = data[stock]['close']
            pre_price = data[stock]['preClose']
            ratio = current_price / pre_price - 1
            
            if ratio > 0.05 and stock not in A.bought_list:
                msg = f"{stock} 涨幅 {ratio*100:.2f}% 买入100股"
                passorder(23, 1101, 'account', stock, 14, -1, 100, msg, 2, msg, C)
                A.bought_list.append(stock)
    
    # 订阅多个品种
    stock_list = ['600000.SH', '000001.SZ']
    for stock in stock_list:
        C.subscribe_quote(stock, period='1d', callback=callback_func)
```

### 与 handlebar 的关系

```
handlebar（实盘）
  ↓
分笔触发
  ↓
如果是新K线首笔
  ↓
触发 handlebar 函数
  
---

subscribe
  ↓
分笔到达
  ↓
立即触发回调函数
  ↓
无需等待K线完成
```

---

## ⏰ 三、定时任务：run_time 定时运行

### 定义与特点

**run_time** 指定固定的时间间隔或具体时间，持续触发指定的回调函数。

### 运行流程

```
程序启动
  ↓
执行 init(C) 初始化
  ↓
C.run_time() 启动定时任务
  ↓
按指定时间间隔定时触发
  ↓
执行定时函数
  ↓
继续循环触发
```

### 时间间隔指定

#### 格式
```python
C.run_time("function_name", "time_interval", "start_time")
```

#### 时间间隔类型
```python
"1nSecond"      # 每1秒触发一次
"5nSecond"      # 每5秒触发一次
"60nSecond"     # 每60秒触发一次
"1nMinute"      # 每1分钟触发一次
"1nHour"        # 每1小时触发一次
```

#### 起始时间格式
```python
"2019-10-14 13:20:00"   # 指定日期和时间
"13:20:00"              # 仅指定时间（每天）
"20:30:00"              # 盘后的定时任务
```

### 代码模板

```python
#coding:gbk
import time, datetime

class MarketState:
    def __init__(self):
        self.hsa = []              # 沪深A股列表
        self.vol_dict = {}         # 成交量字典
        self.bought_list = []      # 已买入列表

A = MarketState()

def init(C):
    # 获取沪深A股列表
    A.hsa = C.get_stock_list_in_sector('沪深A股')
    
    # 初始化每只股票的成交量
    for stock in A.hsa:
        A.vol_dict[stock] = C.get_last_volume(stock)
    
    # 启动定时任务：每秒触发一次，从当前时间开始
    C.run_time("market_monitor", "1nSecond", "")

def market_monitor(C):
    """定时执行的监控函数"""
    now = datetime.datetime.now()
    
    # 获取所有股票的最新行情
    full_tick = C.get_full_tick(A.hsa)
    
    total_market_value = 0
    total_ratio = 0
    
    for stock in A.hsa:
        last_price = full_tick[stock]['lastPrice']
        last_close = full_tick[stock]['lastClose']
        ratio = last_price / last_close - 1
        
        # 涨幅超过5%则买入
        if ratio > 0.05 and stock not in A.bought_list:
            msg = f"{now} {stock} 涨幅 {ratio*100:.2f}% 买入100股"
            # passorder(23, 1101, account, stock, 14, -1, 100, msg, 2, msg, C)
            A.bought_list.append(stock)
        
        # 计算加权涨幅
        market_value = last_price * A.vol_dict[stock]
        total_ratio += ratio * market_value
        total_market_value += market_value
    
    # 输出市场加权涨幅
    market_ratio = (total_ratio / total_market_value * 100) if total_market_value > 0 else 0
    print(f'{now} 市场加权涨幅 {market_ratio:.2f}%')
```

### 常见时间设置

```python
# 每天9:30开盘时准备
C.run_time("prepare", "1nSecond", "09:30:00")

# 盘中每分钟检查一次
C.run_time("check_market", "1nMinute", "09:30:00")

# 每天15:00收盘后平仓
C.run_time("close_position", "1nSecond", "15:00:00")

# 每30秒调整仓位
C.run_time("rebalance", "30nSecond", "")
```

---

## 📊 三种机制对比表

### 功能对比

| 功能 | handlebar | subscribe | run_time |
|------|-----------|-----------|----------|
| 回测支持 | ✅ | ❌ | ❌ |
| 实盘支持 | ✅ | ✅ | ✅ |
| K线级别驱动 | ✅ | ❌ | ❌ |
| 分笔级别驱动 | ✅ | ✅ | ❌ |
| 定时驱动 | ❌ | ❌ | ✅ |
| K线自动拼接 | ✅ | ❌ | ❌ |

### 适用场景

| 场景 | 推荐机制 | 理由 |
|------|--------|------|
| 历史策略回测 | handlebar | 同时支持历史K线遍历 |
| 盘中模拟K线 | handlebar | 模拟逐K线效果 |
| 分笔实时交易 | subscribe | 响应分笔推送 |
| 定时监控 | run_time | 固定时间间隔触发 |
| 高频策略 | subscribe + run_time | 分笔级别控制 |
| 均衡策略 | handlebar | 稳定逐K线执行 |

### 性能对比

| 指标 | handlebar | subscribe | run_time |
|------|-----------|-----------|----------|
| 回测速度 | 🟢 快 | ❌ 不支持 | ❌ 不支持 |
| 实盘反应 | 🟡 中等 | 🟢 快 | 🟡 中等 |
| CPU占用 | 🟡 中等 | 🟡 中等 | 🟢 低 |
| 代码复杂度 | 🟡 中等 | 🟢 简单 | 🟢 简单 |

---

## 🔗 机制选择决策树

```
选择运行机制
  │
  ├─ 需要回测历史数据？
  │  ├─ 是 → 🎯 选择 handlebar
  │  │        运行流程：[回测模型指南](./backtesting-guide.md)
  │  │
  │  └─ 否 → 需要实时响应？
  │         ├─ 是 → 需要什么粒度？
  │         │      ├─ K线粒度 → 🎯 选择 handlebar
  │         │      │             运行流程：[实盘交易指南](./live-trading-guide.md)
  │         │      │
  │         │      └─ 分笔粒度 → 🎯 选择 subscribe
  │         │                      运行流程：[事件驱动示例](./examples/subscribe.md)
  │         │
  │         └─ 否 → 需要定时执行？
  │                ├─ 是 → 🎯 选择 run_time
  │                │        运行流程：[定时任务示例](./examples/run-time.md)
  │                │
  │                └─ 否 → 需要咨询业务需求
```

---

## 💡 常见问题

### Q: handlebar 实盘为什么分笔24个而不是20个？
A: 不同交易时段分笔数不同。1分钟内的分笔数取决于交易活跃度，没有固定值。

### Q: subscribe 回调函数在哪个线程执行？
A: 在推送线程执行，如进行复杂计算，建议在线程安全的前提下操作全局变量。

### Q: handlebar、subscribe、run_time 能否同时使用？
A: 可以。但需注意状态管理，避免竞态条件。

### Q: 怎样判断是否为新K线形成？
A: 通过 `C.get_bar_timetag()` 获取K线时间戳，比较是否与上次不同。

---

## 📚 相关资源

- ✅ [实盘交易指南](./live-trading-guide.md) - handlebar实盘模式
- ✅ [回测模型指南](./backtesting-guide.md) - handlebar回测模式
- ✅ [事件驱动示例](./examples/subscribe.md) - subscribe使用示例
- ✅ [定时任务示例](./examples/run-time.md) - run_time使用示例

