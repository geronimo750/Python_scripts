def A_rule (mdot,A,M,Pt,Tt):
    import numpy as np
    import sympy as sy
    
    gam=1.4
    R=287
    delta=(gam-1)/2.
# mdot=A*(Pt/Tt**0.5)*(gam/R)**0.5*M*(1+delta*M**2)**(-1*(gam+1)/(2*(gam-1))


    if mdot!=0 and M==0 and A!=0:
        Mach = sy.Symbol('Mach', positive=True, real=True)
        eq=mdot-A*Mach*Pt*sy.sqrt(gam/R*Tt)*(1+delta*Mach**2)**((gam+1)/(-2*(gam-1)))
        M=sy.nsolve(eq,Mach,0.2)
        return M
    elif mdot==0 and M!=0 and A!=0:
        mdot=A*Pt*M*sy.sqrt(gam/R*Tt)*(1+delta*M**2)**((gam+1)/(-2*(gam-1)))
        return mdot
    elif mdot!=0 and M!=0 and A==0:
        Area=sy.Symbol ('Area', positive = True, real = True)
        eq=mdot-Area*M*Pt*sy.sqrt(gam/R*Tt)*(1+delta*M**2)**((gam+1)/(-2*(gam-1)))
        A=sy.nsolve (eq,Area,1)
        return A
    else:
        return print("Wrong Values")
    
        
                                                                                     
                                                                                     