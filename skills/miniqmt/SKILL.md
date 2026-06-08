---
name: miniqmt
description: MiniQMT 迅投量化交易接口，基于 XtQuant Python 库，支持 A 股/期货/期权的行情数据获取（K线、分笔、财务数据等）和交易下单（报单、撤单、查询资产/委托/持仓）。当用户提及 miniqmt、xtquant、迅投、获取实时行情、量化交易下单、回测数据获取，或需要连接 MiniQMT 客户端进行程序化交易时使用
metadata: {"openclaw":{"emoji":"📈","requires":{"bins":["python3"]}}}
---

# MiniQMT 量化交易技能

## 任务目标
- 本 Skill 用于：通过 XtQuant 库连接 MiniQMT 客户端，获取 A 股/期货/期权行情数据，执行量化交易操作
- 能力包含：
  - **行情模块 (xtdata)**：K线数据、分笔数据、实时行情订阅、财务数据、板块分类、ETF信息、新股申购、交易日历
  - **交易模块 (xttrader)**：股票/期货/期权下单、撤单、查询资产/委托/持仓、资金划拨、信用交易、约券
- 触发条件：用户提及 miniqmt、xtquant、迅投、获取行情、量化交易、下单交易时使用

## 前置准备

### MiniQMT 环境要求
- **客户端安装**：需安装迅投极速交易终端，并启动 MiniQMT（支持模拟/实盘）
- **Python 库**：`pip install xtquant`
- **路径配置**：MiniQMT 安装目录下的 `userdata_mini` 路径用于 xttrader 连接

### 目录结构
```
QMT安装目录\
├── bin.x64\XtMiniQmt.exe # MiniQMT 主程序
├── userdata_mini\        # 用户数据目录（xttrader 连接路径）
│   ├── xqtrader.ini      # 交易配置
│   └── xtdatacenter.ini  # 行情配置
```

### 核心概念

#### 证券代码格式
- **股票**：6位数字 + 市场后缀，如 `600000.SH`（上海）、`000001.SZ`（深圳）
- **期货**：品种代码 + 合约月份，如 `rb2405.SF`（螺纹钢）
- **期权**：标的代码 + 行权月份，如 `510050.SH`（上证50ETF期权）

#### 周期类型 (period)
| 周期 | 说明 | 周期 | 说明 |
|------|------|------|------|
| `tick` | 分笔数据 | `1q` | 季度线 |
| `1m` | 1分钟线 | `1hy` | 半年线 |
| `5m` | 5分钟线 | `1y` | 年线 |
| `15m` | 15分钟线 | `1w` | 周线 |
| `30m` | 30分钟线 | `1d` | 日线 |
| `1h` | 1小时线 | `1mon` | 月线 |

#### 复权类型 (dividend_type)
- `none` - 不复权
- `front` - 前复权
- `back` - 后复权
- `front_ratio` - 等比前复权
- `back_ratio` - 等比后复权

#### 交易市场 (market)
| 市场 | 常量 | 市场 | 常量 |
|------|------|------|------|
| 上海 | `xtconstant.SH_MARKET` | 中金所 | `xtconstant.MARKET_ENUM_INDEX_FUTURE` |
| 深圳 | `xtconstant.SZ_MARKET` | 上期所 | `xtconstant.MARKET_ENUM_SHANGHAI_FUTURE` |
| 北交所 | `xtconstant.MARKET_ENUM_BEIJING` | 郑商所 | `xtconstant.MARKET_ENUM_ZHENGZHOU_FUTURE` |
| 大商所 | `xtconstant.MARKET_ENUM_DALIANG_FUTURE` | 广期所 | `xtconstant.MARKET_ENUM_GUANGZHOU_FUTURE` |

#### 账号类型 (account_type)
| 类型 | 常量 | 类型 | 常量 |
|------|------|------|------|
| 股票 | `xtconstant.SECURITY_ACCOUNT` | 沪港通 | `xtconstant.HUGANGTONG_ACCOUNT` |
| 期货 | `xtconstant.FUTURE_ACCOUNT` | 深港通 | `xtconstant.SHENGANGTONG_ACCOUNT` |
| 信用 | `xtconstant.CREDIT_ACCOUNT` | 期货期权 | `xtconstant.FUTURE_OPTION_ACCOUNT` |
| 股票期权 | `xtconstant.STOCK_OPTION_ACCOUNT` | - | - |

## 操作步骤

1. **确定需求** — 识别是行情数据获取还是交易操作
2. **选择模块** — xtdata 用于行情，xttrader 用于交易
3. **调用脚本** — 根据数据类型选择对应脚本
4. **解析结果** — 智能体分析返回的 JSON 格式数据

### 意图识别映射示例

| 用户提问 | 对应功能 | 调用方式 |
|---------|---------|---------|
| "贵州茅台实时股价" | 实时行情快照 | xtdata.get_full_tick |
| "平安银行K线数据" | K线数据 | xtdata.get_market_data |
| "招商银行财务指标" | 财务报表 | xtdata.get_financial_data |
| "半导体板块成分股" | 板块成分股 | xtdata.get_stock_list_in_sector |
| "今日可转债信息" | ETF/可转债数据 | xtdata.get_cb_info |
| "新股申购" | 新股信息 | xtdata.get_ipo_info |
| "下单买入平安银行" | 交易下单 | xttrader.order_stock |
| "查询持仓" | 持仓查询 | xttrader.query_stock_positions |
| "撤单" | 撤单操作 | xttrader.cancel_order_stock |

