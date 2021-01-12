import pandas as pd
import numpy as np

df = pd.read_excel("./harmful30jun2020.xls")
digitdf = df.select_dtypes(include=[np.number])
print(digitdf)