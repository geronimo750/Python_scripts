import sympy as sp
import matplotlib.pyplot as plt


x = sp.symbols('x', positive=True, real=True)

eq=3.66e-3*sp.exp(2.14e-3*x)

# sp.plot(eq,(x,1,300))

point=sp.nsolve((6.2e-3-eq),(x),(100,300))

