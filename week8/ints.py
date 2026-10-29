"""ints.py 10/27/26  numerical integration"""
import numpy as np
from numpy import cos,sin

def trap(f,a,b,nn):
    """trapeziod-rule integration of f from a to b with
    nn slices"""
    h = (b-a)/nn
    wts = np.ones(nn+1)
    wts[0] = 0.5
    wts[-1] = 0.5
    xs = np.linspace(a,b,nn+1)
    # print(wts)
    fs = f(xs)
    return h*np.sum(fs*wts)

def igrnd(x):
    return sin(x)

b =  3.0
print(f'exact: {1-cos(b)}')
for nn in (5,10,20):
    print(f'trap result with {nn} slices = {trap(igrnd,0,b,nn)}')