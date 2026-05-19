#!/usr/bin/env python3
"""AKShare 债券数据获取脚本
支持可转债、债券报价等数据"""
import sys
import json
import argparse
import pandas as pd
import akshare as ak

def get_bond_convertible():
    """获取可转债列表"""
    try:
        df = ak.bond_zh_cov()
        return {
            "type": "bond_convertible",
            "data": df.to_dict('records'),
            "count": len(df)
        }
    except Exception as e:
        return {"error": f"获取可转债列表失败: {str(e)}"}

def get_bond_convertible_hist(symbol="sz123456"):
    """获取可转债历史K线数据"""
    try:
        df = ak.bond_zh_hs_cov_daily(symbol=symbol)
        return {
            "type": "bond_convertible_hist",
            "symbol": symbol,
            "data": df.to_dict('records'),
            "count": len(df)
        }
    except Exception as e:
        return {"error": f"获取可转债历史数据失败: {str(e)}"}

def get_bond_spot_quote():
    """获取中国债券现货报价"""
    try:
        df = ak.bond_spot_quote()
        return {
            "type": "bond_spot_quote",
            "data": df.to_dict('records'),
            "count": len(df)
        }
    except Exception as e:
        return {"error": f"获取债券现货报价失败: {str(e)}"}

def get_bond_cov_jsl():
    """获取集思录可转债数据"""
    try:
        df = ak.bond_cov_jsl()
        return {
            "type": "bond_cov_jsl",
            "data": df.to_dict('records'),
            "count": len(df)
        }
    except Exception as e:
        return {"error": f"获取集思录可转债数据失败: {str(e)}"}

def get_bond_zh_hs_cov():
    """获取沪深可转债数据"""
    try:
        df = ak.bond_zh_hs_cov()
        return {
            "type": "bond_zh_hs_cov",
            "data": df.to_dict('records'),
            "count": len(df)
        }
    except Exception as e:
        return {"error": f"获取沪深可转债数据失败: {str(e)}"}

def get_bond_treasure_issue():
    """获取国债发行数据"""
    try:
        df = ak.bond_treasure_issue()
        return {
            "type": "bond_treasure_issue",
            "data": df.to_dict('records'),
            "count": len(df)
        }
    except Exception as e:
        return {"error": f"获取国债发行数据失败: {str(e)}"}

def get_bond_local_government_issue():
    """获取地方债发行数据"""
    try:
        df = ak.bond_local_government_issue()
        return {
            "type": "bond_local_government_issue",
            "data": df.to_dict('records'),
            "count": len(df)
        }
    except Exception as e:
        return {"error": f"获取地方债发行数据失败: {str(e)}"}

def get_bond_corporate_issue():
    """获取企业债发行数据"""
    try:
        df = ak.bond_corporate_issue()
        return {
            "type": "bond_corporate_issue",
            "data": df.to_dict('records'),
            "count": len(df)
        }
    except Exception as e:
        return {"error": f"获取企业债发行数据失败: {str(e)}"}

def main():
    parser = argparse.ArgumentParser(description='AKShare 债券数据获取')
    parser.add_argument('--type', required=True,
                       choices=['convertible', 'convertible_hist', 'spot_quote', 'cov_jsl',
                               'zh_hs_cov', 'treasure_issue', 'local_gov_issue', 'corporate_issue'],
                       help='数据类型')
    parser.add_argument('--symbol', default='sz123456', help='债券代码')

    args = parser.parse_args()

    if args.type == 'convertible':
        result = get_bond_convertible()
    elif args.type == 'convertible_hist':
        result = get_bond_convertible_hist(args.symbol)
    elif args.type == 'spot_quote':
        result = get_bond_spot_quote()
    elif args.type == 'cov_jsl':
        result = get_bond_cov_jsl()
    elif args.type == 'zh_hs_cov':
        result = get_bond_zh_hs_cov()
    elif args.type == 'treasure_issue':
        result = get_bond_treasure_issue()
    elif args.type == 'local_gov_issue':
        result = get_bond_local_government_issue()
    elif args.type == 'corporate_issue':
        result = get_bond_corporate_issue()
    else:
        result = {"error": f"未知类型: {args.type}"}

    print(json.dumps(result, ensure_ascii=False, indent=2, default=str))

if __name__ == "__main__":
    main()
