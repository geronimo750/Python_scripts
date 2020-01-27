from cProfile import label

import numpy as np
import matplotlib.pyplot as plt
from sympy import *
#from sympy.plotting import plot_implicit, Eq

from labellines import labelLine, labelLines



#M=np.linspace [1,10,1]
#theta= np.linspace [0,50,5]
#beta=np.linspace[0,90,5]

theta,beta=symbols('theta beta')
#odo=(sin(beta))**2-1-(sin(beta)-sin(theta))
Mach=[1.2,1.6,2,4,6,10]

#Eq is the equality operator. x equal y ==> Eq (x,y) . the symbol = is the assignment operator.

p=None
for M in Mach :

    print (M)
    expr=Eq((M**2)*(sin(beta*pi/180))**2-1,(1.4+1)/2*(M**2)*(sin(beta*pi/180)*sin(theta*pi/180))/cos(beta*pi/180-theta*pi/180))
    p1=plot_implicit(expr,(beta,0,90),(theta,0,60),show=False,legend=True)

    if p:
        p.extend(p1)
    else:
        p=p1

i=0
for color in ['r', 'b', 'g', 'k', 'm','c']:
   p[i].line_color=color
   i +=1

# i=0
# for M in Mach :
#     p[i].label=str(M)
#     i +=1

#labelLines(plt.gca().get_lines(),align=False,xvals=Mach,color='k')

p.show()


