
## 附录：xtdata行情数据字段与数据字典详情

### 行情数据字段列表

#### tick - 分笔数据

```
'time'                  #时间戳
'lastPrice'             #最新价
'open'                  #开盘价
'high'                  #最高价
'low'                   #最低价
'lastClose'             #前收盘价
'amount'                #成交总额
'volume'                #成交总量
'pvolume'               #原始成交总量
'stockStatus'           #证券状态
'openInt'               #持仓量
'lastSettlementPrice'   #前结算
'askPrice'              #委卖价
'bidPrice'              #委买价
'askVol'                #委卖量
'bidVol'                #委买量
'transactionNum'		#成交笔数
```

#### 1m / 5m / 1d - K线数据

```
'time'                  #时间戳
'open'                  #开盘价
'high'                  #最高价
'low'                   #最低价
'close'                 #收盘价
'volume'                #成交量
'amount'                #成交额
'settelementPrice'      #今结算
'openInterest'          #持仓量
'preClose'              #前收价
'suspendFlag'           #停牌标记 0 - 正常 1 - 停牌 -1 - 当日起复牌
```

#### 除权数据

```
'interest'        		#每股股利（税前，元）
'stockBonus'      		#每股红股（股）
'stockGift'       		#每股转增股本（股）
'allotNum'        		#每股配股数（股）
'allotPrice'      		#配股价格（元）
'gugai'           		#是否股改, 对于股改，在算复权系数时，系统有特殊算法
'dr'              		#除权系数
```

#### l2quote - level2实时行情快照

```
'time'                  #时间戳
'lastPrice'             #最新价
'open'                  #开盘价
'high'                  #最高价
'low'                   #最低价
'amount'                #成交额
'volume'                #成交总量
'pvolume'               #原始成交总量
'openInt'               #持仓量
'stockStatus'           #证券状态
'transactionNum'        #成交笔数
'lastClose'             #前收盘价
'lastSettlementPrice'   #前结算
'settlementPrice'       #今结算
'pe'                    #市盈率
'askPrice'              #多档委卖价
'bidPrice'              #多档委买价
'askVol'                #多档委卖量
'bidVol'                #多档委买量
```

#### l2order - level2逐笔委托

```
'time'                  #时间戳
'price'                 #委托价
'volume'                #委托量
'entrustNo'             #委托号
'entrustType'           #委托类型
'entrustDirection'      #委托方向
```

#### l2transaction - level2逐笔成交

```
'time'                  #时间戳
'price'                 #成交价
'volume'                #成交量
'amount'                #成交额
'tradeIndex'            #成交记录号
'buyNo'                 #买方委托号
'sellNo'                #卖方委托号
'tradeType'             #成交类型
'tradeFlag'             #成交标志
```

#### l2quoteaux - level2实时行情补充（总买总卖）

```
'time'                  #时间戳
'avgBidPrice'           #委买均价
'totalBidQuantity'      #委买总量
'avgOffPrice'           #委卖均价
'totalOffQuantity'      #委卖总量
'withdrawBidQuantity'   #买入撤单总量
'withdrawBidAmount'     #买入撤单总额
'withdrawOffQuantity'   #卖出撤单总量
'withdrawOffAmount'     #卖出撤单总额
```

#### l2orderqueue - level2委买委卖一档委托队列

```
'time'                  #时间戳
'bidLevelPrice'         #委买价
'bidLevelVolume'        #委买量
'offerLevelPrice'       #委卖价
'offerLevelVolume'      #委卖量
'bidLevelNumber'        #委买数量
'offLevelNumber'        #委卖数量
```

### 数据字典

#### 证券状态

```
0,10 - 默认为未知
11 - 开盘前S
12 - 集合竞价时段C
13 - 连续交易T
14 - 休市B
15 - 闭市E
16 - 波动性中断V
17 - 临时停牌P
18 - 收盘集合竞价U
19 - 盘中集合竞价M
20 - 暂停交易至闭市N
21 - 获取字段异常
22 - 盘后固定价格行情
23 - 盘后固定价格行情完毕
```

#### 委托类型

- level2逐笔委托 - `entrustType` 委托类型
- level2逐笔成交 - `tradeType` 成交类型

