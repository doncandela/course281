"""fitting.py 10/13/26
P281 week-6 stuff."""

import numpy as np
from numpy import sqrt,cos,sin
import matplotlib.pyplot as plt
import pandas as pd
from dfit import Dfit

# read data1.xlsx and list its columns
df = pd.read_excel('data1.xlsx')
print(list(df))

# make columns into numpy arrays and plot
c1,c2,c3 = list(df)
xs = df[c1].to_numpy()
ys = df[c2].to_numpy()
yerrs = df[c3].to_numpy()


# write a linear model function
def linmod(x,p0,p1):
    """Model function: linear function of x."""
    return p0 + p1*x

# write a polynomial model function
def polymod(x,p0,p1,p2,p3,p4):
    """Model function: polynomial function of x
    up to x**4."""
    return (p0 + p1*x + p2*x**2 + p3*x**3
            + p4*x**4)

# plot data along with model
# plt.plot(xs,ys,'bo')
# plt.errorbar(xs,ys,yerrs,fmt='bo',capsize=5)
# plt.xlabel(c1)
# plt.ylabel(c2)

# xmods = np.linspace(-1,11,300)
# p0 = 40.0
# p1 = -2.0 # guess params
# ymods = linmod(xmods,p0,p1)
# plt.plot(xmods,ymods,'r-')

# plt.show()

linfit = Dfit(polymod,xs,ys,yerrs,varies=(True,True,True,True))
linfit.plotfit()
linfit.printfit()
