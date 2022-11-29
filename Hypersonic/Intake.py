import numpy as np
import matplotlib.pyplot as plt
from sympy import *


beta=symbols('beta')
theta=np.deg2rad(10)
M=10

# expr=((M**2)*(sin(beta))**2-1-(1.4+1)/2*(M**2)*(sin(beta)*sin(theta))/cos(beta-theta))
expr = Eq((M**2)*(sin(beta))**2 - 1 , (1.4 + 1) / 2 * (M**2) * (sin(beta) * sin(theta)) / cos(beta - theta))

sol=nsolve(expr,beta,(0.7))

Mn=M*sin(sol)

gam=1.4

p2p1=1+2*gam/(gam+1)*(Mn**2-1)

pic=(((gam+1)*Mn**2)/((gam-1)*Mn**2+2))**(gam/(gam-1))*((gam+1)/(2*gam*Mn**2-gam+1))**(1/(gam-1))

psi=(1+2*gam/(gam+1)*(Mn**2-1))*(2+(gam-1)*Mn**2)/((gam+1)*Mn**2)

etac=(psi-(1/pic)**((gam-1)/gam))/(psi-1)

print(etac)


