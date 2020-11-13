import matplotlib.pyplot as plt
import pandas as pd
# from crudef import *
# from Mscalef import *
module=pd.read_csv('Data/AER3008.csv')

def crudef (raw,fact):
    new_mark=pd.Series([],dtype='float64')
    for i in range (0, len(raw)):
        if raw[i] <= 40:
            new_mark[i]=raw[i]
        else :
#             new_module[i]=raw+K*raw*(maxi-raw)
            new_mark[i]=raw[i]*fact
            if new_mark[i] <= 40:
                new_mark[i]= 40
                
    return new_mark

def Mscalef (raw,des):
    maxi=raw.max()
    actual=raw.mean()
    new_mark=pd.Series([],dtype='float64')
    for i in range (0, len(raw)):
        if raw[i]<= 40:
            new_mark[i]=raw[i]
        else :
            new_mark[i]=raw[i]+K*raw[i]*(maxi-raw[i])
            if new_mark[i] <= 40:
                new_mark[i]= 40
    return new_mark

def Conscalef(raw,per):
    maxi=raw.max()
#     actual=raw.mean()
    new_mark=pd.Series([],dtype='float64')
    for i in range (0, len(raw)):
        if raw[i]<= 40:
            new_mark[i]=raw[i]
        else :
            new_mark[i]=raw[i]+per*raw[i]
            if new_mark[i] <= 40:
                new_mark[i]= 40
    return new_mark

# marks["mark"].plot()
# n,bins,patches= plt.hist(module["mark"], edgecolor='black',range=(0,100),bins=int(100/10))
# plt.show()

actual=module["mark"].mean()
maxi=module["mark"].max()
des=70
K=(des-actual)/(actual*(maxi-actual))

crude=crudef(module["mark"],1.15)
Mscale=Mscalef(module["mark"],68)
Connor=Conscalef(module["mark"],0.1)
# Mscale=Mscalef
# 
Scaled_module=pd.DataFrame([module["mark"],crude,Mscale,Connor],["Original","crude","Mscale","Connor"],dtype='float64')
Scaled_module=Scaled_module.T
# create a DataSet in which each column is a different approach

# ax=plt.figure()
# plt.hist(Scaled_module, edgecolor='black',range=(0,100),bins=int(100/10),alpha=0.5)
Scaled_module.hist(edgecolor='black',color='green',range=(0,100),bins=int(100/10),alpha=0.5,
                   sharey=True)
# plt.axex
# plt.hist(new_module, edgecolor='black',range=(0,100),bins=int(100/10))

fig, axs = plt.subplots(2,2)
axs[0,0].set(xlabel=('pincopallo'))
# plt.subplot(221)
# plt.subplot(0,0)
axs[0,0].hist([Scaled_module["Original"],Scaled_module["crude"]],range=(0,100),bins=int(100/10),alpha=0.5)

# plt.subplot(222)
plt.hist([Scaled_module["Original"],Scaled_module["Mscale"]],range=(0,100),bins=int(100/10),alpha=0.5)
# plt.title('$Prova M_\infty$')


plt.show()



       




# mark average used by Conor --- same % differenze drom the mark