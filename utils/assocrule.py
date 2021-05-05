import pandas as pd
import numpy as np
import json
import plotly.graph_objects as go
import os
from apyori import apriori

#dataframe = pd.read_excel("./AssociationRule/covid19.xls")
#dataframe = pd.read_excel('./MRTuser.xlsx' , 'สายฉลองรัชธรรม'  )
# dataframe = pd.read_excel('./sampledatafoodsales.xlsx', 'FoodSales'  )

def association(dataframe, min_support=0.01, min_confidence=0.2, min_lift=2, min_length=2) :
    image_path = "static"

    df = dataframe.select_dtypes(exclude=[np.datetime64, np.number])
    df.replace(r'^\s+$', np.nan, regex=True)
    df.dropna(inplace=True)
    newdf = df.copy(deep=True)
    for c in newdf.columns:
        newdf[c] = newdf[c].apply(lambda s: "{} in {}".format(s,c))

    (col,row) = newdf.shape

    records = []
    #for i in range(1, col):
        #records.append([str(newdf.values[i,j]) for j in range(0, row)])
    for i in range(1, col):
        temp = []
        for j in range(0, row):
            val = str(newdf.values[i,j])
            if not ( val == "" or val == "-" or val == " " ):
                temp.append(val)
        records.append(temp)

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
    data_dict = {}
    data_list_sorted = []
    output_dict['Config'] = config_dict
    
    def byLift(e) :
        return e[1][2]

    i=0
    for item in association_results:
        pair = item[0] 
        items = [x for x in pair]
        # From = items[0]        # X
        # To = items[1]          # Y
        # Support = item[1]      # Y / Total
        # Confidence = item[2][0][2]     # X&Y / X
        # Lift = item[2][0][3]           # Confidence X -> Y / Support Y
        if item[2][0][2] < 1 :           # Confidence Must not be 1.0
            data_dict[(items[0], items[1])] = (item[1], item[2][0][2], item[2][0][3])   # ((From, To) , (Support, Confidence, Lift))

    data_list_sorted = list(data_dict.items())
    data_list_sorted.sort(key=byLift, reverse=True)     # sort by Lift, descending order  / List looks like ((From, To) , (Support, Confidence, Lift))
    
    data_dict = []
    i=0
    for item in data_list_sorted :
        rule = {}
        i += 1
        rule['No'] = i
        rule['From'] = item[0][0]
        rule['To'] = item[0][1]
        rule['Support'] = item[1][0]
        rule['Confidence'] = item[1][1]
        rule['Lift'] = item[1][2]

        data_dict.append(rule)

    output_dict['Data'] = data_dict

    for f in os.listdir(image_path):
        if not f.startswith("asso"):
            continue
        os.remove(os.path.join(image_path, f))

    qa = {}
    for i in output_dict['Data'] :
        fig = go.Figure()
        supp = i["Support"]
        conf = i["Confidence"]
        x = ["Confidence", "Support"]
        y = [conf, supp]
        yn = [1-conf, 1-supp]
        image_loc = image_path + "/asso" + str(i['No']) + str(i['From']).replace(" ", "") + str(i['To']).replace(" ", "") + ".png"

        fig.add_bar(x=x, y=y, name='Occurrence')
        fig.add_bar(x=x, y=yn, name='Non-occurrence', text=y)
        fig.update_layout(barmode="stack")
        fig.update_traces(textposition='outside')
        fig.update_layout(uniformtext_minsize=11, uniformtext_mode='hide', margin=dict(l=10,r=10,t=40,b=20))
        fig.write_image(image_loc, width= 700, height= 500, scale=1.5)
        
        q = "What is the connection between " + str(i['From']) + " and " + str(i['To'])
        qa[q] = ["The probability of " + str(i['From']) + " happening together with " + str(i['To']) + " is " + str("{:.2f}".format(100 * i['Lift'] / (i['Lift'] + 1))) + " %",
                  image_loc]        

    return qa

# association(dataframe)