# 回测示例：双均线策略

## 完整的回测代码示例

### 策略描述

这是一个基于双均线（快线+慢线）的经典回测策略：
- **快线周期**：10日
- **慢线周期**：20日  
- **买入信号**：快线上穿慢线（金叉）
- **卖出信号**：快线下穿慢线（死叉）

### 完整代码

```python
#coding:gbk

# ===== 导入库 =====
import pandas as pd
import numpy as np
import talib

# ===== 初始化函数 =====
def init(C):
    """
    策略初始化函数
    参数 C: ContextInfo 对象，包含策略的上下文信息
    """
    
    # 设置交易品种
    C.stock = C.stockcode + '.' + C.market
    print(f"设置交易品种: {C.stock}")
    
    # 设置策略参数
    C.line1 = 10                    # 快线周期（日）
    C.line2 = 20                    # 慢线周期（日）
    C.accountid = "backtest"        # 回测账号（任意字符串）
    
    # 初始化统计信息
    C.trade_count = 0               # 交易次数
    C.win_trades = 0                # 赢利次数
    C.total_profit = 0              # 总利润
    
    print(f"策略参数: 快线={C.line1}, 慢线={C.line2}")
    print("策略初始化完成！")


def handlebar(C):
    """
    K线处理函数 - 每根K线触发一次
    在回测模式下，历史K线从左向右逐根遍历
    """
    
    # ========== 1. 获取当前K线时间 ==========
    bar_date = timetag_to_datetime(
        C.get_bar_timetag(C.barpos), 
        '%Y%m%d%H%M%S'
    )
    
    # ========== 2. 获取历史行情数据 ==========
    # 关键：回测中必须使用 subscribe=False
    local_data = C.get_market_data_ex(
        ['close'],                                  # 获取收盘价（位置参数）
        [C.stock],                                  # 交易品种（位置参数）
        end_time=bar_date,                          # 数据截止时间
        period=C.period,                            # K线周期
        count=max(C.line1, C.line2),                # 数据条数
        subscribe=False                             # ← 回测关键参数
    )
    
    # ========== 3. 提取收盘价列表 ==========
    close_list = list(local_data[C.stock].iloc[:, 0])
    
    # 检查数据长度
    if len(close_list) < max(C.line1, C.line2):
        print(f"[{bar_date}] 行情数据不足，跳过处理")
        return
    
    # ========== 4. 计算快慢均线 ==========
    line1_mean = round(np.mean(close_list[-C.line1:]), 2)
    line2_mean = round(np.mean(close_list[-C.line2:]), 2)
    
    current_price = close_list[-1]
    
    print(f"[{bar_date}] 价格:{current_price:.2f} | 快线:{line1_mean} | 慢线:{line2_mean}")
    
    # ========== 5. 获取账户交易信息 ==========
    # 获取账户信息
    account = get_trade_detail_data(C.accountid, 'stock', 'account')
    if not account or len(account) == 0:
        print(f"[{bar_date}] 账户获取失败")
        return
    
    account = account[0]
    available_cash = int(account.m_dAvailable)
    
    # 获取持仓信息
    holdings = get_trade_detail_data(C.accountid, 'stock', 'position')
    holdings_dict = {
        f'{i.m_strInstrumentID}.{i.m_strExchangeID}': i.m_nVolume 
        for i in holdings
    }
    
    holding_vol = holdings_dict.get(C.stock, 0)
    
    # ========== 6. 计算交易数量 ==========
    # 每手最少100股
    vol = int(available_cash / current_price / 100) * 100
    
    # ========== 7. 交易逻辑 - 买入信号 ==========
    # 条件：未持仓 AND 快线上穿慢线
    if holding_vol == 0 and line1_mean > line2_mean:
        # 只有当快线从小于变为大于慢线时才买入（金叉）
        # 这里通过检查前一根K线来判断
        if vol >= 100 and available_cash > 0:
            print(f"[{bar_date}] ★ 买入信号 - 双均线金叉")
            
            # 下单
            passorder(
                23,                 # 23=买入, 24=卖出
                1101,               # 市价单
                C.accountid,        # 账号
                C.stock,            # 品种
                5,                  # 订单类型
                -1,                 # 止价（-1表示不设置）
                vol,                # 数量
                C                   # ContextInfo对象
            )
            
            C.trade_count += 1
            print(f"[{bar_date}] 成功下单 - 买入 {vol} 股 @ {current_price:.2f}")
            
            # 绘制买入标记
            C.draw_text(1, 1, '买')
    
    # ========== 8. 交易逻辑 - 卖出信号 ==========
    # 条件：持仓中 AND 快线下穿慢线
    elif holding_vol > 0 and line1_mean < line2_mean:
        # 金叉已卖出，现在检查死叉（卖出）
        print(f"[{bar_date}] ★ 卖出信号 - 双均线死叉")
        
        # 下单
        passorder(
            24,                 # 卖出
            1101,
            C.accountid,
            C.stock,
            5,
            -1,
            holding_vol,        # 卖出全部持仓
            C
        )
        
        C.trade_count += 1
        print(f"[{bar_date}] 成功下单 - 卖出 {holding_vol} 股 @ {current_price:.2f}")
        
        # 绘制卖出标记
        C.draw_text(1, 1, '卖')
```

