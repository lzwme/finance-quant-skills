#!/usr/bin/env python3
"""AKShare 基金数据获取脚本
支持ETF、开放式基金、基金评级等数据"""
import sys
import json
import argparse
import pandas as pd
import akshare as ak

def get_etf_spot():
    """获取ETF实时行情"""
    try:
        df = ak.fund_etf_spot_em()
        return {
            "type": "etf_spot",
            "data": df.to_dict('records'),
            "count": len(df),
            "update_time": pd.Timestamp.now().strftime("%Y-%m-%d %H:%M:%S")
        }
    except Exception as e:
        return {"error": f"获取ETF实时行情失败: {str(e)}"}

def get_etf_hist(symbol, period="daily", start_date=None, end_date=None, adjust="qfq"):
    """获取ETF历史K线数据"""
    try:
        df = ak.fund_etf_hist_em(
            symbol=symbol,
            period=period,
            start_date=start_date,
            end_date=end_date,
            adjust=adjust
        )
        return {
            "type": "etf_hist",
            "symbol": symbol,
            "period": period,
            "adjust": adjust,
            "data": df.to_dict('records'),
            "count": len(df)
        }
    except Exception as e:
        return {"error": f"获取ETF历史数据失败: {str(e)}"}

def get_open_fund_daily(symbol):
    """获取开放式基金每日净值"""
    try:
        df = ak.fund_open_fund_daily_em(symbol=symbol)
        return {
            "type": "open_fund_daily",
            "symbol": symbol,
            "data": df.to_dict('records'),
            "count": len(df)
        }
    except Exception as e:
        return {"error": f"获取开放式基金净值失败: {str(e)}"}

def get_fund_rating():
    """获取基金评级"""
    try:
        df = ak.fund_rating_all()
        return {
            "type": "fund_rating",
            "data": df.to_dict('records'),
            "count": len(df)
        }
    except Exception as e:
        return {"error": f"获取基金评级失败: {str(e)}"}

def get_fund_portfolio(symbol):
    """获取基金持仓信息"""
    try:
        df = ak.fund_portfolio_hold_em(symbol=symbol)
        return {
            "type": "fund_portfolio",
            "symbol": symbol,
            "data": df.to_dict('records'),
            "count": len(df)
        }
    except Exception as e:
        return {"error": f"获取基金持仓失败: {str(e)}"}

def get_fund_manager():
    """获取基金经理信息"""
    try:
        df = ak.fund_manager()
        return {
            "type": "fund_manager",
            "data": df.to_dict('records'),
            "count": len(df)
        }
    except Exception as e:
        return {"error": f"获取基金经理信息失败: {str(e)}"}

def get_money_fund():
    """获取货币基金信息"""
    try:
        df = ak.fund_money_fund_em()
        return {
            "type": "money_fund",
            "data": df.to_dict('records'),
            "count": len(df)
        }
    except Exception as e:
        return {"error": f"获取货币基金信息失败: {str(e)}"}

def get_fund_scale():
    """获取基金规模信息"""
    try:
        df = ak.fund_scale_open_em()
        return {
            "type": "fund_scale",
            "data": df.to_dict('records'),
            "count": len(df)
        }
    except Exception as e:
        return {"error": f"获取基金规模信息失败: {str(e)}"}

def get_fund_new():
    """获取新发基金信息"""
    try:
        df = ak.fund_new_found_em()
        return {
            "type": "fund_new",
            "data": df.to_dict('records'),
            "count": len(df)
        }
    except Exception as e:
        return {"error": f"获取新发基金信息失败: {str(e)}"}

def main():
    parser = argparse.ArgumentParser(description='AKShare 基金数据获取')
    parser.add_argument('--type', required=True,
                       choices=['etf_spot', 'etf_hist', 'open_fund', 'rating', 'portfolio',
                               'manager', 'money_fund', 'scale', 'new'],
                       help='数据类型')
    parser.add_argument('--symbol', help='基金代码')
    parser.add_argument('--period', default='daily',
                       choices=['daily', 'weekly', 'monthly'],
                       help='周期')
    parser.add_argument('--start', help='开始日期 YYYYMMDD')
    parser.add_argument('--end', help='结束日期 YYYYMMDD')
    parser.add_argument('--adjust', default='qfq',
                       choices=['', 'qfq', 'hfq'],
                       help='复权类型')

    args = parser.parse_args()

    if args.type == 'etf_spot':
        result = get_etf_spot()
    elif args.type == 'etf_hist':
        if not args.symbol:
            result = {"error": "ETF历史数据需要指定symbol参数"}
        else:
            result = get_etf_hist(args.symbol, args.period, args.start, args.end, args.adjust)
    elif args.type == 'open_fund':
        if not args.symbol:
            result = {"error": "开放式基金数据需要指定symbol参数"}
        else:
            result = get_open_fund_daily(args.symbol)
    elif args.type == 'rating':
        result = get_fund_rating()
    elif args.type == 'portfolio':
        if not args.symbol:
            result = {"error": "基金持仓数据需要指定symbol参数"}
        else:
            result = get_fund_portfolio(args.symbol)
    elif args.type == 'manager':
        result = get_fund_manager()
    elif args.type == 'money_fund':
        result = get_money_fund()
    elif args.type == 'scale':
        result = get_fund_scale()
    elif args.type == 'new':
        result = get_fund_new()
    else:
        result = {"error": f"未知类型: {args.type}"}

    print(json.dumps(result, ensure_ascii=False, indent=2, default=str))

if __name__ == "__main__":
    main()
