import numpy as np
import matplotlib.pyplot as plt
import sympy as sy
from isentropic_rel import *
from Area_rule import *
from Ideal_gas import *

# This programme will evaluate BC for the specific case of PAW05, however
# it is expected to develop some functions that can be used for supersoni flow
# isentropic relationships as well as shock relationships

gam=1.4
R=287

# environmental conditions
Pa=99e3
Ta=300
rhoa=ideal_gas(Pa,0,Ta)

#Plenum conditions

# outlet conditions
Te=2.7*Ta
Pe=Pa
Ae=(68.07e-3)**2
Me=0.304
rhoe=ideal_gas(Pe,0,Te)
Ue=Me*np.sqrt(gam*R*Te)

print ('Nozzle outlet conditions. Ue=',Ue,'rho_e=',rhoe)

#Nozzle conditions
mdotn=0.34
Ptn=Pa/ise_p(0,Me)
Ttn=Te/ise_T(0,Me)
rhotn=rhoe/ise_rho(0,Me)




# inlet conditions
Ai=np.pi*(152.4e-3)**2
Mi=A_rule(mdotn,Ai,0,Ptn,Ttn)
Pi=Ptn*ise_p(0,Mi)
rhoi=rhotn*ise_rho(0,Mi)
Ti=float(Ttn*ise_T(0,Mi))
Ui=Mi*np.sqrt(gam*R*Ti)

print ('Nozzle inlet conditions. Ui=',Ui,'rho_e=',rhoi)