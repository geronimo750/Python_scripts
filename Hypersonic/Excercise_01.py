import numpy as np
import matplotlib.pyplot as plt
from sympy import *
import mpmath

beta = symbols('beta', positive=True, real=True)

Mach = np.array( [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20])

k=np.size(Mach)
theta=10*pi/180

p=np.zeros(k)
i=0
for M in Mach:
#M=2
    print(M)
    expr = Eq((M**2)*(sin(beta))**2 - 1 , (1.4 + 1) / 2 * (M**2) * (sin(beta) * sin(theta)) / cos(beta - theta))
#expr = Eq((M**2)*(sin(beta*pi/180))**2 - 1, (1.4 + 1) / 2 * (M**2)*(sin(beta*pi/180) * sin(theta)/cos(beta*pi/180 - theta)))
#    expr.evalf()
#sol=solveset(expr,beta)
    sol=nsolve(expr,beta,(1.1))
    diff=float(sol*180/pi-theta*180/pi)
    p[i]=diff
    i+=1

    # if p:
    #     p.append(diff)
    # else:
    #     p=diff

#plot(p,Mach)
