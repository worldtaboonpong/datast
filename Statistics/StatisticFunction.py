import pandas as pd 
import numpy as np
import matplotlib
matplotlib.use('Agg')
from matplotlib import pyplot as plt
from operator import xor
import os
import plotly.express as px
import plotly.graph_objects as go

my_path = 'static/'

# dftest = pd.read_excel('harmful30jun2020.xls')
# dftest = pd.read_excel('MRTuser.xlsx', 'สายฉลองรัชธรรม')
# dftest = pd.read_excel('sampledatafoodsales.xlsx', 'FoodSales')

def statistics(df):
    digitdf = df.select_dtypes(include=[np.number])
    dft = df.copy()

    dataTypeDict = dict(digitdf.dtypes)
    for key in dataTypeDict:
        # Check if column is not integer or columnn is index column sorted
        if (not xor(dataTypeDict[key] != 'int64', dataTypeDict[key] != 'float64')
            or (dataTypeDict[key] == 'O')
            or (df[key].is_monotonic and (('ลำดับ' in key) or (key == 'id') or (key == 'ID') or (key == 'Id')))
            or ((key == 'year') or (key == 'YEAR') or (key == 'Year') or (key == 'ปี'))  # check if column is year
            or ((key == 'month') or (key == 'MONTH') or (key == 'Month') or (key == 'เดือน'))):  # check if column is month
                digitdf.drop(key, inplace=True,axis=1)
            
    dft_columns = set(df.columns).difference(digitdf.columns)
    dft = dft[dft_columns]
    # ************************************************** #

    # Iterate to get all column names.
    nameindigitdf = list()
    i = 0
    index = df.shape[0]
    for (columnName, columnData) in digitdf.iteritems():
        nameindigitdf.append(columnName)
    digitc = ", ".join(nameindigitdf)

    nameindft = list()
    i = 0
    index = df.shape[0]
    for (columnName, columnData) in dft.iteritems():
        nameindft.append(columnName)
    dftc = ", ".join(nameindft)
    # ************************************************** #

    #iterate over columns
    i = 0
    index = df.shape[0]
    for (columnName, columnData) in digitdf.iteritems():
        CDNX = list()
        for a in columnData:
            CDNX.append(a)
        max_count = CDNX.count(columnData.max())
        CDNN = list()
        for a in columnData:
            CDNN.append(a)
        min_count = CDNN.count(columnData.min())
        data = df.reset_index()
        fig = px.scatter(data, x= 'index', y = columnName, title="How " + columnName + " relate with " + dftc + " (index)")
        if(max_count < 2):
            fig.add_trace(go.Scatter(x= [digitdf.idxmax()[i]], y =[columnData.max()], 
                                        marker=dict(color='red', size=10), mode="markers+text", name="Max",
                                        text="Max : " + str(columnData.max()), textposition="top center"))
        if(min_count < 2):
            fig.add_trace(go.Scatter(x= [digitdf.idxmin()[i]], y =[columnData.min()], 
                                        marker=dict(color='green', size=10), mode="markers+text", name="Min",
                                        text="Min : " + str(columnData.min()), textposition="bottom center"))

        fig.add_trace(go.Scatter(x=[0, index/2, index], 
                                    y=[columnData.mean(),columnData.mean(),columnData.mean()], 
                                    mode="lines+text", name="Mean", text=["", "", 'Mean: '+ str(round(columnData.mean(),2))], 
                                    textposition="top center"))
        i+=1
        # save graph
        fig.write_image(my_path+'statistic'+ columnName +'.png')
        # fig.show()
    # ************************************************** #

    QA = dict()

    for (columnName, columnData) in digitdf.iteritems():
        # Question #
        ques = "How do Max, Min, Mean of " + columnName + " relate with " + dftc
        # ************************************************** #
        # Answer
        CDNX = list()
        for a in columnData:
            CDNX.append(a)
        max_count = CDNX.count(columnData.max())
        CDNN = list()
        for a in columnData:
            CDNN.append(a)
        min_count = CDNN.count(columnData.min())
        ans = ''
        if(max_count < 2):
            toStringMAX = ''
            for i in range (len(dft.iloc[digitdf.idxmax()[0]].values)) :
                toStringMAX += nameindft[i] + " " + str(dft.iloc[digitdf.idxmax()[0]].values[i]) + " "
            ans += ("Max of " + columnName + " is " + str(columnData.max()) + " at " + toStringMAX)
        else :
            ans += ("There are more than one Max in " + columnName + " ")
        if(min_count < 2):
            toStringMIN = ''
            for i in range (len(dft.iloc[digitdf.idxmin()[0]].values)) :
                toStringMIN += nameindft[i] + " " + str(dft.iloc[digitdf.idxmin()[0]].values[i]) + " "
            ans += ("Min of " + columnName + " is " + str(columnData.min()) + " at " + toStringMIN)
        else :
            ans += ("There are more than one Min in " + columnName + " ")
        ans += ("Mean of " + columnName + " is " + str(columnData.mean().round(2)))
        # ************************************************** #
        # Combine Q&A
        QA[ques] = [ans, my_path+'statistic'+ columnName +'.png']
        # ************************************************** #

    # Return Q&A
    return QA
    # ************************************************** #
    # ********************************************** End of Function **************************************************** #

# result = statistics(dftest)
# print(result)