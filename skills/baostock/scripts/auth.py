#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
BaoStock 认证模块
支持自定义服务器 IP 和端口配置
"""

import json
import sys
import os


def auth_bs():
    """
    登录并返回已认证的 baostock 模块
    
    可选环境变量:
    - BAOSTOCK_SERVER_IP: 自定义服务器地址（用于 nginx 代理等场景）
    - BAOSTOCK_SERVER_PORT: 服务器端口，默认 10030
    
    Returns:
        module: 已认证的 baostock 模块
        
    Exits:
        如果登录失败，输出 JSON 错误信息并退出
    """
    try:
        import baostock as bs
        import baostock.common.contants as cons
    except ImportError:
        print(json.dumps({
            'status': 'error',
            'message': 'baostock 库未安装，请先安装: pip install baostock'
        }, ensure_ascii=False))
        sys.exit(1)
    
    # 获取可选的服务器配置
    server_ip = os.getenv('BAOSTOCK_SERVER_IP')
    server_port = os.getenv('BAOSTOCK_SERVER_PORT')
    
    # 支持自定义 BaoStock 服务器配置（仅首次生效，后续 login 复用已有连接）
    if server_ip:
        cons.BAOSTOCK_SERVER_IP = server_ip
        print(f"BaoStock server IP overridden: {server_ip}", file=sys.stderr)
    
    if server_port:
        try:
            port = int(server_port)
            if port != 10030:
                cons.BAOSTOCK_SERVER_PORT = port
                print(f"BaoStock server port overridden: {port}", file=sys.stderr)
        except ValueError:
            print(json.dumps({
                'status': 'error',
                'message': f'BAOSTOCK_SERVER_PORT 必须是有效的端口号: {server_port}'
            }, ensure_ascii=False))
            sys.exit(1)
    
    # 执行登录
    try:
        lg = bs.login()
        if lg.error_code != "0":
            error_msg = lg.error_msg
            error_code = lg.error_code
            
            if error_code == "10001011":
                error_msg = "IP 已加入黑名单，需联系 BaoStock 官方解除"
            
            print(json.dumps({
                'status': 'error',
                'message': f'BaoStock 登录失败: {error_msg} (错误码: {error_code})'
            }, ensure_ascii=False))
            sys.exit(1)
        
        return bs
        
    except Exception as e:
        print(json.dumps({
            'status': 'error',
            'message': f'BaoStock 登录异常: {str(e)}'
        }, ensure_ascii=False))
        sys.exit(1)


def logout_bs(bs):
    """
    登出 BaoStock
    
    Args:
        bs: baostock 模块
    """
    try:
        bs.logout()
    except Exception:
        pass


if __name__ == '__main__':
    # 测试认证
    bs = auth_bs()
    print(json.dumps({
        'status': 'success',
        'message': 'BaoStock 登录成功'
    }, ensure_ascii=False))
    logout_bs(bs)
