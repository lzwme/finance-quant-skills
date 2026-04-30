---
url: "https://dict.thinktrader.net/nativeApi/code_examples.html"
title: "完整实例 | 迅投知识库"
---

## 行情示例

### 获取行情示例

新手示例

```py
# 用前须知

## xtdata提供和MiniQmt的交互接口，本质是和MiniQmt建立连接，由MiniQmt处理行情数据请求，再把结果回传返回到python层。使用的行情服务器以及能获取到的行情数据和MiniQmt是一致的，要检查数据或者切换连接时直接操作MiniQmt即可。

## 对于数据获取接口，使用时需要先确保MiniQmt已有所需要的数据，如果不足可以通过补充数据接口补充，再调用数据获取接口获取。

## 对于订阅接口，直接设置数据回调，数据到来时会由回调返回。订阅接收到的数据一般会保存下来，同种数据不需要再单独补充。

# 代码讲解

# 从本地python导入xtquant库，如果出现报错则说明安装失败
from xtquant import xtdata
import time

# 设定一个标的列表
code_list = ["000001.SZ"]
# 设定获取数据的周期
period = "1d"

# 下载标的行情数据
if 1:
    ## 为了方便用户进行数据管理，xtquant的大部分历史数据都是以压缩形式存储在本地的
    ## 比如行情数据，需要通过download_history_data下载，财务数据需要通过
    ## 所以在取历史数据之前，我们需要调用数据下载接口，将数据下载到本地
    for i in code_list:
        xtdata.download_history_data(i,period=period,incrementally=True) # 增量下载行情数据（开高低收,等等）到本地

    xtdata.download_financial_data(code_list) # 下载财务数据到本地
    xtdata.download_sector_data() # 下载板块数据到本地
    # 更多数据的下载方式可以通过数据字典查询

# 读取本地历史行情数据
history_data = xtdata.get_market_data_ex([],code_list,period=period,count=-1)
print(history_data)
print("=" * 20)

# 如果需要盘中的实时行情，需要向服务器进行订阅后才能获取
# 订阅后，get_market_data函数于get_market_data_ex函数将会自动拼接本地历史行情与服务器实时行情

# 向服务器订阅数据
for i in code_list:
    xtdata.subscribe_quote(i,period=period,count=-1) # 设置count = -1来取到当天所有实时行情

# 等待订阅完成
time.sleep(1)

# 获取订阅后的行情
kline_data = xtdata.get_market_data_ex([],code_list,period=period)
print(kline_data)

# 获取订阅后的行情，并以固定间隔进行刷新,预期会循环打印10次
for i in range(10):
    # 这边做演示，就用for来循环了，实际使用中可以用while True
    kline_data = xtdata.get_market_data_ex([],code_list,period=period)
    print(kline_data)
    time.sleep(3) # 三秒后再次获取行情

# 如果不想用固定间隔触发，可以以用订阅后的回调来执行
# 这种模式下当订阅的callback回调函数将会异步的执行，每当订阅的标的tick发生变化更新，callback回调函数就会被调用一次
# 本地已有的数据不会触发callback

# 定义的回测函数
    ## 回调函数中，data是本次触发回调的数据，只有一条
def f(data):
    # print(data)

    code_list = list(data.keys())    # 获取到本次触发的标的代码

    kline_in_callabck = xtdata.get_market_data_ex([],code_list,period = period)    # 在回调中获取klines数据
    print(kline_in_callabck)

for i in code_list:
    xtdata.subscribe_quote(i,period=period,count=-1,callback=f) # 订阅时设定回调函数

# 使用回调时，必须要同时使用xtdata.run()来阻塞程序，否则程序运行到最后一行就直接结束退出了。
xtdata.run()
```

### 连接VIP服务器

```py
# 导入 xtdatacenter 模块
import sys

print("Python 版本：", sys.version)

import time
import pandas as pd
from xtquant import xtdatacenter as xtdc
from xtquant import xtdata
'''
设置用于登录行情服务的token，此接口应该先于 init_quote 调用

token可以从投研用户中心获取
https://xuntou.net/#/userInfo
'''
xtdc.set_token('这里输入token')

'''
设置连接池,使服务器只在连接池内优选

建议将VIP服务器设为连接池
'''
addr_list = [
    '115.231.218.73:55310',
    '115.231.218.79:55310',
    '42.228.16.211:55300',
    '42.228.16.210:55300',
    '36.99.48.20:55300',
    '36.99.48.21:55300'
    ]
xtdc.set_allow_optmize_address(addr_list)

xtdc.set_kline_mirror_enabled(True) # 开启K线全推功能(vip),以获取全市场实时K线数据

"""
初始化
"""
xtdc.init()
## 监听端口
port = xtdc.listen(port = 58621) # 指定固定端口进行连接
# port = xtdc.listen(port = (58620, 58630))[1] 通过指定port范围，可以让xtdc在范围内自动寻找可用端口

xtdata.connect(port=port)

print('-----连接上了------')
print(xtdata.data_dir)

servers = xtdata.get_quote_server_status()
# print(servers)
for k, v in servers.items():
    print(k, v)

xtdata.run()
```

### 连接指定服务器

```py

import time
from xtquant import xtdata

#用token方式连接，不需要账号密码
#其他连接方式，需要账号密码
info = {"ip": '115.231.218.73', "port": 55300, "username": '', "pwd": ''}

connect_success = 0
def func(d):
    ip = d.get('ip', '')
    port = d.get('port')
    status = d.get('status', 'disconnected')

    global connect_success
    if ip == info['ip'] and port == info['port']:
        if status == 'connected':
            connect_success = 1
        else:
            connect_success = 2

# 注册连接回调信息
xtdata.watch_quote_server_status(func)

# 行情连接
qs = xtdata.QuoteServer(info)
qs.connect()

# 获取当前数据连接站点
data_server_info = xtdata.get_quote_server_status()
# 显示当前数据连接站点
if 1:
    for k,v in data_server_info.items():
        print(f"data:{k}, connect info:{v.info}")

# 等待连接状态
while connect_success == 0:
    time.sleep(0.3)

if connect_success == 2:
    print("连接失败")
```

### 指定初始化行情连接范围

