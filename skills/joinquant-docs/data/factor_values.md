## 使用方法

**说明：**

- 在单因子分析中可以直接获取因子库中的数据
- 同时也可以通过API的形式，在其他模块中获取这些因子
- 为保证数据的连续性，所有数据基于`后复权`计算
- 涉及到财务数据的因子，使用对应日期所能获取到的最新一期单季度数据进行计算
- 为了防止单次返回数据时间过长，每次调用 api 请求的因子值不能超过 200000 个
- 频率为天，每天05：00更新前一天数据
- 提供股票的因子数据，不支持期货、指数等
- 因子库中nan值：缺少依赖数据;财务数据中如果标的未披露相关字段,依赖数据不完整的话会返回nan值,请注意到财务报表披露规则变更,标的报表披露形式(金融类,非金融类等) , 以及标的上市时间等
- 有关因子处理：除了因子描述及说明中有解释处理方法的因子，其他的都是原始因子，没有经过处理

### 获取因子值

获取因子值:

```python
# 导入函数库
from jqfactor import get_factor_values
# 取值函数
get_factor_values(securities, factors, start_date, end_date, count)
```

**参数**

- securities:股票池，单只股票（字符串）或一个股票列表
- factors: 因子名称，单个因子（字符串）或一个因子列表
- start_date:开始日期，字符串或 datetime 对象，与 coun t参数二选一
- end_date: 结束日期， 字符串或 datetime 对象，可以与 start_date 或 count 配合使用
- count: 截止 end_date 之前交易日的数量（含 end_date 当日），与 start_date 参数二选一

**返回**

- 一个 dict： key 是因子名称， value 是 pandas.dataframe。
- dataframe 的 index 是日期， column 是股票代码， value 是因子值

**示例**

```python
# 导入函数库
from jqfactor import get_factor_values

# 获取因子Skewness60(个股收益的60日偏度)从 2017-01-01 至 2017-03-04 的因子值
factor_data = get_factor_values(securities=['000001.XSHE'], factors=['Skewness60','DEGM','quick_ratio'], start_date='2017-01-01', end_date='2017-03-04')
# 查看因子值
factor_data['Skewness60']
```

### 获取所有因子

```python
get_all_factors()
```

描述：获取聚宽因子库中所有的因子code和因子名称

**参数**：无

**返回**：pandas.DataFrame，

- factor:因子code
- factor_intro:因子说明
- category:因子分类名称
- category_intro:因子分类说明 **示例**：

```python
#获取聚宽因子库所有因子
from jqfactor import get_all_factors
print(get_all_factors())

#输出
                                     factor     factor_intro   category  category_intro
0                                      beta             BETA      style  风险因子 - 风格因子
1                       book_to_price_ratio            市净率因子      style  风险因子 - 风格因子
2                            earnings_yield           盈利预期因子      style  风险因子 - 风格因子
3                                    growth             成长因子      style  风险因子 - 风格因子
4                                  leverage             杠杆因子      style  风险因子 - 风格因子
5                                 liquidity            流动性因子      style  风险因子 - 风格因子
6                                  momentum             动量因子      style  风险因子 - 风格因子
7                           non_linear_size          非线性市值因子      style  风险因子 - 风格因子
8                       residual_volatility           残差波动因子      style  风险因子 - 风格因子
9                                      size             市值因子      style  风险因子 - 风格因子
10               administration_expense_ttm          管理费用TTM     basics      基础科目及衍生类因子
11                asset_impairment_loss_ttm        资产减值损失TTM     basics      基础科目及衍生类因子
12                                     EBIT            息税前利润     basics      基础科目及衍生类因子
...
...
```

## 风险模型因子列表

### 风格因子

#### 风格因子简介

| 因子 code | 因子名称 | 简介 |
| --- | --- | --- |
| size | 市值 | 捕捉大盘股和小盘股之间的收益差异 |
| beta | 贝塔 | 表征股票相对于市场的波动敏感度 |
| momentum | 传统动量 | 描述了过去两年里相对强势的股票与弱势股票之间的差异 |
| residual_volatility | 残差波动率 | 解释了剥离了市场风险后的波动率高低产生的收益率差异 |
| non_linear_size | 非线性市值 | 描述了无法由规模因子解释的但与规模有关的收益差异，通常代表中盘股 |
| book_to_price_ratio | 账面市值比 | 描述了股票估值高低不同而产生的收益差异, 即价值因子 |
| liquidity | 流动性 | 解释了由股票相对的交易活跃度不同而产生的收益率差异 |
| earnings_yield | 盈利能力 | 描述了由盈利收益导致的收益差异 |
| growth | 成长 | 描述了对销售或盈利增长预期不同而产生的收益差异 |
| leverage | 杠杆 | 描述了高杠杆股票与低杠杆股票之间的收益差异 |

除了上面的风格因子，在计算风格因子过程中的描述因子daily_standard_deviation、cumulative_range等也可以通过get_factor_values、get_all_factors以及get_factor_kanban_values获取；描述因子是原始值，没有进行数据处理。

  

#### 风格因子数据处理说明

对描述因子和风格因子的数据分别进行正规化的处理，步骤如下：

- 对描述因子分别进行去极值和标准化
    去极值为将2.5倍标准差之外的值，赋值成2.5倍标准差的边界值
    标准化为市值加权标准化
    x=(x- mean(x))/(std(x))
    其中，均值的计算使用股票的市值加权，标准差为正常标准差。
- 对描述因子按照权重加权求和
    按照公式给出的权重对描述因子加权求和。如果某个因子的值为nan，则对不为nan的因子加权求和，同时权重重新归一化；如果所有因子都为nan，则结果为nan。
- 对风格因子市值加权标准化
- 缺失值填充
    按照聚宽一级行业分行业，以不缺失的股票因子值相对于市值的对数进行回归，对缺失值进行填充
