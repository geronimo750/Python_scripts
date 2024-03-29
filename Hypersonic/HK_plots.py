# import numpy as np
# import matplotlib.pyplot as plt
from sympy import *
import mpmath

H,K = symbols('H K', positive=True, real=True)

gam=1.4


te=H+K-1
te2=H+K-1.2
te3=H+K-1.47

Phi=sqrt(0.5*1/K)*(2*K+(gam-1)/gam*H)-1.2

p1=plot_implicit(Phi,(K,0,1.2),(H,0,1.4),show=False)

p2=plot_implicit(te,(K,0,1.2),(H,0,1.4),'-.',label='te=1',show=False)

p3=plot_implicit(te2,(K,0,1.2),(H,0,1.4),'--',label='te=1.2',show=False)

p4=plot_implicit(te3,(K,0,1.2),(H,0,1.4),linestyle='-',label='te=1.47',show=False)

p1.extend(p2)

p1.extend(p3)

p1.extend(p4)
# p1.legend()

p1.show()

