# jqdatasdk 快速开始

## 目录
- [概览](#概览)
- [安装与配置](#安装与配置)
- [认证配置](#认证配置)
- [基础用法](#基础用法)
- [常见问题](#常见问题)

## 概览

jqdatasdk 是聚宽提供的 Python 数据接口，用于获取 A 股、基金、期货等金融数据。它支持实时行情、历史数据、财务数据、因子数据等多种数据类型。

**核心特点：**
- 官方支持，数据质量高
- 覆盖 A 股、基金、期货等全品种
- 提供财务数据、因子数据等深度数据
- 支持实时行情和历史数据

## 安装与配置

### 1. 安装 Python 依赖

```bash
pip install jqdatasdk>=1.9.0 pandas>=1.3.0
```

### 2. 注册聚宽账号

访问 https://www.joinquant.com/ 注册账号。

### 3. 获取 API Token

1. 登录聚宽官网
2. 进入"个人中心"或"设置"
3. 找到"API Token"或"聚宽数据接口"选项
4. 点击"复制"获取你的 Token

**注意：** Token 相当于账号密码，请妥善保管，不要泄露给他人。

## 认证配置

### 使用 Skill 凭证配置

本 Skill 已集成凭证管理功能，首次使用时会提示配置环境变量 `JQDATA_TOKEN` 凭证。

配置步骤：
1. 当智能体调用脚本时，如果检测到未配置凭证，会弹出凭证配置窗口
2. 将你从聚宽官网复制的 Token 粘贴到输入框
3. 凭证配置完成后，脚本会自动读取并使用

### 手动认证方式

如果在本地测试，可以使用以下方式：

```python
import jqdatasdk as jq

# 使用账号密码认证
jq.auth('你的用户名', '你的密码')

# 或者使用 Token 认证（推荐）
jq.auth('你的Token', '你的Token')

# 检查是否认证成功
print(jq.get_query_count())
```

### 认证状态检查

```python
# 查看剩余调用次数
count_info = jq.get_query_count()
print(f"剩余查询次数: {count_info['total'] - count_info['spare']}")
print(f"当日总查询次数: {count_info['total']}")
```

## 基础用法

### 1. 获取股票列表

```python
import jqdatasdk as jq

jq.auth('你的Token', '你的Token')

# 获取所有股票
stocks = jq.get_all_securities(['stock'])
print(stocks.head())

# 获取所有基金
funds = jq.get_all_securities(['fund'])
print(funds.head())

# 获取所有指数
indices = jq.get_all_securities(['index'])
print(indices.head())
```

### 2. 获取价格数据

```python
# 获取单只股票日线数据
df = jq.get_price('000001.XSHE',
                  start_date='2024-01-01',
                  end_date='2024-01-31',
                  frequency='daily')
print(df)

# 获取多只股票日线数据
codes = ['000001.XSHE', '600000.XSHG', '300001.XSHE']
df = jq.get_price(codes,
                  start_date='2024-01-01',
                  end_date='2024-01-31',
                  frequency='daily')
print(df)

# 获取分钟线数据
df = jq.get_price('000001.XSHE',
                  start_date='2024-01-01',
                  end_date='2024-01-02',
                  frequency='1min')
print(df)
```

**支持的频率：**
- 分钟线：1min, 5min, 15min, 30min, 60min, 120min
- 日线：daily
- 周线：weekly
- 月线：monthly

### 3. 获取财务数据

```python
# 查询财务数据
from jqdatasdk import finance

query = finance.query(finance.STK_BALANCE_SHEET.code,
                      finance.STK_BALANCE_SHEET.statDate,
                      finance.STK_BALANCE_SHEET.total_assets)
query = query.filter(finance.STK_BALANCE_SHEET.code == '000001.XSHE')
query = query.filter(finance.STK_BALANCE_SHEET.statDate == '2023')
df = finance.run_query(query)
print(df)

# 查询指标数据
query = finance.query(finance.indicator.code,
                      finance.indicator.statDate,
                      finance.indicator.roe,
                      finance.indicator.pe_ratio)
query = query.filter(finance.indicator.code == '000001.XSHE')
df = finance.run_query(query)
print(df)

# 查询估值数据
query = finance.query(finance.valuation.code,
                      finance.valuation.day,
                      finance.valuation.market_cap,
                      finance.valuation.pe_ratio)
query = query.filter(finance.valuation.code == '000001.XSHE')
df = finance.run_query(query)
print(df)
```

### 4. 获取实时数据

```python
# 获取实时数据
data = jq.get_current_data()
print(data)

# 获取指定股票实时数据
if '000001.XSHE' in data:
    print(f"最新价: {data['000001.XSHE'].last_price}")
    print(f"成交量: {data['000001.XSHE'].volume}")
```

### 5. 获取 Tick 数据

```python
# 获取 Tick 数据
ticks = jq.get_ticks(security='000001.XSHE',
                     start_dt='2024-01-01',
                     end_dt='2024-01-01')
for tick in ticks:
    print(f"{tick.time} 价格:{tick.price} 成交量:{tick.volume}")
```

## 常见问题

### Q1: 认证失败怎么办？

**可能原因：**
1. Token 输入错误
2. 账号未开通聚宽数据服务
3. Token 已过期

**解决方法：**
- 检查 Token 是否正确复制
- 登录聚宽官网确认账号状态
- 重新生成 Token

### Q2: 调用次数限制？

聚宽对不同类型的账号有不同的调用限制：
- 免费账号：每日约 100 万次调用
- 付费账号：更高的调用限制

查看剩余次数：
```python
count_info = jq.get_query_count()
print(count_info)
```

### Q3: 数据为空或错误？

**检查项：**
1. 股票代码格式是否正确（XXXXXX.XSHG 或 XXXXXX.XSHE）
2. 日期范围是否合理
3. 是否在交易时间内（实时数据）
4. 数据是否有延迟

### Q4: 支持哪些市场？

- ✅ A 股（上海、深圳）
- ✅ 基金
- ✅ 指数
- ✅ 期货
- ✅ 期权（部分）

### Q5: 如何获取最新数据？

实时数据：
```python
data = jq.get_current_data()
```

最新收盘价：
```python
df = jq.get_price('000001.XSHE', end_date=None, count=1)
```

### Q6: 复权价格如何获取？

```python
# 前复权（默认）
df = jq.get_price('000001.XSHE',
                  start_date='2024-01-01',
                  end_date='2024-01-31',
                  fq_ref_date='2024-01-31')

# 后复权
df = jq.get_price('000001.XSHE',
                  start_date='2024-01-01',
                  end_date='2024-01-31',
                  fq_ref_date='2024-01-01')

# 不复权
df = jq.get_price('000001.XSHE',
                  start_date='2024-01-01',
                  end_date='2024-01-31',
                  fq_ref_date=None)
```

### Q7: 如何提高数据获取效率？

- 使用批量接口一次获取多只股票
- 合理设置日期范围，避免一次性获取过多数据
- 使用本地缓存减少重复请求
- 优先使用日线数据，分钟线数据获取较慢

### Q8: 数据延迟说明？

- 实时行情：接近实时（毫秒级延迟）
- 日线数据：T+1（交易日收盘后可用）
- 财务数据：根据财报发布时间延迟
- 指标数据：T+1 或更长时间
