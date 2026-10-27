"""subplots.py 9/28/26  Don Candela
try out subplots.
"""

import numpy as np
from numpy import cos,sin
import matplotlib.pyplot as plt

# plot x**n for n=1,2,3,4 in subplots

xs = np.linspace(-1,1,300)

plt.subplot(221)   # 2 cols, 2 rows, plot 1
plt.plot(xs,xs**1)

plt.subplot(222)   # 2 cols, 2 rows, plot 2
plt.plot(xs,xs**2)

plt.subplot(223)   # 2 cols, 2 rows, plot 3
plt.plot(xs,xs**3)

plt.subplot(224)   # 2 cols, 2 rows, plot 4
plt.plot(xs,xs**4)

plt.show()