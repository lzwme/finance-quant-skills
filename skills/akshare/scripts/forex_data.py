#!/usr/bin/env python3
"""AKShare 外汇贵金属数据获取脚本
支持外汇行情、汇率数据、贵金属价格等"""
import sys
import json
import argparse
import pandas as pd
import akshare as ak

def get_forex_spot():
    """获取外汇实时行情"""
    try:
        df = ak.forex_spot_em()
        return {
            "type": "forex_spot",
            "data": df.to_dict('records'),
            "count": len(df),
            "update_time": pd.Timestamp.now().strftime("%Y-%m-%d %H:%M:%S")
        }
    except Exception as e:
        return {"error": f"获取外汇实时行情失败: {str(e)}"}

def get_fx_spot_quote():
    """获取外汇即期报价"""
    try:
        df = ak.fx_spot_quote()
        return {
            "type": "fx_spot_quote",
            "data": df.to_dict('records'),
            "count": len(df)
        }
    except Exception as e:
        return {"error": f"获取外汇即期报价失败: {str(e)}"}

def get_fx_swap_quote():
    """获取外汇掉期报价"""
    try:
        df = ak.fx_swap_quote()
        return {
            "type": "fx_swap_quote",
            "data": df.to_dict('records'),
            "count": len(df)
        }
    except Exception as e:
        return {"error": f"获取外汇掉期报价失败: {str(e)}"}

def get_usd_cny():
    """获取美元兑人民币汇率"""
    try:
        df = ak.forex_usd_cny()
        return {
            "type": "usd_cny",
            "data": df.to_dict('records'),
            "count": len(df)
        }
    except Exception as e:
        return {"error": f"获取美元兑人民币汇率失败: {str(e)}"}

def get_metals_gold():
    """获取国际金价"""
    try:
        df = ak.metals_gold()
        return {
            "type": "metals_gold",
            "data": df.to_dict('records'),
            "count": len(df)
        }
    except Exception as e:
        return {"error": f"获取国际金价失败: {str(e)}"}

def get_metals_silver():
    """获取国际银价"""
    try:
        df = ak.metals_silver()
        return {
            "type": "metals_silver",
            "data": df.to_dict('records'),
            "count": len(df)
        }
    except Exception as e:
        return {"error": f"获取国际银价失败: {str(e)}"}

def get_metals_shibor():
    """获取上海银行间拆借利率"""
    try:
        df = ak.metals_shibor()
        return {
            "type": "metals_shibor",
            "data": df.to_dict('records'),
            "count": len(df)
        }
    except Exception as e:
        return {"error": f"获取上海银行间拆借利率失败: {str(e)}"}

def get_currency_pair_rate(pair="USD/CNY"):
    """获取指定货币对汇率"""
    try:
        # 根据货币对选择对应接口
        if pair.upper() in ["USD/CNY", "USDCNY"]:
            df = ak.forex_usd_cny()
        elif pair.upper() in ["EUR/CNY", "EURCNY"]:
            df = ak.forex_eur_cny()
        elif pair.upper() in ["GBP/CNY", "GBPCNY"]:
            df = ak.forex_gbp_cny()
        elif pair.upper() in ["JPY/CNY", "JPYCNY"]:
            df = ak.forex_jpy_cny()
        else:
            # 尝试通用外汇接口
            df = ak.forex_hist(symbol=pair.replace("/", ""))

        return {
            "type": "currency_pair_rate",
            "pair": pair,
            "data": df.to_dict('records'),
            "count": len(df)
        }
    except Exception as e:
        return {"error": f"获取货币对汇率失败: {str(e)}"}

def get_forex_trading_calendar():
    """获取外汇交易日历"""
    try:
        df = ak.fx_trading_calendar()
        return {
            "type": "forex_trading_calendar",
            "data": df.to_dict('records'),
            "count": len(df)
        }
    except Exception as e:
        return {"error": f"获取外汇交易日历失败: {str(e)}"}

def get_currency_rates_boc():
    """获取中国银行外汇牌价"""
    try:
        df = ak.currency_boc_sina()
        return {
            "type": "currency_rates_boc",
            "data": df.to_dict('records'),
            "count": len(df)
        }
    except Exception as e:
        return {"error": f"获取中国银行外汇牌价失败: {str(e)}"}

def main():
    parser = argparse.ArgumentParser(description='AKShare 外汇贵金属数据获取')
    parser.add_argument('--type', required=True,
                       choices=['spot', 'spot_quote', 'swap_quote', 'usd_cny', 'gold',
                               'silver', 'shibor', 'pair_rate', 'calendar', 'boc_rates'],
                       help='数据类型')
    parser.add_argument('--symbol', help='货币对或贵金属代码')
    parser.add_argument('--pair', default='USD/CNY', help='货币对，如 USD/CNY')

    args = parser.parse_args()

    if args.type == 'spot':
        result = get_forex_spot()
    elif args.type == 'spot_quote':
        result = get_fx_spot_quote()
    elif args.type == 'swap_quote':
        result = get_fx_swap_quote()
    elif args.type == 'usd_cny':
        result = get_usd_cny()
    elif args.type == 'gold':
        result = get_metals_gold()
    elif args.type == 'silver':
        result = get_metals_silver()
    elif args.type == 'shibor':
        result = get_metals_shibor()
    elif args.type == 'pair_rate':
        pair = args.pair if args.pair else "USD/CNY"
        result = get_currency_pair_rate(pair)
    elif args.type == 'calendar':
        result = get_forex_trading_calendar()
    elif args.type == 'boc_rates':
        result = get_currency_rates_boc()
    else:
        result = {"error": f"未知类型: {args.type}"}

    print(json.dumps(result, ensure_ascii=False, indent=2, default=str))

if __name__ == "__main__":
    main()
