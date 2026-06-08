---
name: tdxquant
description: 通达信量化数据获取技能。当用户提及 tdxquant、通达信、TdxQuant、tqcenter，并且需要获取A股数据（行情快照、K线、财务、板块、可转债、新股、交易数据等）、查询交易日历、执行通达信公式、订阅行情、交易下单时使用
metadata: {"openclaw":{"emoji":"📈","requires":{"bins":["python3"]}}}
---

# 通达信量化数据获取技能

## 任务目标
- 本 Skill 用于：通过通达信 TdxQuant (tqcenter) 接口获取A股市场数据、执行技术分析和查询交易相关信息
- 能力包含：行情快照、K线数据、证券基本信息、专业财务数据、股票/板块/市场交易数据、板块与成份股、可转债/ETF/新股信息、交易日历、通达信公式执行、行情订阅、交易下单
- 触发条件：用户提到 tdxquant、通达信、TdxQuant、tqcenter、获取A股数据、K线查询、财务数据、板块分析等

## 前置准备
- **tqcenter 模块说明**：tqcenter 位于通达信安装目录的 `PYPlugins\user\tqcenter.py`。脚本通过 `_tdx_init.py` 自动检测安装目录并将路径加入 `sys.path`。用户也可以通过设置环境变量 `TDX_ROOT` 指定安装目录。
- 环境要求：需安装通达信金融终端（支持 TQ 策略功能的专业研究版、量化模拟版或期货通），并预先启动客户端
- Python 版本：支持 64 位 Python 3.7~3.14，建议 3.13
- 数据准备：部分数据（如专业财务数据、交易数据）需先在客户端中下载对应数据包

## 核心概念
- **证券代码格式**：6位数字 + 市场后缀（大小写均可），如 `600519.SH`（上海）、`000001.SZ`（深圳）、`430047.BJ`（北交所）
- **周期参数**：`1m`/`5m`/`15m`/`30m`/`1h`/`1d`/`1w`/`1mon`/`1q`/`1y`/`tick`
- **复权类型**：`none` 不复权、`front` 前复权、`back` 后复权
- **市场类型后缀**：`.SH`上海 `.SZ`深圳 `.BJ`北交所 `.HK`港股 `.US`美股 `.CSI`中证指数 `.CNI`国证指数 `.CFF`中金期货 等

**安装目录结构**：

```
通达信安装目录\
├── TdxW.exe              # 主程序
├── PYPlugins\
│   ├── TPyth.dll         # 通信DLL
│   ├── TPythClient.dll   # 通信DLL
│   ├── user\
│   │   └── tqcenter.py   # TdxQuant 核心模块
│   ├── data\             # 下载数据目录
│   └── file\             # 发送文件目录
```

## 操作步骤

1. 确定数据需求 — 智能体理解用户意图
2. 调用对应脚本 — 根据数据类型选择脚本
3. 解析结果 — 智能体分析返回的 JSON 格式数据

### 意图识别映射示例

| 用户提问 | 对应功能模块 | 调用参数 |
|---|---|---|
| "贵州茅台实时股价" | market_data.py snapshot | --code 600519.sh |
| "平安银行K线数据" | market_data.py kline | --code 000001.sz --period 1d |
| "招商银行基本信息" | market_data.py stock_info | --code 600036.sh |
| "招商银行财务指标" | financial_data.py financial | --code 600036.sh --fields fn193,fn197 |
| "半导体板块成分股" | sector_data.py sector_stocks | --block_name 半导体 |
| "今日新股申购" | etf_bond_data.py ipo_info | --ipo_type 2 --ipo_date 1 |
| "市场融资融券数据" | trading_data.py scjy | --fields sc1,sc25 |
| "MACD指标" | formula.py zb | --name MACD --arg 12,26,9 |
| "连涨3天选股" | formula.py xg | --name UPN --arg 3 |

### 使用示例

- 示例1：获取股票实时行情快照
  - 场景/输入：用户说"查看贵州茅台的实时行情"
  - 预期产出：返回股票代码、名称、现价、涨跌幅、成交量、五档买卖等信息
  - 关键要点：调用 `python scripts/market_data.py snapshot --code 600519.sh`
- 示例2：获取日K线数据
  - 场景/输入：用户说"获取平安银行最近100天的日K线数据"
  - 预期产出：返回日期、开盘价、最高价、最低价、收盘价、成交量等OHLCV数据
  - 关键要点：调用 `python scripts/market_data.py kline --code 000001.sz --period 1d --count 100`
- 示例3：查询专业财务数据
  - 场景/输入：用户说"查看招商银行最近的成本费用利润率和营业利润率"
  - 预期产出：返回fn193成本费用利润率、fn194营业利润率等财务指标
  - 关键要点：调用 `python scripts/financial_data.py financial --code 600036.sh --fields fn193,fn194 --start 20240101`

### 脚本调用映射参考

