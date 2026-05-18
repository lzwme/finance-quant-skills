#!/usr/bin/env python3
"""AKShare 股票数据获取脚本
支持A股、港股、美股的历史K线、实时行情、财务数据等"""
import sys
import json
import argparse
import pandas as pd
import akshare as ak

def get_stock_hist(symbol, period="daily", start_date=None, end_date=None, adjust=""):
    """获取股票历史K线数据"""
    try:
        df = ak.stock_zh_a_hist(
            symbol=symbol,
            period=period,
            start_date=start_date,
            end_date=end_date,
            adjust=adjust
        )
        return {
            "symbol": symbol,
            "period": period,
            "adjust": adjust,
            "data": df.to_dict('records'),
            "count": len(df)
        }
    except Exception as e:
        return {"error": f"获取历史数据失败: {str(e)}"}

def get_stock_hist_min(symbol, period="5", start_date=None, end_date=None, adjust=""):
    """获取股票分钟K线数据"""
    try:
        df = ak.stock_zh_a_hist_min_em(
            symbol=symbol,
            period=period,
            start_date=start_date,
            end_date=end_date,
            adjust=adjust
        )
        return {
            "symbol": symbol,
            "period": f"{period}min",
            "adjust": adjust,
            "data": df.to_dict('records'),
            "count": len(df)
        }
    except Exception as e:
        return {"error": f"获取分钟数据失败: {str(e)}"}

def get_stock_spot():
    """获取全部A股实时行情"""
    try:
        df = ak.stock_zh_a_spot_em()
        return {
            "data": df.to_dict('records'),
            "count": len(df),
            "update_time": pd.Timestamp.now().strftime("%Y-%m-%d %H:%M:%S")
        }
    except Exception as e:
        return {"error": f"获取实时行情失败: {str(e)}"}

def get_stock_info(symbol):
    """获取个股基本信息"""
    try:
        df = ak.stock_individual_info_em(symbol=symbol)
        return {
            "symbol": symbol,
            "info": df.to_dict('records')[0] if len(df) > 0 else {}
        }
    except Exception as e:
        return {"error": f"获取个股信息失败: {str(e)}"}

def get_stock_fundamental(symbol):
    """获取股票基本面数据"""
    try:
        df = ak.stock_fundamental(symbol=symbol)
        return {
            "symbol": symbol,
            "fundamental": df.to_dict('records')
        }
    except Exception as e:
        return {"error": f"获取基本面数据失败: {str(e)}"}

def get_stock_valuation(symbol):
    """获取股票估值指标"""
    try:
        df = ak.stock_valuation(symbol=symbol)
        return {
            "symbol": symbol,
            "valuation": df.to_dict('records')
        }
    except Exception as e:
        return {"error": f"获取估值数据失败: {str(e)}"}

def get_hk_stock_hist(symbol, period="daily", start_date=None, end_date=None, adjust=""):
    """获取港股历史数据"""
    try:
        df = ak.stock_hk_hist(
            symbol=symbol,
            period=period,
            start_date=start_date,
            end_date=end_date,
            adjust=adjust
        )
        return {
            "symbol": symbol,
            "market": "hk",
            "period": period,
            "adjust": adjust,
            "data": df.to_dict('records'),
            "count": len(df)
        }
    except Exception as e:
        return {"error": f"获取港股历史数据失败: {str(e)}"}

def get_hk_stock_spot():
    """获取港股实时行情"""
    try:
        df = ak.stock_hk_spot_em()
        return {
            "market": "hk",
            "data": df.to_dict('records'),
            "count": len(df)
        }
    except Exception as e:
        return {"error": f"获取港股实时行情失败: {str(e)}"}

def get_us_stock_hist(symbol, adjust="qfq"):
    """获取美股历史数据"""
    try:
        df = ak.stock_us_daily(symbol=symbol, adjust=adjust)
        return {
            "symbol": symbol,
            "market": "us",
            "adjust": adjust,
            "data": df.to_dict('records'),
            "count": len(df)
        }
    except Exception as e:
        return {"error": f"获取美股历史数据失败: {str(e)}"}

