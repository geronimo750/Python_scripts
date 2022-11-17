import numpy as np
import matplotlib.pyplot as plt
import sympy as sp
from Thermo import *

# free stream conditions

Tinf= 198.6386
muinf=0.000013208
ainf=282.5379
pinf=1.0525
rhoinf=0.000018458
Minf=25


# Tinf= 224.5272
# muinf=1.27e-5
# ainf=300.38
# pinf=1616.2
# rhoinf=0.025076
# Minf=14

# Tinf= 220.55
# muinf=1.44e-5
# ainf=297.72
# pinf=2971.7
# rhoinf=0.047
# Minf=12

# wall conditions
Taw=0.88*Tinf*(1+0.2*Minf**2)

Twall=1200
#Twall=Taw

muwall=mus(Twall)
print("Mu wall=",muwall)

C=Twall*muinf/(Tinf*muwall)
print("C=",C)

X=sp.symbols('X')

Rex=rhoinf*Minf*ainf*X/muinf

print ("Rex1=", rhoinf*Minf*ainf/muinf)
Cibar=Minf**3*sp.sqrt(C)/sp.sqrt(Rex)


xmin=(sp.solve(Cibar-7,X))
xmed=(sp.solve(Cibar-3,X))
xmax=5
xm=float(xmin[0])
xe=float(xmed[0])
print("xmin=",xm)
print("xmed=",xe)


# Cold
ps=1+0.15*Cibar
pw=1+0.078*Cibar

# adiabatic
#ps=0.514*Cibar+0.759
#pw=1+0.31*Cibar+0.05*Cibar**2

f=sp.Piecewise((ps, X>xe),(ps,X>xm))
sp.plot(ps,(X,0.1,xmax))
#

