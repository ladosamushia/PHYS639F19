# -*- coding: utf-8 -*-
"""
Created on Thu Nov 14 13:55:51 2019
Nathan Marshall

1D Schrodinger Equation - Lennard-Jones Potential
Finding the first two solutions using the 'shooting' method.
"""
#%% Run to find approximate solutions, this takes a while...
#Run the next section of code to see my predetermined solutions
import numpy as np

L = 3 #width of the well
x0 = 0.4
E = np.arange(-110, 0, 0.001)
psi = 0 #starting value of psi, 0 at well edge
dpsi = 1 #arbitrary choice for starting derivative of psi
dx = 0.01
bounds = [] #list to contain values at the boundary

def shoot(psi0, dpsi0, E, L, dx):
    '''Shooting method for Schrodinger eqn.'''
    x = x0 #starting value for x
    while x < L:
        U = 1/x**12 - 30/x**6 #Lennard-Jones potential function
        ddpsi = (U-E) * psi0 #2nd deriv. of psi from Schrodinger eqn.
        dpsi0 += ddpsi * dx
        psi0 += dpsi0 * dx
        x += dx
    return(psi0)
    
for e in E:
    bounds.append(shoot(psi, dpsi, e, L, dx))
    
cross = [] #list to contain zero crossing energies
for i in range(0, len(bounds)-1):
    
    if bounds[i] > 0 and bounds[i+1] < 0:
        cross.append((E[i] + E[i+1])/2)
        
    if bounds[i] < 0 and bounds[i+1] > 0:
        cross.append((E[i] + E[i+1])/2)
        
#%% Plot pre-determined solutions from this code
import matplotlib.pyplot as plt

L = 3 #width of the well
cross = [-108.5907658225, -9.0465]
x0 = 0.4
dx = 0.01
for e in cross:
    psi = [0] #starting value of psi, 0 at well edge
    dpsi = [1] #arbitary choice for starting derivative of psi
    x = [x0]
    while x[-1] < L:
        U = 1/x[-1]**12 - 30/x[-1]**6 #Lennard-Jones potential function
        ddpsi = (U-e) * psi[-1] #2nd deriv. of psi from Schrodinger eqn.
        dpsi.append(dpsi[-1] + ddpsi * dx)
        psi.append(psi[-1] + dpsi[-1] * dx)
        x.append(x[-1] + dx)
    plt.plot(x, psi)
plt.title('Lennard-Jones Potential Solutions')
plt.xlabel('x')
plt.ylabel(r'$\psi(x)$')