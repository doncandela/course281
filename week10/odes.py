"""odes.py 11/10/26"""
import numpy as np
from numpy import cos,sin
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp

# define the ODE
def fun1(t,y):
    """derivative func"""
    dydt = -y**3 + sin(t)
    return dydt

# domain
ta = 0.
tb =10.
# IC
y0 = [0.]      # need list for solve_ivp

# Solve with solve_ivp
nnivp = 300
ts = np.linspace(ta,tb,nnivp)
t_span = ts[0],ts[-1]
sol = solve_ivp(fun1,t_span,y0,t_eval=ts)
ys = sol.y[0] # solution is 1st and only row

# solve with Euler
nn = 30
tes = np.linspace(ta,tb,nn)
h = (tb-ta)/(nn-1)
yes = np.zeros_like(tes)
yes[0] = y0[0]     # set ic (y0 is a list)
for j in range(nn-1):
    tj = tes[j]
    yj = yes[j]
    yes[j+1]= yj + h*fun1(tj,yj)

# solve with RK2 on same time points
y2s = np.zeros_like(tes)
y2s[0] = y0[0]     # set ic (y0 is a list)
for j in range(nn-1):
    tj = tes[j]
    yj = y2s[j]
    k1 = h*fun1(tj,yj)
    k2 = h*fun1(tj+h/2,yj+k1/2)
    y2s[j+1]= yj + k2

plt.plot(ts,ys,label='solve_ivp')
plt.plot(tes,yes,'b.',label='Euler')
plt.plot(tes,y2s,'r.',label='RK2')
plt.legend()
plt.xlabel('t')
plt.ylabel('y')
plt.title(f'Using {nn} points')
plt.show()


