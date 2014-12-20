"""
      Program to evaluate heat transfer characteristics parameters
      and correlations
"""

import sys
import numpy as np
from pylab import *
import matplotlib
#functions

# Sutherland law for viscosity
def mus(T): 
    result=0; #in Python functions (objects) do not return values
    mu_ref=1.716e-5;T_ref=273.15;S=110.4;C1=1.458e-6;
    result=C1*T**(3./2.)/(T+S)
    return result

def mus2(T):
    result=0.
    result=-1.71E-11*T**2+5.63E-8*T+3.009E-6
    return result

def cond(T):
    result=0.
    result=-2.817E-8*T**2+9.366E-5*T+0.0007
    return result

def Cp(T):
    result=0.
    result=1.436E-7*T**2+1.332E-5*T+0.9912
    return result

# Gas law
def rho(T):
    result=0
    R=247
    P0=101325.
    result=P0/(R*T)
    return result

# Horizontal Cylinder Correlation
def nuc(RaL,Pra):
    result=(0.6+(0.387*RaL**(1./6.)/(1+(0.559/Pra)**(9./16.))**(8./27.)))**2
    return result

#Enclosure Correlation
def nucav(RaL,Pra,LB,HB):
    result=0.18*(Pra/(0.2+Pra)*RaL)**(0.29)*(LB/HB)**(-0.13)
    return result
# Typical data

g=9.81
T0=0 # assign zero if values given in K
P0=101325
Tc=293.15
Tc=Tc+T0;
Th=333.15
Th=Th+T0
beta=1./Tc
L=0.30      # Characteristic lenght 
H=0.30
Tfilm=(Tc+Th)/2.
mu=mus2(Tfilm)
rhol=rho(Tfilm)

# dimensionaless numbers
Pr=0.71
Gr=(g*(Th-Tc)*beta*L**3.)/(mu/rhol)**2
Ra=Pr*Gr

print >> sys.stdout, "Rayley", "%e" %Ra, "Grashof", "%e" %Gr,"Prandtl", Pr

ANUC=nucav(Ra,Pr,L,H)

#print >> sys.stdout, " Horizontal Cylinder averag Nu", ANUC
print >> sys.stdout, " Squared Cavity averag Nu", ANUC
Raplot=linspace(10E6,2E8,100)
ANUplot=nucav(Raplot,Pr,L,H)
plot(Raplot,ANUplot)
show()
