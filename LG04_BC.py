import numpy as np
from matplotlib import pyplot as plt
from Heatransfer import rho as rho
# Gas law
def rho(T):
    result=0
    R=287
    P0=101325.
    result=P0/(R*T)
    return result
    
    
#reference values    
l=0.8;d=0.12
V=0.45
Tout=273.15+45.0

mass1=rho(Tout)*(l*d)*V

Vz=V*np.cos(20./180.*np.pi)
Vx=V*np.sin(20./180.*np.pi)


