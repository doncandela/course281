"""linalg.py 10/20/26  Don Candela
try out fitting.
"""
import numpy as np
from numpy import cos,sin
import matplotlib.pyplot as plt
from scipy import linalg

# ii3 = np.eye(3)
# print(ii3)

dd = np.array(((2,-1),(-1,2)))
print(dd)
evals,evecs = linalg.eigh(dd)
print(evecs[0],evals[0])
print(evecs[1],evals[1])
