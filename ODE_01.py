import numpy as np
from scipy.integrate import odeint
from matplotlib import pyplot as plt
#import matplotlib.pyplot as plt
import warnings
#from colorline import colorline

a=2
def f(y,t):
    return a*y
    
y0=1.0
t_output = np.arange(0, 6, 0.1)
y_result = odeint(f, y0, t_output)
y_result = y_result[:, 0]


#plt.plot(t_output, y_result)
plt.figure()
plt.plot(t_output, y_result)
plt.plot(t_output, y0 * np.exp(a * t_output))
plt.show()
