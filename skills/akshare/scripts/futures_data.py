#!/usr/bin/env python3
"""AKShare 期货数据获取脚本
支持期货行情、历史K线、库存数据等"""
import sys
import json
import argparse
import pandas as pd
from akshare import get_futures_daily
import akshare as ak

def get_futures_daily_data(start_date, end_date, market="CFFEX"):
    """获取期货日线数据"""
    try:
        df = get_futures_daily(
            start_date=start_date,
            end_date=end_date,
            market=market
        )
        return {
            "market": market,
            "start_date": start_date,
            "end_date": end_date,
            "data": df.to_dict('records'),
            "count": len(df)
        }
    except Exception as e:
        return {"error": f"获取期货日线数据失败: {str(e)}"}

def get_futures_spot():
    """获取期货实时行情"""
    try:
        df = ak.futures_zh_spot()
        return {
            "data": df.to_dict('records'),
            "count": len(df),
            "update_time": pd.Timestamp.now().strftime("%Y-%m-%d %H:%M:%S")
        }
    except Exception as e:
        return {"error": f"获取期货实时行情失败: {str(e)}"}

def get_futures_inventory(symbol="豆一"):
    """获取期货库存数据"""
    try:
        df = ak.futures_inventory_99(symbol=symbol)
        return {
            "symbol": symbol,
            "data": df.to_dict('records'),
            "count": len(df)
        }
    except Exception as e:
        return {"error": f"获取期货库存数据失败: {str(e)}"}

def get_cffex_daily(start_date, end_date):
    """获取中金所期货数据"""
    return get_futures_daily_data(start_date, end_date, "CFFEX")

def get_shfe_daily(start_date, end_date):
    """获取上期所期货数据"""
    return get_futures_daily_data(start_date, end_date, "SHFE")

def get_dce_daily(start_date, end_date):
    """获取大商所期货数据"""
    return get_futures_daily_data(start_date, end_date, "DCE")

def get_czce_daily(start_date, end_date):
    """获取郑商所期货数据"""
    return get_futures_daily_data(start_date, end_date, "CZCE")

def get_ine_daily(start_date, end_date):
    """获取上海国际能源交易中心期货数据"""
    return get_futures_daily_data(start_date, end_date, "INE")

def get_gfex_daily(start_date, end_date):
    """获取广期所期货数据"""
    return get_futures_daily_data(start_date, end_date, "GFEX")

def get_futures_contracts(exchange="CFFEX"):
    """获取期货合约列表"""
    try:
        # 获取实时行情来提取合约信息
        df = ak.futures_zh_spot()
        # 根据交易所筛选
        if exchange == "CFFEX":
            contracts = df[df['symbol'].str.contains('IF|IC|IH|T|TF|TS')]
        elif exchange == "SHFE":
            contracts = df[df['symbol'].str.contains('AU|AG|CU|AL|ZN|PB|NI|SN|RB|WR|HC')]
        elif exchange == "DCE":
            contracts = df[df['symbol'].str.contains('C|CS|A|M|Y|B|P|FB|BB|L|V|PP')]
        elif exchange == "CZCE":
            contracts = df[df['symbol'].str.contains('SR|CF|TA|OI|RI|WH|RS|RM|JR|LR|SF|SM')]
        else:
            contracts = df

        return {
            "exchange": exchange,
            "contracts": contracts[['symbol', 'contract']].drop_duplicates().to_dict('records'),
            "count": len(contracts)
        }
    except Exception as e:
        return {"error": f"获取期货合约列表失败: {str(e)}"}

def get_futures_main_contract(symbol="IF"):
    """获取期货主力合约"""
    try:
        df = ak.futures_main_sure_em(symbol=symbol)
        return {
            "symbol": symbol,
            "main_contract": df.to_dict('records'),
            "count": len(df)
        }
    except Exception as e:
        return {"error": f"获取期货主力合约失败: {str(e)}"}

def main():
    parser = argparse.ArgumentParser(description='AKShare 期货数据获取')
    parser.add_argument('--type', required=True,
                       choices=['daily', 'spot', 'inventory', 'contracts', 'main_contract',
                               'cffex', 'shfe', 'dce', 'czce', 'ine', 'gfex'],
                       help='数据类型')
    parser.add_argument('--start', required=True, help='开始日期 YYYYMMDD')
    parser.add_argument('--end', required=True, help='结束日期 YYYYMMDD')
    parser.add_argument('--market', default='CFFEX',
                       choices=['CFFEX', 'SHFE', 'DCE', 'CZCE', 'INE', 'GFEX'],
                       help='交易所')
    parser.add_argument('--symbol', help='期货品种或合约代码')

    args = parser.parse_args()

    if args.type == 'daily':
        result = get_futures_daily_data(args.start, args.end, args.market)
    elif args.type == 'spot':
        result = get_futures_spot()
    elif args.type == 'inventory':
        symbol = args.symbol if args.symbol else "豆一"
        result = get_futures_inventory(symbol)
    elif args.type == 'contracts':
        market = args.market if args.market else "CFFEX"
        result = get_futures_contracts(market)
    elif args.type == 'main_contract':
        symbol = args.symbol if args.symbol else "IF"
        result = get_futures_main_contract(symbol)
    elif args.type == 'cffex':
        result = get_cffex_daily(args.start, args.end)
    elif args.type == 'shfe':
        result = get_shfe_daily(args.start, args.end)
    elif args.type == 'dce':
        result = get_dce_daily(args.start, args.end)
    elif args.type == 'czce':
        result = get_czce_daily(args.start, args.end)
    elif args.type == 'ine':
        result = get_ine_daily(args.start, args.end)
    elif args.type == 'gfex':
        result = get_gfex_daily(args.start, args.end)
    else:
        result = {"error": f"未知类型: {args.type}"}

    print(json.dumps(result, ensure_ascii=False, indent=2, default=str))

if __name__ == "__main__":
    main()
