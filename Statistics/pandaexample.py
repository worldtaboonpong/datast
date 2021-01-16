#Using pandas to work with .xlsx files
import pandas as pd 
import numpy as np

#Using pd.read_excel to read file .xls or .xlsx from your local path
#In the future, we will read file from user's input instead of this method.
df = pd.read_excel('./harmful30jun2020.xls')
digitdf = df.select_dtypes(include=[np.number])
print(digitdf)

# #Using df.head to show the top 5 rows of dataframe
# print(df.head())
# #Using df.shape to show dimension of dataframe
# print(df.shape)
# print(df.columns)
print(df.describe())

#Using df.dtypes to show type of data of each column
#Using dict(df.types) to make Dict which the keys are column header and the values are type of data of each column
# dataTypeDict = dict(df.dtypes)
# print(dataTypeDict)
# for key in dataTypeDict:
#     if (dataTypeDict[key] != 'int64'):
#         print (key)
#         # Using df[key] to access data which column header is key 
#         # Using tail to show the last 5 rows of datatframe 
#         print(df[key].tail())
#         # Using count to count the row
#         rowCount = df[key].count()
#         print(rowCount)
#         # Trying to access each row of this column
#         for i in range (rowCount):
#             if i&2 == 0 :
#                 print(df[key][i])
        

#iterate over columns
for (columnName, columnData) in digitdf.iteritems():
    if columnName != 'ลำดับ':
        print('Colunm Name : ', columnName)
        print('Column Contents : ', columnData.values)
        print('Column Mean : ', columnData.mean())



