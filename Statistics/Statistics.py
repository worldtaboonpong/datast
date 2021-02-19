#Using pandas to work with .xlsx files
import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt
import os

my_path = os.path.abspath(__file__)

#Using pd.read_excel to read file .xls or .xlsx from your local path.
#If can't read .xlsx file then, 'pip install xlrd==1.2.0'.
#In the future, we will read file from user's input instead of this method.
#To read excel file with multiple sheets, put ", 'sheetname'" after 'filename'.
df = pd.read_excel('MRTuser.xlsx', 'สายฉลองรัชธรรม')
# df = pd.read_excel('harmful30jun2020.xls')
dft = df.copy()
digitdf = df.select_dtypes(include=[np.number])

dataTypeDict = dict(digitdf.dtypes)
for key in dataTypeDict:
    # Check if column is not integer or columnn is index column sorted
    if (dataTypeDict[key] != 'int64' or digitdf[key].is_monotonic):
        digitdf.drop(key, inplace=True,axis=1)

# print(digitdf.describe())
dft_columns = set(df.columns).difference(digitdf.columns)
# print(dft[dft_columns].head())
dft = dft[dft_columns]


#iterate over columns
i = 0
index = df.shape[0]
for (columnName, columnData) in digitdf.iteritems():
        # print('Column Name : ', columnName)
        # print('Column Mean : ', columnData.mean())
        # print('Column Min : ', columnData.min())
        # print('Column Max : ', columnData.max())
        # print('\n')
        plt.rcParams['font.family'] = 'Tahoma'
        df.reset_index().plot.scatter( x= 'index', y = columnName, color = 'black')
        plt.scatter(digitdf.idxmax()[i], columnData.max(), color = 'blue')
        plt.scatter(digitdf.idxmin()[i], columnData.min(), color = 'red')
        plt.annotate('Max: '+ str(columnData.max()), (digitdf.idxmax()[i], columnData.max()), color="blue")
        plt.annotate('Min: '+ str(columnData.min()), (digitdf.idxmin()[i], columnData.min()), color="red")
        plt.text(index/2, columnData.mean(), 'Mean: '+ str(columnData.mean().round(2)), fontsize=10, va='center', ha='center', backgroundcolor='w')
        plt.axhline(columnData.mean(), color = 'gray', linestyle = '--', linewidth = .5)
        i+=1
        # save graph
        plt.savefig(__file__ + columnName +'.png')
        plt.show()

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
ques = ("ค่า Max, Min, Mean ของ " + digitc + " มีความสัมพันธ์กับ " + dftc + " อย่างไร")
# print("Question : ")
# print(ques)
# ************************************************** #

# Answer
ans = list()
for (columnName, columnData) in digitdf.iteritems():
    toStringMAX = ''
    for i in range (len(dft.iloc[digitdf.idxmax()[i]].values)) :
        toStringMAX += nameindft[i] + " " + str(dft.iloc[digitdf.idxmax()[i]].values[i]) + " "
    ans.append("ค่า Max ของ " + columnName + " คือ " + str(columnData.max()) + " ที่ " + toStringMAX)
    toStringMIN = ''
    for i in range (len(dft.iloc[digitdf.idxmin()[i]].values)) :
        toStringMIN += nameindft[i] + " " + str(dft.iloc[digitdf.idxmin()[i]].values[i]) + " "
    ans.append("ค่า Min ของ " + columnName + " คือ " + str(columnData.max()) + " ที่ " + toStringMIN)
    ans.append("ค่า Mean ของ " + columnName + " คือ " + str(columnData.mean().round(2)))
    ans.append("")
print("Answer : ")
print(*ans, sep="\n")
# ************************************************** #