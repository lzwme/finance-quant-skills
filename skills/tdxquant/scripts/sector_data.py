#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
板块与分类数据获取脚本
支持：系统分类成份股(stock_list)、板块代码列表(sector_list)、板块成份股(sector_stocks)、
     股票所属板块(stock_relation)、自定义板块(user_sector)
"""

import argparse
import json
import sys
import os

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _tdx_init import init_tq


def cmd_stock_list(tq, args):
    """获取系统分类成份股"""
    result = {"status": "success", "data_type": "stock_list", "list_type": args.list_type}
    data = tq.get_stock_list(market=str(args.list_type), list_type=1 if args.with_name else 0)
    result["data"] = data if data else []
    result["count"] = len(data) if data else 0
    return result


def cmd_sector_list(tq, args):
    """获取A股板块代码列表"""
    result = {"status": "success", "data_type": "sector_list"}
    data = tq.get_sector_list(list_type=1 if args.with_name else 0)
    result["data"] = data if data else []
    result["count"] = len(data) if data else 0
    return result


def cmd_sector_stocks(tq, args):
    """获取板块成份股"""
    result = {"status": "success", "data_type": "sector_stocks"}
    block_code = args.block_code or ""
    block_name = args.block_name or ""

    if not block_code and not block_name:
        result["status"] = "error"
        result["message"] = "请提供 --block_code 或 --block_name"
        return result

    identifier = block_name if block_name else block_code
    block_type = 1 if args.custom else 0

    data = tq.get_stock_list_in_sector(
        block_code=identifier,
        block_type=block_type,
        list_type=1 if args.with_name else 0
    )
    result["block"] = identifier
    result["data"] = data if data else []
    result["count"] = len(data) if data else 0
    return result


def cmd_stock_relation(tq, args):
    """获取股票所属板块"""
    result = {"status": "success", "data_type": "stock_relation", "code": args.code}
    data = tq.get_relation(stock_code=args.code)
    result["data"] = data if data else []
    return result


def cmd_user_sector(tq, args):
    """自定义板块操作"""
    result = {"status": "success", "data_type": "user_sector"}

    if args.action == "list":
        data = tq.get_user_sector()
        result["data"] = data if data else []
    elif args.action == "create":
        data = tq.create_sector(block_code=args.block_code, block_name=args.block_name)
        result["data"] = data
    elif args.action == "add_stocks":
        stocks = args.stocks.split(",") if args.stocks else []
        data = tq.send_user_block(block_code=args.block_code, stocks=stocks, show=False)
        result["data"] = data
    elif args.action == "clear":
        data = tq.send_user_block(block_code=args.block_code, stocks=[], show=False)
        result["data"] = data
    else:
        result["status"] = "error"
        result["message"] = f"未知操作: {args.action}"

    return result


def main():
    parser = argparse.ArgumentParser(description="通达信板块与分类数据获取")
    sub = parser.add_subparsers(dest="command", required=True)

    # stock_list
    p = sub.add_parser("stock_list", help="获取系统分类成份股")
    p.add_argument("--list_type", type=int, default=5,
                   help="分类类型: 0=自选股, 1=持仓股, 5=所有A股, 7=上证主板, 8=深证主板, "
                        "9=重点指数, 10=所有板块指数, 11=行业板块, 12=概念板块, 13=风格板块, "
                        "16=研究行业一级, 17=研究行业二级, 23=沪深300, 24=中证500, "
                        "32=可转债, 50=沪深A股, 51=创业板, 52=科创板, 53=北交所")
    p.add_argument("--with_name", action="store_true", help="返回代码和名称")

    # sector_list
    p = sub.add_parser("sector_list", help="获取A股板块代码列表")
    p.add_argument("--with_name", action="store_true", help="返回代码和名称")

    # sector_stocks
    p = sub.add_parser("sector_stocks", help="获取板块成份股")
    p.add_argument("--block_code", default="", help="板块代码，如 880081.SH")
    p.add_argument("--block_name", default="", help="板块名称，如 钛金属")
    p.add_argument("--custom", action="store_true", help="是否为自定义板块")
    p.add_argument("--with_name", action="store_true", help="返回代码和名称")

    # stock_relation
    p = sub.add_parser("stock_relation", help="获取股票所属板块")
    p.add_argument("--code", required=True, help="证券代码，如 688318.SH")

    # user_sector
    p = sub.add_parser("user_sector", help="自定义板块操作")
    p.add_argument("--action", required=True, choices=["list", "create", "add_stocks", "clear"],
                   help="操作: list-查看列表, create-创建板块, add_stocks-添加股票, clear-清空板块")
    p.add_argument("--block_code", default="", help="板块简称(zxg=自选股)")
    p.add_argument("--block_name", default="", help="板块名称(create时使用)")
    p.add_argument("--stocks", default="", help="股票代码，逗号分隔(add_stocks时使用)")

    args = parser.parse_args()
    tq = init_tq()

    handlers = {
        "stock_list": cmd_stock_list,
        "sector_list": cmd_sector_list,
        "sector_stocks": cmd_sector_stocks,
        "stock_relation": cmd_stock_relation,
        "user_sector": cmd_user_sector,
    }

    try:
        result = handlers[args.command](tq, args)
        print(json.dumps(result, ensure_ascii=False, indent=2, default=str))
    except Exception as e:
        print(json.dumps({
            "status": "error", "message": str(e), "error_type": type(e).__name__
        }, ensure_ascii=False))
        sys.exit(1)


if __name__ == "__main__":
    main()