```py
if 1:
    from xtquant import xtdatacenter as xtdc

    ## 设置数据目录
    xtdc.set_data_home_dir('data')

    ## 设置token
    token = "你的token"
    xtdc.set_token(token)

    ## 限定行情站点的优选范围
    opt_list = [
        '115.231.218.73:55310',
        '115.231.218.79:55310',
        '42.228.16.210:55300',
        '42.228.16.211:55300',
        '36.99.48.20:55300',
        '36.99.48.21:55300',
    ]
    xtdc.set_allow_optmize_address(opt_list)

    ## 开启指定市场的K线全推
    xtdc.set_kline_mirror_markets(['SH', 'SZ', 'BJ'])

    ## 设置要初始化的市场列表
    init_markets = [
        'SH', 'SZ', 'BJ',
        #'DF', 'GF', 'IF', 'SF', 'ZF', 'INE',
        #'SHO', 'SZO',
    ]
    xtdc.set_init_markets(init_markets)

    ## 初始化xtdc模块
    xtdc.init(start_local_service = False)

    ## 监听端口
    #xtdc.listen(port = 58620)
    listen_port = xtdc.listen(port = (58620, 58650))

    #import code; code.interact(local = locals())

import xtquant.xtdata as xtdata

xtdata.connect(port = listen_port)

import code; code.interact(local = locals())
```

### 订阅全推数据/下载历史数据

```py
# coding:utf-8
import time

from xtquant import xtdata

code = '600000.SH'

#取全推数据
full_tick = xtdata.get_full_tick([code])
print('全推数据 日线最新值', full_tick)

#下载历史数据 下载接口本身不返回数据
xtdata.download_history_data(code, period='1m', start_time='20230701')

#订阅最新行情
def callback_func(data):
    print('回调触发', data)

xtdata.subscribe_quote(code, period='1m', count=-1, callback= callback_func)
data = xtdata.get_market_data(['close'], [code], period='1m', start_time='20230701')
print('一次性取数据', data)

#死循环 阻塞主线程退出
xtdata.run()
```

### 获取对手价

```py
# 以卖出为例

import pandas as pd
import numpy as np
from xtquant import xtdata

to_do_trade_list = ["000001.SZ"]
tick = xtdata.get_full_tick(to_do_trade_list)

# 取买一价为对手价，若买一价为0，说明已经跌停，则取最新价
for i in tick:
    fix_price = tick[i]["bidPrice"][0] if tick[i]["bidPrice"][0] != 0 else tick[i]["lastPrice"]
    print(fix_price)
```

```
10.01
```

### 复权计算方式

```py
#coding:utf-8

import numpy as np
import pandas as pd

from xtquant import xtdata

#def gen_divid_ratio(quote_datas, divid_datas):
#    drl = []
#    for qi in range(len(quote_datas)):
#        q = quote_datas.iloc[qi]
#        dr = 1.0
#        for di in range(len(divid_datas)):
#            d = divid_datas.iloc[di]
#            if d.name <= q.name:
#                dr *= d['dr']
#        drl.append(dr)
#    return pd.DataFrame(drl, index = quote_datas.index, columns = quote_datas.columns)

def gen_divid_ratio(quote_datas, divid_datas):
    drl = []
    dr = 1.0
    qi = 0
    qdl = len(quote_datas)
    di = 0
    ddl = len(divid_datas)
    while qi < qdl and di < ddl:
        qd = quote_datas.iloc[qi]
        dd = divid_datas.iloc[di]
        if qd.name >= dd.name:
            dr *= dd['dr']
            di += 1
        if qd.name <= dd.name:
            drl.append(dr)
            qi += 1
    while qi < qdl:
        drl.append(dr)
        qi += 1
    return pd.DataFrame(drl, index = quote_datas.index, columns = quote_datas.columns)

def process_forward_ratio(quote_datas, divid_datas):
    drl = gen_divid_ratio(quote_datas, divid_datas)
    drlf = drl / drl.iloc[-1]
    result = (quote_datas * drlf).apply(lambda x: round(x, 2))
    return result

def process_backward_ratio(quote_datas, divid_datas):
    drl = gen_divid_ratio(quote_datas, divid_datas)
    result = (quote_datas * drl).apply(lambda x: round(x, 2))
    return result

def process_forward(quote_datas1, divid_datas):
    quote_datas = quote_datas1.copy()
    def calc_front(v, d):
        return ((v - d['interest'] + d['allotPrice'] * d['allotNum'])
            / (1 + d['allotNum'] + d['stockBonus'] + d['stockGift']))
    for qi in range(len(quote_datas)):
        q = quote_datas.iloc[qi]
        for di in range(len(divid_datas)):
            d = divid_datas.iloc[di]
            if d.name <= q.name:
                continue
            q.iloc[0] = calc_front(q.iloc[0], d)
    return quote_datas

def process_backward(quote_datas1, divid_datas):
    quote_datas = quote_datas1.copy()
    def calc_back(v, d):
        return ((v * (1.0 + d['stockGift'] + d['stockBonus'] + d['allotNum'])
            + d['interest'] - d['allotNum'] * d['allotPrice']))
    for qi in range(len(quote_datas)):
        q = quote_datas.iloc[qi]
        for di in range(len(divid_datas) - 1, -1, -1):
            d = divid_datas.iloc[di]
            if d.name > q.name:
                continue
            q.iloc[0] = calc_back(q.iloc[0], d)
    return quote_datas

#--------------------------------

s = '002594.SZ'

#xtdata.download_history_data(s, '1d', '20100101', '')

dd = xtdata.get_divid_factors(s)
print(dd)

#复权计算用于处理价格字段
field_list = ['open', 'high', 'low', 'close']
datas_ori = xtdata.get_market_data(field_list, [s], '1d', dividend_type = 'none')['close'].T
#print(datas_ori)

#等比前复权
datas_forward_ratio = process_forward_ratio(datas_ori, dd)
print('datas_forward_ratio', datas_forward_ratio)

#等比后复权
datas_backward_ratio = process_backward_ratio(datas_ori, dd)
print('datas_backward_ratio', datas_backward_ratio)

#前复权
datas_forward = process_forward(datas_ori, dd)
print('datas_forward', datas_forward)

#后复权
datas_backward = process_backward(datas_ori, dd)
print('datas_backward', datas_backward)
```

### 根据商品期货期权代码获取对应的商品期货合约代码

```py
from xtquant import xtdata

def get_option_underline_code(code:str) -> str:
    """
    注意：该函数不适用于股指期货期权与ETF期权
    Todo: 根据商品期权代码获取对应的具体商品期货合约
    Args:
        code:str 期权代码
    Return:
        对应的期货合约代码
    """
    Exchange_dict = {
        "SHFE":"SF",
        "CZCE":"ZF",
        "DCE":"DF",
        "INE":"INE",
        "GFEX":"GF"
    }

    if code.split(".")[-1] not in [v for k,v in Exchange_dict.items()]:
        raise KeyError("此函数不支持该交易所合约")
    info = xtdata.get_option_detail_data(code)
    underline_code = info["OptUndlCode"] + "." + Exchange_dict[info["OptUndlMarket"]]

    return underline_code

if __name__ == "__main__":

    symbol_code = get_option_underline_code('sc2403C465.INE') # 获取期权合约'sc2403C465.INE'对应的期货合约代码
    print(symbol_code)
```

```
'sc2403.INE'
```

### 根据指数代码，返回对应的期货合约

