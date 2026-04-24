#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
因子数据获取脚本
支持获取估值因子、情绪因子、技术因子、成长因子等
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
    parser = argparse.ArgumentParser(description='获取聚宽因子数据')
    parser.add_argument('--code', required=True, help='股票代码，格式: 000001.XSHE 或 600000.XSHG，多个用逗号分隔')
    parser.add_argument('--factor', required=True,
                       choices=['valuation', 'turnover', 'basic', 'technical', 'growth', 'momentum', 'size'],
                       help='因子类型: valuation-估值, turnover-换手率, basic-基础, technical-技术, growth-成长, momentum-动量, size-规模')
    parser.add_argument('--start', help='开始日期，格式YYYY-MM-DD，如 2024-01-01')
    parser.add_argument('--end', help='结束日期，格式YYYY-MM-DD，如 2024-12-31')

    args = parser.parse_args()

    try:
        # 使用统一认证模块进行认证
        jq = auth_jq()

        # 设置默认日期范围
        if not args.start:
            args.start = (datetime.now() - timedelta(days=30)).strftime('%Y-%m-%d')
        if not args.end:
            args.end = datetime.now().strftime('%Y-%m-%d')

        codes = args.code.split(',')

        result = {
            'status': 'success',
            'factor_type': args.factor,
            'code': args.code,
            'start_date': args.start,
            'end_date': args.end,
            'timestamp': datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        }

        if args.factor == 'valuation':
            # 估值因子
            query = jq.query(jq.valuation.code,
                            jq.valuation.day,
                            jq.valuation.market_cap,
                            jq.valuation.circulating_market_cap,
                            jq.valuation.pe_ratio,
                            jq.valuation.pb_ratio,
                            jq.valuation.pcf_ratio,
                            jq.valuation.ps_ratio,
                            jq.valuation.turnover_ratio)

            query = query.filter(jq.valuation.code.in_(codes))
            query = query.filter(jq.valuation.day >= args.start)
            query = query.filter(jq.valuation.day <= args.end)

            df = jq.finance.run_query(query)

            if df is not None and not df.empty:
                result['data'] = df.to_dict('records')
                result['count'] = len(df)
            else:
                result['data'] = []
                result['count'] = 0

        elif args.factor == 'turnover':
            # 换手率因子
            query = jq.query(jq.valuation.code,
                            jq.valuation.day,
                            jq.valuation.turnover_ratio,
                            jq.valuation.circulating_market_cap)

            query = query.filter(jq.valuation.code.in_(codes))
            query = query.filter(jq.valuation.day >= args.start)
            query = query.filter(jq.valuation.day <= args.end)

            df = jq.finance.run_query(query)

            if df is not None and not df.empty:
                result['data'] = df.to_dict('records')
                result['count'] = len(df)
            else:
                result['data'] = []
                result['count'] = 0

        elif args.factor == 'basic':
            # 基础因子
            query = jq.query(jq.valuation.code,
                            jq.valuation.day,
                            jq.valuation.market_cap,
                            jq.valuation.circulating_market_cap,
                            jq.valuation.pe_ratio,
                            jq.valuation.pb_ratio)

            query = query.filter(jq.valuation.code.in_(codes))
            query = query.filter(jq.valuation.day >= args.start)
            query = query.filter(jq.valuation.day <= args.end)

            df = jq.finance.run_query(query)

            if df is not None and not df.empty:
                result['data'] = df.to_dict('records')
                result['count'] = len(df)
            else:
                result['data'] = []
                result['count'] = 0

        elif args.factor == 'technical':
            # 技术因子（通过价格数据计算）
            prices = jq.get_price(
                security=codes,
                start_date=args.start,
                end_date=args.end,
                frequency='daily',
                fields=['open', 'close', 'high', 'low', 'volume', 'money']
            )

            if prices is not None and not prices.empty:
                # 计算简单技术指标
                import pandas as pd
                df = prices.reset_index()

                # 按代码分组计算
                result_list = []
                for code in codes:
                    code_df = df[df['code'] == code].copy()
                    if not code_df.empty:
                        code_df = code_df.sort_values('time')
                        # 计算5日、20日移动平均
                        code_df['ma5'] = code_df['close'].rolling(window=5).mean()
                        code_df['ma20'] = code_df['close'].rolling(window=20).mean()
                        # 计算振幅
                        code_df['amplitude'] = (code_df['high'] - code_df['low']) / code_df['close'] * 100
                        # 计算涨跌幅
                        code_df['change_pct'] = code_df['close'].pct_change() * 100

                        result_list.extend(code_df.to_dict('records'))

                result['data'] = result_list
                result['count'] = len(result_list)
            else:
                result['data'] = []
                result['count'] = 0

        elif args.factor == 'growth':
            # 成长因子（需要财务数据）
            query = jq.query(jq.indicator.code,
                            jq.indicator.statDate,
                            jq.indicator.inc_return,
                            jq.indicator.inc_revenue_year_on_year,
                            jq.indicator.roe)

            query = query.filter(jq.indicator.code.in_(codes))

            if args.start:
                query = query.filter(jq.indicator.statDate >= args.start.replace('-', ''))
            if args.end:
                query = query.filter(jq.indicator.statDate <= args.end.replace('-', ''))

            df = jq.finance.run_query(query)

            if df is not None and not df.empty:
                result['data'] = df.to_dict('records')
                result['count'] = len(df)
            else:
                result['data'] = []
                result['count'] = 0

        elif args.factor == 'momentum':
            # 动量因子（通过价格数据计算）
            prices = jq.get_price(
                security=codes,
                start_date=args.start,
                end_date=args.end,
                frequency='daily',
                fields=['close', 'volume']
            )

            if prices is not None and not prices.empty:
                import pandas as pd
                df = prices.reset_index()

                result_list = []
                for code in codes:
                    code_df = df[df['code'] == code].copy()
                    if not code_df.empty:
                        code_df = code_df.sort_values('time')
                        # 计算5日、20日、60日收益率
                        code_df['return_5d'] = code_df['close'].pct_change(5) * 100
                        code_df['return_20d'] = code_df['close'].pct_change(20) * 100
                        code_df['return_60d'] = code_df['close'].pct_change(60) * 100
                        # 计算波动率
                        code_df['volatility'] = code_df['close'].pct_change().rolling(window=20).std() * 100

                        result_list.extend(code_df.to_dict('records'))

                result['data'] = result_list
                result['count'] = len(result_list)
            else:
                result['data'] = []
                result['count'] = 0

        elif args.factor == 'size':
            # 规模因子
            query = jq.query(jq.valuation.code,
                            jq.valuation.day,
                            jq.valuation.market_cap,
                            jq.valuation.circulating_market_cap)

            query = query.filter(jq.valuation.code.in_(codes))
            query = query.filter(jq.valuation.day >= args.start)
            query = query.filter(jq.valuation.day <= args.end)

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
