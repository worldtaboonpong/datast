import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn import tree
back={}
class DecisionTree():
    def cleandata(self,Data,Predict):
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
    def decisiontree(self, Dataframe, Target, input_n):
        model = tree.DecisionTreeClassifier()
        model.fit(Dataframe,Target)
        model.score(Dataframe,Target)
        result=model.predict(input_n)
        return result[0]
    def getanswer(self,x):
        return x #return here
    def __init__(self,df,ip):
        s=df.columns.tolist()
        d=[]
        predict=[]
        for i in ip:
            predict.append(ip[i])
            d.append(i)
        tg=list(set(s)-set(d))[0]
        column = df.pop(tg)
        df.insert(len(d), tg, column)
        Dataframe,Target,Input=self.cleandata(df,predict)
        answer=str(back[self.decisiontree(Dataframe,Target,Input.values.tolist())])
        self.getanswer(answer)


#Df=pd.read_csv(str(input("File : ")))
#Dict={}
#Dict['temp']='hot'
#Dict['humidity']='high'
#Dict['windy']=False
#Dict['play']='yes'
DecisionTree(Df,Dict)
