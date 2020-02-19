import numpy as np
import matplotlib.pyplot as plt
import sympy as sy
import mpmath



mach = sy.symbols('mach', positive=True, real=True)





# v=sy.sqrt(gamr)*1/(sy.tan(1/gamr*(Mach**2-1)))-1/(sy.tan(sy.sqrt(Mach**2-1)))
def nu_MP(Mach):
#     v=0
    gam=1.4
    gamr=(gam+1)/(gam-1)
    v=np.sqrt(gamr)*((np.arctan(np.sqrt((1/gamr)*(Mach**2-1)))))-((np.arctan(np.sqrt(Mach**2-1))))
#     print (v)
    return v

def mus(T): 
    result=0; #in Python functions (objects) do not return values
    mu_ref=1.716e-5;T_ref=273.15;S=110.4;C1=1.458e-6;
    result=C1*T**(3./2.)/(T+S)
    return result



gam=1.4
gamr=(gam+1)/(gam-1)

m1=10
sol=nu_MP(m1)
theta=np.deg2rad(10)
nu=sol+theta
PM_sol=nu-sy.sqrt(gamr)*((sy.atan(sy.sqrt((1/gamr)*(mach**2-1)))))+((sy.atan(sy.sqrt(mach**2-1))))
solution=sy.nsolve (PM_sol, mach,2)
print(solution)

# eqHy=np.deg2rad(10)-2/(gam-1)*(1/m1-1/mach)
# solHy=sy.solveset(eqHy,mach)
# print(solHy)
# err=(solution-solHy)/solution