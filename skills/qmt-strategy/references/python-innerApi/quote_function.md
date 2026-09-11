---
url: "https://dict.thinktrader.net/innerApi/quote_function.html"
title: "引用函数 | 迅投知识库"
---

## ext_data - 获取扩展数据

获取扩展数据

**调用方法：**`ext_data(extdataname, stockcode, deviation, ContextInfo)`

**参数：**

| 参数名 | 类型 | 说明 | 提示 |
| --- | --- | --- | --- |
| `extdataname` | `string` | 扩展数据名 |  |
| `stockcode` | `string` | 证券代码 | 形式如 '600000.SH' |
| `deviation` | `number` | K 线偏移 | 0：不偏移，N：向右偏移N，-N：向左偏移N |
| `ContextInfo` | `pythonObj` | Python 对象 | ython 对象，这里必须是 ContextInfo |

**返回：** number

\\*\\* 示例：\*\*

```py
#coding:gbk
def init(ContextInfo):
	print(ext_data('CR', '600000.SH', 0, ContextInfo))
```

## ext_data_rank - 获取引用的扩展数据的数值在所有品种中的排名

获取引用的扩展数据的数值在所有品种中的排名

**调用方法：**`ext_data_rank(extdataname, stockcode, deviation, ContextInfo)`

**参数：**

| 参数名 | 类型 | 说明 | 提示 |
| --- | --- | --- | --- |
| `extdataname` | `string` | 扩展数据名 |  |
| `stockcode` | `string` | 证券代码 | 形式如 '600000.SH' |
| `deviation` | `number` | K 线偏移 | 0：不偏移，N：向右偏移N，-N：向左偏移N |
| `ContextInfo` | `pythonObj` | Python 对象 | ython 对象，这里必须是 ContextInfo |

**返回：** number

\\*\\* 示例：\*\*

```py
#coding:gbk
def init(ContextInfo):
	print(ext_data_rank('mycci', '600000.SH', 0, ContextInfo))
```

## ext_data_rank_range - 获取引用的扩展数据的数值在指定时间区间内所有品种中的排名

获取引用的扩展数据的数值在指定时间区间内所有品种中的排名

\\*\\* 调用方法： \*\*`ext_data_rank_range(extdataname, stockcode, begintime, endtime, ContextInfo)`

**参数：**

| 参数名 | 类型 | 说明 | 提示 |
| --- | --- | --- | --- |
| `extdataname` | `string` | 扩展数据名 |  |
| `stockcode` | `string` | 证券代码 | 形式如 '600000.SH' |
| `begintime` | `string` | 区间的起始时间 | 格式为 '2016-08-02 12:12:30'（包括该时间点在内） |
| `endtime` | `string` | 区间的结束时间 | 格式为 '2017-08-02 12:12:30' （包括该时间点在内） |
| `ContextInfo` | `pythonObj` | Python对象 | Python 对象，这里必须是 ContextInfo |

**返回：** pythonDict

\\*\\* 示例：\*\*

```py
#coding:gbk
def init(ContextInfo):
	print(ext_data_rank_range('mycci', '600000.SH','2022-08-02 12:12:30', '2023-08-02 12:12:30', ContextInfo))
```

## ext_data_range - 获取扩展数据在指定时间区间内的值

获取扩展数据在指定时间区间内的值

**调用方法：**`ext_data_range(extdataname, stockcode, begintime, endtime, ContextInfo)`

**参数：**

| 参数名 | 类型 | 说明 | 提示 |
| --- | --- | --- | --- |
| `extdataname` | `string` | 扩展数据名 |  |
| `stockcode` | `string` | 证券代码 | 形式如 '600000.SH' |
| `begintime` | `string` | 区间的起始时间 | 格式为 '2016-08-02 12:12:30'（包括该时间点在内） |
| `endtime` | `string` | 区间的结束时间 | 格式为 '2017-08-02 12:12:30' （包括该时间点在内） |
| `ContextInfo` | `pythonObj` | Python对象 | Python 对象，这里必须是 ContextInfo |

**返回：** pythonDict

**示例：**

