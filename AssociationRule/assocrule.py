import pandas as pd
import numpy as np
#import json
from apyori import apriori

#dataframe = pd.read_excel("./AssociationRule/covid19.xls")
#dataframe = pd.read_excel('./MRTuser.xlsx' , 'สายฉลองรัชธรรม'  )

def association(dataframe, min_support=0.01, min_confidence=0.4, min_lift=6, min_length=2) :
    df = dataframe.select_dtypes(exclude=[np.datetime64, np.number])
    df.replace(r'^\s+$', np.nan, regex=True)
    df.dropna(inplace=True)
    newdf = df.copy(deep=True)
    for c in newdf.columns:
        newdf[c] = newdf[c].apply(lambda s: "{} in {}".format(s,c))

    (col,row) = newdf.shape

    records = []
    for i in range(1, col):
        records.append([str(newdf.values[i,j]) for j in range(0, row)])

    config_dict = {}
    # customizable
    config_dict["min_support"] = min_support
    config_dict["min_confidence"] = min_confidence
    config_dict["min_lift"] = min_lift
    config_dict["min_length"] = min_length
    #config_dict["max_show"] = max_show  # Maximum amount of result shown

    association_rules = apriori(records, min_support=config_dict["min_support"], min_confidence=config_dict["min_confidence"],
        min_lift=config_dict["min_lift"], min_length=config_dict["min_length"])
    association_results = list(association_rules)

    output_dict = {}
    data_list = []
    output_dict['Config'] = config_dict
    output_dict['Data'] = data_list

    apriori_result = []
    def byLift(e) :
        return e[1]

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
        apriori_result.append((items[0], items[1], item[2][0][3])) # (From, To, Lift)

    result_nodup = {}   # remove duplicate
    for i in apriori_result :
        result_nodup[(i[0], i[1])] = i[2]

    list_nodup = list(result_nodup.items())
    list_nodup.sort(key=byLift, reverse=True)     # sort by Lift, descending order  / List looks like (( From, To ) , Lift)

    qa = {}
    for e in list_nodup :
        q = "What is the connection between " + str(e[0][1]) + " and " + str(e[0][0])
        qa[q] = "Probability of " + str(e[0][1]) + " happening together with " + str(e[0][0]) + " is " + str(e[1]) + " times more likely than to happen by itself"
    #print(len(qa))

    #with open("assocqa.txt", "w", encoding="utf-8-sig") as text_file:
        #text_file.write(json.dumps(qa, ensure_ascii=False, indent = 4))

    #with open("output.txt", "w", encoding="utf-8-sig") as text_file:
        #text_file.write(json.dumps(output_dict, ensure_ascii=False, indent = 4))

    return qa

#association(dataframe)