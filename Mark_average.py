import matplotlib.pyplot as plt
import pandas as pd

marks=pd.read_csv('Data/AER3008.csv')

# marks["mark"].plot()
n,bins,patches= plt.hist(marks["mark"], edgecolor='black',range=(0,100),bins=int(100/10))
plt.show()
marks["mark"].mean()