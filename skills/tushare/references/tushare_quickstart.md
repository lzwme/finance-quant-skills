# Tushare 快速开始

## 目录
- [概览](#概览)
- [安装与配置](#安装与配置)
- [认证配置](#认证配置)
- [基础用法](#基础用法)
- [常见问题](#常见问题)

## 概览

Tushare 是一个免费、开源的财经数据接口包，主要用于获取中国股票市场数据。它提供包括行情、财务、宏观数据等多种类型的金融数据。

**核心特点：**
- 免费开源，社区活跃
- 数据覆盖全面，支持 A 股、指数、基金、期货等
- 提供 API 接口和 Python SDK
- 数据质量高，更新及时

## 安装与配置

### 1. 安装 Python 依赖

```bash
pip install tushare>=1.2.60 pandas>=1.3.0
```

### 2. 注册 Tushare 账号

访问 https://tushare.pro/ 注册账号。

### 3. 获取 API Token

1. 登录 Tushare 官网
2. 进入"个人中心"或"用户中心"
3. 找到"接口 Token"选项
4. 复制你的 Token

**注意：** Token 相当于账号密码，请妥善保管，不要泄露给他人。

## 认证配置

### 使用 Skill 凭证配置

本 Skill 已集成凭证管理功能，首次使用时会提示配置 `TUSHARE_TOKEN` 凭证。

配置步骤：
1. 当智能体调用脚本时，如果检测到未配置凭证，会弹出凭证配置窗口
2. 将你从 Tushare 官网复制的 Token 粘贴到输入框
3. 凭证配置完成后，脚本会自动读取并使用

### 手动认证方式

如果在本地测试，可以使用以下方式：

```python
import tushare as ts

# 设置 Token
pro = ts.pro_api('你的Token')

# 测试连接
df = pro.trade_cal(exchange='SSE', start_date='20240101', end_date='20240110')
print(df)
```

## 基础用法

### 1. 获取股票列表

```python
import tushare as ts

pro = ts.pro_api('你的Token')

# 获取所有股票列表
df = pro.stock_basic(exchange='', list_status='L')
print(df.head())

# 获取上交所股票
df = pro.stock_basic(exchange='SSE', list_status='L')
print(df)

# 获取特定股票信息
df = pro.stock_basic(ts_code='600000.SH')
print(df)
```

### 2. 获取日线行情

```python
# 获取单只股票日线数据
df = pro.daily(ts_code='000001.SZ',
               start_date='20240101',
               end_date='20240131')
print(df)

# 获取多只股票日线数据
df = pro.daily(ts_code='000001.SZ,600000.SH',
               start_date='20240101',
               end_date='20240131')
print(df)

# 获取指定交易日数据
df = pro.daily(trade_date='20240101')
print(df)
```

### 3. 获取复权因子

```python
# 获取复权因子
df = pro.adj_factor(ts_code='000001.SZ',
                    start_date='20240101',
                    end_date='20240131')
print(df)
```

### 4. 获取财务数据

```python
# 获取利润表
df = pro.income(ts_code='000001.SZ',
                period='2023',
                report_type='1')
print(df)

# 获取资产负债表
df = pro.balancesheet(ts_code='000001.SZ',
                      period='2023',
                      report_type='1')
print(df)

# 获取现金流量表
df = pro.cashflow(ts_code='000001.SZ',
                  period='2023',
                  report_type='1')
print(df)

# 获取财务指标
df = pro.fina_indicator(ts_code='000001.SZ',
                        period='2023')
print(df)
```

### 5. 获取指数数据

```python
# 获取指数基础信息
df = pro.index_basic(market='SSE')
print(df)

# 获取指数行情
df = pro.index_daily(ts_code='000001.SH',
                     start_date='20240101',
                     end_date='20240131')
print(df)

# 获取上证指数
df = pro.index_daily(ts_code='000001.SH',
                     start_date='20240101',
                     end_date='20240131')
print(df)
```

### 6. 获取交易日历

```python
# 获取交易日历
df = pro.trade_cal(exchange='SSE',
                   start_date='20240101',
                   end_date='20240131')
print(df)

# 获取开市日期
df = pro.trade_cal(exchange='SSE',
                   start_date='20240101',
                   end_date='20240131',
                   is_open='1')
print(df)
```

### 7. 获取宏观数据

```python
# 获取 Shibor 数据
df = pro.shibor(start_date='20240101',
                end_date='20240131')
print(df)

# 获取 Shibor 利率
df = pro.shibor_rate(start_date='20240101',
                     end_date='20240131')
print(df)
```

## 常见问题

### Q1: 认证失败怎么办？

**可能原因：**
1. Token 输入错误
2. Token 已过期
3. 账号未激活

**解决方法：**
- 检查 Token 是否正确复制
- 登录 Tushare 官网确认账号状态
- 重新生成 Token

### Q2: 调用次数限制？

Tushare 对不同类型的账号有不同的调用限制：
- 免费账户：每分钟最多 120 次调用
- 付费账户：更高的调用限制

查看当前调用次数：
```python
# 查看账户信息
# 需要根据 Tushare 官方提供的接口查询
```

### Q3: 数据为空或错误？

**检查项：**
1. 股票代码格式是否正确（XXXXXX.SH 或 XXXXXX.SZ）
2. 日期范围是否合理
3. 数据是否有延迟
4. 是否有权限访问该数据（部分数据需要付费）

### Q4: 支持哪些市场？

- ✅ A 股（上海、深圳）
- ✅ 指数
- ✅ 基金
- ✅ 期货
- ✅ 期权（部分）
- ✅ 港股（部分）
- ✅ 宏观数据

### Q5: 股票代码格式说明？

- 上海市场：`XXXXXX.SH`（如 600000.SH）
- 深圳市场：`XXXXXX.SZ`（如 000001.SZ）
- 北交所：`XXXXXX.BJ`（如 832566.BJ）

### Q6: 如何获取最新数据？

最新交易日数据：
```python
# 获取最新交易日
import datetime
today = datetime.datetime.now().strftime('%Y%m%d')
df = pro.daily(trade_date=today)
print(df)
```

### Q7: 财务数据报告期说明？

财务数据支持多种报告期：
- 年报：`2023` 或 `202312`
- 中报：`2023` 或 `202306`
- 季报：`2023Q1`、`2023Q2`、`2023Q3`、`2023Q4`

### Q8: 如何提高数据获取效率？

- 使用批量接口一次获取多只股票
- 合理设置日期范围，避免一次性获取过多数据
- 使用本地缓存减少重复请求
- 优先获取需要的字段，减少数据传输量

### Q9: Tushare Pro 社区版权限？

社区版（免费）权限：
- 每分钟 120 次调用
- 基础行情数据
- 财务数据（延迟）
- 指数数据
- 部分宏观数据

付费版本权限更高，详见 Tushare 官方文档。

### Q10: 数据更新频率说明？

- 日线行情：T+1（交易日收盘后更新）
- 分钟线行情：需要付费权限
- 财务数据：根据财报发布时间更新
- 指数数据：实时或 T+1
- 宏观数据：根据发布时间更新
