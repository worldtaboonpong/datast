#Using pandas to work with .xlsx files
import pandas as pd 

#Using pd.read_excel to read file .xls or .xlsx from your local path
#In the future, we will read file from user's input instead of this method.
df = pd.read_excel('C:/Users/World/Documents/SeniorProject/datast/harmful30jun2020.xls')

#Using df.head to show the top 5 rows of dataframe
print(df.head())

#Using df.dtypes to show type of data of each column
#Using dict(df.types) to make Dict which the keys are column header and the values are type of data of each column
dataTypeDict = dict(df.dtypes)
for key in dataTypeDict:
    if (dataTypeDict[key] != 'int64'):
        print (key)
        # Using df[key] to access data which column header is key 
        # Using tail to show the last 5 rows of datatframe 
        print(df[key].tail())


