# AKShare 基金数据 API 参考

## 主要功能

AKShare 提供全面的基金数据获取功能，包括ETF、开放式基金、货币基金、基金评级等。

## 核心API接口

### ETF基金数据

#### ETF实时行情

```python
# 获取ETF实时行情
ak.fund_etf_spot_em()
```

**返回字段：**
- 代码、名称、最新价、涨跌幅、涨跌额、成交量、成交额、振幅、最高、最低、今开、昨收、换手率等

#### ETF历史K线

```python
# 获取ETF历史K线数据
ak.fund_etf_hist_em(
    symbol="510300",       # ETF代码
    period="daily",        # 周期: "daily", "weekly", "monthly"
    start_date="20240101", # 开始日期
    end_date="20240630",   # 结束日期
    adjust="qfq"           # 复权: "", "qfq", "hfq"
)
```

**返回字段：**
- 日期、开盘、收盘、最高、最低、成交量、成交额、涨跌幅等

### 开放式基金数据

#### 开放式基金每日净值

```python
# 获取开放式基金每日净值
ak.fund_open_fund_daily_em(symbol="000001")
```

**返回字段：**
- 基金代码、基金名称、净值日期、单位净值、累计净值、日增长率等

#### 开放式基金列表

```python
# 获取开放式基金列表
ak.fund_open_fund_rank_em()
```

### 基金评级数据

```python
# 获取基金评级
ak.fund_rating_all()
```

**返回字段：**
- 基金代码、基金名称、评级机构、评级、评级日期等

### 基金持仓信息

```python
# 获取基金持仓信息
ak.fund_portfolio_hold_em(symbol="000001")
```

**返回字段：**
- 基金代码、股票代码、股票名称、持仓比例、持股数量等

### 基金经理信息

```python
# 获取基金经理信息
ak.fund_manager()
```

**返回字段：**
- 基金代码、基金名称、基金经理、从业时间、管理规模等

### 货币基金数据

```python
# 获取货币基金信息
ak.fund_money_fund_em()
```

**返回字段：**
- 基金代码、基金名称、万份收益、七日年化收益率等

### 基金规模信息

```python
# 获取基金规模信息
ak.fund_scale_open_em()
```

**返回字段：**
- 基金代码、基金名称、基金规模、基金规模变化等

### 新发基金信息

```python
# 获取新发基金信息
ak.fund_new_found_em()
```

**返回字段：**
- 基金代码、基金名称、成立日期、基金类型等

## 基金分类数据

### 股票型基金

```python
# 股票型基金排行
ak.fund_stock_open_em()
```

### 债券型基金

```python
# 债券型基金排行
ak.fund_bond_open_em()
```

### 混合型基金

```python
# 混合型基金排行
ak.fund_mixed_open_em()
```

### QDII基金

```python
# QDII基金排行
ak.fund_qdii_em()
```

## 基金净值数据

### 基金净值走势

```python
# 获取基金净值走势
ak.fund_value_hist_em(symbol="000001")
```

### 基金累计净值

```python
# 获取基金累计净值
ak.fund_accumulated_net_em(symbol="000001")
```

## 基金分红信息

```python
# 获取基金分红信息
ak.fund_dividend_em(symbol="000001")
```

**返回字段：**
- 基金代码、基金名称、分红年度、权益登记日、除息日、分红金额等

## 基金行业配置

```python
# 获取基金行业配置
ak.fund_portfolio_industry_allocation_em(symbol="000001")
```

## 使用注意事项

1. **基金代码格式：**
   - ETF基金：5/6位数字代码（如510300）
   - 开放式基金：6位数字代码（如000001）
   - LOF基金：5/6位数字代码

2. **净值更新频率：**
   - 交易日净值：T+1日更新
   - 货币基金：每日更新
   - 分红信息：分红公告后更新

3. **数据延迟：**
   - 实时行情：可能有15分钟延迟
   - 历史净值：交易日结束后更新
   - 持仓信息：季度报告后更新

4. **基金类型：**
   - 股票型、债券型、混合型、货币型、QDII等
   - 开放式、封闭式、ETF、LOF等

## 常见应用场景

### 1. ETF投资分析

```python
# 获取ETF实时行情
etf_spot = ak.fund_etf_spot_em()

# 筛选特定类型的ETF
stock_etf = etf_spot[etf_spot['名称'].str.contains('指数|ETF')]
bond_etf = etf_spot[etf_spot['名称'].str.contains('债券')]

# 获取特定ETF的历史数据
hs300_etf = ak.fund_etf_hist_em(
    symbol="510300",
    period="daily",
    start_date="20240101",
    end_date="20241231",
    adjust="qfq"
)

# 计算ETF技术指标
hs300_etf["MA5"] = hs300_etf["收盘"].rolling(window=5).mean()
hs300_etf["MA20"] = hs300_etf["收盘"].rolling(window=20).mean()
hs300_etf["RSI"] = calculate_rsi(hs300_etf["收盘"], 14)
```

### 2. 基金筛选与评级

