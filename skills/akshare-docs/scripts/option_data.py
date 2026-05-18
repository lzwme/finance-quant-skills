#!/usr/bin/env python3
"""AKShare 期权数据获取脚本
支持期权历史数据、实时行情等"""
import sys
import json
import argparse
import pandas as pd
import akshare as ak

def get_option_hist_dce(symbol="豆粕期权"):
    """获取大商所期权历史数据"""
    try:
        df = ak.option_hist_dce(symbol=symbol)
        return {
            "type": "option_hist_dce",
            "symbol": symbol,
            "data": df.to_dict('records'),
            "count": len(df)
        }
    except Exception as e:
        return {"error": f"获取大商所期权历史数据失败: {str(e)}"}

def get_option_hist_czce(symbol="白糖期权"):
    """获取郑商所期权历史数据"""
    try:
        df = ak.option_hist_czce(symbol=symbol)
        return {
            "type": "option_hist_czce",
            "symbol": symbol,
            "data": df.to_dict('records'),
            "count": len(df)
        }
    except Exception as e:
        return {"error": f"获取郑商所期权历史数据失败: {str(e)}"}

def get_option_hist_shfe(symbol="铜期权"):
    """获取上期所期权历史数据"""
    try:
        df = ak.option_hist_shfe(symbol=symbol)
        return {
            "type": "option_hist_shfe",
            "symbol": symbol,
            "data": df.to_dict('records'),
            "count": len(df)
        }
    except Exception as e:
        return {"error": f"获取上期所期权历史数据失败: {str(e)}"}

def get_option_sse_spot_price(symbol="510050"):
    """获取上证50ETF期权实时行情"""
    try:
        df = ak.option_sse_spot_price(symbol=symbol)
        return {
            "type": "option_sse_spot",
            "symbol": symbol,
            "data": df.to_dict('records'),
            "count": len(df)
        }
    except Exception as e:
        return {"error": f"获取上证50ETF期权实时行情失败: {str(e)}"}

def get_option_sse_underlying_spot_price(symbol="510050"):
    """获取上证50ETF期权标的实时行情"""
    try:
        df = ak.option_sse_underlying_spot_price(symbol=symbol)
        return {
            "type": "option_sse_underlying_spot",
            "symbol": symbol,
            "data": df.to_dict('records'),
            "count": len(df)
        }
    except Exception as e:
        return {"error": f"获取期权标的实时行情失败: {str(e)}"}

def get_option_sse_minute_sina(symbol="510050"):
    """获取上证50ETF期权分钟数据"""
    try:
        df = ak.option_sse_minute_sina(symbol=symbol)
        return {
            "type": "option_sse_minute",
            "symbol": symbol,
            "data": df.to_dict('records'),
            "count": len(df)
        }
    except Exception as e:
        return {"error": f"获取期权分钟数据失败: {str(e)}"}

def get_option_sse_daily_sina(symbol="510050"):
    """获取上证50ETF期权日K线数据"""
    try:
        df = ak.option_sse_daily_sina(symbol=symbol)
        return {
            "type": "option_sse_daily",
            "symbol": symbol,
            "data": df.to_dict('records'),
            "count": len(df)
        }
    except Exception as e:
        return {"error": f"获取期权日K线数据失败: {str(e)}"}

def get_option_finance_board(symbol="510050"):
    """获取期权财务指标"""
    try:
        df = ak.option_finance_board(symbol=symbol)
        return {
            "type": "option_finance_board",
            "symbol": symbol,
            "data": df.to_dict('records'),
            "count": len(df)
        }
    except Exception as e:
        return {"error": f"获取期权财务指标失败: {str(e)}"}

def main():
    parser = argparse.ArgumentParser(description='AKShare 期权数据获取')
    parser.add_argument('--type', required=True,
                       choices=['hist_dce', 'hist_czce', 'hist_shfe', 'sse_spot',
                               'sse_underlying', 'sse_minute', 'sse_daily', 'finance_board'],
                       help='数据类型')
    parser.add_argument('--symbol', default='510050', help='期权代码或名称')

    args = parser.parse_args()

    if args.type == 'hist_dce':
        result = get_option_hist_dce(args.symbol)
    elif args.type == 'hist_czce':
        result = get_option_hist_czce(args.symbol)
    elif args.type == 'hist_shfe':
        result = get_option_hist_shfe(args.symbol)
    elif args.type == 'sse_spot':
        result = get_option_sse_spot_price(args.symbol)
    elif args.type == 'sse_underlying':
        result = get_option_sse_underlying_spot_price(args.symbol)
    elif args.type == 'sse_minute':
        result = get_option_sse_minute_sina(args.symbol)
    elif args.type == 'sse_daily':
        result = get_option_sse_daily_sina(args.symbol)
    elif args.type == 'finance_board':
        result = get_option_finance_board(args.symbol)
    else:
        result = {"error": f"未知类型: {args.type}"}

    print(json.dumps(result, ensure_ascii=False, indent=2, default=str))

if __name__ == "__main__":
    main()
