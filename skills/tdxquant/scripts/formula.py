#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
通达信公式执行脚本
支持：技术指标(zb)、条件选股(xg)、专家系统(exp)、批量选股(mul_xg)、批量指标(mul_zb)
"""

import argparse
import json
import sys
import os

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _tdx_init import init_tq


def cmd_zb(tq, args):
    """调用技术指标公式"""
    # 先设置公式数据
    dividend_map = {"bfq": 0, "qfq": 1, "hfq": 2}
    dividend_type = dividend_map.get(args.fq, 1)

    set_res = tq.formula_set_data_info(
        stock_code=args.code,
        stock_period=args.period,
        start_time=args.start or "",
        end_time=args.end or "",
        count=args.count,
        dividend_type=dividend_type
    )

    if set_res and set_res.get("errorid", "-1") != "0":
        return {"status": "error", "message": f"设置公式数据失败: {set_res}"}

    data = tq.formula_zb(
        formula_name=args.name,
        formula_arg=args.arg,
        xsflag=args.xsflag
    )
    return {"status": "success", "data_type": "formula_zb", "formula": args.name, "data": data}


def cmd_xg(tq, args):
    """调用条件选股公式"""
    dividend_map = {"bfq": 0, "qfq": 1, "hfq": 2}
    dividend_type = dividend_map.get(args.fq, 1)

    set_res = tq.formula_set_data_info(
        stock_code=args.code,
        stock_period=args.period,
        start_time=args.start or "",
        end_time=args.end or "",
        count=args.count,
        dividend_type=dividend_type
    )

    if set_res and set_res.get("errorid", "-1") != "0":
        return {"status": "error", "message": f"设置公式数据失败: {set_res}"}

    data = tq.formula_xg(
        formula_name=args.name,
        formula_arg=args.arg
    )
    return {"status": "success", "data_type": "formula_xg", "formula": args.name, "data": data}


def cmd_exp(tq, args):
    """调用专家系统公式"""
    dividend_map = {"bfq": 0, "qfq": 1, "hfq": 2}
    dividend_type = dividend_map.get(args.fq, 1)

    set_res = tq.formula_set_data_info(
        stock_code=args.code,
        stock_period=args.period,
        start_time=args.start or "",
        end_time=args.end or "",
        count=args.count,
        dividend_type=dividend_type
    )

    if set_res and set_res.get("errorid", "-1") != "0":
        return {"status": "error", "message": f"设置公式数据失败: {set_res}"}

    data = tq.formula_exp(
        formula_name=args.name,
        formula_arg=args.arg
    )
    return {"status": "success", "data_type": "formula_exp", "formula": args.name, "data": data}


def cmd_mul_xg(tq, args):
    """批量调用条件选股公式"""
    stock_list = args.codes.split(",") if args.codes else []
    dividend_map = {"bfq": 0, "qfq": 1, "hfq": 2}
    dividend_type = dividend_map.get(args.fq, 1)

    data = tq.formula_process_mul_xg(
        formula_name=args.name,
        formula_arg=args.arg,
        return_count=args.return_count,
        return_date=True,
        stock_list=stock_list,
        stock_period=args.period,
        start_time=args.start or "",
        end_time=args.end or "",
        count=args.count,
        dividend_type=dividend_type
    )
    return {"status": "success", "data_type": "formula_mul_xg", "formula": args.name, "data": data}


def cmd_mul_zb(tq, args):
    """批量调用技术指标公式"""
    stock_list = args.codes.split(",") if args.codes else []
    dividend_map = {"bfq": 0, "qfq": 1, "hfq": 2}
    dividend_type = dividend_map.get(args.fq, 1)

    data = tq.formula_process_mul_zb(
        formula_name=args.name,
        formula_arg=args.arg,
        xsflag=args.xsflag,
        return_count=args.return_count,
        return_date=True,
        stock_list=stock_list,
        stock_period=args.period,
        start_time=args.start or "",
        end_time=args.end or "",
        count=args.count,
        dividend_type=dividend_type
    )
    return {"status": "success", "data_type": "formula_mul_zb", "formula": args.name, "data": data}


def main():
    parser = argparse.ArgumentParser(description="通达信公式执行")
    sub = parser.add_subparsers(dest="command", required=True)

    # 通用参数
    common = argparse.ArgumentParser(add_help=False)
    common.add_argument("--name", required=True, help="公式名称，如 MACD, KDJ, UPN")
    common.add_argument("--arg", default="", help="公式参数，逗号分隔，如 12,26,9")
    common.add_argument("--code", default="", help="证券代码(zb/xg/exp时)，如 688318.SH")
    common.add_argument("--codes", default="", help="证券代码列表(mul时)，逗号分隔")
    common.add_argument("--period", default="1d",
                       choices=["1m", "5m", "15m", "30m", "1h", "1d", "1w", "1mon"],
                       help="K线周期，默认1d")
    common.add_argument("--count", type=int, default=100, help="K线数量，默认100")
    common.add_argument("--start", default="", help="起始日期 YYYYMMDD")
    common.add_argument("--end", default="", help="结束日期 YYYYMMDD")
    common.add_argument("--fq", default="qfq", choices=["qfq", "hfq", "bfq"],
                       help="复权类型: qfq-前复权(默认), hfq-后复权, bfq-不复权")
    common.add_argument("--xsflag", type=int, default=-1, help="数据精度，-1为默认")
    common.add_argument("--return_count", type=int, default=1, help="批量调用时每个返回值的返回数")

    sub.add_parser("zb", parents=[common], help="调用技术指标公式")
    sub.add_parser("xg", parents=[common], help="调用条件选股公式")
    sub.add_parser("exp", parents=[common], help="调用专家系统公式")
    sub.add_parser("mul_xg", parents=[common], help="批量调用条件选股公式")
    sub.add_parser("mul_zb", parents=[common], help="批量调用技术指标公式")

    args = parser.parse_args()
    tq = init_tq()

    handlers = {
        "zb": cmd_zb,
        "xg": cmd_xg,
        "exp": cmd_exp,
        "mul_xg": cmd_mul_xg,
        "mul_zb": cmd_mul_zb,
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
