#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
行情数据获取脚本
支持获取 K 线数据、批量下载、保存 CSV
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
from auth import auth_bs, logout_bs


def get_kline_data(bs, code, start_date, end_date, frequency='d', adjustflag='3', fields=None):
    """
    获取单只股票 K 线数据

    Args:
        bs: baostock 模块
        code: 股票代码，如 sh.600000
        start_date: 开始日期 YYYY-MM-DD
        end_date: 结束日期 YYYY-MM-DD
        frequency: 频率 d/w/m/5/15/30/60
        adjustflag: 复权类型 1=后复权, 2=前复权, 3=不复权
        fields: 字段列表，逗号分隔

    Returns:
        list: K线数据字典列表
    """
    # 默认字段
    if fields is None:
        fields = "date,code,open,high,low,close,volume,amount,pctChg"

    rs = bs.query_history_k_data_plus(
        code,
        fields,
        start_date=start_date,
        end_date=end_date,
        frequency=frequency,
        adjustflag=adjustflag
    )

    data = []
    if rs.error_code == '0':
        while rs.next():
            row = rs.get_row_data()
            data.append(dict(zip(rs.fields, row)))

    return data


def main():
    parser = argparse.ArgumentParser(description='获取 BaoStock A股行情数据')
    parser.add_argument('--type', required=False, choices=['kline', 'current'],
                       help='数据类型: kline-K线数据, current-当前无实时数据（baostock不提供实时）', default = 'kline')
    parser.add_argument('--code', required=True,
                       help='股票代码，格式: sh.600000 或 sz.000001，多个用逗号分隔')
    parser.add_argument('--start', help='开始日期，格式YYYY-MM-DD，如 2024-01-01')
    parser.add_argument('--end', help='结束日期，格式YYYY-MM-DD，如 2024-01-31')
    parser.add_argument('--frequency', default='d',
                       choices=['d', 'w', 'm', '5', '15', '30', '60'],
                       help='数据频率，默认d(日线): d=日线, w=周线, m=月线, 5/15/30/60=分钟线')
    parser.add_argument('--adjust', default='3',
                       choices=['1', '2', '3'],
                       help='复权类型，默认3(不复权): 1=后复权, 2=前复权, 3=不复权')
    parser.add_argument('--fields',
                       help='字段列表，逗号分隔，如 date,open,close,high,low,volume')
    parser.add_argument('--output', help='输出CSV文件路径')
    parser.add_argument('--file', help='股票代码列表文件路径，每行一个代码')

    args = parser.parse_args()

    try:
        # 使用统一认证模块进行登录
        bs = auth_bs()

        result = {
            'status': 'success',
            'data_type': args.type,
            'timestamp': datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        }

        # 处理日期默认值
        if not args.end:
            args.end = datetime.now().strftime('%Y-%m-%d')
        if not args.start:
            # 默认获取最近 30 天
            args.start = (datetime.now() - timedelta(days=30)).strftime('%Y-%m-%d')

        # 获取股票代码列表
        if args.file:
            # 从文件读取代码列表
            with open(args.file, 'r', encoding='utf-8') as f:
                codes = [line.strip() for line in f if line.strip()]
        else:
            # 从命令行参数解析
            codes = [c.strip() for c in args.code.split(',')]

        if args.type == 'kline':
            all_data = []

            for code in codes:
                data = get_kline_data(
                    bs, code, args.start, args.end,
                    args.frequency, args.adjust, args.fields
                )
                all_data.extend(data)

            result['data'] = all_data
            result['count'] = len(all_data)
            result['codes'] = codes
            result['frequency'] = args.frequency
            result['adjust'] = args.adjust

            # 保存到 CSV
            if args.output and all_data:
                import pandas as pd
                df = pd.DataFrame(all_data)
                df.to_csv(args.output, index=False, encoding='utf-8-sig')
                result['output_file'] = args.output

        elif args.type == 'current':
            # baostock 不提供实时数据，返回提示
            result['warning'] = 'BaoStock 不提供实时行情数据，建议使用 kline 类型获取历史数据'
            result['data'] = []
            result['count'] = 0

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
