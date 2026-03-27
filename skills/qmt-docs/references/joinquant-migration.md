# 聚宽策略迁移至 QMT 指南

本文档帮助将聚宽（JoinQuant）策略迁移到 QMT 平台，提供结构对比、API 映射和完整代码移植示例。

## 1. 核心概念对比

### 1.1 运行环境差异

| 特性 | 聚宽 | QMT |
|------|------|-----|
| 运行环境 | 云端服务器 | 本地客户端 |
| 数据存储 | 服务端 | 本地数据库 |
| 编码要求 | UTF-8 | **GBK（必须在首行声明）** |
| 全局变量 | `g.xxx` | `C.xxx`（ContextInfo 对象属性） |
| 回测设置 | 代码配置 | 界面右侧栏设置 |

### 1.2 函数入口对照

| 聚宽 | QMT | 说明 |
|------|-----|------|
| `initialize(context)` | `init(C)` | 初始化函数 |
| `handle_data(context, data)` | `handlebar(C)` | 主逻辑函数（每根K线执行） |
| `before_trading_start(context)` | `run_time()` | 开盘前执行（需配置定时） |

### 1.3 股票代码格式

| 平台 | 格式 | 示例 |
|------|------|------|
| 聚宽 | `代码.市场简称` | `000001.XSHE`、`600000.XSHG` |
| QMT | `代码.市场代码` | `000001.SZ`、`600000.SH` |

**转换规则：** `XSHE` → `SZ`，`XSHG` → `SH`

```python
def convert_code(jq_code):
    """聚宽代码格式转 QMT 格式"""
    code, market = jq_code.split('.')
    return f"{code}.{'SZ' if market == 'XSHE' else 'SH'}"
```

## 2. API 对照表

### 2.1 数据获取

| 功能 | 聚宽 | QMT |
|------|------|------|
| 历史行情 | `attribute_history(security, count, unit, fields)` | `C.get_market_data_ex(fields, stock_list, period, count, subscribe=False)` |
| 实时行情 | `get_current_data()` | `C.get_full_tick([stock])` |
| 当前价格 | `data[security].close` | `C.get_market_data_ex(['close'], [stock])` |
| K线时间 | `data[security].datetime` | `timetag_to_datetime(C.get_bar_timetag(C.barpos), '%Y%m%d%H%M%S')` |
| 财务数据 | `get_fundamentals()` | `get_finance_data()` |

**关键差异：** QMT 数据存储在本地，回测时 `subscribe=False` 使用本地数据，实盘时 `subscribe=True` 订阅服务器数据。

### 2.2 交易函数

| 功能 | 聚宽 | QMT |
|------|------|------|
| 按股数买入 | `order(security, 100)` | `passorder(23, 1101, account, stock, 5, -1, 100, C)` |
| 按金额买入 | `order_value(security, 10000)` | `passorder(23, 1123, account, stock, 5, -1, 1, C)` |
| 按股数卖出 | `order(security, -100)` | `passorder(24, 1101, account, stock, 5, -1, 100, C)` |
| 目标持仓 | `order_target(security, 0)` | 需自行计算差额后下单 |
| 撤单 | `order_cancel(order_id)` | `cancel(order_id, account, C)` |

**passorder 参数速查：**

```python
passorder(opType, orderType, account, stock, priceType, price, volume, C)

# opType: 23=买入, 24=卖出
# orderType: 1101=按股数, 1123=按市值比例(1=100%)
# priceType: 5=限价
# price: -1=当前价
# volume: 股数或比例
```

### 2.3 账户信息

| 功能 | 聚宽 | QMT |
|------|------|------|
| 可用现金 | `context.portfolio.cash` | `get_trade_detail_data(acc, 'stock', 'account')[0].m_dAvailable` |
| 持仓信息 | `context.portfolio.positions` | `get_trade_detail_data(acc, 'stock', 'position')` |
| 可卖数量 | `position.closeable_amount` | `position.m_nCanUseVolume` |
| 持仓数量 | `position.total_amount` | `position.m_nVolume` |

### 2.4 工具函数

| 功能 | 聚宽 | QMT |
|------|------|------|
| 日志输出 | `log.info("msg")` | `print("msg")` |
| 记录变量 | `record(key=value)` | `C.draw_text()` 或界面查看 |
| 定时执行 | `run_daily(func, time)` | `run_time(func, period, C)` |

## 3. 完整迁移示例

### 3.1 策略逻辑

当价格高于 5 日均线 1.05 倍时全仓买入，低于 5 日均线 0.95 倍时全仓卖出。

### 3.2 聚宽原代码

