# 因子分析

## 因子定义和计算

**学习资料**

-   [开源因子分析框架：jqfactor_analyzer](https://github.com/JoinQuant/jqfactor_analyzer)
-   [经典教程：因子及多因子分析](https://www.joinquant.com/view/community/detail/5535e9ae3e551e132aa441219a71999d)
-   [【有用功】从单因子到策略](https://www.joinquant.com/view/community/detail/bcde6092a40c993ba697c70d5477cb89)
-   [获取因子看板列表数据](https://www.joinquant.com/help/api/help?name=api#get_factor_kanban_values)

### 因子计算

在回测以及研究中， 可以通过调用jqfactor中的 calc_factors 函数来计算单因子分析中定义的因子值。

为了便于理解，将因子计算部分置于因子定义前面。

```python python
calc_factors(securities, factors, start_date, end_date, use_real_price, skip_paused)

```

**参数**

-   securities: 股票代码列表。
-   factors: 因子(object)列表
-   start_date: 开始日期
-   end_date: 在回测中使用时，注意应该保证截止日期小于 context.current_dt
-   use_real_price: 是否使用真实价格。默认为 False，表示使用后复权价格。
-   skip_paused:是否跳过停牌。 默认为 False。 注意：当 dependencies 使用的因子为价量信息，且 skip_paused = True 时，返回的 DataFrame 的索引由 datetime 变为 int， 值越大，表示离『当前』日期越近。其他情况下，返回的 DataFrame 的索引为 datetime。

**返回值** 返回一个 dict 对象, key 是各 factors 的 name，value 是一个pandas.DataFrame，DataFrame 的 index 是日期， column 是股票代码。

**示例**

示例中的ALPHA013、GROSSPROFITABILITY为自定义因子，定义因子的方法及说明见下节**因子定义**。

```python python
# 导入函数库
from jqfactor import Factor, calc_factors

# 定义因子
class ALPHA013(Factor):
    name = 'alpha013_name'
    max_window = 1
    dependencies = ['high','low','volume','money']
    def calc(self, data):
        high = data['high']
        low = data['low']
        vwap = data['money']/data['volume']
        return (np.power(high*low,0.5) - vwap).mean()

# 定义因子
class GROSSPROFITABILITY(Factor):
    name = 'gross_profitability'
    max_window = 1
    dependencies = ['total_operating_revenue','total_operating_cost','total_assets']
    def calc(self, data):
        total_operating_revenue = data['total_operating_revenue']
        total_operating_cost = data['total_operating_cost']
        total_assets = data['total_assets']
        gross_profitability = (total_operating_revenue - total_operating_cost)/total_assets
        return gross_profitability.mean()
# 定义股票池
securities = ['600000.XSHG','600016.XSHG']
# 计算因子值
factors = calc_factors(securities, [ALPHA013(),GROSSPROFITABILITY()], start_date='2017-01-01', end_date='2017-02-01',  use_real_price=False, skip_paused=False)

# 查看因子值
factors['alpha013_name'].head()
>>>
600000.XSHG  600016.XSHG
2017-01-03    -0.176511    -0.070154
2017-01-04    -0.068026     0.006268
2017-01-05    -0.092072     0.022604
2017-01-06    -0.021411     0.259906
2017-01-09     0.054015    -0.118956

```

### 因子定义

**使用方法**
`用户需要实现一个自定义因子的类， 继承 Factor 类， 并实现 calc 方法。`
`max_window 和 dependencies 定义了在 calc 中可以获取到的数据，calc 实现因子的算法。`
`calc 的返回值即每天的因子值。 calc 需要返回一个pandas.Series。index 是股票代码， value 是因子值。`

```python python
class MA5(Factor):
    name = 'ma5'
    # 每天获取过去五日的数据
    max_window = 5
    # 获取的数据是收盘价
    dependencies = ['close']
    def calc(self, data):
        # print("现在处理{}的数据"format( self._current_date)) #打印逻辑日期
        return data['close'][-5:].mean()

```

**各属性的含义**

-   name： 因子的名称， 不能与基础因子冲突。
-   max_window： 获取数据的最长时间窗口，返回的是日级别的数据。
-   dependencies： 依赖的基础因子名称。
-   main_class: 指定是否为主因子，取值为 True 或 False，仅单因子分析时有效当因子需要定义依赖因子时，用该字段指定需要分析的主因子。

**dependencies 中可以使用的基础因子**

#data_table th:first-of-type {width: 100px;} #data_table th:nth-of-type(3) {width: 400px;} #data_table td{ vertical-align:middle; }
| 数据          | 说明                                                                                                                                                                                                                                                                                 | 示例                                                                                                            |
| ----------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------- |
| 价量信息        | 包含open\close\high\low\money\volume 字段当use_real_price=True时使用动态复权数据 , 为False时使用后复权数据                                                                                                                                                                                                | dependencies=[‘open']                                                                                         |
| 聚宽因子库数据     | 包含质量因子、基础因子、情绪因子、成长因子、风险因子、每股因子等数百个因子数据详细的因子列表请参考因子库                                                                                                                                                                                                                               | 质量因子: 营业周期、市场杠杆dependencies = ['OperatingCycle','MLEV']                                                       |
| 单季度财务指标因子   | 每日可看到的最新单季度财务指标。包含市值数据（valuation）、资产负债数据（balance）、现金流数据（cash_flow）、利润数据（income）、财务指标数据（indicator）。可以直接使用该指标的名称获取数据。详细的指标列表请参考：股票财务数据                                                                                                                                               | 获取利润表（income）中的营业收入（operating_revenue）数据dependencies = [‘operating_revenue']                                  |
| 前 N 季度的财务数据 | 前1-8季度的单季度财务指标。包含资产负债数据（balance）、现金流数据（cash_flow）、利润数据（income）、财务指标数据（indicator）。可以通过在因子后加『_1』的方式， 获取前几个季度的财务指标。详细的指标列表请参考：股票财务数据                                                                                                                                                  | 某公司于6月23日发布半年报，当前的逻辑时间是6月24日operating_revenue 表示第二季度的营业收入operating_revenue_1 表示第一季度的营业收入。                     |
| 过去五年的年度财务数据 | 过去五年的年度财务数据包含资产负债数据（balance）、现金流数据（cash_flow）、利润数据（income）、财务指标数据（indicator）。可以通过在因子后加『_y1』的方式， 获取前几年的财务指标。详细的指标列表请参考：股票财务数据                                                                                                                                                       | 当前的逻辑时间是2016年9月24日operating_revenue_y 表示当前时间可以看到的最新年度营业收入数据，即2015年的营业收入数据operating_revenue_y1 表示2014年的营业收入数据。 |
| 行业因子        | 包含证监会行业分类、聚宽一、二级行业分类以及申万一、二、三级行业分类。因子名称是行业代码， 因子值是一个哑变量，如果某股票属于某行业， 则返回1， 否则， 返回0。详细的行业列表请参考行业数据                                                                                                                                                                                   | 获取聚宽一级能源行业因子dependencies = [‘HY001’]                                                                          |
| 概念因子        | 因子的名称是概念代码，因子值是一个哑变量， 如果某股票属于某个概念，则返回1； 否则，返回0。详细的概念列表请参考概念数据                                                                                                                                                                                                                      | 获取智能电网概念因子dependencies = [‘GN028’]                                                                            |
| 指数因子        | 因子名称是指数代码， 因子值是一个哑变量， 如果某股票属于某个指数，则返回1； 否则，返回0。详细的指数列表请参考指数数据                                                                                                                                                                                                                      | 获取沪深300指数因子dependencies = [‘000300.XSHG’]                                                                     |
| 资金流因子       | 即 get_money_flow API 查询的数据。可以使用的字段包括：change_pct(涨跌幅(%)、net_amount_main(主力净额(万))、net_pct_main(主力净占比(%))、net_amount_xl(超大单净额(万))、net_pct_xl(超大单净占比(%))、net_amount_l(大单净额(万))、net_pct_l(大单净占比(%))、net_amount_m(中单净额(万))、net_pct_m(中单净占比(%))、net_amount_s(小单净额(万))、net_pct_s(小单净占比(%)) | 获取主力净占比因子dependencies = [‘net_pct_main’]                                                                      |

**calc 的参数**

在 calc 中，
(1) self.\_current_date返回当前数据的逻辑日期，使用此日期可以结合其他取数api获取到更多额外的数据，因子分析是使用T日因子值和T+X日后的收益进行分析，因此获取此日期(T日)收盘后的数据不存在未来信息。
(2) 可以通过 data 参数获取通过 max_window 和 dependencies 定义的数据。 data 是一个 dict， key 是 dependencies 中的因子名称， value 是pandas.DataFrame。

-   DataFrame 的 column 是股票代码;
-   DataFrame 的 index 是一个时间序列，结束时间是当前时间， 长度是 max_window;

**calc 的返回值**

需要保证返回一个pandas.Series, index 股票代码， value 是因子值。

注意：当 max_window 设置为1时，返回的是一个**1行N列**的 dataframe。需要使用dataframe.iloc\[0\] 或 dataframe.mean() 的方式转换为一个 Series。

### 在因子定义中获取额外数据

```python python
self._get_extra_data(securities=[],fields=[])

```

在 calc 方法中获取额外数据的方法。可以用来获取指数收盘价等数据。 **只能在 calc 内部使用**

**参数**

-   securities:股票代码的列表，可以使用个股和指数
-   fields:基础因子名称列表。表示需要获取那些基础因子。支持的因子与 dependencies 中相同。

**返回**

-   dict, 结构与 data 类似。 dict 的 key 是 fields 中定义的基础因子名称。 value 是一个 dataframe。 dataframe 的 index 是日期索引， column 是 securities 中定义的股票代码， values 是因子值。 其中， index 的时间跨度与 data 中一致， 都是由 max_window 定义的。

**示例 获取指数收盘价**

```python python
class IndexClose(Factor):
    name = 'indice_close'
    max_window = 10
    dependencies = ['market_cap']

    def calc(self, data):
        market_cap = data['market_cap']
        # 获取指数的开盘收盘价
        index = self._get_extra_data(securities=['000001.XSHG','000002.XSHG','399433.XSHE'],fields=['open','close'])

        print index.keys()
        print index['close'].columns
        print index['open'].head()
        return 0

```

### 因子定义 dependencies 中的财务因子

在因子定义中，如果依赖的基础因子名称（dependencies）为财务因子，可能有些小伙伴理解起来有困难，下面通过一些场景和示例帮助理解。
也可以自学一下金融方面的基础知识，多查看一些上市公司的财务报告。

#### 情景一

当前时间是2015年8月23日， 平安银行二季报的发布日期是 2015年8月15日。

| 基础因子          | 含义             |
| ------------- | -------------- |
| net_profit    | 2015q2 的单季度净利润 |
| net_profit_1  | 2015q1 的单季度净利润 |
| net_profit_y  | 2014 的年度净利润    |
| net_profit_y1 | 2013 的年度净利润    |

#### 情景二

我们继续以 『00001.XSHE』 的数据为例， 说明 data 中返回数据的逻辑。 『00001.XSHE』2017年 Q1 ~ Q3 的三季营业收入数据如下：

| 季度     | 发布时间       | 营业收入        |
| ------ | ---------- | ----------- |
| 2017q1 | 2017-04-22 | 27712000000 |
| 2017q2 | 2017-08-11 | 26360999936 |
| 2017q3 | 2017-10-21 | 25760000000 |

假设我们定义 max_window = 5, dependencies = \['operating_revenue', 'operating_revenue\_1'\]， 观察10月25日的数据情况：

`data['operating_revenue'] 的数据特征`

由于10月21日是周六， 所以数据在10月23日之前为 2017Q2 的数据， 10月23日之后（含当日）为 2017Q3 的数据 **『operating_revenue』 表示每天（index），每个股票（column），可以看到的最新单季度数据（value）**

| 日期/股票      | 000001.XSHE | 000002.XSHE | 000008.XSHE | 000060.XSHE | 000063.XSHE |
| ---------- | ----------- | ----------- | ----------- | ----------- | ----------- |
| 2017-10-19 | 26360999936 | 51221250048 | 365977728   | 5138314240  | 28265984000 |
| 2017-10-20 | 26360999936 | 51221250048 | 365977728   | 5138314240  | 28265984000 |
| 2017-10-23 | 25760000000 | 51221250048 | 365977728   | 5138314240  | 28265984000 |
| 2017-10-24 | 25760000000 | 51221250048 | 365977728   | 5138314240  | 28265984000 |
| 2017-10-25 | 25760000000 | 51221250048 | 365977728   | 5138314240  | 28265984000 |

`data['operating_revenue_1'] 的数据特征`

1.  2017-10-19 能取到的最新数据是 2017Q2 的季报， 而下表中的数据是 2017Q1 的数据。
2.  2017-10-23 能取到的最新数据是 2017Q3 的季报， 而下表中的数据是 2017Q2 的数据。
    总结一下， **『operating_revenue\_1』 表示获取最新报告期上一期的数据**

| 日期/股票      | 000001.XSHE | 000002.XSHE | 000008.XSHE | 000060.XSHE | 000063.XSHE |
| ---------- | ----------- | ----------- | ----------- | ----------- | ----------- |
| 2017-10-19 | 27712000000 | 18589229056 | 202465472   | 4739692032  | 25744611328 |
| 2017-10-20 | 27712000000 | 18589229056 | 202465472   | 4739692032  | 25744611328 |
| 2017-10-23 | 26360999936 | 18589229056 | 202465472   | 4739692032  | 25744611328 |
| 2017-10-24 | 26360999936 | 18589229056 | 202465472   | 4739692032  | 25744611328 |
| 2017-10-25 | 26360999936 | 18589229056 | 202465472   | 4739692032  | 25744611328 |

#### 示例-计算TTM数据

```python python
# 计算营业收入TTM
from jqfactor import Factor
class OR_TTM(Factor):
    # 设置因子名称
    name = 'operating_revenue_ttm'
    # 设置获取数据的时间窗口长度
    max_window = 1
    # 设置依赖的数据，即前四季度的营业收入
    dependencies = ['operating_revenue',
                    'operating_revenue_1',
                    'operating_revenue_2',
                    'operating_revenue_3']

    # 计算因子的函数， 需要返回一个 pandas.Series, index 是股票代码，value 是因子值
    def calc(self, data):
        # 计算 ttm ， 为前四季度相加
        ttm = data['operating_revenue'] + data['operating_revenue_1'] + data['operating_revenue_2'] + data['operating_revenue_3']
        # 将 ttm 转换成 series
        return ttm.mean()

```

## 因子数据处理函数

提供了常见的数据处理方法。
实践过程中，是否应该对原始的因子数据进一步处理、怎么处理最合理、参数怎么设置效果最优等，需要小伙伴们自己进一步的研究。

### 中性化

```python python
neutralize(series, how=None, date=None, axis=1)

```

**参数**

-   data: pd.Series/pd.DataFrame , 待中性化的序列，序列的 index 为股票的 code
-   how: str list 。 中性化使用的因子名称列表。默认为 \['jq_l1', 'market_cap'\] 支持的内容包括：
    -   'jq_l1'： 聚宽一级行业
    -   'jq_l2'： 聚宽二级行业
    -   'sw_l1'： 申万一级行业
    -   'sw_l2'： 申万二级行业
    -   'sw_l3'： 申万三级行业
    -   风险因子：可以使用的风险因子包括： \['size', 'beta', 'momentum', 'residual_volatility', 'non_linear_size', 'book_to_price_ratio', 'liquidity', 'earnings_yield', 'growth', 'leverage'\]
-   date: 日期格式 str 将用 date 这天的相关变量数据对 series 进行中性化
-   axis: 默认为 1。仅在 data 为 pd.DataFrame 时生效。 表示沿哪个方向做标准化，0 为对每列做中性化，1 为对每行做中性化

**返回**

中性化后的因子数据

**示例**

```python python
# 导入需要的函数库
import pandas as pd
import numpy as np
from jqfactor import neutralize
# 生成数据
data = pd.DataFrame(np.random.rand(3,300), columns=get_index_stocks('000300.XSHG', date='2018-05-02'),index=['a', 'b', 'c'])
# 数据中性化
neutralize(data, how=['jq_l1', 'market_cap'], date='2018-05-02', axis=1)

```

### 去极值

```python python
winsorize(series, scale=None, range=None, qrange=None, inclusive=True, inf2nan=True, axis=1)

```

**参数**

-   data: pd.Series/pd.DataFrame/np.array, 待缩尾的序列
-   scale: 标准差倍数，与 range，qrange 三选一，不可同时使用。会将位于 \[mu - scale \* sigma, mu + scale \* sigma\] 边界之外的值替换为边界值
-   range: 列表， 缩尾的上下边界。与 scale，qrange 三选一，不可同时使用。
-   qrange: 列表，缩尾的上下分位数边界，值应在 0 到 1 之间，如 \[0.05, 0.95\]。与 scale，range 三选一，不可同时使用。
-   inclusive: 是否将位于边界之外的值替换为边界值，默认为 True。如果为 True，则将边界之外的值替换为边界值，否则则替换为 np.nan
-   inf2nan: 是否将 np.inf 和 -np.inf 替换成 np.nan，默认为 True如果为 True，在缩尾之前会先将 np.inf 和 -np.inf 替换成 np.nan，缩尾的时候不会考虑 np.nan，否则 inf 被认为是在上界之上，-inf 被认为在下界之下
-   axis: 在 data 为 pd.DataFrame 时使用，沿哪个方向做标准化，默认为 1。 0 为对每列做缩尾，1 为对每行做缩尾。

**返回**

去极值处理之后的因子数据

**示例**

```python python
# 导入需要的函数库
import pandas as pd
import numpy as np
from jqfactor import winsorize
# 生成数据
data = pd.DataFrame(np.random.rand(3,300), columns=get_index_stocks('000300.XSHG', date='2018-05-02'),index=['a', 'b', 'c'])
# 数据去极值
winsorize(data, qrange=[0.05,0.93], inclusive=True, inf2nan=True, axis=1)

```

### 中位数去极值

```python python
winsorize_med(series, scale=1, inclusive=True, inf2nan=True, axis=1)

```

**参数**

-   data: pd.Series/pd.DataFrame/np.array, 待缩尾的序列
-   scale: 倍数，默认为 1.0。会将位于 \[med - scale \* distance, med + scale \* distance\] 边界之外的值替换为边界值/np.nan
-   inclusive bool 是否将位于边界之外的值替换为边界值，默认为 True。 如果为 True，则将边界之外的值替换为边界值，否则则替换为 np.nan
-   inf2nan: 是否将 np.inf 和 -np.inf 替换成 np.nan，默认为 True。如果为 True，在缩尾之前会先将 np.inf 和 -np.inf 替换成 np.nan，缩尾的时候不会考虑 np.nan，否则 inf 被认为是在上界之上，-inf 被认为在下界之下
-   axis: 在 data 为 pd.DataFrame 时使用，沿哪个方向做标准化，默认为 1。0 为对每列做缩尾，1 为对每行做缩尾

**返回**

中位数去极值之后的因子数据

**示例**

```python python
# 导入需要的函数库
import pandas as pd
import numpy as np
from jqfactor import winsorize_med
# 生成数据
data = pd.DataFrame(np.random.rand(3,300), columns=get_index_stocks('000300.XSHG', date='2018-05-02'),index=['a', 'b', 'c'])
# 数据中位数去极值
winsorize_med(data, scale=1, inclusive=True, inf2nan=True, axis=0)

```

### 标准化

```python python
standardlize(series, inf2nan=True, axis=1)

```

**参数**

-   data: pd.Series/pd.DataFrame/np.array, 待标准化的序列
-   inf2nan: 是否将 np.inf 和 -np.inf 替换成 np.nan。默认为 True
-   axis=1: 在 data 为 pd.DataFrame 时使用，如果 series 为 pd.DataFrame，沿哪个方向做标准化。0 为对每列做标准化，1 为对每行做标准化

**返回**

标准化后的因子数据

**示例**

```python python
# 导入需要的函数库
import pandas as pd
import numpy as np
from jqfactor import standardlize
# 生成数据
data = pd.DataFrame(np.random.rand(3,300), columns=get_index_stocks('000300.XSHG', date='2018-05-02'),index=['a', 'b', 'c'])
# 数据标准化
standardlize(data, inf2nan=True, axis=0)

```

## 因子分析

### 因子分析API

为了让用户在[研究环境](https://www.joinquant.com/research)中，可以便捷的分析因子，我们准备了单因子分析工具

```python python
#载入函数库
from jqfactor import analyze_factor

#对因子进行分析
far = analyze_factor(factor, start_date, end_date, industry, universe, quantiles, periods, weight_method, use_real_price, skip_paused, max_loss, factor_dep_definitions)

```

**参数：**

-   factor：因子值，可输入三种类型的值
    -   pandas.DataFrame:因子值，columns为股票代码（如'000001.XSHE'）,index为日期的DatetimeIndex或str
    -   pandas.Series:因子值，index为日期和股票代码的MultiIndex
    -   Factor的子类：因子定义（具体见下方示例）
-   start_date: 开始日期，如果factor为因子定义的话，默认为'2017-01-01'；如果factor为因子值的话，默认为'2017-12-31'
-   end_date: 结束日期，如果factor为因子定义的话，默认为为'2017-12-31'；如果factor为因子值的话，默认为因子值的日期的最大值。
-   industry: 行业分类，默认为'jq_l1'
    -   'sw_l1':申万一级行业
    -   'sw_l2':申万二级行业
    -   'sw_l3':申万三级行业
    -   'jq_l1':聚宽一级行业
    -   'jq_l2':聚宽二级行业
    -   'zjw':证监会行业
-   universe: 对股票池的定义，可输入两种类型的值。**当factor输入为因子值时(DataFrame、Series)，这个参数失效**
    -   str:认为输入的是一个指数，股票池为这个指数的成分股
    -   list：认为输入的是一个股票池
-   quantiles:分位数数量，默认为5
-   periods：调仓周期，int或int的列表，默认为\[1,5,10\]
-   weight_method: 计算分位数收益时的加权方法
    -   avg: 按平均加权
    -   mktcap：按市值加权
-   use_real_price: 是否动态复权，默认为False（当factor为因子值时这个参数失效）
-   skip_paused: 是否跳过停牌，默认为False（当factor为因子值时这个参数失效）。需要注意的情况同 calc_factors 中的 skip_paused 参数
-   max_loss: 因重复值或nan值太多而无效的因子值的最大占比，默认为0.25
-   factor_dep_definitions: 主因子的依赖因子的列表，默认为空列表（注:当factor为因子值时这个参数失效）

**示例一：自定义因子进行分析**

```python python
#导入需要的数据库
from jqfactor import analyze_factor
from jqfactor import Factor

#自定义因子的类
class MA5(Factor):

    name = 'ma5'
    max_window = 5
    dependencies = ['close']

    def calc(self, data):
        return data['close'][-5:].mean()

#使用自定义因子的类进行单因子分析
far = analyze_factor(factor=MA5, start_date='2018-01-01', end_date='2018-03-01', weight_method='mktcap', universe='000300.XSHG', industry='jq_l1', quantiles=8, periods=(1,5,22))

#分析结束后通过不同属性获取数据
far.ic_monthly #月度信息系数

```

**示例二：获取因子库因子进行分析**

```python python
#导入需要的数据库
from jqfactor import analyze_factor
from jqfactor import get_factor_values

#获取因子值pandas.DataFrame
factor_data=get_factor_values(securities=get_index_stocks('000300.XSHG','2018-01-01'), factors=['Skewness60'],
                  start_date='2018-01-01', end_date='2018-03-01')['Skewness60']

#使用获取的因子值进行单因子分析
far = analyze_factor(factor=factor_data, start_date='2018-01-01', end_date='2018-03-01', weight_method='mktcap', industry='jq_l1', quantiles=8, periods=(1,5,22),max_loss=0.2)

#分析结束后通过不同属性获取数据
far.mean_return_std_by_quantile #获取按分位数分组加权平均因子收益

```

### 绘制图表

#### 展示全部分析

```
far.create_full_tear_sheet(demeaned=False, group_adjust=False, by_group=False, turnover_periods=None, avgretplot=(5, 15), std_bar=False)

```

**参数:**

-   demeaned:
    -   True：使用超额收益计算 (基准收益被认为是每日所有股票收益按照weight列中权重加权的均值)
    -   False：不使用超额收益
-   group_adjust:
    -   True：使用行业中性化后的收益计算 (行业收益被认为是每日各个行业股票收益按照weight列中权重加权的均值)
    -   False：不使用行业中性化后的收益
-   by_group:
    -   True: 按行业展示
    -   False: 不按行业展示
-   turnover_periods: 调仓周期
-   avgretplot: tuple 因子预测的天数:(计算过去的天数, 计算未来的天数)
-   std_bar:
    -   True: 显示标准差
    -   False: 不显示标准差

#### 因子值特征分析

```
far.create_summary_tear_sheet(demeaned=False, group_adjust=False)

```

**参数:**

-   demeaned: 详见 calc_mean_return_by_quantile 中 demeaned 参数
    -   True：使用超额收益计算 (基准收益被认为是每日所有股票收益按照weight列中权重加权的均值)
    -   False：不使用超额收益
-   group_adjust: 详见 calc_mean_return_by_quantile 中 group_adjust 参数
    -   True：使用行业中性化后的收益计算 (行业收益被认为是每日各个行业股票收益按照weight列中权重加权的均值)
    -   False：不使用行业中性化后的收益

#### 因子收益分析

```
far.create_returns_tear_sheet(demeaned=False, group_adjust=False, by_group=False)

```

**参数:**

-   demeaned:
    -   True：使用超额收益计算 (基准收益被认为是每日所有股票收益按照weight列中权重加权的均值)
    -   False：不使用超额收益
-   group_adjust:
    -   True：使用行业中性化后的收益计算 (行业收益被认为是每日各个行业股票收益按照weight列中权重加权的均值)
    -   False：不使用行业中性化后的收益
-   by_group:
    -   True: 画各行业的各分位数平均收益图
    -   False: 不画各行业的各分位数平均收益图

#### 因子 IC 分析

```
far.create_information_tear_sheet(group_adjust=False, by_group=False)

```

**参数:**

-   group_adjust:
    -   True: 使用行业中性收益 (行业收益被认为是每日各个行业股票收益按照weight列中权重的加权的均值)
    -   False: 不使用行业中性收益
-   by_group:
    -   True: 画按行业分组信息系数(IC)图
    -   False: 画月度信息系数(IC)图

#### 因子换手率分析

```
far.create_turnover_tear_sheet(turnover_periods=None)

```

**参数:**

-   turnover_periods: 调仓周期

#### 因子预测能力分析

```
far.create_event_returns_tear_sheet(avgretplot=(5, 15), demeaned=False, group_adjust=False,std_bar=False)

```

**参数:**

-   avgretplot: tuple 因子预测的天数: (计算过去的天数, 计算未来的天数)
-   demeaned: 详见 calc_mean_return_by_quantile 中 demeaned 参数
    -   True: 使用超额收益计算累积收益 (基准收益被认为是每日所有股票收益按照weight列中权重加权的均值)
    -   False: 不使用超额收益
-   group_adjust: 详见 calc_mean_return_by_quantile 中 group_adjust 参数
    -   True: 使用行业中性化后的收益计算累积收益 (行业收益被认为是每日各个行业股票收益按照weight列中权重加权的均值)
    -   False: 不使用行业中性化后的收益
-   std_bar:
    -   True: 显示标准差
    -   False: 不显示标准差

#### 打印因子收益表

```
far.plot_returns_table(demeaned=False, group_adjust=False)

```

**参数：**

-   demeaned:
    -   True：使用超额收益计算 (基准收益被认为是每日所有股票收益按照weight列中权重的加权的均值)
    -   False：不使用超额收益
-   group_adjust:
    -   True：使用行业中性收益 (行业收益被认为是每日各个行业股票收益按照weight列中权重的加权的均值)
    -   False：不使用行业中性收益

#### 打印换手率表

```
far.plot_turnover_table()

```

#### 打印信息系数（IC）相关表

```
far.plot_information_table(group_adjust=False, method='rank')

```

**参数：**

-   group_adjust:
    -   True：使用行业中性收益 (行业收益被认为是每日各个行业股票收益按照weight列中权重的加权的均值)
    -   False：不使用行业中性收益
-   method：
    -   'rank'：用秩相关系数计算IC值
    -   'normal': 用相关系数计算IC值

#### 打印各分位数统计表

```
far.plot_quantile_statistics_table()

```

#### 画信息系数(IC)时间序列图

```
far.plot_ic_ts(group_adjust=False, method='rank')

```

**参数：**

-   group_adjust:
    -   True：使用行业中性收益 (行业收益被认为是每日各个行业股票收益按照weight列中权重的加权的均值)
    -   False：不使用行业中性收益
-   method：
    -   'rank'：用秩相关系数计算IC值
    -   'normal': 用相关系数计算IC值

#### 画信息系数分布直方图

```
far.plot_ic_hist(group_adjust=False, method='rank')

```

**参数：**

-   group_adjust:
    -   True：使用行业中性收益 (行业收益被认为是每日各个行业股票收益按照weight列中权重的加权的均值)
    -   False：不使用行业中性收益
-   method：
    -   'rank'：用秩相关系数计算IC值
    -   'normal': 用相关系数计算IC值

#### 画信息系数 qq 图

```
far.plot_ic_qq(group_adjust=False, method='rank', theoretical_dist='norm')

```

**参数：**

-   group_adjust:
    -   True：使用行业中性收益 (行业收益被认为是每日各个行业股票收益按照weight列中权重的加权的均值)
    -   False：不使用行业中性收益
-   method：
    -   'rank'：用秩相关系数计算IC值
    -   'normal': 用相关系数计算IC值
-   theoretical_dist：
    -   'norm'：正态分布
    -   't'：t分布

#### 画各分位数平均收益图

```
far.plot_quantile_returns_bar(by_group=False, demeaned=False, group_adjust=False)

```

**参数：**

-   by_group：
    -   True：各行业的各分位数平均收益图
    -   False：各分位数平均收益图
-   demeaned:
    -   True：使用超额收益计算累积收益 (基准收益被认为是每日所有股票收益按照weight列中权重加权的均值)
    -   False：不使用超额收益
-   group_adjust:
    -   True：使用行业中性化后的收益计算累积收益 (行业收益被认为是每日各个行业股票收益按照weight列中权重加权的均值)
    -   False：不使用行业中性化后的收益

#### 画最高分位减最低分位收益图

```
far.plot_mean_quantile_returns_spread_time_series(demeaned=False, group_adjust=False, bandwidth=1)

```

**参数：**

-   demeaned:
    -   True：使用超额收益计算累积收益 (基准收益被认为是每日所有股票收益按照weight列中权重加权的均值)
    -   False：不使用超额收益
-   group_adjust:
    -   True：使用行业中性化后的收益计算累积收益 (行业收益被认为是每日各个行业股票收益按照weight列中权重加权的均值)
    -   False：不使用行业中性化后的收益
-   bandwidth：n，加减n倍当日标准差

#### 画按行业分组信息系数(IC)图

```
far.plot_ic_by_group(group_adjust=False, method='rank')

```

**参数：**

-   group_adjust:
    -   True：使用行业中性收益 (行业收益被认为是每日各个行业股票收益按照weight列中权重的加权的均值)
    -   False：不使用行业中性收益
-   method：
    -   'rank'：用秩相关系数计算IC值
    -   'normal': 用相关系数计算IC值

#### 画因子自相关图

```
far.plot_factor_auto_correlation(periods=None, rank=True)

```

**参数：**

-   periods: 滞后周期

-   rank：

    -   True：用秩相关系数
    -   False：用相关系数

#### 画最高最低分位换手率图

```
far.plot_top_bottom_quantile_turnover(periods=(1, 3, 9))

```

**参数：**

-   periods：调仓周期

#### 画月度信息系数(IC)图

```
far.plot_monthly_ic_heatmap(group_adjust=False)

```

**参数：**

-   group_adjust:
    -   True：使用行业中性收益 (行业收益被认为是每日各个行业股票收益按照weight列中权重的加权的均值)
    -   False：不使用行业中性收益 数值越接近0，会越趋向于黄色。 数值大于0会逐渐过渡到绿色 数值小于0会逐渐过渡到红色

#### 画按因子值加权多空组合每日累积收益图

```
far.plot_cumulative_returns(period=1, demeaned=False, group_adjust=False)

```

**参数：**

-   periods：调仓周期
-   demeaned: 详见 calc_factor_returns 中 demeaned 参数
    -   True：对因子值加权组合每日收益的权重去均值 (每日权重 = 每日权重 - 每日权重的均值),使组合转换为cash-neutral多空组合
    -   False：不对权重去均值
-   group_adjust: 详见 calc_factor_returns 中 group_adjust 参数
    -   True：对权重分行业去均值 (每日权重 = 每日权重 - 每日各行业权重的均值)，使组合转换为 industry-neutral 多空组合
    -   False：不对权重分行业去均值

#### 画各分位数每日累积收益图

```
far.plot_cumulative_returns_by_quantile(period=(1, 3, 9), demeaned=False, group_adjust=False)

```

**参数：**

-   period：调仓周期
-   demeaned: 详见 calc_mean_return_by_quantile 中 demeaned 参数
    -   True：使用超额收益计算累积收益 (基准收益被认为是每日所有股票收益按照weight列中权重加权的均值)
    -   False：不使用超额收益
-   group_adjust: 详见 calc_mean_return_by_quantile 中 group_adjust 参数
    -   True：使用行业中性化后的收益计算累积收益 (行业收益被认为是每日各个行业股票收益按照weight列中权重加权的均值)
    -   False：不使用行业中性化后的收益

#### 因子预测能力平均累计收益图

```
far.plot_quantile_average_cumulative_return(periods_before=5, periods_after=10, by_quantile=False, std_bar=False, demeaned=False, group_adjust=False)

```

**参数：**

-   periods_before: 计算过去的天数
-   periods_after: 计算未来的天数
-   by_quantile：是否各分位数分别显示因子预测能力平均累计收益图
-   std_bar：
    -   True：显示标准差
    -   False：不显示标准差
-   demeaned: 详见 calc_mean_return_by_quantile 中 demeaned 参数
    -   True：使用超额收益计算累积收益 (基准收益被认为是每日所有股票收益按照weight列中权重加权的均值)
    -   False：不使用超额收益
-   group_adjust: 详见 calc_mean_return_by_quantile 中 group_adjust 参数
    -   True：使用行业中性化后的收益计算累积收益 (行业收益被认为是每日各个行业股票收益按照weight列中权重加权的均值)
    -   False：不使用行业中性化后的收益

#### 画有效因子数量统计图

```
far.plot_events_distribution(num_days=1)

```

**参数：**

-   num_days：统计间隔天数

#### 关闭中文图例显示

```
far.plot_disable_chinese_label()

```

### 属性列表

用于访问因子分析的结果，大部分为惰性属性，在访问才会计算结果并返回

#### 查看因子值

```
far.factor_data

```

-   类型：pandas.Series
-   index：为日期和股票代码的MultiIndex

#### 去除 nan/inf，整理后的因子值、forward_return 和分位数

```
far.clean_factor_data

```

-   类型：pandas.DataFrame index：为日期和股票代码的MultiIndex
-   columns：根据period选择后的forward_return(如果调仓周期为1天，那么forward_return为\[第二天的收盘价-今天的收盘价\]/今天的收盘价)、因子值、行业分组、分位数数组、权重

#### 按分位数分组加权平均因子收益

```
far.mean_return_by_quantile

```

-   类型：pandas.DataFrame
-   index：分位数分组
-   columns：调仓周期

#### 按分位数分组加权因子收益标准差

```
far.mean_return_std_by_quantile

```

-   类型：pandas.DataFrame
-   index：分位数分组
-   columns：调仓周期

#### 按分位数及日期分组加权平均因子收益

```
far.mean_return_by_date

```

-   类型：pandas.DataFrame
-   index：为日期和分位数的MultiIndex
-   columns：调仓周期

#### 按分位数及日期分组加权因子收益标准差

```
far.mean_return_std_by_date

```

-   类型：pandas.DataFrame
-   index：为日期和分位数的MultiIndex
-   columns：调仓周期

#### 按分位数及行业分组加权平均因子收益

```
far.mean_return_by_group

```

-   类型：pandas.DataFrame
-   index：为行业和分位数的MultiIndex
-   columns：调仓周期

#### 按分位数及行业分组加权因子收益标准差

```
far.mean_return_std_by_group

```

-   类型：pandas.DataFrame
-   index：为行业和分位数的MultiIndex
-   columns：调仓周期

#### 最高分位数因子收益减最低分位数因子收益每日均值

```
far.mean_return_spread_by_quantile

```

-   类型：pandas.DataFrame
-   index：日期
-   columns：调仓周期

#### 最高分位数因子收益减最低分位数因子收益每日标准差

```
far.mean_return_spread_std_by_quantile

```

-   类型：pandas.DataFrame
-   index：日期
-   columns：调仓周期

#### 信息系数

```
far.ic

```

-   类型：pandas.DataFrame
-   index：日期
-   columns：调仓周期

#### 分行业信息系数

```
far.ic_by_group

```

-   类型：pandas.DataFrame
-   index：行业
-   columns：调仓周期

#### 月度信息系数

```
far.ic_monthly

```

-   类型：pandas.DataFrame
-   index：月度
-   columns：调仓周期表

#### 换手率

```
far.quantile_turnover

```

-   键：调仓周期
-   值: pandas.DataFrame 换手率
    -   index：日期
    -   columns：分位数分组

#### 计算按分位数分组因子收益和标准差

```
mean,std = far.calc_mean_return_by_quantile(by_date=False, by_group=False, demeaned=False, group_adjust=False)

```

因子收益为收益按照 weight 列中权重的加权平均值

**参数：**

-   by_date：
    -   True: 按天计算收益
    -   False: 不按天计算收益
-   by_group:
    -   True: 按行业计算收益
    -   False：不按行业计算收益
-   demeaned:
    -   True: 使用超额收益计算各分位数收益，收益=收益-基准收益 (基准收益被认为是每日所有股票收益按照weight列中权重的加权的均值)
    -   False：不使用超额收益
-   group_adjust:
    -   True: 使用行业中性收益计算各分位数收益，收益=收益-行业收益 (行业收益被认为是每日各个行业股票收益按照weight列中权重的加权的均值)
    -   False：不使用行业中性收益

#### 计算按因子值加权组合每日收益

```
far.calc_factor_returns(demeaned=True, group_adjust=False)

```

权重 = 每日因子值 / 每日因子值的绝对值的和

正的权重代表买入, 负的权重代表卖出

**参数：**

-   demeaned:
    -   True: 对权重去均值 (每日权重 = 每日权重 - 每日权重的均值), 使组合转换为 cash-neutral 多空组合
    -   False：不对权重去均值
-   group_adjust:
    -   True：对权重分行业去均值 (每日权重 = 每日权重 - 每日各行业权重的均值)，使组合转换为 industry-neutral 多空组合
    -   False：不对权重分行业去均值

#### 计算两个分位数相减的因子收益和标准差

```
mean, std = far.compute_mean_returns_spread (upper_quant=None, lower_quant=None, by_date=True, by_group=False, demeaned=False, group_adjust=False)

```

**参数：**

-   upper_quant：用upper_quant选择的分位数减去lower_quant选择的分位数，只能在已有的范围内选择，默认为最大分位
-   lower_quant：用upper_quant选择的分位数减去lower_quant选择的分位数，只能在已有的范围内选择，默认为最小分位
-   by_date：
    -   True：按天计算两个分位数相减的因子收益和标准差
    -   False：不按天计算两个分位数相减的因子收益和标准差
-   by_group:
    -   True: 分行业计算两个分位数相减的因子收益和标准差
    -   False：不分行业计算两个分位数相减的因子收益和标准差
-   demeaned:
    -   True：使用超额收益计算 (基准收益被认为是每日所有股票收益按照weight列中权重的加权的均值)
    -   False：不使用超额收益
-   group_adjust:
    -   True：使用行业中性收益 (行业收益被认为是每日各个行业股票收益按照weight列中权重的加权的均值)
    -   False：不使用行业中性收益

#### 计算因子的 alpha 和 beta

```
far.calc_factor_alpha_beta(demeaned=True, group_adjust=False)

```

因子值加权组合每日收益 = beta \* 市场组合每日收益 + alpha

因子值加权组合每日收益计算方法见 calc_factor_returns 函数，

市场组合每日收益是每日所有股票收益按照weight列中权重加权的均值，

结果中的 alpha 是年化 alpha

**参数：**

-   demeaned: 详见 calc_factor_returns 中 demeaned 参数
    -   True: 对因子值加权组合每日收益权重去均值 (每日权重 = 每日权重 - 每日权重的均值),使组合转换为cash-neutral多空组合
    -   False：不对权重去均值
-   group_adjust: 详见 calc_factor_returns 中 group_adjust 参数
    -   True：对权重分行业去均值 (每日权重 = 每日权重 - 每日各行业权重的均值)，使组合转换为 industry-neutral 多空组合
    -   False：不对权重分行业去均值

#### 计算每日因子信息系数（IC值）

```
far.calc_factor_information_coefficient(group_adjust=False, by_group=False, method='rank')

```

**参数：**

-   group_adjust:
    -   True：使用行业中性收益计算 IC (行业收益被认为是每日各个行业股票收益按照weight列中权重加权的均值)
    -   False：不使用行业中性收益
-   by_group:
    -   True：分行业计算 IC
    -   False：不分行业计算 IC
-   method：
    -   'rank'：用秩相关系数计算IC值
    -   'normal'：用普通相关系数计算IC值

#### 计算因子信息系数均值（IC值均值）

```
far.calc_mean_information_coefficient(group_adjust=False, by_group=False, by_time=None, method='rank')

```

**参数：**

-   group_adjust:
    -   True：使用行业中性收益计算 IC (行业收益被认为是每日各个行业股票收益按照weight列中权重加权的均值)
    -   False：不使用行业中性收益
-   by_group:
    -   True：分行业计算 IC
    -   False：不分行业计算 IC
-   by_time：
    -   'Y'：按年求均值
    -   'M'：按月求均值
    -   None：对所有日期求均值
-   method：
    -   'rank'：用秩相关系数计算IC值
    -   'normal'：用普通相关系数计算IC值

#### 按照当天的分位数算分位数未来和过去的收益均值和标准差

```
far.calc_average_cumulative_return_by_quantile(periods_before=5, periods_after=15, demeaned=False, group_adjust=False)

```

**参数：**

-   periods_before：计算过去的天数
-   periods_after：计算未来的天数
-   demeaned：是否使用超额收益计算累积收益 (基准收益被认为是每日所有股票收益按照weight列中权重加权的均值)
-   group_adjust：是否使用行业中性化后的收益计算累积收益 (行业收益被认为是每日各个行业股票收益按照weight列中权重加权的均值)

#### 计算指定调仓周期的各分位数每日累积收益

```
far.calc_cumulative_return_by_quantile(period=5)

```

**参数：**

-   period：指定调仓周期

#### 计算指定调仓周期的按因子值加权组合每日累积收益

```
far.calc_cumulative_returns(period=5, demeaned=False, group_adjust=False)

```

当 调仓周期 period > 1 时，组合的累积收益计算方法为：

组合每日收益 = （从第0天开始每period天一调仓的组合每日收益 + 从第1天开始每period天一调仓的组合每日收益 + … + 从第period-1天开始每period天一调仓的组合每日收益) / period

组合累积收益 = 组合每日收益的累积

**参数：**

-   period：指定调仓周期
-   demeaned: 详见 calc_factor_returns 中 demeaned 参数
    -   True：对权重去均值 (每日权重 = 每日权重 - 每日权重的均值), 使组合转换为 cash-neutral 多空组合
    -   False：不对权重去均值
-   group_adjust: 详见 calc_factor_returns 中 group_adjust 参数
    -   True：对权重分行业去均值 (每日权重 = 每日权重 - 每日各行业权重的均值)，使组合转换为 industry-neutral 多空组合
    -   False：不对权重分行业去均值

#### 计算做多最大分位，做空最小分位组合每日累积收益

```
far.calc_top_down_cumulative_returns(period=5, demeaned=False, group_adjust=False)

```

当 调仓周期 period > 1 时，组合的累积收益计算方法 见 calc_cumulative_returns

**参数：**

-   period：指定调仓周期
-   demeaned: 详见 calc_mean_return_by_quantile 中 demeaned 参数
    -   True：使用超额收益计算累积收益 (基准收益被认为是每日所有股票收益按照weight列中权重加权的均值)
    -   False：不使用超额收益
-   group_adjust: 详见 calc_mean_return_by_quantile 中 group_adjust 参数
    -   True：使用行业中性化后的收益计算累积收益 (行业收益被认为是每日各个行业股票收益按照weight列中权重加权的均值)
    -   False：不使用行业中性化后的收益

#### 根据调仓周期确定滞后期的每天计算因子自相关性

```
far.calc_autocorrelation(rank=True)

```

当日因子值和滞后period天的因子值的自相关性

**参数：**

-   rank：
    -   True：秩相关系数
    -   False：普通相关系数

#### 滞后1-n天因子值自相关性均值

```
far.calc_autocorrelation_n_days_lag(n=9,rank=True)

```

**参数：**

-   n：滞后1天到n天的因子值自相关性
-   rank：
    -   True：秩相关系数
    -   False：普通相关系数

#### 各分位数滞后1天到n天的换手率均值

```
far.calc_quantile_turnover_mean_n_days_lag(n=10)

```

**参数：**

-   n: 滞后1天到n天的换手率

#### 滞后 0 - n 天因子收益信息系数(IC)的均值

```
far.calc_ic_mean_n_days_lag(n=10,group_adjust=False,by_group=False,method=None)

```

滞后 n 天 IC 表示使用当日因子值和滞后 n 天的因子收益计算 IC

**参数：**

-   n：滞后0-n天因子收益的信息系数(IC)的均值
-   group_adjust:
    -   True：使用行业中性收益计算 IC (行业收益被认为是每日各个行业股票收益按照weight列中权重加权的均值)
    -   False：不使用行业中性收益
-   by_group：
    -   True：分行业计算 IC
    -   False：不分行业计算 IC
-   method：
    -   'rank'：用秩相关系数计算IC值
    -   'normal'：用普通相关系数计算IC值

## 因子分析结果

### 收益分析

在收益分析中, 分位数的平均收益， 各分位数的累积收益， 以及分位数的多空组合收益三方面观察因子的表现。 第一分位数的因子值最小， 第五分位数的因子值最大。

1.  分位数收益： 表示持仓1、5、10天后，各分位数可以获得的平均收益。
2.  分位数的累积收益： 表示各分位数持仓收益的累计值。
3.  多空组合收益： 做多五分位（因子值最大）， 做空一分位（因子值最小）的投资组合的收益。

### IC 分析

IC 是 information coefficient 的缩写。IC 代表了预测值和实现值之间的相关性， 通常用以评价预测能力。 取值在-1到1之间， 绝对值越大， 表示预测能力越好。

IC 的计算， 一般有两种方法， normal IC 与 rank IC。 我们计算的是rank IC.

-   normal IC： 因子载荷与因子收益之间的相关系数

-   rank IC： 因子载荷的排序值与收益的排序值之间的相关系数

-   详情：[normal IC 与 rank IC 的区别](#normal_rank_IC)

    同时考虑到单日 IC 的波动较大， 我们提供了 IC 的月度移动平均线作为参考。


### 换手率分析

因子的换手率是在不同的时间周期下， 观察因子个分位中个股的进出情况。 计算方法举例： 某因子第一分位持有的股票数量为30支， 一天后有一只发生变动， 换手率为： 1/30 \*100% = 3.33% 对于5日、10日的换手率，在每日都会对比当日1、5分位数的成分股与5日、10日前该分位数的成分股的变化进行计算。

因子分位数换手率的价值体现在两个方面：

1.  因子稳定性的体现：换手率低的因子，因子值在时间序列层面的持续性更好
2.  衡量交易成本：在实际的交易过程中， 假设我们要维护投资组合的因子暴露恒定， 对于高换手率因子， 则需要进行更多的交易。 交易中的税费和滑点， 也会吞噬掉我们的部分利润。

## 示例

### 『价量』alpha 191 中的 013

**因子链接**

-   [alpha\_013](/data/dict/alpha191#alpha013)

**因子公式**

-   (((HIGH\*LOW)^0.5)-VWAP)

**因子实现**

```python python
from jqfactor import Factor
import numpy as np

class ALPHA013(Factor):
    # 设置因子名称
    name = 'alpha013'
    # 设置获取数据的时间窗口长度
    max_window = 1
    # 设置依赖的数据
    dependencies = ['high','low','volume','money']

    # 计算因子的函数， 需要返回一个 pandas.Series, index 是股票代码，value 是因子值
    def calc(self, data):

    # 最高价的 dataframe ， index 是日期， column 是股票代码
        high = data['high']

        # 最低价的 dataframe ， index 是日期， column 是股票代码
        low = data['low']

        #计算 vwap
        vwap = data['money']/data['volume']

        # 返回因子值， 这里求平均值是为了把只有一行的 dataframe 转成 series
        return (np.power(high*low,0.5) - vwap).mean()

```

### 『基本面』gross profitability

**参考链接**

-   [首席质量因子 - Gross Profitability -- 小兵哥](https://www.joinquant.com/post/6585?tag=algorithm)

**因子公式**

-   (total_operating_revenue - total_operating_cost) / total_assets

**因子实现**

```python python
from jqfactor import Factor

class GROSSPROFITABILITY(Factor):
    # 设置因子名称
    name = 'gross_profitability'
    # 设置获取数据的时间窗口长度
    max_window = 1
    # 设置依赖的数据
    # 在策略中需要使用 get_fundamentals 获取的 income.total_operating_revenue, 在这里可以直接写做total_operating_revenue。 其他数据同理。
    dependencies = ['total_operating_revenue','total_operating_cost','total_assets']

    # 计算因子的函数， 需要返回一个 pandas.Series, index 是股票代码，value 是因子值
    def calc(self, data):
        # 获取单季度的营业总收入数据 , index 是日期，column 是股票代码， value 是营业总收入
        total_operating_revenue = data['total_operating_revenue']
        # 获取单季度的营业总成本数据
        total_operating_cost = data['total_operating_cost']
        # 获取总资产
        total_assets = data['total_assets']
        # 计算 gross_profitability
        gross_profitability = (total_operating_revenue - total_operating_cost)/total_assets
        # 由于 gross_profitability 是一个一行 n 列的 dataframe，可以直接求 mean 转成 series
        return gross_profitability.mean()

```

### 『中性化』产权比率

**因子公式**

-   负债合计/归属母公司所有者权益合计

**因子实现**

```python python
from jqfactor import Factor
import numpy as np
import pandas as pd

class DebtEquityRatio(Factor):
    name = 'debt_to_equity_ratio'
    max_window = 1
    dependencies = ['total_liability','equities_parent_company_owners',
                    # 以下为中性化需要使用的数据
                    'market_cap',
                    'HY001','HY002','HY003',
                    'HY004','HY005','HY006',
                    'HY007','HY008','HY009',
                    'HY010','HY011']

    def calc(self, data):
        tl = data['total_liability']
        epco = data['equities_parent_company_owners']
        result = tl / epco
        return neutralization(data, result.mean())

# 行业市值中性化
def neutralization(data, factor):
    from statsmodels.api import OLS
    industry_exposure = pd.DataFrame(index=data['HY001'].columns)
    industry_list = ['HY001','HY002','HY003','HY004','HY005',
                    'HY006','HY007','HY008','HY009','HY010','HY011']
    for key, value in data.items():
        if key in industry_list:
            industry_exposure[key]=value.iloc[-1]
    market_cap_exposure = data['market_cap'].iloc[-1]
    total_exposure = pd.concat([market_cap_exposure,industry_exposure],axis=1)
    result = OLS(factor, total_exposure, missing='drop').fit().resid
    return result

```

### 『指数』近10日 alpha

**因子公式**

-   个股近10日收益 - 指数（沪深300）近10日收益 近10日收益计算方法： (第10日价格/第1日价格) - 1

**因子实现**

```python python
from jqfactor import Factor

class Hs300Alpha(Factor):
    # 设置因子名称
    name = 'hs300_alpha'
    # 设置获取数据的时间窗口长度
    max_window = 10
    # 设置依赖的数据
    dependencies = ['close']

    # 计算因子的函数， 需要返回一个 pandas.Series, index 是股票代码，value 是因子值
    def calc(self, data):
        # 获取个股的收盘价数据
        close = data['close']
        # 计算个股近10日收益
        stock_return = close.iloc[-1,:]/close.iloc[0,:] -1
        # 获取指数（沪深300）的收盘价数据
        index_close = self._get_extra_data(securities=['000300.XSHG'], fields=['close'])['close']
        # 计算指数的近10日收益
        index_return = index_close.iat[-1,0]/index_close.iat[0,0] - 1
        # 计算 alpha
        alpha = stock_return - index_return
        return alpha

```

### 『基本面』近两年净利润增长率

**因子公式**

-   最新一年度的净利润/上一年度的净利润 -1

**因子实现**

```python python
from jqfactor import Factor

class NetProfitGrowth(Factor):
    # 设置因子名称
    name = 'net_profit_growth_rate'
    # 设置获取数据的时间窗口长度
    max_window = 1
    # 设置依赖的数据
    dependencies = ['net_profit_y','net_profit_y1']

    # 计算因子的函数， 需要返回一个 pandas.Series, index 是股票代码，value 是因子值
    def calc(self, data):
        # 个股最新一年度的净利润数据
        net_profit_y = data['net_profit_y']
        # 个股最新一年度的上一年的净利润数据
        net_profit_y1 = data['net_profit_y1']
        # 计算增长率
        growth = net_profit_y/net_profit_y1 - 1
        # 返回一个 series
        return growth.mean()

```

### 『多季度』 资产回报率

**因子公式**

-   过去四个季度的净利润之和/期末总资产

**因子实现**

```python python
class ROATTM(Factor):
    name = 'roa_ttm'
    max_window = 1
    # 定义依赖的数据： 过去四个季度的净利润， 以及最新一个季度的总资产
    dependencies = ['net_profit', 'net_profit_1', 'net_profit_2', 'net_profit_3',
                    'total_assets']

    def calc(self, data):
        # 计算净利润的 ttm 值
        net_profit_ttm = data['net_profit'] + data['net_profit_1'] + data['net_profit_2'] + data['net_profit_3']
        # 计算 ROA
        result = net_profit_ttm / data['total_assets']
        # 把结果转成一个 series
        return result.mean()

```

### 构建因子数据进行单因子分析

前面的例子讲述了通过自定义类实现因子，本例讲解如何直接获取因子数据或者构建因子数据，然后对得到的数据进行单因子分析。
其中的factor_data数据需要自己获取，并整理成符合因子分析要求的格式。
更多关于factor_data数据格式请查看单因子分析框架[jqfactor_analyzer](https://github.com/JoinQuant/jqfactor_analyzer)

```python python
# 载入函数库
from jqfactor import analyze_factor
from jqdata import *
from jqlib import alpha191
import pandas as pd
import warnings
warnings.filterwarnings("ignore")

# 测试开始时间
start_date = '2019-10-01'
# 测试结束时间
end_date = '2019-11-11'
# 测试时间区间的交易日
date_list = get_trade_days(start_date=start_date, end_date=end_date)
# 转换交易日时间的数据类型
# date_list = [date.strftime('%Y-%m-%d') for date in date_list]

# 获取一段时间股票池191因子数据
factor_data = {}
# 循环获取每天数据
for date in date_list:
    # 获取每天的股票池
    universe = get_index_stocks('000300.XSHG', date=date)
    # 获取每天股票池的因子数据
    _factor_data = alpha191.alpha_002(code=universe, end_date=date, fq='post')
    # 添加每天的因子数据
    factor_data[date] = _factor_data

# 将字典类型数据转换为DataFrame
factor_data = pd.DataFrame(factor_data).T
# 将 index 转换为 DatetimeIndex
factor_data.index = pd.to_datetime(factor_data.index)

# 对因子进行分析，参数使用默认值
far = analyze_factor(factor=factor_data, )
# 展示全部分析
far.create_full_tear_sheet(demeaned=False, group_adjust=False, by_group=False, turnover_periods=None,
                           avgretplot=(5, 15), std_bar=False)

```

### 多因子参考资料

1.  《主动投资组合管理》 英文版的名称是"Active Portfolio Management"
2.  Quantitative Equity Portfolio Management -- An Active Approach to Portfolio Construction and Management
3.  Quantitative Equity Portfolio Management -- Modern Techniques and Applications
4.  Barra Risk Model Handbook

## 附录

### normal IC 与 rank IC 的区别

#### 1、normal IC

IC（Information coefficient 信息系数)的定义：t期的因子载荷（因子值）和t+1期的因子收益之间的相关系数。

举个例子：

因子：Variance20 20日收益方差

股票池：000001.XSHE(平安银行)、000002.XSHE(万科A)、000060.XSHE(中金岭南)、000063.XSHE(中兴通讯)、000069.XSHE(华侨城A)

日期：2018年1月2日

| 股票代码        | 因子值      | 下期股票收益  |
| ----------- | -------- | ------- |
| 000001.XSHE | 0.120140 | -0.0267 |
| 000002.XSHE | 0.105666 | -0.0070 |
| 000060.XSHE | 0.07945  | -0.0547 |
| 000063.XSHE | 0.237343 | 0.0269  |
| 000069.XSHE | 0.134598 | 0.0057  |

(注：下期股票收益为股票下一交易日的涨幅)

可以求IC得两个必要条件就是求到因子值和下一期的股票收益，我们对这两列求相关系数就可以得到该因子在当前股票池范围内的IC值，值为0.8505（由于上表中的股票池极少，导致了求得的IC值比较高）。我们对每一天都求一个IC值就可以得到IC值得时间序列图，单日IC值得波动是比较大的，所以提供了IC的月度移动平均线作为参考，而因子的有效性也是通过IC值均值来判断，当IC值均值大于0.03，可以说该因子是有效因子。

注：当样本股票过少时，IC是没有统计意义的，在对因子做有效性分析时，要保证至少有100只股票，IC才有意义。

#### 2、rank IC

rank IC和IC唯一的不同点就是在求相关系数时，换成秩相关系数，即： rank IC： t 期的因子载荷（因子值）的排序值和 t+1 期的因子收益的排序值之间的相关系数。

举个例子：

| 股票代码        | 因子值      | 因子值排名 | 下期股票收益  | 下期股票收益排名 |
| ----------- | -------- | ----- | ------- | -------- |
| 000001.XSHE | 0.120140 | 3     | -0.0267 | 2        |
| 000002.XSHE | 0.105666 | 2     | -0.0070 | 3        |
| 000060.XSHE | 0.07945  | 1     | -0.0547 | 1        |
| 000063.XSHE | 0.237343 | 5     | 0.0269  | 5        |
| 000069.XSHE | 0.134598 | 4     | 0.0057  | 4        |

(注：下期股票收益为股票下一交易日的涨幅)

IC值是对因子值和下期股票收益求相关系数，而rank IC值是对因子值排名和下期股票收益排名求相关系数，值为0.8999。

现在更多的人选择用rank IC来代替普通的IC，这是因为普通的IC求相关系数有一个前提条件，就是数据要服从正态分布，但金融类数据往往并不如此，所以现在更多人采用秩相关系数也就是rank IC来判断因子的有效性。

### 常见问题或报错

### ValueError: No objects to concatenate

检查下得到的因子数据索引的数据类型是否正常，index为日期的DatetimeIndex;可以使用pandas的to_datetime方法转换；

### 将自有因子值转换成 DataFrame 格式的数据

[将自有因子值转换成 DataFrame 格式的数据](https://github.com/JoinQuant/jqfactor_analyzer)