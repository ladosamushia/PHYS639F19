# -*- coding: utf-8 -*-
"""
Created on Tue Sep 17 13:31:05 2019
Nathan Marshall

Numerically solving differential equation for radioactive decay for a range of
proportionality constants.
"""
#%%
import numpy as np
import matplotlib.pyplot as plt

k = np.linspace(0.1, .8, 10) #range of decay rate constants

def dndt(n, k):
        '''Define functional form of radioactivity diff. eq.'''
        return(-n/k)

for ki in k:    
    dt = 0.0001 #step size
    t0 = 0 #initial condition for time
    n0 = 100000 #initial condition for number of atoms
    tmax = 5 #max value of time
    t = [t0] #list to contain t values
    n = [n0] #list to contain number of atom values
    
    
    while t[-1] < tmax: #loop until time is greater than tmax
        n.append(n[-1] + dndt(n[-1], ki)*dt) #add dn/dt * dt to previous N
        t.append(t[-1] + dt) #add new t value to the list

    plt.plot(t, n) #plotting numerical result
    
plt.title('Numerical Solutions to Radioactive Decay Equation')
plt.xlabel('Time (s)')
plt.ylabel('Number of Radioactive Atoms')
plt.grid(True)

