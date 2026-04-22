#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
财务数据获取脚本
支持：专业财务数据(financial)、指定日期财务(financial_by_date)、单个财务指标(gp_one_data)
"""

import argparse
import json
import sys
import os

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _tdx_init import init_tq


def cmd_financial(tq, args):
    """获取指定时间段的专业财务数据"""
    result = {"status": "success", "data_type": "financial", "code": args.code}
    fields = args.fields.split(",") if args.fields else ["fn193", "fn194", "fn197"]

    report_type_map = {"announce": "announce_time", "tag": "tag_time"}
    report_type = report_type_map.get(args.report_type, "announce_time")

    data = tq.get_financial_data(
        stock_list=[args.code],
        field_list=fields,
        start_time=args.start or "",
        end_time=args.end or "",
        report_type=report_type
    )
    if data and args.code in data:
        import pandas as pd
        df = data[args.code]
        if hasattr(df, "to_dict"):
            result["data"] = df.to_dict(orient="records")
        else:
            result["data"] = str(df)
    else:
        result["data"] = {}
    return result


def cmd_financial_by_date(tq, args):
    """获取指定日期的专业财务数据"""
    result = {"status": "success", "data_type": "financial_by_date", "code": args.code}
    fields = args.fields.split(",") if args.fields else ["fn193", "fn197"]

    data = tq.get_financial_data_by_date(
        stock_list=[args.code],
        field_list=fields,
        year=args.year,
        mmdd=args.mmdd
    )
    if data and args.code in data:
        result["data"] = data[args.code]
    else:
        result["data"] = {}
    return result


def cmd_gp_one_data(tq, args):
    """获取股票的单个财务数据"""
    result = {"status": "success", "data_type": "gp_one_data", "code": args.code}
    fields = args.fields.split(",") if args.fields else ["go1", "go3", "go5"]

    data = tq.get_gp_one_data(
        stock_list=[args.code],
        field_list=fields
    )
    if data and args.code in data:
        result["data"] = data[args.code]
    else:
        result["data"] = {}
    return result


def main():
    parser = argparse.ArgumentParser(description="通达信财务数据获取")
    sub = parser.add_subparsers(dest="command", required=True)

    # financial
    p = sub.add_parser("financial", help="获取专业财务数据(时间段)")
    p.add_argument("--code", required=True, help="证券代码，如 600519.SH")
    p.add_argument("--fields", default="", help="字段列表，逗号分隔，如 fn193,fn194,fn197")
    p.add_argument("--start", default="", help="起始日期 YYYYMMDD")
    p.add_argument("--end", default="", help="结束日期 YYYYMMDD")
    p.add_argument("--report_type", default="announce",
                   choices=["announce", "tag"],
                   help="筛选方式: announce-按公告日期, tag-按报告期")

    # financial_by_date
    p = sub.add_parser("financial_by_date", help="获取指定日期的专业财务数据")
    p.add_argument("--code", required=True, help="证券代码，如 600519.SH")
    p.add_argument("--fields", default="", help="字段列表，逗号分隔，如 fn193,fn197")
    p.add_argument("--year", type=int, default=0, help="指定年份，0表示最新")
    p.add_argument("--mmdd", type=int, default=0,
                   help="指定月日，0表示最新；小于300表示倒数第N期；331/630/930/1231表示季报")

    # gp_one_data
    p = sub.add_parser("gp_one_data", help="获取股票单个财务数据")
    p.add_argument("--code", required=True, help="证券代码，如 600519.SH")
    p.add_argument("--fields", default="", help="字段列表，逗号分隔，如 go1,go3,go5 (go=gp one首字母)")

    args = parser.parse_args()
    tq = init_tq()

    handlers = {
        "financial": cmd_financial,
        "financial_by_date": cmd_financial_by_date,
        "gp_one_data": cmd_gp_one_data,
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
