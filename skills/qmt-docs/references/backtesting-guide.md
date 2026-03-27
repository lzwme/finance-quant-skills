# QMT 回测模型完全指南

## 🎯 回测概述

**回测**是遍历固定的历史数据，模拟交易过程的过程。在历史K线上从左向右逐根遍历，以模拟的资金账号记录每日的买卖信号、持仓盈亏，最终展示策略在历史上的净值走势结果。

### 回测的意义
- ✅ 验证策略逻辑的正确性
- ✅ 评估策略历史表现
- ✅ 优化策略参数
- ✅ 降低实盘风险
- ✅ 快速迭代策略

---

## 📥 第一步：数据准备

### 下载历史行情

#### 操作步骤

1. **打开数据管理**
   - 点击QMT界面左上角 **操作** 按钮
   - 选择 **数据管理** 选项

2. **选择数据类型**
   - 选择回测的周期（日线、周线、月线等）
   - 选择所需的板块（沪深A股、创业板等）

3. **设置时间范围**
   - 时间范围选择 **全部** 或指定范围
   - 点击下载完整历史行情

#### 下载配置建议

```
周期选择：
  ├─ 日线：适合中期策略
  ├─ 周线：适合长期策略
  ├─ 1分钟/5分钟：适合高频策略
  └─ 15分钟/30分钟：适合短期策略

板块选择：
  ├─ 沪深A股：全市场
  ├─ 创业板：创业板股票
  ├─ 科创板：科创板股票
  └─ 指数：股指数据

时间范围：
  ├─ 全部：完整历史
  ├─ 最近1年：最近一年数据
  ├─ 最近3年：最近三年数据
  └─ 自定义：指定起止日期
```

### 设置定时更新

为了保持数据最新，设置每日定时更新：

1. **点击界面右下角 行情 按钮**
2. **进入批量下载界面**
3. **选择需要每天更新的数据**
4. **勾选 定时下载 选项**
5. **指定下载时间**（如每天22:00）

每天在指定时间会自动下载最新行情数据到本地。

---

## ⚙️ 第二步：基础信息设置

### 在"我的界面"配置回测策略

#### 策略名称
```
输入策略的描述名称，方便后续查询和管理
```

#### 默认周期
```
回测使用的K线周期
- 日线（1d）
- 周线（1w）
- 月线（1m）
- 分钟线（1m, 5m, 15m, 30m）
```

#### 默认主图
```
选择回测的品种可以是：
- 单个股票（如 600000.SH）
- 指数（如 000001.SZ）
- 自定义品种
```

#### 账号设置
```python
# 回测模式账号可以填任意字符串
C.accountid = "test"        # 任意名称
C.accountid = "backtest01"  # 建议与策略名称相关
```

#### 初始资金
```python
# 回测使用模拟资金账号
# 账号的初始资金由QMT系统预设
# 默认为 1000000 元（100万）
```

---

## 📊 第三步：回测参数设置

### 回测参数配置

在回测界面设置以下参数：

#### 1. 基础参数

| 参数 | 说明 | 示例 |
|------|------|------|
| 策略选择 | 选择要回测的策略文件 | dual_ma_strategy.py |
| 周期 | K线周期 | 日线（1d） |
| 品种 | 回测的股票代码 | 600000.SH |
| 起始日期 | 回测开始日期 | 2019-01-01 |
| 结束日期 | 回测结束日期 | 2022-12-31 |

#### 2. 资金参数

```python
# 初始资金设置
initial_cash = 1000000  # 100万元

# 手续费率
commission_rate = 0.001  # 0.1%

# 印花税率
stamp_tax = 0.001  # 0.1%（卖出时收取）

# 滑点设置
slippage = 0  # 默认不考虑滑点
```

#### 3. 交易参数

```python
# 每次交易的最小单位
min_order_size = 100  # 100股

# 最大购买力
max_cash_fraction = 0.9  # 最多使用90%的现金

# 杠杆倍数
leverage = 1  # 1倍为无杠杆
```

### 参数设置建议

✅ **入门回测** - 建议设置
```
周期：日线（1d）
时间：最近3年
品种：单只股票或指数
初始资金：100万
```

✅ **中等策略** - 建议设置
```
周期：日线/周线混合
时间：最近5年
品种：板块（如沪深A股）
初始资金：500万
```

✅ **高频策略** - 建议设置
```
周期：5分钟/15分钟
时间：最近1年
品种：流动性好的股票
初始资金：100万
```

---

## 🚀 第四步：代码实现

### 代码结构

```python
#coding:gbk  # ← 必须在第一行

# 导入库
import pandas as pd
import numpy as np
import talib

# 全局变量定义
# ...

def init(C):
    """初始化函数"""
    # 设置初始参数
    pass

def handlebar(C):
    """K线处理函数"""
    # 每根K线触发一次
    # 进行交易逻辑
    pass
```

