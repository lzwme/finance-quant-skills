#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
交易执行脚本
支持：获取账户句柄(account)、下单(order)、撤单(cancel)、
     查询持仓(positions)、查询委托(orders)、查询资产(asset)
"""

import argparse
import json
import sys
import os

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _tdx_init import init_tq


def cmd_account(tq, args):
    """获取资金账户句柄"""
    result = {"status": "success", "data_type": "account"}
    account_id = tq.stock_account(account=args.account or "", account_type=args.account_type)
    if account_id >= 0:
        result["account_id"] = account_id
        result["account_type"] = args.account_type
    else:
        result["status"] = "error"
        result["message"] = f"获取账户句柄失败(句柄={account_id})，请确认客户端已登录账户"
    return result


def cmd_order(tq, args):
    """下单"""
    # 先获取账户句柄
    account_id = tq.stock_account(account=args.account or "", account_type=args.account_type)
    if account_id < 0:
        return {"status": "error", "message": f"获取账户句柄失败(句柄={account_id})"}

    from tqcenter import tqconst
    order_type_map = {
        "buy": tqconst.STOCK_BUY,
        "sell": tqconst.STOCK_SELL,
        "credit_buy": tqconst.CREDIT_BUY,
        "credit_sell": tqconst.CREDIT_SELL,
        "credit_fin_buy": tqconst.CREDIT_FIN_BUY,
        "credit_slo_sell": tqconst.CREDIT_SLO_SELL,
    }
    price_type_map = {
        "my": tqconst.PRICE_MY,
        "sj": tqconst.PRICE_SJ,
        "ztj": tqconst.PRICE_ZTJ,
        "dtj": tqconst.PRICE_DTJ,
    }

    order_type = order_type_map.get(args.order_type, tqconst.STOCK_BUY)
    price_type = price_type_map.get(args.price_type, tqconst.PRICE_MY)

    data = tq.order_stock(
        account_id=account_id,
        stock_code=args.code,
        order_type=order_type,
        order_volume=args.volume,
        price_type=price_type,
        price=args.price
    )
    return {"status": "success", "data_type": "order", "data": data}


def cmd_cancel(tq, args):
    """撤单"""
    account_id = tq.stock_account(account=args.account or "", account_type=args.account_type)
    if account_id < 0:
        return {"status": "error", "message": f"获取账户句柄失败(句柄={account_id})"}

    data = tq.cancel_order_stock(
        account_id=account_id,
        stock_code=args.code,
        order_id=args.order_id
    )
    return {"status": "success", "data_type": "cancel", "data": data}


def cmd_positions(tq, args):
    """查询持仓"""
    account_id = tq.stock_account(account=args.account or "", account_type=args.account_type)
    if account_id < 0:
        return {"status": "error", "message": f"获取账户句柄失败(句柄={account_id})"}

    data = tq.query_stock_positions(account_id=account_id)
    return {"status": "success", "data_type": "positions", "data": data if data else []}


def cmd_orders(tq, args):
    """查询委托"""
    account_id = tq.stock_account(account=args.account or "", account_type=args.account_type)
    if account_id < 0:
        return {"status": "error", "message": f"获取账户句柄失败(句柄={account_id})"}

    data = tq.query_stock_orders(account_id=account_id, stock_code=args.code or "")
    return {"status": "success", "data_type": "orders", "data": data if data else []}


def cmd_asset(tq, args):
    """查询资产"""
    account_id = tq.stock_account(account=args.account or "", account_type=args.account_type)
    if account_id < 0:
        return {"status": "error", "message": f"获取账户句柄失败(句柄={account_id})"}

    data = tq.query_stock_asset(account_id=account_id)
    return {"status": "success", "data_type": "asset", "data": data if data else {}}


def main():
    parser = argparse.ArgumentParser(description="通达信交易执行")
    parser.add_argument("--account", default="", help="资金账号(空则使用当前登录账户)")
    parser.add_argument("--account_type", default="stock",
                       choices=["stock", "credit", "future", "option"],
                       help="账号类型: stock-普通股票, credit-信用, future-期货, option-期权")

    sub = parser.add_subparsers(dest="command", required=True)

    # account
    sub.add_parser("account", help="获取资金账户句柄")

    # order
    p = sub.add_parser("order", help="下单")
    p.add_argument("--code", required=True, help="证券代码，如 688318.SH")
    p.add_argument("--order_type", required=True,
                   choices=["buy", "sell", "credit_buy", "credit_sell", "credit_fin_buy", "credit_slo_sell"],
                   help="委托类型")
    p.add_argument("--volume", type=int, required=True, help="委托数量")
    p.add_argument("--price_type", default="my", choices=["my", "sj", "ztj", "dtj"],
                   help="报价类型: my-自填价, sj-市价, ztj-涨停价, dtj-跌停价")
    p.add_argument("--price", type=float, default=0.0, help="委托价格(price_type=my时必填)")

    # cancel
    p = sub.add_parser("cancel", help="撤单")
    p.add_argument("--code", required=True, help="证券代码")
    p.add_argument("--order_id", required=True, help="委托编号")

    # positions
    sub.add_parser("positions", help="查询持仓")

    # orders
    p = sub.add_parser("orders", help="查询委托")
    p.add_argument("--code", default="", help="证券代码(空则查询全部)")

    # asset
    sub.add_parser("asset", help="查询资产")

    args = parser.parse_args()
    tq = init_tq()

    handlers = {
        "account": cmd_account,
        "order": cmd_order,
        "cancel": cmd_cancel,
        "positions": cmd_positions,
        "orders": cmd_orders,
        "asset": cmd_asset,
    }

    try:
        result = handlers[args.command](tq, args)
        print(json.dumps(result, ensure_ascii=False, indent=2, default=str))
    except Exception as e:
        print(json.dumps({
            "status": "error", "message": str(e), "error_type": type(e).__name__
        }, ensure_ascii=False))
        sys.exit(1)


if __name__ == "__main__":
    main()
