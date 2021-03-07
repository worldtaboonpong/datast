import pandas as pd
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.decomposition import PCA
from operator import xor
import os
import numpy as np

my_path = os.path.abspath(__file__)

df = pd.read_excel('./MRTuser.xlsx','สายฉลองรัชธรรม')


def clustering(df_beforecut):

    qa_clustering = {'How can we cluster the data from this file': []}

    range_n_clusters = list(range(2, 10))
    df = df_beforecut.copy(deep=True)

    dataTypeDict = dict(df.dtypes)
    for key in dataTypeDict:
        if (not xor(dataTypeDict[key] != 'int64', dataTypeDict[key] != 'float64')  # check if column is not integer or float
            or (dataTypeDict[key] == 'O')
            # check if column is something like id or no.
            or (df[key].is_monotonic and (('ลำดับ' in key) or (key == 'id')))
            or ((key == 'year') or (key == 'ปี'))  # check if column is year
            or ('รวม' in key)):
            df.drop(key, inplace=True, axis=1)

    difference_columns = set(df_beforecut.columns).difference(df.columns)
    dfForDetail = df_beforecut[difference_columns]
    dataTypeDictForDetail = dict(dfForDetail.dtypes)

    for key in dataTypeDictForDetail:
        if (dfForDetail[key].is_monotonic and (('ลำดับ' in key) or (key == 'id'))) or ('รวม' in key):
            dfForDetail.drop(key, inplace=True, axis=1)

    if (len(df.columns) >= 2 and len(df.columns) <= 5):
        for i in range(len(df.columns)):
            for j in range(i+1, len(df.columns)):
                scores = []
                new_df = df.iloc[:, [i, j]]

                # Do Silhouette Method to find best K to fit
                for n_cluster in range_n_clusters:
                    if n_cluster > new_df.shape[0]-1:
                        break
                    kmeans = KMeans(n_clusters=n_cluster)
                    new = new_df._get_numeric_data()
                    kmeans.fit(new)
                    predict = kmeans.fit_predict(new)
                    score = silhouette_score(new, predict)
                    scores.append(score)
                # Choose best score to cluster data
                best_cluster = range_n_clusters[scores.index(max(scores))]
                kmeans = KMeans(n_clusters=best_cluster)
                new = new_df._get_numeric_data()
                kmeans.fit(new)
                predict = kmeans.fit_predict(new)
                df_kmeans = new_df.copy(deep=True)
                df_kmeans['Group'] = pd.Series(predict, index=df_kmeans.index)
                # Try to gert more detail to explain
                detailToExplain = ''
                for k in range(best_cluster):
                    dfForGroupI = dfForDetail.loc[df_kmeans['Group'] == k]
                    detailToExplain += ('Group #' + str(k) + ' include ')
                    for l in range(dfForGroupI.shape[0]):
                        for m in range(dfForGroupI.shape[1]):
                            detailToExplain += dfForGroupI.columns.values[m] + str(
                                dfForGroupI.iat[l, m]) + ' '
                
                colormap = np.array(['r','g','b'])
                group = df_kmeans['Group']

                plt.rcParams['font.family'] = 'Tahoma'
                
                df_kmeans.plot.scatter(new.columns.values[0],new.columns.values[1], c=colormap[group] )
                plt.legend(title = 'Group')
    
                plt.title('Clustering by' + ' ' +new.columns.values[0] + ' ' + 'and' + ' ' + new.columns.values[1])
                plt.savefig(my_path+'tograph'+str(i)+str(j)+'.png')
                # plt.show()

                qa_clustering['How can we cluster the data from this file'].append(('We can cluster between' +
                                                                                           ' ' + new.columns.values[0] + ' ' + 'and' + ' ' + new.columns.values[1] + ' ' +
                                                                                           'into' + ' ' +
                                                                                           str(
                                                                                               best_cluster) + ' ' + 'groups' + ' ' + 'which' + ' ' + detailToExplain,
                                                                                           str(my_path) + 'tograph'+str(i)+str(j)+'.png'))
                # print(scores)                                                                           

    return qa_clustering

print(clustering(df))


