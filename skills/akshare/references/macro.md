# AKShare 宏观经济数据 API 参考

## 主要功能

AKShare 提供全面的宏观经济数据获取功能，包括GDP、CPI、PMI、就业数据等国内外宏观经济指标。

## 核心API接口

### 中国宏观经济数据

#### GDP数据

```python
# 获取中国GDP数据
ak.macro_china_gdp()

# 获取中国GDP年度数据
ak.macro_china_gdp_yearly()
```

**返回字段：**
- 时间、GDP数值、同比增长率、环比增长率等

#### CPI数据

```python
# 获取中国CPI数据
ak.macro_china_cpi()

# 获取中国CPI年度数据
ak.macro_china_cpi_yearly()
```

**返回字段：**
- 时间、CPI数值、同比增长率、环比增长率等

#### PMI数据

```python
# 获取中国PMI数据
ak.macro_china_pmi()
```

**返回字段：**
- 时间、PMI数值、制造业PMI、非制造业PMI等

#### 货币供应量

```python
# 获取中国M2货币供应数据
ak.macro_china_m2()

# 获取中国M1货币供应数据
ak.macro_china_m1()

# 获取中国M0货币供应数据
ak.macro_china_m0()
```

#### 利率数据

```python
# 获取中国存款基准利率
ak.macro_china_deposit_rate()

# 获取中国贷款基准利率
ak.macro_china_loan_rate()

# 获取中国存款准备金率
ak.macro_china_rrr()
```

#### 贸易数据

```python
# 获取中国进出口贸易数据
ak.macro_china_trade()

# 获取中国贸易差额数据
ak.macro_china_trade_balance()
```

#### 投资数据

```python
# 获取中国固定资产投资数据
ak.macro_china_fixed_investment()

# 获取中国房地产开发投资数据
ak.macro_china_real_estate()
```

#### 消费数据

```python
# 获取中国社会消费品零售总额
ak.macro_china_consumption()

# 获取中国消费者信心指数
ak.macro_china_consumer_confidence()
```

#### 工业生产数据

```python
# 获取中国工业增加值
ak.macro_china_industrial_production()

# 获取中国工业企业利润
ak.macro_china_industrial_profits()
```

#### 就业数据

```python
# 获取中国就业数据
ak.macro_china_employment()

# 获取中国城镇登记失业率
ak.macro_china_unemployment_rate()
```

### 美国宏观经济数据

#### 就业数据

```python
# 获取美国非农就业数据
ak.macro_usa_non_farm()

# 获取美国失业率数据
ak.macro_usa_unemployment()

# 获取美国就业成本指数
ak.macro_usa_employment_cost()
```

#### 通胀数据

```python
# 获取美国CPI月度数据
ak.macro_usa_cpi_monthly()

# 获取美国CPI年度数据
ak.macro_usa_cpi_yearly()

# 获取美国PPI数据
ak.macro_usa_ppi()
```

#### GDP数据

```python
# 获取美国GDP月度数据
ak.macro_usa_gdp_monthly()

# 获取美国GDP年度数据
ak.macro_usa_gdp_yearly()
```

#### 利率数据

```python
# 获取美国联邦基金利率
ak.macro_usa_interest_rate()

# 获取美国国债收益率
ak.macro_usa_treasury()
```

#### 消费数据

```python
# 获取美国零售销售数据
ak.macro_usa_retail_sales()

# 获取美国消费者信心指数
ak.macro_usa_consumer_confidence()
```

#### 房地产数据

```python
# 获取美国新屋开工数据
ak.macro_usa_housing_starts()

# 获取美国成屋销售数据
ak.macro_usa_existing_home_sales()
```

#### 制造业数据

```python
# 获取美国制造业PMI
ak.macro_usa_manufacturing_pmi()

# 获取美国工业产出数据
ak.macro_usa_industrial_production()
```

### 其他主要经济体数据

#### 欧元区数据

```python
# 获取欧元区GDP数据
ak.macro_euro_gdp()

# 获取欧元区CPI数据
ak.macro_euro_cpi()

# 获取欧元区PMI数据
ak.macro_euro_pmi()
```

#### 日本数据

```python
# 获取日本GDP数据
ak.macro_japan_gdp()

# 获取日本CPI数据
ak.macro_japan_cpi()

# 获取日本PMI数据
ak.macro_japan_pmi()
```

#### 英国数据

```python
# 获取英国GDP数据
ak.macro_uk_gdp()

# 获取英国CPI数据
ak.macro_uk_cpi()

# 获取英国PMI数据
ak.macro_uk_pmi()
```

## 金融市场数据

### 汇率数据

```python
# 获取美元兑人民币汇率
ak.forex_usd_cny()

# 获取主要货币汇率
ak.forex_hist(symbol="USD/CNY")
```

### 商品价格

```python
# 获取原油价格
ak.macro_oil_price()

# 获取黄金价格
ak.metals_gold()

# 获取白银价格
ak.metals_silver()
```

### 债券收益率

```python
# 获取中国国债收益率
ak.macro_china_bond_yield()

# 获取美国国债收益率
ak.macro_usa_treasury()
```