### init 函数 - 初始化

```python
def init(C):
    """
    初始化函数，在回测开始时执行一次
    参数 C: ContextInfo 对象
    """
    
    # 1. 设置交易品种
    C.stock = C.stockcode + '.' + C.market
    # C.stockcode: '600000'
    # C.market: 'SH' 或 'SZ'
    # 结果: '600000.SH'
    
    # 2. 设置策略参数
    C.line1 = 10    # 快线周期
    C.line2 = 20    # 慢线周期
    
    # 3. 设置账号
    C.accountid = 'test'
    
    # 4. 初始化状态变量
    C.holding = False
    C.entry_price = 0
    
    # 5. 获取账户初始信息
    # 账户初始资金由系统自动设置
```

### handlebar 函数 - 交易逻辑

#### 获取当前K线信息

```python
def handlebar(C):
    # 获取当前K线时间
    bar_date = timetag_to_datetime(
        C.get_bar_timetag(C.barpos), 
        '%Y%m%d%H%M%S'
    )
    # 返回格式: '20190101093000'
    
    # 获取当前K线位置
    bar_pos = C.barpos  # K线索引位置
    
    # 获取当前K线周期
    period = C.period  # '1d', '1w', etc.
```

#### 获取历史行情数据

```python
# 回测的关键：使用 subscribe=False 和位置参数
local_data = C.get_market_data_ex(
    ['close', 'high', 'low', 'open'],               # 字段列表（位置参数）
    [C.stock],                                      # 股票列表（位置参数）
    end_time=bar_date,                              # 数据截至时间
    period=C.period,                                # K线周期
    count=max(C.line1, C.line2),                    # 数据条数
    subscribe=False                                 # ← 回测必须False
)

# 提取某个股票的数据
close_list = list(local_data[C.stock].iloc[:, 0])

# close_list: [10.5, 10.4, 10.3, 10.2, 10.1, ...]
```

#### 计算指标

```python
# 数据预检查
if len(close_list) < max(C.line1, C.line2):
    print(f"{bar_date} 行情不足，跳过")
    return

# 计算双均线
line1_mean = round(np.mean(close_list[-C.line1:]), 2)
line2_mean = round(np.mean(close_list[-C.line2:]), 2)

print(f"{bar_date} 短均线:{line1_mean} 长均线:{line2_mean}")
```

#### 获取账户信息

```python
# 获取账户信息
account = get_trade_detail_data('test', 'stock', 'account')
if not account:
    print("账户未登录")
    return
account = account[0]

# 可用现金（单位：分）
available_cash = int(account.m_dAvailable)

# 获取持仓信息
holdings = get_trade_detail_data('test', 'stock', 'position')

# 整理成字典格式
holdings_dict = {
    f'{i.m_strInstrumentID}.{i.m_strExchangeID}': i.m_nVolume 
    for i in holdings
}

holding_vol = holdings_dict.get(C.stock, 0)
current_price = close_list[-1]
```

#### 下单操作

```python
# 计算交易数量
vol = int(available_cash / current_price / 100) * 100

# 买入信号：双线金叉（上穿）
if holding_vol == 0 and line1_mean > line2_mean:
    passorder(
        23,             # 买卖代码（23=卖出, 24=卖出）
        1101,           # 价格订单类型（市价）
        C.accountid,    # 账号
        C.stock,        # 品种
        5,              # 订单等级
        -1,             # 止价 (-1 = 不设置）
        vol,            # 成交数量
        C               # ContextInfo对象
    )
    print(f"{bar_date} 双均线金叉 买入")
    C.draw_text(1, 1, '买')

# 卖出信号：双线死叉（下穿）
elif holding_vol > 0 and line1_mean < line2_mean:
    passorder(
        24,             # 卖出
        1101,
        C.accountid,
        C.stock,
        5,
        -1,
        holding_vol,    # 卖出所有持仓
        C
    )
    print(f"{bar_date} 双均线死叉 卖出")
    C.draw_text(1, 1, '卖')
```

---

## 📈 第五步：运行回测

### 回测运行方式

#### 方式一：在"我的界面"运行
1. 选择策略模型
2. 点击"回测"按钮
3. 使用模型中配置的默认周期、品种

#### 方式二：在行情界面运行
1. 打开目标股票/品种的K线
2. 在K线下方右键点击"回测"
3. 以当前K线周期和品种为准

#### 方式三：在策略编辑器运行
1. 打开策略代码
2. Ctrl+F5 或 点击"运行"按钮
3. 系统自动选择当前配置

### 回测执行的要求

⚠️ **必须执行要求**
```
1. ✅ 副图模式执行（不能选择主图/主图叠加）
2. ✅ 选择需要的股票品种作为主图
3. ✅ 确保已下载对应周期的历史数据
```

