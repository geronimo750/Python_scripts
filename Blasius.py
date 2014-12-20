import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt


etamax=10.
steps=10000
fppwall=0.3318
#fppwall=0.23318
#def blasius (etamax,steps,fppwall):
deta =etamax/(steps-1)
eta = np.zeros(steps)
f=np.zeros(steps)
fp=np.zeros(steps)
fpp=np.zeros(steps)
fppp=np.zeros(steps)

fbar=np.zeros(steps)
fpbar=np.zeros(steps)
fppbar=np.zeros(steps)
fpppbar=np.zeros(steps)    
fpp[0]=fppwall
 
for count in range (0,1)  :     
    #predictor
    for i in range(0,steps-1):
        eta[i+1]=eta[i]+deta
   
        #predictor
        fbar=f[i]+deta*fp[i]
        fpbar=fp[i]+deta*fpp[i]
        fppbar=fpp[i]+deta*fppp[i]
        fpppbar=-fbar*fppbar/2.
        
        
        #corrector
        
        f[i+1]=f[i]+deta*(fp[i]+fpbar)/2.
        fp[i+1]=fp[i]+deta*(fpp[i]+fppbar)/2.
        fpp[i+1]=fpp[i]+deta*(fppp[i]+fpppbar)/2.
        fppp[i+1]=-f[i+1]*fpp[i+1]/2.
       
    #return [eta, f, fp, fpp, fppp]
    

    
    