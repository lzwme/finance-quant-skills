---
url: "https://dict.thinktrader.net/nativeApi/start_now.html"
title: "快速开始 | 迅投知识库"
---

### XtQuant 能提供哪些服务

XtQuant是基于迅投MiniQMT衍生出来的一套完善的Python策略运行框架，对外以Python库的形式提供策略交易所需要的行情和交易相关的API接口。

### XtQuant 运行依赖环境

XtQuant 目前提供的库包括 64 位 Python `3.6`、`3.7`、`3.8`、`3.9`、`3.10`、`3.11`、`3.12`版本，不同版本的 Python 导入时会自动切换。 在运行使用 XtQuant 的程序前需要先启动 MiniQMT 客户端。

### XtQuant 运行逻辑

**Xtdata** 作为行情模块，本模块旨在提供精简直接的数据满足量化交易者的数据需求，主要提供行情数据（历史和实时的K线和分笔）、财务数据、合约基础信息、板块和行业分类信息等通用的行情数据。

**Xttrader** 作为交易模块，封装了策略交易所需要的 Python API 接口，可以和 MiniQMT 客户端交互进行报单、撤单、查询资产、查询委托、查询成交、查询持仓以及接收资金、委托、成交和持仓等变动的主推消息。