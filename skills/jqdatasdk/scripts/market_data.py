#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
行情数据获取脚本
支持获取价格、K线、实时数据、Tick数据
"""

import argparse
import json
import sys
import os
from datetime import datetime, timedelta

# 添加脚本目录到 Python 路径，支持独立运行
script_dir = os.path.dirname(os.path.abspath(__file__))
if script_dir not in sys.path:
    sys.path.insert(0, script_dir)

# 导入认证模块
from auth import auth_jq


def main():
    parser = argparse.ArgumentParser(description='获取聚宽A股行情数据')
    parser.add_argument('--type', required=True, choices=['price', 'current', 'ticks', 'order', 'future_ticks'],
                       help='数据类型: price-价格/K线, current-实时数据, ticks-Tick, order-委托, future_ticks-期货Tick')
    parser.add_argument('--code', required=True, help='股票代码，格式: 000001.XSHE 或 600000.XSHG')
    parser.add_argument('--start', help='开始日期，格式YYYY-MM-DD，如 2024-01-01')
    parser.add_argument('--end', help='结束日期，格式YYYY-MM-DD，如 2024-01-31')
    parser.add_argument('--frequency', default='daily',
                       choices=['1min', '5min', '15min', '30min', '60min', '120min', 'daily', 'weekly', 'monthly'],
                       help='数据频率，默认daily')
    parser.add_argument('--count', type=int, default=100, help='获取数量，默认100')
    parser.add_argument('--fields', help='字段列表，逗号分隔，如 open,close,high,low,volume')

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

        if args.type == 'price':
            if not args.start:
                args.end = datetime.now().strftime('%Y-%m-%d')
                args.start = (datetime.now() - timedelta(days=args.count)).strftime('%Y-%m-%d')

            # 默认字段
            default_fields = ['open', 'close', 'high', 'low', 'volume', 'money']
            fields = args.fields.split(',') if args.fields else default_fields

            data = jq.get_price(
                security=args.code,
                start_date=args.start,
                end_date=args.end,
                frequency=args.frequency,
                fields=fields
            )

            if data is not None and not data.empty:
                result['data'] = data.reset_index().to_dict('records')
                result['count'] = len(data)
            else:
                result['data'] = []
                result['count'] = 0

        elif args.type == 'current':
            if ',' in args.code:
                codes = args.code.split(',')
                data = jq.get_current_data()
                result['data'] = []
                if isinstance(data, dict):
                    for code in codes:
                        if code in data:
                            result['data'].append({
                                'code': code,
                                'last_price': data[code].last_price,
                                'time': data[code].time.strftime('%Y-%m-%d %H:%M:%S') if hasattr(data[code].time, 'strftime') else str(data[code].time),
                                'day_open': data[code].day_open,
                                'day_high': data[code].day_high,
                                'day_low': data[code].day_low,
                                'volume': data[code].volume,
                                'money': data[code].money
                            })
                result['count'] = len(result['data'])
            else:
                data = jq.get_current_data()
                if isinstance(data, dict) and args.code in data:
                    result['data'] = {
                        'code': args.code,
                        'last_price': data[args.code].last_price,
                        'time': data[args.code].time.strftime('%Y-%m-%d %H:%M:%S') if hasattr(data[args.code].time, 'strftime') else str(data[args.code].time),
                        'day_open': data[args.code].day_open,
                        'day_high': data[args.code].day_high,
                        'day_low': data[args.code].day_low,
                        'volume': data[args.code].volume,
                        'money': data[args.code].money
                    }
                else:
                    result['error'] = f'未获取到股票 {args.code} 的实时数据'

        elif args.type == 'ticks':
            if not args.start:
                args.end = datetime.now().strftime('%Y-%m-%d')
                args.start = args.end

            data = jq.get_ticks(
                security=args.code,
                start_dt=args.start,
                end_dt=args.end
            )

            tick_data = []
            if data:
                for tick in data:
                    tick_data.append({
                        'time': tick.time.strftime('%Y-%m-%d %H:%M:%S') if hasattr(tick.time, 'strftime') else str(tick.time),
                        'price': tick.price,
                        'volume': tick.volume,
                        'amount': tick.amount,
                        'direction': tick.direction if hasattr(tick, 'direction') else ''
                    })
            result['ticks'] = tick_data
            result['count'] = len(tick_data)

        elif args.type == 'order':
            if not args.start:
                args.end = datetime.now().strftime('%Y-%m-%d')
                args.start = args.end

            data = jq.get_order_book(
                security=args.code,
                start_dt=args.start,
                end_dt=args.end
            )

            order_data = []
            if data:
                for order in data:
                    order_data.append({
                        'time': order.time.strftime('%Y-%m-%d %H:%M:%S') if hasattr(order.time, 'strftime') else str(order.time),
                        'b_p_1': getattr(order, 'b_p_1', 0),
                        'b_v_1': getattr(order, 'b_v_1', 0),
                        'a_p_1': getattr(order, 'a_p_1', 0),
                        'a_v_1': getattr(order, 'a_v_1', 0),
                        'b_p_2': getattr(order, 'b_p_2', 0),
                        'b_v_2': getattr(order, 'b_v_2', 0),
                        'a_p_2': getattr(order, 'a_p_2', 0),
                        'a_v_2': getattr(order, 'a_v_2', 0),
                        'b_p_3': getattr(order, 'b_p_3', 0),
                        'b_v_3': getattr(order, 'b_v_3', 0),
                        'a_p_3': getattr(order, 'a_p_3', 0),
                        'a_v_3': getattr(order, 'a_v_3', 0)
                    })
            result['orders'] = order_data
            result['count'] = len(order_data)

        elif args.type == 'future_ticks':
            if not args.start:
                args.end = datetime.now().strftime('%Y-%m-%d')
                args.start = args.end

            data = jq.get_future_ticks(
                security=args.code,
                start_dt=args.start,
                end_dt=args.end
            )

            tick_data = []
            if data:
                for tick in data:
                    tick_data.append({
                        'time': tick.time.strftime('%Y-%m-%d %H:%M:%S') if hasattr(tick.time, 'strftime') else str(tick.time),
                        'price': tick.price,
                        'volume': tick.volume,
                        'amount': tick.amount
                    })
            result['ticks'] = tick_data
            result['count'] = len(tick_data)

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
