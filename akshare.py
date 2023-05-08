from stockstats import StockDataFrame
import pandas as pd

# 自定义指标函数

debounceTimes = 2
def my_custom_indicator(df):
    # 在这里添加自定义指标的计算逻辑
    # 返回包含指标值的 Series 对象
    # print(df)

    # 检查macd最后一个数
    df['lgl_macd60'] = 0
    df['lgl_first_max'] = 0
    df['lgl_first_min'] = 0
    df['lgl_first_downs_change'] = 0
    df['lgl_sec_max'] = 0
    df['lgl_sec_min'] = 0
    df['lgl_sec_downs_change'] = 0
    
    lastestMacdh =  df['macdh'].tail(1).values[0]
    lastestClose =  df['close'].tail(1).values[0]
    if lastestMacdh >= 0:
        return


    isOk = False
    checkFirst = True
    addFirst = True
    checkSec = True
    addSec = True
    first = []
    sec = []

    # pArea = 
    # ppArea
    # length = len(list(df.rows()))
    length = len(list(df.iterrows()))
    times = 0
    for i in range(length - 1,-1,-1):
        row = df.iloc[i]
        curMacdh = row['macdh']
        if checkFirst == True:
            if curMacdh >= 0:
                first.append(row.close)
                times += 1
                if times >= debounceTimes:
                    times = 0
                    checkFirst = False
            else: 
                if len(first) > 0:
                    times = 0
                    first = []

        elif addFirst == True:
            if curMacdh < 0:
                times += 1
                if times >= debounceTimes:
                    times = 0
                    addFirst = False
            else: 
                times = 0
                first.append(row.close)

        elif checkSec == True:
            if curMacdh >= 0:
                sec.append(row.close)
                times += 1
                if times >= debounceTimes:
                    times = 0
                    checkSec = False
            else: 
                if len(sec) > 0:
                    times = 0
                    first = []

        elif addSec == True:
            if curMacdh < 0:
                times += 1
                if times >= debounceTimes:
                    times = 0
                    addSec = False
                    isOk = True
                    break
            else: 
                times = 0
                sec.append(row.close)

    print(first)
    print(sec)
    firstArea = pd.Series(first)
    lgl_first_max= firstArea.max()
    lgl_first_min= firstArea.min()

    secArea = pd.Series(sec)
    lgl_sec_max= secArea.max()
    lgl_sec_min= secArea.min()


    lgl_first_downs_change = (lgl_first_min - lastestClose)/lgl_first_min * 100
    lgl_sec_downs_change = (lgl_sec_min - lgl_first_max)/lgl_sec_min * 100

    # print(lgl_sec_min)
    # print(lgl_first_max)
    # # print(lgl_first_min)
    # # print(lastestClose)
    # 检查通过
    if isOk == True and lgl_first_max < lgl_sec_min and  lgl_first_downs_change < lgl_sec_downs_change:
        df['lgl_macd60'][-1] = 1
        df['lgl_first_max'][-1] =lgl_sec_max
        df['lgl_first_min'][-1] =lgl_sec_min
        df['lgl_first_downs_change'] = lgl_sec_downs_change
        df['lgl_sec_max'][-1] =lgl_first_max
        df['lgl_sec_min'][-1] =lgl_first_min
        df['lgl_sec_downs_change'] =  lgl_first_downs_change
    # return pd.Series(df['open'], index=df.index)

# 读取股票数据
# , parse_dates=['date']
df = pd.read_csv('./data/stock.csv')
# 创建 StockDataFrame 对象
sdf = StockDataFrame.retype(df)
sdf.drop('unnamed: 0',axis=1, inplace=True)
stock_column = ['kdjd', 'kdjj', 'kdjk', 'macd', 'macdh']

# all_column = [ *stock_column, *other_base_column]

# all_column.extend(['date']).extend(stock_column).extend(other_base_column)
# # sdf.round(2)
# column_list =  sdf.columns.tolist()
# print(all_column)
# print(sdf.index.tolist())
# print(list(sdf.index))
# print(stock_column)
for col in stock_column:
    sdf[col] = sdf.get(col)

# print(sdf['macdh'].tail(20))
my_custom_indicator(sdf)
sdf.to_csv('./data/out_stock.csv')
# print(sdf['lgl_macd60'])
