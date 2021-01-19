import pandas as pd
import numpy as np
from apyori import apriori

df = pd.read_excel("./harmful30jun2020.xls")
digitdf = df.select_dtypes(include=[np.number])
print(digitdf)

#iterate over columns
for (columnName, columnData) in digitdf.iteritems():
   print('Colunm Name : ', columnName)
   print('Column Contents : ', columnData.values)

#iterate over columns with column names
for column in digitdf:
   columnSeriesObj = digitdf[column]
   print('Colunm Name : ', column)
   print('Column Contents : ', columnSeriesObj.values)

#iterate over certain columns
for column in digitdf[['รถบรรทุกวัสดุอันตราย', 'รถกึ่งพ่วงที่บรรทุกวัตถุอันตราย']]:
   columnSeriesObj = digitdf[column]
   print('Colunm Name : ', column)
   print('Column Contents : ', columnSeriesObj.values)

#iterate over column index
for index in range(digitdf.shape[1]):
   print('Column Number : ', index)
   # Select column by index position using iloc[]
   columnSeriesObj = digitdf.iloc[: , index]
   print('Column Contents : ', columnSeriesObj.values)   