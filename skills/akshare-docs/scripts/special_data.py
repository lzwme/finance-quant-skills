#!/usr/bin/env python3
"""AKShare 特色数据获取脚本
支持龙虎榜、融资融券、北向资金、股东数据等"""
import sys
import json
import argparse
import pandas as pd
import akshare as ak

def get_stock_lhb_detail(start_date, end_date):
    """获取龙虎榜详细数据"""
    try:
        df = ak.stock_lhb_detail_em(start_date=start_date, end_date=end_date)
        return {
            "type": "lhb_detail",
            "start_date": start_date,
            "end_date": end_date,
            "data": df.to_dict('records'),
            "count": len(df)
        }
    except Exception as e:
        return {"error": f"获取龙虎榜详细数据失败: {str(e)}"}

def get_stock_lhb_hyyyb(start_date, end_date):
    """获取龙虎榜营业部排名"""
    try:
        df = ak.stock_lhb_hyyyb_em(start_date=start_date, end_date=end_date)
        return {
            "type": "lhb_hyyyb",
            "start_date": start_date,
            "end_date": end_date,
            "data": df.to_dict('records'),
            "count": len(df)
        }
    except Exception as e:
        return {"error": f"获取龙虎榜营业部排名失败: {str(e)}"}

def get_stock_margin_sse(start_date, end_date):
    """获取沪深融资融券汇总数据"""
    try:
        df = ak.stock_margin_sse(start_date=start_date, end_date=end_date)
        return {
            "type": "margin_sse",
            "start_date": start_date,
            "end_date": end_date,
            "data": df.to_dict('records'),
            "count": len(df)
        }
    except Exception as e:
        return {"error": f"获取融资融券汇总数据失败: {str(e)}"}

def get_stock_margin_detail(date):
    """获取个股融资融券明细"""
    try:
        df = ak.stock_margin_detail_sse(date=date)
        return {
            "type": "margin_detail",
            "date": date,
            "data": df.to_dict('records'),
            "count": len(df)
        }
    except Exception as e:
        return {"error": f"获取融资融券明细失败: {str(e)}"}

def get_stock_hsgt_hist(symbol="北向资金"):
    """获取北向资金历史数据"""
    try:
        df = ak.stock_hsgt_hist_em(symbol=symbol)
        return {
            "type": "hsgt_hist",
            "symbol": symbol,
            "data": df.to_dict('records'),
            "count": len(df)
        }
    except Exception as e:
        return {"error": f"获取北向资金历史数据失败: {str(e)}"}

def get_stock_hsgt_hold_stock(market="北向", indicator="今日排行"):
    """获取北向资金持股明细"""
    try:
        df = ak.stock_hsgt_hold_stock_em(market=market, indicator=indicator)
        return {
            "type": "hsgt_hold_stock",
            "market": market,
            "indicator": indicator,
            "data": df.to_dict('records'),
            "count": len(df)
        }
    except Exception as e:
        return {"error": f"获取北向资金持股明细失败: {str(e)}"}

def get_stock_gdfx_top_10(symbol, date):
    """获取前十大股东"""
    try:
        df = ak.stock_gdfx_top_10_em(symbol=symbol, date=date)
        return {
            "type": "gdfx_top_10",
            "symbol": symbol,
            "date": date,
            "data": df.to_dict('records'),
            "count": len(df)
        }
    except Exception as e:
        return {"error": f"获取前十大股东失败: {str(e)}"}

def get_stock_gdfx_free_top_10(symbol, date):
    """获取前十大流通股东"""
    try:
        df = ak.stock_gdfx_free_top_10_em(symbol=symbol, date=date)
        return {
            "type": "gdfx_free_top_10",
            "symbol": symbol,
            "date": date,
            "data": df.to_dict('records'),
            "count": len(df)
        }
    except Exception as e:
        return {"error": f"获取前十大流通股东失败: {str(e)}"}

def get_stock_board_industry():
    """获取行业板块行情"""
    try:
        df = ak.stock_board_industry_name_em()
        return {
            "type": "board_industry",
            "data": df.to_dict('records'),
            "count": len(df)
        }
    except Exception as e:
        return {"error": f"获取行业板块行情失败: {str(e)}"}

def get_stock_board_concept():
    """获取概念板块行情"""
    try:
        df = ak.stock_board_concept_name_em()
        return {
            "type": "board_concept",
            "data": df.to_dict('records'),
            "count": len(df)
        }
    except Exception as e:
        return {"error": f"获取概念板块行情失败: {str(e)}"}

def get_stock_board_industry_cons(symbol="银行"):
    """获取特定板块成分股"""
    try:
        df = ak.stock_board_industry_cons_em(symbol=symbol)
        return {
            "type": "board_industry_cons",
            "symbol": symbol,
            "data": df.to_dict('records'),
            "count": len(df)
        }
    except Exception as e:
        return {"error": f"获取板块成分股失败: {str(e)}"}

