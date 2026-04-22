#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
交易数据获取脚本
支持：股票交易数据(gpjy/gpjy_by_date)、板块交易数据(bkjy/bkjy_by_date)、市场交易数据(scjy/scjy_by_date)
"""

import argparse
import json
import sys
import os

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _tdx_init import init_tq


def cmd_gpjy(tq, args):
    """获取股票交易数据"""
    result = {"status": "success", "data_type": "gpjy", "code": args.code}
    fields = args.fields.split(",") if args.fields else ["gp1", "gp3", "gp16"]

    data = tq.get_gpjy_value(
        stock_list=[args.code],
        field_list=fields,
        start_time=args.start or "",
        end_time=args.end or ""
    )
    result["data"] = data.get(args.code, {}) if data else {}
    return result


def cmd_gpjy_by_date(tq, args):
    """获取指定日期股票交易数据"""
    result = {"status": "success", "data_type": "gpjy_by_date", "code": args.code}
    fields = args.fields.split(",") if args.fields else ["gp1", "gp3"]

    data = tq.get_gpjy_value_by_date(
        stock_list=[args.code],
        field_list=fields,
        year=args.year,
        mmdd=args.mmdd
    )
    result["data"] = data.get(args.code, {}) if data else {}
    return result


def cmd_bkjy(tq, args):
    """获取板块交易数据"""
    result = {"status": "success", "data_type": "bkjy", "code": args.code}
    fields = args.fields.split(",") if args.fields else ["bk5", "bk6", "bk9"]

    data = tq.get_bkjy_value(
        stock_list=[args.code],
        field_list=fields,
        start_time=args.start or "",
        end_time=args.end or ""
    )
    result["data"] = data.get(args.code, {}) if data else {}
    return result


def cmd_bkjy_by_date(tq, args):
    """获取指定日期板块交易数据"""
    result = {"status": "success", "data_type": "bkjy_by_date", "code": args.code}
    fields = args.fields.split(",") if args.fields else ["bk5", "bk9"]

    data = tq.get_bkjy_value_by_date(
        stock_list=[args.code],
        field_list=fields,
        year=args.year,
        mmdd=args.mmdd
    )
    result["data"] = data.get(args.code, {}) if data else {}
    return result


def cmd_scjy(tq, args):
    """获取市场交易数据"""
    result = {"status": "success", "data_type": "scjy"}
    fields = args.fields.split(",") if args.fields else ["sc1", "sc3", "sc4"]

    data = tq.get_scjy_value(
        field_list=fields,
        start_time=args.start or "",
        end_time=args.end or ""
    )
    result["data"] = data if data else {}
    return result


def cmd_scjy_by_date(tq, args):
    """获取指定日期市场交易数据"""
    result = {"status": "success", "data_type": "scjy_by_date"}
    fields = args.fields.split(",") if args.fields else ["sc1", "sc3"]

    data = tq.get_scjy_value_by_date(
        field_list=fields,
        year=args.year,
        mmdd=args.mmdd
    )
    result["data"] = data if data else {}
    return result


def main():
    parser = argparse.ArgumentParser(description="通达信交易数据获取")
    sub = parser.add_subparsers(dest="command", required=True)

    # gpjy
    p = sub.add_parser("gpjy", help="获取股票交易数据")
    p.add_argument("--code", required=True, help="证券代码，如 688318.SH")
    p.add_argument("--fields", default="", help="字段列表，逗号分隔，如 gp1,gp3,gp16")
    p.add_argument("--start", default="", help="起始日期 YYYYMMDD")
    p.add_argument("--end", default="", help="结束日期 YYYYMMDD")

    # gpjy_by_date
    p = sub.add_parser("gpjy_by_date", help="获取指定日期股票交易数据")
    p.add_argument("--code", required=True, help="证券代码，如 688318.SH")
    p.add_argument("--fields", default="", help="字段列表，逗号分隔")
    p.add_argument("--year", type=int, default=0, help="年份，0表示最新")
    p.add_argument("--mmdd", type=int, default=0, help="月日，0表示最新")

    # bkjy
    p = sub.add_parser("bkjy", help="获取板块交易数据")
    p.add_argument("--code", required=True, help="板块代码，如 880660.SH")
    p.add_argument("--fields", default="", help="字段列表，逗号分隔，如 bk5,bk6,bk9")
    p.add_argument("--start", default="", help="起始日期 YYYYMMDD")
    p.add_argument("--end", default="", help="结束日期 YYYYMMDD")

    # bkjy_by_date
    p = sub.add_parser("bkjy_by_date", help="获取指定日期板块交易数据")
    p.add_argument("--code", required=True, help="板块代码，如 880660.SH")
    p.add_argument("--fields", default="", help="字段列表，逗号分隔")
    p.add_argument("--year", type=int, default=0, help="年份，0表示最新")
    p.add_argument("--mmdd", type=int, default=0, help="月日，0表示最新")

    # scjy
    p = sub.add_parser("scjy", help="获取市场交易数据")
    p.add_argument("--fields", default="", help="字段列表，逗号分隔，如 sc1,sc3,sc4")
    p.add_argument("--start", default="", help="起始日期 YYYYMMDD")
    p.add_argument("--end", default="", help="结束日期 YYYYMMDD")

    # scjy_by_date
    p = sub.add_parser("scjy_by_date", help="获取指定日期市场交易数据")
    p.add_argument("--fields", default="", help="字段列表，逗号分隔")
    p.add_argument("--year", type=int, default=0, help="年份，0表示最新")
    p.add_argument("--mmdd", type=int, default=0, help="月日，0表示最新")

    args = parser.parse_args()
    tq = init_tq()

    handlers = {
        "gpjy": cmd_gpjy,
        "gpjy_by_date": cmd_gpjy_by_date,
        "bkjy": cmd_bkjy,
        "bkjy_by_date": cmd_bkjy_by_date,
        "scjy": cmd_scjy,
        "scjy_by_date": cmd_scjy_by_date,
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
