import numpy as np
import matplotlib.pyplot as plt

my_data=np.genfromtxt('history_0.csv',delimiter=',',names=True) 

my_data_n=np.genfromtxt('history.csv',delimiter=',',names=True)


it=np.size(my_data['Inner_Iter'])
my_data_n['Inner_Iter']=my_data_n['Inner_Iter']+it
my_data_f=np.concatenate((my_data['Inner_Iter'],my_data_n['Inner_Iter']),axis=0)
my_data_f=np.concatenate((my_data,my_data_n),axis=0)

np.savetxt('history_01.csv',my_data_f,delimiter=',',header=','.join(my_data_f.dtype.names),comments='')

