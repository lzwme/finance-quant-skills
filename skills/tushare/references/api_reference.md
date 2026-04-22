# Tushare API 参考

## 目录
- [概览](#概览)
- [行情数据 API](#行情数据-api)
- [财务数据 API](#财务数据-api)
- [股票信息 API](#股票信息-api)
- [指数与宏观数据 API](#指数与宏观数据-api)
- [错误处理](#错误处理)

## 概览

本文档提供 Tushare 核心 API 的详细参数说明和返回格式。

**客户端初始化：**
```python
import tushare as ts

pro = ts.pro_api('你的Token')
```

## 行情数据 API

### daily

获取日线行情

**参数：**
- `ts_code`: str，股票代码，格式 `XXXXXX.SH` 或 `XXXXXX.SZ`，支持多只股票用逗号分隔
- `trade_date`: str，交易日期，格式 `YYYYMMDD`
- `start_date`: str，开始日期，格式 `YYYYMMDD`
- `end_date`: str，结束日期，格式 `YYYYMMDD`
- `fields`: str，字段列表，逗号分隔

**返回字段：**
- `ts_code`: 股票代码
- `trade_date`: 交易日期
- `open`: 开盘价
- `high`: 最高价
- `low`: 最低价
- `close`: 收盘价
- `pre_close`: 昨收价
- `change`: 涨跌额
- `pct_chg`: 涨跌幅 (%)
- `vol`: 成交量 (手)
- `amount`: 成交额 (千元)

**示例：**
```python
df = pro.daily(ts_code='000001.SZ',
               start_date='20240101',
               end_date='20240131')
```

### adj_factor

获取复权因子

**参数：**
- `ts_code`: str，股票代码
- `trade_date`: str，交易日期
- `start_date`: str，开始日期
- `end_date`: str，结束日期

**返回字段：**
- `ts_code`: 股票代码
- `trade_date`: 交易日期
- `adj_factor`: 复权因子

**示例：**
```python
df = pro.adj_factor(ts_code='000001.SZ',
                    start_date='20240101',
                    end_date='20240131')
```

### daily_basic

获取每日指标

**参数：**
- `ts_code`: str，股票代码
- `trade_date`: str，交易日期
- `start_date`: str，开始日期
- `end_date`: str，结束日期
- `fields`: str，字段列表

**返回字段：**
- `ts_code`: 股票代码
- `trade_date`: 交易日期
- `close`: 收盘价
- `turnover_rate`: 换手率 (%)
- `turnover_rate_f`: 换手率（自由流通股）
- `volume_ratio`: 量比
- `pe`: 市盈率
- `pe_ttm`: 市盈率TTM
- `pb`: 市净率
- `ps`: 市销率
- `ps_ttm`: 市销率TTM
- `dv_ratio`: 股息率
- `dv_ttm`: 股息率TTM
- `total_share`: 总股本 (万股)
- `float_share`: 流通股本 (万股)
- `free_share`: 自由流通股本 (万股)
- `total_mv`: 总市值 (万元)
- `circ_mv`: 流通市值 (万元)

**示例：**
```python
df = pro.daily_basic(ts_code='000001.SZ',
                     start_date='20240101',
                     end_date='20240131')
```

### weekly

获取周线行情

**参数：** 同 `daily`

**返回字段：** 同 `daily`

### monthly

获取月线行情

**参数：** 同 `daily`

**返回字段：** 同 `daily`

## 财务数据 API

### income

获取利润表

**参数：**
- `ts_code`: str，股票代码
- `ann_date`: str，公告日期，格式 `YYYYMMDD`
- `f_ann_date`: str，首次公告日期
- `start_date`: str，报告期开始日期
- `end_date`: str，报告期结束日期
- `period`: str，报告期，格式 `YYYY` 或 `YYYYMM`
- `report_type`: str，报告类型
  - `1`: 合并报表
  - `2`: 单季合并
  - `3`: 调整单季合并表
  - `4`: 调整合并报表
  - `5`: 调整前合并报表

**返回字段：**
- `ts_code`: 股票代码
- `ann_date`: 公告日期
- `f_ann_date`: 首次公告日期
- `end_date`: 报告期
- `report_type`: 报告类型
- `comp_type`: 公司类型
- `basic_eps`: 基本每股收益
- `diluted_eps`: 稀释每股收益
- `total_revenue`: 营业总收入
- `revenue`: 营业收入
- `int_income`: 利息收入
- `prem_earned`: 已赚保费
- `comm_income`: 手续费及佣金收入
- `n_commis_income`: 手续费及佣金净收入
- `n_oth_income`: 其他经营收益
- `n_oth_b_income`: 加:其他业务收入
- `total_cogs`: 营业总成本
- `oper_cost`: 营业成本
- `int_exp`: 利息支出
- `comm_exp`: 手续费及佣金支出
- `biz_tax_surchg`: 营业税金及附加
- `sell_exp`: 销售费用
- `admin_exp`: 管理费用
- `fin_exp`: 财务费用
- `assets_impair_loss`: 资产减值损失
- `credit_impair_loss`: 信用减值损失
- `prem_refund`: 退保金
- `compen_payout`: 赔付支出
- `reser_insur_liab`: 提取保险责任准备金
- `div_payout_test`: 保户红利支出
- `reinsur_exp`: 分保费用
- `oper_exp`: 营业支出
- `oper_tax`: 营业税金及附加
- `assets_impair_loss`: 资产减值损失
- `tot_oper_rev`: 营业总收入
- `tot_oper_cost`: 营业总成本
- `oper_profit`: 营业利润
- `non_oper_income`: 加:营业外收入
- `non_oper_exp`: 减:营业外支出
- `nca_disploss`: 减:非流动资产处置损失
- `total_profit`: 利润总额
- `income_tax`: 减:所得税费用
- `n_income`: 净利润
- `n_income_attr_p`: 净利润(含少数股东损益)
- `minority_gain`: 少数股东损益
- `oth_compr_income`: 其他综合收益
- `t_compr_income`: 综合收益总额
- `compr_inc_attr_p`: 归属于母公司(或股东)的综合收益总额
- `compr_inc_attr_m_s`: 归属于母公司所有者的综合收益总额

**示例：**
```python
df = pro.income(ts_code='000001.SZ',
                period='2023',
                report_type='1')
```

### balancesheet

获取资产负债表

**参数：** 同 `income`

**返回字段：**
- `ts_code`: 股票代码
- `ann_date`: 公告日期
- `f_ann_date`: 首次公告日期
- `end_date`: 报告期
- `report_type`: 报告类型
- `comp_type`: 公司类型
- `total_assets`: 资产总计
- `cash_equivalents`: 货币资金
- `trading_assets`: 交易性金融资产
- `note_receivable`: 应收票据
- `accounts_receivable`: 应收账款
- `oth_receivable`: 其他应收款
- `prepayment`: 预付款项
- `oth_receivable`: 其他应收款
- `oth_current_assets`: 其他流动资产
- `total_current_assets`: 流动资产合计
- `fa_avail_for_sale`: 可供出售金融资产
- `htm_investments`: 持有至到期投资
- `lt_eqt_invest`: 长期股权投资
- `invest_real_estate`: 投资性房地产
- `fixed_assets`: 固定资产
- `cip`: 在建工程
- `const_materials`: 工程物资
- `fixed_assets_disp`: 固定资产清理
- `biological_assets`: 生产性生物资产
- `oil_and_gas_assets`: 油气资产
- `intan_assets`: 无形资产
- `goodwill`: 商誉
- `long_deferred_expenses`: 长期待摊费用
- `deferred_tax_assets`: 递延所得税资产
- `other_non_current_assets`: 其他非流动资产
- `total_non_current_assets`: 非流动资产合计
- `total_liab`: 负债合计
- `st_borr`: 短期借款
- `trading_fin_liab`: 交易性金融负债
- `notes_payable`: 应付票据
- `acct_payable`: 应付账款
- `adv_receipts`: 预收款项
- `sold_for_repur_sec`: 卖出回购金融资产款
- `commission_payable`: 应付手续费及佣金
- `employee_benefits_payable`: 应付职工薪酬
- `taxes_payable`: 应交税费
- `int_payable`: 应付利息
- `div_payable`: 应付股利
- `oth_payable`: 其他应付款
- `oth_current_liab`: 其他流动负债
- `total_current_liab`: 流动负债合计
- `lt_borr`: 长期借款
- `bonds_payable`: 应付债券
- `lt_payable`: 长期应付款
- `specific_payables`: 专项应付款
- `estimated_liab`: 预计负债
- `deferred_tax_liab`: 递延所得税负债
- `defer_income_non_cur`: 递延收益-非流动负债
- `other_non_current_liab`: 其他非流动负债
- `total_non_current_liab`: 非流动负债合计
- `total_owner_equities`: 负债和股东权益总计
- `parent_owner_equities`: 归属于母公司所有者权益
- `minority_interest`: 少数股东权益

**示例：**
```python
df = pro.balancesheet(ts_code='000001.SZ',
                      period='2023',
                      report_type='1')
```

### cashflow

获取现金流量表

**参数：** 同 `income`

**返回字段：**
- `ts_code`: 股票代码
- `ann_date`: 公告日期
- `f_ann_date`: 首次公告日期
- `end_date`: 报告期
- `report_type`: 报告类型
- `comp_type`: 公司类型
- `n_cashflow_act`: 经营活动产生的现金流量净额
- `n_cashflow_inv_act`: 投资活动产生的现金流量净额
- `n_cash_flows_fnc_act`: 筹资活动产生的现金流量净额

**示例：**
```python
df = pro.cashflow(ts_code='000001.SZ',
                  period='2023',
                  report_type='1')
```

### fina_indicator

获取财务指标

**参数：**
- `ts_code`: str，股票代码
- `ann_date`: str，公告日期
- `start_date`: str，报告期开始日期
- `end_date`: str，报告期结束日期
- `period`: str，报告期

**返回字段：**
- `ts_code`: 股票代码
- `ann_date`: 公告日期
- `end_date`: 报告期
- `roe`: 净资产收益率(%)
- `roe_dt`: 净资产收益率(扣除非经常损益)(%)
- `roe_wy`: 加权净资产收益率(%)
- `roa`: 总资产净利润率(%)
- `npta`: 总资产净利润率(杜邦分析)(%)
- `roe_yearly`: 净资产收益率(年化)(%)
- `roa2`: 总资产报酬率(%)
- `roe_avg`: 净资产收益率(平均)(%)
- `debt_to_assets`: 资产负债率(%)
- `assets_turnover`: 总资产周转率(次)
- `ca_turnover`: 流动资产周转率(次)
- `fa_turnover`: 固定资产周转率(次)
- `op_profit_growth_rate`: 营业利润增长率(%)
- `gross_profit_margin`: 销售毛利率(%)
- `ebit_interest_coverage: 息税前利润与利息费用比率
- `ebitda_to_interest: EBITDA与利息费用比率
- `ca_to_assets`: 流动资产/总资产(%)
- `ncfo_to_or: 经营现金净流量/营业收入
- `op_to_gr: 营业利润/营业总收入(%)

**示例：**
```python
df = pro.fina_indicator(ts_code='000001.SZ',
                        period='2023')
```

## 股票信息 API

### stock_basic

获取股票基础信息

**参数：**
- `ts_code`: str，股票代码
- `list_status`: str，上市状态
  - `L`: 上市
  - `D`: 退市
  - `P`: 暂停上市
- `exchange`: str，交易所
  - `SSE`: 上交所
  - `SZSE`: 深交所

**返回字段：**
- `ts_code`: 股票代码
- `symbol`: 股票代码
- `name`: 股票名称
- `area`: 所在地
- `industry`: 所属行业
- `fullname`: 股票全称
- `enname`: 英文全称
- `cnspell`: 拼音缩写
- `market`: 市场类型（主板/中小板/创业板/科创板）
- `exchange`: 交易所代码
- `curr_type`: 交易货币
- `list_status`: 上市状态
- `list_date`: 上市日期
- `delist_date`: 退市日期
- `is_hs`: 是否沪深港通标的

**示例：**
```python
df = pro.stock_basic(exchange='SSE', list_status='L')
```

### trade_cal

获取交易日历

**参数：**
- `exchange`: str，交易所
  - `SSE`: 上交所
  - `SZSE`: 深交所
- `start_date`: str，开始日期
- `end_date`: str，结束日期
- `is_open`: str，是否开市
  - `0`: 休市
  - `1`: 开市

**返回字段：**
- `exchange`: 交易所
- `cal_date`: 日历日期
- `is_open`: 是否开市
- `pretrade_date`: 上一交易日

**示例：**
```python
df = pro.trade_cal(exchange='SSE',
                   start_date='20240101',
                   end_date='20240131',
                   is_open='1')
```

### namechange

获取股票名称变更

**参数：**
- `ts_code`: str，股票代码
- `start_date`: str，开始日期
- `end_date`: str，结束日期

**返回字段：**
- `ts_code`: 股票代码
- `name`: 股票名称
- `start_date`: 开始日期
- `end_date`: 结束日期
- `change_reason`: 变更原因

**示例：**
```python
df = pro.namechange(ts_code='000001.SZ',
                    start_date='20230101',
                    end_date='20241231')
```

## 指数与宏观数据 API

### index_daily

获取指数日线行情

**参数：**
- `ts_code`: str，指数代码
- `trade_date`: str，交易日期
- `start_date`: str，开始日期
- `end_date`: str，结束日期

**返回字段：**
- `ts_code`: 指数代码
- `trade_date`: 交易日期
- `close`: 收盘点位
- `open`: 开盘点位
- `high`: 最高点位
- `low`: 最低点位
- `pre_close`: 昨收点位
- `change`: 涨跌点
- `pct_chg`: 涨跌幅 (%)
- `vol`: 成交量 (手)
- `amount`: 成交额 (千元)

**示例：**
```python
df = pro.index_daily(ts_code='000001.SH',
                     start_date='20240101',
                     end_date='20240131')
```

### index_basic

获取指数基础信息

**参数：**
- `ts_code`: str，指数代码
- `market`: str，市场
- `level`: str，级别
  - `L1`: 大类
  - `L2`: 中类
  - `L3`: 小类

**返回字段：**
- `ts_code`: 指数代码
- `name`: 指数名称
- `market`: 市场
- `publisher`: 发布方
- `index_type`: 指数类型
- `category`: 分类
- `base_date`: 基期
- `base_point`: 基点
- `list_date`: 发布日期
- `weight_rule`: 加权规则
- `desc`: 描述
- `exp_date': 终止日期

**示例：**
```python
df = pro.index_basic(market='SSE')
```

### shibor

获取 Shibor 数据

**参数：**
- `date`: str，日期
- `start_date`: str，开始日期
- `end_date`: str，结束日期

**返回字段：**
- `date`: 日期
- `on`: 隔夜利率
- `1w`: 1周利率
- `2w`: 2周利率
- `1m`: 1月利率
- `3m`: 3月利率
- `6m`: 6月利率
- `9m`: 9月利率
- `1y`: 1年利率

**示例：**
```python
df = pro.shibor(start_date='20240101',
                end_date='20240131')
```

## 错误处理

### 常见错误

| 错误类型 | 说明 | 解决方法 |
|---------|------|---------|
| 认证失败 | Token 无效或过期 | 检查 Token 是否正确 |
| 调用次数超限 | 超过每分钟调用限制 | 减少请求频率或升级账号 |
| 数据不存在 | 请求的数据不存在 | 检查参数是否正确 |
| 权限不足 | 部分数据需要付费 | 升级 Tushare 账号 |

### 错误处理示例

```python
try:
    df = pro.daily(ts_code='000001.SZ',
                   start_date='20240101',
                   end_date='20240131')
    if df is None or df.empty:
        print("无数据")
    else:
        print(df)
except Exception as e:
    print(f"错误: {e}")
```

### 调用频率限制

免费账户：每分钟最多 120 次调用

建议：
- 使用批量接口
- 合理设置日期范围
- 使用本地缓存
