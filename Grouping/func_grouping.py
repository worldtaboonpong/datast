import pandas as pd
from operator import xor
import os

my_path = 'static/'
df = pd.read_excel('sampledatafoodsales.xlsx')

def grouping(df_beforecut):

    qa_grouping = {}

    df = df_beforecut.copy(deep=True)
    dataTypeDict = dict(df.dtypes)

    for key in dataTypeDict:
        if (not xor(dataTypeDict[key] != 'int64', dataTypeDict[key] != 'float64') and df[key].is_unique  # check if column is not integer or float
            or (df[key].is_monotonic and (('ลำดับ' in key) or (key == 'id' or key == 'Id')))
            or (key == 'Id')
            or ((key == 'Year') or (key == 'YEAR') or (key == 'year') or (key == 'ปี'))  # check if column is year
            or ((key == 'Month') or  (key == 'MONTH') or (key == 'month') or (key == 'เดือน')) # check if column is month
            or (('รวม' in key) or ('total' in key) or ('Total' in key))):
            df.drop(key, inplace=True, axis=1)

    return df.head()

print(grouping(df))