```python
# 获取基金评级数据
fund_rating = ak.fund_rating_all()

# 筛选高评级基金
high_rated = fund_rating[
    (fund_rating['评级'] == '5星') |
    (fund_rating['评级'] == '4星')
]

# 按基金类型分类
grouped = high_rated.groupby('基金类型')

# 获取各类基金数量
fund_count_by_type = grouped.size()
```

### 3. 基金持仓分析

```python
# 获取基金持仓信息
def analyze_fund_portfolio(symbol):
    # 获取持仓数据
    portfolio = ak.fund_portfolio_hold_em(symbol=symbol)

    if len(portfolio) > 0:
        # 分析行业分布
        industry_dist = portfolio.groupby('行业')['持仓比例'].sum()

        # 分析重仓股
        top_holdings = portfolio.nlargest(10, '持仓比例')

        return {
            "symbol": symbol,
            "industry_distribution": industry_dist.to_dict(),
            "top_holdings": top_holdings[['股票名称', '持仓比例']].to_dict('records')
        }
    return None

# 分析多只基金
fund_symbols = ["000001", "110022", "161725"]
analysis_results = {}

for symbol in fund_symbols:
    result = analyze_fund_portfolio(symbol)
    if result:
        analysis_results[symbol] = result
```

### 4. 基金经理绩效分析

```python
# 获取基金经理信息
managers = ak.fund_manager()

# 分析基金经理绩效
def analyze_manager_performance(manager_name):
    manager_funds = managers[managers['基金经理'] == manager_name]

    if len(manager_funds) > 0:
        # 获取管理的基金数量
        fund_count = len(manager_funds)

        # 计算平均管理规模
        avg_scale = manager_funds['管理规模'].mean()

        # 分析从业时间分布
        experience_years = manager_funds['从业时间'].mean()

        return {
            "manager": manager_name,
            "fund_count": fund_count,
            "avg_scale": avg_scale,
            "experience_years": experience_years
        }
    return None

# 分析顶级基金经理
top_managers = managers.nlargest(10, '管理规模')['基金经理'].unique()
manager_analysis = {}

for manager in top_managers:
    result = analyze_manager_performance(manager)
    if result:
        manager_analysis[manager] = result
```

### 5. 基金规模趋势分析

```python
# 获取基金规模数据
fund_scale = ak.fund_scale_open_em()

# 分析规模变化趋势
def analyze_scale_trend(symbol):
    # 筛选特定基金
    fund_data = fund_scale[fund_scale['基金代码'] == symbol]

    if len(fund_data) > 0:
        # 计算规模变化率
        fund_data = fund_data.sort_values('报告期')
        fund_data['scale_change'] = fund_data['基金规模'].pct_change()

        # 分析规模稳定性
        scale_volatility = fund_data['scale_change'].std()

        # 获取最新规模
        latest_scale = fund_data.iloc[-1]['基金规模']

        return {
            "symbol": symbol,
            "latest_scale": latest_scale,
            "scale_volatility": scale_volatility,
            "scale_trend": fund_data[['报告期', '基金规模', 'scale_change']].to_dict('records')
        }
    return None

# 分析头部基金规模趋势
top_funds = fund_scale.groupby('基金代码')['基金规模'].last().nlargest(10).index.tolist()
scale_analysis = {}

for symbol in top_funds:
    result = analyze_scale_trend(symbol)
    if result:
        scale_analysis[symbol] = result
```

### 6. 新发基金监控

```python
# 获取新发基金信息
new_funds = ak.fund_new_found_em()

# 筛选近期新发基金
from datetime import datetime, timedelta

current_date = datetime.now()
recent_date = current_date - timedelta(days=90)  # 最近3个月

# 转换日期格式并筛选
new_funds['成立日期'] = pd.to_datetime(new_funds['成立日期'])
recent_new_funds = new_funds[new_funds['成立日期'] >= recent_date]

# 按基金类型统计
fund_type_count = recent_new_funds['基金类型'].value_counts()

# 分析新发基金趋势
print(f"最近3个月新发基金数量: {len(recent_new_funds)}")
print("按类型分布:")
print(fund_type_count)
```

## 错误处理

```python
try:
    # 获取基金数据
    df = ak.fund_etf_hist_em(
        symbol="510300",
        period="daily",
        start_date="20240101",
        end_date="20241231"
    )

    if len(df) == 0:
        print("警告: 未获取到基金数据，请检查基金代码")

except Exception as e:
    print(f"基金数据获取失败: {e}")
    # 重试或降级处理
```

## 性能优化建议

1. **批量处理：** 对多只基金数据进行批量获取
2. **数据缓存：** 对历史净值数据建立本地缓存
3. **增量更新：** 只获取新增的净值数据
4. **异步处理：** 对大量基金使用异步获取方式

## 相关资源

- [AKShare公募基金数据完整文档](https://akshare.akfamily.xyz/_sources/data/fund/fund_public.md.txt)
- [AKShare私募基金数据完整文档](https://akshare.akfamily.xyz/_sources/data/fund/fund_private.md.txt)
