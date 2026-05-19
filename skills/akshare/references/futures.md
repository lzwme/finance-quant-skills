# AKShare 期货数据 API 参考

## 主要功能

AKShare 提供全面的期货数据获取功能，包括期货行情、历史K线、库存数据、主力合约等。

## 核心API接口

### 期货行情数据

#### 实时行情

```python
# 获取期货实时行情
ak.futures_zh_spot()
```

**返回字段：**
- symbol: 合约代码
- contract: 合约名称
- price: 最新价
- open: 开盘价
- high: 最高价
- low: 最低价
- volume: 成交量
- open_interest: 持仓量
- change: 涨跌幅

#### 期货日线数据

```python
from akshare import get_futures_daily

# 获取期货日线数据（按交易所）
df = get_futures_daily(
    start_date="20240101",
    end_date="20240131",
    market="CFFEX"  # 交易所代码
)
```

**交易所选项：**
- `"CFFEX"` - 中国金融期货交易所（中金所）
- `"SHFE"` - 上海期货交易所（上期所）
- `"DCE"` - 大连商品交易所（大商所）
- `"CZCE"` - 郑州商品交易所（郑商所）
- `"INE"` - 上海国际能源交易中心
- `"GFEX"` - 广州期货交易所

### 库存数据

```python
# 获取期货库存数据
ak.futures_inventory_99(symbol="豆一")
```

**常用品种：**
- "豆一", "豆二", "豆粕", "豆油", "棕榈油"
- "玉米", "玉米淀粉", "鸡蛋", "纤维板"
- "铁矿石", "焦炭", "焦煤", "聚乙烯"

### 主力合约数据

```python
# 获取期货主力合约
ak.futures_main_sure_em(symbol="IF")  # 股指期货
```

## 各交易所数据接口

### 中国金融期货交易所（CFFEX）

```python
# 中金所期货数据
df = get_futures_daily(
    start_date="20240101",
    end_date="20240131",
    market="CFFEX"
)

# 主要品种：IF(沪深300), IC(中证500), IH(上证50), T(国债)等
```

### 上海期货交易所（SHFE）

```python
# 上期所期货数据
df = get_futures_daily(
    start_date="20240101",
    end_date="20240131",
    market="SHFE"
)

# 主要品种：CU(铜), AL(铝), ZN(锌), PB(铅), NI(镍), SN(锡)
# AU(黄金), AG(白银), RB(螺纹钢), WR(线材), HC(热轧卷板)
```

### 大连商品交易所（DCE）

```python
# 大商所期货数据
df = get_futures_daily(
    start_date="20240101",
    end_date="20240131",
    market="DCE"
)

# 主要品种：C(玉米), CS(淀粉), A(豆一), B(豆二), M(豆粕)
# Y(豆油), P(棕榈油), L(聚乙烯), V(聚氯乙烯), PP(聚丙烯)
```

### 郑州商品交易所（CZCE）

```python
# 郑商所期货数据
df = get_futures_daily(
    start_date="20240101",
    end_date="20240131",
    market="CZCE"
)

# 主要品种：SR(白糖), CF(棉花), TA(PTA), OI(菜籽油), WH(强麦)
# RI(早籼稻), RS(油菜籽), RM(菜籽粕), JR(粳稻), LR(晚籼稻)
```

## 特色数据

### 期货价格指数

```python
# 获取期货价格指数
ak.futures_index_price_sina(symbol="IF")  # 股指期货指数
```

### 期货连续合约

```python
# 获取期货连续合约
ak.futures_zh_daily_sina(symbol="IF0")  # 股指期货连续
```

### 期货主力连续

```python
# 获取期货主力连续合约
ak.futures_main_contract_sina(symbol="IF")
```

## 期货套利数据

```python
# 获取期货套利数据
ak.futures_arbitrage_sina(symbol="CU")
```

## 期货期权数据

```python
# 获取期货期权数据
ak.futures_option_dce(symbol="豆粕期权")  # 大商所期权
ak.futures_option_czce(symbol="白糖期权")  # 郑商所期权
ak.futures_option_shfe(symbol="铜期权")   # 上期所期权
```

## 使用注意事项

1. **数据格式：**
   - 日期格式：YYYYMMDD
   - 价格单位：根据不同品种而定
   - 成交量单位：手
   - 持仓量单位：手

