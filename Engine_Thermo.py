import numpy as np
import matplotlib.pyplot as plt
import sympy as sp

#simulations variable
#cold section
gmc=1.4
Cpc=1005
deltac=(gmc-1)/2
isexpc=(gmc-1)/gmc
invisc=1/isexpc
#hot section
gmh=1.33
Cph=1110
deltah=(gmh-1)/2
isexph=(gmh-1)/gmh
invish=1/isexph
#engine parameters
pic=20
Tt4=1500

#efficiency parameters
etad=1
etac=1
etab=1
deltpb=0
etat=1
etan=1

