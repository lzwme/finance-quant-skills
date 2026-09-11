## 常见问题

感谢您使用JoinQuant（聚宽）量化交易平台，以下内容希望解答您对JoinQuant的疑问。
 如果您想了解我们提供的API如何使用，请查看[API文档](https://www.joinquant.com/help/api/index)。
 如果以下内容仍没有解决您的问题，请您通过[社区提问](https://www.joinquant.com/community#tag=faq)的方式告诉我们，谢谢。

[常见Bug或者警告>>>](https://www.joinquant.com/view/community/detail/6cab768c4b2fa259385a45927089367f)

### 关于JoinQuant

### 数据

#### JoinQuant提供哪些数据及数据更新频率

[提供的数据及更新频率](https://www.joinquant.com/help/api/help?name=JQData#JQData%E6%8F%90%E4%BE%9B%E5%93%AA%E4%BA%9B%E6%95%B0%E6%8D%AE%E5%8F%8A%E6%95%B0%E6%8D%AE%E6%9B%B4%E6%96%B0%E9%A2%91%E7%8E%87)

1. 股票数据：我们拥有所有A股上市公司2005年以来的股票行情数据、[市值数据](https://www.joinquant.com/data/dict/fundamentals#市值数据)、[财务数据](https://www.joinquant.com/data/dict/fundamentals)、[上市公司基本信息](https://www.joinquant.com/help/api/help?name=Stock#上市公司概况)、[融资融券信息](https://www.joinquant.com/help/api/help?name=Stock#获取股票的融资融券信息)等。为了避免[幸存者偏差](https://baike.baidu.com/item/%E5%B9%B8%E5%AD%98%E8%80%85%E5%81%8F%E5%B7%AE/10313799?fr=aladdin)，我们包括了已经退市的股票数据（但是不包含2005年之前退市的股票）。
2. 基金数据：我们目前提供了600多种在交易所上市的基金的行情、净值等数据，包含[ETF](https://www.joinquant.com/data/dict/fundData#etf列表)、[LOF](https://www.joinquant.com/data/dict/fundData#lof列表)、[分级A/B基金](https://www.joinquant.com/data/dict/fundData#分级基金列表)以及[货币基金](https://www.joinquant.com/help/api/help?name=fund#货币基金列表)的完整的行情、净值数据等，请点击[基金数据](https://www.joinquant.com/data/dict/fundData)查看。
3. 金融期货数据：我们提供中金所推出的所有[金融期货产品](https://www.joinquant.com/data/dict/sfData)的行情数据，并包含历史产品的数据。
4. 股票指数：我们支持近600种[股票指数](https://www.joinquant.com/data/dict/indexData)数据，包括指数的行情数据以及成分股数据。为了避免未来函数，我们支持获取历史任意时刻的指数成分股信息，具体见[get_index_stocks](https://www.joinquant.com/help/api/help?name=api#get_index_stocks)和[get_index_weights](https://www.joinquant.com/help/api/help?name=api#get_index_weights)。注意：指数不能买卖
5. 行业板块：我们支持按行业、按板块选股，具体见[get_industry_stocks](https://www.joinquant.com/help/api/help?name=api#get_industry_stocks)
6. 概念板块：我们支持按概念板块选股，具体见[get_concept_stocks](https://www.joinquant.com/help/api/help?name=api#get_concept_stocks)
7. 宏观数据：我们提供全方位的[宏观数据](https://www.joinquant.com/data/dict/macroData)，为投资者决策提供有力数据支持。
8. 所有的行情数据我们均已处理好前复权信息。
9. 我们当日的回测数据会在收盘后通过多数据源进行校验，并在T+1（第二天）的00:01更新。

#### JoinQuant提供的数据支持下载吗？

JoinQuant提供的数据可以在官网的回测、模拟交易、研究模块使用；
 本地下载请使用[jqdatasdk](https://www.joinquant.com/help/api/help?name=JQData#JQData-%E6%9C%AC%E5%9C%B0%E9%87%8F%E5%8C%96%E6%95%B0%E6%8D%AE%E8%AF%B4%E6%98%8E%E4%B9%A6)。

#### 数据后缀是怎么定义的？

市场后缀按照 [ISO10383 标准](https://www.iso20022.org/market-identifier-codes)

| 交易市场 | 代码后缀 | 示例代码 | 证券简称 |
| --- | --- | --- | --- |
| 上海证券交易所 | .XSHG | '600519.XSHG' | 贵州茅台 |
| 深圳证券交易所 | .XSHE | '000001.XSHE' | 平安银行 |
| 中金所 | .CCFX | 'IC9999.CCFX' | 中证500主力合约 |
| 大商所 | .XDCE | 'A9999.XDCE' | 豆一主力合约 |
| 上期所 | .XSGE | 'AU9999.XSGE' | 黄金主力合约 |
| 郑商所 | .XZCE | 'CY8888.XZCE' | 棉纱期货指数 |
| 上海国际能源期货交易所 | .XINE | 'SC9999.XINE' | 原油主力合约 |
| 广州期货交易所 | .GFEX | 'SI9999.GFEX' | 工业硅主力合约 |

- 场外基金：代码后缀为.OF，例如银河沪深300价值指数的代码为519671.OF
- 期权和对应的标的后缀相同，具体的可以查看[期权合约资料](https://www.joinquant.com/help/api/help?name=Option#%E8%8E%B7%E5%8F%96%E6%9C%9F%E6%9D%83%E5%90%88%E7%BA%A6%E8%B5%84%E6%96%99)
- 其他数据后缀请查询[数据字典](https://www.joinquant.com/data)

#### 发现数据有问题怎么办？

（1）查看下我们的[数据常见疑问汇总](https://www.joinquant.com/view/community/detail/1226a48b1f9b7bd90dc3516feea8b5cc?type=2)，也许您认为的问题已经有说明了；
 （2）在[社区发帖](https://www.joinquant.com/view/community/list?listType=2&type=isNew&tags=)，详细描述下您的问题，包括以下内容：

- 具体是什么问题;
- 发下查询语句；
- 发下查询结果并标记下觉得有问题的地方；
- 发下对比截图；
- [发帖参考贴](https://www.joinquant.com/post/15582?tag=algorithm)

#### 不同平台的行情数据或者财务数据不同

行情数据不同
 （1）目前我们默认提供的是前复权数据，不复权数据可以将get_price的fq设置为None获取；
 （2）不同平台的复权数据源或者算法不同，导致前复权及后复权数据的不同，具体的可以多对比一些平台就了解了；
 （3）fq不为None时的成交量数据我们也做了复权处理，需要不复权数据可以将fq设置为None；
 （4）更多行情数据的说明请查看[数据常见疑问汇总](https://www.joinquant.com/view/community/detail/1226a48b1f9b7bd90dc3516feea8b5cc?type=2)

财务数据不同
 （1）财务指标数据有单季度和报告期两种，一般财经网站上提供的财务指标数据都是上市公司披露的原始报告期数据，所以请先确定对比的是相同的数据；
 （2）我们同时提供的有单季度的和报告期的数据，[单季度](https://www.joinquant.com/help/api/help?name=Stock#%E8%8E%B7%E5%8F%96%E5%8D%95%E5%AD%A3%E5%BA%A6%E5%B9%B4%E5%BA%A6%E8%B4%A2%E5%8A%A1%E6%95%B0%E6%8D%AE)和[报告期](https://www.joinquant.com/help/api/help?name=Stock#%E8%8E%B7%E5%8F%96%E6%8A%A5%E5%91%8A%E6%9C%9F%E8%B4%A2%E5%8A%A1%E6%95%B0%E6%8D%AE)的财务数据，您也可以分别查看使用。例如可以通过下面的方式获取报告期的eps:![image](https://image.joinquant.com/a3ddf6470e8205cbb73facdf0814388e)
 （3）单季度财务数据提供上市之后的数据（不包含上市之前的），报告期有上市前的财务数据；核查时请注意上市时间；
 （4）上市公司公布财报分四种，一季度报、中期年度报、前三季度报、全年年报，统计的周期跨度分别为第一季度、前两个季度、前三个季度、全年，而聚宽考虑到量化分析，所以默认查询的财务指标数据是单季度的；例如[同花顺](http://stockpage.10jqka.com.cn/000759/finance/#finance)上的单季度数据查询方法，选择按单季度统计，如下图：![image](https://image.joinquant.com/acea19612851d31b57f3ecd283bbe6fd) （5）市值（valuation）数据中market_cap、pb_ratio、pe_ratio、ps_ratio等由于算法或者数据源不同，各个平台数据不一定完全相同；
 （6）公告没有披露的数据为空值；

查询过程有问题的话，请查看[数据常见疑问汇总](https://www.joinquant.com/view/community/detail/1226a48b1f9b7bd90dc3516feea8b5cc?type=2)

还有问题请在聚宽社区发帖，详细描述下您的问题，并附上对应的查询代码、结果截图以及预期结果，我们核查下答复您。

#### JQData，jqdatasdk和jqdata的关系

（1）JQData和jqdatasdk是同一个产品不同的名称，是一个Python库(或模块)，是聚宽提供的数据接口，在您自己搭建的本地环境中使用（可以脱离官网独立使用），具体方法见[JQData的API](https://www.joinquant.com/help/api/help?name=JQData)；
 （2）jqdata是官网的数据产品，主要在官网使用，具体使用方法见[官网的API](https://www.joinquant.com/help/api/help?name=api)；
 （3）jqdata和jqdatasdk中的获取数据的函数及使用方法稍微不同，使用对应的API就没问题；再强调一下，**jqdatasdk不能在官网的回测、模拟、研究中使用**

#### 如何获取行业及概念板块的行情数据及pe,pb等数据

（1）概念板块目前只可以通过[get_concept_stocks](https://www.joinquant.com/help/api/help?name=api#%E6%95%B0%E6%8D%AE%E8%8E%B7%E5%8F%96%E5%87%BD%E6%95%B0)获取某个概念板块包含哪些股票；
 （2）目前没有概念板块的行情数据，敬请期待；
 （3）可以通过[get_industry_stocks](https://www.joinquant.com/help/api/help?name=api#%E6%95%B0%E6%8D%AE%E8%8E%B7%E5%8F%96%E5%87%BD%E6%95%B0)获取某个行业有哪些股票，也可以通过[get_industry](https://www.joinquant.com/help/api/help?name=api#%E6%95%B0%E6%8D%AE%E8%8E%B7%E5%8F%96%E5%87%BD%E6%95%B0)查询股票属于哪个行业;
 （4）目前不支持行业的行情数据，及指数的PE/股息率

#### 有关期货主力合约或者指数与其他平台问题

### 为什么有时看到的期货主力合约和其他平台不一致，是怎么判断的，什么时候更新的

（1）因此我们根据**持仓量（不是成交量）**对期货合约进行拼接，形成主力连续合约；![image](https://image.joinquant.com/da0e8a09ccc31eae63bbc1c92001ce36)
 （2）主力合约根据T-2和T-1的持仓量生成，在T-1的晚上、也即T日的夜盘开始前就切换到新的主力合约；
 （3）wind等显示主连的数据及主力合约![image](https://image.joinquant.com/455a1877238bb797e628e1d314bb642d)

#### JQData使用过程过程有问题怎么处理？

（1）有关账户、权限、价格等方面，可以查看[JQData文档](https://www.joinquant.com/help/api/doc?name=logon&id=9830)；
 （2）查看[JQData常见问题](https://www.joinquant.com/view/community/detail/16925)；
 （3）在聚宽社区中[社区提问题模块](https://www.joinquant.com/view/community/list/2?type=isNew&tags=)发帖提问，详细描述下问题，发下对应的测试代码及结果截图，我们核查后答复您。

### 回测

爱分享的小伙伴已经在社区分享了[许多策略](https://www.joinquant.com/community/algorithm)，您可以一键克隆免费使用。

#### 回测的作用？

策略有效体现了您的交易思想，通过历史数据的回测，可以检验策略的有效性。

#### 回测可以使用哪些数据？

回测可以免费使用 JoinQuant 提供的所有数据。[点击这里](https://www.joinquant.com/data)了解更多信息。

回测使用的交易数据有一天的延时，即当天的交易数据在第二天的0:01分更新。

延时原因：回测使用的交易数据基于Level-2行情数据，Level-2级别的完整交易数据需要收盘后才能获得，目前市场上没有权威的行情数据，为了保证数据的准确性，我们购买了多个数据提供商的数据，经过一系列处理后才投入使用。

#### 如何创建并运行策略？

通过策略列表页进入策略详情页后，按如下步骤编写策略，运行回测：

（1）进入[策略列表](https://www.joinquant.com/algorithm/index/list)页面

您可以看到一些默认的策略，您可以直接打开这些策略，编译运行或者运行回测。

（2）点击新建策略，编辑策略，编译运行，快速回测

![我的策略-新建策略.png](https://image.joinquant.com/f1ebebb9a0a6ace75745f6b069a99976)

点击新建策略后会出现一些模板策略，您可以直接运行这些策略、修改这些策略或者删除模板策略重新写

![微信图片_20181016171524.png](https://image.joinquant.com/737d7180d04d8542f841b3b0c6526507)

![编译运行.png](https://image.joinquant.com/f894f2cf342d065d2b8902f94d47d013)

（3）完整回测

![运行回测.png](https://image.joinquant.com/0d39e9a33f0ba325bd71ee38144ce269)

#### 如何编写一个最简单的策略？

- 参照[示例策略](https://www.joinquant.com/algorithm/index/new)，修改代码；
- 从[社区](https://www.joinquant.com/community/algorithm)克隆一个您感兴趣的策略；
- [新建一个策略](https://www.joinquant.com/algorithm/index/list)，从头开始实现自己的交易思路；

如果您想要更详细的了解如何写策略，[点击这里](https://www.joinquant.com/api#开始写策略)

#### 编译运行和运行回测的区别？

编译运行便于您快速调试代码，检查代码中的错误，策略的运行结果也能更快的展示，仅统计了基准收益、Total Returns（策略总收益）、Alpha（阿尔法）、Beta（贝塔）、Sharpe（夏普比率）、Max Drawdown（最大回撤）等。

运行回测是一次完整的回测，不仅包括编译运行中已经统计的指标，还包括交易详情、每日持仓&收益等信息。

#### 回测时Cash（可用资金）为负是因为什么？

市价单时, 为了让用户能够满仓买入一支股票, 我们并不是按照涨停价计算可买的数量, 而是按照当时的实际价格计算的, 如果按照涨停价计算可买的数量的话, 可能总是只能有90%的仓位. 而成交价格因为滑点的原因可能比市价高一些. 导致成交金额超出了可用资金，与实际情况有些出入. 这个也是导致仓位有时大于100%的原因。

#### 多次回测的结果不一样， 可能是什么原因？

（1）比较的前提: 开始/结束日期、起始资金、策略及运行频率必须相同；运行环境必须完全相同，例如都是在聚宽官网的Python3环境运行；可以在聚宽官网回测列表中，回测对比和代码对比工具对比查看![img](https://image.joinquant.com/d016e295783fb01eead1252f5157d92a)
 （2）策略的原因（在相同条件下多次回测比较结果是否相同来排除）:

- 代码中有随机因素，包括但不限于这些例子：(A)遍历 dict中的元素. 因为dict 是无序存储的, 每次遍历的顺序可能不一样；(B)集合在Python内部通过哈希表实现，其本征无序，输出时所显示的顺序具有随机性；(c)使用的一些Python模块的函数是随机，例如一些机器学习算法；(d)[MySQL、sqlalchemy等数据查询出现的随机因素](https://www.joinquant.com/view/community/detail/7221e4e7cef20a72bd21b0bd65b7fe6c?type=2)
- 不稳定的排序，比如多列的DataFrame, 根据一列进行排序, 每次排序后最终的DataFrame可能是不一样的；
- 没有采用真实价格回测, 而且建立回测的日期不一样，因为回测中看到的价格可能是根据建立回测的日期做前复权处理的，如果建立的两个日期之间有股票发生了除权, 而策略又操作了这只股票, 则会可能会导致回测不一样；
- Python环境的问题，例如官网的python2和python3环境，这两个一些地方不同（例如：Python2 中除法只保留整数位，除法这个问题加入后面代码可以解决： from **future** import division (注意future前和后面都有两个下划线)）

（3）参考：模拟交易和回测的差别，模拟交易和回测的差别

- [模拟交易和回测的差别](https://www.joinquant.com/help/api/help?name=api#%E6%A8%A1%E6%8B%9F%E4%BA%A4%E6%98%93%E5%92%8C%E5%9B%9E%E6%B5%8B%E7%9A%84%E5%B7%AE%E5%88%AB)

#### 参数优化及并行回测

#### 参数优化及并行回测参考教程

- [多回测运行和参数分析框架](https://www.joinquant.com/view/community/detail/80ee3db068254e1e9aadbdd9b2420270?type=1)
- [多回测运行和参数分析框架(Python3)](https://www.joinquant.com/view/community/detail/aaaf43b0b39a46f1600cbf44f3cf8513)
- [在投资研究中调用回测或者模拟交易，多基准绘图](https://www.joinquant.com/view/community/detail/872b885345bbdf13d2138580a7baa066)
- [研究中写策略并回测](https://www.joinquant.com/view/community/detail/6342bc6bd43e371bda10f7402359b805)

#### 区分create_backtest(策略ID)和get_backtest(回测ID)

- 策略ID（algorithmId）：每个策略的唯一标识，可以为此策略设置不同的回测条件，得到不同的回测ID
    - **聚宽官网**![img](https://image.joinquant.com/ae3bcb713ded3840d50b602e8a84cfd3)
- 回测ID（backtestId）:每个回测的唯一标识
    - **聚宽官网**![img](https://image.joinquant.com/73514339d9b8e3f45818b0eb6c0594bf)
- 模拟交易ID（backtestId）：每个模拟交易的唯一标识
    - **聚宽官网**![img](https://image.joinquant.com/b6c872612c25dc4d24ab5adb6e663279)
- create_backtest:在研究中创建回测，需要使用策略ID（algorithmId）
- get_backtest:在研究中获取回测或者模拟交易的信息，获取回测信息使用回测ID（backtestId），获取模拟交易信息使用模拟交易ID（backtestId）
- 三个ID的关系
    - 策略ID设置不同的回测条件（开始时间、资金、频率），会得到不同的回测结果；
    - 每组回测条件下的回测ID是唯一的
    - 可以根据回测结果创建模拟交易，[创建模拟交易的方法](https://www.joinquant.com/help/api/help?name=faq#%E5%A6%82%E4%BD%95%E8%BF%9B%E8%A1%8C%E6%A8%A1%E6%8B%9F%E4%BA%A4%E6%98%93%EF%BC%9F)

#### 回测运行比较慢

回测时耗费的时间和您的网速、策略、运行频率、回测时间区间有关：

- 整个回测过程是发送请求到服务器，然后在网页上显示回测结果，如果您网络比较慢的话，会有影响；
- 运行频率：一般的数据量，天 < 分钟 < tick，因此一般的tick级策略耗费的时间相对比较长，这个是正常的；
- 回测区间：这个当然是回测的时间越短，耗时越短了；
- 具体策略：可以参考[性能分析](https://www.joinquant.com/help/api/help?name=api#enable_profile)，查看下哪部分比较耗费时间，然后优化下策略；

### 模拟交易

模拟交易的数据与实际数据完全同步，您可以通过模拟交易进一步检验策略的有效性。

#### 模拟交易运行时间

时限为限时的模拟交易，及VIP/SVIP的全部模拟交易，在正常时间实时运行；

普通用户时限为永久的模拟交易，统一在收盘后延时运行（2019-12-01起）。 延时运行的模拟交易，交易数据统一在第二天开盘前更新，并且无法开启微信通知，分钟级、Tick级模拟交易不展示当日收益。运行时间的变更将会在模拟交易下一次运行时生效。如果您想在交易时间实时运行模拟交易，可以

1，[使用积分兑换限时模拟交易位](/view/credits/detail/8)，限时模拟交易位到期后将会关闭，无法再次开启，请注意及时续费

2，[成为VIP或SVIP](/view/vip/charge)，不仅可以实时运行模拟交易，还可以在高峰排队时优先运行，VIP/SVIP到期后将会恢复原先的运行时间

#### 模拟交易使用什么数据？

模拟交易使用的数据是实时更新的Level-1数据，目前模拟交易数据有10s延时。 延时原因：为了保证数据的准确性，我们做了一系列处理。

#### 如何进行模拟交易？

您可以通过以下两种方法进行模拟交易(推荐使用方法一)， **创建模拟交易的前提是已经运行了回测，如果没有回测的话，请先[创建回测](https://www.joinquant.com/help/api/help?name=faq#%E5%A6%82%E4%BD%95%E5%88%9B%E5%BB%BA%E5%B9%B6%E8%BF%90%E8%A1%8C%E7%AD%96%E7%95%A5%EF%BC%9F)**

##### 方法一，使用回测结果创建

找到需要创建模拟交易的回测，点击模拟交易，输入参数，点击确定

![回测创建模拟交易.png](https://image.joinquant.com/5210b4403ebbd893fcf33c6264c0abc2)

##### 方法二，在模拟交易列表中创建

1.进入[模拟交易列表](https://www.joinquant.com/algorithm/trade/list)

2.点击新建模拟交易，在跳出的窗口中依次输入交易名称和初始资金，并选择策略及其回测后点击确定。

![模拟交易-新建模拟交易-1.png](https://image.joinquant.com/7d806841d2cd0b94b14076cf104de9ee)

#### 如果提示没有可用的模拟交易位，请点击[模拟交易列表](https://www.joinquant.com/algorithm/trade/list?process=1)最下面的**获取新的模拟交易位**，使用积分兑换模拟交易位；请注意模拟交易位是和频率有关的，需要选择对应运行频率的模拟交易位。

#### 模拟交易支持哪些操作？

- 模拟交易支持暂停、重启、关闭；
- 模拟交易暂停后，不会再执行策略代码，不会产生交易信号，收益曲线还会一直画；
- 模拟交易重启后，策略恢复执行，重启会从当前时间（执行重启操作的时间）开始执行，注意与重跑的区别；
- 模拟交易关闭后，模拟交易将彻底结束，无法再次打开；

#### 如何替换模拟交易的代码？

您可以根据需要替换模拟交易的代码，替换代码后，我们按照新的代码计算累计收益、持仓、下单等内容，替代之前的各项指标、持仓、下单不会使用新的代码重新计算。 为了保证新代码的正确性，替换代码时只能选择当前模拟交易对应策略的回测详情；需要先回测再创建模拟交易。 旧代码中的全局变量(包括全局对象g)会保留，并应用到新代码中，所以请您确保新代码使用旧代码的全局变量不会出现问题；如果不希望使用旧的全局变量，您可以定义新的全局变量。

替换步骤如下：

- 仔细查看[替换代码注意事项](https://www.joinquant.com/help/api/help?name=api#模拟盘注意事项)
- 仔细查看[怎样替换代码](https://www.joinquant.com/view/community/detail/e5cc8c36bcee96bfe6886153f54a46cf)
- 找到此模拟交易对应的策略，修改策略后并**回测**；
- 在模拟交易页面依次点击：代码--->替换代码；
- 在跳出的窗口中选择需要替换的**回测**，并点击确定；
- 查看替换后的代码。

替换代码与修改代码的区别

- 修改代码少了回测的步骤，适用于修改量比较少且不容易出错的情况；
- 如果对修改后的代码没有把握的话，建议先回测再替换代码；
- 修改代码如果要修改全局变量、修改函数运行时间、添加运行函数等，仍然需要after_code_changed

替换代码后，代码何时运行

- 这个和具体策略的状态（是否已经暂停或者运行失败了）、是不是实时运行的策略、频率（分钟还是天）、代码、替换时间（盘中还是盘后）有关；
- 一般的正常运行模拟，替换代码后，会在原代码下一次运行时运行新代码（例如分钟级别的盘中替换，下一分钟就会运行新代码;天级别的一般是run_daily中下一个运行时间或者下一个交易日）；
- 分钟级别策略可以重新替换代码，在after_code_changed中不加任何判断条件的前提下打印当前时间；
- 仍有疑问可以在确定正常运行分钟级别策略前提下，在社区发帖提供具体信息讨论：(1)设置页面，策略信息部分；(2)设置页面，替换代码记录；(3)代码页面，策略的初始化部分和替换代码部分代码；(4)策略日志；
- 不确定的话，可以关闭使用新代码新建模拟；

替换代码示例

```python
# 初始化函数，设定基准等等
def initialize(context):
    # 设定沪深300作为基准
    set_benchmark('000300.XSHG')
    # 开启动态复权模式(真实价格)
    set_option('use_real_price', True)
    # 将日志级别设置为error
    log.set_level('order', 'error')

    # 设置全局变量
    g.day = 1

    # 开盘时运行
    run_daily(market_open, time='09:30', reference_security='000300.XSHG')
    # 快收盘时运行
    run_daily(close_market_end, time='14:50', reference_security='000300.XSHG')

## 开盘时运行函数
def market_open(context):
    print(context.current_dt)
    print(g.day)
    print('='*50)

## 快收盘时运行
def close_market_end(context):
    print("注意注意，快收盘了")
    print(g.day)
    print('='*50)

########################### 上面为替换代码前原始代码，下面为替换代码添加 ###########################
## 收盘后运行函数，后来添加
def after_market_open(context):
    print("收盘啦，洗洗睡...")
    print('='*50)

def after_code_changed(context):
    # 先取消之前run_daily中注册的函数，否则之前注册的9:30仍然会运行
    unschedule_all()
    # 修改market_open的运行时间为10:00
    run_daily(market_open, time='10:00', reference_security='000300.XSHG')
    # 快收盘时运行（再次注册，因为被unschedule_all取消了）
    run_daily(close_market_end, time='14:50', reference_security='000300.XSHG')
    # 添加新写的函数after_market_open
    run_daily(after_market_open, time='15:30', reference_security='000300.XSHG')
    # 修改全局变量g.day
    g.day = 888
    # 将日志级别设置为debug
    log.set_level('order', 'debug')
```

#### 如何重新设置日志级别（替换代码）

日志级别的说明：
 1.如果还没有开启模拟交易：建议使用默认的日志级别（不用设置日志级别）或者设置日志级别为debug，具体方法为log.set_level('order', 'debug')；
 2.如果已经开启模拟交易，且在初始化中设置日志级别为error，可以通过替换代码的方式实现：
 （1）如果您之前替换过代码，策略中有after_code_changed，直接在after_code_changed中添加log.set_level('order', 'debug')即可；
 （2）如果您之前没有替换过代码，需要在策略中添加after_code_changed，并且在after_code_changed中添加log.set_level('order', 'debug')，最终形式为：

```python
def after_code_changed(context):
    # 设置日志级别为debug
    log.set_level('order', 'debug')
```

(3)替换代码的方法

示例代码如下：

```python
# 初始化函数，设定基准等等
def initialize(context):
    # 推荐：设置日志级别为debug(或者不设置日志级别，使用系统推荐的)
    log.set_level('order', 'debug')

    # 不推荐：设置日志级别为error(为了可以方便地看到您的问题，建议不要这样设置)
    # log.set_level('order', 'error')

    # 开盘前运行
    run_daily(before_market_open, time='09:00', reference_security='000300.XSHG')

## 开盘前运行函数
def before_market_open(context):
    print(context.current_dt)

# 替换代码，设置日志级别为debug
def after_code_changed(context):
    # 设置日志级别为debug
    log.set_level('order', 'debug')
    print("已经设置日志级别为debug啦！")
```

(4)更多的替换代码方法
 [如何替换模拟交易的代码](https://www.joinquant.com/help/api/help?name=faq#%E5%A6%82%E4%BD%95%E6%9B%BF%E6%8D%A2%E6%A8%A1%E6%8B%9F%E4%BA%A4%E6%98%93%E7%9A%84%E4%BB%A3%E7%A0%81%EF%BC%9F)
 [怎样替换代码](https://www.joinquant.com/view/community/detail/0fd4ee9e029c205c4beb48547c582f00)
 [替换代码及注意事项](https://ycjq.95358.com/post/25?tag=new)

#### 如何开启微信通知？

开启微信通知后，您可以通过微信接收模拟交易的下单信号，也可以通过[send_message](https://www.joinquant.com/help/api/help?name=api#%E5%85%B6%E4%BB%96%E5%87%BD%E6%95%B0)发送自定义微信内容。
 回测不支持微信通知；
 盘中开启微信通知，当日不推送微信信号；
 模拟交易的下单信号由腾讯微信发送，可能有30s内的延迟；
 延时模拟交易不支持微信通知，[开启实时运行](https://www.joinquant.com/help/api/help?name=faq#%E5%BB%B6%E6%97%B6%E8%BF%90%E8%A1%8C)
 默认每天发送自定义消息条数为5，[获取更多每日发送自定义消息数据](https://www.joinquant.com/view/credits/detail/9d50cc3a6e3ccc073c297403b84c715e)
 未收到微信消息：（1）确定是否已经开启微信通知，且是实时运行的模拟交易；（2）区分模拟交易的下单信号还是自定义消息：下单先检查一下交易详情页面有没有下单记录；自定义需要自己检查策略逻辑是否符合发送条件，还有是否已经超过自定义消息条数。

- 开启微信通知步骤如下：

绑定微信账号并开启微信通知，使用微信扫一扫绑定微信账号。
 注意：一个JoinQuant账号仅支持绑定一个微信账号，一个微信号也只能和一个聚宽账号绑定

![绑定微信账号.png](https://image.joinquant.com/81d5d584b6121da5b8c6398fcc0ffb40)![enter image description here](https://image.joinquant.com/928691edf26e4954a06189edec981f30)

- 微信通知示例

模拟交易下单信号及异常信号提醒

![微信图片_20181029102058.png](https://image.joinquant.com/d34ce1eb89b0e6baf395a7632f8a8bc2)

- 替换之前绑定的微信号，请查看下面的如何重新绑定 点击如图箭头所示位置，出现如图所示二维码，扫码后即重新绑定微信。

![模拟交易-重新绑定微信.png](https://image.joinquant.com/594ea506c084d5a564dc4a797304fc21)

#### 数据有延迟？

数据有延迟是正常的。即便在同花顺、东方财富等客户端看到的数据也是延迟的数据。
 因为信息从证券交易所发出，再到数据提供商，再到终端，是存在延时的。
 我们数据存在的延时是指与交易所发出数据的时刻的延时，并不是与您在客户端看到的数据的延时。
 可以使用tick级别的数据，基本无延迟；
 本地实时获取数据可以使用[jqdatasdk](https://www.joinquant.com/help/api/help?name=JQData)

#### 日志提示：策略进程异常退出，可能是什么原因？

在平台上运行策略时，日志出现该提示，通常是因为策略进程非正常结束所致。以下列举几种可能得原因：

- 调用 `sys.exit()` 企图退出程序 `sys.exit()` 表示结束进程的运行，在平台上运行时则表示整个回测或者模拟运行结束，这样做是没有必要的。若需退出函数，请使用 `return` 即可。
- 调用 raise SystemExit 企图抛出异常 当调用 `raise SystemExit` ，实际上它会调用 `sys.exit()` ，所以也可能导致进程非正常退出。
- 错误的字符串格式化方式 使用 `%` 来格式化字符串，可能会遇到类似 `ValueError: unsupported format character` 的错误，导致进程异常退出。字符串格式化中希望输出 `%` 的情况如： `收益：%s%` ，实际意图是希望输出 `收益：0.1%` ，但用法可能是错误的，因为输出`%`时需要对其进行转义。建议使用 `str.format` 的方式格式化字符串。[点击这里](https://www.joinquant.com/post/5547)了解更多信息。
- 调用第三方库 部分第三方库是用C语言扩展，直接调用动态库，如：numpy，错误的调用可能会导致**段错误**，这样策略进程也会异常退出。另有部分第三方库可能创建新的进程、线程、锁等，平台资源有限，所以限制了策略进程所能占用的资源，若占用资源过大，可能导致进程崩溃。
- 其他不正确的代码书写方式 Python 是动态型语言，很多错误的书写方式是语法检测不出来的，如：错误的使用了字符串格式化方式，这些错误只有当代码运行到该处时才会报错，否则表现为正常运行的情况。

#### 模拟交易或者回测怎么读取本地文件或者保存文件到研究

- 官网的策略是不能读取您本地文件或数据的，但是我们支持您上传到我们的投资研究中读取，同时也支持连网获取数据，具体使用方法请参考教程[在回测及模拟交易中读取研究中数据](https://www.joinquant.com/view/community/detail/19300)。将回测或者模拟的数据保存到研究中中的方法贴中也有说明。

#### 模拟交易没有运行？

- 鼠标放在收益曲线最右侧, 可以看到最后一次运行的时间;
- 查看模拟交易什么时候开始运行的，一般是当天开启，下一个交易日才运行；
- 如果是对run_weekly/run_monthly有疑问, 注意这两个方法设置的是**第几个交易日**, 不是周几/几号, **开始策略的那一周/月第一个交易日是从开始的那一天开始计算的**, 比如本周w五个交易日, 策略从周二开始, 注册运行run_weekly(day=3), 第一个交易日是周二, 第三个交易日是周四,所以第一周是在周四运行, 往后每周的第三个交易日运行。
- 刷新下页面；
- 查看模拟交易的状态是否正常，查看日志是否运行失败；
- 在模拟交易列表中查看对应的模拟交易位到期时间，检查是否已经到期，被关闭；
- 是否有一个多月没有登录，如果一个月没有登录官网的话，系统会停掉模拟交易，对应的日志也有说明，登录后，下一个交易日即可运行；
- 查看是不是延时运行的，是的话可以[改为实时运行](https://www.joinquant.com/help/api/help?name=faq#%E5%BB%B6%E6%97%B6%E8%BF%90%E8%A1%8C)，然后下一个交易日看看；
- 是不是替换了代码，替换代码注意事项及替换后什么时候生效请查看[如何替换代码](https://www.joinquant.com/help/api/help?name=faq#%E5%A6%82%E4%BD%95%E6%9B%BF%E6%8D%A2%E6%A8%A1%E6%8B%9F%E4%BA%A4%E6%98%93%E7%9A%84%E4%BB%A3%E7%A0%81%EF%BC%9F);
- 确定下，是不是具体什么时候一定有日志，但是没有出现，**没有日志不一定是没有运行**，不符合打印日志的条件就不会打印；如果输出日志带有判断逻辑，请自行检查打印条件是否触发。

#### 模拟交易界面上参数说明

- 查看模拟交易的状态是否正常，查看日志是否运行失败；
- 在模拟交易列表中查看对应的模拟交易位到期时间，检查是否已经到期，被关闭；
- 是否有一个多月没有登录，如果一个月没有登录官网的话，系统会停掉模拟交易，对应的日志也有说明，登录后，下一个交易日即可运行；
- 查看模拟交易什么时候开始运行的，一般是当天开启，下一个交易日才运行；
- 确定下，是不是具体什么时候一定有日志，但是没有出现，没有日志不一定是没有运行；

#### 模拟交易运行时间

#### 延时运行

![yanshi](https://image.joinquant.com/daa36a6b45e302752e3adea5343c465d)

- 为了优化资源配置，非会员及非积分兑换的模拟交易位会在第二天凌晨三点后运行，延时模拟交易不支持微信通知；
- 加入[聚宽会员](https://www.joinquant.com/view/vip/charge)，模拟交易会实时运行；
- 或者使用积分兑换的模拟交易位，模拟交易也会实时运行；[积分兑换](https://www.joinquant.com/view/credits/list)后,再在对应的模拟交易设置页面，将原来的模拟交易位替换成新的模拟交易位即可![tihuan](https://image.joinquant.com/0a45ae7aba261564387064178e33a4fe)
- 加入会员或者替换交易位后立即生效，下一个交易日实时运行

### 投资研究

#### 研究的说明

#### 研究的作用

相较于回测，研究模块提供更大的自由度，您可以更好的验证自己的交易思想。研究模块支持以下功能：

- 每个Cell独立运行，实时查看结果；
- 更好的代码补全；
- 支持自定义库；
- 支持使用matplotlib/seaborn等Python库画各种统计图；
- 支持Markdown和代码混排，可读性更好；
- Notebook支持分享到社区，方便与大家交流。
- 查看[使用帮助](https://www.joinquant.com/research)了解更多信息。
- 支持和回测及模拟交易交互，详情查看API文档 get_backtest和create_backtest。

#### 研究内核的选择

- 在原有 Python2 与 Python 3 内核的基础上， 我们新增加了一个内核， Python2(PacVer 2.0) ，[查看详情](https://www.joinquant.com/post/10330);
- 其中Python2环境和官网回测环境相同，PacVer中的python模块版本相对比较高;
- 建议使用Python2和/或Python3内核。

#### 研究内存、磁盘等不够用怎么办？

- 在[积分商城](https://www.joinquant.com/view/credits/list)使用积分兑换更多资源

#### 上传文件和下载文件是否有限制？

- 最大上传文件20M，下载文件没有大小限制，但由于我们做了限速会慢一些，要耐心；
- 如果要下载的数据比较大，建议使用我们的[JQData](https://www.joinquant.com/help/api/help?name=JQData)

#### 研究和回测中都支持哪些第三方Python库

- [研究和回测中都支持哪些第三方Python库](https://www.joinquant.com/post/10520)
- 云端目前不支持自定义python库

#### 投资研究使用教程

[聚宽新手指南-投资研究使用教程](https://www.joinquant.com/view/community/detail/34426b055bc8600cba6abec85d164ea5)

#### 回测及模拟交易和研究的数据如何交互

- 回测中可以使用[read_file](https://www.joinquant.com/help/api/help?name=api#read_file)/[write_file](https://www.joinquant.com/help/api/help?name=api#write_file)读写研究模块的文件。
 [如何在回测及模拟交易中读取（或写入）研究中不同格式的文件（csv、json等）及数据](https://www.joinquant.com/view/community/detail/19300)
 [在回测及模拟交易中获取研究数据](https://www.joinquant.com/view/community/detail/b048a3e848d190ad810c3930fb07a4dc)
- 研究中可以使用create_backtest创建回测，通过get_backtest获取回测及模拟交易的结果

#### 投资研究打不开的解决方法

- 如果网络正常的话，有可能是文件比较多或者比较大，加载比较慢，稍微等会再看；
- 确定是一个文件打不开，还是所有的问题打不开；一个文件打不开时检查下文件名是不是有特殊字符（&，@，%等）；
- 重启研究环境，在[研究根目录](https://www.joinquant.com/research),右侧点击**重启**按钮；
- 进入[研究服务](https://www.joinquant.com/hub/home),先点击红色"停止服务"，再点击绿色"我的服务"；
- 退出登录，清空浏览器缓存，再次登录；
- 换个浏览器登录，推荐使用Chrome、火狐、edge；
- 文件太多了，清空回收站，然后再删除一些文件；
- 磁盘数据每三小时更新一次（研究文件太多，统计所有研究文件数及大小需要时间及资源），删除三小时后再重启查看；
- 还有问题，请使用官网右下角在线客服系统，联系或者留言技术人员，并提供您的注册手机号；
- 注意：研究环境不要随意安装Python库/模块。
- 如果因为ipynb文件中, 内容输出过多导致页面无法正常加载(个别ipynb打开后无内容但是其他ipynb或者新建的文件可正常打开运行)，可使用以下方法清空ipynb的输出内容建立一个副本:

```python
import json
# 旧notebook文件路径
file_path = 'path_to_your_notebook.ipynb'

# 加载原始.ipynb文件
with open(file_path, 'r', encoding='utf-8') as file:
    notebook = json.load(file)

# 遍历所有单元格并清空code单元格的输出和执行计数
for cell in notebook['cells']:
    if cell['cell_type'] == 'code':
        cell['outputs'] = []
        cell['execution_count'] = None

# 将更新后的notebook保存为新文件
with open(file_path.replace('.ipynb', '_clean.ipynb'), 'w', encoding='utf-8') as file:
    json.dump(notebook, file, ensure_ascii=False, indent=2)
```

#### 查看研究文件大小及数量

在研究文件中运行以下代码，即可查看

```python
import os
from pandas import DataFrame
from collections import defaultdict
import pandas
pandas.set_option('display.max_rows',None)

def list_dir_human(start_path = '.'):
    dir_info_list = []
    first_dir_singel = True
    total_size = 0
    files_number = 0
    # 类型(0-file,1-dir) 大小 子文件数量
    dir_info = defaultdict(list)
    dir_info['.(当前目录)'] = [1, 0, 0]
    for dirpath, dirnames, filenames in os.walk(start_path):
        root_dir = None
        path_url_splited = dirpath.split("/")
        if len(path_url_splited) > 1:
            root_dir = path_url_splited[1]
        else:
            for dir_ in dirnames:
                dir_info[dir_] = [1, 0, 0]
        files_number += 1
        files_number += len(filenames)
        if root_dir:
            dir_info[root_dir][2] += (len(filenames) + 1)
        for f in filenames:
            if os.path.isdir(f):
                print(f)
            fp = os.path.join(dirpath, f)
            if not os.path.islink(fp):
                size_ = os.path.getsize(fp)
                total_size += size_
                if root_dir:
                    dir_info[root_dir][1] += size_
                else:
                    dir_info[f] = [0, size_, -1]
    dir_info['.(当前目录)'][1] = total_size
    dir_info['.(当前目录)'][2] = files_number
    for key, value in dir_info.items():
        dir_info[key].insert(0,key)
        dir_info[key][2] /= (1024*1024)
        dir_info[key][2] = round(dir_info[key][2], 3)
        dir_info_list.append(dir_info[key])
    dir_info_list.sort(key=lambda x:(x[1],x[0]), reverse=True)
    dir_info_list = DataFrame(dir_info_list, columns=['名称', '类型(0-文件，1-目录)', '大小(M)', '文件数量'])
    return dir_info_list

# 参数为相对目录，不可为绝对路径
list_dir_human('.')
```

![img](https://image.joinquant.com/8edbe11386fa4a0751c1f72ca617cb0d)

### 其他第三方库问题

python的第三方库之间往往存在依赖关系，升级或者安装某个第三方库可能会导致其他库不兼容甚至导致研究环境无法正常启动，所以不建议自行安装第三方库。 如果实在有安装第三方库的需求，可以创建个目录，将第三方库安装到此目录中，使用时将此目录加入python环境变量再导入。 **注意:由于研究环境有文件个数不得大于1万的限制，所以安装第三方库需要慎重，不要大肆安装。** 安装命令可以使用:!pip install 库名 --target="/home/jquser/提前建好的目录" --no-dependencies (--no-dependencies <不需要安装的依赖库名> ) 为可选参数, 避免重复安装依赖库) 。 如需要卸载此目录下的第三方库，将对应的文件夹移入到回收站然后删除即可。 使用时，通过以下代码将第三方库添加到环境变量:

```
import sys
sys.path.append( "/home/jquser/提前建好的目录" )
```

#### 研究和回测中都支持哪些第三方Python库

[研究和回测（模拟）中都支持哪些第三方Python库](https://www.joinquant.com/view/community/detail/0b6bcc1ada0ab018f2d7dc2a342cf4ca)

投资研究的使用方法请参考：[投资研究使用教程](https://www.joinquant.com/help/api/help?name=faq#%E6%8A%95%E8%B5%84%E7%A0%94%E7%A9%B6)

#### Pandas常见问题

### Pandas: 如何增加 DataFrame 显示的行、列数？

使用如下代码，更多设置请查看pandas官网教程

```python
import pandas as pd

# 设定最大显示行数、列数为10000
pd.set_option('display.max_rows', 10000)
pd.set_option('display.max_columns', 10000)
pd.set_option('display.width', 10000)
```

### Pandas: object has no attribute sort_values

原因：Pandas的没有sort_values这个方法；不同环境的Pandas版本不同，不同版本Pandas的排序方法不同。

解决方法：您可以查看下您使用环境中Pandas的版本，并使用对应的排序方法。具体使用方法请参考Pandas的教程。

一般的，Pandas早期版本的排序方法是sort，新版本的排序方法为sort_values。
 [sort的使用方法](http://pandas.pydata.org/pandas-docs/version/0.17.0/generated/pandas.DataFrame.sort.html)
 [sort_values的使用方法](http://pandas.pydata.org/pandas-docs/stable/generated/pandas.DataFrame.sort_values.html)

ascending=False为降序排列，即最大值在最前面；默认为升序排列

早期版本的排序order，sort
 years_pct_sum[year].order(ascending=False)
 data.sort('change_pct', ascending=False)

新版本的排序sort_values
 year_pct_sum_sort = years_pct_sum[year].sort_values(ascending=False)
 data.sort_values(by='date')

#### numpy.float64 浮点数的展示问题

有同学问到, 聚宽的数据是不是有问题, 怎么价格还带那么多位小数. 其实并不是我们数据的问题, 是numpy.float64 展示数据的问题.我们的价格是 numpy.float64 对象存储的, numpy.float64 展示的时候跟我们想象的不一样.
 stackoverflow上的答案: [点击这里](http://stackoverflow.com/questions/27098529/numpy-float64-vs-python-float)
 详情可以查看：[点击这里](https://www.joinquant.com/post/754)

#### 忽略或屏蔽提示及警告

```python
import warnings
warnings.filterwarnings("ignore")
```

#### matplotlib中文显示

绘图使用到中文需要设置一下中文字体:

```python
import matplotlib as mpl
mpl.rcParams['font.family']='serif'
mpl.rcParams['font.serif']='Droid Sans Fallback'
plt.rcParams['axes.unicode_minus']=False # 用来正常显示负号
```

#### mpl_finance

下载或者复制粘贴mpl_finance.py，
 https://github.com/matplotlib/mpl-finance/blob/master/mpl_finance.py
 然后上传到研究中即可使用

```python
import warnings
warnings.filterwarnings("ignore")
import mpl_finance
```

mpl_finance的使用方法请自己在网上搜相关教程；
 投资研究的使用方法请参考：[投资研究使用教程](https://www.joinquant.com/help/api/help?name=faq#%E6%8A%95%E8%B5%84%E7%A0%94%E7%A9%B6)

#### 已知的第三方库中的bug

官网使用的第三方库需要兼容系统和用户自身的代码，所以一般不会对第三方库进行升级，容易引起兼容问题。这里对已知的第三方库中存在的bug进行整理。

1. pandas的shift(…., axis=1)在数据集含有nan值时存在异常(同时存在于研究、回测中) 问题复现代码:

```py
import pandas as pd
df = pd.DataFrame([[1,2,3],
                   [1,2,3],
                   [1,2,np.nan]])
print(df.shift(periods= 1,axis=1))
```

这个问题很容易复现，所以建议不要指定axis参数, 尽量使用转置后shift再重新转置的方法进行处理，如上述代码可以变更为:

```py
import pandas as pd
df = pd.DataFrame([[1,2,3],
                   [1,2,3],
                   [1,2,np.nan]])
print(df.T.shift(periods= 1).T)
```

#### 研究中安装第三方库

python的第三方库之间往往存在依赖关系，升级或者安装某个第三方库可能会导致其他库不兼容甚至导致研究环境无法正常启动，所以不建议自行安装第三方库。
 如果实在有安装第三方库的需求，可以创建个目录，将第三方库安装到此目录中，使用时将此目录加入python环境变量再导入。
 **注意:由于研究环境有文件个数不得大于1万的限制，所以安装第三方库需要慎重，不要大肆安装。**
 安装命令可以使用: `!pip install 库名 --target="/home/jquser/提前建好的目录" --no-dependencies` (--no-dependencies <不需要安装的依赖库名> ) 为可选参数, 避免重复安装依赖库) 。
 如需要卸载此目录下的第三方库，将对应的文件夹移入到回收站然后删除即可。
 使用时，通过以下代码将第三方库添加到环境变量:

```
import sys
sys.path.append( "/home/jquser/提前建好的目录" )
import 库名
```

### 聚宽VIP说明

#### 客户服务

聚宽技术支持人员对平台常用功能的答疑，包括平台功能使用、需求及问题反馈等。免费用户只可通过留言的方式进行沟通。
 注意: `服务不包含代写策略、策略答疑、策略分析等`，具体的策略需要您自己实现及检查。

#### 平台资源

**免费回测时间：** 指每个自然日内，用户可以免费编译运行、回测的最长时间。超出后，每运行30分钟需消耗2积分。`积分小于等于0时，用户将无法新建编译运行和回测。`

**最大并行回测：** 指同时运行回测的数量上限。您也可以使用积分进行兑换。

#### 积分优惠

**导出回测结果：** 导出回测交易详情、持仓&收益、日志时，分别需要消耗3积分/次。已经消耗过积分的，下次可以直接导出。

**社区克隆策略/查看策略源码、克隆研究：** 在社区进行上述操作时，需要消耗10积分/次。已经消耗过积分的，下次可以直接克隆。每个用户每天克隆策略/查看策略源码、克隆研究的上限分别都为100次。
 注意：`积分小于等于0时，用户将无法享受上述积分优惠。`

#### 高级功能

**Tick级回测、模拟交易：** VIP、SVIP可以选择使用Tick级数据频率进行回测和模拟交易，普通用户仅能选择天和分钟级数据频率。

**模拟交易实时运行：** VIP和SVIP用户的全部模拟交易位、普通用户购买的限时模拟交易位，可以在交易时间实时运行。普通用户时限为永久的模拟交易，将在次日凌晨的空闲时间延时运行。

**调仓信号优先推送：** 交易拥堵时段会优先运行VIP、SVIP的模拟交易，从而能够更快的收到交易信号推送。

#### 更多专属功能即将上线

#### VIP会员更多问题

- 是否可以开发票？
 如果要开发票请提前咨询小秘书（微信：JQhelper）后再支付
- VIP会员和JQData的数据是什么关系，购买会员后下载数据条数没有变化？
 没有关系的，聚宽官网的VIP会员主要是官网的回测和模拟交易等功能，不包含本地下载数据条数的；
 如果需要购买JQData数据，请查看[JQData文档](https://www.joinquant.com/help/api/doc?name=logon&id=9830)；
 如果误买的话，也可以联系小秘书申请退订。
- 加入会员后模拟交易仍然没有实时运行？
 模拟交易是否实时运行在每天凌晨三点判断一次，三点前成为会员的，下一个交易日实时运行。
- 有关VIP升级SVIP
 SVIP的时限是根据VIP的剩余时限转换的
- 有关会员时间
 月付按照每月30天计算，年付按照每年365天计算

### 实盘说明

**聚宽目前没有提供任何形式的实盘及交易通道服务。**
