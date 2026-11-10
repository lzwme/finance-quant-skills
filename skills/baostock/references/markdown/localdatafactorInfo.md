## 目录

* [1 利用本地Baostock日K线数据手动计算复权价格](#利用本地Baostock日K线数据手动计算复权价格)
  + [1.1 第一步：环境的准备](#第一步环境的准备)
  + [1.2 第二步：下载历史A股日K线数据](#第二步下载历史A股日K线数据)
  + [1.3 第三步：下载每日新增的日K线数据](#第三步下载每日新增的日K线数据)
  + [1.4 第四步：下载历史复权因子数据](#第四步下载历史复权因子数据)
  + [1.5 第五步：下载每日新增的复权因子数据](#第五步下载每日新增的复权因子数据)
  + [1.6 第六步：计算复权数据](#第六步计算复权数据)

## 利用本地Baostock日K线数据手动计算复权价格

在量化策略回测中，复权数据是保证价格连续性的基础。为避免频繁请求BaoStock API，可通过BaoStock复权因子(<a href="factorInfo.md">BaoStock复权因子获取方法见：query_adjust_factor()</a>)与本地存储的原始日K线数据(<a href="stockKData.md">日K线获取方法见：query_history_k_data_plus()</a>)自行计算复权价格（分钟线同理）。
本次示例代码既有历史A股K线数据的下载和存储，也有每日新增A股K线数据和复权数据的下载和存储。

### 第一步：环境的准备

Python及其依赖包的安装
在本文的代码示例里，Python版本是python 3.9.13。依赖包有：pandas和baostock. 这两个依赖包的安装请查看BaoStock官网网页：(<a href="home.md">Baostock知识库</a>)
在安装好了python及其依赖包后，运行代码出现如下错误（或找不到baostock官方提供的接口方法），请考虑升级baostock的版本。

### 第二步：下载历史A股日K线数据

利用 Baostock 接口 query_daily_history_k_AStock() 下载历史 A 股日 K 线数据。您可修改下方 `start_date`和 `end_date`变量获取任意历史日期数据。数据以 CSV 格式保存，按年份归档于 D:\baostock_data\ 目录下。

```python
# -*- coding: utf-8 -*-
import baostock as bs
import pandas as pd
import datetime
import os

# ---------- 可配置参数 ----------
# 数据存储根目录，可按需修改
root_dir = r"D:\baostock_data"

# 设置起始日期和结束日期（字符串格式 "YYYY-MM-DD"）
start_date = "2026-07-01"    # 起始日期
end_date = "2026-07-13"      # 结束日期（包含）

print(f"下载日期范围: {start_date} 至 {end_date}")
# --------------------------------

#### 登录baostock系统（一次性登录，循环复用） ####
lg = bs.login()
if lg.error_code != '0':
    print(f"登录失败: {lg.error_msg}")
    exit()
print("登录成功")

# 设置 pandas 显示选项（可选）
pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
pd.set_option('display.width', 1000)

#### 1. 获取指定日期范围内的所有交易日 ####
print("\n正在获取交易日列表...")
trade_dates_rs = bs.query_trade_dates(start_date=start_date, end_date=end_date)
if trade_dates_rs.error_code != '0':
    print(f"获取交易日失败: {trade_dates_rs.error_msg}")
    bs.logout()
    exit()

trade_date_list = []
while trade_dates_rs.next():
    row = trade_dates_rs.get_row_data()
    # row: [calendarDate, isTradingDay]  isTradingDay="1" 表示交易日
    if row[1] == "1":
        trade_date_list.append(row[0])

print(f"共获取到 {len(trade_date_list)} 个交易日")
if not trade_date_list:
    print("无交易日，程序退出")
    bs.logout()
    exit()

#### 2. 循环每个交易日下载K线数据 ####
success_count = 0
total_days = len(trade_date_list)

for idx, date_str in enumerate(trade_date_list, 1):
    print(f"\n[进度 {idx}/{total_days}] 正在处理: {date_str}")

    # 构建存储路径（按年份归档）
    year = date_str[:4]
    year_dir = os.path.join(root_dir, year)
    os.makedirs(year_dir, exist_ok=True)
    filepath = os.path.join(year_dir, f"{date_str}_k_AStock_data.csv")

    # 查询该交易日数据
    rs = bs.query_daily_history_k_AStock(date=date_str)
    if rs.error_code != '0':
        print(f"  查询失败: {rs.error_msg}")
        continue

    # 提取数据
    data_list = []
    while rs.next():
        data_list.append(rs.get_row_data())

    if not data_list:
        # 理论上交易日应该有数据，但以防万一
        print(f"  警告：日期 {date_str} 无数据，可能为空")
        continue

    # 转换为 DataFrame 并保存
    result = pd.DataFrame(data_list, columns=rs.fields)
    result.to_csv(filepath, encoding="gbk", index=False)
    print(f"  [成功] 保存 {len(result)} 条记录至 {filepath}")
    success_count += 1

print(f"\n全部处理完成！共 {total_days} 个交易日，成功下载 {success_count} 天的数据。")

#### 登出系统 ####
bs.logout()
print("已登出")
```

### 第三步：下载每日新增的日K线数据

利用 Baostock 接口 query_daily_history_k_AStock() 下载 A 股日 K 线数据。默认下载当天数据，您可修改下方 `current_date` 变量获取任意历史日期数据。数据以 CSV 格式保存，按年份归档于 D:\baostock_data\ 目录下。
```python
# -*- coding: utf-8 -*-
import baostock as bs
import pandas as pd
import datetime
import os

# ---------- 可配置参数 ----------
# 获取当天日期
today = datetime.date.today().strftime("%Y-%m-%d")
print("today : " + today)

# 数据存储根目录，可按需修改
root_dir = r"D:\baostock_data"
# --------------------------------

current_date = today        # 默认当天，可改为 "2026-07-10" 等任意日期，下载历史数据
year = current_date[:4]     # 年份
year_dir = os.path.join(root_dir, year)
os.makedirs(year_dir, exist_ok=True)

filepath = os.path.join(year_dir, f"{current_date}_k_AStock_data.csv")

print(f"[信息] 目标日期: {current_date}")
print(f"[信息] 数据文件将保存至: {filepath}")

#### 登陆baostock系统 ####
lg = bs.login()
print('login respond error_code:'+lg.error_code)
print('login respond  error_msg:'+lg.error_msg)

#### 获取当天所有股票日K线数据 ####
rs = bs.query_daily_history_k_AStock(date=current_date)
pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
pd.set_option('display.width', 1000)
print('query_daily_history_k_AStock respond error_code:'+rs.error_code)
print('query_daily_history_k_AStock respond  error_msg:'+rs.error_msg)

#### 打印结果集 ####
data_list = []
while (rs.error_code == '0') & rs.next():
    data_list.append(rs.get_row_data())
result = pd.DataFrame(data_list, columns=rs.fields)

print(f"成功下载了{current_date}的日K线数据, 总共记录数目:{len(data_list)}")

#### 结果集输出到csv文件 ####
result.to_csv(filepath, encoding="gbk", index=False)

print(f"成功下载了{current_date}的日K线数据存储到目录:{filepath}")

#### 登出系统 ####
bs.logout()
```

### 第四步：下载历史复权因子数据

利用 Baostock 接口 query_daily_adjust_factor 获取起止日期的除权股票列表，对这些股票拉取全部历史复权因子（从1990年至今）。
默认下载当天数据，可修改主程序中的 `end_date` 变量获取任意历史日期。最终文件保存至 D:\baostock_data\stock_adjust_factor_data.csv。

```python
# -*- coding: utf-8 -*-
import baostock as bs
import pandas as pd
import datetime
import os
import sys

# ---------- 可配置参数 ----------
# 数据存储根目录，可按需修改
root_dir = r"D:\baostock_data"

# 起始日期（从该日期开始扫描除权股票）
start_date = "2026-01-01"

# 数据起始时间（沪深交易所首日）
history_start_date = "1990-12-19"

# 结束日期默认为当天
today = datetime.date.today().strftime("%Y-%m-%d")
end_date = today
# --------------------------------

# 设置 pandas 显示选项
pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
pd.set_option('display.width', 1000)

print(f"扫描除权股票的起始日期: {start_date}")
print(f"复权因子数据下载范围: {history_start_date} 至 {end_date}")

# 确保根目录存在
os.makedirs(root_dir, exist_ok=True)
file_path = os.path.join(root_dir, "stock_adjust_factor_data.csv")
print(f"[信息] 数据文件将保存至: {file_path}")

# ---------- 1. 登录 Baostock ----------
lg = bs.login()
if lg.error_code != '0':
    print(f"登录失败: {lg.error_msg}")
    sys.exit()
print("登录成功")

# ---------- 2. 获取指定日期范围内的所有交易日 ----------
print("\n正在获取交易日列表...")
trade_dates_rs = bs.query_trade_dates(start_date=start_date, end_date=end_date)
if trade_dates_rs.error_code != '0':
    print(f"获取交易日失败: {trade_dates_rs.error_msg}")
    bs.logout()
    sys.exit()

trade_date_list = []
while trade_dates_rs.next():
    row = trade_dates_rs.get_row_data()
    # row: [calendarDate, isTradingDay]  isTradingDay="1" 表示交易日
    if row[1] == "1":
        trade_date_list.append(row[0])

print(f"共获取到 {len(trade_date_list)} 个交易日")
if not trade_date_list:
    print("无交易日，程序退出")
    bs.logout()
    sys.exit()

# ---------- 3. 扫描每个交易日，收集所有发生除权的股票代码 ----------
print("\n开始扫描每个交易日的除权股票...")
codes_set = set()  # 使用集合去重
total_days = len(trade_date_list)

for idx, date_str in enumerate(trade_date_list, 1):
    try:
        rs_factor = bs.query_daily_adjust_factor(date=date_str)
        if rs_factor.error_code != '0':
            print(f"  [{idx}/{total_days}] {date_str} 查询失败: {rs_factor.error_msg}")
            continue

        day_codes = []
        while (rs_factor.error_code == '0') and rs_factor.next():
            row = rs_factor.get_row_data()
            day_codes.append(row[0])  # 第一列是 code

        if day_codes:
            codes_set.update(day_codes)
            print(f"  [{idx}/{total_days}] {date_str} 有 {len(day_codes)} 只股票除权（累计去重: {len(codes_set)}）")
        else:
            print(f"  [{idx}/{total_days}] {date_str} 无除权股票")
    except Exception as e:
        print(f"  [{idx}/{total_days}] {date_str} 扫描异常: {e}")

print(f"\n扫描完成，共发现 {len(codes_set)} 只不重复的除权股票")

if not codes_set:
    print("未发现任何除权股票，程序退出")
    bs.logout()
    sys.exit()

codes_list = sorted(codes_set)

# ---------- 4. 批量拉取这些股票的全部历史复权因子 ----------
print("\n开始批量拉取历史复权因子数据...")
all_data = []
total_codes = len(codes_list)

for idx, code in enumerate(codes_list, 1):
    try:
        rs = bs.query_adjust_factor(code=code, start_date=history_start_date, end_date=end_date)
        if rs.error_code != '0':
            print(f"  [{idx}/{total_codes}] {code} 查询失败: {rs.error_msg}")
            continue

        data_list = []
        while (rs.error_code == '0') and rs.next():
            data_list.append(rs.get_row_data())

        if data_list:
            df_code = pd.DataFrame(data_list, columns=rs.fields)
            # 只保留需要的字段（不包含 adjustFactor）
            df_code = df_code[['code', 'dividOperateDate', 'foreAdjustFactor', 'backAdjustFactor']]
            all_data.append(df_code)
            print(f"  [{idx}/{total_codes}] {code} 获取 {len(df_code)} 条因子记录")
        else:
            print(f"  [{idx}/{total_codes}] {code} 无历史因子数据")
    except Exception as e:
        print(f"  [{idx}/{total_codes}] {code} 拉取异常: {e}")

bs.logout()
print("已登出 Baostock")

if not all_data:
    print("未获取到任何复权因子数据，程序退出")
    sys.exit()

# ---------- 5. 合并、转换数据类型 ----------
print("\n合并数据...")
combined_df = pd.concat(all_data, ignore_index=True)
combined_df['dividOperateDate'] = pd.to_datetime(combined_df['dividOperateDate'])
combined_df['foreAdjustFactor'] = pd.to_numeric(combined_df['foreAdjustFactor'], errors='coerce')
combined_df['backAdjustFactor'] = pd.to_numeric(combined_df['backAdjustFactor'], errors='coerce')

# 去重（按 code 和 dividOperateDate）
before_dedup = len(combined_df)
combined_df = combined_df.drop_duplicates(subset=['code', 'dividOperateDate'])
print(f"去重前 {before_dedup} 条，去重后 {len(combined_df)} 条")

# 排序
combined_df = combined_df.sort_values(['code', 'dividOperateDate']).reset_index(drop=True)

# 保留6位小数
combined_df['foreAdjustFactor'] = combined_df['foreAdjustFactor'].round(6)
combined_df['backAdjustFactor'] = combined_df['backAdjustFactor'].round(6)

# ---------- 6. 保存到 CSV ----------
try:
    combined_df.to_csv(file_path, index=False, encoding='gbk')
    print(f"\n复权因子数据下载完成！")
    print(f"文件保存至: {file_path}")
    print(f"共 {len(combined_df)} 条记录，涉及 {combined_df['code'].nunique()} 只股票")
    print(f"日期范围: {combined_df['dividOperateDate'].min().strftime('%Y-%m-%d')} 至 {combined_df['dividOperateDate'].max().strftime('%Y-%m-%d')}")
except PermissionError:
    print(f"\n[错误] 文件 {file_path} 被占用，请关闭该文件后重试")
    sys.exit(1)
except Exception as e:
    print(f"\n[错误] 保存文件失败: {e}")
    sys.exit(1)
```

### 第五步：下载每日新增的复权因子数据

利用 Baostock 接口 query_daily_adjust_factor 获取当日除权股票列表，
并针对这些股票拉取全部历史复权因子（从1990年至今），覆盖本地文件中的旧记录，其他股票保持不变。
默认下载当天数据，可修改主程序中的 `current_date` 变量获取任意历史日期。最终文件保存至 D:\baostock_data\stock_adjust_factor_data.csv。

```python
# -*- coding: utf-8 -*-
import sys
import baostock as bs
import pandas as pd
import datetime
import os

# ---------- 可配置参数 ----------
# 获取当天日期
today = datetime.date.today().strftime("%Y-%m-%d")
print("today : " + today)

# 数据存储根目录，可按需修改
root_dir = r"D:\baostock_data"
# --------------------------------

current_date = "2026-08-14"        # 默认当天，可改为 "2026-07-10" 等任意日期，下载历史数据

os.makedirs(root_dir, exist_ok=True)          # 确保目录存在
file_path = os.path.join(root_dir, "stock_adjust_factor_data.csv")

print(f"[信息] 目标日期: {current_date}")
print(f"[信息] 数据文件将保存至: {file_path}")

# ---------- 1. 读取已有数据（如果存在） ----------
file_exists = os.path.exists(file_path)
if file_exists:
    existing_df = pd.read_csv(file_path, encoding="gbk", parse_dates=['dividOperateDate'])
    print(f"已读取现有文件，共 {len(existing_df)} 条记录")
else:
    existing_df = pd.DataFrame()
    print("文件不存在，将退出. 请从附件下载复权因子数据")
    sys.exit()

# ---------- 2. 登录 Baostock ----------
lg = bs.login()
if lg.error_code != '0':
    print(f"登录失败: {lg.error_msg}")
    sys.exit()

# ---------- 3. 获取当天有除权的股票列表 ----------
rs_factor = bs.query_daily_adjust_factor(date=current_date)
if rs_factor.error_code != '0':
    print(f"查询当天复权因子失败: {rs_factor.error_msg}")
    bs.logout()
    sys.exit()

# 解析当天除权股票
daily_list = []
while (rs_factor.error_code == '0') and rs_factor.next():
    daily_list.append(rs_factor.get_row_data())
bs.logout()  # 先登出，后面重新登录

if not daily_list:
    print(f"日期 {current_date} 无任何除权股票，文件无需更新")
    sys.exit()

# 提取股票代码列表
codes_today = [row[0] for row in daily_list]  # 第一列是 code
print(f"当天有 {len(codes_today)} 只股票发生除权: {codes_today[:5]}...")

# ---------- 4. 重新登录，批量拉取这些股票的全部历史因子 ----------
lg = bs.login()
if lg.error_code != '0':
    print(f"登录失败: {lg.error_msg}")
    sys.exit()

all_new_data = []
# 沪深交易所的第一天开始日期
start_date = "1990-12-19"
end_date = current_date

for idx, code in enumerate(codes_today, 1):
    try:
        rs = bs.query_adjust_factor(code=code, start_date=start_date, end_date=end_date)
        if rs.error_code != '0':
            print(f"  查询 {code} 历史因子失败: {rs.error_msg}")
            continue
        data_list = []
        while (rs.error_code == '0') and rs.next():
            data_list.append(rs.get_row_data())
        if data_list:
            df_code = pd.DataFrame(data_list, columns=rs.fields)
            # 只保留需要的字段（不包含 adjustFactor）
            df_code = df_code[['code', 'dividOperateDate', 'foreAdjustFactor', 'backAdjustFactor']]
            all_new_data.append(df_code)
            print(f"  [{idx}/{len(codes_today)}] {code} 获取 {len(df_code)} 条因子记录")
        else:
            print(f"  [{idx}/{len(codes_today)}] {code} 无历史因子数据")
    except Exception as e:
        print(f"  [{idx}/{len(codes_today)}] {code} 拉取异常: {e}")

bs.logout()

if not all_new_data:
    print("未获取到任何新因子数据，文件保持不变")
    sys.exit()

# 合并新数据
new_df = pd.concat(all_new_data, ignore_index=True)
# 转换日期和数值类型
new_df['dividOperateDate'] = pd.to_datetime(new_df['dividOperateDate'])
new_df['foreAdjustFactor'] = pd.to_numeric(new_df['foreAdjustFactor'], errors='coerce')
new_df['backAdjustFactor'] = pd.to_numeric(new_df['backAdjustFactor'], errors='coerce')
print(f"新拉取复权数据共 {len(new_df)} 条记录")

# ---------- 5. 合并数据：删除旧记录，追加新记录 ----------
if file_exists and not existing_df.empty:
    # 删除现有数据中 code 在当天除权列表中的行
    mask = ~existing_df['code'].isin(codes_today)
    kept_df = existing_df[mask].copy()
    print(f"保留未除权股票记录 {len(kept_df)} 条")
    # 合并
    combined_df = pd.concat([kept_df, new_df], ignore_index=True)
else:
    combined_df = new_df

# 去重（按 code 和 dividOperateDate）
combined_df = combined_df.drop_duplicates(subset=['code', 'dividOperateDate'])

# 排序
combined_df = combined_df.sort_values(['code', 'dividOperateDate']).reset_index(drop=True)

# ---------- 6. 保存前保留6位小数 ----------
# 对因子列四舍五入到6位小数
combined_df['foreAdjustFactor'] = combined_df['foreAdjustFactor'].round(6)
combined_df['backAdjustFactor'] = combined_df['backAdjustFactor'].round(6)

# ---------- 6. 保存 ----------
combined_df.to_csv(file_path, index=False, encoding='gbk')
print(f"复权因子数据更新完成，文件已保存至 {file_path}，当前共 {len(combined_df)} 条记录")

```

### 第六步：计算复权数据

利用已下载的日K线数据和复权因子数据，计算指定日期（默认当天）全部A股的前复权与后复权价格。
数据源路径：
- K线数据目录： D:\baostock_data\{年份}\{日期}_k_AStock_data.csv
- 复权因子目录： D:\baostock_data\stock_adjust_factor_data.csv输出文件：
- 前复权目录： D:\baostock_data\{年份}\foreAdjusted_{日期}_k_AStock_data.csv
- 后复权目录： D:\baostock_data\{年份}\backAdjusted_{日期}_k_AStock_data.csv

```python
# -*- coding: utf-8 -*-
import os
import sys
import pandas as pd
import datetime

# ---------- 可配置参数 ----------
today = datetime.date.today().strftime("%Y-%m-%d")
print("today : " + today)

root_dir = r"D:\baostock_data"          # 数据存储根目录，可按需修改
current_date = today             # 默认当天，可改为 "2026-07-10" 等任意日期
# --------------------------------

print(f"[信息] 目标日期: {current_date}")

# 构建文件路径（按年份归档）
year = current_date[:4]
year_dir = os.path.join(root_dir, year)
os.makedirs(year_dir, exist_ok=True)    # 确保年份子目录存在

kline_file_path = os.path.join(year_dir, f"{current_date}_k_AStock_data.csv")
adjust_factor_file_path = os.path.join(root_dir, "stock_adjust_factor_data.csv")

# 输出文件路径（同样放入年份子目录）
fore_adjust_output = os.path.join(year_dir, f"foreAdjusted_{current_date}_k_AStock_data.csv")
back_adjust_output = os.path.join(year_dir, f"backAdjusted_{current_date}_k_AStock_data.csv")

# ==================== 1. 读取数据——非复权的日K线数据和复权因子数据 ====================
print("读取日K线数据...")
if not os.path.exists(kline_file_path):
    print(f"错误：K线数据文件不存在 - {kline_file_path}")
    sys.exit(1)
df_k = pd.read_csv(kline_file_path, parse_dates=['date'])
if df_k.empty:
    print("K线数据为空，退出")
    sys.exit(1)
print(f"K线数据共 {len(df_k)} 条记录")

print("读取复权因子数据...")
if not os.path.exists(adjust_factor_file_path):
    print(f"错误：复权因子文件不存在 - {adjust_factor_file_path}")
    sys.exit(1)
df_factor = pd.read_csv(adjust_factor_file_path, parse_dates=['dividOperateDate'])
if df_factor.empty:
    print("复权因子数据为空，退出")
    sys.exit(1)
print(f"复权因子共 {len(df_factor)} 条记录")

# 确保数值列类型
price_cols = ['open', 'high', 'low', 'close', 'preclose']
for col in price_cols:
    df_k[col] = pd.to_numeric(df_k[col], errors='coerce')

df_factor['foreAdjustFactor'] = pd.to_numeric(df_factor['foreAdjustFactor'], errors='coerce')
df_factor['backAdjustFactor'] = pd.to_numeric(df_factor['backAdjustFactor'], errors='coerce')

# ==================== 2. 按股票分组，每只股票匹配对应的复权因子 ====================
df_k_sorted = df_k.sort_values(['code', 'date'])
df_factor_sorted = df_factor.sort_values(['code', 'dividOperateDate'])

def merge_factor_for_code(group_k, group_factor):
    """
    为单只股票的每日K线匹配截止到当天（含）最近一次生效的复权因子。

    逻辑说明：
    复权因子表中的因子值在 dividOperateDate 当日及之后有效，直至下一次除权。
    因此对于某天的K线，应使用该天之前（含当天）最后一次更新的因子。
    本函数采用 merge_asof(direction='backward') 实现：
        - 对于每一条K线日期，在因子表中寻找小于等于该日期的最近一条因子记录。
        - 若某股票无任何历史因子，则复权因子设为 1.0（不复权）。
        - 复权因子直接乘以原始价格即可得到复权价格。

    Args:
        group_k: 单只股票的K线数据（已按日期排序），包含 date 和价格列。
        group_factor: 同一只股票的全部历史复权因子记录
            （包含 dividOperateDate、foreAdjustFactor、backAdjustFactor）。

    Returns:
        原K线数据扩展 'cum_fore' 和 'cum_back' 两列（累计因子）。
    """
    if group_factor.empty:
        # 无因子记录，返回原始K线，因子设为1.0
        group_k = group_k.copy()
        group_k['cum_fore'] = 1.0
        group_k['cum_back'] = 1.0
        return group_k

        # 使用 merge_asof 进行时间窗口合并
        # direction='backward' 表示取小于等于左表日期的最近右表记录
    merged = pd.merge_asof(
        group_k,
        group_factor[['dividOperateDate', 'foreAdjustFactor', 'backAdjustFactor']],
        left_on='date',
        right_on='dividOperateDate',
        direction='backward'  # 取 <= date 的最近因子
    )
    # 重命名因子列
    merged.rename(columns={'foreAdjustFactor': 'cum_fore', 'backAdjustFactor': 'cum_back'}, inplace=True)
    # 若某日期早于第一笔除权，因子为空，填充为1.0（不复权）
    merged['cum_fore'] = merged['cum_fore'].fillna(1.0)
    merged['cum_back'] = merged['cum_back'].fillna(1.0)
    return merged

all_merged = []
for code, group_k in df_k_sorted.groupby('code'):
    group_factor = df_factor_sorted[df_factor_sorted['code'] == code]
    merged = merge_factor_for_code(group_k, group_factor)
    all_merged.append(merged)

df_merged = pd.concat(all_merged, ignore_index=True)

# ==================== 3. 提取目标日期的数据 ====================
target = pd.to_datetime(current_date)
df_target = df_merged[df_merged['date'] == target].copy()

if df_target.empty:
    print(f"警告：日期 {current_date} 在K线数据中不存在，请检查日期是否为交易日。")
    sys.exit(1)

print(f"目标日期 {current_date} 共有 {len(df_target)} 只股票")

# ==================== 4. 计算复权价格（包含前复权和后复权） ====================
for col in price_cols:
    df_target[f'pre_{col}'] = df_target[col] * df_target['cum_fore']
    df_target[f'post_{col}'] = df_target[col] * df_target['cum_back']

# ==================== 5. 保存结果到指定目录 ====================
pre_df = df_target[['date', 'code'] + [f'pre_{col}' for col in price_cols] + ['volume', 'amount']].copy()
pre_df.columns = ['date', 'code', 'open', 'high', 'low', 'close', 'preclose', 'volume', 'amount']

post_df = df_target[['date', 'code'] + [f'post_{col}' for col in price_cols] + ['volume', 'amount']].copy()
post_df.columns = ['date', 'code', 'open', 'high', 'low', 'close', 'preclose', 'volume', 'amount']

# 保留6位小数
pre_df[['open', 'high', 'low', 'close', 'preclose']] = pre_df[['open', 'high', 'low', 'close', 'preclose']].round(6)
post_df[['open', 'high', 'low', 'close', 'preclose']] = post_df[['open', 'high', 'low', 'close', 'preclose']].round(6)

pre_df.to_csv(fore_adjust_output, index=False, encoding='utf-8-sig')
post_df.to_csv(back_adjust_output, index=False, encoding='utf-8-sig')

print(f"{current_date} 前复权数据已保存至 {fore_adjust_output}")
print(f"{current_date} 后复权数据已保存至 {back_adjust_output}")
print(f"计算{current_date} 的复权数据完成！")

```