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
yapp=np.linspace(0,40,41)

V=V10*(yapp/H_stat)**0.2


angle=110
angle=angle*np.pi/180.



Vzapp=np.cos(angle)*V
Vxapp=-np.sin(angle)*V
Vyapp=0.*V

zapp=np.linspace(-360,360,100)
X=np.empty([99,40])
Y=np.empty([99,40])
Z=np.empty([99,40])
Vx=np.empty([99,40])
Vy=np.empty([99,40])
Vz=np.empty([99,40])


for j in range (0,40):
    for i in range (0,99):
        X[i,j]=240.
        Y[i,j]=yapp[j]
        Z[i,j]=zapp[i]
        Vx[i,j]=Vxapp[j]
        Vy[i,j]=0.
        Vz[i,j]=Vzapp[j]
    
    
    

#write for TECPLOT

f = open('Vel_prof.dat', 'w')
f.write('TITLE= \"pincopallo\" \n')
f.write('VARIABLES= \"X\",\"Y\",\"Z\",\"U\",\"V\",\"W\" \n')
f.write('ZONE T = \"cacio\" \n')
f.write('I = 1,J=41,K=100 \n')
f.write('ZONETYPE = ORDERED, DATAPACKING = BLOCK \n')

np.savetxt(f,X)

np.savetxt(f,Y)

np.savetxt(f,Z)

np.savetxt(f,Vx)

np.savetxt(f,Vy)

np.savetxt(f,Vz)

f.close()


##write in a shape accepted by fluent

f = open('Vel_prof_east.prof', 'w')
f.write('((velocity-profile-e point 3960)')
npoints
f.write('( x \r')
np.savetxt(f,X, delimiter='\n')
f.write(')')
f.write('( y \r')
np.savetxt(f,Y, delimiter='\n')
f.write(')')
f.write('( z \r')
np.savetxt(f,Z, delimiter='\n')
f.write(')')
f.write('( u \r')
np.savetxt(f,Vx, delimiter='\n')
f.write(')')
f.write('( v \r')
np.savetxt(f,Vy, delimiter='\n')
f.write(')')
f.write('( w \r')
np.savetxt(f,Vz, delimiter='\n')
f.write(')')
f.close()

f = open('Vel_prof_east_mesh.prof', 'w')
f.write('((velocity-profile-e mesh 40 99)')
npoints
f.write('( x \r')
np.savetxt(f,X)
f.write(')')
f.write('( y \r')
np.savetxt(f,Y)
f.write(')')
f.write('( z \r')
np.savetxt(f,Z)
f.write(')')
f.write('( u \r')
np.savetxt(f,Vx)
f.write(')')
f.write('( v \r')
np.savetxt(f,Vy)
f.write(')')
f.write('( w \r')
np.savetxt(f,Vz)
f.write(')')
f.close()
#
#
#f = open('Vel_prof_east.txt', 'w')
##f.write('((velocity-profile-e point 5000)')
##f.write('( x \t')
##np.savetxt(f,xeast)
##f.write(')')
#f.write('( y \t')
#np.savetxt(f,y)
#f.write(')')
#f.write('( z \t')
#np.savetxt(f,zeast)
#f.write(')')
#f.write('( u \t')
#np.savetxt(f,Vx)
#f.write(')')
##f.write('( v \t')
##np.savetxt(f,Vy)
##f.write(')')
##f.write('( w \t')
##np.savetxt(f,Vz)
##f.write(')')
#f.close()