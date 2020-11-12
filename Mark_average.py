import matplotlib.pyplot as plt
import pandas as pd

module=pd.read_csv('Data/AER3008.csv')

# marks["mark"].plot()
# n,bins,patches= plt.hist(module["mark"], edgecolor='black',range=(0,100),bins=int(100/10))
# plt.show()

actual=module["mark"].mean()
maxi=module["mark"].max()
des=70
K=(des-actual)/(actual*(maxi-actual))

new_module=pd.Series([],dtype='float64')

# create a DataSet in which each column is a different approach

for i in range (0, len(module)):
    raw=module["mark"][i]
    if raw <= 40:
        new_module[i]=raw
    else :
        new_module[i]=raw+K*raw*(maxi-raw)
        if new_module[i] <= 40:
            new_module[i]= 40

plt.hist([module["mark"],new_module], edgecolor='black',range=(0,100),bins=int(100/10))
# plt.hist(new_module, edgecolor='black',range=(0,100),bins=int(100/10))
plt.show()

#