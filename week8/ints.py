"""ints.py 10/29/26  numerical integration"""
import numpy as np
from numpy import cos,sin


def trap(f,a,b,nn):
    """simpsons-rule integration of f from a to b with
    nn slices"""
    h = (b-a)/nn
    wts = np.ones(nn+1)
    wts[0] = 0.5
    wts[-1] = 0.5
    xs = np.linspace(a,b,nn+1)
    # print(wts)
    fs = f(xs)
    return h*np.sum(fs*wts)

def simps(f,a,b,nn):
    """simpsons-rule integration of f from a to b with
    nn slices"""
    if nn%2:
        nn += 1
        print('nn was odd, increased')
    h = (b-a)/nn
    wts = 4*np.ones(nn+1)
    wts[::2] = 2
    wts[0] = 1
    wts[-1] = 1
    xs = np.linspace(a,b,nn+1)
    # print(wts)
    fs = f(xs)
    return (h/3)*np.sum(fs*wts)

def igrnd(x):
    return sin(x)

b =  3.0
print(f'exact: {1-cos(b)}')
for nn in (6,10,21):
    print(f'trap result with {nn} slices = {trap(igrnd,0,b,nn)}')
    print(f'simps result with {nn} slices = {simps(igrnd,0,b,nn)}')