```
0 - 未知
1 - 正常交易业务
2 - 即时成交剩余撤销
3 - ETF基金申报
4 - 最优五档即时成交剩余撤销
5 - 全额成交或撤销
6 - 本方最优价格
7 - 对手方最优价格
```

#### 委托方向

- level2逐笔委托 - `entrustDirection` 委托方向
  - 注：上交所的撤单信息在逐笔委托的委托方向，区分撤买撤卖

```
1 - 买入
2 - 卖出
3 - 撤买（上交所）
4 - 撤卖（上交所）
```

#### 成交标志

- level2逐笔成交 - `tradeFlag` 成交标志
  - 注：深交所的在逐笔成交的成交标志，只有撤单，没有方向

```
0 - 未知
1 - 外盘
2 - 内盘
3 - 撤单（深交所）
```

#### 现金替代标志

- ETF申赎清单成份股现金替代标志

```
0 - 禁止现金替代（必须有股票）
1 - 允许现金替代（先用股票，股票不足的话用现金替代
2 - 必须现金替代
3 - 非沪市（股票）退补现金替代
4 - 非沪市（股票）必须现金替代
5 - 非沪深退补现金替代
6 - 非沪深必须现金替代
7 - 港市退补现金替代（仅适用于跨沪深ETF产品）
8 - 港市必须现金替代（仅适用于跨沪深港ETF产品）
```

### 财务数据字段列表

#### Balance - 资产负债表

