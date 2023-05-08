import pandas as pd
import numpy as np

# 创建一个包含随机浮点数的Series对象
data = pd.Series(np.random.rand(100))

# 将数据划分为4个区间，并统计各个区间中元素的数量
bins = pd.cut(data, bins=4)
counts = bins.value_counts()

# 输出统计结果
print(counts)


# from stockstats import StockDataFrame
# import pandas as pd

# # 自定义指标函数

# debounceTimes = 2
# def my_custom_indicator(df):
#     # 在这里添加自定义指标的计算逻辑
#     close_series = df['close']
#     max_close = close_series.max()
#     min_close = close_series.min()
#     interval = (max_close-min_close)/100

#     print(max_close,min_close)
#     df['weight_volume'] = df['quote_change'].abs() * df['volume']


#     print(df['weight_volume'])
# # (2 * df['close'] - df['high'] - df['low']) / (df['high'] - df['low']) * stock_data['Volume']
    
#     # # 计算每个日期的筹码结构
#     # stock_data['Chip Structure'] = (2 * stock_data['Close'] - stock_data['High'] - stock_data['Low']) / (stock_data['High'] - stock_data['Low']) * stock_data['Volume']
#     # stock_data['Chip Structure'] = stock_data['Chip Structure'].cumsum() / stock_data['Volume'].cumsum()

# # 读取股票数据
# # , parse_dates=['date']
# df = pd.read_csv('./data/stock.csv')
# # 创建 StockDataFrame 对象
# sdf = StockDataFrame.retype(df)
# # sdf.drop('unnamed: 0',axis=1, inplace=True)
# # stock_column = ['kdjd', 'kdjj', 'kdjk', 'macd', 'macdh']

# # all_column = [ *stock_column, *other_base_column]

# # for col in stock_column:
# #     sdf[col] = sdf.get(col)

# # print(sdf['macdh'].tail(20))
# my_custom_indicator(sdf)
# # print(sdf['lgl_macd60'])