```py

from xtquant import xtdata
import re

def get_financial_futures_code_from_index(index_code:str) -> list:
    """
    ToDo:传入指数代码，返回对应的期货合约（当前）
    Args:
        index_code:指数代码，如"000300.SH","000905.SH"
    Retuen:
        list: 对应期货合约列表
    """
    financial_futures = xtdata.get_stock_list_in_sector("中金所")
    future_list = []
    pattern = r'^[a-zA-Z]{1,2}\d{3,4}\.[A-Z]{2}$'
    for i in financial_futures:

        if re.match(pattern,i):
            future_list.append(i)
    ls = []
    for i in future_list:
        _info = xtdata._get_instrument_detail(i)
        _index_code = _info["ExtendInfo"]['OptUndlCode'] + "." + _info["ExtendInfo"]['OptUndlMarket']
        if _index_code == index_code:
            ls.append(i)
    return ls

if __name__ == "__main__":
    ls = get_financial_futures_code_from_index("000905.SH")
    print(ls)
```

```
['IC2402.IF', 'IC2403.IF', 'IC2406.IF', 'IC2409.IF']
```

## 交易示例

### 简单买卖各一笔示例

**需要调整的参数：**

- `98`行的`path`变量需要改为本地客户端路径,券商端指定到 f"{安装目录}\\userdata_mini",投研端指定到f"{安装目录}\\userdata"
- `107`行的资金账号需要调整为自身资金账号

```py
# coding:utf-8
import time, datetime, traceback, sys
from xtquant import xtdata
from xtquant.xttrader import XtQuantTrader, XtQuantTraderCallback
from xtquant.xttype import StockAccount
from xtquant import xtconstant

# 定义一个类 创建类的实例 作为状态的容器
class _a():
    pass

A = _a()
A.bought_list = []
A.hsa = xtdata.get_stock_list_in_sector('沪深A股')

def interact():
    """执行后进入repl模式"""
    import code
    code.InteractiveConsole(locals=globals()).interact()

xtdata.download_sector_data()

class MyXtQuantTraderCallback(XtQuantTraderCallback):
    def on_disconnected(self):
        """
        连接断开
        :return:
        """
        print(datetime.datetime.now(), '连接断开回调')

    def on_stock_order(self, order):
        """
        委托回报推送
        :param order: XtOrder对象
        :return:
        """
        print(datetime.datetime.now(), '委托回调 投资备注', order.order_remark)

    def on_stock_trade(self, trade):
        """
        成交变动推送
        :param trade: XtTrade对象
        :return:
        """
        print(datetime.datetime.now(), '成交回调', trade.order_remark, f"委托方向(48买 49卖) {trade.offset_flag} 成交价格 {trade.traded_price} 成交数量 {trade.traded_volume}")

    def on_order_error(self, order_error):
        """
        委托失败推送
        :param order_error:XtOrderError 对象
        :return:
        """
        # print("on order_error callback")
        # print(order_error.order_id, order_error.error_id, order_error.error_msg)
        print(f"委托报错回调 {order_error.order_remark} {order_error.error_msg}")

    def on_cancel_error(self, cancel_error):
        """
        撤单失败推送
        :param cancel_error: XtCancelError 对象
        :return:
        """
        print(datetime.datetime.now(), sys._getframe().f_code.co_name)

    def on_order_stock_async_response(self, response):
        """
        异步下单回报推送
        :param response: XtOrderResponse 对象
        :return:
        """
        print(f"异步委托回调 投资备注: {response.order_remark}")

    def on_cancel_order_stock_async_response(self, response):
        """
        :param response: XtCancelOrderResponse 对象
        :return:
        """
        print(datetime.datetime.now(), sys._getframe().f_code.co_name)

    def on_account_status(self, status):
        """
        :param response: XtAccountStatus 对象
        :return:
        """
        print(datetime.datetime.now(), sys._getframe().f_code.co_name)

if __name__ == '__main__':
    print("start")
    # 指定客户端所在路径, 券商端指定到 userdata_mini文件夹
    # 注意：如果是连接投研端进行交易，文件目录需要指定到f"{安装目录}\\userdata"
    path = r'D:\\qmt\\投研\\迅投极速交易终端睿智融科版\\userdata'
    # 生成session id 整数类型 同时运行的策略不能重复
    session_id = int(time.time())
    xt_trader = XtQuantTrader(path, session_id)
    # 开启主动请求接口的专用线程 开启后在on_stock_xxx回调函数里调用XtQuantTrader.query_xxx函数不会卡住回调线程，但是查询和推送的数据在时序上会变得不确定
    # 详见: http://docs.thinktrader.net/vip/pages/ee0e9b/#开启主动请求接口的专用线程
    # xt_trader.set_relaxed_response_order_enabled(True)

    # 创建资金账号为 800068 的证券账号对象 股票账号为STOCK 信用CREDIT 期货FUTURE
    acc = StockAccount('2000128', 'STOCK')
    # 创建交易回调类对象，并声明接收回调
    callback = MyXtQuantTraderCallback()
    xt_trader.register_callback(callback)
    # 启动交易线程
    xt_trader.start()
    # 建立交易连接，返回0表示连接成功
    connect_result = xt_trader.connect()
    print('建立交易连接，返回0表示连接成功', connect_result)
    # 对交易回调进行订阅，订阅后可以收到交易主推，返回0表示订阅成功
    subscribe_result = xt_trader.subscribe(acc)
    print('对交易回调进行订阅，订阅后可以收到交易主推，返回0表示订阅成功', subscribe_result)
    #取账号信息
    account_info = xt_trader.query_stock_asset(acc)
    #取可用资金
    available_cash = account_info.m_dCash

    print(acc.account_id, '可用资金', available_cash)
    #查账号持仓
    positions = xt_trader.query_stock_positions(acc)
    #取各品种 总持仓 可用持仓
    position_total_dict = {i.stock_code : i.m_nVolume for i in positions}
    position_available_dict = {i.stock_code : i.m_nCanUseVolume for i in positions}
    print(acc.account_id, '持仓字典', position_total_dict)
    print(acc.account_id, '可用持仓字典', position_available_dict)

    #买入 浦发银行 最新价 两万元
    stock = '600000.SH'
    target_amount = 20000
    full_tick = xtdata.get_full_tick([stock])
    print(f"{stock} 全推行情： {full_tick}")
    current_price = full_tick[stock]['lastPrice']
    #买入金额 取目标金额 与 可用金额中较小的
    buy_amount = min(target_amount, available_cash)
    #买入数量 取整为100的整数倍
    buy_vol = int(buy_amount / current_price / 100) * 100
    print(f"当前可用资金 {available_cash} 目标买入金额 {target_amount} 买入股数 {buy_vol}股")
    async_seq = xt_trader.order_stock_async(acc, stock, xtconstant.STOCK_BUY, buy_vol, xtconstant.FIX_PRICE, current_price,
                                            'strategy_name', stock)

    #卖出 500股
    stock = '513130.SH'
    #目标数量
    target_vol = 500
    #可用数量
    available_vol = position_available_dict[stock] if stock in position_available_dict else 0
    #卖出量取目标量与可用量中较小的
    sell_vol = min(target_vol, available_vol)
    print(f"{stock} 目标卖出量 {target_vol} 可用数量 {available_vol} 卖出 {sell_vol}股")
    if sell_vol > 0:
        async_seq = xt_trader.order_stock_async(acc, stock, xtconstant.STOCK_SELL, sell_vol, xtconstant.LATEST_PRICE,
                                                -1,
                                                'strategy_name', stock)
    print(f"下单完成 等待回调")
    # 阻塞主线程退出
    xt_trader.run_forever()
    # 如果使用vscode pycharm等本地编辑器 可以进入交互模式 方便调试 （把上一行的run_forever注释掉 否则不会执行到这里）
    interact()
```