def get_stock_restricted_release(symbol="全部A股"):
    """获取限售解禁数据"""
    try:
        df = ak.stock_restricted_release_queue_em(symbol=symbol)
        return {
            "type": "restricted_release",
            "symbol": symbol,
            "data": df.to_dict('records'),
            "count": len(df)
        }
    except Exception as e:
        return {"error": f"获取限售解禁数据失败: {str(e)}"}

def get_stock_market_fund_flow():
    """获取大盘资金流向"""
    try:
        df = ak.stock_market_fund_flow()
        return {
            "type": "market_fund_flow",
            "data": df.to_dict('records'),
            "count": len(df)
        }
    except Exception as e:
        return {"error": f"获取大盘资金流向失败: {str(e)}"}

def get_stock_individual_fund_flow(stock, market="sz"):
    """获取个股资金流向"""
    try:
        df = ak.stock_individual_fund_flow(stock=stock, market=market)
        return {
            "type": "individual_fund_flow",
            "stock": stock,
            "market": market,
            "data": df.to_dict('records'),
            "count": len(df)
        }
    except Exception as e:
        return {"error": f"获取个股资金流向失败: {str(e)}"}

def main():
    parser = argparse.ArgumentParser(description='AKShare 特色数据获取')
    parser.add_argument('--type', required=True,
                       choices=['lhb_detail', 'lhb_hyyyb', 'margin_sse', 'margin_detail',
                               'hsgt_hist', 'hsgt_hold', 'gdfx_top10', 'gdfx_free_top10',
                               'board_industry', 'board_concept', 'board_cons', 'restricted_release',
                               'market_fund_flow', 'individual_fund_flow'],
                       help='数据类型')
    parser.add_argument('--start', help='开始日期 YYYYMMDD')
    parser.add_argument('--end', help='结束日期 YYYYMMDD')
    parser.add_argument('--date', help='指定日期 YYYYMMDD')
    parser.add_argument('--symbol', help='股票代码或板块名称')
    parser.add_argument('--market', default='sz', help='市场类型')
    parser.add_argument('--indicator', default='今日排行', help='指标类型')

    args = parser.parse_args()

    if args.type == 'lhb_detail':
        if not args.start or not args.end:
            result = {"error": "龙虎榜详细数据需要start和end参数"}
        else:
            result = get_stock_lhb_detail(args.start, args.end)
    elif args.type == 'lhb_hyyyb':
        if not args.start or not args.end:
            result = {"error": "龙虎榜营业部排名需要start和end参数"}
        else:
            result = get_stock_lhb_hyyyb(args.start, args.end)
    elif args.type == 'margin_sse':
        if not args.start or not args.end:
            result = {"error": "融资融券汇总数据需要start和end参数"}
        else:
            result = get_stock_margin_sse(args.start, args.end)
    elif args.type == 'margin_detail':
        if not args.date:
            result = {"error": "融资融券明细需要date参数"}
        else:
            result = get_stock_margin_detail(args.date)
    elif args.type == 'hsgt_hist':
        symbol = args.symbol if args.symbol else "北向资金"
        result = get_stock_hsgt_hist(symbol)
    elif args.type == 'hsgt_hold':
        market = args.market if args.market else "北向"
        indicator = args.indicator if args.indicator else "今日排行"
        result = get_stock_hsgt_hold_stock(market, indicator)
    elif args.type == 'gdfx_top10':
        if not args.symbol or not args.date:
            result = {"error": "前十大股东需要symbol和date参数"}
        else:
            result = get_stock_gdfx_top_10(args.symbol, args.date)
    elif args.type == 'gdfx_free_top10':
        if not args.symbol or not args.date:
            result = {"error": "前十大流通股东需要symbol和date参数"}
        else:
            result = get_stock_gdfx_free_top_10(args.symbol, args.date)
    elif args.type == 'board_industry':
        result = get_stock_board_industry()
    elif args.type == 'board_concept':
        result = get_stock_board_concept()
    elif args.type == 'board_cons':
        symbol = args.symbol if args.symbol else "银行"
        result = get_stock_board_industry_cons(symbol)
    elif args.type == 'restricted_release':
        symbol = args.symbol if args.symbol else "全部A股"
        result = get_stock_restricted_release(symbol)
    elif args.type == 'market_fund_flow':
        result = get_stock_market_fund_flow()
    elif args.type == 'individual_fund_flow':
        if not args.symbol:
            result = {"error": "个股资金流向需要symbol参数"}
        else:
            market = args.market if args.market else "sz"
            result = get_stock_individual_fund_flow(args.symbol, market)
    else:
        result = {"error": f"未知类型: {args.type}"}

    print(json.dumps(result, ensure_ascii=False, indent=2, default=str))

if __name__ == "__main__":
    main()
