import pandas as pd
import numpy as np
from apyori import apriori

df = pd.read_excel("./covid19.xls")
digitdf = df.select_dtypes(include=[np.number])
print(df)

#iterate over columns
for (columnName, columnData) in df.iteritems():
   print('Colunm Name : ', columnName)
   print('Column Contents : ', columnData.values)

#iterate over columns with column names
for column in df:
   columnSeriesObj = df[column]
   print('Colunm Name : ', column)
   print('Column Contents : ', columnSeriesObj.values)

#iterate over certain columns
for column in df[['sex', 'age']]:
   columnSeriesObj = df[column]
   print('Colunm Name : ', column)
   print('Column Contents : ', columnSeriesObj.values)

#iterate over column index
for index in range(df.shape[1]):
   print('Column Number : ', index)
   # Select column by index position using iloc[]
   columnSeriesObj = df.iloc[: , index]
   print('Column Contents : ', columnSeriesObj.values)   