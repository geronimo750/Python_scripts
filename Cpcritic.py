import numpy as np
import matplotlib.pyplot as plt
import sympy as sy

Mach = sy.symbols('Mach', positive=True, real=True)

Cpi=-0.35
gam=1.4
a1=(gam-1)/(gam+1)
a2=2/(gam+1)
ex=gam/(gam-1)

Cpc=Cpi/sy.sqrt(1-Mach**2)

Cpcr=((a1*Mach**2+a2)**(ex)-1)*2/(gam*Mach**2)

# sol=sy.solveset(sy.Eq(Cpc,Cpcr),Mach)
sol=sy.nsolve(sy.Eq(Cpc,Cpcr),Mach,(0.7))

print(sol)

#plotting using sympy directly

plot1=sy.plot(-Cpc, (Mach,0.3,0.9), axis_center=(0.3,0), ylabel='Cp', legend=True, show=False) #, label='Cp_c', line_color='red',,
              #ylabel='Cp', show=False, legend=True)
plot2=sy.plot(-Cpcr,(Mach,0.3,0.9), show=False)#, label='Cp_cr', show=False, legend=True)



plot1.append(plot2[0])

p=plot1
p[0].line_color='blue'
p[0].label ='$C_{p_{comp}}$'
p[1].line_color='red'
p[1].label='$C_{p_{crit}}$'




p.show()
# plot1.show()

# problem with legend (not showing label legend)
# use matplot lib
