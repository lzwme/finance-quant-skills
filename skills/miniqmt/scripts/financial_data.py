#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
MiniQMT 财务数据获取脚本
支持：财务数据下载/获取、股东信息、股本数据
"""

import argparse
import json
import sys
import os

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from xtquant import xtdata
xtdata.enable_hello = False

def cmd_financial(args):
    """获取财务数据"""
    result = {
        "status": "success",
        "data_type": "financial",
        "code": args.code,
        "tables": args.tables
    }
    try:
        # 解析表格列表
        tables = [t.strip() for t in args.tables.split(',')] if args.tables else []

        # 下载财务数据
        xtdata.download_financial_data([args.code], tables)

        # 获取财务数据
        data = xtdata.get_financial_data(
            stock_list=[args.code],
            table_list=tables,
            start_time=args.start or '',
            end_time=args.end or '',
            report_type=args.report_type or 'report_time'
        )

        if args.code in data:
            result["data"] = {}
            for table_name, df in data[args.code].items():
                if df is not None and not df.empty:
                    result["data"][table_name] = {
                        "columns": df.columns.tolist(),
                        "data": df.to_dict('records')
                    }
                else:
                    result["data"][table_name] = {"columns": [], "data": []}
        else:
            result["data"] = {}
    except Exception as e:
        result["status"] = "error"
        result["message"] = str(e)
    return result


def cmd_download_financial(args):
    """下载财务数据"""
    result = {"status": "success", "data_type": "download_financial", "code": args.code}
    try:
        tables = [t.strip() for t in args.tables.split(',')] if args.tables else []
        xtdata.download_financial_data([args.code], tables)
        result["message"] = "下载完成"
    except Exception as e:
        result["status"] = "error"
        result["message"] = str(e)
    return result


def cmd_period_list(args):
    """获取可用周期列表"""
    result = {"status": "success", "data_type": "period_list"}
    try:
        periods = xtdata.get_period_list()
        result["data"] = periods
    except Exception as e:
        result["status"] = "error"
        result["message"] = str(e)
    return result


def add_args(parser):
    """添加命令行参数"""
    subparsers = parser.add_subparsers(dest='cmd', help='子命令')

    # financial
    p = subparsers.add_parser('financial', help='获取财务数据')
    p.add_argument('--code', '-c', required=True, help='证券代码')
    p.add_argument('--tables', '-t', default='Balance,Income,CashFlow', help='表格列表，逗号分隔')
    p.add_argument('--start', '-s', default='', help='起始时间 YYYYMMDD')
    p.add_argument('--end', '-e', default='', help='结束时间 YYYYMMDD')
    p.add_argument('--report_type', default='report_time', help='报告类型: report_time/announce_time')

    # download_financial
    p = subparsers.add_parser('download_financial', help='下载财务数据')
    p.add_argument('--code', '-c', required=True, help='证券代码')
    p.add_argument('--tables', '-t', default='', help='表格列表，逗号分隔')

    # period_list
    p = subparsers.add_parser('period_list', help='可用周期列表')


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='MiniQMT 财务数据获取')
    add_args(parser)
    args = parser.parse_args()

    cmd_map = {
        'financial': cmd_financial,
        'download_financial': cmd_download_financial,
        'period_list': cmd_period_list,
    }

    if args.cmd in cmd_map:
        result = cmd_map[args.cmd](args)
        print(json.dumps(result, ensure_ascii=False, indent=2))
    else:
        parser.print_help()