### 单股订阅实盘示例

**需要调整的参数：**

- `113`行的`path`变量需要改为本地客户端路径,券商端指定到 f"{安装目录}\\userdata_mini",投研端指定到f"{安装目录}\\userdata"
- `122`行的资金账号需要调整为自身资金账号

```py
# coding:utf-8
import time, datetime, traceback, sys
from xtquant import xtdata
from xtquant.xttrader import XtQuantTrader, XtQuantTraderCallback
from xtquant.xttype import StockAccount
from xtquant import xtconstant

# 定义一个类 创建类的实例 作为状态的容器
class _a():
    pass

A = _a()
A.bought_list = []
A.hsa = xtdata.get_stock_list_in_sector('沪深A股')

def interact():
    """执行后进入repl模式"""
    import code
    code.InteractiveConsole(locals=globals()).interact()

xtdata.download_sector_data()

def f(data):
    print(data)
    now = datetime.datetime.now()
    for stock in data:
        if stock not in A.hsa:
            continue
        cuurent_price = data[stock][0]['close']
        pre_price = data[stock][0]['preClose']
        ratio = cuurent_price / pre_price - 1 if pre_price > 0 else 0
        if ratio > 0.09 and stock not in A.bought_list:
            print(f"{now} 最新价 买入 {stock} 100股")
            async_seq = xt_trader.order_stock_async(acc, stock, xtconstant.STOCK_BUY, 100, xtconstant.LATEST_PRICE, -1,
                                                    'strategy_name', stock)
            A.bought_list.append(stock)

class MyXtQuantTraderCallback(XtQuantTraderCallback):
    def on_disconnected(self):
        """
        连接断开
        :return:
        """
        print(datetime.datetime.now(), '连接断开回调')

    def on_stock_order(self, order):
        """
        委托回报推送
        :param order: XtOrder对象
        :return:
        """
        print(datetime.datetime.now(), '委托回调', order.order_remark)

    def on_stock_trade(self, trade):
        """
        成交变动推送
        :param trade: XtTrade对象
        :return:
        """
        print(datetime.datetime.now(), '成交回调', trade.order_remark)

    def on_order_error(self, order_error):
        """
        委托失败推送
        :param order_error:XtOrderError 对象
        :return:
        """
        # print("on order_error callback")
        # print(order_error.order_id, order_error.error_id, order_error.error_msg)
        print(f"委托报错回调 {order_error.order_remark} {order_error.error_msg}")

    def on_cancel_error(self, cancel_error):
        """
        撤单失败推送
        :param cancel_error: XtCancelError 对象
        :return:
        """
        print(datetime.datetime.now(), sys._getframe().f_code.co_name)

    def on_order_stock_async_response(self, response):
        """
        异步下单回报推送
        :param response: XtOrderResponse 对象
        :return:
        """
        print(f"异步委托回调 {response.order_remark}")

    def on_cancel_order_stock_async_response(self, response):
        """
        :param response: XtCancelOrderResponse 对象
        :return:
        """
        print(datetime.datetime.now(), sys._getframe().f_code.co_name)

    def on_account_status(self, status):
        """
        :param response: XtAccountStatus 对象
        :return:
        """
        print(datetime.datetime.now(), sys._getframe().f_code.co_name)

if __name__ == '__main__':
    print("start")
    # 指定客户端所在路径, 券商端指定到 userdata_mini文件夹
    # 注意：如果是连接投研端进行交易，文件目录需要指定到f"{安装目录}\userdata"
    path = r'D:\\qmt\\投研\\迅投极速交易终端睿智融科版\\userdata'
    # 生成session id 整数类型 同时运行的策略不能重复
    session_id = int(time.time())
    xt_trader = XtQuantTrader(path, session_id)
    # 开启主动请求接口的专用线程 开启后在on_stock_xxx回调函数里调用XtQuantTrader.query_xxx函数不会卡住回调线程，但是查询和推送的数据在时序上会变得不确定
    # 详见: http://docs.thinktrader.net/vip/pages/ee0e9b/#开启主动请求接口的专用线程
    # xt_trader.set_relaxed_response_order_enabled(True)

    # 创建资金账号为 800068 的证券账号对象 股票账号为STOCK 信用CREDIT 期货FUTURE
    acc = StockAccount('2000128', 'STOCK')
    # 创建交易回调类对象，并声明接收回调
    callback = MyXtQuantTraderCallback()
    xt_trader.register_callback(callback)
    # 启动交易线程
    xt_trader.start()
    # 建立交易连接，返回0表示连接成功
    connect_result = xt_trader.connect()
    print('建立交易连接，返回0表示连接成功', connect_result)
    # 对交易回调进行订阅，订阅后可以收到交易主推，返回0表示订阅成功
    subscribe_result = xt_trader.subscribe(acc)
    print('对交易回调进行订阅，订阅后可以收到交易主推，返回0表示订阅成功', subscribe_result)

    #订阅的品种列表
    code_list = ['600000.SH', '000001.SZ']

    for code in code_list:
        xtdata.subscribe_quote(code, '1d', callback = f)

    # 阻塞主线程退出
    xt_trader.run_forever()
    # 如果使用vscode pycharm等本地编辑器 可以进入交互模式 方便调试 （把上一行的run_forever注释掉 否则不会执行到这里）
    interact()
```

### 全推订阅实盘示例

本示例用于展示如何订阅上海及深圳市场全推，对于沪深A股品种策略进行判断当前涨幅超过 9 个点的买入 200 股

**需要调整的参数：**

- `111`行的`path`变量需要改为本地客户端路径
- `116`行的资金账号需要调整为自身资金账号

注意

本策略只用于提供策略写法及参考，若您直接进行实盘下单，造成损失本网站不负担责任。

