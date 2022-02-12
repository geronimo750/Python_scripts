import numpy as np
import matplotlib.pyplot as plt
import sympy as sy
import mpmath

#Rayleigh formula

M1=7.5
gam=1.1
gamp1=gam+1
gaml1=gam-1

P02P1=((gamp1**2*M1**2)/(4*gam*M1**2-2*gaml1))**(gam/gaml1)*(1-gam+2*gam*M1**2)/gamp1

cp=2/(gam*M1**2)*(P02P1-1)

print('Cp=',cp)