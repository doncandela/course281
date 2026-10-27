"""oop.py 10/8/26  Don Candela
try out OOP
"""

import numpy as np
from numpy import cos,sin,sqrt,newaxis
import matplotlib.pyplot as plt
import pandas as pd


class Spammer:
    def __init__(self,x):
        self.x = x
    def pr(self,n):
        print(n*self.x)
# make two Spammer's:
hah = Spammer('hah ')
hee = Spammer('hee ')

# class inheritance
class Eggs(Spammer):
    def __init__(self):
        super().__init__('Eggs! ')
    def pr(self,n):
        super().pr(n)
        print('That\'s all')

class Part:
    """Class to represent a particle at position x,y.
    """
    def __init__(self,x=0.,y=0.):
        self.x = x
        self.y = y

def showparticles(allparts):
    """Plot the positions of the Particles in the list allparts.
    """
    for p in allparts:
        plt.plot(p.x,p.y,'mo')
    plt.show()

ps = []
for x in np.linspace(-3,3,50):
    for y in np.linspace(-3,3,50):
        r = sqrt(x**2+y**2)
        if r < 2:
            ps.append(Part(x,y))
ax = plt.gca()
ax.set_aspect('equal')
showparticles(ps)