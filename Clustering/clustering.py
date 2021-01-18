import pandas as pd 
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score

df = pd.read_excel('C:/Users/World/Documents/SeniorProject/datast/harmful30jun2020.xls')
range_n_clusters = list (range(2,10))
scores = []

dataTypeDict = dict(df.dtypes)

for key in dataTypeDict:
    # Check if column is not integer or columnn is index column sorted
    if (dataTypeDict[key] != 'int64' or df[key].is_monotonic):
        df.drop(key, inplace=True,axis=1)

# Do Silhouette Method to find best K to fit
for n_clusters in range_n_clusters:
    kmeans = KMeans(n_clusters=n_clusters)
    new = df._get_numeric_data()
    kmeans.fit(new)
    predict=kmeans.predict(new)
    score = silhouette_score(df, predict)
    scores.append(score)
    

best_cluster = range_n_clusters[scores.index(max(scores))]
kmeans = KMeans(n_clusters=best_cluster)
new = df._get_numeric_data()
kmeans.fit(new)
predict=kmeans.predict(new)
df_kmeans = df.copy(deep=True)
df_kmeans['Cluster KMeans'] = pd.Series(predict, index=df_kmeans.index)


print(df_kmeans)



