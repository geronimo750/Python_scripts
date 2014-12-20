import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt
import warnings

eta=np.linspace(0,10,100)


def Blasiusfunc (der_vec,t):
    deri=np.zeros(eta)
    f0=der_vec[0]
    f1=der_vec[1]
    f2=der_vec[2]
    deri[0]=np.array(f1)
    deri[1]=np.array(f2)
    deri[2]=np.array(-0.5*f0*f2)
    
    return(deri)
    
Binit=np.array([0.,0.,0.3318])

Bsol=odeint(Blasiusfunc,Binit,eta)