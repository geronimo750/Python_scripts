import numpy as np
import matplotlib.pyplot as plt
from sympy import *
import mpmath

gam=1.4
delta=(gam-1)/2
gamr=(gam+1)/(gam-1)

mach = symbols('mach', positive=True, real=True)

def nu_MP(Mach):
#     v=0
    gam=1.4
    gamr=(gam+1)/(gam-1)
    v=np.sqrt(gamr)*((np.arctan(np.sqrt((1/gamr)*(Mach**2-1)))))-((np.arctan(np.sqrt(Mach**2-1))))
#     print (v)
    return v

#step one  equivalent wedge

beta=symbols('beta')
theta=np.deg2rad(37)
M=8

# expr=((M**2)*(sin(beta))**2-1-(1.4+1)/2*(M**2)*(sin(beta)*sin(theta))/cos(beta-theta))
expr = Eq((M**2)*(sin(beta))**2 - 1 , (1.4 + 1) / 2 * (M**2) * (sin(beta) * sin(theta)) / cos(beta - theta))

sol=nsolve(expr,beta,(0.7))
# sol=float(sol)
M1n=M*sin(sol)
Mt=M*cos(sol)

M2n=sqrt((1+delta*M1n**2)/(gam*M1n**2-delta))
M2=M2n/sin(sol-theta)
M2=float(M2)
p2p1=1+2*gam/(gam+1)*(M1n**2-1)

cp1=2/(gam*M**2)*(p2p1-1)
print(cp1)
# Expansion 1
m1=M2
solexp=nu_MP(m1)
solexp=float(solexp)
theta=np.deg2rad(12)
nu=solexp+theta
PM_sol=nu-sqrt(gamr)*((atan(sqrt((1/gamr)*(mach**2-1)))))+((atan(sqrt(mach**2-1))))
solution=nsolve (PM_sol, mach,2)
M3=float(solution)
p3p2=((1+delta*M2**2)/(1+delta*M3**2))**(gam/(gam-1))
print(M2,M3)

cp2=2/(gam*M**2)*(p2p1*p3p2-1)
print(cp2)

#Expansion 2
m1=M3
solexp=nu_MP(m1)
solexp=float(solexp)
theta=np.deg2rad(15)
nu=solexp+theta
PM_sol=nu-sqrt(gamr)*((atan(sqrt((1/gamr)*(mach**2-1)))))+((atan(sqrt(mach**2-1))))
solution=nsolve (PM_sol, mach,2)
M4=float(solution)
p4p3=((1+delta*M3**2)/(1+delta*M4**2))**(gam/(gam-1))
print(M3,M4)

cp3=2/(gam*M**2)*(p2p1*p3p2*p4p3-1)

print(cp3)