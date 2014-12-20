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
sensors_name=list(set(my_data['Node_ID']))


Nsens=len(sensors_name)

 
for sensor in sensors_name:
    in_data_count = 0
    for node in my_data['Node_ID']: 
        if node == sensor: 
            in_data_count += 1
    size=[sensor,in_data_count]


temp=np.zeros((2*in_data_count,Nsens)) #here is the problem in this data set there is one sensor reading double the times

#temp=np.array([])


for i in range(Nsens):
    count=0
    for l in range (T.shape[0]):
        if my_data['Node_ID'][l]==sensors_name[i]:
            temp[count,i]=my_data['Temperature'][l]
            count += 1
        else:
            count=count
            
            
        
