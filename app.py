from Clustering.func_clustering import clustering 
from Statistics.StatisticFunction import statistics
from AssociationRule.assocrule import association

import pandas as pd

df = pd.read_excel('./MRTuser.xlsx' , 'สายฉลองรัชธรรม'  )
#df = pd.read_excel("./AssociationRule/covid19.xls")

qa_clustering = clustering(df)
qa_statistic = statistics(df)
qa_assoocrule = association(df) # default association(dataframe, min_support=0.01, min_confidence=0.4, min_lift=6, min_length=2)
qa={**qa_clustering,**qa_statistic,**qa_assoocrule}

keyList = list(qa.keys())

print(keyList)