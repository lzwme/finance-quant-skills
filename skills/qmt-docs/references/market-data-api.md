# QMT 市场数据API 完全参考

## 📊 行情数据函数总览

| 函数 | 用途 | 返回类型 | 场景 |
|------|------|--------|------|
| `get_market_data_ex` | 获取K线历史数据 | DataFrame | 回测、指标计算 |
| `get_full_tick` | 获取最新行情tick | dict | 实盘行情 |
| `subscribe_quote` | 订阅行情推送 | 回调 | 实盘事件驱动 |
| `get_last_volume` | 获取最后成交量 | int | 市场分析 |
| `get_stock_list_in_sector` | 获取板块股票列表 | list | 选股 |
| `get_stock_name` | 获取股票名称 | str | 信息显示 |

---

## 🔄 一、get_market_data_ex - 历史数据获取

### 函数签名

```python
get_market_data_ex(
    fields,                 # [位置参数] 字段列表 - 必须用位置参数，不能用 fields=
    stocks,                 # [位置参数] 股票列表 - 必须用位置参数，不能用 stocks=
    end_time=None,          # [命名参数] 数据截止时间
    period=None,            # [命名参数] K线周期 
    count=None,             # [命名参数] 数据条数
    subscribe=True/False    # [命名参数] 是否订阅
)
```

⚠️ **重要提示**：前两个参数 `fields` 和 `stocks` **必须用位置参数**，不能写成 `fields=...` 或 `stocks=...`

### 参数详解

#### 1. fields - 字段列表

可获取的字段：

```python
# 基础字段
fields = [
    'open',         # 开盘价
    'close',        # 收盘价
    'high',         # 最高价
    'low',          # 最低价
    'volume',       # 成交量
    'amount',       # 成交额
]

# 完整字段示例
data = C.get_market_data_ex(
    ['open', 'close', 'high', 'low', 'volume', 'amount'],
    ['600000.SH'],
    end_time='20190101',
    period='1d',
    count=100
)
```

#### ✅ 正确用法 vs ❌ 错误用法

```python
# ✅ 正确 - 用位置参数
data = C.get_market_data_ex(['close'], [C.stock], count=100, subscribe=False)

# ❌ 错误 - 不能用命名参数 fields= 和 stocks=
data = C.get_market_data_ex(fields=['close'], stocks=[C.stock], count=100)
```

#### 2. stocks - 股票列表

```python
# 单个股票
stocks = ['600000.SH']

# 多个股票
stocks = ['600000.SH', '000001.SZ', '000858.SZ']

# 股票代码格式
# SH - 上海交易所
# SZ - 深圳交易所
```

#### 3. end_time - 数据截止时间

```python
# 日期格式
end_time = '20190101'       # YYYYMMDD

# 日期时间格式
end_time = '20190101093000'  # YYYYMMDDHHmmss

# 在 handlebar 中使用
bar_date = timetag_to_datetime(C.get_bar_timetag(C.barpos), '%Y%m%d%H%M%S')
data = C.get_market_data_ex(..., end_time=bar_date)
```

#### 4. period - K线周期

```python
# 分钟级别
period = '1m'       # 1分钟
period = '5m'       # 5分钟
period = '15m'      # 15分钟
period = '30m'      # 30分钟

# 日线及以上
period = '1d'       # 日线（默认）
period = '1w'       # 周线
period = '1m'       # 月线（与handle中的'1m'冲突，需要注意）

# 在代码中使用
period = C.period   # 获取当前K线周期
```

#### 5. count - 数据条数

```python
# 指定条数
count = 100         # 获取最近100根K线
count = 250         # 获取最近250根K线

# 与 max() 结合使用
count = max(C.line1, C.line2)  # 取两个参数中的最大值
```

#### 6. subscribe - 订阅参数（关键！）

```python
# ✅ 回测使用 False（本地数据）
subscribe = False
# 不需要向服务器订阅，直接读取本地数据
# 速度快，适合回测历史K线

# ✅ 实盘使用 True（实时数据）
subscribe = True
# 向服务器订阅实时行情，获取盘中最新数据
# 适合实盘交易

# 判断场景
if is_backtest:
    subscribe = False
else:
    subscribe = True
```

### 返回数据结构

```python
# 返回类型：pandas DataFrame
data = C.get_market_data_ex(['close'], ['600000.SH'], count=100)

# 数据结构
print(type(data))  # <class 'pandas.core.frame.DataFrame'>

# 访问方式1：通过股票代码
close_data = data['600000.SH']  # Series
print(close_data.values)         # numpy array

# 访问方式2：iloc 或 loc
print(data['600000.SH'].iloc[0])    # 第一个值
print(data['600000.SH'].iloc[-1])   # 最后一个值

# 转换为列表
close_list = list(data['600000.SH'].iloc[:, 0])
```

### 使用示例

#### 示例1：获取单个股票的基础数据

