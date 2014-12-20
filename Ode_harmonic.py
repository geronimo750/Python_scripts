import numpy as np
from scipy.integrate import odeint
from matplotlib import pyplot as plt
#import matplotlib.pyplot as plt



tmax=10.
steps=100
tmax/(steps-1)
 
time=np.linspace(0,10,1000)



def derivative (der_vec,t):
    appo=np.zeros(100)
    omega2=64.
    f0=der_vec[0]
    f1=der_vec[1]
    appo[0]=np.array(f1)
    appo[1]=np.array(-omega2*f0)
    return (appo)
    #return (der_vec[1],-omega2*der_vec[0])

yinit=np.array([0.7,0.5])    
    

y=odeint(derivative,yinit,time)

plt.figure()
plt.plot(time,y[:,0])
plt.show()

