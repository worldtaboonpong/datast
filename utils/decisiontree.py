import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn import tree
import math 
from decimal import Decimal
from operator import xor
import numpy as np
back={}

def cleandata(Data,Predict):
    Target=pd.DataFrame(Data[Data.columns[-1]])
    t1=Target.values.tolist()
    Tg=pd.DataFrame()
    Tg[str(Data.columns[-1])]=LabelEncoder().fit_transform(Target[Target.columns[0]])
    t2=Tg.values.tolist()
    for i in range(len(Tg)):
        if t2[i][0] not in back: back[t2[i][0]]=t1[i][0]
    Df=Data.drop(Data.columns[-1], axis='columns')
    Df.loc[len(Df)] = Predict
    for i in Df:
        Df[i] = Df[i].astype(str)
        Df[i]=LabelEncoder().fit_transform(Df[i])
    Dataframe = Df[:len(Df)-1]
    Input = Df[len(Df)-1:]
    return Dataframe, Tg, Input
def decisiontree(Dataframe, Target, input_n):
    model = tree.DecisionTreeClassifier()
    model.fit(Dataframe,Target)
    score=model.score(Dataframe,Target)
    result=model.predict(input_n)
    return [result[0],round(score*100,2)]
# def getanswer(self,x):
#     return x #return here
def getanswer(df,ip):
    s=df.columns.tolist()
    d=[]
    k=[]
    predict=[]
    df2=pd.DataFrame()
    for i in ip:
        d.append(i)
        predict.append(ip[i])
        k.append(i)
    tg=list(set(s)-set(k))[0]
    for j in range(len(d)):
        column = df.pop(d[j])
        df2.insert(j, d[j], column)
    column = df.pop(tg)
    df2.insert(len(d), tg, column)
    Dataframe,Target,Input=cleandata(df2,predict)
    answer=str(back[decisiontree(Dataframe,Target,Input.values.tolist())[0]])
    score=decisiontree(Dataframe,Target,Input.values.tolist())[1]
    # self.getanswer(answer)
    return [answer,score]

def cleanDataframe(dfToClean):
    cleandf = dfToClean.copy(deep=True)
    dataTypeDict = dict(cleandf.dtypes)
    for key in dataTypeDict:
        if ((cleandf[key].is_monotonic and (('ลำดับ' in key) or (key == 'id')))
        or ((not xor(dataTypeDict[key] != 'int64', dataTypeDict[key] != 'float64')) and cleandf[key].is_unique)
        or ((key == 'year') or (key == 'ปี'))
        or ((key == 'month') or (key == 'เดือน'))
        or ((key == 'day') or (key == 'วันที่') and dataTypeDict[key] != 'O')):      
             cleandf.drop(key,inplace=True,axis=1)
    df1=pd.DataFrame()
    for col_name in cleandf:
        values=[]
        if (cleandf[col_name].dtype == 'int64' or cleandf[col_name].dtype == 'float64'):
            v_max = cleandf[col_name].max()
            v_min = cleandf[col_name].min()
            v_range = (v_max)-(v_min)
            sample = cleandf.shape[0]
            v_floor = math.ceil(1+3.322*math.log10(sample))
            interval = math.ceil(v_range/v_floor)
            start = v_min
            value=[]
            for i in range(v_floor):
                b=start+interval
                value.append([round(start,2),round(start+interval,2)])
                start+=interval
            for j in cleandf[col_name]:
                for k in range(len(value)):
                    if value[k][0] <= j and j<=value[k][1]:
                        values.append('ช่วง '+str(value[k][0])+' ถึง '+str(value[k][1]))
                        break
            df1[str(col_name)]=values
            cleandf[str(col_name)]=df1[str(col_name)]
    if len(cleandf.columns) <= 2:
        return
    return cleandf


# df = pd.read_excel('sampledatafoodsales.xlsx')
# df_after_clean = cleanDataframe(df)
# #print(df_after_clean.loc[0])
# dict = {'City':'Boston', 'Category': 'Bars','TotalPrice':'ช่วง 33.6 ถึง 121.6', 'Quantity': 'ช่วง 20 ถึง 52','Region':'East','UnitPrice':'ช่วง 1.35 ถึง 2.35'}
# DecisionTree = DecisionTree()
# print(DecisionTree.getanswer(df_after_clean,dict))
# # City,Boston Category,Bars Product,Carrot Quantity,ช่วง 20 ถึง 52 UnitPrice,ช่วง 1.35 ถึง 2.35 TotalPrice,ช่วง 33.6 ถึง 121.6
