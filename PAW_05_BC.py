import numpy as np
import matplotlib.pyplot as plt
import sympy as sy
from isentropic_rel import *
from Area_rule import *
from Ideal_gas import *

# This programme will evaluate BC for the specific case of PAW05, however
# it is expected to develop some functions that can be used for supersonic flow
# isentropic relationships as well as shock relationships

gam=1.4
R=287

# environmental conditions
Pa=99e3
Ta=300
rhoa=ideal_gas(Pa,0,Ta)

# Nozzle
#set point 23
# TR=1.765   #input data
# NPR=1.103
# Me=0.376
# BR
    #BR=0.5 
mdotp=0.0062 #input
Pp=105.1e3   #input
Tp=Ta+14     #input

#set point 42
# TR=2.7 
# NPR=1.066
# Me=0.304
# BR




# outlet conditions

Te=TR*Ta
Pe=Pa
Ae=(68.07e-3)**2
rhoe=ideal_gas(Pe,0,Te)
Ue=Me*np.sqrt(gam*R*Te)

print ('Nozzle outlet conditions. Ue=',Ue,'rho_e=',rhoe)

#Nozzle conditions

Ptn=Pa/ise_p(0,Me)
Ttn=Te/ise_T(0,Me)
rhotn=rhoe/ise_rho(0,Me)

print ('Nozzle total conditions: Ttn=',Ttn,'Ptn=',Ptn)

# inlet conditions
Ai=np.pi*(152.4e-3)**2
Mi=A_rule(mdotn,Ai,0,Ptn,Ttn)
Pi=Ptn*ise_p(0,Mi)
rhoi=rhotn*ise_rho(0,Mi)
Ti=float(Ttn*ise_T(0,Mi))
Ui=Mi*np.sqrt(gam*R*Ti)

print ('Nozzle inlet conditions. Ui=',Ui,'rho_i=',rhoi)

#Plenum
Ap=0.0125

rhop=ideal_gas(Pp,0,Tp)
Up=mdotp/rhop/Ap

print ('Plenum inlet conditions. Up=',Up,'rho_p=',rhop)

Mp=Up/np.sqrt(gam*R*Tp)
Ptp=Pp/ise_p(0,Mp)
Ttp=Tp/ise_T(0,Mp)

print ('Plenum Total Conditions : Ttp=',Ttp,'Ptp=',Ptp)

#mdotp=0.0162   #BP2
