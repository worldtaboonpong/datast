import pandas as pd
import math 
from decimal import Decimal
from operator import xor
import numpy as np
import csv


# df = pd.read_excel('test_files/sampledatafoodsales.xlsx')

def cleanDataframe(dfToClean):
    cleandf = dfToClean.copy(deep=True)
    dataTypeDict = dict(cleandf.dtypes)
    for key in dataTypeDict:
        if ((cleandf[key].is_monotonic and (('ลำดับ' in key) or (key == 'id')))
        or ((not xor(dataTypeDict[key] != 'int64', dataTypeDict[key] != 'float64')) and cleandf[key].is_unique)
        or ((key == 'year') or (key == 'ปี'))
        or ((key == 'month') or (key == 'เดือน'))
        or ((key == 'day') or (key == 'วันที่') and dataTypeDict[key] != 'O')):      
             cleandf.drop(key,inplace=True,axis=1)
    df1=pd.DataFrame()
    for col_name in cleandf:
        values=[]
        if (cleandf[col_name].dtype == 'int64' or cleandf[col_name].dtype == 'float64'):
            v_max = cleandf[col_name].max()
            v_min = cleandf[col_name].min()
            v_range = (v_max)-(v_min)
            sample = cleandf.shape[0]
            v_floor = math.ceil(1+3.322*math.log10(sample))
            interval = math.ceil(v_range/v_floor)
            start = v_min
            value=[]
            for i in range(v_floor):
                b=start+interval
                value.append([round(start,2),round(start+interval,2)])
                start+=interval
            for j in cleandf[col_name]:
                for k in range(len(value)):
                    if value[k][0] <= j and j<=value[k][1]:
                        values.append('ช่วง '+str(value[k][0])+' ถึง '+str(value[k][1]))
                        break
            df1[str(col_name)]=values
            cleandf[str(col_name)]=df1[str(col_name)]
    if len(cleandf.columns) <= 2:
        return
    return cleandf

# print(cleanDataframe(df))
# print(type(cleanDataframe(df)))
