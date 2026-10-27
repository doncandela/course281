"""week4.py  10/1/26  D.C.
stuff for week 4
"""

import numpy as np
from numpy import sqrt,cos,sin
import matplotlib.pyplot as plt

xs = np.linspace(-10,10,300)
ys = cos(xs)
plt.plot(xs,ys)
plt.xlabel(r'$\pi\ \Delta\ \delta$',size=15)
plt.ylabel(r'$\cos(x)$',size=15)
plt.show()