#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
股票信息获取脚本
支持获取股票列表、股票信息、基金列表等
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
    parser = argparse.ArgumentParser(description='获取聚宽股票信息')
    parser.add_argument('--type', required=True, choices=['all_securities', 'get_security_info', 'trade_days'],
                       help='类型: all_securities-获取证券列表, get_security_info-获取证券信息, trade_days-获取交易日')
    parser.add_argument('--security_type', default='stock',
                       choices=['stock', 'fund', 'index', 'etf', 'futures', 'all'],
                       help='证券类型，默认stock')
    parser.add_argument('--code', help='证券代码，格式: 000001.XSHE 或 600000.XSHG')
    parser.add_argument('--start', help='开始日期，格式YYYY-MM-DD，如 2024-01-01')
    parser.add_argument('--end', help='结束日期，格式YYYY-MM-DD，如 2024-12-31')

    args = parser.parse_args()

    try:
        # 使用统一认证模块进行认证
        jq = auth_jq()

        result = {
            'status': 'success',
            'data_type': args.type,
            'timestamp': datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        }

        if args.type == 'all_securities':
            # 获取证券列表
            if args.security_type == 'all':
                securities = jq.get_all_securities()
            else:
                securities = jq.get_all_securities(types=[args.security_type])

            if securities is not None and not securities.empty:
                result['data'] = securities.reset_index().to_dict('records')
                result['count'] = len(securities)
            else:
                result['data'] = []
                result['count'] = 0

        elif args.type == 'get_security_info':
            if not args.code:
                result['error'] = '请提供 --code 参数'
            else:
                info = jq.get_security_info(args.code)
                if info:
                    result['data'] = {
                        'code': info.code,
                        'display_name': info.display_name,
                        'name': info.name,
                        'start_date': info.start_date.strftime('%Y-%m-%d') if hasattr(info.start_date, 'strftime') else str(info.start_date),
                        'end_date': info.end_date.strftime('%Y-%m-%d') if info.end_date and hasattr(info.end_date, 'strftime') else str(info.end_date) if info.end_date else None,
                        'type': info.type,
                        'parent': info.parent
                    }
                else:
                    result['error'] = f'未找到证券 {args.code} 的信息'

        elif args.type == 'trade_days':
            if not args.start or not args.end:
                result['error'] = '请提供 --start 和 --end 参数'
            else:
                trade_days = jq.get_trade_days(start_date=args.start, end_date=args.end)
                result['trade_days'] = [day.strftime('%Y-%m-%d') for day in trade_days] if trade_days else []
                result['count'] = len(result['trade_days']) if result['trade_days'] else 0

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
