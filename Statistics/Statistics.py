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
df = pd.read_excel('harmful30jun2020.xls')
digitdf = df.select_dtypes(include=[np.number])

dataTypeDict = dict(digitdf.dtypes)
for key in dataTypeDict:
    # Check if column is not integer or columnn is index column sorted
    if (dataTypeDict[key] != 'int64' or digitdf[key].is_monotonic):
        digitdf.drop(key, inplace=True,axis=1)

print(digitdf.describe())

#iterate over columns
i = 0
index = df.shape[0]
for (columnName, columnData) in digitdf.iteritems():
        print('Column Name : ', columnName)
        print('Column Mean : ', columnData.mean())
        print('Column Min : ', columnData.min())
        print('Column Max : ', columnData.max())
        print('\n')
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