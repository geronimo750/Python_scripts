import sys
import numpy as np
import scipy as sci
import matplotlib
from pylab import *
from StringIO import StringIO

#Generates an array with names of each column ad type auto determined 

my_data=np.genfromtxt('/Users/marcogeron/Documents/Experiment_LG04/R_0_D_1_W_1/20120319/Data.csv',delimiter=",",names=True,dtype=None)

T=my_data['Temperature'] #Shows that column! Remeber it is just a regitry association. If T is modified then my_data is modified


#my_data=np.genfromtxt('Prova.csv',delimiter=",")
#my_data=np.genfromtxt(StringIO('Prova.csv'),delimiter=",")
#my_data=np.genfromtxt('/Users/marcogeron/Documents/Python_scripts/Prova.csv', names=True,delimiter=",")
sensors_name=array([['2001:770:19e:4:0:0:0:b0b'],
              ['2001:770:19e:4:0:0:0:b0c'],
              ['2001:770:19e:4:0:0:0:b0c']]) 

Nsens=sensors_name.shape[0]

temp=np.zeros((my_data.shape[0],Nsens))
#temp=np.array([])

for i in range(0,Nsens):
    count=0
    for l in range (0,my_data.shape[0]):
        if my_data['Node_ID'][l]==sensors_name[i]:
            temp[count,i]=my_data['Temperature'][l]
            count=count+1
        else:
            count=count


dove andiamo?
chi lo sa?

Chi ha mangiato la marmellata?

            
            
        
