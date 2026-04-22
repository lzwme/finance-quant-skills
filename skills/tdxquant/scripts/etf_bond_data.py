#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
ETF/可转债/新股数据获取脚本
支持：可转债信息(kzz_info)、跟踪指数的ETF信息(trackzs_etf)、新股申购(ipo_info)
"""

import argparse
import json
import sys
import os

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _tdx_init import init_tq


def cmd_kzz_info(tq, args):
    """获取可转债信息"""
    result = {"status": "success", "data_type": "kzz_info", "code": args.code}
    fields = args.fields.split(",") if args.fields else []
    data = tq.get_kzz_info(stock_code=args.code, field_list=fields)
    if data:
        result["data"] = data
    else:
        result["status"] = "error"
        result["message"] = f"未获取到可转债 {args.code} 的信息"
    return result


def cmd_trackzs_etf(tq, args):
    """获取跟踪指数的ETF信息"""
    result = {"status": "success", "data_type": "trackzs_etf", "zs_code": args.zs_code}
    data = tq.get_trackzs_etf_info(zs_code=args.zs_code)
    if data:
        result["data"] = data
    else:
        result["data"] = []
    return result


def cmd_ipo_info(tq, args):
    """获取新股申购信息"""
    result = {"status": "success", "data_type": "ipo_info"}
    data = tq.get_ipo_info(ipo_type=args.ipo_type, ipo_date=args.ipo_date)
    if data:
        result["data"] = data
    else:
        result["data"] = []
    return result


def main():
    parser = argparse.ArgumentParser(description="通达信ETF/可转债/新股数据获取")
    sub = parser.add_subparsers(dest="command", required=True)

    # kzz_info
    p = sub.add_parser("kzz_info", help="获取可转债信息")
    p.add_argument("--code", required=True, help="可转债代码，如 123039.SZ")
    p.add_argument("--fields", default="", help="字段列表，逗号分隔")

    # trackzs_etf
    p = sub.add_parser("trackzs_etf", help="获取跟踪指数的ETF信息")
    p.add_argument("--zs_code", required=True, help="指数代码，如 950162.CSI")

    # ipo_info
    p = sub.add_parser("ipo_info", help="获取新股/新发债申购信息")
    p.add_argument("--ipo_type", type=int, default=2,
                   help="0=新股, 1=新发债, 2=新股和新发债(默认)")
    p.add_argument("--ipo_date", type=int, default=1,
                   help="0=只获取今天, 1=获取今天及以后(默认)")

    args = parser.parse_args()
    tq = init_tq()

    handlers = {
        "kzz_info": cmd_kzz_info,
        "trackzs_etf": cmd_trackzs_etf,
        "ipo_info": cmd_ipo_info,
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
