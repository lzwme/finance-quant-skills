#!/usr/bin/env python3
"""AKShare 宏观经济数据获取脚本
支持GDP、CPI、PMI等宏观经济指标"""
import sys
import json
import argparse
import pandas as pd
import akshare as ak

def get_macro_china_gdp():
    """获取中国GDP数据"""
    try:
        df = ak.macro_china_gdp()
        return {
            "type": "macro_china_gdp",
            "data": df.to_dict('records'),
            "count": len(df)
        }
    except Exception as e:
        return {"error": f"获取中国GDP数据失败: {str(e)}"}

def get_macro_china_gdp_yearly():
    """获取中国GDP年度数据"""
    try:
        df = ak.macro_china_gdp_yearly()
        return {
            "type": "macro_china_gdp_yearly",
            "data": df.to_dict('records'),
            "count": len(df)
        }
    except Exception as e:
        return {"error": f"获取中国GDP年度数据失败: {str(e)}"}

def get_macro_china_cpi():
    """获取中国CPI数据"""
    try:
        df = ak.macro_china_cpi()
        return {
            "type": "macro_china_cpi",
            "data": df.to_dict('records'),
            "count": len(df)
        }
    except Exception as e:
        return {"error": f"获取中国CPI数据失败: {str(e)}"}

def get_macro_china_cpi_yearly():
    """获取中国CPI年度数据"""
    try:
        df = ak.macro_china_cpi_yearly()
        return {
            "type": "macro_china_cpi_yearly",
            "data": df.to_dict('records'),
            "count": len(df)
        }
    except Exception as e:
        return {"error": f"获取中国CPI年度数据失败: {str(e)}"}

def get_macro_china_pmi():
    """获取中国PMI数据"""
    try:
        df = ak.macro_china_pmi()
        return {
            "type": "macro_china_pmi",
            "data": df.to_dict('records'),
            "count": len(df)
        }
    except Exception as e:
        return {"error": f"获取中国PMI数据失败: {str(e)}"}

def get_macro_china_m2():
    """获取中国M2货币供应数据"""
    try:
        df = ak.macro_china_m2()
        return {
            "type": "macro_china_m2",
            "data": df.to_dict('records'),
            "count": len(df)
        }
    except Exception as e:
        return {"error": f"获取中国M2数据失败: {str(e)}"}

def get_macro_usa_non_farm():
    """获取美国非农就业数据"""
    try:
        df = ak.macro_usa_non_farm()
        return {
            "type": "macro_usa_non_farm",
            "data": df.to_dict('records'),
            "count": len(df)
        }
    except Exception as e:
        return {"error": f"获取美国非农就业数据失败: {str(e)}"}

def get_macro_usa_cpi_monthly():
    """获取美国CPI月度数据"""
    try:
        df = ak.macro_usa_cpi_monthly()
        return {
            "type": "macro_usa_cpi_monthly",
            "data": df.to_dict('records'),
            "count": len(df)
        }
    except Exception as e:
        return {"error": f"获取美国CPI月度数据失败: {str(e)}"}

def get_macro_usa_gdp_monthly():
    """获取美国GDP月度数据"""
    try:
        df = ak.macro_usa_gdp_monthly()
        return {
            "type": "macro_usa_gdp_monthly",
            "data": df.to_dict('records'),
            "count": len(df)
        }
    except Exception as e:
        return {"error": f"获取美国GDP月度数据失败: {str(e)}"}

def get_macro_usa_unemployment():
    """获取美国失业率数据"""
    try:
        df = ak.macro_usa_unemployment()
        return {
            "type": "macro_usa_unemployment",
            "data": df.to_dict('records'),
            "count": len(df)
        }
    except Exception as e:
        return {"error": f"获取美国失业率数据失败: {str(e)}"}

def get_macro_summary():
    """获取宏观经济概览"""
    try:
        result = {}

        # 中国主要指标
        china_indicators = {
            "gdp": get_macro_china_gdp(),
            "cpi": get_macro_china_cpi(),
            "pmi": get_macro_china_pmi(),
            "m2": get_macro_china_m2()
        }

        # 美国主要指标
        usa_indicators = {
            "non_farm": get_macro_usa_non_farm(),
            "cpi": get_macro_usa_cpi_monthly(),
            "gdp": get_macro_usa_gdp_monthly(),
            "unemployment": get_macro_usa_unemployment()
        }

        # 提取最新数据
        for key, data in china_indicators.items():
            if "error" not in data and len(data.get("data", [])) > 0:
                latest = data["data"][-1]
                result[f"china_{key}"] = {
                    "value": latest.get("value", latest.get("data", None)),
                    "date": latest.get("date", latest.get("time", None))
                }

        for key, data in usa_indicators.items():
            if "error" not in data and len(data.get("data", [])) > 0:
                latest = data["data"][-1]
                result[f"usa_{key}"] = {
                    "value": latest.get("value", latest.get("data", None)),
                    "date": latest.get("date", latest.get("time", None))
                }

        return {
            "type": "macro_summary",
            "data": result,
            "update_time": pd.Timestamp.now().strftime("%Y-%m-%d %H:%M:%S")
        }
    except Exception as e:
        return {"error": f"获取宏观经济概览失败: {str(e)}"}

def main():
    parser = argparse.ArgumentParser(description='AKShare 宏观经济数据获取')
    parser.add_argument('--type', required=True,
                       choices=['gdp', 'gdp_yearly', 'cpi', 'cpi_yearly', 'pmi', 'm2',
                               'usa_non_farm', 'usa_cpi', 'usa_gdp', 'usa_unemployment', 'summary'],
                       help='宏观经济指标类型')

    args = parser.parse_args()

    if args.type == 'gdp':
        result = get_macro_china_gdp()
    elif args.type == 'gdp_yearly':
        result = get_macro_china_gdp_yearly()
    elif args.type == 'cpi':
        result = get_macro_china_cpi()
    elif args.type == 'cpi_yearly':
        result = get_macro_china_cpi_yearly()
    elif args.type == 'pmi':
        result = get_macro_china_pmi()
    elif args.type == 'm2':
        result = get_macro_china_m2()
    elif args.type == 'usa_non_farm':
        result = get_macro_usa_non_farm()
    elif args.type == 'usa_cpi':
        result = get_macro_usa_cpi_monthly()
    elif args.type == 'usa_gdp':
        result = get_macro_usa_gdp_monthly()
    elif args.type == 'usa_unemployment':
        result = get_macro_usa_unemployment()
    elif args.type == 'summary':
        result = get_macro_summary()
    else:
        result = {"error": f"未知类型: {args.type}"}

    print(json.dumps(result, ensure_ascii=False, indent=2, default=str))

if __name__ == "__main__":
    main()
