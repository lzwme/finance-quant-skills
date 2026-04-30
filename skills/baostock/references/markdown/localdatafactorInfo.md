## 利用本地Baostock日K线数据手动计算复权价格

在量化策略回测中，复权数据是保证价格连续性的基础。为避免频繁请求BaoStock API，可通过BaoStock复权因子(<a href="factorInfo.md">BaoStock复权因子获取方法见：query_adjust_factor()</a>)与本地存储的原始日K线数据(<a href="stockKData.md">日K线获取方法见：query_history_k_data_plus()</a>)自行计算复权价格（分钟线同理）。[媒体文件:利用BaoStock本地日K线数据手动计算复权价格.pdf](https://www.baostock.com/helpdocs/pdf/BaoStock前复权日K线数据计算简介.pdf)
本文以浦发银行（sh.600000）为例，展示 2014-01-01 至 2020-01-01 区间内，基于BaoStock复权因子计算前复权日 K 线的完整流程（后复权方法类似）。

```python
import baostock as bs
import pandas as pd

# 初始化baostock
lg = bs.login()

# 定义股票代码和时间范围
stock_code = "sh.600000"  # 浦发银行
start_date = "2014-01-01"
end_date = "2020-01-01"

# 1. 获取非复权日K线数据
print("\n1. 获取非复权日K线数据...")

# "sh600000_from_baostock.csv"是从baostock下载到本地的日K线数据(时间：2014-01-01到2020-01-01)
# "sh600000_from_baostock.csv"包含如下数据：date,open,high,low,close,volume
baostock_file_path = "sh600000_from_baostock.csv"
kline_df = pd.read_csv(baostock_file_path)
print(f"获取到 {len(kline_df)} 条非复权日K线数据")

# 转换数据类型
kline_df["open"] = kline_df["open"].astype(float)
kline_df["high"] = kline_df["high"].astype(float)
kline_df["low"] = kline_df["low"].astype(float)
kline_df["close"] = kline_df["close"].astype(float)
kline_df["volume"] = kline_df["volume"].astype(float)
kline_df['date'] = pd.to_datetime(kline_df['date'])

# 2. 获取复权因子数据
print("\n2. 获取复权因子数据...")
# 注意：需要获取更早的复权因子，因为前复权需要用到整个历史区间的因子
factor_start = "2010-01-01"  # 扩大到2010年
factor_end = end_date

adjust_factor_data = bs.query_adjust_factor(
	stock_code,
	start_date=factor_start,
	end_date=factor_end
)

adjust_factor_df = adjust_factor_data.get_data()
print(f"获取到 {len(adjust_factor_df)} 条复权因子数据")
print(adjust_factor_df[['dividOperateDate', 'foreAdjustFactor']])

# 转换数据类型
adjust_factor_df['dividOperateDate'] = pd.to_datetime(adjust_factor_df['dividOperateDate'])
adjust_factor_df['foreAdjustFactor'] = adjust_factor_df['foreAdjustFactor'].astype(float)
adjust_factor_df = adjust_factor_df.sort_values('dividOperateDate')

# 3. 正确的复权计算方法
print("\n3. 计算前复权数据...")

# 创建复权因子查找函数
def get_factor_for_date(trade_date):
	"""
	查找小于等于交易日期的最接近的复权因子
	"""
	mask = adjust_factor_df['dividOperateDate'] <= trade_date
	if mask.any():
		return adjust_factor_df.loc[mask, 'foreAdjustFactor'].iloc[-1]
	else:
		# 如果没有找到，返回最新的复权因子（用于前复权）
		if not adjust_factor_df.empty:
			return adjust_factor_df['foreAdjustFactor'].iloc[-1]
		return 1.0

# 为每个交易日查找对应的复权因子
print("正在为每个交易日匹配复权因子...")
kline_df['adj_factor'] = kline_df['date'].apply(get_factor_for_date)

# 正确计算前复权数据：原始价格 / 复权因子
kline_df["adj_open"] = kline_df["open"] * kline_df["adj_factor"]
kline_df["adj_high"] = kline_df["high"] * kline_df["adj_factor"]
kline_df["adj_low"] = kline_df["low"] * kline_df["adj_factor"]
kline_df["adj_close"] = kline_df["close"] * kline_df["adj_factor"]

print("\n计算完成，复权后的数据：")
print(kline_df[['date', 'open', 'adj_open', 'close', 'adj_close', 'adj_factor']].head(10))

# 保存数据（可选）
kline_df.to_csv("sh600000_calculated.csv", index=False, float_format='%.6f')
print("\n数据已保存到CSV文件")

# 退出baostock
bs.logout()
```