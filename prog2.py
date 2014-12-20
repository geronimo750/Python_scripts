"""
	Program 2: Using NUMPY
"""
import sys
import numpy as np
from pylab import *

nx = 210
nt = 2000
dt = 0.0005
c = 1
dx = 2.0/(nx-1)


u = np.zeros(nx)
x = np.zeros(nx)
un= np.zeros(nx)
for i in range(0,nx):
	#print >> sys.stdout, i

	x[i]= 0 + (i) * dx
	#print >> sys.stdout, x
	if x[i] <= 1 and x[i] >= 0.5:
		u[i] = 2
	else:
		u[i] = 1

#print >> sys.stdout, u
#plot(x,u)
#show()
for it in range (0,nt):
	un = u.copy()
	if un.all()*dt/dx >=1: 
		sys.exit( "CFL>1");	
	for i in range (1,nx-1):
		u[i]=un[i]-un[i]*dt/dx*(un[i]-un[i-1])
		
	if it % 200 == 0:
		plot(x,u)

	#print >> sys.stdout, u,un
show()