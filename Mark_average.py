import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
# from crudef import *
# from Mscalef import *




# filename='Data/MEE3013.csv'
#_________________
# module=pd.read_csv('Data/AER3008.csv')
# des               #average previous years
# ______________MEE2005 _______________
# module=pd.read_csv('Data/MEE2005.csv')
# filename='Data/MEE2005.csv'
# desired=66.93

# ________________MEE2007____________
# module=pd.read_csv('Data/MEE2007.csv')
# filename='Data/MEE2007.csv'
# desired=54.51

#________________MEE3033______________
# module=pd.read_csv('Data/MEE3033.csv')
# filename='Data/MEE3033.csv'
# desired=69.86

#_________________MEE3013___________
filename='Data/MEE3013.csv'
desired=61.63

module=pd.read_csv(filename)


def crudef (raw,des):
    actual=raw.mean()
    new_mark=pd.Series([],dtype='float64')
    fact=des/actual
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
#     maxi=raw.max()
    maxi=120
    actual=raw.mean()
    new_mark=pd.Series([],dtype='float64')
    K=(des-actual)/(actual*abs(actual-maxi))
    for i in range (0, len(raw)):
        if raw[i]<= 40:
            new_mark[i]=raw[i]
        else :
            new_mark[i]=raw[i]+K*raw[i]*(maxi-raw[i])
            if new_mark[i] <= 40:
                new_mark[i]= 40
    return new_mark

def Conscalef(raw,des):
    actual=raw.mean()
    des=des+3
    per=(des-actual)/des
    new_mark=pd.Series([],dtype='float64')
    eps=abs(des-actual)
    while eps > 1:
        for i in range (0, len(raw)):
            if raw[i]<= 40:
                new_mark[i]=raw[i]
            else :
                new_mark[i]=raw[i]+per*raw[i]
                if new_mark[i] <= 40:
                    new_mark[i]= 40
        
        eps=des-new_mark.mean()
        if eps > 1:
            per=per+0.01
        else :
            if eps < -1:
                per = per-0.01
        eps=abs(eps)
        
    return new_mark

def fitting(raw,des):
    actual=raw.mean()
   
#     des=des
    per=(des-actual)/des
    new_mark=pd.Series([],dtype='float64')
    eps=abs(des-actual)
    for i in range (0, len(raw)):
        if raw[i]<= 40:
            new_mark[i]=raw[i]
        else :
            new_mark[i]=0.9*raw[i]-6
            if new_mark[i] <= 40:
                new_mark[i]= 40
    return new_mark
      
        

module["mark"]=module["mark"].sort_values(ignore_index=True)
crude=crudef(module["mark"],desired)
Mscale=Mscalef(module["mark"],desired)
Connor=Conscalef(module["mark"],desired)
Fitting=fitting(module["mark"],desired)


Scaled_module=pd.DataFrame([module["mark"],crude,Mscale,Connor,Fitting],
                           ["Original","crude","Mscale","Connor","Fitting"],dtype='float64')
Scaled_module=Scaled_module.T

# create a DataSet in which each column is a different approach

# ax=plt.figure()
# plt.hist(Scaled_module, edgecolor='black',range=(0,100),bins=int(100/10),alpha=0.5)
# Scaled_module.hist(edgecolor='black',color='green',range=(0,100),bins=int(100/10),alpha=0.5,
#                    sharey=True)
# plt.axex
# plt.hist(new_module, edgecolor='black',range=(0,100),bins=int(100/10))

fig, axs = plt.subplots(2,2,figsize=(14,14),sharey=True,sharex=True)
fig.suptitle(filename +' '+str(desired),fontsize='x-large')
# axs[0].set(xlabel=('marks bin'))

axs[0,0].hist([Scaled_module["Original"],Scaled_module["crude"]],range=(0,100),bins=int(100/10),alpha=0.5)
axs[0,0].text(0.05, 0.9, r'$\mu= ${0:2.2f}'.format(Scaled_module["crude"].mean()) +
            r'$\quad \mu= ${0:2.2f}'.format(Scaled_module["crude"].std()),
              bbox={'facecolor':'orange','alpha':0.5},
            transform=axs[0,0].transAxes)
