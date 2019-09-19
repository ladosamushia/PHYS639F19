# -*- coding: utf-8 -*-
"""
Created on Tue Sep 17 13:57:03 2019

Solves the differential equations for a radioactive atom A decaying into
a radioactive atom B that decays into atom A. 
"""
#%%
import matplotlib.pyplot as plt

ka = 0.5 #rate constant for decay of atom A 
kb = 0.5 #rate constant for decay of atom B

def dn_adt(na, nb):
    '''Differential equation for the number of atom A.'''
    return(-na/ka + nb/kb)
    
def dn_bdt(na, nb):
    '''Differential equation for the number of atom B.'''
    return(-nb/kb + na/ka)

dt = 0.0001 #step size
t0 = 0 #initial condition for time
na0 = 100000 #initial number of atom A
nb0 = 10000 # initial number of atom B
tmax = 5 #max value of time
t = [t0] #list to contain t values
na = [na0] #list to contain number of A values
nb = [nb0] #list to contain number of B values


while t[-1] < tmax: #loop until tmax is reached
    #add dN/dt * dt to previous N values for atoms A and B
    na.append(na[-1] + dn_adt(na[-1], nb[-1])*dt) 
    nb.append(nb[-1] + dn_bdt(na[-1], nb[-1])*dt)
    t.append(t[-1] + dt) #add new x value to the list
    
    
plt.plot(t, na, label='Number of Atom A') #plotting numerical results
plt.plot(t, nb, label = 'Number of Atom B')
plt.title('Numerical Solutions to Radioactive Decay Equation')
plt.xlabel('Time (s)')
plt.ylabel('Number of Radioactive Atoms')
plt.grid(True)
plt.legend()

