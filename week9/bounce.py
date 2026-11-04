"""bounce.py 11/4/26 D.C.
Make picture of z(t) for a bouncing ball for HW9.
"""
import numpy as np
from numpy import sqrt
import matplotlib.pyplot as plt

TMAX = 10.   # time duration (s)
G = 9.8      # gravity (m/s^2)
R = 0.8      # resitituion coeff (-)

def physics(z0,v0,t):
    """The physics we want our DNN to learn.
    This version is free-fall of a mass with gravity, but bounces on
    a floor at z=0.  This version does not vectorize, must be called with
    scalar argumnents.
    """
    z = z0 + v0*t - G*t**2/2
    ctr=0
    while z<0:
        tb = (v0 + sqrt(v0**2 + 2*G*z0))/G
        vb = v0 - G*tb
        z0 = 0
        v0 = -R*vb
        t -= tb
        z = v0*t - G*t**2/2
    return z

if __name__=='__main__':
    Z0 = 20.
    V0 = 20.
    ts = np.linspace(0,TMAX,300)
    zs = np.zeros_like(ts)
    for i,t in enumerate(ts):
        zs[i] = physics(Z0,V0,t)
    plt.plot(ts,zs)
    plt.xlabel('t (s)')
    plt.ylabel('z (m)')
    plt.show()