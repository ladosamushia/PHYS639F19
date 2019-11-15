# -*- coding: utf-8 -*-
"""
Created on Tue Nov 12 13:13:27 2019
Nathan Marshall

1D Schrodinger Equation - Square Well
Finding the first five solutions using the 'shooting' method.
"""
#%%
import numpy as np
import matplotlib.pyplot as plt

L = 1 #width of the well
E = np.arange(0, 300, 0.1)
psi = 0 #starting value of psi, 0 at well edge
dpsi = 1 #arbitrary choice for starting derivative of psi
dx = 0.01
bounds = [] #list to contain values at the boundary

def shoot(psi0, dpsi0, E, L, dx):
    '''Shooting method for Schrodinger eqn.'''
    x = 0 #starting value for x
    while x < L:
        ddpsi = -E * psi0 #2nd deriv. of psi from Schrodinger eqn.
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
        
for e in cross:
    psi = [0] #starting value of psi, 0 at well edge
    dpsi = [1] #arbitary choice for starting derivative of psi
    x = [0]
    dx = 0.01
    while x[-1] < L:
        ddpsi = -e * psi[-1] #2nd deriv. of psi from Schrodinger eqn.
        dpsi.append(dpsi[-1] + ddpsi * dx)
        psi.append(psi[-1] + dpsi[-1] * dx)
        x.append(x[-1] + dx)
    plt.plot(x, psi)
plt.title('First Five Infinite Square Well Solutions')
plt.xlabel('x')
plt.ylabel(r'$\psi(x)$')