```python
# 回测中获取历史数据
def handlebar(C):
    # 获取最近20根K线的收盘价
    data = C.get_market_data_ex(
        ['close'],                                  # 位置参数
        [C.stock],                                  # 位置参数
        end_time=timetag_to_datetime(C.get_bar_timetag(C.barpos), '%Y%m%d%H%M%S'),
        period=C.period,
        count=20,
        subscribe=False  # 回测使用False
    )
    
    # 提取数据
    close_prices = list(data[C.stock].values.flatten())
    print(f"最近20根K线收盘价: {close_prices}")
```

#### 示例2：获取多个字段

```python
def handlebar(C):
    # 获取OHLCV数据
    data = C.get_market_data_ex(
        ['open', 'high', 'low', 'close', 'volume'],  # 位置参数
        [C.stock],                                   # 位置参数
        period='1d',
        count=10,
        subscribe=False
    )
    
    # 分别提取各字段
    opens = list(data[C.stock]['open'])
    closes = list(data[C.stock]['close'])
    volumes = list(data[C.stock]['volume'])
```

#### 示例3：获取多个股票

```python
def handlebar(C):
    # 获取多个股票的数据
    stocks = ['600000.SH', '000001.SZ', '600031.SH']
    data = C.get_market_data_ex(
        ['close'],                                   # 位置参数
        stocks,                                      # 位置参数
        period='1d',
        count=100,
        subscribe=False
    )
    
    # 遍历获取
    for stock in stocks:
        close_list = list(data[stock].values.flatten())
        print(f"{stock}: {close_list[-1]}")
```

---

## 📍 二、get_full_tick - 最新行情

### 函数签名

```python
tick = C.get_full_tick(stocks)
# 返回最新的tick数据，包含多个字段
```

### 返回数据结构

```python
tick = {
    '600000.SH': {
        'lastPrice': 10.5,          # 最新价
        'lastClose': 10.4,          # 前收盘
        'open': 10.3,               # 今开
        'high': 10.6,               # 今高
        'low': 10.2,                # 今低
        'volume': 1000000,          # 成交量
        'amount': 10500000,         # 成交额
        'time': '143000',           # 时间
        'bid': 10.49,               # 买价
        'ask': 10.51,               # 卖价
        'bidVol': 10000,            # 买量
        'askVol': 5000,             # 卖量
    },
    '000001.SZ': {
        # ...
    }
}
```

### 常用字段

| 字段 | 中文名 | 说明 |
|------|--------|------|
| lastPrice | 最新价 | 当前最新成交价 |
| lastClose | 前收盘 | 前一个交易日收盘价 |
| open | 今开 | 今日开盘价 |
| high | 今高 | 今日最高价 |
| low | 今低 | 今日最低价 |
| volume | 成交量 | 累计成交量 |
| amount | 成交额 | 累计成交金额 |
| bid | 买价 | 一档买价 |
| ask | 卖价 | 一档卖价 |

### 使用示例

```python
def handlebar(C):
    # 获取最新tick
    tick = C.get_full_tick(['600000.SH', '000001.SZ'])
    
    # 获取单个股票数据
    stock_tick = tick['600000.SH']
    current_price = stock_tick['lastPrice']
    previous_close = stock_tick['lastClose']
    
    # 计算涨幅
    rise_ratio = (current_price - previous_close) / previous_close
    print(f"涨幅: {rise_ratio*100:.2f}%")
    
    # 计算买卖价差
    spread = (stock_tick['ask'] - stock_tick['bid']) / current_price
    print(f"买卖价差率: {spread*100:.4f}%")
```

---

## 📮 三、subscribe_quote - 行情订阅

### 函数签名

```python
C.subscribe_quote(
    stock,                # 股票代码
    period=None,          # 周期（可选）
    callback=callback_func # 回调函数
)
```

### 参数说明

```python
stock = '600000.SH'           # 必须指定

period = '1d'                 # 日线
# 或其他周期如 '1m', '5m', etc.

# 回调函数
def callback_func(data):
    """
    参数 data: dict
    {
        '600000.SH': {
            'close': 10.5,
            'open': 10.3,
            ...
        }
    }
    """
    pass
```

### 使用场景

```python
def init(C):
    # 创建回调函数
    def on_quote(data):
        for stock in data:
            price = data[stock]['close']
            if price > 10.5:
                # 执行交易逻辑
                pass
    
    # 订阅行情
    C.subscribe_quote('600000.SH', period='1d', callback=on_quote)
```

---

## 🔍 四、get_last_volume - 最后成交量

### 函数签名

```python
volume = C.get_last_volume(stock)
# 返回最后成交的数量
```

### 使用示例

```python
# 获取单个股票最后成交量
vol = C.get_last_volume('600000.SH')
print(f"最后成交量: {vol}")

# 获取多个股票
stocks = ['600000.SH', '000001.SZ']
volumes = {}
for stock in stocks:
    volumes[stock] = C.get_last_volume(stock)
```

---

## 📋 五、get_stock_list_in_sector - 获取板块股票

### 函数签名