❌ **错误配置**
```
1. ❌ 使用主图固定模式
2. ❌ 未下载对应周期数据
3. ❌ subscribe=True（应为False）
```

---

## 📊 第六步：分析回测结果

### 回测报告

回测完成后，系统生成以下报告：

#### 1. 净值曲线
```
显示策略从开始到结束的累计收益率曲线
用于直观评估策略表现
```

#### 2. 主要指标

| 指标 | 说明 | 目标 |
|------|------|------|
| 总收益率 | 总的收益比例 | 越高越好 |
| 年化收益率 | 年均收益比例 | 15%-30% 为优秀 |
| 夏普比率 | 风险调整收益 | > 1 为良好 |
| 最大回撤 | 最坏情况下的亏损 | 越小越好 |
| 胜率 | 赢利交易的比例 | 50% 以上 |
| 盈亏比 | 平均盈利/平均亏损 | > 1 为良好 |

#### 3. 交易记录

```
显示回测期间的所有交易：
- 交易日期
- 交易价格
- 交易数量
- 交易费用
- 当前盈亏
```

### 优化回测结果

#### 参数优化
```python
# 尝试不同的参数组合
for line1 in range(5, 15):
    for line2 in range(15, 30):
        if line2 > line1:
            # 重新运行回测
            pass
```

#### 模型改进
```python
# 1. 加入止损
# 2. 加入持仓限制
# 3. 加入风险管理
# 4. 改进进出场逻辑
```

---

## ⚠️ 常见问题与解决

### Q1: "行情不足"错误

**问题**：回测时显示"行情不足，跳过"

**原因**：
- 所需的历史数据条数不够
- 周期设置不匹配
- 数据未下载

**解决**：
```python
# 检查 count 是否足够
count = max(C.line1, C.line2) + buffer
# 关键是还需要预留一些缓冲
count = max(C.line1, C.line2) + 10
```

### Q2: 回测速度太慢

**问题**：回测耗时很长

**原因**：
- 查询的数据量太大
- 计算过于复杂
- API调用太频繁

**解决**：
```python
# 1. 减少查询字段
fields = ['close']  # 不要查询不需要的字段

# 2. 缓存计算结果
# 避免重复计算相同的指标

# 3. 减少循环次数
# 只处理需要的数据
```

### Q3: 回测结果与实盘不符

**问题**：回测表现好，但实盘不好

**原因**：
- 回测中没考虑手续费
- 回测中没考虑滑点
- 实盘有交易限制（涨跌停、价格笼子等）
- 参数过拟合

**解决**：
```python
# 1. 加入合理的手续费和滑点
# 2. 考虑涨跌停限制
# 3. 适当放宽参数范围
# 4. 增加回测期间
```

### Q4: 账户信息无法获取

**问题**：`get_trade_detail_data` 返回空

**原因**：
- 账户名称错误
- 账户类型（'stock'）错误
- 账户未登录

**解决**：
```python
# 检查账户参数
account = get_trade_detail_data(
    'test',         # 账户ID（回测可任意）
    'stock',        # 账户类型（固定为'stock'）
    'account'       # 查询类型（固定为'account'）
)

# 添加错误处理
if not account:
    print("账户获取失败")
    return
```

---

## 💡 最佳实践

### ✅ 回测最佳实践

```python
# 1. 始终检查数据完整性
if len(close_list) < required_count:
    return

# 2. 使用异常处理
try:
    line_mean = np.mean(close_list[-period:])
except Exception as e:
    print(f"计算异常: {e}")
    return

# 3. 记录关键信息
print(f"{bar_date} stock:{C.stock} price:{current_price} signal:{signal}")

# 4. 避免过度优化
# 不要调整过多参数以适应历史数据

# 5. 设置合理的参数范围
# 快线: 5-20期
# 慢线: 15-60期
```

### ❌ 常见错误

```python
# ❌ 错误：在回测中使用 subscribe=True
data = C.get_market_data_ex(..., subscribe=True)

# ✅ 正确：使用 subscribe=False
data = C.get_market_data_ex(..., subscribe=False)

# ❌ 错误：不检查数据长度
line_mean = np.mean(close_list[-period:])  # 可能报错

# ✅ 正确：先检查数据长度
if len(close_list) >= period:
    line_mean = np.mean(close_list[-period:])

# ❌ 错误：账户参数灵活变化
account_id = random.choice(['test1', 'test2'])

# ✅ 正确：账户参数固定
account_id = 'backtest'
```

---

## 📚 相关资源

- ✅ [系统概述](./overview.md) - QMT基础概念
- ✅ [运行机制](./execution-mechanisms.md) - handlebar详解
- ✅ [市场数据API](./market-data-api.md) - 行情函数文档
- ✅ [交易API](./trading-api.md) - 下单函数文档
- ✅ [代码示例](./examples/backtest.md) - 完整回测示例

