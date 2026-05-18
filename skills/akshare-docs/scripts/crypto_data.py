#!/usr/bin/env python3
"""AKShare 加密货币数据获取脚本
支持加密货币价格、K线数据等"""
import sys
import json
import argparse
import pandas as pd
import akshare as ak

def get_crypto_symbols():
    """获取加密货币交易对列表"""
    try:
        df = ak.crypto_binance_symbols()
        return {
            "type": "crypto_symbols",
            "data": df.to_dict('records'),
            "count": len(df)
        }
    except Exception as e:
        return {"error": f"获取加密货币交易对失败: {str(e)}"}

def get_crypto_price(symbol="BTC/USDT"):
    """获取加密货币实时价格"""
    try:
        symbol_map = {
            "BTC/USDT": ak.crypto_binance_btc_usdt_spot,
            "ETH/USDT": ak.crypto_binance_eth_usdt_spot,
            "BNB/USDT": ak.crypto_binance_bnb_usdt_spot,
        }

        func = symbol_map.get(symbol, ak.crypto_binance_btc_usdt_spot)
        df = func()

        if df is not None and len(df) > 0:
            latest = df.iloc[-1]
            return {
                "type": "crypto_price",
                "symbol": symbol,
                "price": float(latest.get('close', latest.get('price', 0))),
                "volume": str(latest.get('volume', 'N/A')),
                "timestamp": str(latest.get('date', pd.Timestamp.now()))
            }
        return {"error": "No data available"}
    except Exception as e:
        return {"error": f"获取加密货币价格失败: {str(e)}"}

def get_crypto_kline(symbol="BTC/USDT", period="daily"):
    """获取加密货币K线数据"""
    try:
        if symbol.upper() in ["BTC/USDT", "BTC", "btc"]:
            df = ak.crypto_binance_btc_usdt_kline(period=period)
        elif symbol.upper() in ["ETH/USDT", "ETH", "eth"]:
            df = ak.crypto_binance_eth_usdt_kline(period=period)
        else:
            return {"error": f"不支持的交易对: {symbol}"}

        return {
            "type": "crypto_kline",
            "symbol": symbol,
            "period": period,
            "data": df.to_dict('records'),
            "count": len(df)
        }
    except Exception as e:
        return {"error": f"获取加密货币K线失败: {str(e)}"}

def get_crypto_all_spot():
    """获取所有加密货币实时价格"""
    try:
        # 获取币安所有交易对
        df = ak.crypto_binance_symbols()
        symbols = df['symbol'].tolist()[:10]  # 限制前10个避免请求过多

        results = []
        for symbol in symbols:
            try:
                price_data = get_crypto_price(f"{symbol}/USDT")
                if "error" not in price_data:
                    results.append(price_data)
            except:
                continue

        return {
            "type": "crypto_all_spot",
            "data": results,
            "count": len(results)
        }
    except Exception as e:
        return {"error": f"获取所有加密货币价格失败: {str(e)}"}

def get_crypto_market_cap():
    """获取加密货币市值信息"""
    try:
        df = ak.crypto_bitcoin_market_cap()
        return {
            "type": "crypto_market_cap",
            "data": df.to_dict('records'),
            "count": len(df)
        }
    except Exception as e:
        return {"error": f"获取加密货币市值失败: {str(e)}"}

def get_crypto_global_index():
    """获取加密货币全球指数"""
    try:
        df = ak.crypto_bitcoin_global_index()
        return {
            "type": "crypto_global_index",
            "data": df.to_dict('records'),
            "count": len(df)
        }
    except Exception as e:
        return {"error": f"获取加密货币全球指数失败: {str(e)}"}

def main():
    parser = argparse.ArgumentParser(description='AKShare 加密货币数据获取')
    parser.add_argument('--type', required=True,
                       choices=['symbols', 'price', 'kline', 'all_spot', 'market_cap', 'global_index'],
                       help='数据类型')
    parser.add_argument('--symbol', default='BTC/USDT', help='加密货币交易对')
    parser.add_argument('--period', default='daily',
                       choices=['daily', 'weekly', 'monthly'],
                       help='K线周期')

    args = parser.parse_args()

    if args.type == 'symbols':
        result = get_crypto_symbols()
    elif args.type == 'price':
        result = get_crypto_price(args.symbol)
    elif args.type == 'kline':
        result = get_crypto_kline(args.symbol, args.period)
    elif args.type == 'all_spot':
        result = get_crypto_all_spot()
    elif args.type == 'market_cap':
        result = get_crypto_market_cap()
    elif args.type == 'global_index':
        result = get_crypto_global_index()
    else:
        result = {"error": f"未知类型: {args.type}"}

    print(json.dumps(result, ensure_ascii=False, indent=2, default=str))

if __name__ == "__main__":
    main()