```py
#coding:gbk
def init(ContextInfo):
	print(ext_data_range('mycci', '600000.SH','2022-08-02 12:12:30', '2023-08-02 12:12:30', ContextInfo))
```

## get_factor_value - 获取因子数据

获取因子数据

**调用方法：**`get_factor_value(factorname, stockcode, deviation, ContextInfo)`

**参数：**

| 参数名 | 类型 | 说明 | 提示 |
| --- | --- | --- | --- |
| `factorname` | `string` | 因子名称 |  |
| `stockcode` | `string` | 证券代码 | 形式如 '600000.SH' |
| `deviation` | `number` | K 线偏移 | 0 不偏移，N 向右偏移 N，-N 向左偏移 N |
| `ContextInfo` | `pythonObj` | Python对象 | Python 对象，这里必须是 ContextInfo |

**返回：** number

**示例：**

```py
#coding:gbk
def init(ContextInfo):
	print(get_factor_value('zzz', '600000.SH', 0, ContextInfo))
```

## get_factor_rank - 获取引用的因子数据的数值在所有品种中排名

获取引用的因子数据的数值在所有品种中排名

**调用方法：**`get_factor_rank(factorname, stockcode, deviation, ContextInfo)`

**参数：**

| 参数名 | 类型 | 说明 | 提示 |
| --- | --- | --- | --- |
| `factorname` | `string` | 因子名称 |  |
| `stockcode` | `string` | 证券代码 | 形式如 '600000.SH' |
| `deviation` | `number` | K 线偏移 | 0 不偏移，N 向右偏移 N，-N 向左偏移 N |
| `ContextInfo` | `pythonObj` | Python对象 | Python 对象，这里必须是 ContextInfo |

**示例：**

```py
#coding:gbk
def init(ContextInfo):
	print(get_factor_rank('zzz', '600000.SH', 0, ContextInfo))
```

## （不推荐）call_vba - 获取引用的 VBA 模型运行的结果

更推荐函数：

- 获取历史数据 [call_formula](data_function.md?id=e2M5nZ#call-formula-%E8%B0%83%E7%94%A8%E6%A8%A1%E5%9E%8B)
- 订阅实时数据 [subscribe_formula](data_function.html?id=e2M5nZ#subscribe-formula-%E8%AE%A2%E9%98%85%E6%A8%A1%E5%9E%8B) 更多实时和历史数据调用的示例: [Python调用VBA因子公式的案例](https://dict.thinktrader.net/codeExample/python%E8%B0%83%E7%94%A8VBA.md?id=e2M5nZ)

获取引用的 VBA 模型运行的结果

提示

注意

1. 使用该函数时需补充好本地 K 线或分笔数据

**调用方法：**`call_vba(factorname, stockcode,[period, dividend_type, barpos],ContextInfo)`

**参数：**

| 参数名 | 类型 | 说明 | 提示 |
| --- | --- | --- | --- |
| `factorname` | `string` | 因子名称 |  |
| `stockcode` | `string` | 证券代码 | 形式如 '600000.SH' |
| `period` | `string` | K 线偏移 | 可缺省，默认为当前主图周期线型 |
| `dividend_type` | `string` | 复权方式 | 可缺省，默认当前图复权方式，具体可选值如下 |
| `barpos` | `number` | 对应 bar 下标 | 可缺省，默认当前主图调用到的 bar 的对应下标xtInfo |
| `ContextInfo` | `pythonObj` | Python 对象 | Python 对象，这里必须是 ContextInfo |

- period 可选值：


> 'tick'：分笔线 '1d'：日线 '1m'：1分钟线 '3m'：3分钟线 '5m'：5分钟线 '15m'：15分钟线 '30m'：30分钟线 '1h'：小时线 '1w'：周线 '1mon'：月线 '1q'：季线 '1hy'：半年线 '1y'：年线

- dividend_type 可选值：


> 'none'：不复权 'front'：向前复权 'back'：向后复权 'front_ratio'：等比向前复权 'back_ratio'：等比向后复权


**返回：** number

**示例：**

```py
#coding:gbk
def init(ContextInfo):
	print(call_vba('MA.ma1', '600036.SH', ContextInfo))
```

返回值示例

```
-1.0
```