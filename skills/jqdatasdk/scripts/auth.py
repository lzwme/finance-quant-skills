#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
聚宽数据SDK认证模块
支持用户名密码和Token两种认证方式
支持自定义 host 和 port
"""

import json
import sys
import os


def auth_jq():
    """
    认证并返回已认证的 jqdatasdk 模块
    
    环境变量优先级:
    1. JQDATA_USERNAME + JQDATA_PASSWORD (用户名密码方式)
    2. JQDATA_TOKEN (Token方式)
    
    可选环境变量:
    - JQDATA_HOST: 自定义服务器地址
    - JQDATA_PORT: 自定义端口
    
    Returns:
        module: 已认证的 jqdatasdk 模块
        
    Exits:
        如果认证失败，输出JSON错误信息并退出
    """
    try:
        import jqdatasdk as jq
    except ImportError:
        print(json.dumps({
            'status': 'error',
            'message': 'jqdatasdk 库未安装，请先安装: pip install jqdatasdk'
        }, ensure_ascii=False))
        sys.exit(1)
    
    # 获取可选的 host 和 port 配置
    host = os.getenv('JQDATA_HOST') or None
    port = os.getenv('JQDATA_PORT') or None
    if port:
        try:
            port = int(port)
        except ValueError:
            print(json.dumps({
                'status': 'error',
                'message': f'JQDATA_PORT 必须是有效的端口号: {port}'
            }, ensure_ascii=False))
            sys.exit(1)
    
    # 优先使用用户名密码方式
    username = os.getenv('JQDATA_USERNAME')
    password = os.getenv('JQDATA_PASSWORD')
    
    if username and password:
        try:
            jq.auth(username, password, host=host, port=port)
            return jq
        except Exception as e:
            print(json.dumps({
                'status': 'error',
                'message': f'聚宽认证失败(用户名密码方式): {str(e)}'
            }, ensure_ascii=False))
            sys.exit(1)
    
    # 回退到Token方式，使用正确的 auth_by_token 方法
    token = os.getenv('JQDATA_TOKEN')
    if token:
        try:
            jq.auth_by_token(token, host=host, port=port)
            return jq
        except Exception as e:
            print(json.dumps({
                'status': 'error',
                'message': f'聚宽认证失败(Token方式): {str(e)}'
            }, ensure_ascii=False))
            sys.exit(1)
    
    # 两种认证方式都未配置
    print(json.dumps({
        'status': 'error',
        'message': '缺少聚宽认证凭证，请配置以下任一方式: \n1. JQDATA_USERNAME + JQDATA_PASSWORD (推荐)\n2. JQDATA_TOKEN'
    }, ensure_ascii=False))
    sys.exit(1)


if __name__ == '__main__':
    # 测试认证
    jq = auth_jq()
    print(json.dumps({
        'status': 'success',
        'message': '聚宽认证成功'
    }, ensure_ascii=False))