- 对风格因子去极值，去极值方法同上面去极值描述

#### 风格因子计算说明

- 市值因子 size
    
    -   定义：1•natural_log_of_market_cap
    -   解释
        -   对数市值 natural_log_of_market_cap：公司的总市值的自然对数。
- 贝塔因子 beta
    
    -   定义：1•raw_beta
    -   解释
        -   raw_beta：CAPM 模型中的β，过去252个交易日股票的收益与市场收益（全A股票收益按流通市值加权）进行时间序列指数加权回归后的斜率系数。指数加权的半衰期为63个交易日。 停牌股票收益率为0，股票上市需超过21个交易日，否则beta为nan。
- 动量因子 momentum
    
    -   定义：1•relative_strength
    -   解释
        -   相对强弱 relative_strength：滞后21个交易日的过去504个交易日股票超额对数收益率的指数加权之和。其中指数权重半衰期为126个交易日。停牌股票收益率为0，上市之前收益率为nan。
- 残差波动率因子 residual_volatility
    
    -   定义：0.74•daily_standard_deviation + 0.16•cumulative_range + 0.10•historical_sigma
    -   解释
        -   日收益率标准差 daily_standard_deviation：日标准差，过去252日的超额收益的指数加权标准差，以42个交易日为半衰期。
        -   收益离差 cumulative_range：过去12个月中月收益率（以21个交易日为一个月）的最大值和最小值之间的差异。股票需上市需超过6个月，否则结果为nan。
        -   残差历史波动率 historical_sigma：计算beta时的回归残差项的过去252个交易日的标准差。股票上市需超过21个交易日，否则结果为nan。
        -   用 daily_standard_deviation、cumulative_range、historical_sigma 加权求和得到的 residual_volatility，之后 关于 beta 和 size 因子做正交化以消除共线性。
- 非线性市值因子 non_linear_size
    
    -   定义：1•cube_of_size
    -   解释
        -   市值立方因子 cube_of_size：首先对标准化后的市值因子size暴露值求立方，将得到的结果与市值进行加权回归的正交化处理。
- 账面市值比因子 book_to_price_ratio
    
    -   定义：book_to_price_ratio
    -   解释
        -   最新一季财报的账面价值与当前市值的比值（pb_ratio的倒数）。其中小于0的值设置为nan。
- 流动性因子 liquidity
    
    -   定义：0.35•share_turnover_monthly + 0.35•average_share_turnover_quarterly + 0.3•average_share_turnover_annual
    -   解释
        -   月换手率 share_turnover_monthly：股票一个月换手率，过去21日的股票换手率之和的对数。
        -   季度平均平均月换手率 average_share_turnover_quarterly：过去3个月平均换手率，计算过去3个月的平均换手率，并取对数。
        -   年度平均月换手率 average_share_turnover_annual：过去12个月平均换手率，计算过去12个月的平均换手率，并取对数。
        -   用 share_turnover_monthly、average_share_turnover_quarterly、average_share_turnover_annual 加权求和得到的 liquidity 关于对数市值做正交化以消除共线性。
- 盈利能力因子 earnings_yield
    
    -   定义：0.68•predicted_earnings_to_price_ratio + 0.21•cash_earnings_to_price_ratio + 0.11•earnings_to_price_ratio
    -   解释
        -   预期利润市值比 predicted_earnings_to_price_ratio：用未来12个月的净利预测值除以当前市值。
        -   现金流量市值比 cash_earnings_to_price_ratio：过去12个月的净经营现金流除以当前股票市值。
        -   利润市值比 earnings_to_price_ratio：过去12个月的归母净利润除以当前股票市值。
- 成长因子 growth
    
    -   定义：0.18•long_term_predicted_earnings_growth + 0.11•short_term_predicted_earnings_growth + 0.24•earnings_growth + 0.47•sales_growth
    -   解释
        -   预期长期盈利增长率 long_term_predicted_earnings_growth：未来三年净利润分析师一致预期相对于净利润(不含少数股东损益)最新年报值的平均增长率。一个分析师预测的股票值为nan。
        -   预期短期盈利增长率 short_term_predicted_earnings_growth：未来一年净利润分析师一致预期相对于净利润(不含少数股东损益)最新年报值的平均增长率，只有一个分析师预测的股票值为nan。
        -   5年盈利增长率 earnings_growth：盈利增长率，过去5年的基本每股收益（basic_eps）关于[0,1,2,3,4]回归的斜率系数，然后再除以过去 5 年基本每股收益绝对值的均值。
        -   5年营业收入增长率 sales_growth：营收增长率，过去 5 年每股营业收入关于[0,1,2,3,4]回归的斜率系数，然后再除以过去 5 年每股营业收入绝对值的均值。对于保险行业的股票，使用“已赚保费”代替“销售收入”计算每股营业收入，对于银行业的股票，sales_growth为nan。
        -   earnings_growth和sales_growth至少需要有4年的财务数据，否则为nan。
- 杠杆因子 leverage
    
    -   定义：0.38•market_leverage + 0.35•debt_to_assets + 0.27•book_leverage
    -   解释
        -   市场杠杆 market_leverage：(当前的普通股市值+优先股账面价值+长期债务账面价值)/当前的普通股市值。
        -   资产负债比 debt_to_assets：总负债的账面价值/总资产的账面价值。
        -   账面杠杆 book_leverage：(普通股账面价値+优先股账面价值+长期债务账面价值)/普通股账面价值。账面杠杆需在0到100之间，否则结果为nan。

  

### 行业因子

