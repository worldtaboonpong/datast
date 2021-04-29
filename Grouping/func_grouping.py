import pandas as pd
from operator import xor
import os
import plotly.express as px

my_path = 'static/'
df = pd.read_excel('sampledatafoodsales.xlsx')

def grouping(df_beforecut):

    qa_grouping = {}

    df = df_beforecut.copy(deep=True)
    dataTypeDict = dict(df.dtypes)

    for key in dataTypeDict:
        if ((df[key].is_monotonic and (('ลำดับ' in key) or (key == 'id' or key == 'Id')))
            or (key == 'Id')
            or ((key == 'Year') or (key == 'YEAR') or (key == 'year') or (key == 'ปี'))  # check if column is year
            or ((key == 'Month') or  (key == 'MONTH') or (key == 'month') or (key == 'เดือน')) # check if column is month
            or (('รวม' in key) or ('total' in key) or ('Total' in key))
            or len(set(df[key]))==1 
            or ((key == 'day') or (key == 'วันที่') and dataTypeDict[key] != 'O')):
            df.drop(key, inplace=True, axis=1)

    str_col = []
    num_col = []
    for col_name in df:
        if (df[col_name].dtype == 'int64' or df[col_name].dtype == 'float64'):
            num_col.append(col_name)
        else :
            str_col.append(col_name)
    
    for group in str_col:
        data = df.groupby(group).sum()
        fig = px.bar(data,x=list(set(df[group])),y=num_col,barmode='group',labels={'x':str(group)})
        fig.write_image(my_path+'cluster'+group+'.png')



grouping(df)