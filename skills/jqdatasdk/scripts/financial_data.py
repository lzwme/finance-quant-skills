#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
财务数据获取脚本
支持获取财务数据、指标数据、估值数据
"""

import argparse
import json
import sys
import os
from datetime import datetime

# 添加脚本目录到 Python 路径，支持独立运行
script_dir = os.path.dirname(os.path.abspath(__file__))
if script_dir not in sys.path:
    sys.path.insert(0, script_dir)

# 导入认证模块
from auth import auth_jq


def main():
    parser = argparse.ArgumentParser(description='获取聚宽财务数据')
    parser.add_argument('--type', required=True, choices=['fundamentals', 'indicators', 'valuation'],
                       help='数据类型: fundamentals-财务数据, indicators-指标数据, valuation-估值数据')
    parser.add_argument('--code', required=True, help='股票代码，格式: 000001.XSHE 或 600000.XSHG，多个用逗号分隔')
    parser.add_argument('--statDate', help='报告期，格式YYYY或YYYY-MM-DD，如 2024 或 2024-03-31')
    parser.add_argument('--columns', help='字段列表，逗号分隔，如 pe_ratio, pb_ratio')

    args = parser.parse_args()

    try:
        # 使用统一认证模块进行认证
        jq = auth_jq()

        result = {
            'status': 'success',
            'data_type': args.type,
            'code': args.code,
            'timestamp': datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        }

        codes = args.code.split(',')

        if args.type == 'fundamentals':
            # 财务数据
            query = jq.query(jq.finance.STK_BALANCE_SHEET)

            if args.statDate:
                query = query.filter(jq.finance.STK_BALANCE_SHEET.statDate == args.statDate)

            query = query.filter(jq.finance.STK_BALANCE_SHEET.code.in_(codes))

            if args.columns:
                columns = args.columns.split(',')
                query = query.filter(*[getattr(jq.finance.STK_BALANCE_SHEET, col) != None for col in columns])

            df = jq.finance.run_query(query)

            if df is not None and not df.empty:
                result['data'] = df.to_dict('records')
                result['count'] = len(df)
            else:
                result['data'] = []
                result['count'] = 0

        elif args.type == 'indicators':
            # 指标数据
            query = jq.query(jq.indicator)

            if args.statDate:
                query = query.filter(jq.indicator.statDate == args.statDate)

            query = query.filter(jq.indicator.code.in_(codes))

            df = jq.finance.run_query(query)

            if df is not None and not df.empty:
                result['data'] = df.to_dict('records')
                result['count'] = len(df)
            else:
                result['data'] = []
                result['count'] = 0

        elif args.type == 'valuation':
            # 估值数据
            query = jq.query(jq.valuation)

            if args.statDate:
                query = query.filter(jq.valuation.day == args.statDate)
            else:
                # 获取最新估值数据
                query = query.order_by(jq.valuation.day.desc())

            query = query.filter(jq.valuation.code.in_(codes))

            if args.columns:
                selected_columns = ['code', 'day'] + args.columns.split(',')
                df = jq.finance.run_query(query)
                if df is not None and not df.empty:
                    df = df[selected_columns]
            else:
                df = jq.finance.run_query(query)

            if df is not None and not df.empty:
                result['data'] = df.to_dict('records')
                result['count'] = len(df)
            else:
                result['data'] = []
                result['count'] = 0

        print(json.dumps(result, ensure_ascii=False, indent=2))

    except ImportError:
        print(json.dumps({
            'status': 'error',
            'message': 'jqdatasdk 库未安装，请先安装: pip install jqdatasdk'
        }, ensure_ascii=False))
        sys.exit(1)
    except Exception as e:
        print(json.dumps({
            'status': 'error',
            'message': str(e),
            'error_type': type(e).__name__
        }, ensure_ascii=False))
        sys.exit(1)


if __name__ == '__main__':
    main()
