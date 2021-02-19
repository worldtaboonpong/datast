import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn import tree
back={}
def CleanData(Data,Predict):
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

def DecisionTree(Dataframe, Target, input_n):
    model = tree.DecisionTreeClassifier()
    model.fit(Dataframe,Target)
    model.score(Dataframe,Target)
    result=model.predict(input_n)
    return result[0]

df=pd.read_csv(str(input("File : ")))
predict=[]
for i in range(len(list(df))-1):
    n=input(str(df.columns[i])+" : ")
    predict.append(n)
Dataframe,Target,Input=CleanData(df,predict)
print("Answer : "+str(back[DecisionTree(Dataframe,Target,Input.values.tolist())]))
#data must only have categorized columns only and last column must be target


