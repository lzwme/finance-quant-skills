#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
交易日历获取脚本
"""

import argparse
import json
import sys
import os

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _tdx_init import init_tq


def main():
    parser = argparse.ArgumentParser(description="获取交易日列表")
    parser.add_argument("--start", default="", help="起始日期 YYYYMMDD")
    parser.add_argument("--end", default="", help="结束日期 YYYYMMDD")
    parser.add_argument("--count", type=int, default=-1,
                       help="返回最近N个交易日(count>0时从end往前取)")

    args = parser.parse_args()
    tq = init_tq()

    try:
        data = tq.get_trading_dates(
            market="sh",
            start_time=args.start or "",
            end_time=args.end or "",
            count=args.count
        )
        result = {
            "status": "success",
            "data_type": "trading_dates",
            "start": args.start,
            "end": args.end,
            "count": len(data) if data else 0,
            "data": data if data else []
        }
        print(json.dumps(result, ensure_ascii=False, indent=2, default=str))
    except Exception as e:
        print(json.dumps({
            "status": "error", "message": str(e), "error_type": type(e).__name__
        }, ensure_ascii=False))
        sys.exit(1)


if __name__ == "__main__":
    main()
