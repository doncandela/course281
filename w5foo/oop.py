"""dplots.py 9/28/26  Don Candela
try out density plots.
"""

import numpy as np
from numpy import cos,sin,sqrt,newaxis
import matplotlib.pyplot as plt


class Par:
    """Object to represent a point particle"""
    def __init__(self,x=0,y=0):
        """supply x,y coords of the particle"""
        self.x = x
        self.y = y

def showps(plist):
    for p in plist:
        plt.plot(p.x,p.y,'mo')
    ax = plt.gca()
    ax.set_aspect('equal')
    plt.show() 

#plist = [Par(x,x**2) for x in np.linspace(-5,5,20)]
plist=[]
for x in np.linspace(-10,10,50):
    for y in np.linspace(-10,10,50):
        r = sqrt(x**2+y**2)
        if r>7:
            plist.append(Par(x,y))
showps(plist)