```py
#coding:utf-8
import time, datetime, traceback, sys
from xtquant import xtdata
from xtquant.xttrader import XtQuantTrader, XtQuantTraderCallback
from xtquant.xttype import StockAccount
from xtquant import xtconstant

#定义一个类 创建类的实例 作为状态的容器
class _a():
    pass
A = _a()
A.bought_list = []
A.hsa = xtdata.get_stock_list_in_sector('沪深A股')

def interact():
    """执行后进入repl模式"""
    import code
    code.InteractiveConsole(locals=globals()).interact()
xtdata.download_sector_data()

def f(data):
    now = datetime.datetime.now()
    for stock in data:
        if stock not in A.hsa:
            continue
        cuurent_price = data[stock][0]['lastPrice']
        pre_price = data[stock][0]['lastClose']
        ratio = cuurent_price / pre_price - 1 if pre_price > 0 else 0
        if ratio > 0.09 and stock not in A.bought_list:
            print(f"{now} 最新价 买入 {stock} 200股")
            async_seq = xt_trader.order_stock_async(acc, stock, xtconstant.STOCK_BUY, 200, xtconstant.LATEST_PRICE, -1, 'strategy_name', stock)
            A.bought_list.append(stock)

class MyXtQuantTraderCallback(XtQuantTraderCallback):
    def on_disconnected(self):
        """
        连接断开
        :return:
        """
        print(datetime.datetime.now(),'连接断开回调')

    def on_stock_order(self, order):
        """
        委托回报推送
        :param order: XtOrder对象
        :return:
        """
        print(datetime.datetime.now(), '委托回调', order.order_remark)

    def on_stock_trade(self, trade):
        """
        成交变动推送
        :param trade: XtTrade对象
        :return:
        """
        print(datetime.datetime.now(), '成交回调', trade.order_remark)

    def on_order_error(self, order_error):
        """
        委托失败推送
        :param order_error:XtOrderError 对象
        :return:
        """
        # print("on order_error callback")
        # print(order_error.order_id, order_error.error_id, order_error.error_msg)
        print(f"委托报错回调 {order_error.order_remark} {order_error.error_msg}")

    def on_cancel_error(self, cancel_error):
        """
        撤单失败推送
        :param cancel_error: XtCancelError 对象
        :return:
        """
        print(datetime.datetime.now(), sys._getframe().f_code.co_name)

    def on_order_stock_async_response(self, response):
        """
        异步下单回报推送
        :param response: XtOrderResponse 对象
        :return:
        """
        print(f"异步委托回调 {response.order_remark}")

    def on_cancel_order_stock_async_response(self, response):
        """
        :param response: XtCancelOrderResponse 对象
        :return:
        """
        print(datetime.datetime.now(), sys._getframe().f_code.co_name)

    def on_account_status(self, status):
        """
        :param response: XtAccountStatus 对象
        :return:
        """
        print(datetime.datetime.now(), sys._getframe().f_code.co_name)

if __name__ == '__main__':
    print("start")
    #指定客户端所在路径,
    # 注意：如果是连接投研端进行交易，文件目录需要指定到f"{安装目录}\\userdata"
    path = r'D:\\qmt\\sp3\\迅投极速交易终端 睿智融科版\\userdata_mini'
    # 生成session id 整数类型 同时运行的策略不能重复
    session_id = int(time.time())
    xt_trader = XtQuantTrader(path, session_id)
    # 开启主动请求接口的专用线程 开启后在on_stock_xxx回调函数里调用XtQuantTrader.query_xxx函数不会卡住回调线程，但是查询和推送的数据在时序上会变得不确定
    # 详见: http://docs.thinktrader.net/vip/pages/ee0e9b/#开启主动请求接口的专用线程
    # xt_trader.set_relaxed_response_order_enabled(True)

    # 创建资金账号为 800068 的证券账号对象
    acc = StockAccount('800068', 'STOCK')
    # 创建交易回调类对象，并声明接收回调
    callback = MyXtQuantTraderCallback()
    xt_trader.register_callback(callback)
    # 启动交易线程
    xt_trader.start()
    # 建立交易连接，返回0表示连接成功
    connect_result = xt_trader.connect()
    print('建立交易连接，返回0表示连接成功', connect_result)
    # 对交易回调进行订阅，订阅后可以收到交易主推，返回0表示订阅成功
    subscribe_result = xt_trader.subscribe(acc)
    print('对交易回调进行订阅，订阅后可以收到交易主推，返回0表示订阅成功', subscribe_result)

    #这一行是注册全推回调函数 包括下单判断 安全起见处于注释状态 确认理解效果后再放开
    # xtdata.subscribe_whole_quote(["SH", "SZ"], callback=f)
    # 阻塞主线程退出
    xt_trader.run_forever()
    # 如果使用vscode pycharm等本地编辑器 可以进入交互模式 方便调试 （把上一行的run_forever注释掉 否则不会执行到这里）
    interact()
```

### 定时判断实盘示例

