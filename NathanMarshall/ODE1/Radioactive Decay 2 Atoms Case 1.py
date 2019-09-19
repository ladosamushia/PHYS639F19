# -*- coding: utf-8 -*-
"""
Created on Tue Sep 17 13:47:48 2019
Nathan Marshall

Solves the differential equations for a radioactive atom A decaying into
a radioactive atom B that decays as well. 
"""
#%%
import matplotlib.pyplot as plt

ka = 0.1 #rate constant for decay of atom A
kb = 0.5 #rate constant for decay of atom B

def dn_adt(na, ka):
    '''Define functional form of radioactivity diff. eq.'''
    return(-na/ka)
    
def dn_bdt(nb, kb, na, ka):
    '''Define functional form of radioactivity diff. eq.'''
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
    na.append(na[-1] + dn_adt(na[-1], ka)*dt) 
    nb.append(nb[-1] + dn_bdt(nb[-1], kb, na[-1], ka)*dt)
    t.append(t[-1] + dt) #add new time value to the list
    
    
plt.plot(t, na, label='Number of Atom A') #plotting results
plt.plot(t, nb, label = 'Number of Atom B')
plt.title('Numerical Solutions to Radioactive Decay Equation')
plt.xlabel('Time (s)')
plt.ylabel('Number of Radioactive Atoms')
plt.grid(True)
plt.legend()