```
'm_anntime'                                 #披露日期
'm_timetag'                                 #截止日期
'internal_shoule_recv'                      #内部应收款
'fixed_capital_clearance'                   #固定资产清理
'should_pay_money'                          #应付分保账款
'settlement_payment'                        #结算备付金
'receivable_premium'                        #应收保费
'accounts_receivable_reinsurance'           #应收分保账款
'reinsurance_contract_reserve'              #应收分保合同准备金
'dividends_payable'                         #应收股利
'tax_rebate_for_export'                     #应收出口退税
'subsidies_receivable'                      #应收补贴款
'deposit_receivable'                        #应收保证金
'apportioned_cost'                          #待摊费用
'profit_and_current_assets_with_deal'       #待处理流动资产损益
'current_assets_one_year'                   #一年内到期的非流动资产
'long_term_receivables'                     #长期应收款
'other_long_term_investments'               #其他长期投资
'original_value_of_fixed_assets'            #固定资产原值
'net_value_of_fixed_assets'                 #固定资产净值
'depreciation_reserves_of_fixed_assets'     #固定资产减值准备
'productive_biological_assets'              #生产性生物资产
'public_welfare_biological_assets'          #公益性生物资产
'oil_and_gas_assets'                        #油气资产
'development_expenditure'                   #开发支出
'right_of_split_share_distribution'         #股权分置流通权
'other_non_mobile_assets'                   #其他非流动资产
'handling_fee_and_commission'               #应付手续费及佣金
'other_payables'                            #其他应交款
'margin_payable'                            #应付保证金
'internal_accounts_payable'                 #内部应付款
'advance_cost'                              #预提费用
'insurance_contract_reserve'                #保险合同准备金
'broker_buying_and_selling_securities'      #代理买卖证券款
'acting_underwriting_securities'            #代理承销证券款
'international_ticket_settlement'           #国际票证结算
'domestic_ticket_settlement'                #国内票证结算
'deferred_income'                           #递延收益
'short_term_bonds_payable'                  #应付短期债券
'long_term_deferred_income'                 #长期递延收益
'undetermined_investment_losses'            #未确定的投资损失
'quasi_distribution_of_cash_dividends'      #拟分配现金股利
'provisions_not'                            #预计负债
'cust_bank_dep'                             #吸收存款及同业存放
'provisions'                                #预计流动负债
'less_tsy_stk'                              #减:库存股
'cash_equivalents'                          #货币资金
'loans_to_oth_banks'                        #拆出资金
'tradable_fin_assets'                       #交易性金融资产
'derivative_fin_assets'                     #衍生金融资产
'bill_receivable'                           #应收票据
'account_receivable'                        #应收账款
'advance_payment'                           #预付款项
'int_rcv'                                   #应收利息
'other_receivable'                          #其他应收款
'red_monetary_cap_for_sale'                 #买入返售金融资产
'agency_bus_assets'                         #以公允价值计量且其变动计入当期损益的金融资产
'inventories'                               #存货
'other_current_assets'                      #其他流动资产
'total_current_assets'                      #流动资产合计
'loans_and_adv_granted'                     #发放贷款及垫款
'fin_assets_avail_for_sale'                 #可供出售金融资产
'held_to_mty_invest'                        #持有至到期投资
'long_term_eqy_invest'                      #长期股权投资
'invest_real_estate'                        #投资性房地产
'accumulated_depreciation'                  #累计折旧
'fix_assets'                                #固定资产
'constru_in_process'                        #在建工程
'construction_materials'                    #工程物资
'long_term_liabilities'                     #长期负债
'intang_assets'                             #无形资产
'goodwill'                                  #商誉
'long_deferred_expense'                     #长期待摊费用
'deferred_tax_assets'                       #递延所得税资产
'total_non_current_assets'                  #非流动资产合计
'tot_assets'                                #资产总计
'shortterm_loan'                            #短期借款
'borrow_central_bank'                       #向中央银行借款
'loans_oth_banks'                           #拆入资金
'tradable_fin_liab'                         #交易性金融负债
'derivative_fin_liab'                       #衍生金融负债
'notes_payable'                             #应付票据
'accounts_payable'                          #应付账款
'advance_peceipts'                          #预收账款
'fund_sales_fin_assets_rp'                  #卖出回购金融资产款
'empl_ben_payable'                          #应付职工薪酬
'taxes_surcharges_payable'                  #应交税费
'int_payable'                               #应付利息
'dividend_payable'                          #应付股利
'other_payable'                             #其他应付款
'non_current_liability_in_one_year'         #一年内到期的非流动负债
'other_current_liability'                   #其他流动负债
'total_current_liability'                   #流动负债合计
'long_term_loans'                           #长期借款
'bonds_payable'                             #应付债券
'longterm_account_payable'                  #长期应付款
'grants_received'                           #专项应付款
'deferred_tax_liab'                         #递延所得税负债
'other_non_current_liabilities'             #其他非流动负债
'non_current_liabilities'                   #非流动负债合计
'tot_liab'                                  #负债合计
'cap_stk'                                   #实收资本(或股本)
'cap_rsrv'                                  #资本公积
'specific_reserves'                         #专项储备
'surplus_rsrv'                              #盈余公积
'prov_nom_risks'                            #一般风险准备
'undistributed_profit'                      #未分配利润
'cnvd_diff_foreign_curr_stat'               #外币报表折算差额
'tot_shrhldr_eqy_excl_min_int'              #归属于母公司股东权益合计
'minority_int'                              #少数股东权益
'total_equity'                              #所有者权益合计
'tot_liab_shrhldr_eqy'                      #负债和股东权益总计
```

#### Income - 利润表

```
'm_anntime'                                 #披露日期
'm_timetag'                                 #截止日期
'revenue_inc'                               #营业收入
'earned_premium'                            #已赚保费
'real_estate_sales_income'                  #房地产销售收入
'total_operating_cost'                      #营业总成本
'real_estate_sales_cost'                    #房地产销售成本
'research_expenses'                         #研发费用
'surrender_value'                           #退保金
'net_payments'                              #赔付支出净额
'net_withdrawal_ins_con_res'                #提取保险合同准备金净额
'policy_dividend_expenses'                  #保单红利支出
'reinsurance_cost'                          #分保费用
'change_income_fair_value'                  #公允价值变动收益
'futures_loss'                              #期货损益
'trust_income'                              #托管收益
'subsidize_revenue'                         #补贴收入
'other_business_profits'                    #其他业务利润
'net_profit_excl_merged_int_inc'            #被合并方在合并前实现净利润
'int_inc'                                   #利息收入
'handling_chrg_comm_inc'                    #手续费及佣金收入
'less_handling_chrg_comm_exp'               #手续费及佣金支出
'other_bus_cost'                            #其他业务成本
'plus_net_gain_fx_trans'                    #汇兑收益
'il_net_loss_disp_noncur_asset'             #非流动资产处置收益
'inc_tax'                                   #所得税费用
'unconfirmed_invest_loss'                   #未确认投资损失
'net_profit_excl_min_int_inc'               #归属于母公司所有者的净利润
'less_int_exp'                              #利息支出
'other_bus_inc'                             #其他业务收入
'revenue'                                   #营业总收入
'total_expense'                             #营业成本
'less_taxes_surcharges_ops'                 #营业税金及附加
'sale_expense'                              #销售费用
'less_gerl_admin_exp'                       #管理费用
'financial_expense'                         #财务费用
'less_impair_loss_assets'                   #资产减值损失
'plus_net_invest_inc'                       #投资收益
'incl_inc_invest_assoc_jv_entp'             #联营企业和合营企业的投资收益
'oper_profit'                               #营业利润
'plus_non_oper_rev'                         #营业外收入
'less_non_oper_exp'                         #营业外支出
'tot_profit'                                #利润总额
'net_profit_incl_min_int_inc'               #净利润
'net_profit_incl_min_int_inc_after'         #净利润(扣除非经常性损益后)
'minority_int_inc'                          #少数股东损益
's_fa_eps_basic'                            #基本每股收益
's_fa_eps_diluted'                          #稀释每股收益
'total_income'                              #综合收益总额
'total_income_minority'                     #归属于少数股东的综合收益总额
'other_compreh_inc'                         #其他收益
```

