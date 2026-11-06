---
name: "qmt-strategy"
description: "QMT 客户端（迅投极速策略交易系统）内置 Python 策略引擎开发指南，涵盖策略编写、回测、实盘交易、内置 API 参考与代码示例（基于 ContextInfo/passorder/get_trade_detail_data 等，非 xtquant 库）。当用户需要在 QMT 客户端中编写/回测/运行策略、查询 QMT 内置 API、从聚宽迁移至 QMT，或提及 QMT 策略、迅投策略、QMT 回测时使用；直接提及 passorder、ContextInfo、handlebar、get_market_data_ex、get_trade_detail_data 等内置 API，或描述 QMT 策略报错、回测无成交、GBK 编码报错等问题时同样适用。外部 xtquant/xtdata 连接场景不适用，请用 miniqmt 技能。"
metadata: {"openclaw":{"emoji":"📚"}}
---

# QMT Python 策略开发知识库

> ⛔ **铁律**：输出的一切代码只能使用 QMT 内置 API（`ContextInfo`/`passorder`/`get_trade_detail_data` 等）。代码中出现 `xtdata`/`xttrader`/`import jqdata` 即为错误输出。

本技能面向 QMT 客户端**内置策略引擎**——策略在 QMT 客户端内运行，使用内置 API（`ContextInfo`/`C`、`passorder`、`get_market_data_ex`、`get_trade_detail_data` 等），文件首行需 `#coding:gbk`。若需在**外部 Python 程序**中通过 **xtquant 库**（`xtdata`/`xttrader`）连接 QMT/MiniQMT 客户端获取行情或下单，请使用 `miniqmt` 技能。

## 📖 文档路由

全部文档位于 `references/` 目录，按场景按需读取，不要一次全读：

| 场景 | 读取文件 | 何时读取 |
|------|---------|---------|
| 新手入门 / 选运行机制 | `references/overview.md` → `references/execution-mechanisms.md` | 首次接触 QMT，或不确定 handlebar/subscribe/run_time 该用哪个 |
| API 速查 | `references/quick-reference.md` | 只需确认函数签名、常用参数、枚举取值；末尾骨架含 `TODO` 占位信号，交付前必须替换 |
| 编写回测策略 | `references/backtesting-guide.md` → `references/examples/backtest.md` | 需要完整回测流程、参数设置与可运行模板 |
| 编写实盘策略 | `references/live-trading-guide.md` → `references/examples/live-trading.md` | 涉及账号配置、委托管理、风险控制 |
| 事件驱动 / 定时任务 | `references/examples/subscribe.md`、`references/examples/run-time.md` | 需要用 subscribe 或 run_time 模式 |
| 从聚宽迁移 | `references/joinquant-migration.md` | 已有聚宽策略需改写为 QMT 内置写法 |
| 代码质量与调试 | `references/best-practices.md` | 需要编码规范、性能优化、常见陷阱 |
| 函数完整参数 | `references/python-innerApi/data_function.md`、`references/python-innerApi/trading_function.md`、`references/python-innerApi/system_function.md` | 速查卡不够用，需查全部参数与返回值 |
| 回调函数 | `references/python-innerApi/callback_function.md` | 需要 account/order/deal/position 主推回调 |
| 数据结构与枚举 | `references/python-innerApi/data_structure.md`、`references/python-innerApi/enum_constants.md` | 查 `m_*` 字段含义、opType/orderType/委托状态取值 |
| 报错与数据缺失 | `references/python-innerApi/question_answer.md`、`references/dict/question_answer.md` | 连不上服务、K线缺失、订阅失效、数据更新时间疑问 |
| 品种数据字段 | `references/dict/stock.md`、`references/dict/future.md`、`references/dict/option.md`、`references/dict/indexes.md`、`references/dict/bond.md`、`references/dict/floorfunds.md`、`references/dict/industry.md`、`references/dict/xuntou_factor.md` | 查某品种特有字段（财务、期权希腊字母、因子等） |
| 官方示例合集 | `references/python-innerApi/code_examples.md` | 需要更多可运行范例 |
| 界面与变量约定 | `references/python-innerApi/interface_operation.md`、`references/python-innerApi/variable_convention.md` | 配置回测/实盘界面，或确认周期、代码格式等约定 |
| 其余章节 | `references/python-innerApi/start_now.md`、`references/python-innerApi/quote_function.md`、`references/python-innerApi/drawing_function.md`、`references/python-innerApi/user_attention.md`、`references/dict/scenario_based_example.md` | 快速开始、扩展数据/因子引用、K线绘图标注、官方注意事项、场景化示例 |

