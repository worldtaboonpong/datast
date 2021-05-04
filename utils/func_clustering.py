import pandas as pd
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score
from sklearn.decomposition import PCA
from operator import xor
import os
import numpy as np
from IPython.display import HTML
import plotly.express as px
from pandas.plotting import table

my_path = 'static/'

# df = pd.read_excel('MRTuser.xlsx')


def clustering(df_beforecut):

    qa_clustering = {}

    range_n_clusters = list(range(2, 10))
    df = df_beforecut.copy(deep=True)

    dataTypeDict = dict(df.dtypes)
    # print(dataTypeDict)
    for key in dataTypeDict:
        if (not xor(dataTypeDict[key] != 'int64', dataTypeDict[key] != 'float64')  # check if column is not integer or float
            or (dataTypeDict[key] == 'O')
            # check if column is something like id or no.
            or (df[key].is_monotonic and (('ลำดับ' in key) or (key == 'id' or key == 'Id')))
            or (key == 'Id')
            or ((key == 'Year') or (key == 'YEAR') or (key == 'year') or (key == 'ปี'))  # check if column is year
            or ((key == 'Month') or  (key == 'MONTH') or (key == 'month') or (key == 'เดือน')) # check if column is month
            or (('รวม' in key) or ('total' in key) or ('Total' in key))):
            df.drop(key, inplace=True, axis=1)

    # print(df.head())
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
                best_cluster = 0
                prev_silhouette_score = 0.0
                
                # Do Silhouette Method to find best K to fit
                for n_cluster in range_n_clusters:
                    if n_cluster > new_df.shape[0]-1:
                        break
                    kmeans = KMeans(n_clusters=n_cluster)
                    # new = new_df._get_numeric_data()
                    predict = kmeans.fit_predict(new_df)
                    score = silhouette_score(new_df, predict)
                    if score > prev_silhouette_score:
                        prev_silhouette_score = score
                        best_cluster = n_cluster
                    
                    # scores.append(score)
                # Choose best score to cluster data
                # best_cluster = range_n_clusters[scores.index(max(scores))]
                
                kmeans = KMeans(n_clusters=best_cluster)
                new = new_df._get_numeric_data()
                kmeans.fit(new)
                predict = kmeans.fit_predict(new)
                df_kmeans = new_df.copy(deep=True)
                df_kmeans['Group'] = pd.Series(predict, index=df_kmeans.index)
                dfForDetail['Group'] = pd.Series(predict,index=dfForDetail.index)
                col_name = list(df_kmeans) #list of col name
                first_col = col_name[0]
                second_col = col_name[1]
                result = dfForDetail.to_html()
                df_kmeans['Group'] = df_kmeans['Group'].astype(str)
                col_for_detail_name = list(dfForDetail)
                row_data = list(dfForDetail.values.tolist())
                # print(row_data)

                list_to_graph = []
                list_to_graph.append(col_for_detail_name)
                list_to_graph.append(row_data)
                # print(list_to_graph)
                fig = px.scatter(df_kmeans, x=first_col, y=second_col, color='Group')
                fig.write_image(my_path+'cluster'+first_col+second_col+'.png')
               
               

                qa_clustering['How can we cluster between '+ new.columns.values[0] +' and '+ new.columns.values[1]] = list()
                qa_clustering['How can we cluster between '+ new.columns.values[0] +' and '+ new.columns.values[1]].append(str(my_path)+'cluster'+first_col+second_col+'.png')
                qa_clustering['How can we cluster between '+ new.columns.values[0] +' and '+ new.columns.values[1]].append(list_to_graph)

                                                                                       

    return qa_clustering