## 使用注意事项

1. **数据频率：**
   - 月度数据：每月中旬发布上月数据
   - 季度数据：每季度结束后1个月左右发布
   - 年度数据：次年年初发布

2. **数据发布：**
   - 中国数据：国家统计局、央行等官方机构发布
   - 美国数据：BLS、BEA、美联储等机构发布
   - 数据可能有修正和更新

3. **数据格式：**
   - 时间格式：YYYY-MM-DD 或 YYYYMM
   - 数值格式：浮点数或百分比
   - 增长率：同比、环比、年化等

4. **数据延迟：**
   - 实时数据：可能有1-3天延迟
   - 历史数据：T+1更新
   - 修正数据：可能随时更新

## 常见应用场景

### 1. 宏观经济趋势分析

```python
# 获取主要宏观经济指标
def get_macro_indicators():
    indicators = {}

    try:
        # 中国主要指标
        indicators['china_gdp'] = ak.macro_china_gdp()
        indicators['china_cpi'] = ak.macro_china_cpi()
        indicators['china_pmi'] = ak.macro_china_pmi()
        indicators['china_m2'] = ak.macro_china_m2()

        # 美国主要指标
        indicators['usa_gdp'] = ak.macro_usa_gdp_monthly()
        indicators['usa_cpi'] = ak.macro_usa_cpi_monthly()
        indicators['usa_unemployment'] = ak.macro_usa_unemployment()

        return indicators
    except Exception as e:
        print(f"获取宏观数据失败: {e}")
        return None

# 分析宏观经济趋势
def analyze_macro_trends():
    indicators = get_macro_indicators()

    if indicators:
        analysis = {}

        # 分析中国GDP趋势
        if len(indicators['china_gdp']) > 0:
            gdp_data = indicators['china_gdp']
            latest_gdp = gdp_data.iloc[-1]

            analysis['china_gdp_trend'] = {
                'current_value': latest_gdp.get('value', None),
                'growth_rate': latest_gdp.get('growth_rate', None),
                'trend': '上升' if latest_gdp.get('growth_rate', 0) > 0 else '下降'
            }

        # 分析CPI通胀趋势
        if len(indicators['china_cpi']) > 0:
            cpi_data = indicators['china_cpi']
            latest_cpi = cpi_data.iloc[-1]

            analysis['china_cpi_trend'] = {
                'current_value': latest_cpi.get('value', None),
                'inflation_level': '高通胀' if latest_cpi.get('value', 0) > 3 else '温和通胀'
            }

        return analysis
    return None
```

### 2. 中美经济对比分析

```python
# 中美经济指标对比
def compare_china_usa_economy():
    comparison = {}

    try:
        # 获取中美GDP数据
        china_gdp = ak.macro_china_gdp()
        usa_gdp = ak.macro_usa_gdp_monthly()

        # 获取中美CPI数据
        china_cpi = ak.macro_china_cpi()
        usa_cpi = ak.macro_usa_cpi_monthly()

        # 获取中美就业数据
        china_employment = ak.macro_china_employment()
        usa_unemployment = ak.macro_usa_unemployment()

        # 对比分析
        if len(china_gdp) > 0 and len(usa_gdp) > 0:
            latest_china_gdp = china_gdp.iloc[-1]
            latest_usa_gdp = usa_gdp.iloc[-1]

            comparison['gdp_comparison'] = {
                'china_growth': latest_china_gdp.get('growth_rate', None),
                'usa_growth': latest_usa_gdp.get('growth_rate', None),
                'relative_performance': '中国领先' if latest_china_gdp.get('growth_rate', 0) > latest_usa_gdp.get('growth_rate', 0) else '美国领先'
            }

        if len(china_cpi) > 0 and len(usa_cpi) > 0:
            latest_china_cpi = china_cpi.iloc[-1]
            latest_usa_cpi = usa_cpi.iloc[-1]

            comparison['inflation_comparison'] = {
                'china_inflation': latest_china_cpi.get('value', None),
                'usa_inflation': latest_usa_cpi.get('value', None),
                'inflation_gap': latest_china_cpi.get('value', 0) - latest_usa_cpi.get('value', 0)
            }

        return comparison

    except Exception as e:
        print(f"中美经济对比分析失败: {e}")
        return None
```

### 3. 经济周期分析

```python
# 经济周期分析
def analyze_economic_cycle():
    cycle_analysis = {}

    try:
        # 获取关键指标
        gdp = ak.macro_china_gdp()
        pmi = ak.macro_china_pmi()
        m2 = ak.macro_china_m2()
        cpi = ak.macro_china_cpi()

        if len(gdp) > 0 and len(pmi) > 0:
            # 获取最新数据
            latest_gdp = gdp.iloc[-1]
            latest_pmi = pmi.iloc[-1]
            latest_m2 = m2.iloc[-1] if len(m2) > 0 else None
            latest_cpi = cpi.iloc[-1] if len(cpi) > 0 else None

            # 判断经济周期阶段
            gdp_growth = latest_gdp.get('growth_rate', 0)
            pmi_value = latest_pmi.get('value', 50)

            if gdp_growth > 6 and pmi_value > 50:
                cycle_stage = '扩张期'
            elif gdp_growth > 3 and pmi_value > 50:
                cycle_stage = '复苏期'
            elif gdp_growth < 3 and pmi_value < 50:
                cycle_stage = '衰退期'
            else:
                cycle_stage = '滞胀期'

            cycle_analysis = {
                'cycle_stage': cycle_stage,
                'gdp_growth': gdp_growth,
                'pmi_value': pmi_value,
                'm2_growth': latest_m2.get('growth_rate', None) if latest_m2 else None,
                'cpi_inflation': latest_cpi.get('value', None) if latest_cpi else None
            }

        return cycle_analysis

    except Exception as e:
        print(f"经济周期分析失败: {e}")
        return None
```

