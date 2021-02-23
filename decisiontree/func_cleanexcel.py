import pandas as pd
from operator import xor


def cleanDataframe(dfToClean):

    cleandf = dfToClean.copy(deep=True)
    dataTypeDict = dict(cleandf.dtypes)
    print(dataTypeDict)
    for key in dataTypeDict:
        #delete id row
        if ((cleandf[key].is_monotonic and (('ลำดับ' in key) or (key == 'id')))
        #delete unique row and not a number
        or ((not xor(dataTypeDict[key] != 'int64', dataTypeDict[key] != 'float64')) and cleandf[key].is_unique)):      
             cleandf.drop(key,inplace=True,axis=1)

    # print(cleandf.head())

    return cleandf

