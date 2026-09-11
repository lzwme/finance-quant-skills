# 事件驱动示例：subscribe 订阅推送

## 使用场景

基于**分笔数据实时推送**而不是K线驱动，适合：
- 分笔级别的高频交易
- 需要实时响应行情变化的策略
- 不需要K线聚合的即时交易

## 完整代码示例

### 示例1：涨停追买策略

```python
#coding:gbk

import datetime

class TradeState:
    def __init__(self):
        self.bought_list = []      # 已买入的股票列表
        self.stock_list = []       # 监控的股票列表

A = TradeState()

def init(C):
    """
    初始化函数
    
    在这个函数中定义回调函数并订阅行情
    """
    
    # 获取沪深A股股票列表
    A.stock_list = C.get_stock_list_in_sector('沪深A股')
    print(f"监控股票数: {len(A.stock_list)}")
    
    # 定义行情更新的回调函数
    def on_quote(data):
        """
        每当有新分笔数据到达时，触发此函数
        
        参数 data: 字典，格式如下
        {
            '600000.SH': {
                'close': 10.5,      # 最新价
                'preClose': 10.0,   # 前收盘
                'high': 10.8,
                'low': 10.2,
                ...
            },
            '000001.SZ': { ... }
        }
        """
        
        now = datetime.datetime.now()
        
        # 遍历所有推送的股票
        for stock in data:
            current_price = data[stock]['close']
            pre_close = data[stock]['preClose']
            
            # 计算涨幅
            rise_ratio = current_price / pre_close - 1
            
            # 跳过已买入的股票
            if stock in A.bought_list:
                continue
            
            # 打印较大涨幅的股票
            if rise_ratio > 0.05:  # 涨幅>5%
                print(f"[{now}] {stock} 涨幅{rise_ratio*100:.2f}% 当前价{current_price}")
                
                # 如果涨幅>10%，考虑买入
                if rise_ratio > 0.1:
                    print(f"[{now}] ★ 买入信号: {stock} 涨幅{rise_ratio*100:.2f}%")
                    
                    # 这里可以加入实际下单逻辑
                    # passorder(23, 1101, account, stock, 14, -1, 100, 
                    #          '涨停追买', 2, f'{stock}买入', C)
                    
                    A.bought_list.append(stock)
    
    # 订阅所有股票的行情推送
    for stock in A.stock_list:
        C.subscribe_quote(
            stock,
            period='1d',           # 日线周期
            callback=on_quote      # 回调函数
        )
    
    print(f"已订阅{len(A.stock_list)}只股票的行情推送")
```

### 示例2：价格突破策略

```python
#coding:gbk

import datetime

class TradeState:
    def __init__(self):
        self.key_prices = {}       # 关键价格
        self.bought_list = []      # 已买入

A = TradeState()

def init(C):
    """初始化"""
    
    # 定义关键价格
    key_stocks = ['600000.SH', '000001.SZ', '000002.SZ']
    for stock in key_stocks:
        A.key_prices[stock] = 10.0  # 设置关键价格为10元
    
    def on_quote(data):
        """回调函数 - 处理行情数据"""
        
        for stock in data:
            if stock not in A.key_prices:
                continue
            
            current_price = data[stock]['close']
            key_price = A.key_prices[stock]
            
            # 如果价格突破关键价格，发出信号
            if current_price > key_price and stock not in A.bought_list:
                print(f"[{datetime.datetime.now()}] {stock} 突破{key_price}元 当前{current_price}元")
                
                # 标记为已买入
                A.bought_list.append(stock)
    
    # 订阅关键股票
    for stock in A.key_prices.keys():
        C.subscribe_quote(stock, callback=on_quote)
```

### 示例3：跌幅选股策略

```python
#coding:gbk

import datetime

class TradeState:
    def __init__(self):
        self.watch_list = []

A = TradeState()

def init(C):
    """初始化"""
    
    # 获取所有股票
    all_stocks = C.get_stock_list_in_sector('沪深A股')
    
    def on_quote(data):
        """处理行情推送"""
        
        for stock in data:
            current_price = data[stock]['close']
            pre_close = data[stock]['preClose']
            
            # 计算跌幅
            fall_ratio = (1 - current_price / pre_close)
            
            # 跌幅>5%的股票
            if fall_ratio > 0.05:
                if stock not in A.watch_list:
                    print(f"[{datetime.datetime.now()}] {stock} 跌幅{fall_ratio*100:.2f}% 当前价{current_price}")
                    A.watch_list.append(stock)
    
    # 订阅行情
    for stock in all_stocks[:50]:  # 只订阅前50只以减少系统负担
        C.subscribe_quote(stock, callback=on_quote)
```

---

## 回调函数详解

### 回调函数签名

