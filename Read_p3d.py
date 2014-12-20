import sys
import numpy as np
import scipy as sci
import matplotlib
from pylab import *
from StringIO import StringIO

#ntot=np.fromfile('/Users/marcogeron/Copy/Base_Flow_Project/Test/cazzo.dat',dtype=np.int,count=1) 
# this format is not usable because is valid only for binary file.
f=open('/Users/marcogeron/Copy/Base_Flow_Project/Test/Nozzle_Medium.p3d')
ntot = []
line=f.readline()

#while line:
line = line.strip("\n")
line = line.split()
#ntot.append([])
for item in line:
        ntot.append(int(item))
    #line = f.readline()
    #index += 1

#list or np.array can be used, considering that there will not be a huge manipulation of the data in this case

#for the list it could be possible to use ntot=np.array([line[0],line[1]) 
ntota=np.asarray(ntot) #convert list in array

#ntot=np.genfromtxt('/Users/marcogeron/Copy/Base_Flow_Project/Test/Nozzle_Medium.p3d',dtype=np.int)
my_data=np.genfromtxt('/Users/marcogeron/Copy/Base_Flow_Project/Test/Nozzle_Medium.p3d',skip_header=1,dtype=np.float)
f.close()



totE=ntota[0]*ntota[1]
xvec=np.zeros(totE)
yvec=np.zeros(totE)
zvec=np.zeros(totE)
my_data=np.reshape(my_data, (2*totE,-1))


for i in xrange (totE-1):
    xvec[i]=my_data[i,0]
    yvec[i]=my_data[totE+i,0]
    zvec[i]=0
    
np.savetxt('cazzone',line,fmt='%s %s',delimiter=' ') 




    
    
    