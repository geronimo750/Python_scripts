import numpy as np
import matplotlib.pyplot as plt
#from sympy import *
import mpmath

gamma=1.4
Mach=[3,5,10]
delta=(gamma+1)/2
alpha=np.linspace(0.1,10,20)
alphar=alpha*np.pi/180



# Cp for HSDT shock
for M in Mach:
    Ka = M * np.sin(alphar)
    Cps=(np.sin(alphar))**2*(delta + np.sqrt(delta**2 + 4/Ka**2))
    Cpe=(np.sin(alphar))**2*(2/(gamma*Ka**2)*((1-(gamma-1)/2*Ka)**(2*gamma/(gamma-1))-1))
    plt.plot(alpha,Cps-Cpe, label= 'M= %.2f'%M, color='black')
    # plt.plot(alpha,(gamma+1)*alphar**2)
    plt.plot(alpha,4*alphar/np.sqrt(M**2-1),'--r')

plt.plot(alpha,2*np.pi*alphar)    