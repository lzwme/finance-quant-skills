#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
股票信息获取脚本
支持获取股票列表、行业分类、指数成分股、交易日历等
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
from auth import auth_bs, logout_bs


def main():
    parser = argparse.ArgumentParser(description='获取 BaoStock 股票信息')
    parser.add_argument('--type', required=True, 
                       choices=['all_stocks', 'stock_info', 'trade_dates', 'industry', 
                               'index_stocks', 'dividend'],
                       help='类型: all_stocks-全部股票列表, stock_info-股票基本信息, '
                            'trade_dates-交易日历, industry-行业分类, '
                            'index_stocks-指数成分股, dividend-分红信息')
    parser.add_argument('--date', help='查询日期，格式YYYY-MM-DD，默认今天')
    parser.add_argument('--code', help='股票代码，格式: sh.600000 或 sz.000001')
    parser.add_argument('--index', choices=['hs300', 'sz50', 'zz500'],
                       help='指数类型: hs300=沪深300, sz50=上证50, zz500=中证500')
    parser.add_argument('--start', help='开始日期，格式YYYY-MM-DD')
    parser.add_argument('--end', help='结束日期，格式YYYY-MM-DD')
    parser.add_argument('--year', help='分红查询年份，如 2023')
    parser.add_argument('--output', help='输出CSV文件路径')
    
    args = parser.parse_args()
    
    try:
        # 使用统一认证模块进行登录
        bs = auth_bs()
        
        result = {
            'status': 'success',
            'data_type': args.type,
            'timestamp': datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        }
        
        if args.type == 'all_stocks':
            # 获取全部证券列表
            query_date = args.date or datetime.now().strftime('%Y-%m-%d')
            rs = bs.query_all_stock(day=query_date)
            
            data = []
            if rs.error_code == '0':
                while rs.next():
                    row = rs.get_row_data()
                    data.append({
                        'code': row[0],
                        'tradeStatus': row[1],
                        'code_name': row[2]
                    })
            
            result['data'] = data
            result['count'] = len(data)
            result['date'] = query_date
            
        elif args.type == 'stock_info':
            # 获取股票基本信息
            if not args.code:
                result['error'] = '请提供 --code 参数'
            else:
                rs = bs.query_stock_basic(code=args.code)
                
                if rs.error_code == '0' and rs.next():
                    row = rs.get_row_data()
                    result['data'] = {
                        'code': row[0],
                        'code_name': row[1],
                        'ipoDate': row[2],
                        'outDate': row[3],
                        'type': row[4],
                        'status': row[5]
                    }
                else:
                    result['error'] = f'未找到股票 {args.code} 的信息'
                    
        elif args.type == 'trade_dates':
            # 获取交易日历
            if not args.start or not args.end:
                result['error'] = '请提供 --start 和 --end 参数'
            else:
                rs = bs.query_trade_dates(start_date=args.start, end_date=args.end)
                
                data = []
                if rs.error_code == '0':
                    while rs.next():
                        row = rs.get_row_data()
                        data.append({
                            'calendar_date': row[0],
                            'is_trading_day': row[1]
                        })
                
                result['data'] = data
                result['count'] = len(data)
                # 统计交易日数量
                trade_days = [d for d in data if d['is_trading_day'] == '1']
                result['trade_days_count'] = len(trade_days)
                
        elif args.type == 'industry':
            # 获取行业分类
            rs = bs.query_stock_industry()
            
            data = []
            if rs.error_code == '0':
                while rs.next():
                    row = rs.get_row_data()
                    data.append({
                        'updateDate': row[0],
                        'code': row[1],
                        'code_name': row[2],
                        'industry': row[3],
                        'industryClassification': row[4]
                    })
            
            result['data'] = data
            result['count'] = len(data)
            
        elif args.type == 'index_stocks':
            # 获取指数成分股
            if not args.index:
                result['error'] = '请提供 --index 参数 (hs300/sz50/zz500)'
            else:
                if args.index == 'hs300':
                    rs = bs.query_hs300_stocks()
                elif args.index == 'sz50':
                    rs = bs.query_sz50_stocks()
                elif args.index == 'zz500':
                    rs = bs.query_zz500_stocks()
                else:
                    rs = None
                
                if rs and rs.error_code == '0':
                    data = []
                    while rs.next():
                        row = rs.get_row_data()
                        data.append({
                            'code': row[0],
                            'code_name': row[1]
                        })
                    
                    result['data'] = data
                    result['count'] = len(data)
                    result['index'] = args.index
                else:
                    result['error'] = f'获取指数 {args.index} 成分股失败'
                    
        elif args.type == 'dividend':
            # 获取分红信息
            if not args.code:
                result['error'] = '请提供 --code 参数'
            else:
                year = args.year or datetime.now().strftime('%Y')
                rs = bs.query_dividend_data(code=args.code, year=year, yearType="report")
                
                data = []
                if rs.error_code == '0':
                    while rs.next():
                        row = rs.get_row_data()
                        data.append(dict(zip(rs.fields, row)))
                
                result['data'] = data
                result['count'] = len(data)
                result['code'] = args.code
                result['year'] = year
        
        # 保存到 CSV
        if args.output and 'data' in result and result['data']:
            import pandas as pd
            if isinstance(result['data'], list):
                df = pd.DataFrame(result['data'])
            else:
                df = pd.DataFrame([result['data']])
            df.to_csv(args.output, index=False, encoding='utf-8-sig')
            result['output_file'] = args.output
        
        print(json.dumps(result, ensure_ascii=False, indent=2))
        
        # 登出
        logout_bs(bs)
        
    except ImportError as e:
        print(json.dumps({
            'status': 'error',
            'message': f'导入错误: {str(e)}，请检查 baostock 是否已安装'
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
