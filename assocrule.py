import pandas as pd
import numpy as np
import json
import matplotlib.pyplot as plt
from apyori import apriori

dff = pd.read_excel("./covid19.xls")

def association(df, min_support, min_confidence, min_lift, min_length, max_show) :
    df = dff.select_dtypes(exclude=[np.datetime64])
    df.replace(r'^\s+$', np.nan, regex=True)
    df.dropna(inplace=True)
    (col,row) = df.shape

    records = []
    for i in range(1, col):
        records.append([str(df.values[i,j]) for j in range(0, row)])

    config_dict = {}
    # customizable
    config_dict["min_support"] = min_support
    config_dict["min_confidence"] = min_confidence
    config_dict["min_lift"] = min_lift
    config_dict["min_length"] = min_length
    max_show = max_show  # Maximum amount of result shown

    association_rules = apriori(records, min_support=config_dict["min_support"], min_confidence=config_dict["min_confidence"],
        min_lift=config_dict["min_lift"], min_length=config_dict["min_length"])
    association_results = list(association_rules)

    output_dict = {}
    data_list = []
    output_dict['Config'] = config_dict
    output_dict['Data'] = data_list

    sorted_result = []
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
        sorted_result.append((items[0], items[1], item[2][0][3])) # (From, To, Lift)

    sorted_result.sort(key=byLift)    # sort by Lift, ascending order
    result_nodup = {}   # remove duplicate
    for i in sorted_result :
        result_nodup[(i[0], i[1])] = i[2]

    sorted_result = list(result_nodup.items())
    sorted_result.reverse()     # sort by Lift, descending order  / List looks like (( From, To ) , Lift)

    graph_coord = sorted_result[:max_show]
    #graph_coord = []
    #for i in range(max_show) :
    #    graph_coord.append(sorted_result[i])   # create another list for plotting graph, with limited amount of result

    graph_assoc = []
    graph_lift = []
    for e in graph_coord :
        graph_assoc.append(str(e[0][0]) + "," + str(e[0][1]))
        graph_lift.append(e[1])
        #print("From:" + str(e[0]) + " To:" + str(e[1]) + " Lift:" + str(e[2]))

    # graph plotting
    
    #plt.rc('font', **{'sans-serif' : 'Arial', 'family' : 'sans-serif'})
    #plt.scatter(graph_assoc, graph_lift)
    #plt.xlabel('Association') # Likelihood of the first to happen with the second, rather than the second happenning alone
    #plt.ylabel('Lift')
    #plt.suptitle('Shows the correlation between 2 elements')
    #plt.show()
    
    qa = {}
    for e in graph_coord :
        q = "What is the likelihood of " + str(e[0][1]) + " happening along with " + str(e[0][0]) + " rather than happening alone?"
        qa[q] = str(e[1]) + " times more likely"

    with open("assocqa.txt", "w", encoding="utf-8-sig") as text_file:
        text_file.write(json.dumps(qa, ensure_ascii=False, indent = 4))

    with open("output.txt", "w", encoding="utf-8-sig") as text_file:
        text_file.write(json.dumps(output_dict, ensure_ascii=False, indent = 4))

association(df, 0.01, 0.4, 6, 2, 20)