```py
# coding:utf-8
import time, datetime, traceback, sys
from xtquant import xtdata
from xtquant.xttrader import XtQuantTrader, XtQuantTraderCallback
from xtquant.xttype import StockAccount
from xtquant import xtconstant

# 定义一个类 创建类的实例 作为状态的容器
class _a():
    pass

A = _a()
A.bought_list = []
A.hsa = xtdata.get_stock_list_in_sector('沪深A股')

def interact():
    """执行后进入repl模式"""
    import code
    code.InteractiveConsole(locals=globals()).interact()

xtdata.download_sector_data()

def f(data):
    now = datetime.datetime.now()
    # print(data)
    for stock in data:
        if stock not in A.hsa:
            continue
        cuurent_price = data[stock].iloc[-1, 0]
        pre_price = data[stock].iloc[-2, 0]
        ratio = cuurent_price / pre_price - 1 if pre_price > 0 else 0
        if ratio > 0.09 and stock not in A.bought_list:
            print(f"{now} 最新价 买入 {stock} 100股")
            async_seq = xt_trader.order_stock_async(acc, stock, xtconstant.STOCK_BUY, 100, xtconstant.LATEST_PRICE, -1,
                                                    'strategy_name', stock)
            A.bought_list.append(stock)

class MyXtQuantTraderCallback(XtQuantTraderCallback):
    def on_disconnected(self):
        """
        连接断开
        :return:
        """
        print(datetime.datetime.now(), '连接断开回调')

    def on_stock_order(self, order):
        """
        委托回报推送
        :param order: XtOrder对象
        :return:
        """
        print(datetime.datetime.now(), '委托回调', order.order_remark)

    def on_stock_trade(self, trade):
        """
        成交变动推送
        :param trade: XtTrade对象
        :return:
        """
        print(datetime.datetime.now(), '成交回调', trade.order_remark)

    def on_order_error(self, order_error):
        """
        委托失败推送
        :param order_error:XtOrderError 对象
        :return:
        """
        # print("on order_error callback")
        # print(order_error.order_id, order_error.error_id, order_error.error_msg)
        print(f"委托报错回调 {order_error.order_remark} {order_error.error_msg}")

    def on_cancel_error(self, cancel_error):
        """
        撤单失败推送
        :param cancel_error: XtCancelError 对象
        :return:
        """
        print(datetime.datetime.now(), sys._getframe().f_code.co_name)

    def on_order_stock_async_response(self, response):
        """
        异步下单回报推送
        :param response: XtOrderResponse 对象
        :return:
        """
        print(f"异步委托回调 {response.order_remark}")

    def on_cancel_order_stock_async_response(self, response):
        """
        :param response: XtCancelOrderResponse 对象
        :return:
        """
        print(datetime.datetime.now(), sys._getframe().f_code.co_name)

    def on_account_status(self, status):
        """
        :param response: XtAccountStatus 对象
        :return:
        """
        print(datetime.datetime.now(), sys._getframe().f_code.co_name)

if __name__ == '__main__':
    print("start")
    # 指定客户端所在路径, 券商端指定到 userdata_mini文件夹
    # 注意：如果是连接投研端进行交易，文件目录需要指定到f"{安装目录}\\userdata"
    path = r'D:\\qmt\\投研\\迅投极速交易终端睿智融科版\\userdata'
    # 生成session id 整数类型 同时运行的策略不能重复
    session_id = int(time.time())
    xt_trader = XtQuantTrader(path, session_id)
    # 开启主动请求接口的专用线程 开启后在on_stock_xxx回调函数里调用XtQuantTrader.query_xxx函数不会卡住回调线程，但是查询和推送的数据在时序上会变得不确定
    # 详见: http://docs.thinktrader.net/vip/pages/ee0e9b/#开启主动请求接口的专用线程
    # xt_trader.set_relaxed_response_order_enabled(True)

    # 创建资金账号为 800068 的证券账号对象 股票账号为STOCK 信用CREDIT 期货FUTURE
    acc = StockAccount('2000128', 'STOCK')
    # 创建交易回调类对象，并声明接收回调
    callback = MyXtQuantTraderCallback()
    xt_trader.register_callback(callback)
    # 启动交易线程
    xt_trader.start()
    # 建立交易连接，返回0表示连接成功
    connect_result = xt_trader.connect()
    print('建立交易连接，返回0表示连接成功', connect_result)
    # 对交易回调进行订阅，订阅后可以收到交易主推，返回0表示订阅成功
    subscribe_result = xt_trader.subscribe(acc)
    print('对交易回调进行订阅，订阅后可以收到交易主推，返回0表示订阅成功', subscribe_result)

    #订阅的品种列表
    code_list = ['600000.SH', '000001.SZ']
    #遍历品种 下载历史k线 订阅当日行情
    for code in code_list:
        xtdata.download_history_data(code, period='1d', start_time='20200101')
        xtdata.subscribe_quote(code, '1d', callback = None)

    while True:
        now = datetime.datetime.now()
        now_time = now.strftime('%H%M%S')
        if not '093000' <= now_time < '150000':
            print(f"{now} 非交易时间 循环退出")
            break
        #取k线数据
        data = xtdata.get_market_data_ex(['close'], code_list, period= '1d', start_time= '20240101')
        #判断交易
        f(data)
        #每次循环 睡眠三秒后继续
        time.sleep(3)

    # 阻塞主线程退出
    xt_trader.run_forever()
    # 如果使用vscode pycharm等本地编辑器 可以进入交互模式 方便调试 （把上一行的run_forever注释掉 否则不会执行到这里）
    interact()
```

### 交易接口重连

该示例演示交易连接断开时重连的代码处理。

提示

1. 该示例 **不是线程安全** 的，仅演示断开连接时应该怎么处理重连代码，实际使用时请注意避免潜在的问题
2. 本策略只用于提供策略写法及参考，若您直接进行实盘下单，造成损失本网站不负担责任。

```python
#本文用一个均线策略演示交易连接断开时怎么处理交易接口重连
# 策略本身不严谨，不能作为实盘策略或者参考策略，本策略仅是演示重连用法
import time
from xtquant.xttrader import XtQuantTrader, XtQuantTraderCallback
from xtquant.xttype import StockAccount
from xtquant import xtconstant
from xtquant import xtdata

class MyXtQuantTraderCallback(XtQuantTraderCallback):
    # 更多说明见 http://dict.thinktrader.net/nativeApi/xttrader.html?id=I3DJ97#%E5%A7%94%E6%89%98xtorder
    def on_disconnected(self):
        """
        连接断开
        :return:
        """
        print("connection lost, 交易接口断开，即将重连")
        global xt_trader
        xt_trader = None

    def on_stock_order(self, order):
        print(f'委托回报: 股票代码:{order.stock_code} 账号:{order.account_id}, 订单编号:{order.order_id} 柜台合同编号:{order.order_sysid}
            委托状态:{order.order_status} 成交数量:{order.order_status} 委托数量:{order.order_volume} 已成数量：{order.traded_volume}')

    def on_stock_trade(self, trade):
        print(f'成交回报: 股票代码:{trade.stock_code} 账号:{trade.account_id}, 订单编号:{trade.order_id} 柜台合同编号:{trade.order_sysid}
            成交编号:{trade.traded_id} 成交数量:{trade.traded_volume} 委托数量:{trade.direction} ')

    def on_order_error(self, order_error):
        print(f"报单失败： 订单编号：{order_error.order_id} 下单失败具体信息:{order_error.error_msg} 委托备注:{order_error.order_remark}")

    def on_cancel_error(self, cancel_error):
        print(f"撤单失败: 订单编号：{cancel_error.order_id} 失败具体信息:{cancel_error.error_msg} 市场：{cancel_error.market}")

    def on_order_stock_async_response(self, response):
        print(f"异步下单的请求序号:{response.seq}, 订单编号：{response.order_id} ")

    def on_account_status(self, status):
        print(f"账号状态发生变化， 账号:{status.account_id} 最新状态：{status.status}")

def create_trader(xt_acc,path, session_id):
    trader = XtQuantTrader(path, session_id,callback=MyXtQuantTraderCallback())
    trader.start()
    connect_result = trader.connect()
    trader.subscribe(xt_acc)
    return trader if connect_result == 0 else None

def try_connect(xt_acc,path):
    session_id_range = [i for i in range(100, 120)]

    import random
    random.shuffle(session_id_range)

    # 遍历尝试session_id列表尝试连接
    for session_id in session_id_range:
        trader = create_trader(xt_acc,path, session_id)
        if trader:
            print('连接成功，session_id:{}', session_id)
            return trader
        else:
            print('连接失败，session_id:{}，继续尝试下一个id', session_id)
            continue

    print('所有id都尝试后仍失败，放弃连接')
    return None

def get_xttrader(xt_acc,path):
    global xt_trader
    if xt_trader is None:
        xt_trader = try_connect(xt_acc,path)
    return xt_trader

if __name__ == "__main__":

    # 注意实际连接XtQuantTrader时不要写类似while True 这种无限循环的尝试，因为每次连接都会用session_id创建一个对接文件，这样就会占满硬盘导致电脑运行异常
    # 要控制session_id在有限的范围内尝试，这里提供10个session_id供重连尝试
    # 当所有session_id都尝试后，程序会抛出异常。实际使用过程中当session_id用完时，可以增加邮件等通知方式提醒人工处理

    #指定客户端所在路径
    path = 'E:\\qmt\\userdata_mini'
    xt_trader = None
    xt_acc = StockAccount('2000204')
    xt_trader = get_xttrader(xt_acc,path)
    if not xt_trader:
        raise Exception('交易接口连接失败')
    print('交易接口连接成功， 策略开始')

    stock = '513050.SH'
    xtdata.subscribe_quote(stock, '5m','','',count=-1)
    time.sleep(1)
    order_record = []
    while '093000'<=time.strftime('%H%M%S')<'150000':
        time.sleep(3)
        xt_trader = get_xttrader(xt_acc,path)

        price = xtdata.get_market_data_ex(['close'],[stock],period='5m',)[stock]
        #计算均线
        ma5 = price['close'].rolling(5).mean()
        ma10 = price['close'].rolling(10).mean()

        if ma5.iloc[-1]>ma5.iloc[-10]:
            t = price.index[-1]
            order_flag = (t, '买')
            if order_flag not in order_record: #防止重复下单
                print(f'发起买入 {stock}  k线时间:{t}')

                # 用最新价买100股
                xt_trader.order_stock_async(xt_acc, stock, xtconstant.STOCK_BUY,100,xtconstant.LATEST_PRICE,0)
                order_record.append(order_flag)
        elif ma5.iloc[-1]<ma5[-10]:
            t = price.index[-1]
            order_flag = (t, '卖')
            if order_flag not in order_record: #防止重复下单
                print(f'发起卖出 {stock} k线时间:{t}')
                # 用最新价买100股
                xt_trader.order_stock_async(xt_acc, stock, xtconstant.STOCK_SELL,100,xtconstant.LATEST_PRICE,0)

                order_record.append(order_flag)
```

