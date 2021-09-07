import numpy as np
import matplotlib
matplotlib.rcParams['text.usetex'] = True
import matplotlib.pyplot as plt
#from sympy import *
# import mpmath

T3T0=np.linspace(1.4,8,8)
mach=np.linspace(0,25,101)
gam=1.4
delta=(1.4-1)/2
T=8
i=0

k=np.size(mach)

for T in T3T0:
    M3=np.zeros(k)
    i=0
    for M0 in mach:
        a=(1/T*(1+delta*M0**2))
        if a < 1:
            a=1
    
        M3[i]=np.sqrt(1/delta*(a-1))
        i+=1
    
    plt.plot(mach, M3 )
   
   
plt.xlabel(r'$$M_0$$')
plt.ylabel (r'$$M_3$$')
plt.show()