import numpy as np
import matplotlib.pyplot as plt
import sympy as sp



def Energy (K,H,te):
    import sympy as sp
    rel=sp.Eq(H+K,te)
    return rel

def Stream (K,H,pi,gam):
    import sympy as sp
    gm=(gam-1)/gam
    rel=sp.Eq(sp.sqrt(0.5*1/K)*(2*K+gm*H),pi)
    return rel

def Mach (K,H,M,gam):
    import sympy as sp
    delta=(gam-1)/2
    Mach=sp.symbols('Mach')
    if M==0:
        rel=sp.Eq(1/delta*K/H,Mach*Mach)
        M=sp.solve(rel,Mach)
        return M
    else :
        rel=sp.Eq(1/delta*K/H,M*M)
        return rel
    

X,Y=sp.symbols('X Y')
eq=Energy(X,Y,1)
eq2=Energy(X,Y,1.4)
eq3=Stream(X,Y,1.2,1.4)
eq4=Mach(X,Y,2.73,1.4)
# sol=sp.linsolve((eq,eq3),X,Y)

#fig, ax = plt.subplots(1)
p1=sp.plot_implicit(eq,(X,0,1.6),(Y,0,1.6),line_color='Red',show=False)
p2=sp.plot_implicit(eq3,(X,0,1.6),(Y,0,1.6),depth=2,show=False)
p3=sp.plot_implicit(eq2,(X,0,1.6),(Y,0,1.6),line_color='Red',linestyle='*',show=False)
p4=sp.plot_implicit(eq4,(X,0,1.6),(Y,0,1.6),line_color='Black',show=False)
p1.append(p2[0])
p1.append(p3[0])
p1.append(p4[0])


p1.show()

