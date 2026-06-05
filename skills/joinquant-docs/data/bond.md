## 债券数据

[Query的简单教程](https://www.joinquant.com/view/community/detail/433d0e9ed9fed11fc9f7772eab8d9376)

### 使用说明

```python
from jqdata import bond
df=bond.run_query(query(bond.BOND_BASIC_INFO).filter(bond.BOND_BASIC_INFO.code == '131801').limit(n))
```

获取债券基本信息数据、债券票面利率数据和国债逆回购日行情数据

**参数：**

- **query(bond.BOND_BASIC_INFO)**：表示从bond.BOND_BASIC_INFO 这张表中查询债券基本信息数据，其中bond是库名，BOND_BASIC_INFO是表名。bond库中的表都可以使用run_query方法调用，表名如下所示：
    
    | **表名** | **描述** |
    | --- | --- |
    | BOND_BASIC_INFO | 债券基本信息数据 |
    | BOND_COUPON | 债券票面利率数据 |
    | REPO_DAILY_PRICE | 国债逆回购日行情数据 |
    | CONBOND_BASIC_INFO | 可转债基本资料 |
    | CONBOND_CONVERT_PRICE_ADJUST | 可转债转股价格调整 |
    | CONBOND_DAILY_PRICE | 可转债日行情 |
    | CONBOND_DAILY_CONVERT | 可转债每日转股统计 |
    | BOND_INTEREST_PAYMENT | 债券付息事件 |
    
    在查询表数据时还可以指定所要查询的字段名，格式如下：query(库名.表名.字段名1，库名.表名.字段名2，多个字段用逗号分隔进行提取；query函数的更多用法详见： **[query简易教程](https://www.joinquant.com/view/community/detail/16411)**
    
- **filter(bond.BOND_BASIC_INFO.code == '131801')**：指定筛选条件，通过bond.BOND_BASIC_INFO.code == '131801' 可以指定债券代码来获取债券基本信息数据；除此之外，还可以对表中其他字段指定筛选条件，如filter(bond.BOND_BASIC_INFO.exchange=='上交所')，表示交易市场在上交所的所有债券基本信息数据；多个筛选条件用英文逗号分隔。
    
- **limit(n)**：限制返回的数据条数，n指定返回条数。
    

**返回结果：**

- 返回一个 dataframe，每一行对应数据表中的一条数据， 列索引是您所查询的字段名称

**注意：**

1.  **为了防止返回数据量过大, 我们每次最多返回5000行**
2.  不能进行连表查询，即同时查询多张表的数据

**示例：**

```python
# 查询交易市场为上交所的债券基本信息数据
from jqdata import bond

df = bond.run_query(query(bond.BOND_BASIC_INFO).filter(bond.BOND_BASIC_INFO.exchange == '上交所').limit(10))
print(df)
```

```python
   id    code short_name                            full_name  list_status_id  \
0   2  131800      16东莞次  中国中投证券-东莞证券融出资金债权1号资产支持专项计划次级资产支持证券             NaN
1   3  131801     花呗01A1         德邦花呗第一期消费贷款资产支持专项计划优先级资产支持证券        301006.0
2   4  131802     花呗01A2        德邦花呗第一期消费贷款资产支持专项计划次优先级资产支持证券        301006.0
3   5  131803      花呗01B          德邦花呗第一期消费贷款资产支持专项计划次级资产支持证券        301006.0
4   6  131805       海尔优B             海尔保理一期资产支持专项计划优先B级资产支持证券        301006.0
5   7  131806       海尔优C             海尔保理一期资产支持专项计划优先C级资产支持证券        301006.0
6  11  204001      GC001                           1天新质押式国债回购             NaN
7  12  204002      GC002                           2天新质押式国债回购             NaN
8  13  204003      GC003                           3天新质押式国债回购             NaN
9  14  204004      GG004                           4天新质押式国债回购             NaN

  list_status           issuer company_code  exchange_code exchange  \
0        None       东莞证券股份有限公司         None         705001      上交所
1        终止上市  重庆市阿里小微小额贷款有限公司         None         705001      上交所
2        终止上市  重庆市阿里小微小额贷款有限公司         None         705001      上交所
3        终止上市  重庆市阿里小微小额贷款有限公司         None         705001      上交所
4        终止上市   海尔金融保理(重庆)有限公司         None         705001      上交所
5        终止上市   海尔金融保理(重庆)有限公司         None         705001      上交所
6        None             None         None         705001      上交所
7        None             None         None         705001      上交所
8        None             None         None         705001      上交所
9        None             None         None         705001      上交所

      ...      bond_type  bond_form_id bond_form   list_date  delist_Date  \
0     ...         资产支持证券        704001       记账式  2016-07-25   2019-06-18
1     ...         资产支持证券        704001       记账式  2016-07-12   2017-06-13
2     ...         资产支持证券        704001       记账式  2016-07-12   2017-06-13
3     ...         资产支持证券        704001       记账式  2016-07-12   2017-06-13
4     ...         资产支持证券        704001       记账式  2016-07-07   2016-12-02
5     ...         资产支持证券        704001       记账式  2016-07-07   2017-03-09
6     ...          质押式回购        704001       记账式        None         None
7     ...          质押式回购        704001       记账式        None         None
8     ...          质押式回购        704001       记账式        None         None
9     ...          质押式回购        704001       记账式        None         None

  interest_begin_date  maturity_date  interest_date  last_cash_date  \
0          2016-06-17     2019-06-18           None      2019-06-18
1          2016-06-07     2017-06-15           None      2017-06-15
2          2016-06-07     2017-06-15           None      2017-06-15
3          2016-06-07     2017-06-15           None      2017-06-15
4          2016-06-08     2016-12-06           None      2016-12-06
5          2016-06-08     2017-03-13           None      2017-03-13
6                None           None           None            None
7                None           None           None            None
8                None           None           None            None
9                None           None           None            None

  cash_comment
0         None
1         None
2         None
3         None
4         None
5         None
6         None
7         None
8         None
9         None
```

### 数据字典

#### 债券基本信息（BOND_BASIC_INFO）

**表结构：**

| 名称 | 类型 | 描述 |
| --- | --- | --- |
| code | str | 债券代码(不加后缀） |
| short_name | str | 债券简称 |
| full_name | str | 债券全称 |
| list_status_id | int | 上市状态编码，见下表上市状态编码对照表 |
| list_status | str | 上市状态 |
| issuer | str | 发行人 |
| company_code | str | 发行人股票代码 |
| exchange_code | int | 交易市场编码，见下表交易市场编码 |
| exchange | str | 交易市场 |
| currency_id | str | 货币代码。CNY-人民币 |
| coupon_type_id | int | 计息方式编码，见下表计息方式编码 |
| coupon_type | str | 计息方式 |
| coupon_frequency | int | 付息频率，单位：月/次。按年付息是12月/次；半年付息是6月/次 |
| payment_type_id | int | 兑付方式编码，见下表兑付方式编码表 |
| payment_type | str | 兑付方式 |
| par | float | 债券面值(元) |
| repayment_period | int | 偿还期限(月） |
| bond_type_id | int | 债券分类编码。 |
| bond_type | str | 债券分类 |
| bond_form_id | int | 债券形式编码，见下表债券形式编码表 |
| bond_form | str | 债券形式 |
| list_date | date | 上市日期 |
| delist_Date | date | 退市日期 |
| interest_begin_date | date | 起息日 |
| maturity_date | date | 到期日 |
| interest_date | str | 付息日 |
| last_cash_date | date | 最终兑付日 |
| cash_comment | str | 兑付说明 |

**编码对照表:**

| 上市状态编码 | 上市状态 |
| --- | --- |
| 301001 | 正常上市 |
| 301006 | 终止上市 |
| 301007 | 已发行未上市 |
| 301099 | 其他（数据源未披露等） |

| **交易市场编码** | **交易市场** |
| --- | --- |
| 705001 | 上交所 |
| 705002 | 深交所主板 |
| 705007 | 银行间债券市场 |
| 705008 | 商业银行柜台市场 |
| 705099 | 其他 |

| 计息方式编码 | 计息方式 |
| --- | --- |
| 701001 | 利随本清 |
| 701002 | 固定利率附息 |
| 701003 | 递进利率 |
| 701004 | 浮动利率 |
| 701005 | 贴现 |
| 701006 | 未公布 |
| 701007 | 无利率 |
| 701008 | 累进利率 |

| 兑付方式编码 | 兑付方式 |
| --- | --- |
| 702001 | 到期一次付息 |
| 702002 | 按年付息 |
| 702003 | 按半年付息 |
| 702004 | 按季付息 |
| 702005 | 按月付息 |
| 702006 | 未公布 |
| 702099 | 其他 |

| 债券分类编码 | 债券分类 |
| --- | --- |
| 703001 | 短期融资券 |
| 703002 | 质押式回购 |
| 703003 | 私募债 |
| 703004 | 企业债 |
| 703005 | 次级债 |
| 703006 | 一般金融债 |
| 703007 | 中期票据 |
| 703008 | 资产支持证券 |
| 703009 | 小微企业扶持债 |
| 703010 | 地方政府债 |
| 703011 | 公司债 |
| 703012 | 可交换私募债 |
| 703013 | 可转债 |
| 703014 | 集合债券 |
| 703015 | 国际机构债券 |
| 703016 | 政府支持机构债券 |
| 703017 | 集合票据 |
| 703018 | 外国主权政府人民币债券 |
| 703019 | 央行票据 |
| 703020 | 政策性金融债 |
| 703021 | 国债 |
| 703022 | 非银行金融债 |
| 703023 | 可分离可转债 |
| 703024 | 国库定期存款 |
| 703025 | 可交换债 |
| 703026 | 特种金融债 |

| 债券形式编码 | 债券形式 |
| --- | --- |
| 704001 | 记账式 |
| 704002 | 实物式 |
| 704003 | 储蓄电子式 |
| 704004 | 凭证式 |
| 704005 | 未公布 |

#### 债券票面利率（BOND_COUPON）

**表结构：**

| 名称 | 类型 | 描述 |
| --- | --- | --- |
| code | str | 债券代码（不加后缀） |
| short_name | str | 债券简称 |
| exchange_code | int | 证券市场编码(新增字段) |
| exchange | str | 证券市场(新增字段) |
| pub_date | date | 信息发布日期 |
| coupon_type_id | int | 计息方式编码，见下表计息方式编码 |
| coupon_type | str | 计息方式 |
| coupon | float(5) | 票面年利率(%) |
| coupon_start_date | date | 票面利率起始适用日期 |
| coupon_end_date | date | 票面利率终止适用日期 |
| reference_rate | float | 浮息债参考利率(%) |
| reference_rate_comment | str | 浮息债参考利率说明 |
| margin_rate | float | 浮息债利差(%)-(等于票面利率减参考利率） |
| coupon_upper_limit | float | 利率上限 |
| coupon_lower_limit | float | 利率下限 |

**编码对照表：**

| 计息方式编码 | 计息方式 |
| --- | --- |
| 701001 | 利随本清 |
| 701002 | 固定利率附息 |
| 701003 | 递进利率 |
| 701004 | 浮动利率 |
| 701005 | 贴现 |
| 701006 | 未公布 |
| 701007 | 无利率 |

#### 国债逆回购日行情（REPO_DAILY_PRICE）

**数据字典：**

| 名称 | 类型 | 描述 |
| --- | --- | --- |
| date | date | 交易日期 |
| code | varchar(12) | 回购代码，如 '204001.XSHG' |
| name | varchar(20) | 回购简称，如 'GC001' |
| exchange_code | varchar(12) | 证券市场编码。XSHG-上海证券交易所；XSHE-深圳证券交易所 |
| pre_close | decimal(10,4) | 前收盘利率(%) |
| open | decimal(10,4) | 开盘利率(%) |
| high | decimal(10,4) | 最高利率(%) |
| low | decimal(10,4) | 最低利率(%) |
| close | decimal(10,4) | 收盘利率(%) |
| volume | bigint | 成交量（手） |
| money | decimal（20,2） | 成交额（元） |
| deal_number | int | 成交笔数（笔） |

#### 可转债基本资料（CONBOND_BASIC_INFO）

**表结构：**

| 名称 | 类型 | 描述 |
| --- | --- | --- |
| code | str | 债券代码 |
| short_name | str | 债券简称 |
| short_name_spelling | str | 债券简称拼音 |
| full_name | str | 债券全称 |
| list_status_id | int | 上市状态编码，见下表上市状态编码对照表 |
| list_status | str | 上市状态 |
| issuer | str | 发行人 |
| company_code | str | 发行人股票代码（带后缀） |
| issue_start_date | date | 发行起始日 |
| issue_end_date | date | 发行终止日 |
| plan_raise_fund | decimal(20,4) | 计划发行总量（万元） |
| actual_raise_fund | decimal(20,4) | 实际发行总量（万元） |
| issue_par | int | 发行面值 |
| issue_price | decimal(10,3) | 发行价格 |
| is_guarantee | int | 是否有担保(1-是，0-否） |
| fund_raising_purposes | varchar(200) | 募资用途说明 |
| list_date list_declare_date | date | 上市公告日期 |
| convert_price_reason | varchar(300) | 初始转股价确定方式 |
| convert_price | decimal(10,3) | 初始转股价格 |
| convert_start_date | start_date | 转股开始日期 |
| convert_end_date | end_date | 转股终止日期 |
| convert_code | varchar(10) | 转股代码（不带后缀） |
| coupon | decimal(10,3) | 初始票面利率 |
| exchange_code | int | 交易市场编码，见下表交易市场编码 |
| exchange | str | 交易市场 |
| currency_id | str | 货币代码。CNY-人民币 |
| coupon_type_id | int | 计息方式编码，见下表计息方式编码 |
| coupon_type | str | 计息方式 |
| coupon_frequency | int | 付息频率，单位：月/次。按年付息是12月/次；半年付息是6月/次 |
| payment_type_id | int | 兑付方式编码，见下表兑付方式编码表 |
| payment_type | str | 兑付方式 |
| par | float | 债券面值(元) |
| repayment_period | int | 偿还期限(月） |
| bond_type_id | int | 债券分类编码，见下表债券分类编码 |
| bond_type | str | 债券分类 |
| bond_form_id | int | 债券形式编码，见下表债券形式编码表 |
| bond_form | str | 债券形式 |
| list_date | date | 上市日期 |
| delist_Date | date | 退市日期 |
| interest_begin_date | date | 起息日 |
| maturity_date | date | 到期日 |
| interest_date | str | 付息日 |
| last_cash_date | date | 最终兑付日 |
| cash_comment | str | 兑付说明 |

**编码对照表：**

| 上市状态编码 | 上市状态 |
| --- | --- |
| 301001 | 正常上市 |
| 301006 | 终止上市 |
| 301099 | 其他 |

| **交易市场编码** | **交易市场** |
| --- | --- |
| 705001 | 上交所 |
| 705002 | 深交所主板 |
| 705003 | 深交所中小板 |
| 705004 | 深交所创业板 |
| 705005 | 上交所综合业务平台 |
| 705006 | 深交所综合协议交易平台 |
| 705007 | 银行间债券市场 |
| 705008 | 商业银行柜台市场 |
| 705009 | 港交所创业板 |
| 705010 | 新加坡证券交易所 |
| 705011 | 拟上市 |
| 705012 | 产权交易市场 |
| 705013 | 美国NASDAQ证券交易所 |
| 705014 | 港交所主板 |
| 705015 | 股份报价系统 |
| 705016 | 代办转让 |
| 705017 | 上交所CDR |
| 705018 | 深交所存托凭证 |
| 705099 | 其他 |

| 计息方式编码 | 计息方式 |
| --- | --- |
| 701001 | 利随本清 |
| 701002 | 固定利率附息 |
| 701003 | 递进利率 |
| 701004 | 浮动利率 |
| 701005 | 贴现 |
| 701006 | 未公布 |
| 701007 | 无利率 |
| 701008 | 累进利率 |

| 兑付方式编码 | 兑付方式 |
| --- | --- |
| 702001 | 到期一次付息 |
| 702002 | 按年付息 |
| 702003 | 按半年付息 |
| 702004 | 按季付息 |
| 702005 | 按月付息 |
| 702006 | 未公布 |
| 702099 | 其他 |

| 债券分类编码 | 债券分类 |
| --- | --- |
| 703001 | 短期融资券 |
| 703002 | 质押式回购 |
| 703003 | 私募债 |
| 703004 | 企业债 |
| 703005 | 次级债 |
| 703006 | 一般金融债 |
| 703007 | 中期票据 |
| 703008 | 资产支持证券 |
| 703009 | 小微企业扶持债 |
| 703010 | 地方政府债 |
| 703011 | 公司债 |
| 703012 | 可交换私募债 |
| 703013 | 可转债 |
| 703014 | 集合债券 |
| 703015 | 国际机构债券 |
| 703016 | 政府支持机构债券 |
| 703017 | 集合票据 |
| 703018 | 外国主权政府人民币债券 |
| 703019 | 央行票据 |
| 703020 | 政策性金融债 |
| 703021 | 国债 |
| 703022 | 非银行金融债 |
| 703023 | 可分离可转债 |
| 703024 | 国库定期存款 |
| 703025 | 可交换债 |
| 703026 | 特种金融债 |

| 债券形式编码 | 债券形式 |
| --- | --- |
| 704001 | 记账式 |
| 704002 | 实物式 |
| 704003 | 储蓄电子式 |
| 704004 | 凭证式 |
| 704005 | 未公布 |

#### 可转债转股价格调整（CONBOND_CONVERT_PRICE_ADJUST）

**表结构：**

| 名称 | 类型 | 描述 |
| --- | --- | --- |
| code | str | 债券代码 |
| name | str | 债券名称 |
| pub_date | date | 公告日期 |
| adjust_date | date | 调整生效日期 |
| new_convert_price | float | 调整后转股价格 |
| adjust_reason | str | 调整原因 |

#### 可转债日行情，从2018-09-13开始（CONBOND_DAILY_PRICE）

**表结构：**

| 名称 | 类型 | 描述 |
| --- | --- | --- |
| date | date | 交易日期（以YYYY-MM-DD表示） |
| code | str | 债券代码 |
| name | str | 债券简称 |
| exchange_code | str | 证券市场编码（XSHG-上交所；XSHE-深交所） |
| pre_close | float | 昨收价 |
| open | float | 开盘价，以人民币计 |
| high | float | 最高价，以人民币计 |
| low | float | 最低价，以人民币计 |
| close | float | 收盘价，以人民币计 |
| volume | float | 成交量（手），1手为10张债券 |
| money | float | 成交额，以人民币计 |
| deal_number | int | 成交笔数 |
| change_pct | float | 涨跌幅，单位：% |

#### 可转债每日转股统计，从2000-7-12开始(CONBOND_DAILY_CONVERT)

**表结构：** 深交所每日披露，上交所仅当日发生转股时才会披露

| 名称 | 类型 | 描述 |
| --- | --- | --- |
| date | date | 交易日期（以YYYY-MM-DD表示） |
| code | str | 债券代码 |
| name | str | 债券简称 |
| exchange_code | str | 证券市场编码（XSHG-上海证券交易所；XSHE-深圳证券交易所） |
| issue_number | int | 发行总量（单位：张） |
| convert_price | float | 转股价格 |
| daily_convert_number | int | 当日转股数量（深交所披露为债券转换量 单位：张，上交所披露为股票转换量 单位 :股） |
| acc_convert_number | int | 累计转股数量（深交所披露为债券转换量 单位：张，上交所披露为股票转换量 单位 :股） |
| acc_convert_ratio | float | 累计转股比例（单位：% ， 因上交所只披露转股股数，因此计算剩余转股张数时公式应为 : 发行总量 *(1 -累计转股比例) ） |
| convert_premium | float | 转股溢价，从2018-09-13开始计算（每张可转债转股后可以获得的收益，单位：元。**转股溢价=可转债收盘价-（100/转股价格）*正股收盘价**） |
| convert_premium_rate | float | 转股溢价率 |

#### 债券付息事件（含可转债）（BOND_INTEREST_PAYMENT）

**表结构：**

| 名称 | 类型 | 描述 |
| --- | --- | --- |
| code | str | 债券代码(不加后缀） |
| name | str | 债券简称 |
| exchange_code | int | 证券市场编码(新增字段) |
| exchange | str | 证券市场(新增字段) |
| pub_date | date | 公告日期 |
| event_type | str | 事件类型 |
| interest_start_date | date | 年度计息起始日 |
| coupon | float | 票面利率（%） |
| interest_end_date | date | 年度计息终止日 |
| autual_interest | float | 实际付息利率（%） |
| interest_per_unit | float | 每手付息数（单位：元，每1000元付息金额） |
| register_date | date | 债权登记日 |
| dividend_date | date | 除息日 |
| interest_pay_start_date | date | 付息起始日（债务人实际付息开始日期） |
| interest_pay_end_date | date | 付息终止日（债务人实际付息截止日期） |
| payment_date | date | 兑付日（债券到期兑付） |
| payment_per_unit | float | 每百元面值的到期兑付资金（元） |
| tax_rate | float | 代扣所得税率（%） |
| tax_channel | str | 扣税渠道 |

#### 可转债分钟/tick行情(仅本地接口jqdatasdk提供)

可转债分钟及tick行情仅本地接口jqdatasdk提供，官网无法使用，具体查看[JQData文档](https://www.joinquant.com/help/api/doc?name=JQDatadoc&id=9954)