"""dplots.py 9/28/26  Don Candela
try out density plots.
"""

import numpy as np
from numpy import cos,sin,sqrt,newaxis
import matplotlib.pyplot as plt

cat = plt.imread('cat.jpg').copy()
# print(cat[:5,:5])

cat[:,:,0] = 0

plt.imshow(cat)
plt.show()