- 行情快照 → `python scripts/market_data.py snapshot --code 600519.sh`
- K线数据 → `python scripts/market_data.py kline --code 600519.sh --period 1d --count 100`
- 证券基本信息 → `python scripts/market_data.py stock_info --code 600519.sh`
- 股票更多信息 → `python scripts/market_data.py more_info --code 600519.sh`
- 分红配送 → `python scripts/market_data.py divid_factors --code 600519.sh`
- 股本数据 → `python scripts/market_data.py gb_info --code 600519.sh --dates 20250101,20250601`
- 专业财务数据 → `python scripts/financial_data.py financial --code 600519.sh --fields fn193,fn194,fn197 --start 20250101`
- 指定日期财务数据 → `python scripts/financial_data.py financial_by_date --code 600519.sh --fields fn193,fn197 --year 0 --mmdd 0`
- 单个财务指标 → `python scripts/financial_data.py gp_one_data --code 600519.sh --fields go1,go3,go5`
- 股票交易数据 → `python scripts/trading_data.py gpjy --code 600519.sh --fields gp1,gp2,gp3 --start 20250101`
- 板块交易数据 → `python scripts/trading_data.py bkjy --code 880660.sh --fields bk5,bk6,bk9 --start 20250101`
- 市场交易数据 → `python scripts/trading_data.py scjy --fields sc1,sc2,sc3 --start 20250101`
- 系统分类成份股 → `python scripts/sector_data.py stock_list --list_type 5`
- 板块代码列表 → `python scripts/sector_data.py sector_list --with_name`
- 板块成份股 → `python scripts/sector_data.py sector_stocks --block_code 880081.sh`
- 股票所属板块 → `python scripts/sector_data.py stock_relation --code 688318.sh`
- 自定义板块操作 → `python scripts/sector_data.py user_sector --action list`
- 可转债信息 → `python scripts/etf_bond_data.py kzz_info --code 123039.sz`
- ETF跟踪指数 → `python scripts/etf_bond_data.py trackzs_etf --zs_code 950162.csi`
- 新股申购 → `python scripts/etf_bond_data.py ipo_info --ipo_type 2 --ipo_date 1`
- 交易日列表 → `python scripts/calendar.py --start 20250101 --end 20250601`
- 通达信公式(指标) → `python scripts/formula.py zb --name MACD --arg 12,26,9 --code 688318.sh --period 1d --count 100`
- 通达信公式(选股) → `python scripts/formula.py xg --name UPN --arg 3 --code 688318.sh --period 1d --count 100`
- 批量选股公式 → `python scripts/formula.py mul_xg --name UPN --arg 3 --codes 688318.sh,600519.sh --period 1d --count 20`

## 资源索引

### 数据获取脚本

- [scripts/market_data.py](scripts/market_data.py) (用途与参数：行情快照snapshot、K线kline、基本信息stock_info、更多信息more_info、分红divid_factors、股本gb_info)
- [scripts/financial_data.py](scripts/financial_data.py) (用途与参数：专业财务financial、指定日期财务financial_by_date、单个指标gp_one_data)
- [scripts/trading_data.py](scripts/trading_data.py) (用途与参数：股票交易gpjy、板块交易bkjy、市场交易scjy及其by_date变体)
- [scripts/sector_data.py](scripts/sector_data.py) (用途与参数：系统分类stock_list、板块列表sector_list、板块成份股sector_stocks、股票所属板块stock_relation、自定义板块user_sector)
- [scripts/etf_bond_data.py](scripts/etf_bond_data.py) (用途与参数：可转债kzz_info、ETF跟踪trackzs_etf、新股申购ipo_info)
- [scripts/calendar.py](scripts/calendar.py) (用途与参数：获取交易日列表，支持 --start/--end/--count)
- [scripts/formula.py](scripts/formula.py) (用途与参数：通达信公式执行，支持zb指标/xg选股/exp专家/mul批量)
- [scripts/trade.py](scripts/trade.py) (用途与参数：交易下单、查询持仓/委托/资产、撤单)

### 扩展参考

- [Python 初始化指引](references/python-init.md) (何时读取：需要写 python 脚本自定义获取更多的数据时)
- [API 使用示例与故障排除](references/tq_use_case.md) (何时读取：需要查看常见用法时。提供了八种常见数据查询示例)
- [tqcenter API](references/tq_api.md) (何时读取：需要查看完整API参数、字段说明、初始化配置时，**此为最核心参考文档**)
- [常量字典](references/dict.md) (何时读取：需要查看市场类型、周期、复权类型等常量映射时)
- [策略开发与回测指引](references/backtest.md) (何时读取：需要写策略、执行策略回测时)

## 注意事项

- 运行脚本前，必须先启动通达信金融终端（支持TQ策略功能的版本），且 TdxW.exe 进程正在运行
- 如果安装目录下不存在 `tqcenter.py`，说明当前客户端不支持TQ策略，需升级通达信终端
- 证券代码必须带市场后缀（如 `.SH`、`.SZ`、`.BJ`），大小写均可，但不可省略
- 专业财务数据和交易数据需先在客户端中下载对应数据包
- 部分数据（如交易数据中的融资融券、陆股通等）仅展示特定日期之后的数据
- K线数据一次最多返回24000条，获取完整分钟线需多次分批获取
- 通达信公式执行时，公式名称和参数需符合通达信语法规范
- 后复权数据与获取的数据个数有关，只在返回的数据中进行后复权
- 使用 `sys.path.insert(0, ...)` 而非 `append()`，确保优先加载通达信安装目录的 tqcenter.py