```python
def callback_func(data):
    """
    行情推送回调函数
    
    参数:
        data (dict): 本次推送的行情数据
        
    数据结构:
    {
        '600000.SH': {
            'lastPrice': 10.5,      # 最新价
            'lastClose': 10.4,      # 前收盘
            'open': 10.3,           # 今开
            'high': 10.6,           # 今高
            'low': 10.2,            # 今低
            'volume': 1000000,      # 成交量
            'amount': 10500000,     # 成交额
            'bid': 10.49,           # 买价
            'ask': 10.51,           # 卖价
            'bidVol': 10000,        # 买量
            'askVol': 5000,         # 卖量
            'close': 10.5,          # 收盘（等同于lastPrice）
            'preClose': 10.4,       # 前收（同lastClose）
        },
        # 其他股票数据...
    }
    """
    pass
```

### 回调函数执行线程

- ✅ 在行情推送线程中执行
- ⚠️ 如进行复杂计算，注意时间不要过长
- ⚠️ 访问全局变量时要注意线程安全

---

## subscribe vs handlebar 对比

| 方面 | subscribe | handlebar |
|------|-----------|-----------|
| **触发条件** | 分笔推送 | K线完成 |
| **数据粒度** | 分笔级别 | K线级别 |
| **回测支持** | ❌ 否 | ✅ 是 |
| **实盘支持** | ✅ 是 | ✅ 是 |
| **反应速度** | 🟢 快（秒级） | 🟡 中等（分钟级） |
| **使用场景** | 高频交易 | 中期策略 |
| **复杂度** | 🟡 中等 | 🟢 相对简单 |

---

## 性能优化建议

### 1. 限制订阅数量

```python
# ❌ 订阅所有股票（系统负担重）
all_stocks = C.get_stock_list_in_sector('沪深A股')  # 3000+只
for stock in all_stocks:
    C.subscribe_quote(stock, callback=on_quote)

# ✅ 只订阅关键股票
key_stocks = ['600000.SH', '000001.SZ', '000002.SZ']
for stock in key_stocks:
    C.subscribe_quote(stock, callback=on_quote)
```

### 2. 回调函数要轻量化

```python
# ❌ 回调中进行复杂计算
def on_quote(data):
    for stock in data:
        # 复杂的算法计算
        for i in range(10000):
            sqrt(i)
            # ...

# ✅ 只处理必要信息
def on_quote(data):
    for stock in data:
        price = data[stock]['close']
        
        # 简单的判断
        if price > 10:
            # 标记或记录
            pass
```

### 3. 避免重复评估

```python
# ❌ 每次推送都重新计算
def on_quote(data):
    stock_list = C.get_stock_list_in_sector('沪深A股')  # 重复计算
    
    for stock in data:
        if stock in stock_list:
            pass

# ✅ 初始化一次，缓存使用
A.stock_list = C.get_stock_list_in_sector('沪深A股')  # 初始化时计算一次

def on_quote(data):
    for stock in data:
        if stock in A.stock_list:
            pass
```

---

## 与立即下单模式(quicktrade=2)

subscribe 通常与 **立即下单模式** 结合使用：

```python
def on_quote(data):
    for stock in data:
        price = data[stock]['close']
        
        if should_buy(price):
            # 立即下单
            passorder(
                23, 1101, account, stock, 14, -1, 100,
                'subscribe策略',
                2,                # ← 立即下单（不等待K线）
                f'{stock}-buy',
                C
            )
```

需要使用**全局变量**来保存订单状态，而不是 ContextInfo。

---

## 常见问题

### Q: 回调函数为什么没有被调用？

**A**: 检查：
1. 是否成功订阅（打印日志确认）
2. 是否在实盘时段（交易时间内）
3. 股票代码格式是否正确
4. 行情是否有推送

### Q: 如何取消订阅？

**A**: subscribe 没有取消机制，需要：
1. 重新启动策略
2. 或使用 handlebar 替代

### Q: 为什么体验到行情延迟？

**A**: 可能原因：
1. 网络延迟
2. 订阅数量过多
3. 回调函数执行时间太长

---

## 实战建议

✅ **推荐使用 subscribe 的场景**：
- 需要分笔级别的数据
- 高频交易
- 分笔显示的策略

❌ **不推荐使用 subscribe 的场景**：
- 需要K线聚合
- 需要回测验证
- 中期策略

💡 **最佳实践**：
- 先用 handlebar + 回测验证策略逻辑
- 再用 subscribe 进行高频优化
- 或者两种机制结合使用

---

## 下一步

- 📖 了解 handlebar：[执行机制详解](../execution-mechanisms.md#一逐k线驱动handlebar)
- 🔧 立即下单模式：[实盘交易指南](../live-trading-guide.md#⚡-模式二立即下单模式quicktrade2)
- 定时任务示例：[定时任务示例](./run-time.md)

