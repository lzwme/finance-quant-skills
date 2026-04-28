<table style="border-collapse:collapse; margin:0 auto; border:none;">
  <tr>
    <td style="background:#fff; text-align:center; padding:2px; border:none;">
      <img src="helpdocs/img/md/huodong.png" style="height:150px;" onerror="this.src='data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAEAAAABCAQAAAC1HAwCAAAAC0lEQVR42mNkYAAAAAYAAjCB0C8AAAAASUVORK5CYII='"/>
    </td>
    <td style="background:#fff; text-align:center; padding:2px; border:none;">
      <img src="helpdocs/img/md/QQ.png" style="height:150px;" onerror="this.src='data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAEAAAABCAQAAAC1HAwCAAAAC0lEQVR42mNkYAAAAAYAAjCB0C8AAAAASUVORK5CYII='"/>
    </td>
  </tr>
  <tr>
    <td style="background:#fff; text-align:center; padding:2px; border:none;">
      <strong style="font-size:17px;">Baostock和湘财证券业务交流群 (可咨询PTrade、QMT)</strong>
    </td>
    <td style="background:#fff; text-align:center; padding:2px; border:none;">
      <strong style="font-size:17px;">Baostock官方技术服务QQ群:<b>1091604126</b> (问题解答 技术交流)</b></strong>
    </td>
  </tr>
</table>

<p style="margin:0;padding:0;line-height:1.2;"><strong style="font-size:24px;">平台介绍</strong></p>

**证券宝`www.baostock.com`**是一个**免费、开源**的**证券数据平台**（无需注册）。
* 提供大量准确、完整的证券历史行情数据、上市公司财务数据等。
* 通过python API获取证券数据信息，满足量化交易投资者、数量金融爱好者、计量经济从业者数据需求。
* 返回的数据格式：
  * pandas DataFrame类型，以便于用pandas/NumPy/Matplotlib进行数据分析和可视化。
  * 同时支持通过BaoStock的数据存储功能，将数据全部保存到本地后进行分析。
* 支持语言：目前版本BaoStock.com目前只支持**Python3.5**或**Python3.6**及以上(暂不支持python 2.x)。
* 持续更新：BaoStock.com还在不断的完善和优化，后续将逐步增加港股、期货、外汇和基金等方面的金融数据，为成为一个免费金融数据平台努力。
* 分享优化：请通过微信、网站博客或者知乎文章等方式分享给大家，使它能在大家的使用过程中逐步得到改进与提升，以便于更好地为大家提供免费服务。
* 平台麦克：证券宝BaoStock.com从发布到现在，已经帮助很多用户在数据方面减轻了工作量，同时也得到很多用户的反馈。它将一如既往的以免费、开源的形式分享出来，希望给有需要的朋友带来一些帮助。
**联系方式：Baostock官方技术QQ群：1091604126(问题解答、技术交流)；EMail:`baostock@163.com`。**
免费证券数据平台证券宝`www.baostock.com`会逐步分享证券投资文章、投资观点及教程，希望能够帮助大家！

## 下载安装

### 方式1：pip install baostock
使用指定源安装：
```python
pip install baostock -i https://pypi.org/simple
```

### 方式2：访问 [https://pypi.python.org/pypi/baostock](https://pypi.python.org/pypi/baostock) 下载安装
```python
python setup.py install或pip install xxx.whl
```
**注意：程序运行时，文件名、文件夹名不能是baostock。**

## 版本升级
```
 pip install --upgrade baostock -i https://pypi.org/simple
```

**使用前提：**

安装Python

安装pandas（pip install pandas）

建议安装Anaconda，以免出现问题（Anaconda是一个开源的Python发行版本，其包含了conda、Python等180多个科学包及其依赖项，下载地址`https://www.anaconda.com/download/`）。

## 每日最新数据更新时间：

* 当前交易日**17:30**，完成日K线数据入库；
* 当前交易日**18:00**，完成复权因子数据入库；
* 当前交易日**20:00**，完成分钟K线数据入库；
* 第二自然日**1:30**，完成前交易日“其它财务报告数据”入库；
* 周六**17:30**，完成周K线数据入库；
* 每月1号**17:30**，完成上月月K线数据入库；

## 每周数据更新时间：

* 每周一下午，完成上证50成份股、沪深300成份股、中证500成份股信息数据入库；

## 数据范围说明

### 股票数据

* 日、周、月K线数据，时间范围：1990-12-19至今。
* 5、15、30、60分钟K线数据，时间范围（近5年）：2020-01-03至今。

### ETF数据

* 日、周、月K线数据，时间范围：2026-01-05至今。
* 5、15、30、60分钟K线数据，时间范围：2026-01-05至今。

### 指数数据

* 日、周、月K线已经包含指数(不提供分钟K线数据)：综合指数，规模指数，一级行业指数，二级行业指数，策略指数，成长指数，价值指数，主题指数，基金指数，债券指数。
* 时间范围：2006-01-01至今。

### 季频财务数据

* 已经包含的财务数据：部分上市公司资产负债信息、上市公司现金流量信息、上市公司利润信息、上市公司杜邦指标信息。
* 时间范围：2007年至今。

### 季频公司报告

* 上市公司业绩预告信息，时间范围：2003年至今。
* 上市公司业绩快报信息，时间范围：2006年至今。

