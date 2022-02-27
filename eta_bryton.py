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
p1=sp.plot(eta1,(PR,1,80),ylabel='Thermal efficiency $\eta_{th}$', show=False, label='$\gamma$=1.67', legend=True)
p2=sp.plot(eta2,(PR,1,80),ylabel='Thermal efficiency $\eta_{th}$', show=False, label='$\gamma$=1.4',legend=True)
p3=sp.plot(eta3,(PR,1,80),ylabel='Thermal efficiency $\eta_{th}$', show=False, label='$\gamma$=1.33',legend=True)

p1.extend(p2)
p1.extend(p3)

p1.show()


