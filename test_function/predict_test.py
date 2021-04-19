import pandas as pd
import os, sys
sys.path.insert(0, os.path.abspath("C:/Users/World/Documents/SeniorProject/datast/decisiontree"))
from decisiontree.func_cleanexcel import cleanDataframe
from decisiontree.decisiontree import DecisionTree


df = pd.read_excel('MRTuser.xlsx')
df_after_clean = cleanDataframe(df)
dict = {'จำนวนผู้โดยสารรวม': 'ช่วง 1231255 ถึง 1429320', 'จำนวนผู้โดยสารเฉลี่ยรายวัน': 'ช่วง 46300 ถึง 52632', 'จำนวนผู้โดยสารเฉลี่ยรายวันธรรมดา': 'ช่วง 40333 ถึง 47777', 'จำนวนผู้โดยสารเฉลี่ยรายวันหยุด': 'ช่วง 11956 ถึง 17115'}
DecisionTree = DecisionTree()
print(DecisionTree.showAnswer(df_after_clean,dict))