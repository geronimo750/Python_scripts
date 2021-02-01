import numpy as np
import matplotlib.pyplot as plt
import sympy as sy

#import mpmath

Mc_exp=np.array([1.2,1.6,2,3,4,5])
d_exp=np.array([14,28.1,36.5,46.3,50.2,52.0])

d_exp_r=np.deg2rad(d_exp)

Kd_exp=Mc_exp*np.sin(d_exp_r)



#theoretical

gam=1.4
gam2=(gam+1)/2.

Kd=np.linspace(0,6)
Mc=1+gam2*Kd**2*(1+np.log(gam2+1/Kd**2))

plt.plot(Kd,Mc)

plt.plot(Kd_exp,Mc_exp,'*')

plt.show()
