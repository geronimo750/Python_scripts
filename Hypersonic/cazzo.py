import numpy as np
import matplotlib.pyplot as plt
import sympy as sy
import mpmath

def nu_MP(Mach):
#     v=0
    gam=1.4
    gamr=(gam+1)/(gam-1)
    v=np.sqrt(gamr)*((np.arctan(np.sqrt((1/gamr)*(Mach**2-1)))))-((np.arctan(np.sqrt(Mach**2-1))))
#     print (v)
    return v

sol=nu_MP(10)