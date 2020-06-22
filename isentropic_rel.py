def ise_p (p_p0,M):
#    p_p0=(1+delta*Mach**2)**(-gam/(gam-1))
    import numpy as np
    import sympy as sy
    gam=1.4
    delta=(gam-1)/2
    if p_p0 !=0 and M==0:
        Mach = sy.Symbol('Mach', positive=True, real=True)
        eq=p_p0-(1+delta*Mach**2)**(-gam/(gam-1))
        M=sy.nsolve(eq,Mach, 2.5)
        print (M)
        return M
    elif p_p0==0 and M!=0:
        Mach=M
        p_p0=(1+delta*Mach**2)**(-gam/(gam-1))
        return p_p0
    else :
        print ("wrong input")
        return


def ise_rho (rho_rho0,M):
#    rho_rho0=(1+delta*Mach**2)**(-1/(gam-1))
    import numpy as np
    import sympy as sy
    gam=1.4
    delta=(gam-1)/2
    if rho_rho0 !=0 and M==0:
        Mach = sy.Symbol('Mach', positive=True, real=True)
        eq=rho_rho0-(1+delta*Mach**2)**(-1/(gam-1))
        M=sy.nsolve(eq,Mach, 2.5)
        print (M)
        return M
    elif rho_rho0==0 and M!=0:
        Mach=M
        rho_rho0=(1+delta*Mach**2)**(-1/(gam-1))
        return rho_rho0
    else :
        print ("wrong input")
        return


def ise_T (T_T0,M):
#    T_T0=(1+delta*Mach**2)**(-1)
    import numpy as np
    import sympy as sy
    gam=1.4
    delta=(gam-1)/2
    if T_T0 !=0 and M==0:
        Mach = sy.Symbol('Mach', positive=True, real=True)
        eq=T_T0-(1+delta*Mach**2)**(-1)
        M=sy.nsolve(eq,Mach, 2.5)
        print (M)
        return M
    elif T_T0==0 and M!=0:
        Mach=M
        T_T0=(1+delta*Mach**2)**(-1/(gam-1))
        return T_T0
    else :
        print ("wrong input")
        return

