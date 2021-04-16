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
    def decisiontree(self,Dataframe, Target, input_n):
        model = tree.DecisionTreeClassifier()
        model.fit(Dataframe,Target)
        model.score(Dataframe,Target)
        result=model.predict(input_n)
        return result[0]
    def getanswer(self,x):
        return x #return here
    def __init__(self,df,ip):
        predict=[]
        for i in ip:
            predict.append(ip[i])
        Dataframe,Target,Input=self.cleandata(df,predict)
        answer=str(back[self.decisiontree(Dataframe,Target,Input.values.tolist())])
        self.getanswer(answer)

#Df=pd.read_csv(str(input("File : ")))
#Dict={}
#for i in range(len(list(Df))-1):
#    n=input(str(Df.columns[i])+" : ")
#    Dict[Df.columns[i]]=n
DecisionTree(Df,Dict)
