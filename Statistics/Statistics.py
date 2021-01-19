#Using pandas to work with .xlsx files
import pandas as pd 
import numpy as np

#Using pd.read_excel to read file .xls or .xlsx from your local path.
#If can't read .xlsx file then, 'pip install xlrd==1.2.0'.
#In the future, we will read file from user's input instead of this method.
#To read excel file with multiple sheets, put ", 'sheetname'" after 'filename'.
df = pd.read_excel('./MRTuser.xlsx', 'สายเฉลิมรัชมงคล')
digitdf = df.select_dtypes(include=[np.number])

dataTypeDict = dict(digitdf.dtypes)
for key in dataTypeDict:
    # Check if column is not integer or columnn is index column sorted
    if (dataTypeDict[key] != 'int64' or digitdf[key].is_monotonic):
        digitdf.drop(key, inplace=True,axis=1)

# print(digitdf)

#iterate over columns
for (columnName, columnData) in digitdf.iteritems():
        print('Colunm Name : ', columnName)
        print('Column Mean : ', columnData.mean())
        print('Column Std : ', columnData.std())
        print('Column Min : ', columnData.min())
        print('Column Max : ', columnData.max())
        print('\n')