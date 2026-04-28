#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
财务数据获取脚本
支持获取盈利能力、营运能力、成长能力、偿债能力、现金流、杜邦分析等数据
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


def query_financial_data(bs, query_func, code, year, quarter):
    """
    通用财务数据查询函数
    
    Args:
        bs: baostock 模块
        query_func: 查询函数
        code: 股票代码
        year: 年份
        quarter: 季度 1/2/3/4
    
    Returns:
        dict: 财务数据字典
    """
    rs = query_func(code=code, year=year, quarter=quarter)
    
    if rs.error_code == '0' and rs.next():
        row = rs.get_row_data()
        return dict(zip(rs.fields, row))
    return None


def main():
    parser = argparse.ArgumentParser(description='获取 BaoStock 财务数据')
    parser.add_argument('--type', required=True,
                       choices=['profit', 'operation', 'growth', 'balance', 
                               'cash_flow', 'dupont', 'all'],
                       help='财务数据类型: '
                            'profit-盈利能力, operation-营运能力, '
                            'growth-成长能力, balance-偿债能力, '
                            'cash_flow-现金流, dupont-杜邦分析, '
                            'all-获取全部财务指标')
    parser.add_argument('--code', required=True,
                       help='股票代码，格式: sh.600000 或 sz.000001')
    parser.add_argument('--year', required=True, type=int,
                       help='查询年份，如 2023')
    parser.add_argument('--quarter', required=True, type=int,
                       choices=[1, 2, 3, 4],
                       help='查询季度: 1/2/3/4')
    parser.add_argument('--output', help='输出CSV文件路径')
    
    args = parser.parse_args()
    
    try:
        # 使用统一认证模块进行登录
        bs = auth_bs()
        
        result = {
            'status': 'success',
            'data_type': args.type,
            'code': args.code,
            'year': args.year,
            'quarter': args.quarter,
            'timestamp': datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        }
        
        if args.type == 'profit' or args.type == 'all':
            # 盈利能力
            data = query_financial_data(
                bs, bs.query_profit_data, args.code, args.year, args.quarter
            )
            if data:
                result['profit'] = data
            else:
                result['profit_error'] = f'未获取到 {args.code} 的盈利能力数据'
                
        if args.type == 'operation' or args.type == 'all':
            # 营运能力
            data = query_financial_data(
                bs, bs.query_operation_data, args.code, args.year, args.quarter
            )
            if data:
                result['operation'] = data
            else:
                result['operation_error'] = f'未获取到 {args.code} 的营运能力数据'
                
        if args.type == 'growth' or args.type == 'all':
            # 成长能力
            data = query_financial_data(
                bs, bs.query_growth_data, args.code, args.year, args.quarter
            )
            if data:
                result['growth'] = data
            else:
                result['growth_error'] = f'未获取到 {args.code} 的成长能力数据'
                
        if args.type == 'balance' or args.type == 'all':
            # 偿债能力
            data = query_financial_data(
                bs, bs.query_balance_data, args.code, args.year, args.quarter
            )
            if data:
                result['balance'] = data
            else:
                result['balance_error'] = f'未获取到 {args.code} 的偿债能力数据'
                
        if args.type == 'cash_flow' or args.type == 'all':
            # 现金流
            data = query_financial_data(
                bs, bs.query_cash_flow_data, args.code, args.year, args.quarter
            )
            if data:
                result['cash_flow'] = data
            else:
                result['cash_flow_error'] = f'未获取到 {args.code} 的现金流数据'
                
        if args.type == 'dupont' or args.type == 'all':
            # 杜邦分析
            data = query_financial_data(
                bs, bs.query_dupont_data, args.code, args.year, args.quarter
            )
            if data:
                result['dupont'] = data
            else:
                result['dupont_error'] = f'未获取到 {args.code} 的杜邦分析数据'
        
        # 保存到 CSV
        if args.output:
            import pandas as pd
            
            # 合并所有数据
            all_data = {}
            for key in ['profit', 'operation', 'growth', 'balance', 'cash_flow', 'dupont']:
                if key in result:
                    all_data.update(result[key])
            
            if all_data:
                df = pd.DataFrame([all_data])
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
