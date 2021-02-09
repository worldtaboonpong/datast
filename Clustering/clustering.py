import pandas as pd 
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score
import matplotlib.pyplot as plot
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.decomposition import PCA
import os

my_path = os.path.abspath(__file__)

df = pd.read_excel('C:/Users/World/Documents/SeniorProject/datast/untitled.xlsx')
range_n_clusters = list (range(2,10))

# print(df.head())

dataTypeDict = dict(df.dtypes)
print(dataTypeDict)
for key in dataTypeDict:
    if ((dataTypeDict[key] != 'int64' or dataTypeDict[key] != 'float64') #check if column is not integer
    or (df[key].is_monotonic and (('ลำดับ' in key) or ( key == 'id')  )) #check if column is something like id or no.
    or ((key == 'year') or (key == 'ปี')) # check if column is year
    or ('รวม' in key)):
        df.drop(key, inplace=True,axis=1)
print(df.head())

# Clustering each 2 columns of dataframe
# If there are more than 5 columns, exit()
if (len(df.columns) >= 2 and len(df.columns) < 5 ):
    for i in range (len(df.columns)):
        for j in range (i+1,len(df.columns)) :
            # print(i,j)
            scores = []
            new_df = df.iloc[:,[i,j]]
            # Do Silhouette Method to find best K to fit
            for n_clusters in range_n_clusters:
                kmeans = KMeans(n_clusters=n_clusters)
                new = new_df._get_numeric_data()
                kmeans.fit(new)
                predict=kmeans.fit_predict(new)
                score = silhouette_score(df, predict)
                scores.append(score)
            # Choose best score to cluster data
            best_cluster = range_n_clusters[scores.index(max(scores))]
            kmeans = KMeans(n_clusters=best_cluster)
            new = new_df._get_numeric_data()
            # print(new)
            kmeans.fit(new)
            predict=kmeans.fit_predict(new)
            df_kmeans = new_df.copy(deep=True)
            df_kmeans['Cluster KMeans'] = pd.Series(predict, index=df_kmeans.index)
            # todo: get tha name of column header from i and j
            plt.rcParams['font.family'] = 'Tahoma'
            df_kmeans.plot.scatter('รถบรรทุกวัสดุอันตราย','รถกึ่งพ่วงที่บรรทุกวัตถุอันตราย', c='Cluster KMeans', colormap='rainbow')
            plt.show()


# plot.show(block=True)
# print(len(df_kmeans.columns))

# if len(df_kmeans.columns) > 3:
#     reduced_data = PCA(n_components=2).fit_transform(df_kmeans)
#     results = pd.DataFrame(reduced_data,columns=['pca1','pca2'])
#     sns.scatterplot(x="pca1", y="pca2", hue=df_kmeans['Cluster KMeans'], data=results)
#     plt.title('K-means Clustering with 2 dimensions')
#     plt.savefig(my_path+'clustering.png')
#     plt.show()
    
# else:
#     sns.scatterplot(x=df_kmeans[:,0], y=df_kmeans[:,1], hue=df_kmeans['Cluster KMeans'], data=results)
#     plt.title('K-means Clustering with 2 dimensions')
#     plt.show()


