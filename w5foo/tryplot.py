"""tryplot.py 9/28/26  Don Candela
try out plotting.
"""

import numpy as np
from numpy import cos,sin
import matplotlib.pyplot as plt

xs = np.linspace(-10,10,300)
ys = cos(xs)

plt.plot(xs,ys)
# plt.show()

ys2 = sin(xs)

plt.plot(xs,ys2)
plt.show()