#### CashFlow - 现金流量表

```
'm_anntime'                                 #披露日期
'm_timetag'                                 #截止日期
'cash_received_ori_ins_contract_pre'        #收到原保险合同保费取得的现金
'net_cash_received_rei_ope'                 #收到再保险业务现金净额
'net_increase_insured_funds'                #保户储金及投资款净增加额
'Net'                                       #处置交易性金融资产净增加额 increase_in_disposal
'cash_for_interest'                         #收取利息、手续费及佣金的现金
'net_increase_in_repurchase_funds'          #回购业务资金净增加额
'cash_for_payment_original_insurance'       #支付原保险合同赔付款项的现金
'cash_payment_policy_dividends'             #支付保单红利的现金
'disposal_other_business_units'             #处置子公司及其他收到的现金
'cash_received_from_pledges'                #减少质押和定期存款所收到的现金
'cash_paid_for_investments'                 #投资所支付的现金
'net_increase_in_pledged_loans'             #质押贷款净增加额
'cash_paid_by_subsidiaries'                 #取得子公司及其他营业单位支付的现金净额
'increase_in_cash_paid'                     #增加质押和定期存款所支付的现金
'cass_received_sub_abs'                     #其中子公司吸收现金
'cass_received_sub_investments'             #其中:子公司支付给少数股东的股利、利润
'minority_shareholder_profit_loss'          #少数股东损益
'unrecognized_investment_losses'            #未确认的投资损失
'ncrease_deferred_income'                   #递延收益增加(减:减少)
'projected_liability'                       #预计负债
'increase_operational_payables'             #经营性应付项目的增加
'reduction_outstanding_amounts_less'        #已完工尚未结算款的减少(减:增加)
'reduction_outstanding_amounts_more'        #已结算尚未完工款的增加(减:减少)
'goods_sale_and_service_render_cash'        #销售商品、提供劳务收到的现金
'net_incr_dep_cob'                          #客户存款和同业存放款项净增加额
'net_incr_loans_central_bank'               #向中央银行借款净增加额(万元
'net_incr_fund_borr_ofi'                    #向其他金融机构拆入资金净增加额
'net_incr_fund_borr_ofi'                    #拆入资金净增加额
'tax_levy_refund'                           #收到的税费与返还
'cash_paid_invest'                          #投资支付的现金
'other_cash_recp_ral_oper_act'              #收到的其他与经营活动有关的现金
'stot_cash_inflows_oper_act'                #经营活动现金流入小计
'goods_and_services_cash_paid'              #购买商品、接受劳务支付的现金
'net_incr_clients_loan_adv'                 #客户贷款及垫款净增加额
'net_incr_dep_cbob'                         #存放中央银行和同业款项净增加额
'handling_chrg_paid'                        #支付利息、手续费及佣金的现金
'cash_pay_beh_empl'                         #支付给职工以及为职工支付的现金
'pay_all_typ_tax'                           #支付的各项税费
'other_cash_pay_ral_oper_act'               #支付其他与经营活动有关的现金
'stot_cash_outflows_oper_act'               #经营活动现金流出小计
'net_cash_flows_oper_act'                   #经营活动产生的现金流量净额
'cash_recp_disp_withdrwl_invest'            #收回投资所收到的现金
'cash_recp_return_invest'                   #取得投资收益所收到的现金
'net_cash_recp_disp_fiolta'                 #处置固定资产、无形资产和其他长期投资收到的现金
'other_cash_recp_ral_inv_act'               #收到的其他与投资活动有关的现金
'stot_cash_inflows_inv_act'                 #投资活动现金流入小计
'cash_pay_acq_const_fiolta'                 #购建固定资产、无形资产和其他长期投资支付的现金
'other_cash_pay_ral_oper_act'               #支付其他与投资的现金
'stot_cash_outflows_inv_act'                #投资活动现金流出小计
'net_cash_flows_inv_act'                    #投资活动产生的现金流量净额
'cash_recp_cap_contrib'                     #吸收投资收到的现金
'cash_recp_borrow'                          #取得借款收到的现金
'proc_issue_bonds'                          #发行债券收到的现金
'other_cash_recp_ral_fnc_act'               #收到其他与筹资活动有关的现金
'stot_cash_inflows_fnc_act'                 #筹资活动现金流入小计
'cash_prepay_amt_borr'                      #偿还债务支付现金
'cash_pay_dist_dpcp_int_exp'                #分配股利、利润或偿付利息支付的现金
'other_cash_pay_ral_fnc_act'                #支付其他与筹资的现金
'stot_cash_outflows_fnc_act'                #筹资活动现金流出小计
'net_cash_flows_fnc_act'                    #筹资活动产生的现金流量净额
'eff_fx_flu_cash'                           #汇率变动对现金的影响
'net_incr_cash_cash_equ'                    #现金及现金等价物净增加额
'cash_cash_equ_beg_period'                  #期初现金及现金等价物余额
'cash_cash_equ_end_period'                  #期末现金及现金等价物余额
'net_profit'                                #净利润
'plus_prov_depr_assets'                     #资产减值准备
'depr_fa_coga_dpba'                         #固定资产折旧、油气资产折耗、生产性物资折旧
'amort_intang_assets'                       #无形资产摊销
'amort_lt_deferred_exp'                     #长期待摊费用摊销
'decr_deferred_exp'                         #待摊费用的减少
'incr_acc_exp'                              #预提费用的增加
'loss_disp_fiolta'                          #处置固定资产、无形资产和其他长期资产的损失
'loss_scr_fa'                               #固定资产报废损失
'loss_fv_chg'                               #公允价值变动损失
'fin_exp'                                   #财务费用
'invest_loss'                               #投资损失
'decr_deferred_inc_tax_assets'              #递延所得税资产减少
'incr_deferred_inc_tax_liab'                #递延所得税负债增加
'decr_inventories'                          #存货的减少
'decr_oper_payable'                         #经营性应收项目的减少
'others'                                    #其他
'im_net_cash_flows_oper_act'                #经营活动产生现金流量净额
'conv_debt_into_cap'                        #债务转为资本
'conv_corp_bonds_due_within_1y'             #一年内到期的可转换公司债券
'fa_fnc_leases'                             #融资租入固定资产
'end_bal_cash'                              #现金的期末余额
'less_beg_bal_cash'                         #现金的期初余额
'plus_end_bal_cash_equ'                     #现金等价物的期末余额
'less_beg_bal_cash_equ'                     #现金等价物的期初余额
'im_net_incr_cash_cash_equ'                 #现金及现金等价物的净增加额
'tax_levy_refund'                           #收到的税费返还
```

