import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt
from operator import xor
import os

my_path = os.path.abspath(__file__)

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

    #iterate over columns
    i = 0
    index = df.shape[0]
    for (columnName, columnData) in digitdf.iteritems():
        # print('Column Name : ', columnName)
        # print('Column Mean : ', columnData.mean())
        # print('Column Min : ', columnData.min())
        # print('Column Max : ', columnData.max())
        # print('\n')
        CDNX = list()
        for a in columnData:
            CDNX.append(a)
        max_count = CDNX.count(columnData.max())
        CDNN = list()
        for a in columnData:
            CDNN.append(a)
        min_count = CDNN.count(columnData.min())
        plt.rcParams['font.family'] = 'Tahoma'
        df.reset_index().plot.scatter( x= 'index', y = columnName, color = 'black')
        if(max_count < 2):
            plt.scatter(digitdf.idxmax()[0], columnData.max(), color = 'blue')
            plt.annotate('Max: '+ str(columnData.max()), (digitdf.idxmax()[i], columnData.max()), color="blue")
        if(min_count < 2):
            plt.scatter(digitdf.idxmin()[i], columnData.min(), color = 'red')
            plt.annotate('Min: '+ str(columnData.min()), (digitdf.idxmin()[i], columnData.min()), color="red")
        plt.text(index/2, columnData.mean(), 'Mean: '+ str(columnData.mean().round(2)), fontsize=10, va='center', ha='center', backgroundcolor='w')
        plt.axhline(columnData.mean(), color = 'gray', linestyle = '--', linewidth = .5)
        i+=1
        # save graph
        plt.savefig(__file__ + columnName +'.png')
        # plt.show()
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

    # Question #
    ques = ("How do Max, Min, Mean of " + digitc + " relate with " + dftc )
    # ************************************************** #

    QA = {ques:[]}

    # Answer
    for (columnName, columnData) in digitdf.iteritems():
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
        QA[ques].append((ans,__file__ + columnName +'.png'))
    # ************************************************** #

    # Return Q&A
    return QA
    # ************************************************** #
    # ********************************************** End of Function **************************************************** #

# result = statistics(dftest)
# print(result)