### 指定session id范围连接交易

该示例演示指定session重试连接次数的代码处理。

```py

#coding:utf-8

def connect(path, session):
    from xtquant import xttrader

    trader = xttrader.XtQuantTrader(path, session)
    trader.start()

    connect_result = trader.connect()
    return trader if connect_result == 0 else None

def try_connect_range():
    # 随机 session_id 的待尝试列表
    # 100以内的id保留
    ids = [i for i in range(100, 200)]

    import random
    random.shuffle(ids)

    # 要连接到的对接路径
    path = r'userdata_mini'

    # 遍历id列表尝试连接
    for session_id in ids:
        print(f'尝试id:{session_id}')
        trader = connect(path, session_id)

        if trader:
            print('连接成功')
            return trader
        else:
            print('连接失败，继续尝试下一个id')
            continue

    # 所有id都尝试后仍失败，放弃连接
    raise Exception('XtQuantTrader 连接失败,请重试')

try:
    trader = try_connect_range()
except Exception as e:
    import traceback
    print(e, traceback.format_exc())

import time
while True:
    print('.', end = '')
    time.sleep(2)
```

### 信用账号执行还款

本示例用于展示如何使用xtquant库对信用账号执行还款的操作

提示

本策略只用于提供策略写法及参考，若您直接进行实盘下单，造成损失本网站不负担责任。

```py
#coding=utf-8
from xtquant.xttrader import XtQuantTrader, XtQuantTraderCallback
from xtquant.xttype import StockAccount
from xtquant import xtconstant

# 修改参数
# path为mini qmt客户端安装目录下userdata_mini路径
path = 'E:\\qmt\\userdata_mini'
# session_id为会话编号，策略使用方对于不同的Python策略需要使用不同的会话编号
session_id = 1234567
repay_money = 1000.51  # 元，需要执行还款的金额

class MyXtQuantTraderCallback(XtQuantTraderCallback):
    def on_disconnected(self):
        """
        连接断开
        :return:
        """
        print("connection lost")
    def on_stock_order(self, order):
        """
        委托回报推送
        :param order: XtOrder对象
        :return:
        """
        print("on order callback:")
        print(order.stock_code, order.order_status, order.order_sysid)
    def on_stock_asset(self, asset):
        """
        资金变动推送
        :param asset: XtAsset对象
        :return:
        """
        print("on asset callback")
        print(asset.account_id, asset.cash, asset.total_asset)
    def on_stock_trade(self, trade):
        """
        成交变动推送
        :param trade: XtTrade对象
        :return:
        """
        print("on trade callback")
        print(trade.account_id, trade.stock_code, trade.order_id)
    def on_order_error(self, order_error):
        """
        委托失败推送
        :param order_error:XtOrderError 对象
        :return:
        """
        print("on order_error callback")
        print(order_error.order_id, order_error.error_id, order_error.error_msg)
    def on_cancel_error(self, cancel_error):
        """
        撤单失败推送
        :param cancel_error: XtCancelError 对象
        :return:
        """
        print("on cancel_error callback")
        print(cancel_error.order_id, cancel_error.error_id, cancel_error.error_msg)
    def on_order_stock_async_response(self, response):
        """
        异步下单回报推送
        :param response: XtOrderResponse 对象
        :return:
        """
        print("on_order_stock_async_response")
        print(response.account_id, response.order_id, response.seq)
    def on_account_status(self, status):
        """
        :param response: XtAccountStatus 对象
        :return:
        """
        print("on_account_status")
        print(status.account_id, status.account_type, status.status)

if __name__ == "__main__":
    print("demo test")

    xt_trader = XtQuantTrader(path, session_id)
    # 创建资金账号为1000000365的证券账号对象
    acc = StockAccount('200035', 'CREDIT')
    # StockAccount可以用第二个参数指定账号类型，如沪港通传'HUGANGTONG'，深港通传'SHENGANGTONG'
    # acc = StockAccount('1000000365','STOCK')
    # 创建交易回调类对象，并声明接收回调
    callback = MyXtQuantTraderCallback()
    xt_trader.register_callback(callback)
    # 启动交易线程
    xt_trader.start()
    # 建立交易连接，返回0表示连接成功
    connect_result = xt_trader.connect()
    if connect_result != 0:
        import sys
        sys.exit('连接失败，程序即将退出 %d'%connect_result)
    # 对交易回调进行订阅，订阅后可以收到交易主推，返回0表示订阅成功
    subscribe_result = xt_trader.subscribe(acc)
    if subscribe_result != 0:
        print('账号订阅失败 %d'%subscribe_result)
    print(subscribe_result)
    stock_code = '600000.SH'  # 参数占位用，任意股票代码都可以
    volume = 200  # 参数占位用，任意数量
    # 使用指定价下单，接口返回订单编号，后续可以用于撤单操作以及查询委托状态
    fix_result_order_id = xt_trader.order_stock(acc, stock_code, xtconstant.CREDIT_DIRECT_CASH_REPAY, repay_money, xtconstant.FIX_PRICE, -1, 'strategy_name', 'remark')

    # 阻塞线程，接收交易推送
    xt_trader.run_forever()
```

