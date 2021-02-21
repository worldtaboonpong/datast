# from Clustering.func_clustering import clustering 
# from Statistics.StatisticFunction import statistics
from decisiontree.func_cleanexcel import cleanDataframe
# from AssociationRule.assocrule import association

import pandas as pd

df = pd.read_excel('./MRTuser.xlsx' , 'สายฉลองรัชธรรม'  )

# qa_clustering = clustering(df)
# qa_statistic = statistics(df)
dfAfterClean = cleanDataframe(df)
print(dfAfterClean.columns)

# print(qa_clustering)
# print(qa_statistic)