"""dplots.py 9/28/26  Don Candela
try out density plots.
"""
import numpy as np
from numpy import cos,sin,sqrt,newaxis
import matplotlib.pyplot as plt
import pandas as pd
from dfit import Dfit

df = pd.read_excel('falldata.xlsx')
hs = df['height (m)'].to_numpy()
ts = df['time (s)'].to_numpy()


# plot the data
plt.plot(hs,ts,'go')
plt.xlabel('h (m)')
plt.ylabel('t (s)')

# make a physics model
def tfall(h,h0,g):
    t = sqrt(2*(h0-h)/g)
    return t

# plot the model with guessed constants
H0 = 2.2
G = 9.8

hmods = np.linspace(0,2,300)
tmods = tfall(hmods,H0,G)
plt.plot(hmods,tmods,'b-')

plt.show()

fallfit = Dfit(tfall,hs,ts,p0s=[2.2,9.8])
fallfit.plotfit()
fallfit.printfit()