```python
stock_list = C.get_stock_list_in_sector(sector_name)
# 返回指定板块的所有股票代码
```

### 板块名称

```python
# 主要板块
'沪深A股'        # 沪深A股
'上证50'         # 上证50
'沪深300'        # 沪深300
'中证500'        # 中证500
'科创板'         # 科创板50
'创业板'         # 创业板

# 其他板块
'银行'           # 银行板块
'房地产'         # 房地产
'制造业'         # 制造业
```

### 使用示例

```python
def init(C):
    # 获取沪深A股所有股票
    hsa = C.get_stock_list_in_sector('沪深A股')
    print(f"沪深A股股票数: {len(hsa)}")
    print(f"前5只: {hsa[:5]}")
    
    # 获取科创板
    kcb = C.get_stock_list_in_sector('科创板')
    print(f"科创板股票数: {len(kcb)}")
```

### 返回格式

```python
stock_list = [
    '600000.SH',
    '600001.SH',
    '000001.SZ',
    '000002.SZ',
    ...
]
```

---

## 💬 六、get_stock_name - 获取股票名称

### 函数签名

```python
name = C.get_stock_name(stock_code)
# 返回股票名称
```

### 使用示例

```python
stock = '600000.SH'
name = C.get_stock_name(stock)
print(f"{stock} - {name}")  # 600000.SH - 浦发银行
```

---

## 🕐 七、时间相关函数

### timetag_to_datetime - 时间戳转换

```python
def timetag_to_datetime(timetag, fmt):
    """
    将K线时间戳转换为日期时间字符串
    
    参数:
        timetag: K线时间戳（整数）
        fmt: 输出格式字符串
    
    返回:
        格式化的日期时间字符串
    """
    pass

# 使用示例
bar_date = timetag_to_datetime(C.get_bar_timetag(C.barpos), '%Y%m%d%H%M%S')
# 返回: '20190101093000'
```

### get_bar_timetag - 获取K线时间

```python
# 获取当前K线时间戳
timetag = C.get_bar_timetag(C.barpos)

# 转换为日期时间
bar_date = timetag_to_datetime(timetag, '%Y%m%d%H%M%S')
```

---

## 📊 完整数据获取示例

### 示例：获取完整的OHLCV数据

```python
def get_full_ohlcv(C, stock, period='1d', count=100):
    """获取完整的OHLCV数据"""
    
    # 获取K线截止时间
    bar_date = timetag_to_datetime(
        C.get_bar_timetag(C.barpos), 
        '%Y%m%d%H%M%S'
    )
    
    # 获取所有字段
    data = C.get_market_data_ex(
        ['open', 'high', 'low', 'close', 'volume'],  # 位置参数
        [stock],                                     # 位置参数
        end_time=bar_date,
        period=period,
        count=count,
        subscribe=False
    )
    
    # 整理数据
    df = pd.DataFrame({
        'open': data[stock]['open'],
        'high': data[stock]['high'],
        'low': data[stock]['low'],
        'close': data[stock]['close'],
        'volume': data[stock]['volume']
    })
    
    return df
```

### 示例：实时行情数据

```python
def get_realtime_data(C, stocks):
    """获取实时行情数据"""
    
    tick = C.get_full_tick(stocks)
    
    realtime_data = {}
    for stock in stocks:
        t = tick[stock]
        realtime_data[stock] = {
            'price': t['lastPrice'],
            'volume': t['volume'],
            'amount': t['amount'],
            'bid': t['bid'],
            'ask': t['ask'],
        }
    
    return realtime_data
```

---

## 🎯 性能优化建议

### 1. 只查询必要的字段

```python
# ❌ 低效：查询所有字段
data = C.get_market_data_ex(
    ['open', 'high', 'low', 'close', 'volume', 'amount'],
    stocks_list,
    count=500
)

# ✅ 高效：只查询需要的字段
data = C.get_market_data_ex(
    ['close'],
    stocks_list,
    count=500
)
```

### 2. 缓存数据

```python
class DataCache:
    def __init__(self):
        self.cache = {}
        self.timestamp = {}
    
    def get(self, stock, period, count):
        key = f"{stock}_{period}_{count}"
        
        # 检查缓存是否过期
        if key in self.cache:
            if time.time() - self.timestamp[key] < 60:
                return self.cache[key]
        
        # 获取新数据
        data = C.get_market_data_ex([...], [stock], ...)
        self.cache[key] = data
        self.timestamp[key] = time.time()
        
        return data
```

### 3. 批量获取

```python
# ✅ 一次获取多个股票
stocks = ['600000.SH', '000001.SZ', '000858.SZ']
data = C.get_market_data_ex(['close'], stocks, count=100)

# 分别处理
for stock in stocks:
    close_prices = data[stock]
    # 处理逻辑
```

---

## 📚 相关资源

- ✅ [回测模型指南](./backtesting-guide.md) - 数据获取用法
- ✅ [实盘交易指南](./live-trading-guide.md) - 实时数据用法
- ✅ [交易API](./trading-api.md) - 下单函数