## 🚦 执行流程

1. 判定场景（回测 / 实盘 / 仅查 API），按上表读 1~2 个文件；不整目录加载。
2. ⛔ 实盘确认门：涉及真实账号、`passorder` 或写入策略文件时，先确认账号类型（`stock`/`credit`/`FUTURE`）、是否模拟信号模式、标的代码、单笔数量；未确认前只给模板，不填真实账号、不产出可直接运行的实盘下单代码。
3. 输出完整策略文件（首行 `#coding:gbk`，含 `init`/`handlebar`），不只贴片段。
4. ⚠️ 逐条执行「交付前自检」，把未通过项明确列出。

## 🔧 关键速查

### 核心概念
| 概念 | 说明 |
|------|------|
| handlebar | 逐K线驱动（回测默认） |
| subscribe / run_time | 事件 / 定时驱动，仅实盘，回测不可用 |
| quicktrade=0 | 逐K线：下一根K线首个 tick 触发（默认值） |
| quicktrade=1 | 立即下单，仅非历史 bar（`C.is_last_bar()` 为 True 时触发） |
| quicktrade=2 | 立即下单且不判断 bar，历史 bar 也会触发，⚠️ 仅在明确知情时使用 |
| 编码与单位 | 文件首行 `#coding:gbk`；股票下单量必须是 100 的整数倍 |

> `2` 会在历史 bar 上也发出委托；`subscribe`/`run_time` 回调没有 K 线上下文，官方示例用 `2`。取值含义见 `references/python-innerApi/trading_function.md`。

### 最常用代码（签名速记）
```python
C.get_market_data_ex(['close'], [stock], end_time=bar_date, period='1d', count=100, subscribe=False)
C.get_full_tick(['600000.SH'])                                        # 仅实盘
passorder(23, 1101, account, stock, 5, -1, 100, C)                   # 8 参数短式，quicktrade 缺省为 0
passorder(23, 1101, account, stock, 5, -1, 100, '策略名', 1, '备注', C)  # 11 参数式，实盘立即下单
get_trade_detail_data(account, 'stock', 'position')                  # 持仓
get_trade_detail_data(account, 'stock', 'account')[0].m_dAvailable    # 可用资金（float，元）
```

- `get_market_data_ex` 的 `fields`、`stocks` 必须位置传参；回测 `subscribe=False`，实盘 `True`。
- 以上是片段。交付完整策略文件时必须补首行 `#coding:gbk` 与 `init`/`handlebar` 骨架，`C`/`stock`/`account`/`bar_date` 需在 `init` 中定义；完整模板见 `references/quick-reference.md` 与 `references/examples/`，其中 `TODO` 占位信号必须替换。

## ⚠️ 交付前自检

生成或修改任何 QMT 策略代码后，逐条核对：

- [ ] **编码声明**：文件首行 `#coding:gbk`，不可省略
- [ ] **位置参数**：`get_market_data_ex` 的 `fields`、`stocks` 必须位置传参，写成 `fields=`/`stocks=` 会报错
- [ ] **subscribe**：回测 `False`，实盘 `True`；`subscribe`/`run_time` 运行模式仅实盘支持，回测不可用
- [ ] **账号类型**：`get_trade_detail_data` 第二参数，股票 `'stock'`、两融 `'credit'`、期货 `'FUTURE'`
- [ ] **金额单位**：`m_dAvailable` 等资金字段是 **float，单位元**，可直接参与计算；若下单量恰为预期 100 倍，才检查该账户是否按分返回
- [ ] **数量单位**：股票下单量必须是 100 的整数倍
- [ ] **quicktrade**：实盘 `handlebar` 立即下单用 `1`；`2` 会让历史 bar 也触发委托，仅在用户明确要求时使用
- [ ] **完整文件**：交付的是可运行策略文件（编码声明 + `init`/`handlebar`），不是无骨架片段；模板中 `TODO` 占位信号已全部替换
- [ ] **API 边界**：无 `xtdata`/`xttrader`/聚宽 API 混入

## 📄 文档来源与合规

`references/` 根目录文档与 `references/examples/` 为本技能作者原创整理；`references/python-innerApi/`、`references/dict/` 为迅投官方知识库（[dict.thinktrader.net](https://dict.thinktrader.net)）离线快照，版权归迅投所有，各文件首部保留官方原文 `url` 与 `title`。官方层内容仅作离线查阅与内部学习参考，对外分发、转载或商业使用请以迅投官方知识库为准并遵守其使用条款；原创主张仅适用于原创教程层内容。
