# 模拟盘热更新与状态管理

替换代码只更新代码与配置的装载入口，不重置已有运行状态：`initialize` 不会重跑，`g` 中的旧值会被恢复。所以"回测正常、模拟盘改参数没生效"通常是配置没有迁移过去，而不是选股逻辑出错。

与 `api.md`「模拟盘注意事项」互补：那边是平台机制原文，这里给定位顺序、迁移模板和验证方法。

## 先定位断点

| 断点 | 现象 | 处理 |
|------|------|------|
| ① 代码未装载 | 模拟盘代码页仍是旧代码，替换记录为空 | 「修改代码」，或「替换代码」选已回测版本（同策略、同 Python 版本） |
| ② 代码已装载，参数没更新 | 日志打印的仍是旧参数 | 配置迁移到 `after_code_changed` |
| ③ 参数已更新，行为没变 | 日志是新参数，但没有委托/成交 | 查候选名单、卖出逻辑、委托状态 |

逐段核对这条链：**代码版本 → 参数装载 → 定时回调 → 候选名单 → 委托 → 成交**。哪一段没有日志，就停在那一段排查。参数生效不等于成交：旧持仓不会因参数变化自动减仓。

## 三个入口

| 入口 | 执行时机 | 职责 |
|------|----------|------|
| `initialize(context)` | 首次创建模拟盘时一次 | 基准、费率、滑点、初始 `g`、任务注册 |
| `after_code_changed(context)` | 替换/修改代码后，下一次进程启动 | 新参数、新调度、状态保留策略、日志级别 |
| `process_initialize(context)` | 每次进程启动 | 重建不可序列化对象（`query`、连接、文件句柄）；**不能**替代迁移 |

回测也会执行一次 `after_code_changed`，不要放入只该在模拟盘执行的动作。

## g 里的三类数据

| 类型 | 例子 | 替换代码时 |
|------|------|-----------|
| 策略参数 | 目标持仓数、阈值、调仓时间 | 按新版本覆盖 |
| 运行状态 | 禁买标志、冷却期结束日、持仓最高价 | 保留，不要随手清零 |
| 临时对象 | `query` 对象、网络连接 | 每次进程启动重建 |

前两类最容易混：改持仓数是更新配置；把已触发的禁买标志重新赋值 `False`，则可能破坏当前风控状态。

## 模板：单一配置源 + 日志打点

真实策略把 `check_state` 换成调仓函数即可；排障时放在独立模拟盘，只打日志、不下单。

```python
from jqdata import *


def initialize(context):
    set_benchmark('000300.XSHG')
    set_option('use_real_price', True)
    apply_settings(context)


def after_code_changed(context):
    apply_settings(context)


def apply_settings(context):
    g.code_version = 'hotupdate_demo_v1'   # 每次替换改为 v2、v3…
    g.stock_num = 8
    g.check_time = '09:35'
    if not hasattr(g, 'buy_blocked'):
        g.buy_blocked = False
    unschedule_all()
    run_daily(check_state, time=g.check_time)
    log.info('配置装载 version=%s stock_num=%s time=%s blocked=%s' % (
        g.code_version, g.stock_num, g.check_time, g.buy_blocked))


def check_state(context):
    log.info('回调执行 dt=%s version=%s stock_num=%s blocked=%s' % (
        context.current_dt, g.code_version, g.stock_num, g.buy_blocked))
```

- 参数只写在 `apply_settings`，避免 `initialize` 与 `after_code_changed` 两处漂移
- `unschedule_all()` 取消**全部**定时任务；组合策略要连同其他子策略的任务一起重注册
- 不可序列化对象不要放 `g`；确需放置时用 `__` 前缀（不参与 pickle），并在 `process_initialize` 重建

## 验证步骤

1. 用 v1 建模拟盘，确认「配置装载」日志出现
2. 版本改 v2、`stock_num` 改 6、`check_time` 改到一个**尚未到达**的交易时点，替换代码
3. 看「配置装载」是否为新值——验证迁移是否成功
4. 到点看「回调执行」是否为新值——验证调度是否生效
5. 状态保留：先把 `g.buy_blocked` 置 `True`，替换后确认仍为 `True`

## 常见误判

- **9:40 替换，任务设在 9:35**：错过的调度时点不补跑，当天没有该回调日志不代表更新失败；需要当天生效的风控动作应在替换入口显式处理，是否顺带下单要结合时点和重复下单控制
- **只有「配置装载」没有「回调执行」**：任务未注册成功或时间已过
- **日志时间是逻辑时间**：与回测同，需要真实时间请 `print(datetime.datetime.now())`
- **平台侧未运行**：长时间未登录被停、延迟运行、暂停、运行失败，都表现为"代码没生效"
- **回测无法覆盖**：单次回测不能复现"运行到中途替换代码"，热更新必须在独立模拟盘验证；状态检查与收益回测分开记录
