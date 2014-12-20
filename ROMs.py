import sys
import numpy as np
import scipy as sci
import matplotlib.pylab as plt
from mpl_toolkits.mplot3d import Axes3D
#from pylab import * as plt
from StringIO import StringIO

#import data from file

my_data=np.genfromtxt('/Users/marcogeron/Documents/Python_scripts/R1D0W0.dat',delimiter=" ",names=True,dtype=None)

Xmat=np.reshape(my_data['x'],(65,88,67),order='F')
Ymat=np.reshape(my_data['y'],(65,88,67),order='F')
Zmat=np.reshape(my_data['z'],(65,88,67),order='F')
Pmat=np.reshape(my_data['p'],(65,88,67),order='F')
Umat=np.reshape(my_data['u'],(65,88,67),order='F')
Vmat=np.reshape(my_data['v'],(65,88,67),order='F')
Wmat=np.reshape(my_data['w'],(65,88,67),order='F')
KEmat=np.reshape(my_data['ke'],(65,88,67),order='F')
EPmat=np.reshape(my_data['ep'],(65,88,67),order='F')
PRPSmat=np.reshape(my_data['prps'],(65,88,67),order='F')
Tmat=np.reshape(my_data['T'],(65,88,67),order='F')

#xdraw=Xmat[:,:,25]
#ydraw=Ymat[:,:,25]
#Tdraw=Tmat[:,:,25]

#fig = plt.figure()
##ax = fig.add_subplot(111, projection='3d')
#ax=Axes3D(fig)

#ax.plot_wireframe(xdraw,ydraw,Tdraw, rstride=1, cstride=1)
#plt.show()

#Generate zones

def create_zone(matri): 
   #in Python functions (objects) do not return values
    mini=np.amin(matri)
    mini=18.0 #some cells have zero value needs to be corrected
    maxi=np.amax(matri)
    imax=matri.shape[0]
    jmax=matri.shape[1]
    kmax=matri.shape[2]
    
    ntot=10 #define number of zones
    
    #define zone type
    zonelimit=np.zeros(ntot+1)
    Deltazone=(maxi-mini)/(ntot)
    for i in range (ntot+1):
        zonelimit[i]=18+(i*Deltazone)
        
    zonetype=np.empty_like(matri)
    for i in range (imax):
        for j in range (jmax):
            for k in range (kmax):
                for zone in range (ntot):
                    if matri[i,j,k] >= zonelimit[zone] and matri[i,j,k] < zonelimit[zone+1]:
                        zonetype[i,j,k]=zone
    return zonetype



def plot_slice (xgrid,ygrid,vargrid,zval):
    levels=[0,1,2,3,4,5,6,7,8,9]
    slice_v=zval
    xdraw=xgrid[:,:,slice_v]
    ydraw=ygrid[:,:,slice_v]
    Vdraw=vargrid[:,:,slice_v]
    aa=plt.contourf(xdraw,ydraw,Vdraw,levels,apha=.75,cmap='jet')
    C=plt.contour(xdraw,ydraw,Vdraw, levels, colors='black', linewidth=.5)
    bb=plt.clabel(C, inline=1, fontsize=10)
    plt.colorbar(aa)
    #plt.show()
    return
    
    
    
    

def create_cluster(zonetype):
    C=1 #first cluster type
    imax=zonetype.shape[0]
    jmax=zonetype.shape[1]
    kmax=zonetype.shape[2]
    
    cluster=np.empty_like(zonetype)
    
    
    cluster[0,0,0]=C #inizialization first element
    
    #mirrror on 2D first
    
    D2_zt=zonetype[:,:,25]
    D2_cl=cluster[:,:,25]
    D2_cl[0,0]=C
    for i in range(imax-1):
        for j in range (jmax-1):
            #if not_equal(cluster[i,j],0):
                if D2_zt[i,j] == D2_zt[i+1,j]:
                    D2_cl[i+1,j]=D2_cl[i,j]
                else:
                    D2_cl[i+1,j]=D2_cl[i,j]+1
                if D2_zt[i,j] == D2_zt[i,j+1]:
                    D2_cl[i,j+1]=D2_cl[i,j]
                else:
                    D2_cl[i,j+1]=D2_cl[i,j]+1
                    
    return D2_cl
                    
    
    




    
    
Tzone=create_zone(Tmat)    
cazzo=create_cluster(Tzone)    