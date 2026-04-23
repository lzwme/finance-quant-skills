---
url: "https://dict.thinktrader.net/innerApi/system_function.html"
title: "系统函数 | 迅投知识库"
---

### ContextInfo 对象

ContextInfo 是策略运行环境对象，是 init, after\_init, handlebar 等基本方法的入参，里面包括了终端自带的属性和方法。一般情况下不建议对ContextInfo添加自定义属性，ContextInfo会随着bar的切换而重置到上一根bar的结束状态，建议用自建的全局变量来存储。 [详细说明请看这里](question_answer.md?id=null#%E7%B3%BB%E7%BB%9F%E5%AF%B9%E8%B1%A1-contextinfo-%E9%80%90-k-%E7%BA%BF%E4%BF%9D%E5%AD%98%E7%9A%84%E6%9C%BA%E5%88%B6)

### init - 初始化函数

初始化函数，只在整个策略开始时调用运行到一次。用于初始订阅行情，订阅账号信息使用。init函数执行完成前部分接口无法使用，如交易日获取函数get\_trading\_dates。

**系统函数 不可被手动调用**

**参数：**

| 名称 | 类型 | 描述 |
| --- | --- | --- |
| `ContextInfo` | `object` | 策略运行环境对象，可以用于存储自定义的全局变量 |

**返回：** 无

**示例：**

python

```
def init(ContextInfo):
    ContextInfo.initProfit = 0
```

**在init函数中订阅行情示例：**

python

 ```py
#coding:gbk

def init(C):
	#init函数入参为ContextInfo对象 定义时可以选择更简短的形参名 如C
	#在init函数中 可以进行 订阅行情的操作
    #如需在行情回调函数中下单 下单函数需要传入ContextInfo对象 可以通过在init中定义回调函数 来使用外层的ContextInfo
	def my_callback_function(data):
		#自定义行情回调函数 入参为指数据字典
		print(data)
	stock = '600000.SH'
	C.subscribe_quote(stock, period = '5m', callback = my_callback_function)
	#init函数执行完成后
	print('init函数执行完成')
```

### after\_init - 初始化后函数

后初始化函数，在初始化函数执行完成后被调用一次。可以用于放置一次性触发的下单，取数据操作代码。

系统会在`init`函数执行完后和执行`handlebar`之前调用`after_init`, 有些`init`里不支持的函数比如 [ContextInfo.get\_trading\_dates](https://dict.thinktrader.net/pages/fd9cbd/#_23-%E8%8E%B7%E5%8F%96%E6%8C%87%E5%AE%9A%E4%B8%AA%E8%82%A1-%E5%90%88%E7%BA%A6-%E6%8C%87%E6%95%B0%E7%9A%84-k-%E7%BA%BF-%E4%BA%A4%E6%98%93%E6%97%A5-%E5%88%97%E8%A1%A8-contextinfo-get-trading-dates) 可以在`after_init`里调用。

**系统函数 不可被手动调用**

**参数：**

| 名称 | 类型 | 描述 |
| --- | --- | --- |
| `ContextInfo` | `object` | 策略运行环境对象，可以用于存储自定义的全局变量 |

**返回：** 无

**示例：**

python

 ```py
#coding:gbk
def init(ContextInfo):
    print('init')

def after_init(ContextInfo):
    print('系统会在init函数执行完后和执行handlebar之前调用after_init')

def handlebar(ContextInfo):
    if ContextInfo.is_last_bar():
        print('handlebar')
```

**after\_init函数中立刻下单示例：**

python

 ```py
#coding:gbk

def after_init(C):
	#after_init 函数 可以用于执行运行开始时 需要执行一次的代码 例如下一笔委托
	#account变量是模型交易界面 添加策略时选择的资金账号 不需要手动填写 交易模型需要在模型交易界面运行 才有效
	#快速交易参数(quickTrade )填2 passorder函数执行后立刻下单 不会等待k线走完再委托。 可以在after_init函数 run_time函数注册的回调函数里进行委托
	msg = f"投资备注字符串 用来区分不同委托"
	passorder(23, 1101, account, '600000.SH', 5, -1, 100, '测试下单', 2, msg, C)
```

### handlebar - 行情事件函数

**系统函数 不可被手动调用**

**释义：** 行情事件函数，每根 K 线运行一次；实时行情获取状态下，先每根历史 K 线运行一次，再在每个 tick 数据来后驱动运行一次

历史k线上，按时间顺序每根K线触发一次调用；盘中，每个新到达的TICK数据驱动运行一次。可以作为行情驱动的函数，实现指标计算，回测，实盘下单的效果。

**参数：**

| 名称 | 类型 | 描述 |
| --- | --- | --- |
| `ContextInfo` | `object` | 策略运行环境对象，可以用于存储自定义的全局变量 |

**返回：** 无

**示例：**

```
def handlebar(ContextInfo):
    # 输出当前运行到的 K 线的位置
    print(ContextInfo.barpos)
```

### ContextInfo.schedule\_run - 设置定时器

说明

1. 该函数是新版设置定时器函数，相比旧版`run_time`，新版`schedule_run`新增了`任务分组`,`任务取消`等多种功能

**原型:**

python

```
ContextInfo.schedule_run(
    func:Callable, # 回调函数，到达定时器预定时间时触发调用，参数为ContextInfo类型，无需返回值
    time_point:Union[dt.datetime,str], # 表示预定的第一次触发时间，如果设置定时器时已经过了预定时间，会立即执行func以及后续逻辑；当使用str类型时，格式为'yyyymmddHHMMSS'如'20231231235959'，需要满足转换dt.datetime.strptime('20231231235959','%Y%m%d%H%M%S')
    repeat_times:int=0, # 表示在预定时间触发后按interval间隔再触发多少次
    interval:datetime.timedelta=None, # 表示预定时间触发后的后续重复执行的时间间隔
    name:str='' # 定时器任务组名，可用于定时器分组，多次设置同名定时任务不会互相覆盖，会计入同一个任务组，按任务组名取消时会全部取消
    )
```

**参数：**

| 名称 | 类型 | 描述 |
| --- | --- | --- |
| `func` | `Callable` | 回调函数，到达定时器预定时间时触发调用，参数为ContextInfo类型，无需返回值，定义示例如下：<br> def on\_timer(C:ContextInfo): pass |
| `time_point` | `Union[datetime.datetime,str]` | 表示预定的第一次触发时间，如果设置定时器时已经过了预定时间，会立即执行func以及后续逻辑；<br> 当使用str类型时，格式为'yyyymmddHHMMSS'如'20231231235959'，需要满足转换datetime.datetime.strptime('20231231235959','%Y%m%d%H%M%S') |
| `repeat_times` | `int` | 表示在预定时间触发后按interval间隔再触发多少次，传`-1`表示不限制次数 |
| `interval` | `datetime.timedelta` | 表示预定时间触发后的后续重复执行的时间间隔 |
| `name` | `str` | 定时器任务组名，可用于定时器分组，多次设置同名定时任务不会互相覆盖，会计入同一个任务组，按任务组名取消时会全部取消 |

**回调函数参数：** ContextInfo：策略模型全局对象

**返回值：**

`int`类型，表示本次调用后生成的定时任务号，可用于取消本次定时任务，全局唯一不重复

**示例：**

python

```
import datetime as dt
def on_timer(C:ContextInfo):
    print('hello world')
def init(ContextInfo):
    tid=ContextInfo.schedule_run(on_timer,'20231231235959',-1,dt.timedelta(minutes=1),'my_timer')
def handlebar(ContextInfo):
    pass
#此例为自2023-12-31 23:59:59后每60s运行一次on_timer
```

### ContextInfo.cancel\_schedule\_run - 取消由schedule\_run产生的定时任务

**原型：**

python

```
ContextInfo.cancel_schedule_run(
    key:Union[seq:int,name:str] # 定时任务号或定时任务组名称
    )
```

**参数：**

| 名称 | 类型 | 描述 |
| --- | --- | --- |
| `key:` | `Union[seq:int,name:str]` | 类型为int时，表示按任务号取消;类型为str时，表示按任务组取消，会取消组内所有定时任务 |

**返回值：**

`bool`类型，表示是否取消成功，即是否能按key找到目标定时任务

**示例：**

示例

```

ContextInfo.cancel_schedule_run('my_timer') #取消my_timer任务组所有定时任务
ContextInfo.cancel_schedule_run(1) #取消任务号为1的定时任务
```

### ContextInfo.run\_time - 设置定时器

设置定时器函数，可以指定时间间隔，定时触发用户定义的回调函数。适用与在盘中，持续判断交易信号的模型。

**用法：**`ContextInfo.run_time(funcName,period,startTime)` 定时触发指定的 funcName函数, funcName函数由用户定义, 入参为ContextInfo对象。

**参数：**

- funcName：回调函数名
- period：重复调用的时间间隔,'5nSecond'表示每5秒运行1次回调函数,'5nDay'表示每5天运行一次回调函数,'500nMilliSecond'表示每500毫秒运行1次回调函数
- startTime：表示定时器第一次启动的时间,如果要定时器立刻启动,可以设置历史的时间

**回调函数参数：** ContextInfo：策略模型全局对象

**示例：**

python

```
import time
def init(ContextInfo):
    ContextInfo.run_time("f","5nSecond","2019-10-14 13:20:00")
def f(ContextInfo):
    print('hello world')

#此例为自2019-10-14 13:20:00后每5s运行一次函数f
```

注意

1. 模型回测时无效
2. 定时器没有结束方法，会随着策略的结束而结束。
3. period有nMilliSecond、nSecond和Day三个周期单元，部分周期下定时器函数在第一次运行之前会先等待一个period

### stop - 停止处理函数

**系统函数 不可被手动调用**

**释义：** PY策略模型关闭停止前运行到的函数，复杂策略模型，如中间有起线程可通过在该函数内实现停止线程操作。注意, 当前版本stop函数被调用时交易连接已断开, 不能在stop函数中做报单 / 撤单操作.

**参数：**

| 名称 | 类型 | 描述 |
| --- | --- | --- |
| `ContextInfo` | `object` | 策略运行环境对象，可以用于存储自定义的全局变量 |

**示例：**

python

```
def stop(ContextInfo):
    print( 'strategy is stop !')
```

### ContextInfo.is\_last\_bar - 是否为最后一根K线

**用法：** ContextInfo.is\_last\_bar()

**释义：** 判定是否为最后一根 K 线

**参数：** 无

**返回：** bool，返回值含义：True 是右侧最新k线 False不是最新k线

> True：是
>
> False：否

**示例：**

pythonresult

```
def handlebar(ContextInfo):
    print(ContextInfo.is_last_bar())
```

```
False
False
...
False
True
```

### ContextInfo.is\_new\_bar - 判定是否为新的 K 线

**用法：** ContextInfo.is\_new\_bar()

**释义：** 某根 K 线的第一个 tick 数据到来时，判定该 K 线为新的 K 线，其后的tick不会认为是新的 K 线

**参数：** 无

**返回：** bool，返回值含义：

> True：是
>
> False：否

**示例：**

pythonresult

```
def handlebar(ContextInfo):
    print(ContextInfo.is_new_bar()) #历史k线每根都是新k线 盘中 每根新k线第一个分笔返回True 其他分笔返回False
```

```
True
True
...
True
False
```

### ContextInfo.get\_stock\_name - 根据代码获取名称

注意

我们计划后续版本抛弃这个函数，不建议继续使用，可以用ContextInfo.get\_instrument\_detail("stockcode")\["InstrumentName"\]来实现同样功能

**用法：** ContextInfo.get\_stock\_name('stockcode')

**释义：** 根据代码获取名称

**参数：** stockcode：股票代码，如'000001.SZ'，缺省值 ' ' 默认为当前图代码

**返回：** string（GBK编码）

**示例：**

示例返回值

```
def handlebar(ContextInfo):
    print(ContextInfo.get_stock_name('000001.SZ'))
```

```
平安银行
```

### ContextInfo.get\_open\_date - 根据代码返回对应股票的上市时间

**用法：** ContextInfo.get\_open\_date('stockcode')

**释义：** 根据代码返回对应股票的上市时间

**参数：** stockcode：股票代码，如'000001.SZ'，缺省值 ' ' 默认为当前图代码

**返回：** number

**示例：**

pythonresult

```
def init(ContextInfo):
    print(ContextInfo.get_open_date('000001.SZ'))
```

```
19910403
```

### ContextInfo.set\_output\_index\_property - 设定指标绘制的属性

**用法：** ContextInfo.set\_output\_index\_property(index\_name,draw\_style=0,color='white',noaxis=False,nodraw=False,noshow=False)

**释义：** 设定指标绘制的属性，会最终覆盖掉指标对应的属性字段

**参数：**

- index\_name:string,指标名称，不可缺省
- draw\_style,同paint函数的drawstyle，可缺省默认为0
- color,同paint函数的color，可缺省默认为'white'
- noaxis:bool,是否无坐标，可缺省默认为False
- nodraw:bool,是否不画线，可缺省默认为False
- noshow:bool,是否不展示，可缺省默认为False

**返回：** 无

**示例：**

pythonpythonresult

```
def init(ContextInfo):
    ContextInfo.set_output_index_property('单位净值', nodraw = True)#使回测指标'单位净值'不画线
```

### create\_sector - 创建板块

**用法：** create\_sector(parent\_node,sector\_name,overwrite)

**释义：** 创建板块

**参数：**

- parent\_node：str，父节点，''为'我的'（默认目录）
- sector\_name：str，要创建的板块名
- overwrite：bool，是否覆盖。如果目标节点已存在，为True时跳过，为False时在sector\_name后增加数字编号，编号为从1开始自增的第一个不重复的值。

**返回：** sector\_name2：实际创建的板块名

**示例：**

```
sector=create_sector('我的','新建板块',False)
```

```
新建板块
```

### create\_sector\_folder - 创建板块目录节点

**用法：** create\_sector\_folder(parent\_node,folder\_name,overwrite)

**释义：** 创建板块目录节点

**参数：**

- parent\_node：str，父节点，''为'我的'（默认目录）
- sector\_name：str，要创建的节点名
- overwrite：bool，是否覆盖。如果目标节点已存在，为True时跳过，为False时在folder\_name后增加数字编号，编号为从1开始自增的第一个不重复的值。

**返回：** sector\_name2：实际创建的节点名

**示例：**

pythonresult

```
folder=create_sector_folder('我的','新建分类',False)
```

```
新建分类
```

### get\_sector\_list - 获取板块目录信息

**用法：** get\_sector\_list(node)

**释义：** 获取板块目录信息

**参数：**

- node：str，板块节点名，''为顶层目录

**返回：** info\_list：\[\[s1,s2,...\],\[f1,f2,...\]\]s为板块名，f为目录节点名，例如\[\['我的自选'\],\['新建分类1'\]\]

**示例：**

pythonresult

```
get_sector_list('我的')
```

```
[['我的自选', '龙头', '卖出篮子', 'TMP', '震荡', '待分析'], []]
```

### reset\_sector\_stock\_list - 设置板块成分股

**用法：** reset\_sector\_stock\_list(sector,stock\_list)

**释义：** 设置板块成分股

**参数：**

- sector：板块名
- stock\_list：list，品种代码列表，例如\['000001.SZ','600000.SH'\]

**返回：** result：bool，操作成功为True，失败为False

**示例：**

pythonresult

```
reset_sector_stock_list('我的自选',['000001.SZ','600000.SH'])
```

```
True / False
```

### remove\_stock\_from\_sector - 移除板块成分股

**用法：** remove\_stock\_from\_sector(sector,stock\_code)

**释义：** 移除板块成分股

**参数：**

- sector：板块名
- stock\_code：品种代码，例如'000001.SZ'

**返回：** result：bool，操作成功为True，失败为False

**示例：**

pythonresult

```
remove_stock_from_sector('我的自选','000001.SZ')
```

```
True / False
```

### add\_stock\_to\_sector - 添加板块成分股

**用法：** add\_stock\_to\_sector(sector,stock\_code)

**释义：** 添加板块成分股

**参数：**

- sector：板块名
- stock\_code：品种代码，例如'000001.SZ'

**返回：** result：bool，操作成功为True，失败为False

**示例：**

pythonresult

```
add_stock_to_sector('我的自选','000001.SZ')
```

```
True / False
```