#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
MiniQMT 交易脚本
支持：下单、撤单、查询资产/持仓/委托/成交

注意：此脚本需要 MiniQMT 客户端在后台运行
"""

import argparse
import json
import sys
import os

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

# 默认路径配置（可通过环境变量覆盖）
DEFAULT_PATH = os.environ.get('MINIQMT_PATH', 'C:\\迅投极速交易终端\\userdata_mini')


def get_trader():
    """获取交易实例"""
    from xtquant.xttrader import XtQuantTrader, XtQuantTraderCallback
    # from xtquant import xtconstant

    path = DEFAULT_PATH
    session_id = int(os.environ.get('MINIQMT_SESSION', '123456'))

    xt_trader = XtQuantTrader(path, session_id)
    return xt_trader


def get_account(acc_type='STOCK'):
    """获取账号对象"""
    from xtquant.xttype import StockAccount, FutureAccount

    acc_id = os.environ.get('MINIQMT_ACCOUNT', '')
    if not acc_id:
        return None

    if acc_type == 'FUTURE':
        return FutureAccount(acc_id)
    return StockAccount(acc_id)


def cmd_order(args):
    """下单"""
    from xtquant import xtconstant

    result = {"status": "success", "data_type": "order", "code": args.code}

    try:
        xt_trader = get_trader()
        acc = get_account(args.acc_type)

        if not acc:
            result["status"] = "error"
            result["message"] = "未配置账号，请设置 MINIQMT_ACCOUNT 环境变量"
            return result

        # 启动连接
        xt_trader.start()
        if xt_trader.connect() != 0:
            result["status"] = "error"
            result["message"] = "连接失败"
            return result
        xt_trader.subscribe(acc)

        # 解析参数
        order_type = xtconstant.STOCK_BUY if args.type.lower() == 'buy' else xtconstant.STOCK_SELL
        price_type = xtconstant.FIX_PRICE

        # 下单
        order_id = xt_trader.order_stock(
            acc,
            args.code,
            order_type,
            args.volume,
            price_type,
            args.price,
            args.strategy or 'script',
            args.remark or ''
        )

        result["data"] = {
            "order_id": order_id,
            "success": order_id > 0
        }
        if order_id < 0:
            result["status"] = "error"
            result["message"] = "下单失败"

    except Exception as e:
        result["status"] = "error"
        result["message"] = str(e)

    return result


def cmd_cancel(args):
    """撤单"""
    result = {"status": "success", "data_type": "cancel", "order_id": args.order_id}

    try:
        xt_trader = get_trader()
        acc = get_account(args.acc_type)

        if not acc:
            result["status"] = "error"
            result["message"] = "未配置账号"
            return result

        xt_trader.start()
        if xt_trader.connect() != 0:
            result["status"] = "error"
            result["message"] = "连接失败"
            return result
        xt_trader.subscribe(acc)

        cancel_result = xt_trader.cancel_order_stock(acc, args.order_id)
        result["data"] = {
            "success": cancel_result == 0,
            "code": cancel_result
        }

    except Exception as e:
        result["status"] = "error"
        result["message"] = str(e)

    return result


def cmd_positions(args):
    """查询持仓"""
    result = {"status": "success", "data_type": "positions"}

    try:
        xt_trader = get_trader()
        acc = get_account(args.acc_type)

        if not acc:
            result["status"] = "error"
            result["message"] = "未配置账号"
            return result

        xt_trader.start()
        if xt_trader.connect() != 0:
            result["status"] = "error"
            result["message"] = "连接失败"
            return result
        xt_trader.subscribe(acc)

        positions = xt_trader.query_stock_positions(acc)
        if positions:
            result["data"] = {
                "count": len(positions),
                "positions": [
                    {
                        "code": p.stock_code,
                        "volume": p.volume,
                        "can_use": p.can_use_volume,
                        "avg_price": p.avg_price,
                        "market_value": p.market_value
                    }
                    for p in positions
                ]
            }
        else:
            result["data"] = {"count": 0, "positions": []}

    except Exception as e:
        result["status"] = "error"
        result["message"] = str(e)

    return result


def cmd_orders(args):
    """查询委托"""
    result = {"status": "success", "data_type": "orders"}

    try:
        xt_trader = get_trader()
        acc = get_account(args.acc_type)

        if not acc:
            result["status"] = "error"
            result["message"] = "未配置账号"
            return result

        xt_trader.start()
        if xt_trader.connect() != 0:
            result["status"] = "error"
            result["message"] = "连接失败"
            return result
        xt_trader.subscribe(acc)

        orders = xt_trader.query_stock_orders(acc, cancelable_only=args.cancelable_only)
        if orders:
            result["data"] = {
                "count": len(orders),
                "orders": [
                    {
                        "order_id": o.order_id,
                        "code": o.stock_code,
                        "type": o.order_type,
                        "volume": o.order_volume,
                        "traded": o.traded_volume,
                        "price": o.price,
                        "status": o.order_status,
                        "time": o.order_time
                    }
                    for o in orders
                ]
            }
        else:
            result["data"] = {"count": 0, "orders": []}

    except Exception as e:
        result["status"] = "error"
        result["message"] = str(e)

    return result


def cmd_trades(args):
    """查询成交"""
    result = {"status": "success", "data_type": "trades"}

    try:
        xt_trader = get_trader()
        acc = get_account(args.acc_type)

        if not acc:
            result["status"] = "error"
            result["message"] = "未配置账号"
            return result

        xt_trader.start()
        if xt_trader.connect() != 0:
            result["status"] = "error"
            result["message"] = "连接失败"
            return result
        xt_trader.subscribe(acc)

        trades = xt_trader.query_stock_trades(acc)
        if trades:
            result["data"] = {
                "count": len(trades),
                "trades": [
                    {
                        "traded_id": t.traded_id,
                        "code": t.stock_code,
                        "volume": t.traded_volume,
                        "price": t.traded_price,
                        "amount": t.traded_amount,
                        "time": t.traded_time
                    }
                    for t in trades
                ]
            }
        else:
            result["data"] = {"count": 0, "trades": []}

    except Exception as e:
        result["status"] = "error"
        result["message"] = str(e)

    return result


def cmd_asset(args):
    """查询资产"""
    result = {"status": "success", "data_type": "asset"}

    try:
        xt_trader = get_trader()
        acc = get_account(args.acc_type)

        if not acc:
            result["status"] = "error"
            result["message"] = "未配置账号"
            return result

        xt_trader.start()
        if xt_trader.connect() != 0:
            result["status"] = "error"
            result["message"] = "连接失败"
            return result
        xt_trader.subscribe(acc)

        asset = xt_trader.query_stock_asset(acc)
        if asset:
            result["data"] = {
                "cash": asset.cash,
                "frozen": asset.frozen_cash,
                "market_value": asset.market_value,
                "total": asset.total_asset,
                "account_id": asset.account_id
            }
        else:
            result["data"] = {}

    except Exception as e:
        result["status"] = "error"
        result["message"] = str(e)

    return result


def cmd_async_order(args):
    """异步下单"""
    from xtquant import xtconstant

    result = {"status": "success", "data_type": "async_order", "code": args.code}

    try:
        xt_trader = get_trader()
        acc = get_account(args.acc_type)

        if not acc:
            result["status"] = "error"
            result["message"] = "未配置账号"
            return result

        xt_trader.start()
        if xt_trader.connect() != 0:
            result["status"] = "error"
            result["message"] = "连接失败"
            return result
        xt_trader.subscribe(acc)

        order_type = xtconstant.STOCK_BUY if args.type.lower() == 'buy' else xtconstant.STOCK_SELL
        seq = xt_trader.order_stock_async(
            acc,
            args.code,
            order_type,
            args.volume,
            xtconstant.FIX_PRICE,
            args.price,
            args.strategy or 'script',
            args.remark or ''
        )

        result["data"] = {
            "seq": seq,
            "success": seq > 0
        }

    except Exception as e:
        result["status"] = "error"
        result["message"] = str(e)

    return result


def add_args(parser):
    """添加命令行参数"""
    subparsers = parser.add_subparsers(dest='cmd', help='子命令')

    # order
    p = subparsers.add_parser('order', help='下单')
    p.add_argument('--code', '-c', required=True, help='证券代码')
    p.add_argument('--type', '-t', required=True, choices=['buy', 'sell'], help='买入/卖出')
    p.add_argument('--volume', '-v', type=int, required=True, help='数量')
    p.add_argument('--price', '-p', type=float, required=True, help='价格')
    p.add_argument('--strategy', '-s', default='', help='策略名称')
    p.add_argument('--remark', '-r', default='', help='备注')
    p.add_argument('--acc_type', default='STOCK', help='账号类型: STOCK/FUTURE')

    # cancel
    p = subparsers.add_parser('cancel', help='撤单')
    p.add_argument('--order_id', '-i', type=int, required=True, help='委托编号')
    p.add_argument('--acc_type', default='STOCK', help='账号类型')

    # positions
    p = subparsers.add_parser('positions', help='查询持仓')
    p.add_argument('--acc_type', default='STOCK', help='账号类型')

    # orders
    p = subparsers.add_parser('orders', help='查询委托')
    p.add_argument('--cancelable_only', '-o', action='store_true', help='仅可撤委托')
    p.add_argument('--acc_type', default='STOCK', help='账号类型')

    # trades
    p = subparsers.add_parser('trades', help='查询成交')
    p.add_argument('--acc_type', default='STOCK', help='账号类型')

    # asset
    p = subparsers.add_parser('asset', help='查询资产')
    p.add_argument('--acc_type', default='STOCK', help='账号类型')

    # async_order
    p = subparsers.add_parser('async_order', help='异步下单')
    p.add_argument('--code', '-c', required=True, help='证券代码')
    p.add_argument('--type', '-t', required=True, choices=['buy', 'sell'], help='买入/卖出')
    p.add_argument('--volume', '-v', type=int, required=True, help='数量')
    p.add_argument('--price', '-p', type=float, required=True, help='价格')
    p.add_argument('--strategy', '-s', default='', help='策略名称')
    p.add_argument('--remark', '-r', default='', help='备注')
    p.add_argument('--acc_type', default='STOCK', help='账号类型')


if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description='MiniQMT 交易脚本',
        epilog='环境变量: MINIQMT_PATH (默认路径), MINIQMT_ACCOUNT (账号), MINIQMT_SESSION (会话ID)'
    )
    add_args(parser)
    args = parser.parse_args()

    cmd_map = {
        'order': cmd_order,
        'cancel': cmd_cancel,
        'positions': cmd_positions,
        'orders': cmd_orders,
        'trades': cmd_trades,
        'asset': cmd_asset,
        'async_order': cmd_async_order,
    }

    if args.cmd in cmd_map:
        result = cmd_map[args.cmd](args)
        print(json.dumps(result, ensure_ascii=False, indent=2))
    else:
        parser.print_help()
