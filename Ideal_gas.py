def ideal_gas (p,rho,T):
    import numpy as np
    import sympy as sy
    
    
    R=287
    if p==0 and rho!=0 and T!=0:
        p=rho*R*T
        return p
    elif p!=0 and rho==0 and T!=0:
        rho=p/(R*T)
        return rho
    elif p!=0 and rho!=0 and T==0:
        T=p/(rho*R)
        return T
    else:
        print ('wrong combination of input values')
        return
    