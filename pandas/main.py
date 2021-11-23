import pandas as pd
import numpy as np
from pandas import Series, DataFrame

list = Series([1,2,3,4], index=['A','B','C','D'])
print(list)
print(list.index)
print(list[0])
print(list[2:])

print('-------------------------------------------------------------')

"""
    データを組み合わせる
"""

se1 = Series([2, np.nan, 4, np.nan, 6, np.nan], index=['Q', 'R', 'S', 'T', 'U', 'V'])
# print(se1)
# print('--------')
se2 = Series(np.arange(len(se1), dtype=np.float64), index=['Q', 'R', 'S', 'T', 'U', 'V'])
# print(se2)

# print(Series(np.where(pd.isnull(se1),se2,se1)))
# print(Series(np.where(pd.isnull(se1),se2,se1), index=se1.index))
# print(se1.combine_first(se2))

print('-------------------------------------------------------------')

"""
    SeriesとDataframeの変換
"""
# データフレームを用意
data = DataFrame(np.arange(8).reshape((2, 4)), index=pd.Index(['LA', 'SP'], name='city'), columns=pd.Index(['A', 'B', 'C', 'D'], name='letter'))
# print(data)
# print(type(data))

# データフレーム型をシリーズ型に変換
data_st = data.stack()
# print(data_st)
# print(type(data_st))

# シリーズ型をデータフレーム型に変換
data_st_2 = data_st.unstack()
print(data_st_2)

# 結合
se1 = Series([0, 1, 2], index=['A', 'X', 'Y'])
se2 = Series([3, 4, 5], index=['AX', 'Y', 'Z'])
result = pd.concat()
