# 通用策略模板

可直接运行的股票日级骨架，覆盖四件事：配置集中到 `apply_settings`、盘前选池 + 盘中调仓、防未来数据、模拟盘热更新入口。换策略只改 `apply_settings` 的参数和 `select_targets` 的选股逻辑。

最小示例见 `SKILL.md`「策略骨架」；热更新机制与排查见 [simulation.md](simulation.md)。

```python
# 聚宽通用策略模板（股票 / 日级）
# 结构：配置集中 + 盘前选池 + 盘中调仓 + 模拟盘热更新入口
from jqdata import *


def initialize(context):
    set_benchmark('000300.XSHG')
    set_option('use_real_price', True)        # 动态复权（真实价格）
    set_option('avoid_future_data', True)     # 取到未来数据直接抛错，便于自查
    set_order_cost(OrderCost(open_tax=0, close_tax=0.001,
                             open_commission=0.0003, close_commission=0.0003,
                             close_today_commission=0, min_commission=5), type='stock')
    set_slippage(PriceRelatedSlippage(0.00246), type='stock')
    apply_settings(context)


def after_code_changed(context):
    # 模拟盘替换代码后的唯一入口，此时 initialize 不会重跑
    apply_settings(context)


def process_initialize(context):
    # 每次进程启动都执行；不可序列化对象在此重建，用 __ 开头的名字避免被 pickle
    g.__query = query(valuation)


def apply_settings(context):
    # ---- 策略参数：唯一来源，改策略只改这里 ----
    g.code_version = 'v1'
    g.index = '000300.XSHG'
    g.stock_num = 10             # 目标持仓数
    g.pool_size = 200            # 候选池上限
    g.ma_window = 20             # 均线过滤窗口，0 表示不过滤
    g.rebalance_time = '09:35'   # 调仓时间

    # ---- 运行状态：只初始化，不重置 ----
    if not hasattr(g, 'candidates'):
        g.candidates = []
    if not hasattr(g, 'buy_blocked'):
        g.buy_blocked = False

    # ---- 调度：先清空再全量注册，新增或改时间后不会残留旧任务 ----
    unschedule_all()
    run_daily(prepare, time='09:00')
    run_daily(rebalance, time=g.rebalance_time)
    log.info('配置装载 version=%s index=%s num=%s time=%s' % (
        g.code_version, g.index, g.stock_num, g.rebalance_time))


def prepare(context):
    # 盘前用上一交易日数据构建候选池，避免盘中重复查询
    date = context.previous_date
    stocks = get_index_stocks(g.index, date=date)
    if not stocks:
        g.candidates = []
        return
    q = query(valuation.code).filter(
        valuation.code.in_(stocks),
        valuation.pe_ratio > 0,
        valuation.market_cap > 0,
    ).order_by(valuation.market_cap.desc()).limit(g.pool_size)
    df = get_fundamentals(q, date=date)
    g.candidates = list(df['code'])
    log.info('候选池 %s 只 date=%s' % (len(g.candidates), date))


def select_targets(context):
    if not g.candidates:
        return []

    picked = g.candidates
    if g.ma_window > 0:
        # history 取天数据不含当天，无未来数据
        close = history(g.ma_window, '1d', 'close', g.candidates, df=True)
        if close.empty or len(close) < g.ma_window:
            return []
        ma = close.mean()
        last = close.iloc[-1]
        picked = [s for s in g.candidates if last[s] > ma[s]]

    # 过滤停牌、ST（只用当日可知字段，不拿 last_price 做信号）
    current = get_current_data()
    result = []
    for stock in picked:
        d = current[stock]
        if d.paused or d.is_st:
            continue
        result.append(stock)
        if len(result) >= g.stock_num:
            break
    return result


def rebalance(context):
    if g.buy_blocked:  # 由风控逻辑置 True，跨进程保留
        log.info('风控禁买，跳过调仓')
        return

    targets = select_targets(context)

    # 先卖：调出目标池，卖光不受整手限制
    for stock in list(context.portfolio.positions.keys()):
        pos = context.portfolio.positions[stock]
        if stock not in targets and pos.closeable_amount > 0:
            order_target_value(stock, 0)
            log.info('卖出 %s' % stock)

    # 再买：等权配置，order_target_value 会按整手取整
    if not targets:
        return
    target_value = context.portfolio.total_value / len(targets)
    for stock in targets:
        order_target_value(stock, target_value)
    log.info('调仓完成 version=%s targets=%s 单标的金额=%.0f' % (
        g.code_version, len(targets), target_value))
```

## 改造清单

| 需求 | 改哪里 |
|------|--------|
| 换股票池 | `apply_settings` 的 `g.index`；或 `prepare` 改用 `get_industry_stocks` / `get_all_securities(date=...)` |
| 换选股逻辑 | `select_targets`：财务筛选放 `prepare`（`run_query` 单次 4000 行、不支持连表），价量信号用 `history` |
| 换调仓频率 | `apply_settings` 中改为 `run_weekly` / `run_monthly`，注意 `day` 指第几个交易日，不是周几 |
| 加止损 | 用持仓 `avg_cost` 与 `history` 昨日收盘比较；日级回测不要用 `get_current_data().last_price` 做盘中判断 |
| 过滤涨停 | `get_current_data()` 的 `last_price >= high_limit` 跳过买入；该字段盘中才准确，盘前不可用 |
| 多策略组合 | `unschedule_all()` 会清掉其他子策略任务，重注册时必须全部列出 |
| 打包成模拟盘 | 先回测再创建；替换代码后看「配置装载」日志的 `code_version` 是否更新 |

## 回测到模拟的检查点

- 回测能跑通、日志正常，再创建模拟交易
- 日级模拟实际在 9:27~9:30 之间启动，`time='09:30'` 的任务可能早于开盘价可用，9:31 之后更稳
- 替换代码只在下一个调度时点生效，错过的时点不补跑
- 其余排查见 [simulation.md](simulation.md)
