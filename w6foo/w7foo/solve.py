import numpy as np
from numpy import cos,sin
import matplotlib.pyplot as plt
from scipy import linalg

dd = np.array(((2,1,4,1),(3,4,-1,-1),(1,-4,1,5),(2,-2,1,3)))
v = np.array((-4,3,9,7))
print(dd)
w,x,y,z = linalg.inv(dd)@v
print(w,x,y,z)

# better
w,x,y,z = linalg.solve(dd,v)
print(w,x,y,z)
