#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
股票信息获取脚本
支持获取股票列表、交易日历、名称变更等
"""

import argparse
import json
import sys
import os
from datetime import datetime


def main():
    parser = argparse.ArgumentParser(description='获取 Tushare 股票信息')
    parser.add_argument('--type', required=True, choices=['stock_basic', 'trade_cal', 'namechange', 'trade_cal_ext', 'suspend'],
                       help='类型: stock_basic-股票列表, trade_cal-交易日历, namechange-名称变更, trade_cal_ext-交易日历扩展, suspend-停牌信息')
    parser.add_argument('--ts_code', help='股票代码，格式: 000001.SZ 或 600000.SH')
    parser.add_argument('--list_status', help='股票状态: L-上市, D-退市, P-暂停上市')
    parser.add_argument('--exchange', help='交易所: SSE-上交所, SZSE-深交所')
    parser.add_argument('--start_date', help='开始日期，格式YYYYMMDD')
    parser.add_argument('--end_date', help='结束日期，格式YYYYMMDD')
    parser.add_argument('--exchange_id', help='交易所ID: SSE-上交所, SZSE-深交所')
    parser.add_argument('--is_open', help='是否开市: 0-休市, 1-开市')

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

        params = {}

        if args.type == 'stock_basic':
            # 股票列表
            if args.ts_code:
                params['ts_code'] = args.ts_code
            if args.list_status:
                params['list_status'] = args.list_status
            if args.exchange:
                params['exchange'] = args.exchange

            data = pro.stock_basic(**params)

        elif args.type == 'trade_cal':
            # 交易日历
            if args.exchange_id:
                params['exchange'] = args.exchange_id
            if args.start_date:
                params['start_date'] = args.start_date
            if args.end_date:
                params['end_date'] = args.end_date
            if args.is_open:
                params['is_open'] = args.is_open

            data = pro.trade_cal(**params)

        elif args.type == 'namechange':
            # 名称变更
            if args.ts_code:
                params['ts_code'] = args.ts_code
            if args.start_date:
                params['start_date'] = args.start_date
            if args.end_date:
                params['end_date'] = args.end_date

            data = pro.namechange(**params)

        elif args.type == 'trade_cal_ext':
            # 交易日历扩展
            if args.exchange_id:
                params['exchange'] = args.exchange_id
            if args.start_date:
                params['start_date'] = args.start_date
            if args.end_date:
                params['end_date'] = args.end_date
            if args.is_open:
                params['is_open'] = args.is_open

            data = pro.trade_cal_ext(**params)

        elif args.type == 'suspend':
            # 停牌信息
            if args.ts_code:
                params['ts_code'] = args.ts_code
            if args.start_date:
                params['start_date'] = args.start_date
            if args.end_date:
                params['end_date'] = args.end_date

            data = pro.suspend(**params)

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
