---
name: pywencai
description: 同花顺问财数据查询：使用中文自然语言查询A股、指数、基金、港美股、可转债等市场数据；当用户需要通过自然语言从问财获取选股、财务、资金流、技术指标等数据时使用。
metadata: {"clawdbot":{"emoji":"📈","requires":{"bins":["python","node"]}}, "repo": "https://github.com/zsrl/pywencai"}
---

# PyWenCai（同花顺问财数据查询）

通过Python使用中文自然语言从[同花顺问财](https://www.iwencai.com)查询A股及其他市场数据。

> ⚠️ **需要Cookie**：必须提供问财网站的有效Cookie。获取方法见下文。

## 环境要求

- **Python 3.7+**
- **Node.js v16+**（pywencai 内部执行 JS 代码）
- **pip** package manager

## 安装

```bash
pip install pywencai --upgrade
```

## 如何获取Cookie

若存在环境变量 `WENCAI_COOKIE`，可直接使用；若调用失败，则按如下步骤重新获取：

1. 在浏览器中打开 https://www.iwencai.com 并登录。
2. 按F12打开开发者工具 → 切换到Network标签。
3. 在问财页面执行任意查询。
4. 找到发往`iwencai.com`的请求，从请求头中复制`Cookie`值。
5. 将该字符串作为`cookie`参数使用。

## Cookie管理

优先使用环境变量或文件管理Cookie，避免硬编码：

```python
import os
import pywencai

# 方法1：从环境变量读取Cookie（推荐）
cookie = os.environ.get('WENCAI_COOKIE', '')

# 方法2：从文件读取Cookie
def load_cookie(path='~/.wencai_cookie'):
    path = os.path.expanduser(path)
    if os.path.exists(path):
        with open(path) as f:
            return f.read().strip()
    return ''

# 方法3：封装查询函数，统一管理Cookie和错误处理
def query(q, **kwargs):
    cookie = load_cookie()
    try:
        return pywencai.get(
            query=q, cookie=cookie,
            no_detail=True, retry=3, sleep=1,
            **kwargs
        )
    except Exception as e:
        print(f"查询失败: {e}")
        return None

# 使用
df = query('今日涨停的股票')
```

## 基本用法

```python
import pywencai

# 查询今日涨幅前10的股票，需要有效cookie
res = pywencai.get(query='今日涨幅前10', cookie='your_cookie_here')
print(res)
```

## API参考：`pywencai.get(**kwargs)`

### 必选参数

- **query** — 中文自然语言查询字符串，如 `'今日涨停股票'`、`'市盈率小于20的股票'`
- **cookie** — 从问财网站获取的Cookie字符串（必需）

### 可选参数

- **sort_key** — 排序字段名，如 `'退市@退市日期'`
- **sort_order** — 排序方向：`'asc'`（升序）或 `'desc'`（降序）
- **page** — 页码（默认：`1`）
- **perpage** — 每页结果数（默认和最大：`100`）
- **loop** — 设为`True`获取所有页；或设为整数`n`获取前n页
- **query_type** — 查询类别（默认：`'stock'`），可选值：

| 值 | 说明 |
|---|---|
| `stock` | A股股票 |
| `zhishu` | 指数 |
| `fund` | 基金 |
| `hkstock` | 港股 |
| `usstock` | 美股 |
| `threeboard` | 新三板 |
| `conbond` | 可转债 |
| `insurance` | 保险 |
| `futures` | 期货 |
| `lccp` | 理财产品 |

- **retry** — 失败重试次数（默认：`10`）
- **sleep** — 分页请求间延迟秒数（默认：`0`）
- **log** — 设为`True`在控制台打印日志
- **pro** — 设为`True`使用付费版（需要对应的cookie）
- **no_detail** — 设为`True`始终返回`DataFrame`或`None`（不返回dict）
- **find** — 优先返回的股票代码列表，如 `['600519', '000010']`
- **request_params** — 传递给`requests`的额外参数，如 `{'proxies': proxies}`

### 返回值

- **列表类查询** → 返回 `pandas.DataFrame`
- **详情类查询** → 返回 `dict`（可能包含文本和DataFrame）

## 使用示例

### 按市场类型查询

```python
import pywencai

# A股股票（默认）
res = pywencai.get(query='今日涨停的股票', cookie=cookie)

# 指数数据
res = pywencai.get(query='上证指数近5日涨跌幅', query_type='zhishu', cookie=cookie)

# 基金数据
res = pywencai.get(query='近一年收益率最高的前20只基金', query_type='fund', cookie=cookie)

# 可转债数据
res = pywencai.get(query='可转债溢价率小于10%', query_type='conbond', cookie=cookie)

# 港股数据
res = pywencai.get(query='港股市值最大的前20只股票', query_type='hkstock', cookie=cookie)
```

### 基本面选股

```python
# 估值筛选
res = pywencai.get(query='市盈率小于20的股票', cookie=cookie)
res = pywencai.get(query='市盈率小于10且市净率小于1的股票', cookie=cookie)

# 财务指标
res = pywencai.get(query='ROE大于15%且营收同比增长率大于20%的股票', cookie=cookie)

# 多条件综合筛选
res = pywencai.get(query='市盈率小于20且营收同比增长大于30%且机构持仓比例大于10%的股票', cookie=cookie)
res = pywencai.get(query='今日站上20日均线且市盈率小于30且ROE大于10%的股票', cookie=cookie)
```

### 技术面与资金流

```python
# 技术信号
res = pywencai.get(query='今日MACD金叉的股票', cookie=cookie)
res = pywencai.get(query='KDJ的J值小于0的股票', cookie=cookie)
res = pywencai.get(query='今日成交量是5日均量2倍以上且涨幅大于5%的股票', cookie=cookie)

# 资金流向
res = pywencai.get(query='今日主力资金净流入前20的股票', cookie=cookie)
res = pywencai.get(query='北向资金持股比例最高的前20只股票', cookie=cookie)
```

### 排序、分页与代理

```python
# 按指定字段排序
res = pywencai.get(
    query='退市股票',
    sort_key='退市@退市日期',
    sort_order='asc',
    cookie=cookie
)

# 自动分页获取全部数据（使用代理）
proxies = {'http': 'http://proxy:8080', 'https': 'http://proxy:8080'}
res = pywencai.get(
    query='昨日涨幅',
    loop=True,
    log=True,
    cookie=cookie,
    request_params={'proxies': proxies}
)
```

### 历史数据查询

```python
# 指定日期
res = pywencai.get(query='2024年1月2日涨幅前10的股票', cookie=cookie)

# 日期范围
res = pywencai.get(query='2024年上半年涨幅最大的前20只股票', cookie=cookie)
```

### 完整示例：多策略自动化选股并导出

```python
import pywencai
import pandas as pd
import time

cookie = os.environ.get('WENCAI_COOKIE', '')

# 定义多个筛选策略
strategies = {
    "低估值高分红": "市盈率小于15且股息率大于3%的股票",
    "高成长": "营收同比增长大于30%且净利润同比增长大于30%的股票",
    "技术突破": "今日放量突破20日均线且涨幅大于3%的股票",
    "机构关注": "近一个月机构调研次数大于3次的股票",
    "北向资金": "北向资金今日净买入前20的股票",
}

results = {}
for name, query in strategies.items():
    try:
        res = pywencai.get(query=query, cookie=cookie, no_detail=True)
        if res is not None and not res.empty:
            results[name] = res
            print(f"策略 [{name}] 选出 {len(res)} 只股票")
        else:
            print(f"策略 [{name}] 无结果")
    except Exception as e:
        print(f"策略 [{name}] 查询失败: {e}")
    time.sleep(2)  # 每次查询间隔2秒，避免被封禁

# 保存结果到Excel（每个策略一个工作表）
if results:
    with pd.ExcelWriter("选股结果.xlsx") as writer:
        for name, df in results.items():
            df.to_excel(writer, sheet_name=name, index=False)
    print("筛选结果已保存到 选股结果.xlsx")
```

## 使用技巧

- **适度使用** — 高频调用可能被问财服务器封禁，建议每次查询间隔 ≥ 2秒。
- 始终使用**最新版本**：`pip install pywencai --upgrade`
- 查询字符串使用**中文自然语言** — 像在问财网站搜索一样编写查询。
- 当`loop=True`且设置了`find`时，`loop`被忽略，仅返回前100条结果。
- 使用付费数据时，设置`pro=True`并提供有效`cookie`。

## 常见错误处理

| 错误 | 原因 | 解决方法 |
|------|------|----------|
| `Cookie expired` | Cookie过期 | 重新登录问财网站获取新Cookie |
| 返回`None` | 查询无结果或被限流 | 检查查询语句，降低调用频率 |
| `Node.js not found` | 未安装Node.js | 安装Node.js v16+ |
| `JSONDecodeError` | 服务端返回异常 | 增加`retry`参数，稍后重试 |
| 返回dict而非DataFrame | 查询为详情类 | 设置`no_detail=True`强制返回DataFrame |

## 规则

- 使用此 Skill 前，确认用户需要的是**问财自然语言数据查询**，而非纯行情 API（如 baostock）或回测框架（如 backtrader/rqalpha）。
- 示例中的 `cookie` 参数应统一使用环境变量 `WENCAI_COOKIE` 或 Cookie 文件管理方式，**不要硬编码 Cookie 字符串**。
- 始终设置 `no_detail=True` 以确保返回 `DataFrame`（除非用户明确需要详情 dict）。
- 批量查询时必须设置 `sleep` 参数（建议 ≥ 2秒），避免被服务器封禁。
- 查询字符串应使用中文自然语言，与问财网站搜索框的输入方式一致。
