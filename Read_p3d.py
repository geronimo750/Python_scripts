import sys
import numpy as np
import scipy as sci
import matplotlib
from pylab import *
from StringIO import StringIO

#ntot=np.fromfile('/Users/marcogeron/Copy/Base_Flow_Project/Test/cazzo.dat',dtype=np.int,count=1) 
# this format is not usable because is valid only for binary file.
f=open('/Users/marcogeron/Copy/Base_Flow_Project/Test/Nozzle_Medium.p3d')

#read blocs
line=f.readline()
line = line.strip("\n")
bloc=int(line)


#read number of lements for each bloc
ntot = np.zeros([bloc,3])
for b in bloc

line=f.readline()

#while line:
line = line.strip("\n")
line = line.split()
#ntot.append([])

for dim in range 1:
        ntot[b,dim]=line[dim]
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
my_data=np.reshape(my_data, (2*totE,-1)) #this needs to be adapted to the number of the blocks


for i in xrange (totE-1):
    xvec[i]=my_data[i,0]
    yvec[i]=my_data[totE+i,0]
    zvec[i]=0
    
    
f.open('some_name.p3d','w')    

#f.write('6 \n') ... scrivi il numero deu blocchi
f.write(ntota[0],ntota[1],ntota[2]) #ntota[2] needs to be defined
np.savetxt(f,xvec)
f.write('\n')
np.savetxtx(f,yvec)
f.write('\n')
np.savetxtx(f,zvec)
    
np.savetxt('cazzone',line,fmt='%s %s',delimiter=' ') 




    
    
    