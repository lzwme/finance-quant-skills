#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
MiniQMT 行情数据获取脚本
支持：行情快照、K线数据、分笔数据、实时行情（全推/单股订阅）
"""

import argparse
import json
import sys
import os
import time

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from xtquant import xtdata
xtdata.enable_hello = False

def cmd_snapshot(args):
    """获取行情快照"""
    result = {"status": "success", "data_type": "snapshot", "code": args.code}
    try:
        data = xtdata.get_instrument_detail(args.code)
        if data:
            result["data"] = data
        else:
            result["status"] = "error"
            result["message"] = f"未找到合约 {args.code}"
    except Exception as e:
        result["status"] = "error"
        result["message"] = str(e)
    return result


def cmd_kline(args):
    """获取K线数据"""
    result = {
        "status": "success",
        "data_type": "kline",
        "code": args.code,
        "period": args.period,
        "count": args.count
    }
    try:
        # 先下载历史数据
        xtdata.download_history_data(args.code, args.period, incrementally=True)
        df_dict = xtdata.get_market_data_ex(
            field_list=[],
            stock_list=[args.code],
            period=args.period,
            start_time=args.start or "",
            end_time=args.end or "",
            count=args.count or -1,
            dividend_type=args.fq or "none",
            fill_data=True
        )

        if df_dict and args.code in df_dict:
            import pandas as pd
            df = df_dict[args.code]
            if isinstance(df, pd.DataFrame) and not df.empty:
                result["data"] = {
                    "columns": df.columns.tolist(),
                    "data": df.to_dict('records'),
                    "count": len(df)
                }
            else:
                result["data"] = {"columns": [], "data": [], "count": 0}
        else:
            result["data"] = {"columns": [], "data": [], "count": 0}
    except Exception as e:
        result["status"] = "error"
        result["message"] = str(e)
    return result


def cmd_tick(args):
    """获取分笔数据"""
    result = {
        "status": "success",
        "data_type": "tick",
        "code": args.code,
        "count": args.count
    }
    try:
        tick_dict = xtdata.get_market_data_ex(
            field_list=[],
            stock_list=[args.code],
            period='tick',
            start_time=args.start or "",
            end_time=args.end or "",
            count=args.count or -1,
            dividend_type='none',
            fill_data=True
        )
        if tick_dict and args.code in tick_dict:
            ticks = tick_dict[args.code]
            if hasattr(ticks, 'tolist'):
                ticks = ticks.tolist()
            result["data"] = {"count": len(ticks) if isinstance(ticks, list) else 0}
            if args.count > 0 and isinstance(ticks, list):
                result["data"]["ticks"] = ticks[-args.count:]
            else:
                result["data"]["ticks"] = ticks
        else:
            result["data"] = {"count": 0, "ticks": []}
    except Exception as e:
        result["status"] = "error"
        result["message"] = str(e)
    return result


def cmd_full_tick(args):
    """获取全推/实时行情快照"""
    result = {"status": "success", "data_type": "full_tick"}
    try:
        codes = [c.strip() for c in args.codes.split(',')]
        ticks = xtdata.get_full_tick(codes)
        result["data"] = {
            "count": len(ticks),
            "items": {code: ticks.get(code, {}) for code in ticks}
        }
    except Exception as e:
        result["status"] = "error"
        result["message"] = str(e)
    return result


def cmd_download(args):
    """下载历史数据"""
    result = {
        "status": "success",
        "data_type": "download",
        "code": args.code,
        "period": args.period
    }
    try:
        xtdata.download_history_data(
            args.code,
            args.period,
            start_time=args.start or "",
            end_time=args.end or ""
        )
        result["message"] = "下载完成"
    except Exception as e:
        result["status"] = "error"
        result["message"] = str(e)
    return result


def cmd_instrument_info(args):
    """获取合约详细信息"""
    result = {"status": "success", "data_type": "instrument_info", "code": args.code}
    try:
        data = xtdata.get_instrument_detail(args.code, iscomplete=args.verbose)
        result["data"] = data
        if data is None:
            result["status"] = "error"
            result["message"] = f"未找到合约 {args.code}"
    except Exception as e:
        result["status"] = "error"
        result["message"] = str(e)
    return result


def cmd_divid_factors(args):
    """获取除权数据"""
    result = {"status": "success", "data_type": "divid_factors", "code": args.code}
    try:
        df = xtdata.get_divid_factors(args.code, args.start or "", args.end or "")
        if df is not None and not df.empty:
            result["data"] = {
                "columns": df.columns.tolist(),
                "data": df.to_dict('records')
            }
        else:
            result["data"] = {"columns": [], "data": []}
    except Exception as e:
        result["status"] = "error"
        result["message"] = str(e)
    return result


def cmd_ipo_info(args):
    """获取新股申购信息"""
    result = {"status": "success", "data_type": "ipo_info"}
    try:
        ipo_list = xtdata.get_ipo_info(args.start or "", args.end or "")
        result["data"] = {"count": len(ipo_list), "items": ipo_list}
    except Exception as e:
        result["status"] = "error"
        result["message"] = str(e)
    return result


def cmd_trading_calendar(args):
    """获取交易日历"""
    result = {"status": "success", "data_type": "trading_calendar", "market": args.market}
    try:
        dates = xtdata.get_trading_calendar(
            args.market,
            start_time=args.start or "",
            end_time=args.end or ""
        )
        result["data"] = {"count": len(dates), "dates": dates}
    except Exception as e:
        result["status"] = "error"
        result["message"] = str(e)
    return result


def cmd_subscribe(args):
    """订阅实时行情（带回调）"""
    result = {"status": "success", "data_type": "subscribe", "code": args.code}
    callbacks = []

    def on_data(datas):
        callbacks.append(datas)
        print(json.dumps({"event": "tick", "data": datas}))

    try:
        seq = xtdata.subscribe_quote(
            args.code,
            period=args.period or 'tick',
            start_time=args.start or "",
            end_time=args.end or "",
            count=args.count or 0,
            callback=on_data
        )
        result["data"] = {"seq": seq, "callbacks_count": 0}
        if args.duration > 0:
            time.sleep(args.duration)
            result["data"]["callbacks_count"] = len(callbacks)
        else:
            xtdata.run()
    except Exception as e:
        result["status"] = "error"
        result["message"] = str(e)
    return result


def add_args(parser):
    """添加命令行参数"""
    subparsers = parser.add_subparsers(dest='cmd', help='子命令')

    # snapshot
    p = subparsers.add_parser('snapshot', help='行情快照')
    p.add_argument('--code', '-c', required=True, help='证券代码，如 600519.SH')

    # kline
    p = subparsers.add_parser('kline', help='K线数据')
    p.add_argument('--code', '-c', required=True, help='证券代码')
    p.add_argument('--period', default='1d', help='周期: tick/1m/5m/15m/30m/1h/1d/1w/1mon')
    p.add_argument('--start', '-s', default='', help='起始时间 YYYYMMDD')
    p.add_argument('--end', '-e', default='', help='结束时间 YYYYMMDD')
    p.add_argument('--count', '-n', type=int, default=-1, help='数据个数，-1为全部')
    p.add_argument('--fq', default='none', help='复权: none/front/back/front_ratio/back_ratio')

    # tick
    p = subparsers.add_parser('tick', help='分笔数据')
    p.add_argument('--code', '-c', required=True, help='证券代码')
    p.add_argument('--start', '-s', default='', help='起始时间')
    p.add_argument('--end', '-e', default='', help='结束时间')
    p.add_argument('--count', '-n', type=int, default=-1, help='数据个数')

    # full_tick
    p = subparsers.add_parser('full_tick', help='实时行情快照')
    p.add_argument('--codes', required=True, help='证券代码列表，逗号分隔')

    # download
    p = subparsers.add_parser('download', help='下载历史数据')
    p.add_argument('--code', '-c', required=True, help='证券代码')
    p.add_argument('--period', default='1d', help='周期')
    p.add_argument('--start', '-s', default='', help='起始时间')
    p.add_argument('--end', '-e', default='', help='结束时间')

    # instrument_info
    p = subparsers.add_parser('instrument_info', help='合约详细信息')
    p.add_argument('--code', '-c', required=True, help='证券代码')
    p.add_argument('--verbose', '-v', action='store_true', help='完整字段')

    # divid_factors
    p = subparsers.add_parser('divid_factors', help='除权数据')
    p.add_argument('--code', '-c', required=True, help='证券代码')
    p.add_argument('--start', '-s', default='', help='起始时间')
    p.add_argument('--end', '-e', default='', help='结束时间')

    # ipo_info
    p = subparsers.add_parser('ipo_info', help='新股申购信息')
    p.add_argument('--start', '-s', default='', help='起始日期')
    p.add_argument('--end', '-e', default='', help='结束日期')

    # trading_calendar
    p = subparsers.add_parser('trading_calendar', help='交易日历')
    p.add_argument('--market', default='SH', help='市场: SH/SZ')
    p.add_argument('--start', '-s', default='', help='起始时间')
    p.add_argument('--end', '-e', default='', help='结束时间')

    # subscribe
    p = subparsers.add_parser('subscribe', help='订阅实时行情')
    p.add_argument('--code', '-c', required=True, help='证券代码')
    p.add_argument('--period', default='tick', help='周期')
    p.add_argument('--start', '-s', default='', help='起始时间')
    p.add_argument('--end', '-e', default='', help='结束时间')
    p.add_argument('--count', '-n', type=int, default=0, help='历史数据个数')
    p.add_argument('--duration', '-d', type=int, default=0, help='持续秒数，0表示无限')


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='MiniQMT 行情数据获取')
    add_args(parser)
    args = parser.parse_args()

    cmd_map = {
        'snapshot': cmd_snapshot,
        'kline': cmd_kline,
        'tick': cmd_tick,
        'full_tick': cmd_full_tick,
        'download': cmd_download,
        'instrument_info': cmd_instrument_info,
        'divid_factors': cmd_divid_factors,
        'ipo_info': cmd_ipo_info,
        'trading_calendar': cmd_trading_calendar,
        'subscribe': cmd_subscribe,
    }

    if args.cmd in cmd_map:
        result = cmd_map[args.cmd](args)
        print(json.dumps(result, ensure_ascii=False, indent=2))
    else:
        parser.print_help()