```python
# 导入函数库
import jqdata

# 初始化函数，设定要操作的股票、基准等等
def initialize(context):
    # 定义一个全局变量, 保存要操作的股票
    # 000001(股票:平安银行)
    g.security = '000001.XSHE'
    # 设定沪深300作为基准
    set_benchmark('000300.XSHG')
    # 开启动态复权模式(真实价格)
    set_option('use_real_price', True)

# 每个单位时间(如果按天回测,则每天调用一次,如果按分钟,则每分钟调用一次)调用一次
def handle_data(context, data):
    security = g.security
    # 获取股票的收盘价
    close_data = attribute_history(security, 5, '1d', ['close'])
    # 取得过去五天的平均价格
    MA5 = close_data['close'].mean()
    # 取得上一时间点价格
    current_price = close_data['close'][-1]
    # 取得当前的现金
    cash = context.portfolio.cash

    # 如果上一时间点价格高出五天平均价5%, 则全仓买入
    if current_price > 1.05 * MA5:
        # 用所有 cash 买入股票
        order_value(security, cash)
        # 记录这次买入
        log.info("Buying %s" % (security))
    # 如果上一时间点价格低于五天平均价, 则空仓卖出
    elif current_price < 0.95 * MA5 and context.portfolio.positions[security].closeable_amount > 0:
        # 卖出所有股票,使这只股票的最终持有量为0
        order_target(security, 0)
        # 记录这次卖出
        log.info("Selling %s" % (security))
    # 画出上一时间点价格
    record(stock_price=current_price)
```

### 3.3 QMT 移植代码

```python
#coding:gbk
# QMT是一个本地端界面化软件，回测基准、回测手续费、回测起止时间都可在界面右侧栏进行设置

def init(C):
    # 定义一个全局变量，设定要操作的股票
    C.stock_list = ["000001.SZ"]
    # 设定回测账号，实盘中账号在交易设置截面选择
    C.account_id = "testaccID"

def handlebar(C):
    # 当前K线日期
    bar_date = timetag_to_datetime(C.get_bar_timetag(C.barpos), '%Y%m%d%H%M%S')
    
    # 获取市场行情
    market_data = C.get_market_data_ex(
        ["open", "high", "low", "close"], 
        C.stock_list, 
        period="1d", 
        end_time=bar_date
    )

    # 获取当前账户资金
    cash = 0
    for i in get_trade_detail_data(C.account_id, "stock", "account"):
        cash = i.m_dAvailable

    # 获取当前持仓信息
    # holding_dict 结构：{stock_code: lots}
    holding_dict = {
        obj.m_strInstrumentID + "." + obj.m_strExchangeID: obj.m_nVolume 
        for obj in get_trade_detail_data(C.account_id, "stock", "position")
    }
    
    # 遍历股票
    for i in market_data:
        # 获取K线数据
        kline = market_data[i]
        # 获取收盘价序列
        close_data = kline["close"]
        # 计算MA5
        MA5 = close_data.rolling(5).mean()
        
        # 如果价格高出五天平均价5%，且当前无持仓，则全仓买入
        if close_data.iloc[-1] > 1.05 * MA5.iloc[-1] and i not in holding_dict.keys():
            # 全仓买入
            passorder(23, 1123, C.account_id, i, 5, -1, 1, C)
            print(f"{bar_date}——{i}触发买入")
            
        # 如果价格低于五天平均价5%，且有持仓，则全仓卖出
        elif close_data.iloc[-1] < 0.95 * MA5.iloc[-1] and i in holding_dict.keys():
            # 获取当前持仓数量
            lots = holding_dict[i]
            # 全仓卖出
            passorder(24, 1101, C.account_id, i, 5, -1, lots, C)
            print(f"{bar_date}——{i}触发卖出")
```

## 4. QMT 特色功能

QMT 提供聚宽没有的特色函数：

```python
# 指数权重
get_weight_in_index(index_code, stock_code)

# 复权因子
get_divid_factors(stock_code, start_date, end_date)

# 十大股东
get_top10_share_holder(stock_code)

# ETF 数据
get_etf_info(etf_code)      # 申赎清单
get_etf_iopv(etf_code)      # 参考净值

# 实时订阅
subscribe_whole_quote(market, callback)  # 全推 tick
subscribe_quote(stocks, period, callback) # 单股行情

# 期权列表
get_option_list(date, underlying)
```

## 5. 迁移检查清单

### 必做事项

- [ ] 文件首行添加 `#coding:gbk`
- [ ] 股票代码格式转换（`XSHE`→`SZ`，`XSHG`→`SH`）
- [ ] 函数名替换：`initialize`→`init`，`handle_data`→`handlebar`
- [ ] 全局变量：`g.xxx`→`C.xxx`
- [ ] 数据函数替换
- [ ] 下单函数替换为 `passorder`
- [ ] 账户信息获取方式替换
- [ ] 兼容支持回测模式（使用 `C.is_backtest` 判断）

---

**相关文档：**
- [QMT 系统概述](overview.md)
- [回测完全指南](backtesting-guide.md)
- [交易 API](trading-api.md)
- [最佳实践](best-practices.md)
