# QMT 编码最佳实践与规范

## 📋 编码规范

### 1. 文件编码与基础规范

#### 放在文件第一行（必须！）
```python
#coding:gbk
# 这一行必须在文件的第一行，不能有任何Comment或空行在它之前
```

#### 缩进规范
```python
# ✅ 推荐：使用4个空格缩进
def init(C):
    C.stock = 'test'
    pass

# ❌ 错误：混合缩进（有的2个空格，有的4个）
def init(C):
  C.stock = 'test'      # 2个空格
    pass                # 4个空格
```

#### 导入库
```python
#coding:gbk

# 标准库
import pandas as pd
import numpy as np
import talib
import datetime
import time

# 然后是策略代码
def init(C):
    pass
```

---

## 🏗️ 代码结构最佳实践

### 标准的策略代码结构

```python
#coding:gbk

import pandas as pd
import numpy as np
import datetime

# ========== 1. 全局类/变量定义 ==========
class StrategyState:
    """策略状态管理"""
    def __init__(self):
        self.holding = False
        self.entry_price = 0
        self.params = {}

state = StrategyState()

# ========== 2. 初始化函数 ==========
def init(C):
    """策略初始化"""
    # 设置策略参数
    C.stock = C.stockcode + '.' + C.market
    C.line1 = 10
    C.line2 = 20
    
    # 初始化策略状态
    state.holding = False
    state.entry_price = 0
    
    print(f"策略初始化完成: {C.stock}")

# ========== 3. 主逻辑函数 ==========
def handlebar(C):
    """K线处理函数"""
    
    # 3.1 数据准备
    bar_date = timetag_to_datetime(C.get_bar_timetag(C.barpos), '%Y%m%d%H%M%S')
    
    # 3.2 获取行情
    data = get_market_data(C)
    if data is None:
        return
    
    # 3.3 指标计算
    signal = calculate_signal(C, data)
    
    # 3.4 交易执行
    execute_trade(C, signal)
    
    # 3.5 状态更新
    update_state(C)

# ========== 4. 辅助函数 ==========
def get_market_data(C):
    """获取行情数据"""
    try:
        bar_date = timetag_to_datetime(C.get_bar_timetag(C.barpos), '%Y%m%d%H%M%S')
        data = C.get_market_data_ex(
            ['close'],
            [C.stock],
            end_time=bar_date,
            period=C.period,
            count=max(C.line1, C.line2),
            subscribe=False
        )
        return data
    except Exception as e:
        print(f"获取行情异常: {e}")
        return None

def calculate_signal(C, data):
    """计算交易信号"""
    try:
        close_list = list(data[C.stock].values.flatten())
        if len(close_list) < max(C.line1, C.line2):
            return None
        
        line1 = np.mean(close_list[-C.line1:])
        line2 = np.mean(close_list[-C.line2:])
        
        if line1 > line2:
            return 'BUY'
        elif line1 < line2:
            return 'SELL'
        else:
            return None
    except Exception as e:
        print(f"计算信号异常: {e}")
        return None

def execute_trade(C, signal):
    """执行交易"""
    if signal is None:
        return
    
    # 获取账户信息
    account = get_trade_detail_data('test', 'stock', 'account')
    if not account:
        return
    
    # 加载具体的交易逻辑
    if signal == 'BUY':
        place_buy_order(C, account[0])
    elif signal == 'SELL':
        place_sell_order(C, account[0])

def place_buy_order(C, account):
    """执行买入"""
    vol = 100
    passorder(23, 1101, 'test', C.stock, 14, -1, vol, C)

def place_sell_order(C, account):
    """执行卖出"""
    vol = 100
    passorder(24, 1101, 'test', C.stock, 14, -1, vol, C)

def update_state(C):
    """更新策略状态"""
    state.holding = not state.holding
```

---

## ⚡ 性能优化建议

### 1. 最小化 API 调用

```python
# ❌ 低效：每次都重新查询
def handlebar(C):
    for i in range(100):
        data = C.get_market_data_ex(['close'], [C.stock], count=100)  # 多次调用
        # 处理 data

# ✅ 高效：查询一次，重复使用
def handlebar(C):
    data = C.get_market_data_ex(['close'], [C.stock], count=100)  # 只调用一次
    for i in range(100):
        # 使用已有的 data
        close_price = data[C.stock].values[i][0]
```

### 2. 缓存常用的计算

```python
class DataCache:
    def __init__(self):
        self.cache = {}
        self.timestamps = {}
    
    def get_ma(self, close_list, period):
        """计算移动平均线（带缓存）"""
        key = f"ma_{period}"
        
        # 检查缓存
        if key in self.cache:
            cached_data, cached_list = self.cache[key]
            if cached_list == close_list:
                return cached_data
        
        # 计算
        ma = np.mean(close_list[-period:])
        self.cache[key] = (ma, close_list)
        
        return ma

cache = DataCache()
```

### 3. 避免重复检查

