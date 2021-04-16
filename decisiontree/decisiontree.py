import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn import tree
import math 
from decimal import Decimal
from operator import xor
import numpy as np

back={}
class DecisionTree:

    def CleanData(self,Data,Predict):
        Target=pd.DataFrame(Data[Data.columns[-1]])
        t1=Target.values.tolist()
        Tg=pd.DataFrame()
        Tg['play']=LabelEncoder().fit_transform(Target[Target.columns[0]])
        t2=Tg.values.tolist()
        for i in range(len(Tg)):
            if t2[i][0] not in back: back[t2[i][0]]=t1[i][0]
        #------target must be last column
        Df=Data.drop(Data.columns[-1], axis='columns')
        Df.loc[len(Df)] = Predict
        for i in Df:
            Df[i] = Df[i].astype(str)
            Df[i]=LabelEncoder().fit_transform(Df[i])
        Dataframe = Df[:len(Df)-1]
        Input = Df[len(Df)-1:]
        return Dataframe, Tg, Input
    def decisiontree(self,Dataframe, Target, input_n):
        model = tree.DecisionTreeClassifier()
        model.fit(Dataframe,Target)
        model.score(Dataframe,Target)
        result=model.predict(input_n)
        return result[0]
    def showAnswer(self,Df, Dc):
        Dcs=[]
        for i in Dc:
            Dcs.append(Dc[i])
        Dataframe,Target,Input=self.CleanData(Df,Dcs)
        return ("Answer : "+str(back[self.decisiontree(Dataframe,Target,Input.values.tolist())]))

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


df = pd.read_excel('MRTuser.xlsx')
df_after_clean = cleanDataframe(df)
dict = {'จำนวนผู้โดยสารรวม': 'ช่วง 1231255 ถึง 1429320', 'จำนวนผู้โดยสารเฉลี่ยรายวัน': 'ช่วง 46300 ถึง 52632', 'จำนวนผู้โดยสารเฉลี่ยรายวันธรรมดา': 'ช่วง 40333 ถึง 47777', 'จำนวนผู้โดยสารเฉลี่ยรายวันหยุด': 'ช่วง 11956 ถึง 17115'}
#df=pd.read_csv(str(input("File : ")))
#predict=[]
#for i in range(len(list(df))-1):
#    n=input(str(df.columns[i])+" : ")
#    predict.append(n)
DecisionTree = DecisionTree()
print(DecisionTree.showAnswer(df_after_clean,dict))
#Call init

