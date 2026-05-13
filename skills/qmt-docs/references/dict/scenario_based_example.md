---
url: "https://dict.thinktrader.net/dictionary/scenario_based_example.html"
title: "场景化示例 | 迅投知识库"
---

## 场景化示例

### 判断市场状态，获取市场最新分钟K线

```
import pandas as pd
from xtquant import xtdata

market = 'SH'

# 获取市场的品种列表
sl = xtdata.get_stock_list_in_sector(market)

def on_data(datas):
    # 获取当前市场时间
    # 根据推送的数据统计最新的tick时间作为当前市场时间
    market_time = max([datas[i]["time"] for i in datas])

    # 判断是否到达57秒，认为这时的分钟K线已经结束
    if market_time % 60 >= 57:
        print('reach 57 seconds, market_time:' + str(market_time))

        # 获取这个时刻的分钟K线数据
        data = xtdata.get_full_kline([], sl, '1m')
        print(data)
    return

# 订阅全推数据
xtdata.subscribe_whole_quote([market], callback = on_data)

# 保持程序运行
xtdata.run()
```

### 盘前数据准备

```py
from xtquant import xtdata
from datetime import datetime,timedelta
import time
from tqdm import tqdm

## 交易日切换判断

def trading_date_is_change(market_list = ['SH', 'SZ']) -> bool:
    """判断交易日是否切换，当全部交易市场都完成交易日切换后，返回True

    Args:
        market_list (list, optional): 交易市场，市场分类参考 https://dict.thinktrader.net/innerApi/variable_convention.html?id=7zqjlm
    Return:
        bool
    """

    market_list = ['SH', 'SZ', 'BJ']
    ls = [0,0,0]
    now_date = datetime.now().date()
    for i in range(len(market_list)):
        market = market_list[i]
        trading_dates = xtdata.get_trading_dates(market)
        if trading_dates:
            if datetime.fromtimestamp(trading_dates[-1] / 1000).date() == now_date:
                print(f'trading date switch success, market: {market}, trading date: {now_date}')
                ls[i] = 1
            else:
                print(f"{market} -- 交易日未切换")

    if all(ls):
        return True
    else:
        return False

def update_sector_data() -> None:
    """更新静态数据，包含板块数据
    静态数据是指在当天交易日内不会变化，或基本不会变化的数据（如合约信息可能会盘中少量更新，可忽略）
        交易日列表 合约列表（合约信息）    <- 当日自动更新
        复权数据    <- 当日自动更新
        板块列表、板块成分   <- 需要每天执行下载
    """

    xtdata.download_sector_data() # 下载当日板块数据
    xtdata.download_index_weight() # 更新指数权重数据
    xtdata.download_history_contracts() # 下载过期合约数据，包含退市标的信息


def update_kline_data(sector_name:str ,period_list:list, start_time:str = "", end_time:str = "", incrementally:bool = True) -> None:
    """xtquant历史数据都是以压缩形式存储在本地的，get_market_data函数与get_market_data_ex函数将会自动拼接本地历史行情与服务器实时行情

    Args:
        sector_name (str): 板块名称，如"沪深A股"
        period_list (list): 支持的周期参考 https://dict.thinktrader.net/innerApi/data_function.html?id=7zqjlm#download-history-data
        start_time (str): 开始时间
            格式为 YYYYMMDD 或 YYYYMMDDhhmmss 或 ''
            例如：'20230101' '20231231235959'
            空字符串代表全部，自动扩展到完整范围
        end_time (str): 结束时间 格式同开始时间
        incrementally (bool): 是否增量下载

    Raises:
        KeyError: _description_
    """
    ls = xtdata.get_stock_list_in_sector(sector_name)
    if len(ls) == 0:
        raise KeyError("股票列表长度为0,板块可能不存在，或数据未更新")
    for period in period_list:
        for stock in tqdm(ls,f"{period} 数据"):
            xtdata.download_history_data(stock,period,start_time,end_time,incrementally)


def update_financial_data(sector_name:str) -> None:
    """
    Args:
        sector_name (str): 板块名称，如"沪深A股"
    """
    ls = xtdata.get_stock_list_in_sector(sector_name)
    for stock in tqdm(ls,f"更新财务数据"):
        xtdata.download_financial_data(stock)


def is_trade_time(trading_time_info) -> bool:
    '''
    Args:
        trading_time_info:格式需要如下
            stock : (["09:30:00","11:30:00"],["13:00:00","15:00:00"])
            future : (["09:00:00","10:15:00"],["10:30:00","11:30:00"],["13:30:00","15:00:00"],["21:00:00","26:30:00"])
    return:bool
    '''

    _now = int((datetime.datetime.now() - datetime.timedelta(hours=4)).strftime("%H%M%S"))
    for _time_list_ in trading_time_info:
        st_str = _time_list_[0]
        _sp_st = (int(st_str.split(":")[0]) - 4) * 10000 + (int(st_str.replace(":", "")) % 10000)
        et_str = _time_list_[1]
        _sp_et = (int(et_str.split(":")[0]) - 4) * 10000 + (int(et_str.replace(":", "")) % 10000)

        if _sp_st <= _now < _sp_et:
            return True
    return False

def trade_logic():
    """具体策略逻辑，写法参考 https://dict.thinktrader.net/nativeApi/code_examples.html?id=7zqjlm#%E4%BA%A4%E6%98%93%E7%A4%BA%E4%BE%8B
    """
    pass

if __name__ == "__main__":
    while not trading_date_is_change(["SH","SZ"]):
        print("休眠60s")
        time.sleep(60)
    # 更新板块信息
    update_sector_data()
    # 更新财务数据
    update_financial_data("沪深A股")
    # 更新历史K线数据
    # 当前交易日的数据来自服务器，历史交易日的数据来自本地
    # 实时K线数据需要通过subscribe_quote订阅,get_market_data_ex函数将会自动拼接本地历史行情与服务器实时行情
    update_kline_data("沪深A股",["1d"],"","",True)


    ## 非交易时间过滤
    while not is_trade_time((["09:30:00","11:30:00"],["13:00:00","15:00:00"])):
        print("非交易时间")
        time.sleep(3)

    while 1:
        # 固定3s判断一次交易逻辑
        trade_logic()
        time.sleep(3)

```