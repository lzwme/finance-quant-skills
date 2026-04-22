#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
宏观数据与指数数据获取脚本
支持获取指数行情、指数基础信息、Shibor 利率等
"""

import argparse
import json
import sys
import os
from datetime import datetime


def main():
    parser = argparse.ArgumentParser(description='获取 Tushare 指数与宏观数据')
    parser.add_argument('--type', required=True,
                       choices=['index_daily', 'index_basic', 'index_classify', 'index_daily_basic', 'shibor', 'shibor_rate', 'shibor_quote'],
                       help='类型: index_daily-指数行情, index_basic-指数基础信息, index_classify-指数分类, index_daily_basic-指数每日指标, shibor-Shibor, shibor_rate-Shibor利率, shibor_quote-Shibor报价')
    parser.add_argument('--ts_code', help='指数代码，格式: 000001.SH 或 399001.SZ')
    parser.add_argument('--start_date', help='开始日期，格式YYYYMMDD')
    parser.add_argument('--end_date', help='结束日期，格式YYYYMMDD')
    parser.add_argument('--trade_date', help='交易日，格式YYYYMMDD')
    parser.add_argument('--market', help='市场:主板/中小板/创业板/科创板等')
    def main():
    parser.add_argument('--level', help='级别: L1-大, L2-中, L3-小')

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

        if args.type == 'index_daily':
            # 指数行情
            if args.ts_code:
                params['ts_code'] = args.ts_code
            if args.start_date:
                params['start_date'] = args.start_date
            if args.end_date:
                params['end_date'] = args.end_date
            if args.trade_date:
                params['trade_date'] = args.trade_date

            data = pro.index_daily(**params)

        elif args.type == 'index_basic':
            # 指数基础信息
            if args.ts_code:
                params['ts_code'] = args.ts_code
            if args.market:
                params['market'] = args.market
            if args.level:
                params['level'] = args.level

            data = pro.index_basic(**params)

        elif args.type == 'index_classify':
            # 指数分类
            if args.market:
                params['market'] = args.market
            if args.level:
                params['level'] = args.level

            data = pro.index_classify(**params)

        elif args.type == 'index_daily_basic':
            # 指数每日指标
            if args.ts_code:
                params['ts_code'] = args.ts_code
            if args.start_date:
                params['start_date'] = args.start_date
            if args.end_date:
                params['end_date'] = args.end_date
            if args.trade_date:
                params['trade_date'] = args.trade_date

            data = pro.index_daily_basic(**params)

        elif args.type == 'shibor':
            # Shibor 数据
            if args.start_date:
                params['start_date'] = args.start_date
            if args.end_date:
                params['end_date'] = args.end_date
            if args.trade_date:
                params['trade_date'] = args.trade_date

            data = pro.shibor(**params)

        elif args.type == 'shibor_rate':
            # Shibor 利率
            if args.start_date:
                params['start_date'] = args.start_date
            if args.end_date:
                params['end_date'] = args.end_date

            data = pro.shibor_rate(**params)

        elif args.type == 'shibor_quote':
            # Shibor 报价
            if args.start_date:
                params['start_date'] = args.start_date
            if args.end_date:
                params['end_date'] = args.end_date

            data = pro.shibor_quote(**params)

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
