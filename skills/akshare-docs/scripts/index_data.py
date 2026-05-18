#!/usr/bin/env python3
"""AKShare 指数数据获取脚本
支持A股指数、全球指数等数据"""
import sys
import json
import argparse
import pandas as pd
import akshare as ak

def get_index_daily(symbol="sh000001"):
    """获取A股指数日线数据"""
    try:
        df = ak.stock_zh_index_daily_em(symbol=symbol)
        return {
            "type": "index_daily",
            "symbol": symbol,
            "data": df.to_dict('records'),
            "count": len(df)
        }
    except Exception as e:
        return {"error": f"获取指数日线数据失败: {str(e)}"}

def get_index_component(symbol="000300"):
    """获取指数成分股"""
    try:
        df = ak.index_stock_cons_csindex(symbol=symbol)
        return {
            "type": "index_component",
            "symbol": symbol,
            "data": df.to_dict('records'),
            "count": len(df)
        }
    except Exception as e:
        return {"error": f"获取指数成分股失败: {str(e)}"}

def get_global_index():
    """获取全球指数数据"""
    try:
        df = ak.index_global_em()
        return {
            "type": "global_index",
            "data": df.to_dict('records'),
            "count": len(df)
        }
    except Exception as as e:
        return {"error": f"获取全球指数失败: {str(e)}"}

def get_index_value(symbol="000300"):
    """获取指数估值数据"""
    try:
        df = ak.index_value_name_funddb()
        # 筛选指定指数
        if symbol:
            df = df[df['指数代码'] == symbol]
        return {
            "type": "index_value",
            "symbol": symbol,
            "data": df.to_dict('records'),
            "count": len(df)
        }
    except Exception as e:
        return {"error": f"获取指数估值失败: {str(e)}"}

def get_index_weight(symbol="000300"):
    """获取指数权重数据"""
    try:
        df = ak.index_stock_weight_csindex(symbol=symbol)
        return {
            "type": "index_weight",
            "symbol": symbol,
            "data": df.to_dict('records'),
            "count": len(df)
        }
    except Exception as e:
        return {"error": f"获取指数权重失败: {str(e)}"}

def get_index_analysis(symbol="000300"):
    """获取指数分析数据"""
    try:
        df = ak.index_analysis_weekly(symbol=symbol)
        return {
            "type": "index_analysis",
            "symbol": symbol,
            "data": df.to_dict('records'),
            "count": len(df)
        }
    except Exception as e:
        return {"error": f"获取指数分析失败: {str(e)}"}

def main():
    parser = argparse.ArgumentParser(description='AKShare 指数数据获取')
    parser.add_argument('--type', required=True,
                       choices=['daily', 'component', 'global', 'value', 'weight', 'analysis'],
                       help='数据类型')
    parser.add_argument('--symbol', default='000300', help='指数代码')

    args = parser.parse_args()

    if args.type == 'daily':
        # 处理带前缀的指数代码
        symbol = args.symbol
        if not symbol.startswith(('sh', 'sz')):
            if symbol.startswith('000'):
                symbol = f"sh{symbol}"
            elif symbol.startswith('399'):
                symbol = f"sz{symbol}"
        result = get_index_daily(symbol)
    elif args.type == 'component':
        result = get_index_component(args.symbol)
    elif args.type == 'global':
        result = get_global_index()
    elif args.type == 'value':
        result = get_index_value(args.symbol)
    elif args.type == 'weight':
        result = get_index_weight(args.symbol)
    elif args.type == 'analysis':
        result = get_index_analysis(args.symbol)
    else:
        result = {"error": f"未知类型: {args.type}"}

    print(json.dumps(result, ensure_ascii=False, indent=2, default=str))

if __name__ == "__main__":
    main()
