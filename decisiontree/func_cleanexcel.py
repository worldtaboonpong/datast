import pandas as pd



def cleanDataframe(dfToClean):

    cleandf = dfToClean.copy(deep=True)
    dataTypeDict = dict(cleandf.dtypes)

    return cleandf

