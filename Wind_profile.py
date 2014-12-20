#Develop of wind profile for Fluent


import sys
import numpy as np
import scipy as sci
import matplotlib.pylab as plt
from mpl_toolkits.mplot3d import Axes3D
#from pylab import * as plt
from StringIO import StringIO

H_stat=10

#Formuala -- V=V_10*(y/H_stat)**0.2

V10=4.3
npoints=5000
y=np.linspace(0,40,npoints)

V=V10*(y/H_stat)**0.2

angle=110
angle=angle*np.pi/180.

Vz=np.cos(angle)*V
Vx=-np.sin(angle)*V
Vy=0.*V

##Coordinate along x and z it does not matter being the profile always the same

#sud profile

xsud=np.linspace(-241,241,npoints)
zsud=np.empty(npoints) 
zsud.fill(367)

#east profile
zeast=np.linspace(-367,367,npoints)
xeast=np.empty(npoints)
xeast.fill(241)

##write in a shape accepted by fluent

f = open('Vel_prof_sud.prof', 'w')
f.write('((velocity-profile-s point 5000)')
npoints
f.write('( x \t')
np.savetxt(f,xsud)
f.write(')')
f.write('( y \t')
np.savetxt(f,y)
f.write(')')
f.write('( z \t')
np.savetxt(f,zsud)
f.write(')')
f.write('( u \t')
np.savetxt(f,Vx)
f.write(')')
f.write('( v \t')
np.savetxt(f,Vy)
f.write(')')
f.write('( w \t')
np.savetxt(f,Vz)
f.write(')')
f.close()


f = open('Vel_prof_east.prof', 'w')
f.write('((velocity-profile-e point 5000)')
f.write('( x \t')
np.savetxt(f,xeast)
f.write(')')
f.write('( y \t')
np.savetxt(f,y)
f.write(')')
f.write('( z \t')
np.savetxt(f,zeast)
f.write(')')
f.write('( u \t')
np.savetxt(f,Vx)
f.write(')')
f.write('( v \t')
np.savetxt(f,Vy)
f.write(')')
f.write('( w \t')
np.savetxt(f,Vz)
f.write(')')
f.close()