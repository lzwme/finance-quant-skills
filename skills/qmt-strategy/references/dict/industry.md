---
url: "https://dict.thinktrader.net/dictionary/industry.html"
title: "行业概念数据 | 迅投知识库"
---

## 获取行业概念数据

提示

获取行业/板块信息前，需要先通过`download_sector_data`下载板块分类信息，或者在界面端下载中心手动选择`全部板块`

提供行业板块信息，概念板块信息，包含行业代码、名称等。

### 下载板块分类信息

**调用方法**

```py
from xtquant import xtdata
xtdata.download_sector_data()
```

**参数**

- 无

**返回值**

- 无

**示例**

示例

```py
from xtquant import xtdata
xtdata.download_sector_data()
```

### 下载历史板块分类信息

**调用方法**

```py
from xtquant import xtdata
xtdata.download_history_contracts()
```

**参数**

- 无

**返回值**

- 无

**示例**

示例

```py
from xtquant import xtdatacenter as xtdc

xtdc.set_token("这里输入token")

xtdc.init()

from xtquant import xtdata

xtdata.download_history_contracts()
```

### 获取板块分类信息数据

**调用方法**

```py
from xtquant import xtdata
xtdata.get_sector_list()
```

**参数**

- 无

**返回值**

- `list`：所有板块的列表信息(包含过期板块)，可以配合板块成分股查询接口使用

**示例**

示例与返回值

```py
from xtquant import xtdata
sector_list = xtdata.get_sector_list()
```

```
[ '1000SW1交通运输',
 '1000SW1传媒',
 '1000SW1公用事业',
 '1000SW1农林牧渔',
 '1000SW1医药生物',
 '1000SW1商贸零售',
 '1000SW1国防军工',
 '1000SW1基础化工',
 '1000SW1家用电器',
 '1000SW1建筑材料',
 '1000SW1建筑装饰',
 '1000SW1房地产',
 '1000SW1有色金属',
 '1000SW1机械设备',...]
```

### 获取板块成分股数据

**调用方法**

```py
from xtquant import xtdata
xtdata.get_stock_list_in_sector(sector_name)
```

**参数**

| 参数名称 | 数据类型 | 描述 |
| --- | --- | --- |
| `sector_name` | `string` | 板块名，如'沪深300'，'中证500'、'上证50'、'我的自选'等 |

**返回值**

- `list`：内含成份股代码，代码形式为 'stockcode.market'，如 '000002.SZ'

**示例1:获取当最新板块数据**

示例与返回值

```py
# 获取沪深300的板块成分股
from xtquant import xtdata
sector = xtdata.get_stock_list_in_sector('沪深300')
print(sector)
```

```
['000001.SZ', '000002.SZ', '000063.SZ', '000069.SZ',...]
```

**示例2:获取板块退市股票数据**

示例与返回值

```py
from xtquant import xtdatacenter as xtdc

xtdc.set_token("这里输入token")

xtdc.init()

from xtquant import xtdata

xtdata.download_history_contracts()

print([i for i in xtdata.get_sector_list() if "过期" in i])

print("="*10)

print(xtdata.get_stock_list_in_sector('过期上证A股'))
```

```
['过期上期所', '过期上证A股', '过期上证B股', '过期上证期权', '过期上证转债', '过期中金所', '过期大商所', '过期沪深A股', '过期沪深B股', '过期沪深转债', '过期深证A股', '过期深证B股', '过期深证期权', '过期深证转债', '过期科创板', '过期能源中心', '过期郑商所']
==========
['600001.SH', '600003.SH', '600005.SH', '600068.SH', '600069.SH', '600074.SH', '600077.SH', '600086.SH', '600087.SH', '600090.SH', '600091.SH', '600093.SH', '600102.SH', '600122.SH', '600139.SH', '600145.SH', '600146.SH', '600175.SH', '600209.SH', '600240.SH', '600242.SH', '600247.SH', '600253.SH', '600260.SH', '600263.SH', '600270.SH', '600275.SH', '600291.SH', '600311.SH', '600317.SH', '600357.SH', '600385.SH', '600393.SH', '600401.SH', '600432.SH', '600466.SH', '600485.SH', '600532.SH', '600553.SH', '600555.SH', '600591.SH', '600607.SH', '600614.SH', '600631.SH', '600634.SH', '600652.SH', '600656.SH', '600677.SH', '600680.SH', '600687.SH', '600695.SH', '600701.SH', '600723.SH', '600747.SH', '600767.SH', '600781.SH', '600806.SH', '600832.SH', '600842.SH', '600849.SH', '600856.SH', '600870.SH', '600890.SH', '600891.SH', '600896.SH', '600978.SH', '600991.SH', '601258.SH', '601268.SH', '601299.SH', '601313.SH', '601558.SH', '603157.SH', '603996.SH', '688086.SH', '688555.SH']
```

### 获取概念成分股数据

**调用方法**

```py
from xtquant import xtdata
xtdata.get_stock_list_in_sector(sector_name)
```

**参数**

| 参数名称 | 数据类型 | 描述 |
| --- | --- | --- |
| `sector_name` | `string` | 板块名，如'GN上海'等 |

**返回值**

- `list`：内含成份股代码，代码形式为 'stockcode.market'，如 '000002.SZ'

**示例**

示例与返回值

```py
# 获取GN上海的板块成分股
from xtquant import xtdata
sector = xtdata.get_stock_list_in_sector('GN上海')
print(sector)
```

```
['000863.SZ', '001266.SZ', '002022.SZ', '002269.SZ',...]
```

### 获取迅投行业成分股数据

**调用方法**

```py
from xtquant import xtdata
xtdata.get_stock_list_in_sector(sector_name)
```

**参数**

| 参数名称 | 数据类型 | 描述 |
| --- | --- | --- |
| `sector_name` | `string` | 板块名，如'SW1汽车'等 |

**返回值**

- `list`：内含成份股代码，代码形式为 'stockcode.market'，如 '000002.SZ'

**示例**

示例与返回值

```py
# 获取SW1汽车行业的成分股
from xtquant import xtdata

sector = xtdata.get_stock_list_in_sector('SW1汽车')
print(sector)
```

```
['000030.SZ', '000338.SZ', '000550.SZ',....]
```