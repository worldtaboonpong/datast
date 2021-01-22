import pandas as pd 
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score
import matplotlib.pyplot as plot
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.decomposition import PCA
import os

my_path = os.path.abspath(__file__)

df = pd.read_excel('C:/Users/World/Documents/SeniorProject/datast/harmful30jun2020.xls')
range_n_clusters = list (range(2,10))
scores = []
# print(df.head())

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
    predict=kmeans.fit_predict(new)
    score = silhouette_score(df, predict)
    scores.append(score)

# Choose best score to cluster data
best_cluster = range_n_clusters[scores.index(max(scores))]
kmeans = KMeans(n_clusters=best_cluster)
new = df._get_numeric_data()
# print(new)
kmeans.fit(new)
predict=kmeans.fit_predict(new)
df_kmeans = df.copy(deep=True)
df_kmeans['Cluster KMeans'] = pd.Series(predict, index=df_kmeans.index)

# to do: make it choose just 2 columns to cluster data
# plt.rcParams['font.family'] = 'Tahoma'
# df_kmeans.plot.scatter('รวมมัธยม','รวมทั้งหมด', c='Cluster KMeans', colormap='rainbow')

# plot.show(block=True)
# print(len(df_kmeans.columns))
if len(df_kmeans.columns) > 3:
    reduced_data = PCA(n_components=2).fit_transform(df_kmeans)
    results = pd.DataFrame(reduced_data,columns=['pca1','pca2'])
    sns.scatterplot(x="pca1", y="pca2", hue=df_kmeans['Cluster KMeans'], data=results)
    plt.title('K-means Clustering with 2 dimensions')
    plt.savefig(my_path+'clustering.png')
    plt.show()
    
else:
    sns.scatterplot(x=df_kmeans[:,0], y=df_kmeans[:,1], hue=df_kmeans['Cluster KMeans'], data=results)
    plt.title('K-means Clustering with 2 dimensions')
    plt.show()

# sns.lmplot(x='รวมประถม', y='รวมมัธยม', 
#            data=df_kmeans, 
#            hue="Cluster KMeans",  
#            markers=["o", "x"])
# plt.show()
# plt.title('World')
# plt.xlabel('X')
# plt.ylabel('Y')
# plt.scatter('รวมมัธยม','รวมทั้งหมด',c=df_kmeans['Cluster Kmeans'], cmap='rainbow')


