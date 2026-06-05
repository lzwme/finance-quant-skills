## 获取沪深指数数据

目前只提供了指数的行情数据，指数其他数据请参考[获取中证指数/行业的行情,pe,pb,股息率](https://www.joinquant.com/view/community/detail/16656)

### 指数概况

包含指数的上市时间、退市时间、代码、名称等。平台支持的指数见指数列表。

#### 获取单支指数数据

获取单支指数的信息.

**调用方法**

```python
get_security_info(code)
```

**参数**

- code: 指数代码

**返回值**

- 一个对象, 有如下属性:

- display_name # 中文名称
- name # 缩写简称
- start_date # 上市日期, [datetime.date] 类型
- end_date # 退市日期，[datetime.date] 类型, 如果没有退市则为2200-01-01
- type # 类型，index(指数)

**示例**

```python
# 输出沪深300指数信息
print(get_security_info('000300.XSHG'))
```

#### 获取所有指数数据

获取平台支持的所有指数数据

**调用方法**

```
get_all_securities(types=['index'], date=None)
```

这里请在使用时注意防止未来函数。

**返回**
 - display_name # 中文名称
 - name # 缩写简称
 - start_date # 上市日期
 - end_date # 退市日期，如果没有退市则为2200-01-01
 - type # 类型，index(指数)

[pandas.DataFrame], 比如:`get_all_securities(['index'])[:2]`返回:

|  | display_name | name | start_date | end_date | type |
| --- | --- | --- | --- | --- | --- |
| 000001.XSHG | 上证指数 | SZZS | 1991-07-15 | 2200-01-01 | index |
| 000002.XSHG | A股指数 | AGZS | 1992-02-21 | 2200-01-01 | index |

**示例**

```
print(get_all_securities(['index']))
```

#### 获取指数成份股

获取一个指数给定日期在平台可交易的成分股列表，我们支持近600种股票指数数据，包括指数的行情数据以及成分股数据。为了避免未来函数，我们支持获取历史任意时刻的指数成分股信息。请点击[指数列表](https://www.joinquant.com/data/dict/indexData)查看指数信息.

**调用方法**

```
get_index_stocks(index_symbol, date=None)
```

**参数**
 - index_symbol, 指数代码
 - date: 查询日期, 一个字符串(格式类似’2015-10-15’)或者[datetime.date]/[datetime.datetime]对象, 可以是None, 使用默认日期. 这个默认日期在回测和研究模块上有点差别:

1. 回测模块: 默认值会随着回测日期变化而变化, 等于context.current_dt
2. 研究模块: 默认是今天

**返回**
 - 返回股票代码的list

**示例**

```
# 获取所有沪深300的股票
  codes= get_index_stocks('000300.XSHG')
  print(codes)
```

#### 获取指数成份股权重

获取给定日期和指数的指数成分股权重数据，指数数据请查看下面的**沪深指数列表**

**调用方法**

```
get_index_weights(index_id, date=None)
```

**参数**

- index_id: 代表指数的标准形式代码， 形式：指数代码.交易所代码，例如"000001.XSHG"。
- date: 查询权重信息的日期，形式："%Y-%m-%d"，例如"2018-05-03"；date可以是None，当date=None时，返回最近一次更新的指数成份股权重。

**返回**

- 查询到对应日期，且有权重数据，返回 pandas.DataFrame， code(股票代码)，display_name(股票名称), date(日期), weight(权重)；
- 查询到对应日期，且无权重数据， 返回距离查询日期最近日期的权重信息；
- 找不到对应日期的权重信息， 返回距离查询日期最近日期的权重信息；

**示例**

```
#获取2018年5月9日这天的上证指数的成份股权重
df = get_index_weights(index_id="000001.XSHG", date="2018-05-09")
print(df)

＃输出
code          display_name      date     weight
603648.XSHG         畅联股份  2018-05-09   0.023
603139.XSHG         康惠制药  2018-05-09   0.007
603138.XSHG         海量数据  2018-05-09   0.015
603136.XSHG          天目湖  2018-05-09   0.009
603131.XSHG         上海沪工  2018-05-09   0.011
                 ...         ...     ...
603005.XSHG         晶方科技  2018-05-09   0.023
603007.XSHG         花王股份  2018-05-09   0.013
603006.XSHG         联明股份  2018-05-09   0.008
603009.XSHG         北特科技  2018-05-09   0.014
603008.XSHG          喜临门  2018-05-09   0.022
```

### 行情数据

交易类数据提供指数的行情数据，通过API接口调用即可获取相应的数据。主要包括以下类别：

- [历史行情数据](https://www.joinquant.com/help/data/index#%E5%8E%86%E5%8F%B2%E8%A1%8C%E6%83%85%E6%95%B0%E6%8D%AE)
- [当前单位时间的行情数据](https://www.joinquant.com/help/data/index#%E5%BD%93%E5%89%8D%E5%8D%95%E4%BD%8D%E6%97%B6%E9%97%B4%E7%9A%84%E6%95%B0%E6%8D%AE)

#### 历史行情数据

获取指数历史交易数据，**可以通过参数设置获取日k线、分钟k线数据**。获取数据的基本属性如下：

- open 时间段开始时价格
- close 时间段结束时价格
- low 最低价
- high 最高价
- volume 成交的指数数量
- money 成交的金额
- factor 前复权因子, 我们提供的价格都是前复权后的, 但是利用这个值可以算出原始价格, 方法是价格除以factor, 比如: `close/factor`
- high_limit 涨停价
- low_limit 跌停价
- avg 这段时间的平均价, 等于`money/volume`
- pre_close 前一个单位时间结束时的价格, 按天则是前一天的收盘价, 按分钟这是前一分钟的结束价格
- paused 布尔值, 这只指数是否停牌, 停牌时open/close/low/high/pre_close依然有值,都等于停牌前的收盘价, volume=money=0

**调用方法**

```
get_price(security, start_date='2015-01-01', end_date='2015-12-31', frequency='daily', fields=None, skip_paused=False, fq='pre')
```

**注：设定不同的unit参数，获取日K线或分钟k线，详情见参数。** 这里请在使用时注意防止未来函数.

用户可以在 [after_trading_end](https://www.joinquant.com/api#after_trading_end)中调用[get_price](https://www.joinquant.com/help/data/index#getdd)函数获取当日的开盘价、收盘价、成交额、成交量、最高价以及最低价等

**关于停牌**: 因为此API可以获取多只股票的数据, 可能有的股票停牌有的没有, 为了保持时间轴的一致, 我们默认没有跳过停牌的日期, 停牌时使用停牌前的数据填充(请看[SecurityUnitData]的paused属性). 如想跳过, 请使用 skip_paused=True 参数, 同时只取一只股票的信息

**参数**

- security: 一支指数代码或者一个指数代码的list
 - start_date: 字符串或者[datetime.datetime]/[datetime.date]对象, 开始时间, 默认是’2015-01-01’. 注意:

- 当取分钟数据时, 时间可以精确到分钟, 比如: 传入 `datetime.datetime(2015, 1, 1, 10, 0, 0)` 或者 `'2015-01-01 10:00:00'`.
- 当取分钟数据时, 如果只传入日期, 则日内时间是当日的 00:00:00.
- 当取天数据时, 传入的日内时间会被忽略

- end_date: 格式同上, 结束时间, 默认是’2015-12-31’, 包含此日期. **注意: 当取分钟数据时, 如果 end_date 只有日期, 则日内时间等同于 00:00:00, 所以返回的数据是不包括 end_date 这一天的**.
 - frequency: 单位时间长度, 几天或者几分钟, 现在支持’Xd’,’Xm’, ‘daily’(等同于’1d’), ‘minute’(等同于’1m’), X是一个正整数, 分别表示X天和X分钟(不论是按天还是按分钟回测都能拿到这两种单位的数据), 注意, 当X > 1时, field只支持[‘open’, ‘close’, ‘high’, ‘low’, ‘volume’, ‘money’]这几个标准字段. 默认值是daily
 - fields: 字符串list, 选择要获取的行情数据字段, 默认是None(表示[‘open’, ‘close’, ‘high’, ‘low’, ‘volume’, ‘money’]这几个标准字段), 支持[属性](https://www.joinquant.com/help/data/index#%E5%8E%86%E5%8F%B2%E8%A1%8C%E6%83%85%E6%95%B0%E6%8D%AE)里面的所有基本属性.
 - skip_paused: 是否跳过不交易日期(包括停牌, 未上市或者退市后的日期). 如果不跳过, 停牌时会使用停牌前的数据填充(具体请看[SecurityUnitData]的paused属性), 上市前或者退市后数据都为 nan,, 但要注意:

- 默认为 False

- 当 skip_paused 是 True 时, 只能取一只股票的信息
 - fq: 复权选项:

- `'pre'`: 前复权(根据’use_real_price’选项不同含义会有所不同, 参见[set_option](https://www.joinquant.com/api#set_option)), 默认是前复权
- `None`: 不复权, 返回实际价格
- `'post'`: 后复权

**返回**

- **请注意, 为了方便比较一只指数的多个属性, 同时也满足对比多只指数的一个属性的需求, 我们在security参数是一只指数和多只指数时返回的结构完全不一样**
- 如果是一支指数, 则返回[pandas.DataFrame]对象, 行索引是[datetime.datetime]对象, 列索引是行情字段名字, 比如’open’/’close’. 比如: `get_price('000300.XSHG')[:2]`返回:

|  | open | close | high | low | volume | money |
| --- | --- | --- | --- | --- | --- | --- |
| 2015-01-05 00:00:00 | 3566.09 | 3641.54 | 3669.04 | 3551.51 | 451198098.0 | 519849817448.0 |
| 2015-01-06 00:00:00 | 3608.43 | 3641.06 | 3683.23 | 3587.23 | 420962185.0 | 498529588258.0 |

- 如果是多支指数, 则返回[pandas.Panel]对象, 里面是很多[pandas.DataFrame]对象, 索引是行情字段(open/close/…), 每个[pandas.DataFrame]的行索引是[datetime.datetime]对象, 列索引是指数代号. 比如`get_price(['000300.XSHG', '000001.XSHG'])['open'][:2]`返回:

|  | 000300.XSHG | 000001.XSHG |
| --- | --- | --- |
| 2015-01-05 00:00:00 | 3566.09 | 3258.63 |
| 2015-01-06 00:00:00 | 3608.43 | 3330.80 |

**示例**

```python
# 获取一支指数
df = get_price('000001.XSHG') # 获取000001.XSHG的2015年的按天数据
df = get_price('000001.XSHG', start_date='2015-01-01', end_date='2015-02-01', frequency='minute', fields=['open', 'close']) # 获得000001.XSHG的2015年02月的分钟数据, 只获取open+close字段
df = get_price('000001.XSHG', start_date='2015-12-01 14:00:00', end_date='2015-12-02 12:00:00', frequency='1m') # 获得000001.XSHG的2015年12月1号14:00-2015年12月2日12:00的分钟数据

# 获取多只指数
panel =  get_price(get_index_stocks('000903.XSHG')) # 获取中证100的所有成分股的2015年的天数据, 返回一个[pandas.Panel]
df_open = panel['open']  # 获取开盘价的[pandas.DataFrame],  行索引是[datetime.datetime]对象, 列索引是指数代号
df_volume = panel['volume']  # 获取交易量的[pandas.DataFrame]

print(df_open['000001.XSHE']) # 获取平安银行的2015年每天的开盘价数据
```

#### 当前单位时间的行情数据(策略专用)

获取当前时刻指数的如下属性：
 - high_limit # 涨停价
 - low_limit # 跌停价
 - paused # 是否停牌
 - day_open # 当天开盘价, 分钟回测时可用, 天回测时, 是NaN

**调用方法**

```
get_current_data(security_list=None)
```

回测时, 通过API获取的是一个单位时间(天/分钟)的数据, 而有些数据, 我们在这个单位时间是知道的, 比如涨跌停价,是否停牌,当天的开盘价(分钟回测时). 所以可以使用这个API用来获取这些数据.

**参数**
 - security_list: 指数代码列表.

**返回值**
 一个dict, key是指数代码, value是拥有如下属性的对象
 - high_limit # 涨停价
 - low_limit # 跌停价
 - paused # 是否停牌
 - day_open # 当天开盘价, 分钟回测时可用, 天回测时, 是NaN

**示例**

```
def handle_data(context, data):
      current_data = get_current_data(['000001.XSHG'])
      print current_data
      print current_data['000001.XSHG'].day_open #查询指数当天的开盘价
```

#### 获取指数tick数据

```python
get_ticks(security,end_dt,start_dt,count, fields, skip ,df)
```

**获取指数tick数据， 支持 2017-01-01 至今的tick数据。（每3秒一次快照）**

**参数**：

- security: 指数代码，如'000001.XSHG'
- end_dt: 结束日期，格式为'YYYY-MM-DD HH:MM:SS'
- start_dt: 开始日期，格式为'YYYY-MM-DD HH:MM:SS'
- count: 取出指定时间区间内前N条的tick数据。
- fields: 选择要获取的行情数据字段，默认为None，返回结果如下指数tick返回结果。
- skip:默认为True，过滤掉无成交变化的tick数据；当指定skip=False时，返回的tick数据会保留从2019年9月11日以来无成交的tick数据。
- df:默认为False，返回numpy.ndarray格式的tick数据；df=True的时候，返回pandas.Dataframe格式的数据。
- **指数tick返回结果**

| 字段名 | 说明 | 字段类型 |
| --- | --- | --- |
| time | 时间 | datetime |
| current | 当前价 | float |
| high | 当日最高价 | float |
| low | 当日最低价 | float |
| volume | 累计成交量（股） | float |
| money | 累计成交额 | float |

**获取指数tick数据示例**：

```python
#获取上证指数2019-11-19的tick数据
get_ticks('000001.XSHG',start_dt='2019-11-19 09:00:00',end_dt='2019-11-19 15:05:00')

array([(20191119092524.0, 2904.2783, 2904.2783, 2904.2783, 97512400.0, 1020336191.2),
       (20191119093001.25, 2904.7994, 2904.7994, 2903.8679, 183081500.0, 2000573900.1),
       (20191119093006.55, 2903.451, 2904.7994, 2902.855, 200479500.0, 2179424162.3),
       ...,
       (20191119150000.29, 2932.609, 2933.3961, 2902.855, 13441031700.0, 154664571071.1),
       (20191119150003.0, 2933.3928, 2933.3961, 2902.855, 13515838000.0, 155541500735.1),
       (20191119150003.06, 2933.9908, 2933.9908, 2902.855, 13541760400.0, 155770741258.1)],
      dtype=(numpy.record, [('time', '<f8'), ('current', '<f8'), ('high', '<f8'), ('low', '<f8'), ('volume', '<f8'), ('money', '<f8')]))
```

## 沪深指数列表

我们支持交易所披露的指数数据，包括指数的行情数据以及成分股数据。为了避免未来函数，我们支持获取历史任意时刻的指数成分股信息。
 温馨提示：

- 由于不断会有新的指数被创建，文档无法及时更新，建议直接使用get_all_securities获取所有指数列表
- 指数相关问题如创业板成交量请查看[数据常见问题](https://www.joinquant.com/view/community/detail/1226a48b1f9b7bd90dc3516feea8b5cc?type=2)行情部分
- **因部分中证指数不再由交易所披露行情，部分指数自2020-04-22停止更新，详情见[更新日志](https://www.joinquant.com/view/community/detail/26929)**

```python
df = get_all_securities("index",'2023-06-21')  #获取截至2023-06-21还未退市的指数
df = get_all_securities("index")  #获取所有支持的指数
df[df.display_name.str.contains("全指")] #获取名称中含"全指"的指数
df[df.index.str.contains("000905")]  # 获取000905指数的信息
```