## 版本信息

### V0.9.1版本 2026/04/15

* 支持多节点服务请求。

### V0.8.9版本 2024/05/31

* 修复退出时socket未关闭问题；调整Demo程序的位置。

### V0.8.8版本 2019/01/25

* 新增接口get_data()，返回dataframe格式数据。

### V0.8.7版本 2018/12/14

* 优化服务器、客户端之间的网络传输。

### V0.8.5版本 2018/12/7

* 新增2019年交易日数据。

### V0.8.5版本 2018/11/27

* 新增2006年01月-2018年09月指数成分股数据。

### V0.8.5版本 2018/10/15

* 新增2006-2010年，日、周、月K线数据。

### V0.8.5版本 2018/9/14

* 新增2011年，5分钟、15分钟、30分钟、60分钟、日、周、月K线数据。
* 新增“行业分类”接口：query_stock_industry()。
* 新增“上证50成分股”接口：query_sz50_stocks()。
* 新增“沪深300成分股”接口：query_hs300_stocks()。
* 新增“中证500成分股”接口：query_zz500_stocks()。

### V0.8.1版本 2018/8/10

* 新增2012、2013年，5分钟、15分钟、30分钟、60分钟、日、周、月K线数据。
* 增强“历史A股K线数据”接口：query_history_k_data()，添加周、月线前后复权功能。
* 增强“证券代码查询”接口：query_all_stock()，查询结果添加证券名称。
* 增强“季频盈利能力”接口：query_profit_data()，查询结果添加总股本(totalShare)、流通股本(liqaShare)。

### V0.8.0版本 2018/7/27

* 新增“证券基本资料”接口query_stock_basic()。
* 新增“存款利率”接口query_deposit_rate_data()，提供1990年至今数据。
* 新增“贷款利率”接口query_loan_rate_data()，提供1990年至今数据。
* 新增“存款准备金率”接口query_required_reserve_ratio_data()，提供1999年至今数据。
* 新增“货币供应量”接口query_money_supply_data_month()，提供1978年至今数据。
* 新增“货币供应量(年底余额)”接口query_money_supply_data_year()，提供1952年至今数据。
* 新增“银行间同业拆放利率”接口query_shibor_data()，提供2006-10-08至今数据。

### V0.7.6.03版本 2018/6/1

* 新增2014年，5分钟、15分钟、30分钟、60分钟、日、周、月K线数据。
* 新增2014年交易日信息。
* 优化登陆逻辑。

### V0.7.6.02版本 2018/5/14

* 新增2015-2016交易日信息。
* 优化获取K线前后复权数据的性能。

### V0.7.5版本 2018/4/20

* 增强接口“获取历史A股K线数据”：query_history_k_data()，新增查询日K线、分钟线前后复权数据；周K线、月K线暂不支持。

### V0.7.2版本 2018/4/13

* 新增接口“交易日查询”：query_trade_dates()，提供2017-2018年数据。
* 新增接口“证券代码查询”：query_all_stock()，提供2015年至今数据。

### V0.7.0版本 2018/3/30

* 新增接口“盈利能力”接口query_profit_data()，提供2007至今的数据。
* 新增接口“营运能力”接口query_operation_data()，提供2007至今的数据。
* 新增接口“成长能力”接口query_growth_data()，提供2007至今的数据。
* 新增接口“偿债能力”接口query_balance_data()，提供2007至今的数据。
* 新增接口“现金流量”接口query_cash_flow_data()，提供2007至今的数据。
* 新增接口“杜邦指标”接口query_dupont_data()，提供2007至今的数据。
* 新增接口“公司业绩快报”接口query_performance_express_report()，提供2003至今的数据。
* 新增接口“公司业绩预告”接口query_forcast_report()，提供2006至今的数据。
* 新增web端下载示例数据。

### V0.6.2版本 2018/3/16

* 新增'查询复权因子'接口query_adjust_factor()，提供1990至2017年数据。
* API性能优化，加快获取数据速度。
* 接口中忽略证券代码大小写。
* 接口中对指标参数大小写不敏感。
* 官网中提供搜索功能。

### V0.6.1版本 2018/2/13

* 接口query_history_k_data()，新增"d=日k线、w=周k线、m=月k线"2015-01-01至今的规模指数、一级行业指数、二级行业指数、策略指数、成长指数、价值指数、主题指数。
* 接口query_history_k_data()，新增"d=日k线"滚动市盈率(peTTM)、市净率(pbMRQ)、滚动市销率(psTTM)、滚动市现率(pcfNcfTTM)。
* 接口query_history_k_data()，新增指数、股票"d=日k线、w=周k线、m=月k线"的涨跌幅(pctChg)。
* 接口query_history_k_data()，新增股票"d=日k线"的'是否ST(isST)'。
* 新增'查询除权除息信息'接口query_dividend_data()，提供1990年至2017年数据。

### V0.5.5版本 2018/2/5

* 优化next()方法，获取大量数据时分批次获取。

### V0.5.1版本 2018/1/11

* 新增获取历史K线数据接口query_history_k_data()。
* 提供2015-01-01至今的上交所A股、深交所A股，上交所指数（综合指数）、深交所指数（综合指数）d=日k线、w=周k线、m=月k线、5=5分钟、15=15分钟、30=30分钟、60=60分钟k线数据。