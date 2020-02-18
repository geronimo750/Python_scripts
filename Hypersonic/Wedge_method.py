import numpy as np
import matplotlib.pyplot as plt
from sympy import *


beta=symbols('beta')
theta=np.deg2rad(37)
M=8

# expr=((M**2)*(sin(beta))**2-1-(1.4+1)/2*(M**2)*(sin(beta)*sin(theta))/cos(beta-theta))
expr = Eq((M**2)*(sin(beta))**2 - 1 , (1.4 + 1) / 2 * (M**2) * (sin(beta) * sin(theta)) / cos(beta - theta))

sol=nsolve(expr,beta,(0.7))