## BaoStock API 错误代码说明

本文档列出了 BaoStock API 所有错误代码及其含义，供开发调试时参考。

## 目录
  * [1 错误代码分类](#错误代码分类)
  * [2 常见问题排查](#常见问题排查)
    * [2.1 登录失败](#登录失败)
    * [2.2 网络连接失败](#网络连接失败)
    * [2.3 查询数据异常](#查询数据异常)
    * [2.4 IP黑名单检查](#IP黑名单检查)
  * [3 登录认证错误](#登录认证错误)
  * [4 网络连接错误](#网络连接错误)
  * [5 数据与参数错误](#数据与参数错误)
  * [6 系统错误](#系统错误)
  * [7 客户端错误提示](#客户端错误提示)
  * [8 正确用法示例](#正确用法示例)

---

## 1 错误代码分类

<table class="overview-table">
  <thead>
    <tr>
      <th>错误代码段</th>
      <th>分类</th>
      <th>说明</th>
    </tr>
  </thead>
  <tbody>
    <tr><td>10001xxx</td><td>登录认证错误</td><td>与用户登录、认证、权限相关的错误</td></tr>
    <tr><td>10002xxx</td><td>网络连接错误</td><td>与网络连接、通信相关的错误</td></tr>
    <tr><td>10004xxx</td><td>数据与参数错误</td><td>与输入参数、数据解析相关的错误</td></tr>
    <tr><td>10005xxx</td><td>系统错误</td><td>服务端系统级别错误</td></tr>
  </tbody>
</table>

---

## 2 常见问题排查

### 2.1 登录失败

```python
import baostock as bs

lg = bs.login()
print('login respond error_code:' + lg.error_code)  # 错误代码
print('login respond  error_msg:' + lg.error_msg)   # 错误信息
```

<table class="faq-table">
  <thead>
    <tr>
      <th>现象</th>
      <th>可能原因</th>
      <th>解决方案</th>
    </tr>
  </thead>
  <tbody>
    <tr><td>错误代码 10001002</td><td>用户名或密码错误</td><td>确认账号密码正确</td></tr>
    <tr><td>错误代码 10001004</td><td>客户端版本过期</td><td>执行 <code>pip install baostock --upgrade</code></td></tr>
    <tr><td>错误代码 10001005</td><td>登录数达上限</td><td>等待其他会话过期或先 <code>bs.logout()</code></td></tr>
    <tr><td>错误代码 10001008/09</td><td>用户名或密码为空</td><td>登录时传入用户名和密码参数</td></tr>
    <tr><td>错误代码 10001011</td><td>IP被加入黑名单</td><td>详见下方"2.4 IP黑名单检查"</td></tr>
  </tbody>
</table>

### 2.2 网络连接失败

<table class="faq-table">
  <thead>
    <tr>
      <th>现象</th>
      <th>可能原因</th>
      <th>解决方案</th>
    </tr>
  </thead>
  <tbody>
    <tr><td>错误代码 10002002</td><td>连接失败</td><td>检查网络、防火墙、代理设置</td></tr>
    <tr><td>错误代码 10002003</td><td>连接超时</td><td>检查网络状况，稍后重试</td></tr>
    <tr><td>错误代码 10002004</td><td>连接断开</td><td>重新登录并重试</td></tr>
    <tr><td>错误代码 10002007</td><td>网络接收错误</td><td>重新登录确认登录有没有成功</td></tr>
  </tbody>
</table>

### 2.3 查询数据异常

<table class="faq-table">
  <thead>
    <tr>
      <th>现象</th>
      <th>可能原因</th>
      <th>解决方案</th>
    </tr>
  </thead>
  <tbody>
    <tr><td>错误代码 10004005</td><td>参数为空</td><td>检查必填参数是否已提供</td></tr>
    <tr><td>错误代码 10004006</td><td>参数错误</td><td>检查参数格式和值</td></tr>
    <tr><td>错误代码 10004007/08/10</td><td>日期格式错误</td><td>使用 <code>YYYY-MM-DD</code> 格式</td></tr>
    <tr><td>错误代码 10004009</td><td>起始日期晚于结束日期</td><td>调整日期范围</td></tr>
    <tr><td>错误代码 10004011</td><td>证券代码无效</td><td>使用正确格式如 <code>sh.600000</code></td></tr>
    <tr><td>错误代码 10004012</td><td>指标名称无效</td><td>检查指标拼写是否正确</td></tr>
  </tbody>
</table>

### 2.4 IP黑名单检查

当登录时返回错误代码 `10001011`，表示IP已被加入黑名单。可使用以下代码检查：

```python
import baostock as bs

# 示例代码：查看IP是否加入黑名单
lg = bs.login()

# 显示登陆返回信息
# 当黑名单控制时，error_code输出"10001011"、error_msg输出"黑名单用户，请与管理员联系"
print('login respond error_code:' + lg.error_code)
print('login respond  error_msg:' + lg.error_msg)

if lg.error_code == "10001011":
    print("IP已经受黑名单控制, 请去官网QQ群里向管理员求助.")
```

**解决方案：** 等待自动解封（访问规则(统计)：https://www.baostock.com/blacklist ），如果其他疑问请去官网QQ群里向管理员求助。

---

## 3 登录认证错误（10001xxx）

<table class="error-table">
  <thead>
    <tr>
      <th>错误代码</th>
      <th>错误名称</th>
      <th>说明</th>
      <th>处理建议</th>
    </tr>
  </thead>
  <tbody>
    <tr><td>10001001</td><td>BSERR_NO_LOGIN</td><td>用户未登陆</td><td>请先调用 <code>bs.login()</code> 进行登录</td></tr>
    <tr><td>10001002</td><td>BSERR_USERNAMEORPASSWORD_ERR</td><td>用户名或密码错误</td><td>请检查登录账号和密码是否正确</td></tr>
    <tr><td>10001003</td><td>BSERR_GETUSERINFO_FAIL</td><td>获取用户信息失败</td><td>请稍后重试，或联系客服</td></tr>
    <tr><td>10001004</td><td>BSERR_CLIENT_VESION_EXPIRE</td><td>客户端版本号过期</td><td>请升级 BaoStock 客户端到最新版本：<code>pip install baostock --upgrade</code></td></tr>
    <tr><td>10001005</td><td>BSERR_LOGIN_COUNT_LIMIT</td><td>账号登陆数达到上限</td><td>请等待其他登录会话过期后重试，或先调用 <code>bs.logout()</code> 登出其他会话</td></tr>
    <tr><td>10001006</td><td>BSERR_ACCESS_INSUFFICIENCE</td><td>用户权限不足</td><td>当前账号无权限执行该操作，请联系客服提升权限</td></tr>
    <tr><td>10001007</td><td>BSERR_NEED_ACTIVATE</td><td>需要登录激活</td><td>请先登录激活账号</td></tr>
    <tr><td>10001008</td><td>BSERR_USERNAME_EMPTY</td><td>用户名为空</td><td>登录时请提供用户名参数</td></tr>
    <tr><td>10001009</td><td>BSERR_PASSWORD_EMPTY</td><td>密码为空</td><td>登录时请提供密码参数</td></tr>
    <tr><td>10001010</td><td>BSERR_LOGOUT_FAIL</td><td>用户登出失败</td><td>请稍后重试</td></tr>
    <tr><td>10001011</td><td>BSERR_BLACKLIST_USER</td><td>黑名单用户</td><td>该账号已被限制使用，请联系客服</td></tr>
    <tr><td>10001012</td><td>BSERR_APIKey_FORMAT_INCORRECT</td><td>APIKey格式不正确</td><td>请检查 APIKey 格式是否正确</td></tr>
  </tbody>
</table>

---

## 4 网络连接错误（10002xxx）

<table class="error-table">
  <thead>
    <tr>
      <th>错误代码</th>
      <th>错误名称</th>
      <th>说明</th>
      <th>处理建议</th>
    </tr>
  </thead>
  <tbody>
    <tr><td>10002001</td><td>BSERR_SOCKET_ERR</td><td>网络错误</td><td>请检查网络连接是否正常</td></tr>
    <tr><td>10002002</td><td>BSERR_CONNECT_FAIL</td><td>网络连接失败</td><td>请检查网络连接和防火墙设置，确认服务器地址可访问</td></tr>
    <tr><td>10002003</td><td>BSERR_CONNECT_TIMEOUT</td><td>网络连接超时</td><td>请检查网络状况，稍后重试</td></tr>
    <tr><td>10002004</td><td>BSERR_RECVCONNECTION_CLOSED</td><td>网络接收时连接断开</td><td>连接被中断，请重新登录并重试</td></tr>
    <tr><td>10002005</td><td>BSERR_SENDSOCK_FAIL</td><td>网络发送失败</td><td>请检查网络连接后重试</td></tr>
    <tr><td>10002006</td><td>BSERR_SENDSOCK_TIMEOUT</td><td>网络发送超时</td><td>网络状况不佳，请稍后重试</td></tr>
    <tr><td>10002007</td><td>BSERR_RECVSOCK_FAIL</td><td>网络接收错误</td><td>请检查网络连接后重试</td></tr>
    <tr><td>10002008</td><td>BSERR_RECVSOCK_TIMEOUT</td><td>网络接收超时</td><td>网络状况不佳，请稍后重试</td></tr>
  </tbody>
</table>

---

## 5 数据与参数错误（10004xxx）

<table class="error-table">
  <thead>
    <tr>
      <th>错误代码</th>
      <th>错误名称</th>
      <th>说明</th>
      <th>处理建议</th>
    </tr>
  </thead>
  <tbody>
    <tr><td>10004001</td><td>BSERR_PARSE_DATA_ERR</td><td>解析数据错误</td><td>返回数据格式异常，请重试或联系客服</td></tr>
    <tr><td>10004002</td><td>BSERR_UNGZIP_DATA_FAIL</td><td>gzip 解压失败</td><td>数据解压失败，请重试</td></tr>
    <tr><td>10004003</td><td>BSERR_UNKNOWN_ERR</td><td>客户端未知错误</td><td>请升级客户端版本后重试</td></tr>
    <tr><td>10004004</td><td>BSERR_OUTOF_BOUNDS</td><td>数组越界</td><td>内部错误，请重试或联系客服</td></tr>
    <tr><td>10004005</td><td>BSERR_INPARAM_EMPTY</td><td>传入参数为空</td><td>请检查必填参数是否已提供</td></tr>
    <tr><td>10004006</td><td>BSERR_PARAM_ERR</td><td>参数错误</td><td>请检查传入参数的格式和值是否正确</td></tr>
    <tr><td>10004007</td><td>BSERR_START_DATE_ERR</td><td>起始日期格式不正确</td><td>日期格式应为 <code>YYYY-MM-DD</code>，如 <code>2024-01-01</code></td></tr>
    <tr><td>10004008</td><td>BSERR_END_DATE_ERR</td><td>截止日期格式不正确</td><td>日期格式应为 <code>YYYY-MM-DD</code>，如 <code>2024-12-31</code></td></tr>
    <tr><td>10004009</td><td>BSERR_START_BIGTHAN_END</td><td>起始日期大于终止日期</td><td>请确保起始日期早于终止日期</td></tr>
    <tr><td>10004010</td><td>BSERR_DATE_ERR</td><td>日期格式不正确</td><td>日期格式应为 <code>YYYY-MM-DD</code></td></tr>
    <tr><td>10004011</td><td>BSERR_CODE_INVALIED</td><td>无效的证券代码</td><td>请检查证券代码格式，如 <code>sh.600000</code>、<code>sz.000001</code></td></tr>
    <tr><td>10004012</td><td>BSERR_INDICATOR_INVALIED</td><td>无效的指标</td><td>请检查查询指标名称是否正确</td></tr>
    <tr><td>10004013</td><td>BSERR_BEYOND_DATE_SUPPORT</td><td>超出日期支持范围</td><td>请调整查询日期范围</td></tr>
    <tr><td>10004014</td><td>BSERR_MIXED_CODES_MARKET</td><td>不支持的混合证券品种</td><td>请不要混合查询不同市场的证券</td></tr>
    <tr><td>10004015</td><td>BSERR_NO_SUPPORT_CODES_MARKET</td><td>不支持的证券代码品种</td><td>请检查证券代码是否为支持的品种</td></tr>
    <tr><td>10004016</td><td>BSERR_ORDER_TO_UPPER_LIMIT</td><td>交易条数超过上限</td><td>请减少查询条数</td></tr>
    <tr><td>10004017</td><td>BSERR_NO_SUPPORT_ORDERINFO</td><td>不支持的交易信息</td><td>请检查交易信息查询参数</td></tr>
    <tr><td>10004018</td><td>BSERR_INDICATOR_REPEAT</td><td>指标重复</td><td>请去除重复的指标参数</td></tr>
    <tr><td>10004019</td><td>BSERR_MESSAGE_ERROR</td><td>消息格式不正确</td><td>内部通信错误，请重试</td></tr>
    <tr><td>10004020</td><td>BSERR_MESSAGE_CODE_ERROR</td><td>错误的消息类型</td><td>内部通信错误，请重试</td></tr>
  </tbody>
</table>

---

## 6 系统错误（10005xxx）

<table class="error-table">
  <thead>
    <tr>
      <th>错误代码</th>
      <th>错误名称</th>
      <th>说明</th>
      <th>处理建议</th>
    </tr>
  </thead>
  <tbody>
    <tr><td>10005001</td><td>BSERR_SYSTEM_ERROR</td><td>系统级别错误</td><td>服务端异常，请稍后重试。如持续出现请联系客服</td></tr>
  </tbody>
</table>

---

## 7 客户端错误提示

<table class="faq-table">
  <thead>
    <tr>
      <th>提示信息</th>
      <th>说明</th>
      <th>处理建议</th>
    </tr>
  </thead>
  <tbody>
    <tr><td>参数错误，请检查。</td><td>客户端参数校验不通过</td><td>请检查传入参数的格式和值</td></tr>
  </tbody>
</table>

---

## 8 正确用法示例

```python
import baostock as bs
import pandas as pd

lg = bs.login()
print('login respond error_code:' + lg.error_code)  # 错误代码
print('login respond  error_msg:' + lg.error_msg)   # 错误信息

rs = bs.query_history_k_data_plus(
    "sh.600000",
    "date,code,open,high,low,close,preclose,volume,amount,adjustflag,turn,tradestatus,pctChg,isST",
    start_date="2024-07-01",end_date="2024-12-31",frequency="d",adjustflag="3",)

# 关键：遍历取数
data_list = []
while (rs.error_code == "0") & rs.next():
    data_list.append(rs.get_row_data())

df = pd.DataFrame(data_list, columns=rs.fields)
print(df.to_string())   # 完整输出，不省略列
print("共", len(df), "行")

bs.logout()
```

---

> 如遇到无法解决的问题，请联系客服邮箱：baostock@163.com