```python
# ❌ 每个handlebar都检查账户
def handlebar(C):
    account = get_trade_detail_data('test', 'stock', 'account')  # 每次检查

# ✅ 初始化时检查，保存状态
class TradeState:
    def __init__(self):
        self.account_ok = False

A = TradeState()

def init(C):
    account = get_trade_detail_data('test', 'stock', 'account')
    A.account_ok = len(account) > 0

def handlebar(C):
    if not A.account_ok:
        return  # 账户有问题，直接返回
    # 继续交易逻辑
```

---

## 🛡️ 风险管理最佳实践

### 1. 止损设置

```python
class RiskManager:
    def __init__(self):
        self.stop_loss_pct = 0.03  # 3%止损
        self.entry_prices = {}
    
    def should_stop_loss(self, stock, current_price):
        """检查是否触发止损"""
        if stock not in self.entry_prices:
            return False
        
        entry_price = self.entry_prices[stock]
        loss_pct = (entry_price - current_price) / entry_price
        
        return loss_pct >= self.stop_loss_pct
    
    def record_entry(self, stock, price):
        """记录入场价格"""
        self.entry_prices[stock] = price
    
    def clear_entry(self, stock):
        """清除入场记录"""
        if stock in self.entry_prices:
            del self.entry_prices[stock]

rm = RiskManager()
```

### 2. 持仓管理

```python
class PositionManager:
    def __init__(self):
        self.max_position_size = 10000  # 最大持仓 10000 股
        self.max_single_volume = 5000   # 单笔最大 5000 股
    
    def can_buy(self, stock, current_holding, buy_volume):
        """检查是否可以买入"""
        
        # 检查单笔限制
        if buy_volume > self.max_single_volume:
            return False, "超过单笔最大额度"
        
        # 检查持仓限制
        new_total = current_holding + buy_volume
        if new_total > self.max_position_size:
            return False, "超过最大持仓"
        
        return True, "OK"
    
    def get_max_buy_volume(self, current_holding):
        """获取最大可买数量"""
        return min(
            self.max_single_volume,
            self.max_position_size - current_holding
        )

pm = PositionManager()
```

### 3. 日损失管理

```python
class DailyLossControl:
    def __init__(self, loss_limit_pct=0.05):
        self.loss_limit_pct = loss_limit_pct  # 日损失限制 5%
        self.initial_cash = 0
    
    def init_cash(self, cash):
        """初始化参考资金"""
        self.initial_cash = cash
    
    def check_loss(self, current_profit):
        """检查是否超过日损失限制"""
        loss_pct = -current_profit / self.initial_cash
        return loss_pct >= self.loss_limit_pct
    
    def get_allowed_loss(self):
        """获取允许的最大亏损额"""
        return self.initial_cash * self.loss_limit_pct

dlc = DailyLossControl()
```

---

## 🐛 调试与日志最佳实践

### 1. 结构化日志

```python
import datetime

class Logger:
    def __init__(self):
        self.logs = []
    
    def log(self, level, message):
        """记录日志"""
        timestamp = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        log_entry = f"[{timestamp}] [{level}] {message}"
        self.logs.append(log_entry)
        print(log_entry)
    
    def info(self, msg):
        self.log("INFO", msg)
    
    def warning(self, msg):
        self.log("WARN", msg)
    
    def error(self, msg):
        self.log("ERROR", msg)
    
    def get_logs(self):
        return self.logs

logger = Logger()

# 使用
def handlebar(C):
    try:
        # 逻辑处理
        logger.info(f"处理 K 线: {bar_date}")
    except Exception as e:
        logger.error(f"异常: {str(e)}")
```

### 2. 关键信息记录

```python
def handlebar(C):
    bar_date = timetag_to_datetime(C.get_bar_timetag(C.barpos), '%Y%m%d%H%M%S')
    
    # 记录重要信息
    print(f"[{bar_date}]")
    print(f"  股票: {C.stock}")
    print(f"  周期: {C.period}")
    print(f"  位置: {C.barpos}")
    
    # 获取行情后记录
    data = C.get_market_data_ex(['close'], [C.stock], count=1, subscribe=False)
    price = data[C.stock].values[0][0]
    print(f"  价格: {price}")
    
    # 记录交易信号
    if buy_signal:
        print(f"  [BUY] 信号强度: 0.87")
    elif sell_signal:
        print(f"  [SELL] 信号强度: 0.92")
```

### 3. 异常处理

```python
def handlebar(C):
    try:
        # 获取数据
        data = C.get_market_data_ex(['close'], [C.stock], count=100, subscribe=False)
        
        # 检查数据
        if data is None or C.stock not in data:
            logger.warning(f"数据不完整: {C.stock}")
            return
        
        # 处理数据
        close_list = list(data[C.stock].values.flatten())
        
        if len(close_list) == 0:
            logger.warning("收盘价列表为空")
            return
        
        # 计算指标
        ma = np.mean(close_list)
        
        # 交易
        if ma > 0:
            passorder(23, 1101, 'test', C.stock, 14, -1, 100, C)
            logger.info(f"买入: {C.stock} @ {close_list[-1]}")
    
    except KeyError as e:
        logger.error(f"数据键错误: {str(e)}")
    except ValueError as e:
        logger.error(f"数据值错误: {str(e)}")
    except Exception as e:
        logger.error(f"未知异常: {str(e)}")
        import traceback
        logger.error(traceback.format_exc())
```

