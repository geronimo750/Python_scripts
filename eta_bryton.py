import numpy as np
import matplotlib.pyplot as plt
import sympy as sp
import mpmath


PR = sp.symbols('PR', positive=True, real=True)

spec=[1.67,1.4,1.3]


eta=[3]
i=0

# %for gam in spec:
#     
# %    eta[i]=1-(1/PR)**((gam-1)/gam)
# %    i+=1

gam=1.67
eta1=1-(1/PR)**((gam-1)/gam)

gam=1.4
eta2=1-(1/PR)**((gam-1)/gam)

gam=1.3
eta3=1-(1/PR)**((gam-1)/gam)

plt.rc('font', size=20)
p1=sp.plot(eta1,(PR,1,80),ylabel='Thermal efficiency $\eta_{th}$', show=False )
p2=sp.plot(eta2,(PR,1,80),ylabel='Thermal efficiency $\eta_{th}$', show=False )
p3=sp.plot(eta3,(PR,1,80),ylabel='Thermal efficiency $\eta_{th}$', show=False )

x1, y1 =p1[0].get_points()
x2, y2 =p2[0].get_points()
x3, y3 =p3[0].get_points()


fig, ax = plt.subplots()

plt.plot(x1,y1,label='$\gamma$=1.67' )
plt.plot(x2,y2,label='$\gamma$=1.4')
plt.plot(x3,y3,label='$\gamma$=1.33')

ax.set_xlabel('$r_p$')
ax.set_ylabel('Thermal efficiency $\eta_{th}$')

plt.legend()

plt.show()