### 4. 通胀压力监测

```python
# 通胀压力监测
def monitor_inflation_pressure():
    inflation_monitor = {}

    try:
        # 获取通胀相关指标
        cpi = ak.macro_china_cpi()
        ppi = ak.macro_china_ppi() if hasattr(ak, 'macro_china_ppi') else None
        m2 = ak.macro_china_m2()
        commodity_prices = ak.macro_commodity_prices() if hasattr(ak, 'macro_commodity_prices') else None

        if len(cpi) > 0:
            latest_cpi = cpi.iloc[-1]

            # 分析通胀水平
            cpi_value = latest_cpi.get('value', 0)

            if cpi_value > 3:
                inflation_level = '高通胀'
                risk_level = '高风险'
            elif cpi_value > 2:
                inflation_level = '温和通胀'
                risk_level = '中等风险'
            else:
                inflation_level = '低通胀'
                risk_level = '低风险'

            inflation_monitor = {
                'current_cpi': cpi_value,
                'inflation_level': inflation_level,
                'risk_level': risk_level,
                'trend': analyze_inflation_trend(cpi)
            }

            # 分析货币供应对通胀的影响
            if len(m2) > 0:
                latest_m2 = m2.iloc[-1]
                m2_growth = latest_m2.get('growth_rate', 0)

                if m2_growth > 10 and cpi_value > 2:
                    inflation_monitor['monetary_pressure'] = '货币供应增长较快，存在通胀压力'
                else:
                    inflation_monitor['monetary_pressure'] = '货币供应相对稳定'

        return inflation_monitor

    except Exception as e:
        print(f"通胀压力监测失败: {e}")
        return None

def analyze_inflation_trend(cpi_data):
    """分析通胀趋势"""
    if len(cpi_data) >= 3:
        recent_values = cpi_data.tail(3)['value'].tolist()

        if recent_values[2] > recent_values[1] > recent_values[0]:
            return '上升趋势'
        elif recent_values[2] < recent_values[1] < recent_values[0]:
            return '下降趋势'
        else:
            return '震荡趋势'
    return '数据不足'
```

### 5. 货币政策分析

```python
# 货币政策分析
def analyze_monetary_policy():
    policy_analysis = {}

    try:
        # 获取货币政策相关指标
        deposit_rate = ak.macro_china_deposit_rate()
        loan_rate = ak.macro_china_loan_rate()
        rrr = ak.macro_china_rrr()
        m2 = ak.macro_china_m2()

        if len(deposit_rate) > 0 and len(m2) > 0:
            latest_deposit_rate = deposit_rate.iloc[-1]
            latest_loan_rate = loan_rate.iloc[-1] if len(loan_rate) > 0 else None
            latest_rrr = rrr.iloc[-1] if len(rrr) > 0 else None
            latest_m2 = m2.iloc[-1]

            # 分析货币政策立场
            current_deposit_rate = latest_deposit_rate.get('value', 0)
            current_m2_growth = latest_m2.get('growth_rate', 0)

            if current_deposit_rate < 2 and current_m2_growth > 10:
                policy_stance = '宽松货币政策'
            elif current_deposit_rate > 3 and current_m2_growth < 8:
                policy_stance = '紧缩货币政策'
            else:
                policy_stance = '中性货币政策'

            policy_analysis = {
                'policy_stance': policy_stance,
                'deposit_rate': current_deposit_rate,
                'loan_rate': latest_loan_rate.get('value', None) if latest_loan_rate else None,
                'rrr': latest_rrr.get('value', None) if latest_rrr else None,
                'm2_growth': current_m2_growth
            }

        return policy_analysis

    except Exception as e:
        print(f"货币政策分析失败: {e}")
        return None
```

## 错误处理

```python
try:
    # 获取宏观经济数据
    df = ak.macro_china_gdp()

    if len(df) == 0:
        print("警告: 未获取到GDP数据")

except Exception as e:
    print(f"宏观数据获取失败: {e}")
    # 重试或降级处理
```

## 性能优化建议

1. **批量获取：** 一次性获取多个相关指标
2. **数据缓存：** 对历史数据建立本地缓存
3. **增量更新：** 只获取最新的数据更新
4. **异步处理：** 对多个指标使用异步获取

## 相关资源

- [AKShare宏观经济数据完整文档](https://akshare.akfamily.xyz/_sources/data/macro/macro.md.txt)
