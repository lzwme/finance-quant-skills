# AWESOME QUANT

## 金融机构量化交易平台

- [QMT迅投知识库](https://dict.thinktrader.net) 与券商合作最多的量化交易平台。部分券商提供 miniQMT 支持，让高质量数据获取、策略回测与交易等均能以编码的形式简单便捷的关联执行。
- [JoinQuant 聚宽社区](https://www.joinquant.com) 社区较为活跃，基于积分机制鼓励策略分享与交流。
- [东方财富-妙想](https://ai.eastmoney.com)

## 金融数据获取

### 免费数据源

- [AKShare](https://akshare.akfamily.xyz) 基于 Python 的开源财经数据接口库。通过采集权威财经数据网站公开的原始数据进行交叉验证，进而再加工，从而得出科学的数据或结论。
- [baostock](https://www.baostock.com) 专为中国股市数据提供支持的Python库，用户可以通过它无需登录获取免费的股票、指数、基金等金融数据。
- [jqdatasdk](https://github.com/JoinQuant/jqdatasdk) 聚宽数据，简单易用的量化金融数据包。
- [tdxquant](https://help.tdx.com.cn/quant/) TdxQuant 是一套基于通达信金融终端构建的 Python 量化策略运行框架。该框架通过 API 接口形式，为策略交易提供所需的行情数据获取与交易指令执行功能。
- [chenditc/investment_data](https://github.com/chenditc/investment_data) 基于 tushare 等数据源提供适用于 [QLib](https://github.com/microsoft/qlib) 的高质量日线行情数据。通过定时任务每日生成数据，并通过 github release 发布 (约在 19:10)。
- [pytdx](https://rainx.gitbooks.io/pytdx/content/) 第三方封装的通达信 Python API。最近更新是 2019 年。当前内置的 IP 基本已失效，需自行测试获取可用的行情服务器 IP。
- [mootdx](https://github.com/mootdx/mootdx)基于 pytdx 二次封装的第三方库，旨在于简化数据获取。
- [tdx-api](https://github.com/oficcejo/tdx-api) 第三方开发的tdx通达信实时数据查询及api接口，支持docker本地部署，支持32个接口
- [XtQuant/miniqmt](https://dict.thinktrader.net/nativeApi/start_now.html?id=1L5eYT) XtQuant是基于迅投MiniQMT衍生出来的一套完善的Python策略运行框架，对外以Python库的形式提供策略交易所需要的行情和交易相关的API接口。需要购买，或使用QMT券商版并且支持 miniQMT
- [efinance](https://github.com/Micro-sheep/efinance) 一个可以快速获取基金、股票、债券、期货数据的 Python 库。**通过模拟浏览器形式访问东方财富网站API的数据。可能存在稳定性问题。**
- [yfinance](https://github.com/ranaroussi/yfinance) Yahoo Finance 雅虎财经数据API。**需科学访问。**

### 付费/门槛数据源

- [tushare](https://tushare.pro) 提供股票、期货、期权、港股、美股、加密货币等数据。**付费积分模式，不同等级积分权限不同。免费用户可访问日线行情。**
- [INSIGHT](https://findata-insight.htsc.com:9151/insight_help/) INSIGHT是华泰证券依托大数据存储、实时分析等领域的技术积累，整合接入国内多家交易所高频行情数据，为投资者提供集行情接入、推送、回测、计算及分析等功能于一体的行情数据服务解决方案。需要有 INSIGHT 经纪账户。
- [米筐 RQData](https://www.ricequant.com/doc/rqdata/python/manual)  RQData 是米筐提供的一个基于 Python 的金融数据工具包。个人可申请免费使用，企业版支持付费私有化部署服务端。
- [同花顺iFinD](https://ft.10jqka.com.cn)
- [天勤TQSDK](https://www.shinnytech.com/products/tqsdk)
- 万得Wind
- 天软 Tinysoft


## 量化交易策略框架

- [vnpy](https://github.com/vnpy/vnpy) 基于Python的开源量化交易平台开发框架
- [AKQuant](https://akquant.akfamily.xyz) akshare作者开发的开源量化投研框架。一款专为 量化投研 (Quantitative Research) 打造的 高性能混合架构引擎。它以 Rust 铸造极速撮合内核，以 Python 链接数据与 AI 生态，旨在为量化投资者提供可靠高效的解决方案。
- [QUANTAXIS](https://github.com/yutiansut/QUANTAXIS) 支持任务调度 分布式部署的 股票/期货/期权 数据/回测/模拟/交易/可视化/多账户 纯本地量化解决方案
- [bullet-trade](https://github.com/BulletTrade/bullet-trade) BulletTrade 是一个专业的量化交易系统 Python 包，提供完整的回测和实盘交易解决方案。完全兼容聚宽策略直接执行。
- [ricequant/rqalpha](https://github.com/ricequant/rqalpha) 米筐 RQAlpha 从数据获取、算法交易、回测引擎，实盘模拟，实盘交易到数据分析，为程序化交易者提供了全套解决方案。**仅限非商业使用。**
- [Backtrader](https://www.backtrader.com) 一个强大的开源Python量化回测框架，支持多数据源、多策略、多周期回测与实盘交易。纯Python实现，无外部依赖，架构清晰且易于扩展。但已多年未更新。
- [zvtvz/zvt](https://github.com/zvtvz/zvt/blob/master/README-cn.md) 模块化的量化框架。ZVT希望提供一个简单的工具来构建直白的算法。
- [hftbacktest](https://github.com/nkaz001/hftbacktest) 一个专业的高频交易回测工具，能够精准模拟限价订单、队列位置和延迟因素，利用完整的订单簿和交易数据为高频交易策略提供可靠的回测支持。虚拟货币交易机器人。
- [vectorbt](https://github.com/polakowo/vectorbt) 一个高性能极速回测框架。用矩阵思考、大规模回测：它不再一次只用一个策略循环，而是将数千个配置打包进NumPy数组，加速Numba和Rust的热路径，并一次性运行，将数小时的网格搜索变成几秒钟。

## 量化工具与研究

- [waditu/czsc](https://github.com/waditu/czsc) 缠中说禅技术分析工具；缠论；股票；期货；Quant；量化交易
- [hugo2046/QuantsPlaybook](https://github.com/hugo2046/QuantsPlaybook) 利用python对国内各大券商的金工研报进行复现



## 策略分享

- [fmzquant/strategies](https://github.com/fmzquant/strategies) quantitative trading with Javascript, Python, C++, PineScript, Blockly, MyLanguage
- [Quant-Strategy](https://github.com/JizhiXiang/Quant-Strategy) 一个量化代码合集，以qmt、okx、聚宽为主
- [asmcos/quantrader](https://github.com/asmcos/quantrader) quantrader是基于backtrack框架的回测系统，包含常见的macd，二八动量等。 希望收集各种常见的交易策略算法，供各网友学习，交流。

## 量化资源索引

[wilsonfreitas/awesome-quant](https://github.com/wilsonfreitas/awesome-quant) 一份精选的量化金融超棒图书馆、软件包和资源清单
- [thuquant/awesome-quant](https://github.com/thuquant/awesome-quant) 中国的 Quant 相关资源索引
- [best-of-algorithmic-trading](https://github.com/merovinh/best-of-algorithmic-trading) 算法交易精选
：算法交易开源库、框架、机器人、工具、书籍、社区、教育材料的排名列表。每周更新。

## AI 量化相关

### AI 因子挖掘

- [QLib](https://github.com/microsoft/qlib) 微软开源的一个面向人工智能的量化投资平台，旨在利用人工智能技术赋能量化研究，从探索创意到实施生产。Qlib支持多样化的机器学习建模范式，包括监督学习、市场动态建模和强化学习。
- [RD-Agent](https://github.com/microsoft/RD-Agent) 基于大型语言模型的自主进化智能体，以数据为中心、多代理的框架，旨在通过协调因子-模型协同优化，自动化工业研发流程中最关键和最有价值的环节。
- [QuantaAlpha](https://github.com/QuantaAlpha/QuantaAlpha) LLM 驱动的自进化因子挖掘框架。QuantaAlpha 将大语言模型（LLM）与进化策略结合，通过自进化轨迹自动完成量化 Alpha 因子的挖掘、进化与验证。你只需输入研究方向，其余流程将自动运行。
- [FactorHub](https://github.com/cn-vhql/FactorHub) 个开源的现代化量化因子分析平台，专为中国A股市场设计。

### AI 交易相关

- [qlibAssistant](https://github.com/touhoufan2024/qlibAssistant) qlib助手, 每日自动预测a股
- [TradingAgents](https://github.com/TauricResearch/TradingAgents) 一个基于多智能体 LLM 的金融交易框架，通过模拟专业交易团队的协作机制，实现智能化的投资决策。将复杂的投资决策分解为多个专业角色的协作过程，每个智能体负责特定的分析维度，最终通过集体讨论形成交易决策。
- [TradingAgents-CN](https://github.com/hsliuping/TradingAgents-CN) TradingAgents 中文增强版，面向中国 A 股交易设计。其 v2.0 版本未开源。
- [Dzy-HW-XD/a-share-quant-selector](https://github.com/Dzy-HW-XD/a-share-quant-selector) A股量化选股系统 - 基于碗口反弹策略的智能选股工具，支持Web界面和钉钉通知
- [oficcejo/aiagents-stock](https://github.com/oficcejo/aiagents-stock) 复合多AI智能体股票团队分析盯盘系统，基于多个ai智能体，模拟证券分析师团队分析过程，提供全方位的股票投资分析和决策建议，新增游资龙虎榜跟踪分析、板块预警轮动分析，支持批量多线程分析，支持实时监测关键点位，发送警报信息，预留miniqmt接口，支持量化交易，真正做到了ai帮你来炒股，适合大陆A股。
- [Evan-XYZ/YMOS](https://github.com/Evan-XYZ/YMOS) YMOS 是一个面向独立投资者的人机协作投研系统：帮你从投研的重复劳动中解放出来——数据收集、信号追踪、报告生成交给 AI， 你专注于三件最重要的事：优化投资策略 、 做深度调研和关键判断。
- [facecat-kronos](https://github.com/Fidingks/facecat-kronos) 由 花卷猫量化研究团队 打造的一款金融量化工具。本项目基于清华大学最新开源的K线预测模型 Kronos，融合了前沿的人工智能技术，旨在为金融市场提供科学的分析与预测能力。 本工具能够对股票历史数据进行深度预训练，实现精准的做市商K线规划，并对未来市场走势进行科学推演，适用于量化研究、策略研发、交易决策支持、投研汇报、教学演示、二次开发。
- [virattt/ai-hedge-fund](https://github.com/virattt/ai-hedge-fund) 一个人工智能驱动的对冲基金的概念验证。该项目的目标是探索利用人工智能来做出交易决策。本项目仅供教育用途，不适用于真实交易或投资。
- [FinRL-Trading](https://github.com/AI4Finance-Foundation/FinRL-Trading) 一个AI原生的定量交易模块化基础设施。FinRL-X 是一款下一代、基于人工智能的量化交易基础设施，重新定义了研究人员和从业者构建、测试和部署算法交易策略的方式。
