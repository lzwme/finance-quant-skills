---
url: "https://dict.thinktrader.net/innerApi/drawing_function.html"
title: "绘图函数 | 迅投知识库"
---

## ContextInfo.paint - 在界面上画图

在界面上画图

**调用方法：** ContextInfo.paint(name, value, index, line_style, color = 'white', limit = '')

**参数：**

| 参数名 | 类型 | 说明 | 提示 |
| --- | --- | --- | --- |
| `name` | `string` | 需显示的指标名 |  |
| `value` | `number` | 需显示的数值 |  |
| `index` | `number` | 显示索引位置 | 填 -1 表示按主图索引显示 |
| `line_style` | `number` | 线型 | 0：曲线<br>42：柱状线 |
| `color` | `string` | 颜色（不填默认为白色） | blue：蓝色<br>brown：棕<br>cyan：蓝绿<br>green：绿<br>magenta：品红<br>red：红<br>white：白<br>yellow：黄 |
| `limit` | `string` | 画线控制 | 'noaxis'：不影响坐标画线<br>'nodraw'：不画线 |

\*\*返回：\*\*无

**示例：**

```py
def init(ContextInfo):
    realtimetag = ContextInfo.get_bar_timetag(ContextInfo.barpos)
    value = ContextInfo.get_close_price('', '', realtimetag)
    ContextInfo.paint('close', value, -1, 0, 'white','noaxis')
```

## ContextInfo.draw_text - 在图形上显示文字

在图形上显示数字   **调用方法：**`ContextInfo.draw_text(condition, position, text)`

**参数：**

| 参数名 | 类型 | 说明 | 提示 |
| --- | --- | --- | --- |
| `condition` | `bool` | 条件 |  |
| `Position` | `number` | 文字显示的位置 |  |
| `text` | `string` | 文字 |  |

\*\*返回值：\*\*无

**示例：**

```
def init(ContextInfo):
    ContextInfo.draw_text(1, 10, '文字')
```

## ContextInfo.draw_number - 在图形上显示数字

在图形上显示数字

**调用方法：**`ContextInfo.draw_number(cond, height, number, precision)`

**参数：**

| 参数名 | 类型 | 说明 | 提示 |
| --- | --- | --- | --- |
| `cond` | `bool` | 条件 |  |
| `height` | `number` | 显示文字的高度位置 |  |
| `text` | `string` | 显示的数字 |  |
| `precision` | `number` | 为小数显示位数 | 取值范围 0 - 7 |

\*\*返回值：\*\*无

**示例：**

```
def init(ContextInfo):
    close = ContextInfo.get_market_data(['close'])
    ContextInfo.draw_number(1 > 0, close, 66, 1)
```

## ContextInfo.draw_vertline - 在数字 1 和数字 2 之间绘垂直线

在数字1和数字2之间绘垂直线

**调用方法：**`ContextInfo.draw_vertline(cond, number1, number2, color = '', limit = '')`

**参数：**

| 参数名 | 类型 | 说明 | 提示 |
| --- | --- | --- | --- |
| `cond` | `bool` | 条件 |  |
| `number1` | `number` | 数字1 |  |
| `number2` | `number` | 数字2 |  |
| `color` | `string` | 颜色（不填默认为白色） | blue：蓝色<br>brown：棕<br>cyan：蓝绿<br>green：绿<br>magenta：品红<br>red：红<br>white：白<br>yellow：黄 |
| `limit` | `string` | 画线控制 | 'noaxis'：不影响坐标画线<br>'nodraw'：不画线 |

**返回：** 无

**示例：**

```
def init(ContextInfo):
    close = ContextInfo.get_market_data(['close'])
    open = ContextInfo.get_market_data(['open'])
    ContextInfo.draw_vertline(1 > 0, close, open, 'cyan')
```

## ContextInfo.draw_icon - 在图形上绘制小图标

在图形上绘制小图标

**调用方法：**`ContextInfo.draw_icon(cond, height, type)`

**参数：**

| 参数名 | 类型 | 说明 | 提示 |
| --- | --- | --- | --- |
| `cond` | `bool` | 条件 |  |
| `height` | `number` | 图标的位置 |  |
| `text` | `number` | 图标的类型 | 1：椭圆<br>0：矩形 |

\*\*返回值：\*\*无

**示例：**

```
def init(ContextInfo):
    close = ContextInfo.get_market_data(['close'])
    ContextInfo.draw_icon(1 > 0, close, 0)
```