# -*- coding: utf-8 -*-
"""
Created on Thu Nov 14 13:17:13 2019
Nathan Marshall

1D Schrodinger Equation - Harmonic Potential
Finding the first three solutions using the 'shooting' method.
"""
#%%
import numpy as np
import matplotlib.pyplot as plt

L = 1 #width of the well
E = np.arange(0, 71, 0.003)
psi = 0 #starting value of psi, 0 at well edge
dpsi = 1 #arbitrary choice for starting derivative of psi
dx = 0.01
bounds = [] #list to contain values at the boundary

def shoot(psi0, dpsi0, E, L, dx):
    '''Shooting method for Schrodinger eqn.'''
    x = -L #starting value for x
    while x < L:
        U = 200*x**2 #harmonic potential, parabola dependent on x
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
        
for e in cross:
    psi = [0] #starting value of psi, 0 at well edge
    dpsi = [1] #arbitary choice for starting derivative of psi
    x = [-L]
    while x[-1] < L:
        U = 200*x[-1]**2 #harmonic potential, parabola dependent on x
        ddpsi = (U-e) * psi[-1] #2nd deriv. of psi from Schrodinger eqn.
        dpsi.append(dpsi[-1] + ddpsi * dx)
        psi.append(psi[-1] + dpsi[-1] * dx)
        x.append(x[-1] + dx)
    plt.plot(x, psi)
plt.title('First Three Harmonic Potential Solutions')
plt.xlabel('x')
plt.ylabel(r'$\psi(x)$')