可以获取以下行业的分类因子，股票属于这个行业则为赋值为1，否则赋值为0
1.[证监会行业](https://www.joinquant.com/help/api/help#plateData:%E8%AF%81%E7%9B%91%E4%BC%9A%E8%A1%8C%E4%B8%9A)
2.[聚宽行业(一二级)](https://www.joinquant.com/help/api/help#plateData:%E8%81%9A%E5%AE%BD%E8%A1%8C%E4%B8%9A)
3.[申万行业(一二三级)](https://www.joinquant.com/help/api/help#plateData:%E7%94%B3%E4%B8%87%E8%A1%8C%E4%B8%9A)

```python
>>> df_dic = get_factor_values('000001.XSHE',['A01','HY007','801780','801723'] ,end_date='2023-02-23',count=1)
print(df_dic)
>>>  {'A01':             000001.XSHE
    2023-02-23            0,
'HY007':             000001.XSHE
    2023-02-23            1,
'801780':             000001.XSHE
    2023-02-23            1,
'801723':             000001.XSHE
    2023-02-23            0}
```

### 风格因子pro(仅本地数据jqdatasdk可用)

#### 风格因子PRO简介

风格因子pro在原有的风格因子基础上，对底层的因子进一步细分和扩充。目前仅jqdatasdk提供，如有需求可[咨询运营开通](https://www.joinquant.com/help/api/doc?name=logon&id=9831)

| 因子 code | 因子名称 | 简介 |
| --- | --- | --- |
| btop | 市净率因子 | 描述了股票估值高低不同而产生的收益差异, 即价值因子 |
| divyild | 分红因子 | 股票历史和预测的股息价格比的股票回报差异 |
| earnqlty | 盈利质量因子 | 股票收益因其收益的应计部分而产生的差异 |
| earnvar | 盈利变动率因子 | 解释由于收益、销售额和现金流的可变性而导致的股票回报差异，以及分析师预测的收益与价格之比。 |
| earnyild | 收益因子 | 描述了由盈利收益导致的收益差异 |
| financial_leverage | 财务杠杆因子 | 描述了高杠杆股票与低杠杆股票之间的收益差异 |
| invsqlty | 投资能力因子 | 衡量当股票价格过高/过低时，公司对资产扩张/紧缩的的倾向以及管理观点 |
| liquidty | 流动性因子 | 解释了由股票相对的交易活跃度不同而产生的收益率差异 |
| long_growth | 长期成长因子 | 描述了对销售或盈利增长预期不同而产生的收益差异 |
| ltrevrsl | 长期反转因子 | 解释与长期股票价格行为相关的常见回报变化 |
| market_beta | 市场波动率因子 | 表征股票相对于市场的波动敏感度 |
| market_size | 市值规模因子 | 捕捉大盘股和小盘股之间的收益差异 |
| midcap | 中等市值因子 | 捕捉中等市值股票与大盘股或者小盘股之间的收益差异 |
| profit | 盈利能力因子 | 表征公司运营的效率，盈利能力指标的组合 |
| relative_momentum | 相对动量因子 | 解释与最近（12个月，滞后1个月）股价行为相关的股票回报的常见变化 |
| resvol | 残余波动率因子 | 捕捉股票回报的相对波动性，这种波动性不能用股票对市场回报的敏感性差异来解释（市场波动率因子） |

## 基本面及量价因子列表

### 财务基本面因子

#### 质量因子

| 因子 code | 因子名称 | 计算方法 |
| --- | --- | --- |
| net_profit_to_total_operate_revenue_ttm | 净利润与营业总收入之比 | 净利润与营业总收入之比=净利润（TTM）/营业总收入（TTM） |
| cfo_to_ev | 经营活动产生的现金流量净额与企业价值之比TTM | 经营活动产生的现金流量净额TTM / 企业价值。其中，企业价值=司市值+负债合计-货币资金 |
| accounts_payable_turnover_days | 应付账款周转天数 | 应付账款周转天数 = 360 / 应付账款周转率 |
| net_profit_ratio | 销售净利率 | 售净利率=净利润（TTM）/营业收入（TTM） |
| net_non_operating_income_to_total_profit | 营业外收支利润净额/利润总额 | 营业外收支利润净额/利润总额 |
| fixed_asset_ratio | 固定资产比率 | 固定资产比率=(固定资产+工程物资+在建工程)/总资产 |
| account_receivable_turnover_days | 应收账款周转天数 | 应收账款周转天数=360/应收账款周转率 |
| DEGM | 毛利率增长 | 毛利率增长=(今年毛利率（TTM）/去年毛利率（TTM）)-1 |
| sale_expense_to_operating_revenue | 营业费用与营业总收入之比 | 营业费用与营业总收入之比=销售费用（TTM）/营业总收入（TTM） |
| operating_tax_to_operating_revenue_ratio_ttm | 销售税金率 | 销售税金率=营业税金及附加（TTM）/营业收入（TTM） |
| inventory_turnover_days | 存货周转天数 | 存货周转天数=360/存货周转率 |
| OperatingCycle | 营业周期 | 应收账款周转天数+存货周转天数 |
| net_operate_cash_flow_to_operate_income | 经营活动产生的现金流量净额与经营活动净收益之比 | 经营活动产生的现金流量净额（TTM）/(营业总收入（TTM）-营业总成本（TTM）） |
| net_operating_cash_flow_coverage | 净利润现金含量 | 经营活动产生的现金流量净额/归属于母公司所有者的净利润 |
| quick_ratio | 速动比率 | 速动比率=(流动资产合计-存货)/ 流动负债合计 |
| intangible_asset_ratio | 无形资产比率 | 无形资产比率=(无形资产+研发支出+商誉)/总资产 |
| MLEV | 市场杠杆 | 市场杠杆=非流动负债合计/(非流动负债合计+总市值) |
| debt_to_equity_ratio | 产权比率 | 产权比率=负债合计/归属母公司所有者权益合计 |
| super_quick_ratio | 超速动比率 | （货币资金+交易性金融资产+应收票据+应收帐款+其他应收款）／流动负债合计 |
| inventory_turnover_rate | 存货周转率 | 存货周转率=营业成本（TTM）/AvgQ(存货,4,0) |
| operating_profit_growth_rate | 营业利润增长率 | 营业利润增长率=(今年营业利润（TTM）/去年营业利润（TTM）)-1 |
| long_debt_to_working_capital_ratio | 长期负债与营运资金比率 | 长期负债与营运资金比率=非流动负债合计/(流动资产合计-流动负债合计) |
| current_ratio | 流动比率(单季度) | 流动比率=流动资产合计/流动负债合计 |
| net_operate_cash_flow_to_net_debt | 经营活动产生现金流量净额/净债务 | 经营活动产生现金流量净额/净债务 |
| net_operate_cash_flow_to_asset | 总资产现金回收率 | 经营活动产生的现金流量净额(ttm) / 总资产 |
| non_current_asset_ratio | 非流动资产比率 | 非流动资产比率=非流动资产合计/总资产 |
| total_asset_turnover_rate | 总资产周转率 | 总资产周转率=营业收入(ttm)/总资产 |
| long_debt_to_asset_ratio | 长期借款与资产总计之比 | 长期借款与资产总计之比=长期借款/总资产 |
| debt_to_tangible_equity_ratio | 有形净值债务率 | 负债合计/有形净值 其中有形净值=股东权益-无形资产净值，无形资产净值= 商誉+无形资产 |
| ROAEBITTTM | 总资产报酬率 | （利润总额（TTM）+利息支出（TTM）） / 总资产在过去12个月的平均 |
| operating_profit_ratio | 营业利润率 | 营业利润率=营业利润（TTM）/营业收入（TTM） |
| long_term_debt_to_asset_ratio | 长期负债与资产总计之比 | 长期负债与资产总计之比=非流动负债合计/总资产 |
| current_asset_turnover_rate | 流动资产周转率TTM | 过去12个月的营业收入/过去12个月的平均流动资产合计 |
| financial_expense_rate | 财务费用与营业总收入之比 | 财务费用（TTM） / 营业总收入（TTM） |
| operating_profit_to_total_profit | 经营活动净收益/利润总额 | 经营活动净收益/利润总额 |
| debt_to_asset_ratio | 债务总资产比 | 债务总资产比=负债合计/总资产 |
| equity_to_fixed_asset_ratio | 股东权益与固定资产比率 | 股东权益与固定资产比率=股东权益/(固定资产+工程物资+在建工程) |
| net_operate_cash_flow_to_total_liability | 经营活动产生的现金流量净额/负债合计 | 经营活动产生的现金流量净额/负债合计 |
| cash_rate_of_sales | 经营活动产生的现金流量净额与营业收入之比 | 经营活动产生的现金流量净额（TTM） / 营业收入（TTM） |
| operating_profit_to_operating_revenue | 营业利润与营业总收入之比 | 营业利润与营业总收入之比=营业利润（TTM）/营业总收入（TTM） |
| roa_ttm | 资产回报率TTM | 资产回报率=净利润（TTM）/期末总资产 |
| admin_expense_rate | 管理费用与营业总收入之比 | 管理费用与营业总收入之比=管理费用（TTM）/营业总收入（TTM） |
| fixed_assets_turnover_rate | 固定资产周转率 | 等于过去12个月的营业收入/过去12个月的平均（固定资产+工程物资+在建工程） |
| invest_income_associates_to_total_profit | 对联营和合营公司投资收益/利润总额 | 对联营和营公司投资收益/利润总额 |
| equity_to_asset_ratio | 股东权益比率 | 股东权益比率=股东权益/总资产 |
| goods_service_cash_to_operating_revenue_ttm | 销售商品提供劳务收到的现金与营业收入之比 | 销售商品提供劳务收到的现金与营业收入之比=销售商品和提供劳务收到的现金（TTM）/营业收入（TTM） |
| cash_to_current_liability | 现金比率 | 期末现金及现金等价物余额/流动负债合计的12个月均值 |
| net_operate_cash_flow_to_total_current_liability | 现金流动负债比 | 现金流动负债比=经营活动产生的现金流量净额（TTM）/流动负债合计 |
| ACCA | 现金流资产比和资产回报率之差 | 现金流资产比-资产回报率,其中现金流资产比=经营活动产生的现金流量净额/总资产 |
| roe_ttm | 权益回报率TTM | 权益回报率=净利润（TTM）/期末股东权益 |
| accounts_payable_turnover_rate | 应付账款周转率 | TTM(营业成本,0)/（AvgQ(应付账款,4,0) + AvgQ(应付票据,4,0) ） |
| gross_income_ratio | 销售毛利率 | 销售毛利率=(营业收入（TTM）-营业成本（TTM）)/营业收入（TTM） |
| adjusted_profit_to_total_profit | 扣除非经常损益后的净利润/利润总额 | 扣除非经常损益后的净利润/利润总额 |
| account_receivable_turnover_rate | 应收账款周转率 | 即，TTM(营业收入,0)/（AvgQ(应收账款,4,0)+ AvgQ(应收票据,4,0)） |
| equity_turnover_rate | 股东权益周转率 | 股东权益周转率=营业收入(ttm)/股东权益 |
| total_profit_to_cost_ratio | 成本费用利润率 | 成本费用利润率=利润总额/(营业成本+财务费用+销售费用+管理费用)，以上科目使用的都是TTM的数值 |
| operating_cost_to_operating_revenue_ratio | 销售成本率 | 销售成本率=营业成本（TTM）/营业收入（TTM） |
| LVGI | 财务杠杆指数 | 本期(年报)资产负债率/上期(年报)资产负债率 |
| SGI | 营业收入指数 | 本期(年报)营业收入/上期(年报)营业收入 |
| GMI | 毛利率指数 | 上期(年报)毛利率/本期(年报)毛利率 |
| DSRI | 应收账款指数 | 本期(年报)应收账款占营业收入比例/上期(年报)应收账款占营业收入比例 |
| rnoa_ttm | 经营资产回报率TTM | 销售利润率*经营资产周转率 |
| profit_margin_ttm | 销售利润率TTM | 营业利润/营业收入 |
| roe_ttm_8y | 长期权益回报率TTM | 8年(1+roe_ttm)的累乘 ^ (1/8) - 1 # 至少要有近4年的数据，否则为 nan |
| asset_turnover_ttm | 经营资产周转率TTM | 营业收入TTM/近4个季度期末净经营性资产均值; 净经营性资产=经营资产-经营负债 |
| roic_ttm | 投资资本回报率TTM | 权益回报率=归属于母公司股东的净利润（TTM）/ 前四个季度投资资本均值; 投资资本=股东权益+负债合计-无息流动负债-无息非流动负债; 无息流动负债=应付账款+预收款项+应付职工薪酬+应交税费+其他应付款+一年内的递延收益+其它流动负债; 无息非流动负债=非流动负债合计-长期借款-应付债券； |
| roa_ttm_8y | 长期资产回报率TTM | 8年(1+roa_ttm)的乘积 ^ (1/8) - 1 # 至少要有近4年的数据，否则为 nan |
| SGAI | 销售管理费用指数 | 本期(年报)销售管理费用占营业收入的比例/上期(年报)销售管理费用占营业收入的比例 |
| DEGM_8y | 长期毛利率增长 | 过去8年(1+DEGM)的累成 ^ (1/8) - 1 |
| maximum_margin | 最大盈利水平 | max(margin_stability, DEGM_8y) |
| margin_stability | 盈利能力稳定性 | mean(GM)/std(GM); GM 为过去8年毛利率ttm |

#### 基础因子

| 因子 code | 因子名称 | 计算方法 |
| --- | --- | --- |
| net_working_capital | 净运营资本 | 流动资产 － 流动负债 |
| total_operating_revenue_ttm | 营业总收入TTM | 计算过去12个月的 营业总收入 之和 |
| operating_profit_ttm | 营业利润TTM | 计算过去12个月 营业利润 之和 |
| net_operate_cash_flow_ttm | 经营活动现金流量净额TTM | 计算过去12个月 经营活动产生的现金流量净值 之和 |
| operating_revenue_ttm | 营业收入TTM | 计算过去12个月的 营业收入 之和 |
| interest_carry_current_liability | 带息流动负债 | 流动负债合计 - 无息流动负债 |
| sale_expense_ttm | 销售费用TTM | 计算过去12个月 销售费用 之和 |
| gross_profit_ttm | 毛利TTM | 过去12个月的 毛利润 之和 |
| retained_earnings | 留存收益 | 盈余公积金+未分配利润 |
| total_operating_cost_ttm | 营业总成本TTM | 计算过去12个月的 营业总成本 之和 |
| non_operating_net_profit_ttm | 营业外收支净额TTM | 营业外收入（TTM） - 营业外支出（TTM） |
| net_invest_cash_flow_ttm | 投资活动现金流量净额TTM | 计算过去12个月 投资活动现金流量净额 之和 |
| financial_expense_ttm | 财务费用TTM | 计算过去12个月 财务费用 之和 |
| administration_expense_ttm | 管理费用TTM | 计算过去12个月 管理费用 之和 |
| net_interest_expense | 净利息费用 | 利息支出-利息收入 |
| value_change_profit_ttm | 价值变动净收益TTM | 计算过去12个月 价值变动净收益 之和 |
| total_profit_ttm | 利润总额TTM | 计算过去12个月 利润总额 之和 |
| net_finance_cash_flow_ttm | 筹资活动现金流量净额TTM | 计算过去12个月 筹资活动现金流量净额 之和 |
| interest_free_current_liability | 无息流动负债 | 应付票据+应付账款+预收账款(用 预售款项 代替)+应交税费+应付利息+其他应付款+其他流动负债 |
| EBIT | 息税前利润 | 净利润+所得税+财务费用 |
| net_profit_ttm | 净利润TTM | 计算过去12个月 净利润 之和 |
| OperateNetIncome | 经营活动净收益 | 经营活动净收益/利润总额(%) * 利润总额 |
| EBITDA | 息税折旧摊销前利润（报告期） | 一般企业：（营业总收入-营业税金及附加）-（营业成本+利息支出+手续费及佣金支出+销售费用+管理费用+研发费用+资产减值损失）+（固定资产折旧、油气资产折耗、生产性生物资产折旧）+无形资产摊销+长期待摊费用摊销;
银行业：（营业总收入-营业税金及附加）-（营业成本+管理费用+资产减值损失）+（固定资产折旧、油气资产折耗、生产性生物资产折旧+无形资产摊销+长期待摊费用摊销） |
| asset_impairment_loss_ttm | 资产减值损失TTM | 计算过去12个月 资产减值损失 之和 |
| np_parent_company_owners_ttm | 归属于母公司股东的净利润TTM | 计算过去12个月 归属于母公司股东的净利润 之和 |
| operating_cost_ttm | 营业成本TTM | 计算过去12个月的 营业成本 之和 |
| net_debt | 净债务 | 总债务-期末现金及现金等价物余额 |
| non_recurring_gain_loss | 非经常性损益 | 归属于母公司股东的净利润-扣除非经常损益后的净利润(元) |
| goods_sale_and_service_render_cash_ttm | 销售商品提供劳务收到的现金 | 计算过去12个月 销售商品提供劳务收到的现金 之和 |
| market_cap | 市值 | 市值 |
| cash_flow_to_price_ratio | 现金流市值比 | 1 / pcf_ratio (ttm) |
| sales_to_price_ratio | 营收市值比 | 1 / ps_ratio (ttm) |
| circulating_market_cap | 流通市值 | 流通市值 |
| operating_assets | 经营性资产 | 总资产 - 金融资产 |
| financial_assets | 金融资产 | 货币资金 + 交易性金融资产 + 应收票据 + 应收利息 + 应收股利 + 可供出售金融资产 + 持有至到期投资 |
| operating_liability | 经营性负债 | 总负债 - 金融负债 |
| financial_liability | 金融负债 | (流动负债合计-无息流动负债)+(有息非流动负债)=(流动负债合计-应付账款-预收款项-应付职工薪酬-应交税费-其他应付款-一年内的递延收益-其它流动负债)+(长期借款+应付债券) |

#### 成长因子

| 因子 code | 因子名称 | 计算方法 |
| --- | --- | --- |
| operating_revenue_growth_rate | 营业收入增长率 | 营业收入增长率=（今年营业收入（TTM）/去年营业收入（TTM））-1 |
| total_asset_growth_rate | 总资产增长率 | 总资产 / 总资产_4 -1 |
| net_operate_cashflow_growth_rate | 经营活动产生的现金流量净额增长率 | (今年经营活动产生的现金流量净额（TTM）/去年经营活动产生的现金流量净额（TTM）)-1 |
| total_profit_growth_rate | 利润总额增长率 | 利润总额增长率=(今年利润总额（TTM）/去年利润总额（TTM）)-1 |
| np_parent_company_owners_growth_rate | 归属母公司股东的净利润增长率 | (今年归属于母公司所有者的净利润（TTM）/去年归属于母公司所有者的净利润（TTM）)-1 |
| financing_cash_growth_rate | 筹资活动产生的现金流量净额增长率 | 过去12个月的筹资现金流量净额 / 4季度前的12个月的筹资现金流量净额 - 1 |
| net_profit_growth_rate | 净利润增长率 | 净利润增长率=(今年净利润（TTM）/去年净利润（TTM）)-1 |
| net_asset_growth_rate | 净资产增长率 | （当季的股东权益/三季度前的股东权益）-1 |
| PEG | 市盈率相对盈利增长比率 | PEG = PE / (归母公司净利润(TTM)增长率 * 100) # 如果 PE 或 增长率为负，则为 nan |

#### 每股因子

| 因子 code | 因子名称 | 计算方法 |
| --- | --- | --- |
| total_operating_revenue_per_share_ttm | 每股营业总收入TTM | 营业总收入（TTM）除以总股本 |
| cash_and_equivalents_per_share | 每股现金及现金等价物余额 | 每股现金及现金等价物余额 |
| surplus_reserve_fund_per_share | 每股盈余公积金 | 每股盈余公积金 |
| retained_profit_per_share | 每股未分配利润 | 每股未分配利润 |
| operating_revenue_per_share_ttm | 每股营业收入TTM | 营业收入（TTM）除以总股本 |
| net_asset_per_share | 每股净资产 | (归属母公司所有者权益合计-其他权益工具)除以总股本 |
| total_operating_revenue_per_share | 每股营业总收入 | 每股营业总收入 |
| retained_earnings_per_share | 每股留存收益 | 每股留存收益 |
| operating_revenue_per_share | 每股营业收入 | 每股营业收入 |
| net_operate_cash_flow_per_share | 每股经营活动产生的现金流量净额 | 每股经营活动产生的现金流量净额 |
| operating_profit_per_share_ttm | 每股营业利润TTM | 营业利润（TTM）除以总股本 |
| eps_ttm | 每股收益TTM | 过去12个月归属母公司所有者的净利润（TTM）除以总股本 |
| cashflow_per_share_ttm | 每股现金流量净额，根据当时日期来获取最近变更日的总股本 | 现金流量净额（TTM）除以总股本 |
| operating_profit_per_share | 每股营业利润 | 每股营业利润 |
| capital_reserve_fund_per_share | 每股资本公积金 | 每股资本公积金 |

### 量价因子

#### 情绪因子

| 因子 code | 因子名称 | 计算方法 |
| --- | --- | --- |
| VROC12 | 12日量变动速率指标 | 成交量减N日前的成交量，再除以N日前的成交量，放大100倍，得到VROC值 ，n=12 |
| TVMA6 | 6日成交金额的移动平均值 | 6日成交金额的移动平均值 |
| VEMA10 | 成交量的10日指数移动平均 |  |
| VR | 成交量比率（Volume Ratio） | VR=（AVS+1/2CVS）/（BVS+1/2CVS） |
| VOL5 | 5日平均换手率 | 5日换手率的均值,单位为% |
| BR | 意愿指标 | BR=N日内（当日最高价－昨日收盘价）之和 / N日内（昨日收盘价－当日最低价）之和×100 n设定为26 |
| VEMA12 | 12日成交量的移动平均值 |  |
| TVMA20 | 20日成交金额的移动平均值 | 20日成交金额的移动平均值 |
| DAVOL5 | 5日平均换手率与120日平均换手率 | 5日平均换手率 / 120日平均换手率 |
| VDIFF | 计算VMACD因子的中间变量 | EMA(VOLUME，SHORT)-EMA(VOLUME，LONG) short设置为12，long设置为26，M设置为9 |
| WVAD | 威廉变异离散量 | (收盘价－开盘价)/(最高价－最低价)×成交量，再做加和，使用过去6个交易日的数据 |
| MAWVAD | 因子WVAD的6日均值 |  |
| VSTD10 | 10日成交量标准差 | 10日成交量标准差 |
| ATR14 | 14日均幅指标 | 真实振幅的14日移动平均 |
| VOL10 | 10日平均换手率 | 10日换手率的均值,单位为% |
| DAVOL10 | 10日平均换手率与120日平均换手率之比 | 10日平均换手率 / 120日平均换手率 |
| VDEA | 计算VMACD因子的中间变量 | EMA(VDIFF，M) short设置为12，long设置为26，M设置为9 |
| VSTD20 | 20日成交量标准差 | 20日成交量标准差 |
| ATR6 | 6日均幅指标 | 真实振幅的6日移动平均 |
| VOL20 | 20日平均换手率 | 20日换手率的均值,单位为% |
| DAVOL20 | 20日平均换手率与120日平均换手率之比 | 20日平均换手率 / 120日平均换手率 |
| VMACD | 成交量指数平滑异同移动平均线 | 快的指数移动平均线（EMA12）减去慢的指数移动平均线（EMA26）得到快线DIFF, 由DIFF的M日移动平均得到DEA，由DIFF-DEA的值得到MACD |
| AR | 人气指标 | AR=N日内（当日最高价—当日开市价）之和 / N日内（当日开市价—当日最低价）之和 * 100，n设定为26 |
| VOL60 | 60日平均换手率 | 60日换手率的均值,单位为% |
| turnover_volatility | 换手率相对波动率 | 取20个交易日个股换手率的标准差 |
| VOL120 | 120日平均换手率 | 120日换手率的均值,单位为% |
| VROC6 | 6日量变动速率指标 | 成交量减N日前的成交量，再除以N日前的成交量，放大100倍，得到VROC值 ，n=6 |
| TVSTD20 | 20日成交金额的标准差 | 20日成交额的标准差 |
| ARBR | ARBR | 因子 AR 与因子 BR 的差 |
| money_flow_20 | 20日资金流量 | 用收盘价、最高价及最低价的均值乘以当日成交量即可得到该交易日的资金流量 |
| VEMA5 | 成交量的5日指数移动平均 |  |
| VOL240 | 240日平均换手率 | 240日换手率的均值,单位为% |
| VEMA26 | 成交量的26日指数移动平均 |  |
| VOSC | 成交量震荡 | 'VEMA12'和'VEMA26'两者的差值，再求差值与'VEMA12'的比，最后将比值放大100倍，得到VOSC值 |
| TVSTD6 | 6日成交金额的标准差 | 6日成交额的标准差 |
| PSY | 心理线指标 | 12日内上涨的天数/12 *100 |

#### 风险因子

| 因子 code | 因子名称 | 计算方法 |
| --- | --- | --- |
| Variance20 | 20日年化收益方差 | 20日年化收益方差 |
| Skewness20 | 个股收益的20日偏度 | 个股收益的20日偏度 |
| Kurtosis20 | 个股收益的20日峰度 | 个股收益的20日峰度 |
| sharpe_ratio_20 | 20日夏普比率 | （Rp - Rf）/Sigma p 其中，Rp是个股的年化收益率，Rf是无风险利率（在这里设置为0.04），Sigma p是个股的收益波动率（标准差） |
| Variance60 | 60日年化收益方差 | 60日年化收益方差 |
| Skewness60 | 个股收益的60日偏度 | 个股收益的60日偏度 |
| Kurtosis60 | 个股收益的60日峰度 | 个股收益的60日峰度 |
| sharpe_ratio_60 | 60日夏普比率 | （Rp - Rf）/Sigma p 其中，Rp是个股的年化收益率，Rf是无风险利率（在这里设置为0.04），Sigma p是个股的收益波动率（标准差） |
| Variance120 | 120日年化收益方差 | 120日年化收益方差 |
| Skewness120 | 个股收益的120日偏度 | 个股收益的120日偏度 |
| Kurtosis120 | 个股收益的120日峰度 | 个股收益的120日峰度 |
| sharpe_ratio_120 | 120日夏普比率 | （Rp - Rf）/Sigma p 其中，Rp是个股的年化收益率，Rf是无风险利率（在这里设置为0.04），Sigma p是个股的收益波动率（标准差） |

#### 技术因子

| 因子 code | 因子名称 | 计算方法 |
| --- | --- | --- |
| boll_down | 下轨线（布林线）指标 | (MA(CLOSE,M)-2*STD(CLOSE,M)) / 今日收盘价; M=20 |
| boll_up | 上轨线（布林线）指标 | (MA(CLOSE,M)+2*STD(CLOSE,M)) / 今日收盘价; M=20 |
| EMA5 | 5日指数移动均线 | 5日指数移动均线 / 今日收盘价 |
| EMAC10 | 10日指数移动均线 | 10日指数移动均线 / 今日收盘价 |
| EMAC12 | 12日指数移动均线 | 12日指数移动均线 / 今日收盘价 |
| EMAC20 | 20日指数移动均线 | 20日指数移动均线 / 今日收盘价 |
| EMAC26 | 26日指数移动均线 | 26日指数移动均线 / 今日收盘价 |
| EMAC120 | 120日指数移动均线 | 120日指数移动均线 / 今日收盘价 |
| MAC5 | 5日移动均线 | 5日移动均线 / 今日收盘价 |
| MAC10 | 10日移动均线 | 10日移动均线 / 今日收盘价 |
| MAC20 | 20日移动均线 | 20日移动均线 / 今日收盘价 |
| MAC60 | 60日移动均线 | 60日移动均线 / 今日收盘价 |
| MAC120 | 120日移动均线 | 120日移动均线 / 今日收盘价 |
| MACDC | 平滑异同移动平均线 | MACD(SHORT=12, LONG=26, MID=9) / 今日收盘价 |
| MFI14 | 资金流量指标 | ①求得典型价格（当日最高价，最低价和收盘价的均值）
②根据典型价格高低判定正负向资金流（资金流=典型价格*成交量）
③计算MR= 正向/负向 ④MFI=100-100/（1+MR） |
| price_no_fq | 不复权价格 | 不复权价格 |

#### 动量因子

| 因子 code | 因子名称 | 计算方法 |
| --- | --- | --- |
| arron_up_25 | Aroon指标上轨 | Aroon(上升)=[(计算期天数-最高价后的天数)/计算期天数]*100 |
| arron_down_25 | Aroon指标下轨 | Aroon(下降)=[(计算期天数-最低价后的天数)/计算期天数]*100 |
| BBIC | BBI 动量 | BBI(3, 6, 12, 24) / 收盘价 （BBI 为常用技术指标类因子“多空均线”） |
| bear_power | 空头力道 | (最低价-EMA(close,13)) / close |
| BIAS5 | 5日乖离率 | （收盘价-收盘价的N日简单平均）/ 收盘价的N日简单平均*100，在此n取5 |
| BIAS10 | 10日乖离率 | （收盘价-收盘价的N日简单平均）/ 收盘价的N日简单平均*100，在此n取10 |
| BIAS20 | 20日乖离率 | （收盘价-收盘价的N日简单平均）/ 收盘价的N日简单平均*100，在此n取20 |
| BIAS60 | 60日乖离率 | （收盘价-收盘价的N日简单平均）/ 收盘价的N日简单平均*100，在此n取60 |
| bull_power | 多头力道 | (最高价-EMA(close,13)) / close |
| CCI10 | 10日顺势指标 | CCI:=(TYP-MA(TYP,N))/(0.015*AVEDEV(TYP,N)); TYP:=(HIGH+LOW+CLOSE)/3; N:=10 |
| CCI15 | 15日顺势指标 | CCI:=(TYP-MA(TYP,N))/(0.015*AVEDEV(TYP,N)); TYP:=(HIGH+LOW+CLOSE)/3; N:=15 |
| CCI20 | 20日顺势指标 | CCI:=(TYP-MA(TYP,N))/(0.015*AVEDEV(TYP,N)); TYP:=(HIGH+LOW+CLOSE)/3; N:=20 |
| CCI88 | 88日顺势指标 | CCI:=(TYP-MA(TYP,N))/(0.015*AVEDEV(TYP,N)); TYP:=(HIGH+LOW+CLOSE)/3; N:=88 |
| CR20 | CR指标 | ①中间价=1日前的最高价+最低价/2
②上升值=今天的最高价-前一日的中间价（负值记0）
③下跌值=前一日的中间价-今天的最低价（负值记0）
④多方强度=20天的上升值的和，空方强度=20天的下跌值的和
⑤CR=（多方强度÷空方强度）×100 |
| fifty_two_week_close_rank | 当前价格处于过去1年股价的位置 | 取过去的250个交易日各股的收盘价时间序列，每只股票按照从大到小排列，并找出当日所在的位置 |
| MASS | 梅斯线 | MASS(N1=9, N2=25, M=6) |
| PLRC12 | 12日收盘价格与日期线性回归系数 | 计算 12 日收盘价格，与日期序号（1-12）的线性回归系数，(close / mean(close)) = beta * t + alpha |
| PLRC24 | 24日收盘价格与日期线性回归系数 | 计算 24 日收盘价格，与日期序号（1-24）的线性回归系数， (close / mean(close)) = beta * t + alpha |
| PLRC6 | 6日收盘价格与日期线性回归系数 | 计算 6 日收盘价格，与日期序号（1-6）的线性回归系数，(close / mean(close)) = beta * t + alpha |
| Price1M | 当前股价除以过去一个月股价均值再减1 | 当日收盘价 / mean(过去一个月(21天)的收盘价) -1 |
| Price3M | 当前股价除以过去三个月股价均值再减1 | 当日收盘价 / mean(过去三个月(61天)的收盘价) -1 |
| Price1Y | 当前股价除以过去一年股价均值再减1 | 当日收盘价 / mean(过去一年(250天)的收盘价) -1 |
| Rank1M | 1减去 过去一个月收益率排名与股票总数的比值 | 1-(Rank(个股20日收益) / 股票总数) |
| ROC12 | 12日变动速率（Price Rate of Change） | ①AX=今天的收盘价—12天前的收盘价
②BX=12天前的收盘价
③ROC=AX/BX*100 |
| ROC120 | 120日变动速率（Price Rate of Change） | ①AX=今天的收盘价—120天前的收盘价
②BX=120天前的收盘价
③ROC=AX/BX*100 |
| ROC20 | 20日变动速率（Price Rate of Change） | ①AX=今天的收盘价—20天前的收盘价
②BX=20天前的收盘价
③ROC=AX/BX*100 |
| ROC6 | 6日变动速率（Price Rate of Change） | ①AX=今天的收盘价—6天前的收盘价
②BX=6天前的收盘价
③ROC=AX/BX*100 |
| ROC60 | 60日变动速率（Price Rate of Change） | ①AX=今天的收盘价—60天前的收盘价
②BX=60天前的收盘价
③ROC=AX/BX*100 |
| single_day_VPT | 单日价量趋势 | （今日收盘价 - 昨日收盘价）/ 昨日收盘价 * 当日成交量 # (复权方法为基于当日前复权) |
| single_day_VPT_12 | 单日价量趋势12均值 | MA(single_day_VPT, 12) |
| single_day_VPT_6 | 单日价量趋势6日均值 | MA(single_day_VPT, 6) |
| TRIX10 | 10日终极指标TRIX | MTR=收盘价的10日指数移动平均的10日指数移动平均的10日指数移动平均(求三次ema10);
TRIX=(MTR-1日前的MTR)/1日前的MTR*100 |
| TRIX5 | 5日终极指标TRIX | MTR=收盘价的5日指数移动平均的5日指数移动平均的5日指数移动平均(求三次ema5);
TRIX=(MTR-1日前的MTR)/1日前的MTR*100 |
| Volume1M | 当前交易量相比过去1个月日均交易量 与过去过去20日日均收益率乘积 | 当日交易量 / 过去20日交易量MEAN * 过去20日收益率MEAN |