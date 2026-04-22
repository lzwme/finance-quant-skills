#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
行情数据获取脚本
支持：行情快照(snapshot)、K线(kline)、证券基本信息(stock_info)、
     更多信息(more_info)、分红配送(divid_factors)、股本数据(gb_info)
"""

import argparse
import json
import sys
import os

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _tdx_init import init_tq


def cmd_snapshot(tq, args):
    result = {"status": "success", "data_type": "snapshot", "code": args.code}
    data = tq.get_market_snapshot(stock_code=args.code, field_list=[])
    if data and data.get("ErrorId", "-1") == "0":
        result["data"] = data
    else:
        result["status"] = "error"
        result["message"] = f"未获取到 {args.code} 的行情快照"
    return result


def cmd_kline(tq, args):
    result = {
        "status": "success", "data_type": "kline", "code": args.code,
        "period": args.period, "count": args.count
    }
    dividend_map = {"none": "none", "qfq": "front", "hfq": "back", "bfq": "none"}
    dividend_type = dividend_map.get(args.fq, "none")

    df_dict = tq.get_market_data(
        field_list=[],
        stock_list=[args.code],
        period=args.period,
        start_time=args.start or "",
        end_time=args.end or "",
        count=args.count,
        dividend_type=dividend_type,
        fill_data=True
    )

    if df_dict and args.code in df_dict:
        import pandas as pd
        df = df_dict[args.code] if isinstance(df_dict, dict) else df_dict
        # get_market_data 返回的是 {field: DataFrame} 结构
        # 需要重新组装
        try:
            close_df = df_dict.get("Close", df_dict.get("close", None))
            if close_df is not None and hasattr(close_df, "to_dict"):
                result["data"] = close_df.to_dict()
            else:
                result["data"] = str(df_dict)
        except Exception:
            result["data"] = str(df_dict)
    else:
        result["status"] = "error"
        result["message"] = f"未获取到 {args.code} 的K线数据"
    return result


def cmd_stock_info(tq, args):
    result = {"status": "success", "data_type": "stock_info", "code": args.code}
    fields = args.fields.split(",") if args.fields else []
    data = tq.get_stock_info(stock_code=args.code, field_list=fields)
    if data and data.get("ErrorId", "-1") == "0":
        data.pop("ErrorId", None)
        result["data"] = data
    else:
        result["data"] = data or {}
    return result


def cmd_more_info(tq, args):
    result = {"status": "success", "data_type": "more_info", "code": args.code}
    fields = args.fields.split(",") if args.fields else []
    data = tq.get_more_info(stock_code=args.code, field_list=fields)
    if data:
        result["data"] = data
    else:
        result["status"] = "error"
        result["message"] = f"未获取到 {args.code} 的更多信息"
    return result


def cmd_divid_factors(tq, args):
    result = {"status": "success", "data_type": "divid_factors", "code": args.code}
    df = tq.get_divid_factors(
        stock_code=args.code,
        start_time=args.start or "",
        end_time=args.end or ""
    )
    if df is not None and hasattr(df, "to_dict"):
        result["data"] = df.to_dict(orient="records")
    else:
        result["data"] = []
    return result


def cmd_gb_info(tq, args):
    result = {"status": "success", "data_type": "gb_info", "code": args.code}
    date_list = args.dates.split(",") if args.dates else []
    data = tq.get_gb_info(
        stock_code=args.code,
        date_list=date_list,
        count=len(date_list)
    )
    if data:
        result["data"] = data
    else:
        result["data"] = []
    return result


def main():
    parser = argparse.ArgumentParser(description="通达信行情数据获取")
    sub = parser.add_subparsers(dest="command", required=True)

    # snapshot
    p = sub.add_parser("snapshot", help="获取实时行情快照")
    p.add_argument("--code", required=True, help="证券代码，如 600519.SH")

    # kline
    p = sub.add_parser("kline", help="获取K线数据")
    p.add_argument("--code", required=True, help="证券代码，如 600519.SH")
    p.add_argument("--period", default="1d",
                   choices=["1m", "5m", "15m", "30m", "1h", "1d", "1w", "1mon", "1q", "1y", "tick"],
                   help="K线周期，默认1d")
    p.add_argument("--count", type=int, default=100, help="K线条数，默认100")
    p.add_argument("--fq", default="qfq", choices=["qfq", "hfq", "bfq"],
                   help="复权类型: qfq-前复权(默认), hfq-后复权, bfq-不复权")
    p.add_argument("--start", help="起始日期 YYYYMMDD")
    p.add_argument("--end", help="结束日期 YYYYMMDD")

    # stock_info
    p = sub.add_parser("stock_info", help="获取证券基本信息")
    p.add_argument("--code", required=True, help="证券代码，如 600519.SH")
    p.add_argument("--fields", default="", help="字段列表，逗号分隔，如 Name,J_zgb,J_jzc")

    # more_info
    p = sub.add_parser("more_info", help="获取股票更多信息(涨幅/PE/PB/市值等)")
    p.add_argument("--code", required=True, help="证券代码，如 600519.SH")
    p.add_argument("--fields", default="", help="字段列表，逗号分隔，如 zaf,dynape,pb_mrq,zsz")

    # divid_factors
    p = sub.add_parser("divid_factors", help="获取分红配送数据")
    p.add_argument("--code", required=True, help="证券代码，如 688318.SH")
    p.add_argument("--start", default="", help="起始日期 YYYYMMDD")
    p.add_argument("--end", default="", help="结束日期 YYYYMMDD")

    # gb_info
    p = sub.add_parser("gb_info", help="获取股本数据")
    p.add_argument("--code", required=True, help="证券代码，如 688318.SH")
    p.add_argument("--dates", default="", help="日期列表，逗号分隔，如 20250101,20250601")

    args = parser.parse_args()
    tq = init_tq()

    handlers = {
        "snapshot": cmd_snapshot,
        "kline": cmd_kline,
        "stock_info": cmd_stock_info,
        "more_info": cmd_more_info,
        "divid_factors": cmd_divid_factors,
        "gb_info": cmd_gb_info,
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
