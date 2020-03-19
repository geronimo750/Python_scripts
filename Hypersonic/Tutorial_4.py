import numpy as np
import matplotlib.pyplot as plt
import sympy as sp

from Thermo import mus

R=287

# Free stream conditions
Tw=1200 # [K]
Minf=25
Pinf=0.53 #[Pa]
rhoinf=9.6e-6 #[Kg/m3]
ainf=276.9 #[m/s]
muinf=12.53e-6 #[kg/ms]

rhow=Pinf/(R*Tw)

muw=mus(Tw)

Croot=sp.sqrt(rhow*muw/(rhoinf*muinf))

x=sp.symbols('x')

xi=Minf**3*Croot/sp.sqrt(rhoinf*(Minf*ainf)*x/muinf)

sol=sp.solve(xi-3)
print(sol)
ps=1+0.15*xi
pd=1+0.078*xi
sp.plot(xi,(x,0.5,5))
sp.plot(pd,(x,0.5,5))


