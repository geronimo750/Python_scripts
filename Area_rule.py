def A_rule (mdot,A,M):
    import numpy as np
    import sympy as sy
    
    gam=1.4
    R=287
    delta=(gam-1)/2.
# mdot=A*(Pt/Tt**0.5)*(gam/R)**0.5*M*(1+delta*M**2)**(-1*(gam+1)/(2*(gam-1))


    if mdot!=0 and M==0 and A!=0:
        Mach = sy.Symbol('Mach', positive=True, real=True)
        eq=mdot-A*sy.sqrt(Pt/Tt)*sy.sqrt(gam/R)*Mach*(1+delta*Mach**2)**(-1*(gam+1)/(2*(gam-1)))
        nsolve(eq,Mach,0.2)
        return Mach
    elif mdot==0 and M!=0 and A!=0:
        mdot-A*sy.sqrt(Pt/Tt)*sy.sqrt(gam/R)*Mach*(1+delta*Mach**2)**(-1*(gam+1)/(2*(gam-1)))
        return mdot
    elif mdot!=0 and M!=0 and A==0:
        Area=sy.Symbol ('Area', positive = True, real = True)
        eq=mdot-Area*sy.sqrt(Pt/Tt)*sy.sqrt(gam/R)*Mach*(1+delta*Mach**2)**(-1*(gam+1)/(2*(gam-1)))
        return Area
    else:
        return print("Wrong Values")
    
        
                                                                                     
                                                                                     