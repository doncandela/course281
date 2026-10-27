"""subplots.py 9/28/26  Don Candela
try out pandas.
"""

import numpy as np
from numpy import cos,sin
import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_excel('gl2_missing.xlsx')
# print(type(df))
# print(list(df))
xs = df['x'].to_numpy()
ys = df['y'].to_numpy()
print(ys)
plt.plot(xs,ys,'bo-')
plt.show()