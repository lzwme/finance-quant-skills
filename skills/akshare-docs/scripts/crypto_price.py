#!/usr/bin/env python3
"""获取加密货币价格"""
import sys
import json
import akshare as ak

def get_crypto_price(symbol="BTC/USDT"):
    """获取加密货币价格"""
    try:
        if symbol in ["BTC/USDT", "BTC", "btc"]:
            df = ak.crypto_binance_btc_usdt_spot()
        elif symbol in ["ETH/USDT", "ETH", "eth"]:
            df = ak.crypto_binance_eth_usdt_spot()
        else:
            # 尝试通用接口
            symbol_map = {
                "BTC/USDT": ak.crypto_binance_btc_usdt_spot,
                "ETH/USDT": ak.crypto_binance_eth_usdt_spot,
            }
            func = symbol_map.get(symbol, ak.crypto_binance_btc_usdt_spot)
            df = func()
        
        if df is not None and len(df) > 0:
            latest = df.iloc[-1]
            return {
                "symbol": symbol,
                "price": float(latest.get('close', latest.get('price', 0))),
                "volume": str(latest.get('volume', 'N/A'))
            }
        return {"error": "No data"}
    except Exception as e:
        return {"error": str(e)}

def get_crypto_kline(symbol="BTC/USDT", period="daily"):
    """获取加密货币K线"""
    try:
        if symbol in ["BTC/USDT", "BTC", "btc"]:
            df = ak.crypto_binance_btc_usdt_kline(period=period)
        else:
            return {"error": f"Unsupported symbol: {symbol}"}
        
        latest = df.iloc[-1]
        return {
            "symbol": symbol,
            "period": period,
            "open": float(latest['open']),
            "high": float(latest['high']),
            "low": float(latest['low']),
            "close": float(latest['close']),
            "volume": int(latest['volume'])
        }
    except Exception as e:
        return {"error": str(e)}

if __name__ == "__main__":
    if len(sys.argv) > 1:
        cmd = sys.argv[1]
        symbol = sys.argv[2] if len(sys.argv) > 2 else "BTC/USDT"
        
        if cmd == "price":
            result = get_crypto_price(symbol)
        elif cmd == "kline":
            period = sys.argv[3] if len(sys.argv) > 3 else "daily"
            result = get_crypto_kline(symbol, period)
        else:
            result = {"error": f"Unknown command: {cmd}"}
    else:
        result = {"usage": "python crypto.py price <symbol> | kline <symbol> <period>"}
    
    print(json.dumps(result, ensure_ascii=False, indent=2))
