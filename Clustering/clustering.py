import pandas as pd 
from sklearn.model_selection import train_test_split
from sklearn.cluster import KMeans

df = pd.read_excel('C:/Users/World/Documents/SeniorProject/datast/harmful30jun2020.xls')

# (df_train, df_test) = train_test_split(df,test_size=0.30)

dataTypeDict = dict(df.dtypes)
# kmeans = KMeans(n_clusters=2, n_init=3, max_iter=3000, random_state=1).fit(df)
# kmeans = kmeans.fit(df_train[['รถบรรทุกวัสดุอันตราย'],['รถกึ่งพ่วงที่บรรทุกวัตถุอันตราย']])

for key in dataTypeDict:
    if (dataTypeDict[key] != 'int64'):
        df.drop(key, inplace=True, axis=1)

kmeans = KMeans(n_clusters=4, n_init=3, max_iter=3000, random_state=1).fit(df)
print(kmeans.labels_)



# df_train.loc[:,'clusters'] = kmeans.labels_



# X = pd.DataFrame({'id': [1,2,3,4,5],
#                   'value_1': [1,3,1,4,5],
#                   'value_2': [0,0,1,5,0]})

# # Split ALL columns
# (X_train, X_test) = train_test_split(X,test_size=0.30)
# # Cluster using SOME columns
# kmeans = KMeans(n_clusters=2, n_init=3, max_iter=3000, random_state=1)
# kmeans = kmeans.fit(X_train[['value_1','value_2']])
# # Save the labels
# X_train.loc[:,'labels'] = kmeans.labels_

# print(X_train)