2. **交易时间：**
   - 日盘：09:00-15:00
   - 夜盘：21:00-02:30（部分品种）
   - 注意节假日休市安排

3. **合约代码规则：**
   - 品种代码 + 年份 + 月份（如：IF2406）
   - 连续合约：品种代码 + 0（如：IF0）

4. **数据延迟：**
   - 实时行情：可能有1-3秒延迟
   - 历史数据：T+1更新
   - 库存数据：每周更新

## 常见应用场景

### 1. 获取特定交易所数据

```python
# 获取中金所期货数据
df_cffex = get_futures_daily(
    start_date="20240101",
    end_date="20240131",
    market="CFFEX"
)

# 获取上期所期货数据
df_shfe = get_futures_daily(
    start_date="20240101",
    end_date="20240131",
    market="SHFE"
)
```

### 2. 分析期货主力合约

```python
# 获取股指期货主力合约
main_contracts = ak.futures_main_sure_em(symbol="IF")

# 分析主力合约走势
df_main = get_futures_daily(
    start_date="20240101",
    end_date="20240131",
    market="CFFEX"
)

# 筛选主力合约数据
df_main = df_main[df_main['symbol'].isin(main_contracts['symbol'])]
```

### 3. 期货库存分析

```python
# 获取多个品种库存数据
commodities = ["豆一", "豆粕", "玉米", "铁矿石"]
inventory_data = {}

for commodity in commodities:
    try:
        df = ak.futures_inventory_99(symbol=commodity)
        inventory_data[commodity] = df
        print(f"已获取 {commodity} 库存数据")
    except Exception as e:
        print(f"获取 {commodity} 数据失败: {e}")

# 分析库存变化趋势
for commodity, df in inventory_data.items():
    if len(df) > 0:
        latest = df.iloc[-1]
        previous = df.iloc[-2] if len(df) > 1 else None

        if previous is not None:
            change = latest['库存'] - previous['库存']
            print(f"{commodity} 库存变化: {change}")
```

### 4. 期货技术分析

```python
# 获取期货数据用于技术分析
df = get_futures_daily(
    start_date="20240101",
    end_date="20241231",
    market="CFFEX"
)

# 筛选特定合约
df_if = df[df['symbol'] == 'IF2406'].copy()

# 计算技术指标
df_if["MA5"] = df_if["close"].rolling(window=5).mean()
df_if["MA10"] = df_if["close"].rolling(window=10).mean()
df_if["MA20"] = df_if["close"].rolling(window=20).mean()

# 计算波动率
df_if["returns"] = df_if["close"].pct_change()
df_if["volatility"] = df_if["returns"].rolling(window=20).std() * (252 ** 0.5)

# 分析持仓量变化
df_if["oi_change"] = df_if["open_interest"].diff()
```

### 5. 跨期套利分析

```python
# 获取同一品种不同月份合约
contracts = ["IF2406", "IF2409", "IF2412"]
contract_data = {}

for contract in contracts:
    df = get_futures_daily(
        start_date="20240101",
        end_date="20240131",
        market="CFFEX"
    )
    contract_df = df[df['symbol'] == contract]
    if len(contract_df) > 0:
        contract_data[contract] = contract_df

# 计算价差
if len(contract_data) >= 2:
    near_contract = contract_data[contracts[0]]
    far_contract = contract_data[contracts[1]]

    # 计算价差
    spread = far_contract["close"].values - near_contract["close"].values

    # 分析价差统计特征
    spread_mean = spread.mean()
    spread_std = spread.std()

    print(f"价差均值: {spread_mean:.2f}")
    print(f"价差标准差: {spread_std:.2f}")
```

## 错误处理

```python
try:
    df = get_futures_daily(
        start_date="20240101",
        end_date="20240131",
        market="CFFEX"
    )
    if len(df) == 0:
        print("警告: 未获取到数据，请检查参数")
except Exception as e:
    print(f"数据获取失败: {e}")
    # 重试或降级处理
```

## 性能优化建议

1. **批量获取：** 尽量一次性获取较长时间段的数据
2. **数据筛选：** 在获取后立即筛选需要的合约
3. **缓存机制：** 对历史数据建立本地缓存
4. **异步处理：** 对多个品种使用异步获取

## 相关资源

- [AKShare期货完整文档](https://akshare.akfamily.xyz/_sources/data/futures/futures.md.txt)
