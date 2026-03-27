#!/usr/bin/env python3
"""获取宏观经济数据"""
import sys
import json
import akshare as ak

def get_macro_data(indicator="gdp"):
    """获取宏观经济指标"""
    try:
        indicators = {
            "gdp": ("GDP", ak.macro_china_gdp),
            "cpi": ("CPI通胀", ak.macro_china_cpi),
            "pmi": ("PMI采购经理指数", ak.macro_china_pmi),
            "m2": ("M2货币供应", ak.macro_china_m2),
        }
        
        if indicator not in indicators:
            return {"error": f"Unknown indicator: {indicator}"}
        
        name, func = indicators[indicator]
        df = func()
        
        # 获取最新数据
        latest = df.iloc[-1]
        return {
            "indicator": indicator,
            "name": name,
            "date": str(latest.iloc[0]),
            "value": float(latest.iloc[1]) if len(latest) > 1 else None
        }
    except Exception as e:
        return {"error": str(e)}

def get_macro_summary():
    """获取宏观经济概览"""
    try:
        result = {}
        for ind in ["gdp", "cpi", "pmi", "m2"]:
            data = get_macro_data(ind)
            if "error" not in data:
                result[ind] = {
                    "value": data.get("value"),
                    "date": data.get("date")
                }
        return result
    except Exception as e:
        return {"error": str(e)}

if __name__ == "__main__":
    if len(sys.argv) > 1:
        cmd = sys.argv[1]
        if cmd == "data":
            indicator = sys.argv[2] if len(sys.argv) > 2 else "gdp"
            result = get_macro_data(indicator)
        elif cmd == "summary":
            result = get_macro_summary()
        else:
            result = {"error": f"Unknown command: {cmd}"}
    else:
        result = {"usage": "python macro.py data <indicator> | summary"}
    
    print(json.dumps(result, ensure_ascii=False, indent=2))