### 下单后通过回调撤单

```py
import pandas as pd
import numpy as np
import datetime
from xtquant import xtdata,xttrader
from xtquant.xttype import StockAccount
from xtquant import xtconstant
from xtquant.xttrader import XtQuantTraderCallback
import sys
import time

"""
异步下单委托流程为
1.order_stock_async发出委托
2.回调on_order_stock_async_response收到回调信息
3.回调on_stock_order收到委托信息
4.回调cancel_order_stock_sysid_async发出异步撤单指令
5.回调on_cancel_order_stock_async_response收到撤单回调信息
6.回调on_stock_order收到委托信息
"""
strategy_name = "委托撤单测试"

class MyXtQuantTraderCallback(XtQuantTraderCallback):
    # 用于接收回调信息的类
    def on_stock_order(self, order):
        """
        委托回报推送
        :param order: XtOrder对象
        :return:
        """
        # 属性赋值
        account_type = order.account_type  # 账号类型
        account_id = order.account_id  # 资金账号
        stock_code = order.stock_code  # 证券代码，例如"600000.SH"
        order_id = order.order_id  # 订单编号
        order_sysid = order.order_sysid  # 柜台合同编号
        order_time = order.order_time  # 报单时间
        order_type = order.order_type  # 委托类型，参见数据字典
        order_volume = order.order_volume  # 委托数量
        price_type = order.price_type  # 报价类型，该字段在返回时为柜台返回类型，不等价于下单传入的price_type，枚举值不一样功能一样，参见数据字典
        price = order.price  # 委托价格
        traded_volume = order.traded_volume  # 成交数量
        traded_price = order.traded_price  # 成交均价
        order_status = order.order_status  # 委托状态，参见数据字典
        status_msg = order.status_msg  # 委托状态描述，如废单原因
        strategy_name = order.strategy_name  # 策略名称
        order_remark = order.order_remark  # 委托备注
        direction = order.direction  # 多空方向，股票不适用；参见数据字典
        offset_flag = order.offset_flag  # 交易操作，用此字段区分股票买卖，期货开、平仓，期权买卖等；参见数据字典

        # 打印输出
        print(f"""
        =============================
                委托信息
        =============================
        账号类型: {order.account_type},
        资金账号: {order.account_id},
        证券代码: {order.stock_code},
        订单编号: {order.order_id},
        柜台合同编号: {order.order_sysid},
        报单时间: {order.order_time},
        委托类型: {order.order_type},
        委托数量: {order.order_volume},
        报价类型: {order.price_type},
        委托价格: {order.price},
        成交数量: {order.traded_volume},
        成交均价: {order.traded_price},
        委托状态: {order.order_status},
        委托状态描述: {order.status_msg},
        策略名称: {order.strategy_name},
        委托备注: {order.order_remark},
        多空方向: {order.direction},
        交易操作: {order.offset_flag}
        """)
        if order.strategy_name == strategy_name:
            # 该委托是由本策略发出
            ssid = order.order_sysid
            status = order.order_status
            market = order.stock_code.split(".")[1]
            # print(ssid)
            if ssid and status in [50,55]:
                ## 使用cancel_order_stock_sysid_async时，投研端market参数可以填写为0，券商端按实际情况填写
                print(xt_trade.cancel_order_stock_sysid_async(account,0,ssid))

    def on_stock_trade(self, trade):
        """
        成交变动推送
        :param trade: XtTrade对象
        :return:
        """
        print(datetime.datetime.now(), '成交回调', trade.order_remark,trade.stock_code,trade.traded_volume,trade.offset_flag)

    def on_order_stock_async_response(self, response):
        """
        异步下单回报推送
        :param response: XtOrderResponse 对象
        :return:
        """

        print(datetime.datetime.now(),'异步下单编号为：',response.seq)

    def on_cancel_order_stock_async_response(self, response):
        """
        异步撤单回报
        :param response: XtCancelOrderResponse 对象
        :return:
        """
        account_type = response.account_type # 账号类型
        account_id = response.account_id  # 资金账号
        order_id = response.order_id  # 订单编号
        order_sysid = response.order_sysid  # 柜台委托编号
        cancel_result = response.cancel_result  # 撤单结果
        seq = response.seq  # 异步撤单的请求序号

        print(f"""
            ===========================
                   异步撤单回调信息
            ===========================
            账号类型: {response.account_type},
            资金账号: {response.account_id},
            订单编号: {response.order_id},
            柜台委托编号: {response.order_sysid},
            撤单结果: {response.cancel_result},
            异步撤单的请求序号: {response.seq}""")
        pass

callback = MyXtQuantTraderCallback()
# 填投研端的期货账号
account = StockAccount("1000024",account_type = "FUTURE")
# 填写投研端的股票账号
# account = StockAccount("2000567")
# 填投研端的userdata路径,miniqmt指定到userdata_mini
xt_trade = xttrader.XtQuantTrader(r"C:\\Program Files\\测试1\\迅投极速交易终端睿智融科版\\userdata",int(time.time()))
# 注册接受回调
xt_trade.register_callback(callback)
# 启动交易线程
xt_trade.start()
# 链接交易
connect_result = xt_trade.connect()
# 订阅账号信息，接受这个账号的回调，回调是账号维度的
subscribe_result = xt_trade.subscribe(account)
print(subscribe_result)

code = "rb2410.SF"
# code = "000001.SZ"

tick = xtdata.get_full_tick([code])[code]

last_price = tick["lastPrice"] # 最新价

ask_price = round(tick["askPrice"][0],3) # 卖方1档价
bid_price = round(tick["bidPrice"][4],3) # 买方5档价

symbol_info = xtdata.get_instrument_detail(code)

up_limit = symbol_info["UpStopPrice"]
down_limit = symbol_info["DownStopPrice"]

lots = 1
res_id = xt_trade.order_stock_async(account, code, xtconstant.FUTURE_OPEN_LONG, lots, xtconstant.FIX_PRICE, down_limit, strategy_name, "跌停价/固定手数")

# lots = 100
# res_id = xt_trade.order_stock_async(account, code, xtconstant.STOCK_BUY, lots, xtconstant.FIX_PRICE, bid_price, strategy_name, "跌停价/固定手数")

xtdata.run()
```