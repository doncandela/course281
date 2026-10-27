"""fitting.py 10/13/26  Don Candela
try out fitting.
"""
import numpy as np
from numpy import cos,sin
import matplotlib.pyplot as plt
import pandas as pd
from dfit import Dfit

# read data file and print the column names
data1 = pd.read_excel('wavedata.xlsx')
print(list(data1))

# extract to arrays
c0,c1 = list(data1)
ts = data1[c0].to_numpy()
ys = data1[c1].to_numpy()
# yerrs = data1[c2].to_numpy()

# plot the data
# plt.errorbar(xs,ys,yerrs,fmt='bo',capsize=5)
# plt.plot(ts,ys,'g+')
# plt.xlabel(c0)
# plt.ylabel(c1)
# plt.show()

# define a fitting function
def wmod(t,aa,omega,phi,bb):
    """osc model"""
    return aa*cos(omega*t + phi) + bb
 
# use Dfit to fit the data
linfit = Dfit(wmod,ts,ys,p0s=[0,0.6])
linfit.printfit()
linfit.plotfit()
