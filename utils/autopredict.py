import pandas as pd

df = pd.read_excel('sampledatafoodsales.xlsx')

def autoPredict(df):

    # df_after_clean = cleanDataframe(df)
    # columns = list(df_after_clean)
    dataTypeDict = dict(df.dtypes)

    for key in dataTypeDict:
        if ((df[key].is_monotonic and (('ลำดับ' in key) or (key == 'id' or key == 'Id')))
            or (key == 'Id')
            or ((key == 'Year') or (key == 'YEAR') or (key == 'year') or (key == 'ปี'))  # check if column is year
            or ((key == 'Month') or  (key == 'MONTH') or (key == 'month') or (key == 'เดือน')) # check if column is month
            or (('รวม' in key) or ('total' in key) or ('Total' in key))
            or len(set(df[key]))==1 
            or ((key == 'day') or (key == 'วันที่') and dataTypeDict[key] != 'O')
            or dataTypeDict[key] == 'datetime64[ns]'):
            df.drop(key, inplace=True, axis=1)

    str_col = []
    num_col = []
    for col_name in df:
        if (df[col_name].dtype == 'int64' or df[col_name].dtype == 'float64'):
            num_col.append(col_name)
        else :
            str_col.append(col_name)

    if (len(str_col)) <1 or (len(num_col) <1) :
        return

    for group in str_col:
        data = (df.groupby(group))[num_col[0]].max()
        print (data)


    # # call decision tree
    # predicter = DecisionTree()
    # # get answer
    # # will throw df and dict as parameter
    # answer = predicter.getanswer()

    return

autoPredict(df)