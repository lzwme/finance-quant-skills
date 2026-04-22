#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
TdxQuant 公共初始化模块
- 自动检测通达信安装目录（注册表 / TdxW.exe 进程）
- 将 PYPlugins/user 添加到 sys.path
- 初始化 tq 连接
"""

import json
import os
import subprocess
import sys


def find_tdx_root():
    """查找通达信安装目录"""

    def is_vaild_root_path(install_path: str | None):
        if install_path is None: return False
        tqcenter_path = os.path.join(install_path, "PYPlugins", "user", "tqcenter.py")
        return os.path.isfile(tqcenter_path)

    # 环境变量读取，优先级最高
    install_path = os.getenv('TDX_ROOT')
    if is_vaild_root_path(install_path): return install_path

    # 方法1: 从注册表读取
    try:
        import winreg
        key_path = r"SOFTWARE\Microsoft\Windows\CurrentVersion\Uninstall\通达信金融终端64"
        with winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, key_path) as key:
            install_path, _ = winreg.QueryValueEx(key, "InstallLocation")
            if is_vaild_root_path(install_path): return install_path
    except Exception:
        pass

    # 方法2: 从 TdxW.exe 进程路径获取
    try:
        result = subprocess.run(
            ["wmic", "process", "where", "name='TdxW.exe'", "get", "ExecutablePath", "/value"],
            capture_output=True, text=True, timeout=5
        )
        for line in result.stdout.strip().split("\n"):
            line = line.strip()
            if line.startswith("ExecutablePath="):
                exe_path = line.split("=", 1)[1].strip()
                install_path = os.path.dirname(exe_path)
                if is_vaild_root_path(install_path): return install_path
    except Exception:
        pass

    return None


def init_tq():
    """初始化 tq 连接，返回 tq 对象"""
    tdx_root = find_tdx_root()
    if not tdx_root:
        print(json.dumps({
            "status": "error",
            "message": "未找到通达信安装目录。请确保：1) 已安装通达信金融终端(支持TQ策略版)；2) 通达信客户端正在运行"
        }, ensure_ascii=False))
        sys.exit(1)

    user_path = os.path.join(tdx_root, "PYPlugins", "user")
    if user_path not in sys.path:
        sys.path.insert(0, user_path)

    try:
        from tqcenter import tq
    except ImportError:
        print(json.dumps({
            "status": "error",
            "message": f"无法导入 tqcenter 模块。请检查 {user_path} 下是否存在 tqcenter.py"
        }, ensure_ascii=False))
        sys.exit(1)

    tq.initialize(os.path.abspath(__file__))
    return tq
