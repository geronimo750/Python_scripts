import numpy as np
import matplotlib.pyplot as plt
import sympy as sy
from isentropic_rel import *
from Area_rule import *

# This programme will evaluate BC for the specific case of PAW05, however
# it is expected to develop some functions that can be used for supersoni flow
# isentropic relationships as well as shock relationships

    

# environmental conditions
pa=99e3
Ta=300

#Plenum conditions

#Nozzle conditions
Te=2.7*Ta
Ai=np.pi*(152.4e-3)**2
Ae=68.07**2
Me=0.304
mdotn=0.34
Ptn=pa/ise_p(0,Me)
Ttn=Ta/ise_T(0,Me)
Rhon=
p0=p/ise_p(0,2)
Min=A_rule(mdotn,Ai,0)



    