axs[0,0].text(0.05, 0.8, r'$\mu= ${0:2.2f}'.format(Scaled_module["Original"].mean()) +
            r'$\quad \sigma= ${0:2.2f}'.format(Scaled_module["Original"].std()) ,
              bbox={'facecolor':'lightblue','alpha':0.5},
            transform=axs[0,0].transAxes)
axs[0,0].text(0.05,0.55,r'$Adjusted=Raw*\dfrac{Avg_{des}}{Avg_{raw}}$',
            transform=axs[0,0].transAxes)
# axs[0,0].set(xtick=([10,20,30,40,50,50,70,80,90,100]))

# plt.subplot(222)

axs[0,1].hist([Scaled_module["Original"],Scaled_module["Mscale"]],
                  range=(0,100),bins=int(100/10),alpha=0.5)

axs[0,1].text(0.05, 0.9, r'$\mu= ${0:2.2f}'.format(Scaled_module["Mscale"].mean()) +
            r'$\quad \sigma= ${0:2.2f}'.format(Scaled_module["Mscale"].std()),
              bbox={'facecolor':'orange','alpha':0.5},
            transform=axs[0,1].transAxes)

axs[0,1].text(0.05, 0.8, r'$\mu= ${0:2.2f}'.format(Scaled_module["Original"].mean()) +
            r'$\quad \sigma=$ {0:2.2f}'.format(Scaled_module["Original"].std()) ,
              bbox={'facecolor':'lightblue','alpha':0.5},
            transform=axs[0,1].transAxes)
axs[0,1].text(0.05, 0.5, '$Adjusted=Raw+K*Raw*(Max-Raw)$\n'
            r'$\quad K=\frac{Avg_{des}-Avg_{raw}}{Avg_{des}*(Max-Avg_{raw})}$',
            transform=axs[0,1].transAxes)



axs[1,0].hist([Scaled_module["Original"],Scaled_module["Connor"]],
                  range=(0,100),bins=int(100/10),alpha=0.5)
axs[1,0].text(0.05, 0.9, r'$\mu= ${0:2.2f}'.format(Scaled_module["Connor"].mean()) +
            r'$\quad \sigma= ${0:2.2f}'.format(Scaled_module["Mscale"].std()),
              bbox={'facecolor':'orange','alpha':0.5},
            transform=axs[1,0].transAxes)

axs[1,0].text(0.05, 0.8, r'$\mu= ${0:2.2f}'.format(Scaled_module["Original"].mean()) +
            r'$\quad \sigma= ${0:2.2f}'.format(Scaled_module["Original"].std()) ,
              bbox={'facecolor':'lightblue','alpha':0.5},
            transform=axs[1,0].transAxes)
axs[1,0].text(0.05, 0.5, '$Adjusted=Raw+K*Raw$\n' r'$K=\frac{Avg_{des}-Avg_{raw}}{Avg_{des}} $',
            transform=axs[1,0].transAxes)



axs[1,1].hist([Scaled_module["Original"],Scaled_module["Fitting"]],
                  range=(0,100),bins=int(100/10),alpha=0.5)
axs[1,1].text(0.05, 0.9, r'$\mu= ${0:2.2f}'.format(Scaled_module["Fitting"].mean()) +
            r'$\quad \sigma= ${0:2.2f}'.format(Scaled_module["Mscale"].std()),
              bbox={'facecolor':'orange','alpha':0.5},
            transform=axs[1,1].transAxes)

axs[1,1].text(0.05, 0.8, r'$\mu= ${0:2.2f}'.format(Scaled_module["Original"].mean()) +
            r'$\quad \sigma= ${0:2.2f}'.format(Scaled_module["Original"].std()) ,
              bbox={'facecolor':'lightblue','alpha':0.5},
            transform=axs[1,1].transAxes)
axs[1,1].text(0.05, 0.5, '$Adjusted=K*Raw+q$ \n q and K from fitting',
            transform=axs[1,1].transAxes)

axs[0,0].set(ylabel=('number of students'))
axs[1,0].set(ylabel=('number of students'))
axs[1,1].set(xlabel=('marks bin'))
axs[1,0].set(xlabel=('marks bin'))

plt.xticks((0,10,20,30,40,50,60,70,80,90,100))
plt.tight_layout()
fig.subplots_adjust(top=0.92)
plt.savefig(filename + '.png',format='png')

Scaled_module.plot()
plt.savefig(filename +'dis.png',format='png')
plt.show()



       




# mark average used by Conor --- same % differenze drom the mark