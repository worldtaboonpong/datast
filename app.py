from Clustering.func_clustering import clustering 
from Statistics.StatisticFunction import statistics
from AssociationRule.assocrule import association

import pandas as pd

df = pd.read_excel('./MRTuser.xlsx' , 'สายฉลองรัชธรรม'  )

qa_clustering = clustering(df)
qa_statistic = statistics(df)
qa_assoocrule = association(df)
qa={**qa_clustering,**qa_statistic,**qa_assoocrule}

keyList = list(qa.keys())

print(keyList)