# Python 脚本初始化

## 重要：Python 文件路径配置

### 文件目录结构

```
通达信安装目录\
├── Tdxw.exe                 # 主程序
├── PYPlugins\               # 插件目录
│   ├── TPyth.dll            # 通达信Python通信DLL
│   ├── TPythClient.dll      # 通达信Python通信DLL
│   ├── user\                # 用户策略目录
│   │   └── tqcenter.py      # TdxQuant核心模块
│   ├── data\                # 下载数据目录
│   └── file\                # 发送文件目录
```

**Python 策略文件可以放在任意位置。**

导入 `tqcenter` 前，必须将通达信安装目录的 `PYPlugins\user` 路径添加到 `sys.path`。**使用 `sys.path.insert(0, ...)` 确保加载正确的 `tqcenter.py`。**

### 获取通达信安装目录

通达信Tdxw的安装目录存储在 Windows 注册表中：

- **注册表路径**：`HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows\CurrentVersion\Uninstall\通达信金融终端64`
- **键名**：`InstallLocation`

可参考以下 Python 代码自动读取安装目录。示例：

```python
import sys, winreg, os

# 从注册表获取安装目录
key_path = r"SOFTWARE\Microsoft\Windows\CurrentVersion\Uninstall\通达信金融终端64"
with winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, key_path) as key:
    tdx_root, _ = winreg.QueryValueEx(key, "InstallLocation")

# 添加 PYPlugins/user 到 sys.path
sys.path.insert(0, os.path.join(tdx_root, 'PYPlugins', 'user'))

from tqcenter import tq

tq.initialize(__file__)
```

**关键说明：**
- `tqcenter.py` 会在其上上级目录（`PYPlugins/`）自动定位 `TPythClient.dll`
- 使用 `sys.path.insert(0, ...)` 而非 `sys.path.append()`，优先加载通达信安装目录的 `tqcenter.py`
- `__file__` 为当前 Python 文件路径，用作策略唯一标识符
- 允许用户通过环境变量 `TDX_ROOT` 自定义安装目录。

**初始化要点：**

- 本技能必须检测到进程中有运行的TdxW.exe进程。
- 进程路径所在的程序目录即为通达信安装目录。
- python 文件示例中，请将 `tdx_root` 替换为通达信安装目录。
- 如果检测不到tdxw.exe进程，请提示用户先运行通达信客户端。
- 通达信安装目录下面指定位置如果不存在tqcenter.py 文件，提示用户当前的客户端不支持TQ策略，需升级。
- 如果有多个TdxW.exe进程，请依次寻找，直到找到第一个含有tqcenter.py 文件的进程。
- 找到之后，请记住这个位置，作为 `tdx_root`，不用每次都查找，除非这个位置失效。


## 股票代码格式

- **上交所**：`600000.SH`
- **深交所**：`000001.SZ`
- **北交所**：`430047.BJ`
- **港股**：`00700.HK`
- **美股**：`AAPL.US`
- **新三板**：`430047.NQ`
- **股票期权**：`10004073.SZO` / `10004073.SHO`
- **国内期货**：代码.CFF / .SHF / .DCE / .CZC / .INE / .GFE
- **中证指数**：`000300.CSI`
- **开放式基金净值**：代码.OF


## 时间格式

- 仅日期：`YYYYMMDD`（如 `20231231`）
- 含时间：`YYYYMMDDHHMMSS`（如 `20231231150000`）

## 相关参考

- [常量字典](dict.md)
- [tqcenter API](tq_api.md)
- [API 使用示例与故障排除](tq_use_case.md)
- [策略开发与回测指引](backtest.md)