## 使用示例

### 示例1：获取股票实时行情
```python
import xtdata

# 获取全推行情快照
ticks = xtdata.get_full_tick(['600519.SH', '000001.SZ'])

# 订阅单股实时行情
def on_data(datas):
    for code in datas:
        print(code, datas[code])

xtdata.subscribe_quote('600519.SH', period='tick', callback=on_data)
xtdata.run()
```

### 示例2：获取K线历史数据
```python
import xtdata

# 下载历史K线数据
xtdata.download_history_data2(['600519.SH'], period='1d', start_time='')

# 获取K线数据
data = xtdata.get_market_data(
    field_list=['open', 'high', 'low', 'close', 'volume'],
    stock_list=['600519.SH'],
    period='1d',
    start_time='20240101',
    end_time='',
    count=100,
    dividend_type='front'
)
```

### 示例3：交易下单
```python
from xtquant.xttrader import XtQuantTrader, XtQuantTraderCallback
from xtquant.xttype import StockAccount
from xtquant import xtconstant

# 配置路径和会话
path = 'D:\\迅投极速交易终端\\userdata_mini'
session_id = 123456
xt_trader = XtQuantTrader(path, session_id)

# 创建账号对象
acc = StockAccount('1000000365')  # 替换为实际账号

# 连接交易
xt_trader.start()
connect_result = xt_trader.connect()
subscribe_result = xt_trader.subscribe(acc)

# 下单买入
order_id = xt_trader.order_stock(
    acc,
    '600519.SH',
    xtconstant.STOCK_BUY,
    100,  # 100股
    xtconstant.FIX_PRICE,
    1800.0,  # 价格
    'strategy1',
    'remark'
)

# 查询资产
asset = xt_trader.query_stock_asset(acc)
print(f"可用资金: {asset.cash}")
```

### 示例4：订阅行情并实时处理
```python
import xtdata

def on_tick_data(datas):
    for code in datas:
        tick = datas[code]
        print(f"{code}: 现价={tick['lastPrice']}, 成交量={tick['volume']}")

# 订阅多只股票
xtdata.subscribe_whole_quote(['SH', 'SZ'], callback=on_tick_data)
xtdata.run()
```

## 资源索引

### 行情数据脚本

- **行情快照**：`python scripts/market_data.py snapshot --code 600519.SH`
- **K线数据**：`python scripts/market_data.py kline --code 600519.SH --period 1d --count 100`
- **分笔数据**：`python scripts/market_data.py tick --code 600519.SH --count 100`
- **实时行情**：`python scripts/market_data.py full_tick --codes 600519.SH,000001.SZ`

### 板块与财务脚本

- **板块列表**：`python scripts/sector_data.py sector_list`
- **板块成分股**：`python scripts/sector_data.py sector_stocks --sector 半导体`
- **财务数据**：`python scripts/financial_data.py financial --code 600519.SH --tables Balance,Income`

### 交易脚本

- **下单**：`python scripts/trade.py order --code 600519.SH --type buy --volume 100 --price 1800.0`
- **撤单**：`python scripts/trade.py cancel --order_id 12345`
- **查询持仓**：`python scripts/trade.py positions`
- **查询委托**：`python scripts/trade.py orders`
- **查询资产**：`python scripts/trade.py asset`
- **查询成交**：`python scripts/trade.py trades`

### 参考文档

- [xtdata 行情模块 API](references/xtdata.md)（何时读取：需要查看行情数据接口时）
- [xtdata行情数据字段与数据字典](references/xtdata_dict.md) （何时读取：需要查看行情数据字段、数据字典时）
- [xttrader 交易模块 API](references/xttrader.md)（何时读取：需要查看交易接口、数据结构说明时）
- [安装与下载指南](references/download_xtquant.md)（何时读取：首次安装 XtQuant 或遇到安装问题时）
- [常见问题](references/question_function.md)（何时读取：遇到常见问题时）
- [代码示例](references/code_examples.md)（何时读取：需要参考完整代码示例时）
- [更新日志](references/changelog.md)（何时读取：查看版本更新历史时）

## 注意事项

### 环境要求
- **必须运行 MiniQMT**：xttrader 交易模块需要 MiniQMT 客户端在后台运行
- **路径配置**：确保 `userdata_mini` 路径正确，否则连接会失败
- **行情订阅限制**：单股订阅建议不超过 50 只，较多时建议使用全推数据

### 数据获取注意
- **数据补下载**：历史数据需先通过 `download_history_data2` 下载
- **权限限制**：Level2 数据需要终端有相应权限
- **时间格式**：K线时间参数格式为 `'20240101'` 或 `'20240101000000'`

### 交易注意
- **账号格式**：股票账号直接使用资金账号字符串，期货账号需指定 `'FUTURE'`
- **委托数量**：股票以"股"为单位，债券以"张"为单位，期货以"手"为单位
- **订单编号**：下单成功后返回正整数 order_id，-1 表示失败
- **异步操作**：交易操作支持同步/异步两种模式，异步模式需配合回调使用

### 性能优化
- **批量请求**：多只股票数据建议使用 `get_market_data` 批量获取
- **缓存利用**：已订阅的数据会自动缓存，无需重复订阅
- **线程安全**：xttrader 支持多策略，但需使用不同的 session_id
