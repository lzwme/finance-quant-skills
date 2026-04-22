#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
行情数据获取脚本
支持获取日线行情、复权因子、分钟线数据
"""

import argparse
import json
import sys
import os
from datetime import datetime


def main():
    parser = argparse.ArgumentParser(description='获取 Tushare 行情数据')
    parser.add_argument('--type', required=True, choices=['daily', 'adj_factor', 'daily_basic', 'weekly', 'monthly'],
                       help='数据类型: daily-日线, adj_factor-复权因子, daily_basic-每日指标, weekly-周线, monthly-月线')
    parser.add_argument('--ts_code', help='股票代码，格式: 000001.SZ 或 600000.SH，多个用逗号分隔')
    parser.add_argument('--start_date', help='开始日期，格式YYYYMMDD，如 20240101')
    parser.add_argument('--end_date', help='结束日期，格式YYYYMMDD，如 20240131')
    parser.add_argument('--trade_date', help='交易日，格式YYYYMMDD，单日数据查询')
    parser.add_argument('--fields', help='字段列表，逗号分隔，如 ts_code,trade_date,open,high,low,close,vol')

    args = parser.parse_args()

    try:
        # 获取凭证
        credential = os.getenv(f"TUSHARE_TOKEN")
        if not credential:
            print(json.dumps({
                'status': 'error',
                'message': '缺少 Tushare Token 凭证配置，请先配置 TUSHARE_TOKEN 凭证'
            }, ensure_ascii=False))
            sys.exit(1)

        import tushare as ts

        # 初始化
        pro = ts.pro_api(credential)

        result = {
            'status': 'success',
            'data_type': args.type,
            'timestamp': datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        }

        if args.type == 'daily':
            # 日线行情
            params = {}
            if args.ts_code:
                params['ts_code'] = args.ts_code
            if args.start_date:
                params['start_date'] = args.start_date
            if args.end_date:
                params['end_date'] = args.end_date
            if args.trade_date:
                params['trade_date'] = args.trade_date
            if args.fields:
                params['fields'] = args.fields

            data = pro.daily(**params)

            if data is not None and not data.empty:
                result['data'] = data.to_dict('records')
                result['count'] = len(data)
            else:
                result['data'] = []
                result['count'] = 0

        elif args.type == 'adj_factor':
            # 复权因子
            params = {}
            if args.ts_code:
                params['ts_code'] = args.ts_code
            if args.start_date:
                params['start_date'] = args.start_date
            if args.end_date:
                params['end_date'] = args.end_date
            if args.trade_date:
                params['trade_date'] = args.trade_date

            data = pro.adj_factor(**params)

            if data is not None and not data.empty:
                result['data'] = data.to_dict('records')
                result['count'] = len(data)
            else:
                result['data'] = []
                result['count'] = 0

        elif args.type == 'daily_basic':
            # 每日指标
            params = {}
            if args.ts_code:
                params['ts_code'] = args.ts_code
            if args.start_date:
                params['start_date'] = args.start_date
            if args.end_date:
                params['end_date'] = args.end_date
            if args.trade_date:
                params['trade_date'] = args.trade_date
            if args.fields:
                params['fields'] = args.fields

            data = pro.daily_basic(**params)

            if data is not None and not data.empty:
                result['data'] = data.to_dict('records')
                result['count'] = len(data)
            else:
                result['data'] = []
                result['count'] = 0

        elif args.type == 'weekly':
            # 周线行情
            params = {}
            if args.ts_code:
                params['ts_code'] = args.ts_code
            if args.start_date:
                params['start_date'] = args.start_date
            if args.end_date:
                params['end_date'] = args.end_date
            if args.trade_date:
                params['trade_date'] = args.trade_date
            if args.fields:
                params['fields'] = args.fields

            data = pro.weekly(**params)

            if data is not None and not data.empty:
                result['data'] = data.to_dict('records')
                result['count'] = len(data)
            else:
                result['data'] = []
                result['count'] = 0

        elif args.type == 'monthly':
            # 月线行情
            params = {}
            if args.ts_code:
                params['ts_code'] = args.ts_code
            if args.start_date:
                params['start_date'] = args.start_date
            if args.end_date:
                params['end_date'] = args.end_date
            if args.trade_date:
                params['trade_date'] = args.trade_date
            if args.fields:
                params['fields'] = args.fields

            data = pro.monthly(**params)

            if data is not None and not data.empty:
                result['data'] = data.to_dict('records')
                result['count'] = len(data)
            else:
                result['data'] = []
                result['count'] = 0

        print(json.dumps(result, ensure_ascii=False, indent=2))

    except ImportError:
        print(json.dumps({
            'status': 'error',
            'message': 'tushare 库未安装，请先安装: pip install tushare'
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
