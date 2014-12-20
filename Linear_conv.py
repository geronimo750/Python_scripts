import sys
import numpy as np
import scipy as sci
import matplotlib
from pylab import *
nx=21;
nt=50;
dt=0.01;
c=1;
dx=2./(nx-1);
u=[]
xval=[]
for i in range(0,nx):
    print >> sys.stdout, i
    x=(0+i*dx)
    xval.append(x)
    print x
    if x <= 1 and x >= 0.5:
        u.append(2);
    else:
        u.append(1);
    
print >> sys.stdout, u
plot(xval,u)
show()