#### PershareIndex - 主要指标

```
's_fa_ocfps'                                #每股经营活动现金流量
's_fa_bps'                                  #每股净资产
's_fa_eps_basic'                            #基本每股收益
's_fa_eps_diluted'                          #稀释每股收益
's_fa_undistributedps'                      #每股未分配利润
's_fa_surpluscapitalps'                     #每股资本公积金
'adjusted_earnings_per_share'               #扣非每股收益
'du_return_on_equity'                       #净资产收益率
'sales_gross_profit'                        #销售毛利率
'inc_revenue_rate'                          #主营收入同比增长
'du_profit_rate'                            #净利润同比增长
'inc_net_profit_rate'                       #归属于母公司所有者的净利润同比增长
'adjusted_net_profit_rate'                  #扣非净利润同比增长
'inc_total_revenue_annual'                  #营业总收入滚动环比增长
'inc_net_profit_to_shareholders_annual'     #归属净利润滚动环比增长
'adjusted_profit_to_profit_annual'          #扣非净利润滚动环比增长
'equity_roe'                                #加权净资产收益率
'net_roe'                                   #摊薄净资产收益率
'total_roe'                                 #摊薄总资产收益率
'gross_profit'                              #毛利率
'net_profit'                                #净利率
'actual_tax_rate'                           #实际税率
'pre_pay_operate_income'                    #预收款 / 营业收入
'sales_cash_flow'                           #销售现金流 / 营业收入
'gear_ratio'                                #资产负债比率
'inventory_turnover'                        #存货周转率
'm_anntime'                                 #公告日
'm_timetag'                                 #报告截止日
```

