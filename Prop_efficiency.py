import sympy as sp
import matplotlib.pyplot as plt
# plt.rcParams.update({
#     "font.family": "serif",
#     # Use LaTeX default serif font.
#     "font.serif": [],
#     # Use specific cursive fonts.
#     "font.cursive": ["Comic Neue", "Comic Sans MS"],
# })

plt.rc('font', size=20)
X=sp.symbols('X')

Peff=(2/(1+X))*100

Peff2=(2/(1+1/X))*100

Peffx=(2*X/(1+X**2))*100

# p1=sp.plot(Peff,(X,1,4),line_color='Black',ylabel='Propulsion efficiency $\eta_p$ (%)'
#            ,xlabel='$U_e/U_0$',xlim=(1,4),ylim=(30,100),axis_center=(1,30))

p1=sp.plot(Peffx,(X,0,4),line_color='Black',ylabel='Propulsion efficiency $\eta_p$ (%)'
           ,xlabel='$U_0/U_e$',label='Rocket',xlim=(0,2.2),ylim=(0,110),axis_center=(0,0),legend=True,show=False)


p2=sp.plot(Peff2,(X,0,1),line_color='Red',label='Turbojet',legend=True,show=False)
p1.extend(p2)

p1.show()