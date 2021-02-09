if (xor(dataTypeDict[key] != 'int64',dataTypeDict[key] != 'float64')  #check if column is not integer
    # or (dataTypeDict[key] == 'O')
    # or (df[key].is_monotonic and (('ลำดับ' in key) or ( key == 'id')  )) #check if column is something like id or no.
    # or ((key == 'year') or (key == 'ปี')) # check if column is year
    # or ('รวม' in key)):
    #     df.drop(key, inplace=True,axis=1)