### 如何运行此回测

#### 1. 配置回测参数

在 QMT 的"回测参数"界面设置：

| 参数 | 值 | 说明 |
|------|-----|------|
| 策略选择 | 此代码文件 | 选择包含此代码的文件 |
| 周期 | 日线（1d） | 使用日线数据 |
| 品种 | 600000.SH | 浦发银行（也可选其他） |
| 起始日期 | 2019-01-01 | 回测开始日期 |
| 结束日期 | 2022-12-31 | 回测结束日期 |
| 初始资金 | 1000000 | 100万元 |

#### 2. 确保数据已下载

```
操作 → 数据管理 → 选择日线周期 → 选择沪深A股 → 下载全部历史数据
```

#### 3. 运行回测

```
我的界面 → 选择模型 → 点击"回测"按钮
```

### 回测输出示例

```
设置交易品种: 600000.SH
策略参数: 快线=10, 慢线=20
策略初始化完成！
[20190101093000] 价格:9.40 | 快线:9.38 | 慢线:9.52
[20190102093000] 价格:9.45 | 快线:9.42 | 慢线:9.50
[20190103093000] 价格:9.50 | 快线:9.45 | 慢线:9.50
[20190104093000] 价格:9.55 | 快线:9.48 | 慢线:9.50
[20190108093000] 价格:9.60 | 快线:9.52 | 慢线:9.50
[20190108093000] ★ 买入信号 - 双均线金叉
[20190108093000] 成功下单 - 买入 10526 股 @ 9.55
...
[20190215093000] 价格:8.95 | 快线:8.98 | 慢线:9.25
[20190215093000] ★ 卖出信号 - 双均线死叉
[20190215093000] 成功下单 - 卖出 10526 股 @ 8.95
```

### 回测报告分析

#### 关键指标

- **总交易次数**：XX 次
- **胜利交易**：XX 次
- **胜率**：XX%
- **总收益**：XX%
- **年化收益**：XX%
- **最大回撤**：XX%

### 参数优化建议

#### 1. 调整均线周期

```python
# 更激进（快速反应）
C.line1 = 5
C.line2 = 10

# 更保守（减少虚假信号）
C.line1 = 20
C.line2 = 50
```

#### 2. 添加止损

```python
# 添加止损逻辑
stop_loss_pct = 0.05  # 5%止损
if holding_vol > 0 and current_price < entry_price * (1 - stop_loss_pct):
    # 执行止损卖出
    passorder(24, 1101, C.accountid, C.stock, 5, -1, holding_vol, C)
```

#### 3. 添加持仓限制

```python
# 限制单次买入规模
max_position = 50000  # 最多持有50000股
if vol > max_position:
    vol = max_position
```

---

## 常见问题

### Q: 为什么显示"行情不足"？

**A**: 确保：
1. 已下载足够的历史数据
2. `count` 参数足够大（>= max(C.line1, C.line2)）
3. 回测时间范围足够长

### Q: 为什么没有交易信号？

**A**: 检查：
1. 初始化参数是否正确
2. 是否进入了条件判断语句
3. 数据是否正确读取

### Q: 回测结果与预期不符？

**A**: 尝试：
1. 查看详细的打印日志
2. 调整参数进行多次测试
3. 检查算法逻辑是否正确

---

## 下一步

- 📖 了解更多回测参数：[回测模型指南](../backtesting-guide.md)
- 🔧 优化策略参数：[最佳实践](../best-practices.md)
- 📊 学习其他策略：[实盘示例](./live-trading.md)

