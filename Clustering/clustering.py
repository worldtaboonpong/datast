import pandas as pd 
from sklearn.cluster import KMeans

df = pd.read_excel('C:/Users/World/Documents/SeniorProject/datast/harmful30jun2020.xls')
num_cluster=3

dataTypeDict = dict(df.dtypes)

for key in dataTypeDict:
    if (dataTypeDict[key] != 'int64'):
        df.drop(key, inplace=True, axis=1)

kmeans = KMeans(n_clusters=num_cluster,random_state=1)
new = df._get_numeric_data()
kmeans.fit(new)
predict=kmeans.predict(new)
df_kmeans = df.copy(deep=True)
df_kmeans['Cluster KMeans'] = pd.Series(predict, index=df_kmeans.index)

print(df_kmeans)


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