def get_us_stock_spot():
    """获取美股实时行情"""
    try:
        df = ak.stock_us_spot_em()
        return {
            "market": "us",
            "data": df.to_dict('records'),
            "count": len(df)
        }
    except Exception as e:
        return {"error": f"获取美股实时行情失败: {str(e)}"}

def get_market_overview():
    """获取市场概览"""
    try:
        df = ak.stock_zh_a_spot_em()

        # 计算市场统计
        total_stocks = len(df)
        up_stocks = len(df[df['涨跌幅'].astype(float) > 0])
        down_stocks = len(df[df['涨跌幅'].astype(float) < 0])
        flat_stocks = len(df[df['涨跌幅'].astype(float) == 0])

        # 获取涨跌停股票
        limit_up = len(df[df['涨跌幅'].astype(float) >= 9.5])
        limit_down = len(df[df['涨跌幅'].astype(float) <= -9.5])

        # 获取涨跌榜
        df_sorted = df.sort_values('涨跌幅', ascending=False)
        top_gainers = df_sorted.head(10)[['代码', '名称', '最新价', '涨跌幅']].to_dict('records')
        top_losers = df_sorted.tail(10)[['代码', '名称', '最新价', '涨跌幅']].to_dict('records')

        return {
            "market_stats": {
                "total_stocks": total_stocks,
                "up_stocks": up_stocks,
                "down_stocks": down_stocks,
                "flat_stocks": flat_stocks,
                "limit_up": limit_up,
                "limit_down": limit_down
            },
            "top_gainers": top_gainers,
            "top_losers": top_losers,
            "update_time": pd.Timestamp.now().strftime("%Y-%m-%d %H:%M:%S")
        }
    except Exception as e:
        return {"error": f"获取市场概览失败: {str(e)}"}

def main():
    parser = argparse.ArgumentParser(description='AKShare 股票数据获取')
    parser.add_argument('--type', required=True,
                       choices=['hist', 'hist_min', 'spot', 'info', 'fundamental', 'valuation',
                               'hk_hist', 'hk_spot', 'us_hist', 'us_spot', 'overview'],
                       help='数据类型')
    parser.add_argument('--symbol', help='股票代码')
    parser.add_argument('--period', default='daily',
                       choices=['daily', 'weekly', 'monthly'],
                       help='周期')
    parser.add_argument('--start', help='开始日期 YYYYMMDD')
    parser.add_argument('--end', help='结束日期 YYYYMMDD')
    parser.add_argument('--adjust', default='',
                       choices=['', 'qfq', 'hfq'],
                       help='复权类型')

    args = parser.parse_args()

    if args.type == 'hist':
        result = get_stock_hist(args.symbol, args.period, args.start, args.end, args.adjust)
    elif args.type == 'hist_min':
        period = args.period if args.period in ['1', '5', '15', '30', '60'] else '5'
        result = get_stock_hist_min(args.symbol, period, args.start, args.end, args.adjust)
    elif args.type == 'spot':
        result = get_stock_spot()
    elif args.type == 'info':
        result = get_stock_info(args.symbol)
    elif args.type == 'fundamental':
        result = get_stock_fundamental(args.symbol)
    elif args.type == 'valuation':
        result = get_stock_valuation(args.symbol)
    elif args.type == 'hk_hist':
        result = get_hk_stock_hist(args.symbol, args.period, args.start, args.end, args.adjust)
    elif args.type == 'hk_spot':
        result = get_hk_stock_spot()
    elif args.type == 'us_hist':
        result = get_us_stock_hist(args.symbol, args.adjust)
    elif args.type == 'us_spot':
        result = get_us_stock_spot()
    elif args.type == 'overview':
        result = get_market_overview()
    else:
        result = {"error": f"未知类型: {args.type}"}

    print(json.dumps(result, ensure_ascii=False, indent=2, default=str))

if __name__ == "__main__":
    main()
