import numpy as np
import matplotlib.pyplot as plt


r=np.array([1.667,-14.52,56.452])
v=np.linspace(0,10,num=21)

dim_v=v.shape[0]
kl=np.zeros(dim_v)
Dp=np.zeros(dim_v)
for j in range(dim_v):
    for i in range(3): # for i in range (2)
        kl[j] += r[i]*v[j]**(i)
        
    Dp[j]=kl[j]*0.5*1.21*v[j]**2.
    
plt.plot(V,Dp)
plt.show()
    
    
