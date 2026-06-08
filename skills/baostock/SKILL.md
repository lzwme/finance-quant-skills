---
name: baostock
description: BaoStock 免费开源 A 股数据平台，无需注册、无需 API Key，支持股票行情、K线、财务数据、行业分类、指数成分股查询。当用户提及 baostock、需要获取A股历史行情、财务报表、交易日历，或需要**免费、免注册**的A股数据时使用。与 tushare（数据更全但需注册）和 jqdatasdk（聚宽数据）不同，baostock 完全免费无限制，适合快速入门和低成本数据需求。
metadata: {"openclaw":{"emoji":"📈","requires":{"bins":["python3"]}}}
---

# baostock A股数据获取

## 任务目标
- 本 Skill 用于：通过 BaoStock 接口获取 A 股市场数据、财务指标和股票信息
- 能力包含：历史 K 线、财务数据、股票信息、行业分类、指数成分股、交易日历
- 触发条件：用户提及 baostock 或需要获取 A 股免费数据、历史行情、财务信息时

## 前置准备
- 依赖说明：安装 baostock 库（已包含在 dependency 中）
- 凭证配置：BaoStock 无需注册或 API Key，直接调用即可使用
- 可选配置：支持通过环境变量自定义服务器地址（用于代理场景）
  - `BAOSTOCK_SERVER_IP`：自定义服务器 IP（用于 nginx 代理等场景）
  - `BAOSTOCK_SERVER_PORT`：服务器端口，默认 10030

## 操作步骤
- 标准流程：
  1. 确定数据需求 — 智能体理解用户意图（行情/K线/财务/股票信息等）
  2. 调用对应脚本 — 根据数据类型选择脚本
  3. 解析结果 — 智能体分析返回的 JSON 格式数据
- 脚本调用映射：
  - K线/行情数据 → `python scripts/market_data.py --type kline --code sh.600000 --start 2024-01-01 --end 2024-01-31`
  - 财务数据 → `python scripts/financial_data.py --type profit --code sh.600000 --year 2023 --quarter 4`
  - 股票列表/信息 → `python scripts/stock_info.py --type all_stocks --date 2024-01-02`
  - 指数成分股 → `python scripts/stock_info.py --type index_stocks --index hs300`
  - 行业分类 → `python scripts/stock_info.py --type industry`
  - 交易日历 → `python scripts/stock_info.py --type trade_dates --start 2024-01-01 --end 2024-12-31`
- 可选分支：
  - 当需要多只股票数据：使用逗号分隔多个代码，或使用 `--file` 指定代码列表文件
  - 当需要指定频率：使用 `--frequency` 参数（d/w/m/5/15/30/60）
  - 当需要调整复权类型：使用 `--adjust` 参数（1=后复权，2=前复权，3=不复权）

## 使用示例
- 示例1：获取股票日K线数据
  - 场景/输入：用户说"查看贵州茅台最近一个月的K线数据"
  - 预期产出：返回日期、开盘价、最高价、最低价、收盘价、成交量等 OHLCV 数据
  - 关键要点：调用 `python scripts/market_data.py --type kline --code sh.600519 --start 2024-03-01 --end 2024-03-31 --frequency d --adjust 2`
- 示例2：查询财务指标
  - 场景/输入：用户说"获取工商银行2023年的盈利能力指标"
  - 预期产出：返回 ROE、净利润率、毛利率等财务指标
  - 关键要点：调用 `python scripts/financial_data.py --type profit --code sh.601398 --year 2023 --quarter 4`
- 示例3：获取沪深300成分股
  - 场景/输入：用户说"查询沪深300指数的成分股列表"
  - 预期产出：返回沪深300指数的所有成分股代码和名称
  - 关键要点：调用 `python scripts/stock_info.py --type index_stocks --index hs300`
- 示例4：批量下载多只股票数据
  - 场景/输入：用户说"下载茅台、平安、招行的2024年日K线数据"
  - 预期产出：返回多只股票的 K 线数据并保存为 CSV
  - 关键要点：调用 `python scripts/market_data.py --type kline --code sh.600519,sz.000001,sh.600036 --start 2024-01-01 --end 2024-12-31 --output stocks.csv`

## 快速参考

### 常用代码示例

```python
import baostock as bs
import pandas as pd

# 登录系统
lg = bs.login()

# 获取日K线数据
rs = bs.query_history_k_data_plus(
    "sh.600519",
    "date,code,open,high,low,close,volume,amount",
    start_date='2024-01-01', end_date='2024-12-31',
    frequency="d", adjustflag="2"
)

# 转换为 DataFrame
data_list = []
while (rs.error_code == '0') & rs.next():
    data_list.append(rs.get_row_data())
df = pd.DataFrame(data_list, columns=rs.fields)

# 登出系统
bs.logout()
```

### 与其他数据源对比

| 特性 | baostock | tushare | jqdatasdk | akshare |
|------|----------|---------|-----------|---------|
| 费用 | 免费 | 免费/付费 | 需注册积分 | 免费 |
| 注册要求 | ❌ 不需要 | ✅ 需要 | ✅ 需要 | ❌ 不需要 |
| 数据范围 | A股为主 | 全面（含宏观） | A股+因子 | 全面（含加密货币） |
| K线数据 | ✅ | ✅ | ✅ | ✅ |
| 财务数据 | ✅ | ✅ | ✅ | ✅ |
| 分钟线 | ✅ | ✅ | ✅ | ✅ |
| 实时行情 | ❌ | ❌ | ❌ | ✅ |
| 特色数据 | 交易日历 | 宏观/Shibor | 因子数据 | 龙虎榜/北向/加密货币 |

## 资源索引
### 脚本：

- [scripts/market_data.py](scripts/market_data.py)（用途与参数：获取 K 线/行情数据，支持 --type/--code/--start/--end/--frequency/--adjust/--fields/--output）
- [scripts/financial_data.py](scripts/financial_data.py)（用途与参数：获取财务数据，支持 --type/--code/--year/--quarter/--output）
- [scripts/stock_info.py](scripts/stock_info.py)（用途与参数：获取股票列表/信息/行业/指数成分股，支持 --type/--date/--code/--index/--output）
- [scripts/auth.py](scripts/auth.py)（用途与参数：认证模块，支持自定义服务器配置）

### 参考文档

- [常用API文档](references/api.md)（何时读取：需要使用 BaoStock Python API、查看详细 API 参数说明时）
- [知识库文档目录](references/markdown/index.md)（何时读取：需要查看更为全面详细 API 参数说明时）

## 注意事项
- BaoStock 无需注册或 API Key，直接调用 `bs.login()` 即可使用
- BaoStock 股票代码格式：`sh.600000`（上海）、`sz.000001`（深圳）、`bj.430047`（北京）
- 部分数据（如财务数据）可能有延迟，建议在交易日 9:30-15:00 之外获取
- 脚本返回 JSON 格式数据，智能体负责解析并转换为用户友好的展示
- 每个会话必须以 `bs.login()` 开始、`bs.logout()` 结束
- K 线数据默认返回字符串类型，数值计算前需用 `.astype(float)` 转换
- 非线程安全，并行下载请使用多进程而非多线程
- 财务数据按季度提供，报告期结束后约有 2 个月的延迟
