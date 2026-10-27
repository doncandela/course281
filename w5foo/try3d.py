"""tryplot.py 9/28/26  Don Candela
try out plotting.
"""

import numpy as np
from numpy import cos,sin,sqrt,newaxis
import matplotlib.pyplot as plt

xs = np.linspace(-10,10,50)
ys = np.linspace(-10,10,50)[:,newaxis]
def f(x,y):
    r = sqrt(x**2+y**2)
    return cos(r)
fs = f(xs,ys)
print(fs.shape)

ax = plt.axes(projection='3d')
ax.plot_surface(xs,ys,fs)

# plt.plot(xs,ys)
plt.show()
