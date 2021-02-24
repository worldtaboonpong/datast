import pandas as pd
import math 
from decimal import Decimal
from operator import xor



df = pd.read_excel('Clustering/untitled.xlsx')

def cleanDataframe(dfToClean):

    # print(dfToClean)
    cleandf = dfToClean.copy(deep=True)
    dataTypeDict = dict(cleandf.dtypes)
    # print(dataTypeDict)
    for key in dataTypeDict:
        #delete id row
        if ((cleandf[key].is_monotonic and (('ลำดับ' in key) or (key == 'id')))
        #delete unique row and not a number
        or ((not xor(dataTypeDict[key] != 'int64', dataTypeDict[key] != 'float64')) and cleandf[key].is_unique)
        #delete separate column of day-month-year
        or ((key == 'year') or (key == 'ปี'))
        or ((key == 'month') or (key == 'เดือน'))
        or ((key == 'day') or (key == 'วันที่') and dataTypeDict[key] != 'O')):      
             cleandf.drop(key,inplace=True,axis=1)

        # todo: change int and float to be string of range of value
    for col_name in cleandf.columns:
        if (cleandf[col_name].dtype == 'int64' or cleandf[col_name].dtype == 'float64'):


            v_max = cleandf[col_name].max()
            v_min = cleandf[col_name].min()
            # print(max,min)
            v_range = Decimal(v_max)-Decimal(v_min)
            # print(v_max,v_min)
            # print(v_range)
            sample = cleandf.shape[0]
            v_floor = math.ceil(1+3.322*math.log10(sample))
            # print(v_floor)
            interval = math.ceil(v_range/v_floor)
            # print(interval)
            
            # cleandf.loc[cleandf[col] > 1,col] = 'Hi'


            start = v_min

            # condition = (cleandf[col_name] >= start) & (cleandf[col_name] <= start+interval)
            # cleandf.loc[condition,col_name] = 'ช่วง '+str(start)+' ถึง ' + str(start+interval) 

            # print(cleandf)

            for i in range(v_floor):
                # stringStart = str(start)
                # stringStartInterval = str(start+interval)
                # condition = (cleandf[col_name] >= start) & (cleandf[col_name] < start+interval)
                cleandf.loc[(cleandf[col_name] >= start) & (cleandf[col_name] < start+interval),col_name] = 'ช่วง '+str(start)+' ถึง ' + str(start+interval)
                # print(cleandf,start,start+interval,condition)                
                start = start+interval

    
    

    if len(cleandf.columns) <= 2:
        return
    else:
        return cleandf

cleanDataframe(df)