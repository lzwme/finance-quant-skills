---
name: jqdatasdk
description: 聚宽（JoinQuant）本地数据 SDK，提供 A 股行情、历史K线、财务数据、指标数据等，与聚宽官网数据同源。当用户提及 jqdatasdk、聚宽数据、需要获取A股数据，或已注册聚宽账号时使用。与 baostock（免费）和 tushare（数据最全）不同，jqdatasdk 需注册聚宽账号获取 Token，适合已在使用聚宽平台的用户。本地数据获取请用本技能，聚宽官网策略开发请用 joinquant-docs 技能。
metadata: {"openclaw":{"emoji":"📈","requires":{"bins":["python3"]}}}
---

# jqdatasdk 聚宽数据获取

## 任务目标
- 本 Skill 用于:通过聚宽数据接口获取A股市场数据、财务指标和因子数据
- 能力包含:实时行情、历史K线、财务数据、指标数据、股票信息、因子数据
- 触发条件:用户提及聚宽、jqdata、jqdatasdk或需要获取A股数据、财务信息、因子数据时

## 前置准备
- 依赖说明:安装 jqdatasdk 库（已包含在 dependency 中）
- 凭证配置:需配置聚宽账号 Token（环境变量: JQDATA_TOKEN）或登录用户名及密码（环境变量: JQDATA_USERNAME、JQDATA_PASSWORD）
- 账号申请:访问 https://www.joinquant.com/ 注册账号并获取 API Token（详见 references/jqdatasdk_quickstart.md）

## 操作步骤
- 标准流程:
  1. 确定数据需求 — 智能体理解用户意图（行情/K线/财务/因子等）
  2. 调用对应脚本 — 根据数据类型选择脚本
  3. 解析结果 — 智能体分析返回的 JSON 格式数据
- 脚本调用映射:
  - 行情/K线/实时数据 → `python scripts/market_data.py --type price --code 000001.XSHE --start 2024-01-01 --end 2024-01-31`
  - 财务数据/指标/估值 → `python scripts/financial_data.py --type fundamentals --code 000001.XSHE --statDate 2024`
  - 股票列表/信息 → `python scripts/stock_info.py --type all_securities --security_type stock`
  - 因子数据 → `python scripts/factor_data.py --code 000001.XSHE --factor valuation --start 2024-01-01 --end 2024-01-31`
- 可选分支:
  - 当需要多只股票数据:使用 --code 参数逗号分隔
  - 当需要指定频率:使用 --frequency 参数（1min/5min/15min/30min/60min/120min/daily/weekly/monthly）
  - 当需要调整价格类型:使用 --fq_ref_date 参数或直接指定复权类型

## 使用示例
- 示例1:获取股票日K线数据
  - 场景/输入:用户说"查看平安银行最近一个月的K线数据"
  - 预期产出:返回日期、开盘价、最高价、最低价、收盘价、成交量等OHLCV数据
  - 关键要点:调用 `python scripts/market_data.py --type price --code 000001.XSHE --start 2024-03-01 --end 2024-03-31 --frequency daily`
- 示例2:查询财务指标
  - 场景/输入:用户说"获取招商银行2023年的财务指标"
  - 预期产出:返回PE、PB、ROE、营业收入、净利润等财务指标
  - 关键要点:调用 `python scripts/financial_data.py --type indicators --code 600036.XSHG --statDate 2023`
- 示例3:获取因子数据
  - 场景/输入:用户说"查询贵州茅台的估值因子"
  - 预期产出:返回市盈率、市净率、市值等估值因子数据
  - 关键要点:调用 `python scripts/factor_data.py --code 600519.XSHG --factor valuation --start 2024-01-01 --end 2024-03-31`

## 快速参考

### 常用代码示例

```python
import jqdatasdk as jq
import pandas as pd

# 认证（需先设置环境变量 JQDATA_TOKEN 或 JQDATA_USERNAME/JQDATA_PASSWORD）
jq.auth(os.environ.get('JQDATA_USERNAME', ''), os.environ.get('JQDATA_PASSWORD', ''))
# 或使用 Token: jq.auth(token='your_token')

# 获取日K线数据
df = jq.get_price('000001.XSHE', start_date='2024-01-01', end_date='2024-12-31',
                  frequency='daily', fields=['open', 'high', 'low', 'close', 'volume'])

# 获取财务数据
q = jq.query(jq.valuation).filter(jq.valuation.code == '000001.XSHE')
fundamentals = jq.get_fundamentals(q, date='2024-01-01')
```

## 资源索引
- 脚本:
  - [scripts/market_data.py](scripts/market_data.py) (用途与参数:获取行情/K线/实时数据，支持 --type/--code/--start/--end/--frequency/--count)
  - [scripts/financial_data.py](scripts/financial_data.py) (用途与参数:获取财务/指标/估值数据，支持 --type/--code/--statDate/--columns)
  - [scripts/stock_info.py](scripts/stock_info.py) (用途与参数:获取股票列表/信息，支持 --type/--security_type/--code)
  - [scripts/factor_data.py](scripts/factor_data.py) (用途与参数:获取因子数据，支持 --code/--factor/--start/--end)
- 参考:
  - [references/jqdatasdk_quickstart.md](references/jqdatasdk_quickstart.md) (何时读取:首次配置或认证失败时)
  - [references/api.md](references/api.md) (何时读取：需要使用聚宽 Python API、查看详细API参数说明时)

## 注意事项
- 脚本执行需配置聚宽账号 Token 或登录用户名及密码，首次使用需先完成凭证配置
- 聚宽股票代码格式:上海市场为 `XXXXXX.XSHG`，深圳市场为 `XXXXXX.XSHE`
- 部分数据（如财务数据）可能有延迟，建议在交易日9:30-15:00之外获取
- 脚本返回 JSON 格式数据，智能体负责解析并转换为用户友好的展示
- 调用频率有限制，避免短时间内大量请求（详见聚宽官方文档）
- 首次使用建议先读取 jqdatasdk_quickstart.md 完成认证配置
