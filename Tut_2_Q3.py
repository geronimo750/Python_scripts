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

Kd=np.linspace(0.1,4)
Mc=1+gam2*Kd**2*(1+np.log(gam2+1/Kd**2))

fig, ax=plt.subplots(figsize=(6,6))

ax.set_xlabel('$K_{\delta}$')
ax.set_ylabel('$M_c$')
ax.plot(Kd,Mc, label='HSDT')
ax.plot(Kd_exp,Mc_exp,'*',label='Exact Theory')
ax.legend()
plt.show()
