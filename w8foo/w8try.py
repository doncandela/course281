import numpy as np
from numpy import cos,sin,pi
import matplotlib.pyplot as plt

from scipy.integrate import quad


def trap(f,a,b,nn):
    wts = np.ones(nn+1)
    wts[0] = 0.5
    wts[1] = 0.5
    xs = np.linspace(a,b,nn+1)
    fs = f(xs)
    h = (b-a)/nn
    return h*sum(wts*fs)

def simps(f,a,b,nn):
    if nn%2:
        nn += 1
        print(f'simps: increased nn to {nn}')
    wts = 4*np.ones(nn+1)
    wts[::2] = 2
    wts[0] = 1
    wts[-1] = 1
    # print(wts)
    xs = np.linspace(a,b,nn+1)
    fs = f(xs)
    h = (b-a)/nn
    return (h/3)*sum(wts*fs)



def igr(x):
    return sin(x)

for a in (0.1, 3, pi/2):
    exact = 1 - cos(a)
    tint = trap(igr,0,a,20)
    sint = simps(igr,0,a,21)
    qint = quad(igr,0,a)
    print(f'for a = {a} exact = {exact}\n'
          f'        trap gives {tint}\n'
          f'        simps gives {sint}\n'
        f'        quad gives {qint}')