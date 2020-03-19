import numpy as np

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