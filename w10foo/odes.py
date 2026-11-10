"""ints.py 10/29/26  numerical integration"""
import numpy as np
from numpy import cos,sin
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp

def fun1(t,y):
    """Deriv function for an ODE"""
    dydt = -y**3 + sin(t)
    return dydt

y0 = [0.]

# Set time range and points for soln
nn = 200
ta = 0.0
tb = 10.
ts = np.linspace(ta,tb,nn)

# solve using solve_ivp
t_span = ts[0],ts[-1]
sol = solve_ivp(fun1,t_span,y0,t_eval=ts)
ys = sol.y[0]

# solve using euler
nne = 30
tse = np.linspace(ta,tb,nne)
h = (tb-ta)/(nne-1)
yse = np.zeros_like(tse)
yse[0] = y0[0]
for j in range(nne-1):
    tj = tse[j]
    yj = yse[j]
    yse[j+1] = yj + h*fun1(tj,yj)

# solve using RK2 on same time points
ys2 = np.zeros_like(tse)
ys2[0] = y0[0]
for j in range(nne-1):
    tj = tse[j]
    yj = ys2[j]
    k1 = h*fun1(tj,yj)
    k2 = h*fun1(tj + h/2, yj + k1/2)
    ys2[j+1] = yj + k2



plt.plot(ts,ys,label='solve_ivp')
plt.plot(tse,yse,'b.',label='Euler')
plt.plot(tse,ys2,'r.',label='RK2')
plt.legend()
plt.title(f'Using {nne} points')
plt.show()