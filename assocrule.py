import pandas as pd
import numpy as np
import json
import matplotlib.pyplot as plt
from apyori import apriori

dff = pd.read_excel("./covid19.xls")
df = dff.select_dtypes(exclude=[np.datetime64])
df.replace('', np.nan, inplace=True)
df.dropna(inplace=True)
(col,row) = df.shape

records = []
for i in range(1, col):
    records.append([str(df.values[i,j]) for j in range(0, row)])

config_dict = {}
# customizable
config_dict["min_support"] = 0.01
config_dict["min_confidence"] = 0.4
config_dict["min_lift"] = 6
config_dict["min_length"] = 2

association_rules = apriori(records, min_support=config_dict["min_support"], min_confidence=config_dict["min_confidence"],
     min_lift=config_dict["min_lift"], min_length=config_dict["min_length"])
association_results = list(association_rules)

output_dict = {}
data_list = []
output_dict['Config'] = config_dict
output_dict['Data'] = data_list

graph_coord = []
def byLift(e) :
    return e[2]

i=0
for item in association_results:
    rule_dict = {}
    i += 1

    #print("Rule No.: " + str(i)) 
    rule_dict['No'] = i

    # first index of the inner list
    # Contains base item and add item
    pair = item[0] 
    items = [x for x in pair]
    rule_dict['From'] = items[0]
    rule_dict['To'] = items[1]

    # second index of the inner list
    rule_dict['Support'] = item[1]

    # third index of the list located at 0th of the third index of the inner list
    rule_dict['Confidence'] = item[2][0][2]
    rule_dict['Lift'] = item[2][0][3]

    data_list.append(rule_dict)    

    # for graph plotting
    graph_coord.append((items[0], items[1], item[2][0][3])) #(From, To, Lift)

graph_coord.sort(reverse=True, key=byLift) # sort by Lift, descending order
for e in graph_coord :
    print("From:" + str(e[0]) + " To:" + str(e[1]) + " Lift:" + str(e[2]))

with open("output.txt", "w", encoding="utf-8-sig") as text_file:
    text_file.write(json.dumps(output_dict, ensure_ascii=False, indent = 4))