"""fitting.py 10/13/26
P281 week-6 stuff."""

import numpy as np
from numpy import sqrt,cos,sin
import matplotlib.pyplot as plt
import pandas as pd
from dfit import Dfit

# read data1.xlsx and list its columns
df = pd.read_excel('wavedata.xlsx')
print(list(df))

# make columns into numpy arrays and plot
c1,c2 = list(df)
ts = df[c1].to_numpy()
ys = df[c2].to_numpy()
# plt.plot(xs,ys,'m+')
# plt.xlabel(c1)
# plt.ylabel(c2)
# plt.show()

def wmod(t,aa,omega,phi,bb):
    """Model function: oscillation."""
    return aa*cos(omega*t + phi) + bb

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

wfit = Dfit(wmod,ts,ys,p0s=(0,0.6))
wfit.printfit()
wfit.plotfit()
