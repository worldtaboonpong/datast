import pandas as pd 
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score

df = pd.read_excel('C:/Users/World/Documents/SeniorProject/datast/harmful30jun2020.xls')
# num_cluster=3
range_n_clusters = list (range(2,10))

dataTypeDict = dict(df.dtypes)

for key in dataTypeDict:
    if (dataTypeDict[key] != 'int64'):
        df.drop(key, inplace=True, axis=1)

for n_clusters in range_n_clusters:
    kmeans = KMeans(n_clusters=n_clusters)
    new = df._get_numeric_data()
    kmeans.fit(new)
    predict=kmeans.predict(new)
    score = silhouette_score(df, predict)
    print("For n_clusters = {}, silhouette score is {})".format(n_clusters, score))

print(range_n_clusters[1])

# df_kmeans = df.copy(deep=True)
# df_kmeans['Cluster KMeans'] = pd.Series(predict, index=df_kmeans.index)

# print(df_kmeans)


