import pandas as pd 
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.decomposition import PCA
from operator import xor
import os

my_path = os.path.abspath(__file__)

df_beforecut = pd.read_excel('C:/Users/World/Documents/SeniorProject/datast/Clustering/untitled.xlsx')
df = df_beforecut.copy(deep=True)

range_n_clusters = list (range(2,10))

# print(df.head())

qa_clustering = {'จากไฟล์ สามารถแบ่งกลุ่มข้อมูลเป็นกี่กลุ่ม อย่างไรบ้าง':[]}


dataTypeDict = dict(df.dtypes)
# print(dataTypeDict)
for key in dataTypeDict:
    if (not xor(dataTypeDict[key] != 'int64',dataTypeDict[key] != 'float64')  #check if column is not integer or float
    or (dataTypeDict[key] == 'O')
    or (df[key].is_monotonic and (('ลำดับ' in key) or ( key == 'id')  )) #check if column is something like id or no.
    or ((key == 'year') or (key == 'ปี')) # check if column is year
    or ('รวม' in key)):
        df.drop(key, inplace=True,axis=1)
# print(df.head())
# print(df_beforecut.head())

difference_columns = set(df_beforecut.columns).difference(df.columns)
dfForDetail = df_beforecut[difference_columns]
dataTypeDictForDetail = dict(dfForDetail.dtypes)

for key in dataTypeDictForDetail:
    if (dfForDetail[key].is_monotonic and (('ลำดับ' in key) or ( key == 'id')  )) or ('รวม' in key) :
        dfForDetail.drop(key, inplace=True,axis=1)
# print(df_beforecut[difference_columns].columns.values)


# print(len(df.columns))
# Clustering each 2 columns of dataframe
# If there are more than 5 columns, exit()
if (len(df.columns) >= 2 and len(df.columns) <= 5 ):
    for i in range (len(df.columns)):
        for j in range (i+1,len(df.columns)) :

            
            # print(i,j)
            scores = []
            new_df = df.iloc[:,[i,j]]
            # print(new_df.head())
            # print(new_df.shape[0])
            # Do Silhouette Method to find best K to fit
            for n_cluster in range_n_clusters:
                if n_cluster > new_df.shape[0]-1:
                    break
                kmeans = KMeans(n_clusters=n_cluster)
                new = new_df._get_numeric_data()
                # print(new.head())
                kmeans.fit(new)
                predict=kmeans.fit_predict(new)
                score = silhouette_score(new , predict)
                scores.append(score)
            # Choose best score to cluster data
            best_cluster = range_n_clusters[scores.index(max(scores))]
            kmeans = KMeans(n_clusters=best_cluster)
            new = new_df._get_numeric_data()
            # print(new)
            kmeans.fit(new)
            predict=kmeans.fit_predict(new)
            df_kmeans = new_df.copy(deep=True)
            df_kmeans['Group'] = pd.Series(predict, index=df_kmeans.index)


 
            # Try to gert more detail to explain
            detailToExplain = ''
            for i in range (best_cluster):
                dfForGroupI = dfForDetail.loc[df_kmeans['Group'] == i]
                detailToExplain += ('กลุ่มที่ ' + str(i) + ' ได้แก่ ')
                # print(detailToExplain, dfForGroupI.shape[0])
                for j in range (dfForGroupI.shape[0]):
                    for k in range (dfForGroupI.shape[1]):
                        detailToExplain += dfForGroupI.columns.values[k] + str(dfForGroupI.iat[j,k]) + ' '
            

            
            # plt.rcParams['font.family'] = 'Tahoma'
            # df_kmeans.plot.scatter(new.columns.values[0],new.columns.values[1], c='Group', colormap='rainbow')
            # plt.title('Clustering by' + ' ' +new.columns.values[0] + ' ' + 'and' + ' ' + new.columns.values[1])
            # plt.savefig(my_path+'tograph'+str(i)+str(j)+'.png')
            # plt.show()
            
            qa_clustering['จากไฟล์ สามารถแบ่งกลุ่มข้อมูลเป็นกี่กลุ่ม อย่างไรบ้าง'].append(( 'การจัดกลุ่มระหว่าง' + 
            ' ' + new.columns.values[0] + ' ' + 'และ' + ' ' + new.columns.values[1] +' ' + 
            'สามารถแบ่งได้เป็น' + ' ' + str(best_cluster) + ' ' + 'กลุ่ม' + ' ' + 'ดังนี้' + ' ' + detailToExplain, 
            str(my_path) + 'tograph'+str(i)+str(j)+'.png'))



print(qa_clustering)