#### Capital - 股本表

```
'total_capital'                             #总股本
'circulating_capital'                       #已上市流通A股
'restrict_circulating_capital'              #限售流通股份
'm_timetag'                                 #报告截止日
'm_anntime'                                 #公告日
```

#### Top10holder/Top10flowholder - 十大股东/十大流通股东

```
'declareDate'                                #公告日期
'endDate'                                    #截止日期
'name'                                       #股东名称
'type'                                       #股东类型
'quantity'                                   #持股数量
'reason'                                     #变动原因
'ratio'                                      #持股比例
'nature'                                     #股份性质
'rank'                                       #持股排名
```

#### Holdernum - 股东数

```
'declareDate'                                 #公告日期
'endDate'                                     #截止日期
'shareholder'                                 #股东总数
'shareholderA'                                #A股东户数
'shareholderB'                                #B股东户数
'shareholderH'                                #H股东户数
'shareholderFloat'                            #已流通股东户数
'shareholderOther'                            #未流通股东户数
```

### 合约信息字段列表

```
'ExchangeID' 				#合约市场代码
'InstrumentID' 				#合约代码
'InstrumentName' 			#合约名称
'Abbreviation' 				#合约名称的拼音简写
'ProductID' 				#合约的品种ID（期货）
'ProductName' 				#合约的品种名称（期货）
'UnderlyingCode' 			#标的合约
'ExtendName' 				#扩位名称
'ExchangeCode' 				#交易所代码
'RzrkCode' 					#rzrk代码
'UniCode' 					#统一规则代码
'CreateDate' 				#上市日期（期货）
'OpenDate' 					#IPO日期（股票）
'ExpireDate' 				#退市日或者到期日
'PreClose' 					#前收盘价格
'SettlementPrice' 			#前结算价格
'UpStopPrice' 				#当日涨停价
'DownStopPrice' 			#当日跌停价
'FloatVolume' 				#流通股本
'TotalVolume' 				#总股本
'AccumulatedInterest' 		#自上市付息日起的累积未付利息额（债券）
'LongMarginRatio' 			#多头保证金率
'ShortMarginRatio' 			#空头保证金率
'PriceTick' 				#最小变价单位
'VolumeMultiple' 			#合约乘数（对期货以外的品种，默认是1）
'MainContract' 				#主力合约标记，1、2、3分别表示第一主力合约，第二主力合约，第三主力合约
'MaxMarketOrderVolume' 		#市价单最大下单量
'MinMarketOrderVolume' 		#市价单最小下单量
'MaxLimitOrderVolume' 		#限价单最大下单量
'MinLimitOrderVolume' 		#限价单最小下单量
'MaxMarginSideAlgorithm' 	#上期所大单边的处理算法
'DayCountFromIPO' 			#自IPO起经历的交易日总数
'LastVolume' 				#昨日持仓量
'InstrumentStatus' 			#合约停牌状态
'IsTrading' 				#合约是否可交易
'IsRecent' 					#是否是近月合约
'IsContinuous' 				#是否是连续合约
'bNotProfitable' 			#是否非盈利状态
'bDualClass' 				#是否同股不同权
'ContinueType' 				#连续合约类型
'secuCategory' 				#证券分类
'secuAttri' 				#证券属性
'MaxMarketSellOrderVolume' 	#市价卖单最大单笔下单量
'MinMarketSellOrderVolume' 	#市价卖单最小单笔下单量
'MaxLimitSellOrderVolume' 	#限价卖单最大单笔下单量
'MinLimitSellOrderVolume' 	#限价卖单最小单笔下单量
'MaxFixedBuyOrderVol' 		#盘后定价委托数量的上限（买）
'MinFixedBuyOrderVol' 		#盘后定价委托数量的下限（买）
'MaxFixedSellOrderVol' 		#盘后定价委托数量的上限（卖）
'MinFixedSellOrderVol' 		#盘后定价委托数量的下限（卖）
'HSGTFlag' 					#标识港股是否为沪港通或深港通标的证券。沪港通:0-非标的，1-标的，2-历史标的；深港通:0-非标的，3-标的，4-历史标的，5-是沪港通也是深港通
'BondParValue' 				#债券面值
'QualifiedType' 			#投资者适当性管理分类
'PriceTickType' 			#价差类别（港股用），1-股票，3-债券，4-期权，5-交易所买卖基金
'tradingStatus' 			#交易状态
'OptUnit' 					#期权合约单位
'MarginUnit' 				#期权单位保证金
'OptUndlCode' 				#期权标的证券代码或可转债正股标的证券代码
'OptUndlMarket' 			#期权标的证券市场或可转债正股标的证券市场
'OptLotSize' 				#期权整手数
'OptExercisePrice' 			#期权行权价或可转债转股价
'NeeqExeType' 				#全国股转转让类型，1-协议转让方式，2-做市转让方式，3-集合竞价+连续竞价转让方式（当前全国股转并未实现），4-集合竞价转让
'OptExchFixedMargin' 		#交易所期权合约保证金不变部分
'OptExchMiniMargin' 		#交易所期权合约最小保证金
'Ccy' 						#币种
'IbSecType' 				#IB安全类型，期货或股票
'OptUndlRiskFreeRate' 		#期权标的无风险利率
'OptUndlHistoryRate' 		#期权标的历史波动率
'EndDelivDate' 				#期权行权终止日
'RegisteredCapital' 		#注册资本（单位:百万）
'MaxOrderPriceRange' 		#最大有效申报范围
'MinOrderPriceRange' 		#最小有效申报范围
'VoteRightRatio' 			#同股同权比例
'm_nMinRepurchaseDaysLimit' #最小回购天数
'm_nMaxRepurchaseDaysLimit' #最大回购天数
'DeliveryYear' 				#交割年份
'DeliveryMonth' 			#交割月
'ContractType' 				#标识期权，1-过期，2-当月，3-下月，4-下季，5-隔季，6-隔下季
'ProductTradeQuota' 		#期货品种交易配额
'ContractTradeQuota' 		#期货合约交易配额
'ProductOpenInterestQuota' 	#期货品种持仓配额
'ContractOpenInterestQuota' #期货合约持仓配额
'ChargeType' 				#期货和期权手续费方式，0-未知，1-按元/手，2-按费率
'ChargeOpen' 				#开仓手续费率，-1表示没有
'ChargeClose' 				#平仓手续费率，-1表示没有
'ChargeClose'				#平仓手续费率，-1表示没有
'ChargeTodayOpen'			#开今仓（日内开仓）手续费率，-1表示没有
'ChargeTodayClose'			#平今仓（日内平仓）手续费率，-1表示没有
'OptionType'				#期权类型，-1为非期权，0为期权认购，1为期权认沽
'OpenInterestMultiple'		#交割月持仓倍数
```

### 代码示例

#### 时间戳转换

```py
import time
def conv_time(ct):
    '''
    conv_time(1476374400000) --> '20161014000000.000'
    '''
    local_time = time.localtime(ct / 1000)
    data_head = time.strftime('%Y%m%d%H%M%S', local_time)
    data_secs = (ct - int(ct)) * 1000
    time_stamp = '%s.%03d' % (data_head, data_secs)
    return time_stamp
```
