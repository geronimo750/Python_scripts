import numpy as np
import matplotlib.pyplot as plt
from sympy import *


x=np.linspace(0.1,3,20)

y1=np.array(20)
y2=np.array(20)
y1=x**(1/2)
y2=x**(3/4)

plt.plot(x,y1)
plt.plot(x,y2)
