#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
财务数据获取脚本
支持获取财务数据、利润表、资产负债表、现金流量表、财务指标
"""

import argparse
import json
import sys
import os
from datetime import datetime


def main():
    parser = argparse.ArgumentParser(description='获取 Tushare 财务数据')
    parser.add_argument('--type', required=True,
                       choices=['financial', 'income', 'balancesheet', 'cashflow', 'fina_indicator', 'fina_audit', 'fina_mainbz'],
                       help='数据类型: financial-财务数据, income-利润表, balancesheet-资产负债表, cashflow-现金流量表, fina_indicator-财务指标, fina_audit-审计意见, fina_mainbz-主营业务')
    parser.add_argument('--ts_code', help='股票代码，格式: 000001.SZ 或 600000.SH，多个用逗号分隔')
    parser.add_argument('--period', help='报告期，格式YYYY或YYYYMM，如 2023 或 202312')
    parser.add_argument('--start_date', help='开始日期，格式YYYYMMDD')
    parser.add_argument('--end_date', help='结束日期，格式YYYYMMDD')
    parser.add_argument('--report_type', help='报告类型: 1-合并报表, 2-单季合并, 3-调整单季合并表, 4-调整合并报表, 5-调整前合并报表')
    parser.add_argument('--fields', help='字段列表，逗号分隔')

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
        if args.ts_code:
            params['ts_code'] = args.ts_code
        if args.period:
            params['period'] = args.period
        if args.start_date:
            params['start_date'] = args.start_date
        if args.end_date:
            params['end_date'] = args.end_date
        if args.report_type:
            params['report_type'] = args.report_type
        if args.fields:
            params['fields'] = args.fields

        if args.type == 'financial':
            # 财务数据（旧接口）
            data = pro.financial(**params)

        elif args.type == 'income':
            # 利润表
            data = pro.income(**params)

        elif args.type == 'balancesheet':
            # 资产负债表
            data = pro.balancesheet(**params)

        elif args.type == 'cashflow':
            # 现金流量表
            data = pro.cashflow(**params)

        elif args.type == 'fina_indicator':
            # 财务指标
            data = pro.fina_indicator(**params)

        elif args.type == 'fina_audit':
            # 审计意见
            data = pro.fina_audit(**params)

        elif args.type == 'fina_mainbz':
            # 主营业务
            data = pro.fina_mainbz(**params)

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