---

## 📊 测试与验证最佳实践

### 1. 单元测试

```python
def test_calculate_ma():
    """测试移动平均线计算"""
    close_list = [10, 11, 12, 13, 14, 15]
    period = 3
    
    ma = np.mean(close_list[-period:])
    expected = 14.0  # (13+14+15)/3
    
    assert abs(ma - expected) < 0.01, f"MA计算错误: {ma} != {expected}"
    print("✓ test_calculate_ma 通过")

def test_buy_signal():
    """测试买入信号"""
    line1 = 15
    line2 = 14
    
    signal = 'BUY' if line1 > line2 else None
    
    assert signal == 'BUY', "买入信号判断错误"
    print("✓ test_buy_signal 通过")

# 运行测试
if __name__ == '__main__':
    test_calculate_ma()
    test_buy_signal()
    print("所有测试通过！")
```

### 2. 回测验证

```python
def validate_backtest_result(result):
    """验证回测结果是否合理"""
    
    validations = {
        'total_trades': result['total_trades'] > 0,
        'win_rate': 0 < result['win_rate'] < 1,
        'profit_factor': result['profit_factor'] > 0,
        'max_drawdown': result['max_drawdown'] < 0.5,
        'annual_return': -0.5 < result['annual_return'] < 2.0
    }
    
    for check, passed in validations.items():
        status = "✓" if passed else "✗"
        print(f"{status} {check}: {validations[check]}")
    
    return all(validations.values())
```

---

## 📚 常见模式

### 模式1：双均线策略框架

```python
#coding:gbk

def init(C):
    C.line1 = 10
    C.line2 = 20
    C.accountid = 'test'

def handlebar(C):
    # 获取数据
    data = C.get_market_data_ex(['close'], [C.stock], count=max(C.line1, C.line2), subscribe=False)
    close_prices = data[C.stock].values
    
    if len(close_prices) < max(C.line1, C.line2):
        return
    
    # 计算均线
    ma1 = np.mean(close_prices[-C.line1:])
    ma2 = np.mean(close_prices[-C.line2:])
    
    # 交易逻辑
    if ma1 > ma2:
        passorder(23, 1101, C.accountid, C.stock, 14, -1, 100, C)
    elif ma1 < ma2:
        passorder(24, 1101, C.accountid, C.stock, 14, -1, 100, C)
```

### 模式2：涨幅选股框架

```python
#coding:gbk

def init(C):
    C.stock_list = C.get_stock_list_in_sector('沪深A股')
    C.rise_threshold = 0.05

def handlebar(C):
    tick = C.get_full_tick(C.stock_list)
    
    for stock in C.stock_list:
        last_price = tick[stock]['lastPrice']
        last_close = tick[stock]['lastClose']
        rise_ratio = (last_price - last_close) / last_close
        
        if rise_ratio > C.rise_threshold:
            print(f"{stock} 涨幅 {rise_ratio*100:.2f}%")
            # 执行买入逻辑
```

---

## ⚠️ 常见陷阱

### 陷阱1：忘记检查数据长度

```python
# ❌ 错误：可能导致IndexError
ma = np.mean(close_list[-10:])

# ✅ 正确：先检查长度
if len(close_list) >= 10:
    ma = np.mean(close_list[-10:])
else:
    return  # 数据不足，跳过
```

### 陷阱2：混淆回测和实盘参数

```python
# ❌ 错误：回测中使用 subscribe=True
data = C.get_market_data_ex(..., subscribe=True)

# ✅ 正确：根据场景选择
subscribe = False if is_backtest else True
data = C.get_market_data_ex(..., subscribe=subscribe)
```

### 陷阱3：忽略单位转换

```python
# ❌ 错误：m_dAvailable 单位是分（1/100元）
cash = account.m_dAvailable  # 这是分

# ✅ 正确：转换为元
cash_yuan = account.m_dAvailable / 100
```

### 陷阱4：未经验证直接交易

```python
# ❌ 错误：直接根据信号下单
if signal > 0:
    passorder(...)

# ✅ 正确：验证信号后再下单
if signal > 0 and validate_signal(signal):
    passorder(...)
```

---

## 📚 相关资源

- ✅ [系统概述](./overview.md) - QMT基础
- ✅ [回测模型指南](./backtesting-guide.md) - 回测实践
- ✅ [实盘交易指南](./live-trading-guide.md) - 实盘实践
- ✅ [代码示例](./examples/) - 完整示例代码

