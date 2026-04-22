---
name: tushare
description: A股行情、历史K线、财务数据、宏观数据等证券财经信息获取；当用户提及Tushare或需要获取A股数据时使用
dependency:
  python:
    - tushare>=1.2.60
    - pandas>=1.3.0
  system: []
---

# Tushare 数据获取

## 任务目标
- 本 Skill 用于:通过 Tushare 数据接口获取 A 股市场数据、财务指标和宏观数据
- 能力包含:实时行情、历史K线、财务数据、指标数据、股票信息、宏观数据、指数数据
- 触发条件:用户提及 Tushare 或需要获取 A 股数据、财务信息、宏观数据时

## 前置准备
- 依赖说明:安装 tushare 库（已包含在 dependency 中）
- 凭证配置:需配置 Tushare Token（凭证名: TUSHARE_TOKEN，环境变量: TUSHARE_TOKEN）
- 账号申请:访问 https://tushare.pro/ 注册账号并获取 API Token（详见 references/tushare_quickstart.md）

## 操作步骤
- 标准流程:
  1. 确定数据需求 — 智能体理解用户意图（行情/K线/财务/宏观/指数等）
  2. 调用对应脚本 — 根据数据类型选择脚本
  3. 解析结果 — 智能体分析返回的 JSON 格式数据
- 脚本调用映射:
  - 行情/K线/复权数据 → `python scripts/market_data.py --type daily --ts_code 000001.SZ --start_date 20240101 --end_date 20240131`
  - 财务数据/利润表/资产负债表 → `python scripts/financial_data.py --type financial --ts_code 000001.SZ --period 2023`
  - 股票列表/交易日历 → `python scripts/stock_info.py --type stock_basic`
  - 指数数据/宏观数据 → `python scripts/macro_index_data.py --type index_daily --ts_code 000001.SH --start_date 20240101 --end_date 20240131`
- 可选分支:
  - 当需要多只股票数据:使用 --ts_code 参数逗号分隔
  - 当需要复权数据:使用 --type adj_factor 获取复权因子
  - 当需要指定报告期:使用 --period 参数（YYYY 或 YYYYMM）

## 使用示例
- 示例1:获取股票日K线数据
  - 场景/输入:用户说"查看平安银行最近一个月的K线数据"
  - 预期产出:返回日期、开盘价、最高价、最低价、收盘价、成交量等OHLCV数据
  - 关键要点:调用 `python scripts/market_data.py --type daily --ts_code 000001.SZ --start_date 20240301 --end_date 20240331`
- 示例2:查询财务数据
  - 场景/输入:用户说"获取招商银行2023年的财务指标"
  - 预期产出:返回ROE、ROA、毛利率、净利率等财务指标
  - 关键要点:调用 `python scripts/financial_data.py --type fina_indicator --ts_code 600036.SH --period 2023`
- 示例3:获取指数数据
  - 场景/输入:用户说"查询上证指数最近的走势"
  - 预期产出:返回上证指数的日期、收盘价、成交量等数据
  - 关键要点:调用 `python scripts/macro_index_data.py --type index_daily --ts_code 000001.SH --start_date 20240301 --end_date 20240331`

## 资源索引
- 脚本:
  - [scripts/market_data.py](scripts/market_data.py) (用途与参数:获取行情/K线/复权数据，支持 --type/--ts_code/--start_date/--end_date)
  - [scripts/financial_data.py](scripts/financial_data.py) (用途与参数:获取财务数据/利润表/资产负债表/现金流量表/指标，支持 --type/--ts_code/--period)
  - [scripts/stock_info.py](scripts/stock_info.py) (用途与参数:获取股票列表/交易日历/名称变更，支持 --type/--ts_code/--start_date/--end_date)
  - [scripts/macro_index_data.py](scripts/macro_index_data.py) (用途与参数:获取指数数据/宏观数据/Shibor，支持 --type/--ts_code/--start_date/--end_date)
- 参考:
  - [references/tushare_quickstart.md](references/tushare_quickstart.md) (何时读取:首次配置或认证失败时)
  - [references/api_reference.md](references/api_reference.md) (何时读取:需要查看详细API参数说明时)

## 注意事项
- 脚本执行需配置 Tushare Token，首次使用需先完成凭证配置
- Tushare 股票代码格式:上海市场为 XXXXXX.SH，深圳市场为 XXXXXX.SZ
- 部分数据（如财务数据）可能有延迟，建议在交易日9:30-15:00之外获取
- 脚本返回 JSON 格式数据，智能体负责解析并转换为用户友好的展示
- 调用频率有限制，免费账户每分钟最多120次调用（详见 Tushare 官方文档）
- 首次使用建议先读取 tushare_quickstart.md 完成认证配置
