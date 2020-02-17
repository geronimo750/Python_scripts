import numpy as np
import matplotlib.pyplot as plt
#from sympy import *
import mpmath

gamma=1.4
Mach=[3,5,10]
delta=(gamma+1)/2
alpha=np.linspace(0.01,10,20)
alphar=alpha*np.pi/180



# Cp for HSDT shock
for M in Mach:
    Ka = M * np.sin(alphar)
    Cps=(np.sin(alphar))**2*(delta + np.sqrt(delta**2 + 4/Ka**2))
    Cpe=(np.sin(alphar))**2*(2/(gamma*Ka**2)*((1-(gamma-1)/2*Ka)**(2*gamma/(gamma-1))-1))
    plt.plot(alpha,Cps-Cpe, color='black')
    plt.plot(alpha,4*alphar/np.sqrt(M**2-1),'--r')


plt.plot(alpha,2*np.pi*alphar)
plt.ylim(0,0.20)
plt.xlabel('AoA in deg')
plt.ylabel ('C_L')
plt.text(6,.18, 'M=3',{'color':'black', 'fontsize':14})
plt.text(8,.14, 'M=5',{'color':'black', 'fontsize':14})
plt.text(8.5,.097, 'M=10',{'color':'black', 'fontsize':14})
plt.legend(('_nolegend_' ,'_nolegend_' ,'_nolegend_' ,'_nolegend_' ,'Hyp. Sim. par.','small perturbation','incompressible'))

plt.show()