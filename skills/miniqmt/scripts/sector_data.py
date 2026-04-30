#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
MiniQMT 板块与分类数据获取脚本
支持：板块列表、板块成分股、股票所属板块、指数成分权重、ETF信息
"""

import argparse
import json
import sys
import os

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from xtquant import xtdata
xtdata.enable_hello = False

def cmd_sector_list(args):
    """获取板块列表"""
    result = {"status": "success", "data_type": "sector_list"}
    try:
        sectors = xtdata.get_sector_list()
        result["data"] = {"count": len(sectors), "sectors": sectors}
    except Exception as e:
        result["status"] = "error"
        result["message"] = str(e)
    return result


def cmd_sector_stocks(args):
    """获取板块成分股"""
    result = {"status": "success", "data_type": "sector_stocks", "sector": args.sector}
    try:
        stocks = xtdata.get_stock_list_in_sector(args.sector)
        result["data"] = {"stocks": stocks, "count": len(stocks)}
    except Exception as e:
        result["status"] = "error"
        result["message"] = str(e)
    return result


def cmd_stock_sectors(args):
    """获取股票所属板块"""
    result = {"status": "success", "data_type": "stock_sectors", "code": args.code}
    try:
        # 尝试获取股票类型信息
        info = xtdata.get_instrument_type(args.code)
        result["data"] = {"info": info, "sectors": []}
    except Exception as e:
        result["status"] = "error"
        result["message"] = str(e)
    return result


def cmd_index_weight(args):
    """获取指数成分权重"""
    result = {"status": "success", "data_type": "index_weight", "index": args.index}
    try:
        weights = xtdata.get_index_weight(args.index)
        result["data"] = {"count": len(weights), "weights": weights}
    except Exception as e:
        result["status"] = "error"
        result["message"] = str(e)
    return result


def cmd_etf_info(args):
    """获取ETF信息"""
    result = {"status": "success", "data_type": "etf_info"}
    try:
        xtdata.download_etf_info()
        etf_data = xtdata.get_etf_info()
        result["data"] = {"count": len(etf_data), "items": etf_data}
    except Exception as e:
        result["status"] = "error"
        result["message"] = str(e)
    return result


def cmd_cb_info(args):
    """获取可转债信息"""
    result = {"status": "success", "data_type": "cb_info", "code": args.code}
    try:
        xtdata.download_cb_data()
        info = xtdata.get_cb_info(args.code)
        result["data"] = info if info else {}
    except Exception as e:
        result["status"] = "error"
        result["message"] = str(e)
    return result


def cmd_instrument_type(args):
    """获取合约类型"""
    result = {"status": "success", "data_type": "instrument_type", "code": args.code}
    try:
        info = xtdata.get_instrument_type(args.code)
        result["data"] = info
    except Exception as e:
        result["status"] = "error"
        result["message"] = str(e)
    return result


def cmd_stock_list(args):
    """获取市场股票列表"""
    result = {"status": "success", "data_type": "stock_list", "market": args.market}
    try:
        stocks = xtdata.get_stock_list_in_sector(args.market)
        result["data"] = {"count": len(stocks), "stocks": stocks}
    except Exception as e:
        result["status"] = "error"
        result["message"] = str(e)
    return result


def add_args(parser):
    """添加命令行参数"""
    subparsers = parser.add_subparsers(dest='cmd', help='子命令')

    # sector_list
    p = subparsers.add_parser('sector_list', help='板块列表')

    # sector_stocks
    p = subparsers.add_parser('sector_stocks', help='板块成分股')
    p.add_argument('--sector', '-s', required=True, help='板块名称')

    # stock_sectors
    p = subparsers.add_parser('stock_sectors', help='股票所属板块')
    p.add_argument('--code', '-c', required=True, help='证券代码')

    # index_weight
    p = subparsers.add_parser('index_weight', help='指数成分权重')
    p.add_argument('--index', '-i', required=True, help='指数代码，如 000300.SH')

    # etf_info
    p = subparsers.add_parser('etf_info', help='ETF信息')

    # cb_info
    p = subparsers.add_parser('cb_info', help='可转债信息')
    p.add_argument('--code', '-c', required=True, help='可转债代码')

    # instrument_type
    p = subparsers.add_parser('instrument_type', help='合约类型')
    p.add_argument('--code', '-c', required=True, help='证券代码')

    # stock_list
    p = subparsers.add_parser('stock_list', help='市场股票列表')
    p.add_argument('--market', '-m', default='沪深A股', help='市场名称')


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='MiniQMT 板块数据获取')
    add_args(parser)
    args = parser.parse_args()

    cmd_map = {
        'sector_list': cmd_sector_list,
        'sector_stocks': cmd_sector_stocks,
        'stock_sectors': cmd_stock_sectors,
        'index_weight': cmd_index_weight,
        'etf_info': cmd_etf_info,
        'cb_info': cmd_cb_info,
        'instrument_type': cmd_instrument_type,
        'stock_list': cmd_stock_list,
    }

    if args.cmd in cmd_map:
        result = cmd_map[args.cmd](args)
        print(json.dumps(result, ensure_ascii=False, indent=2))
    else:
        parser.print_help()
