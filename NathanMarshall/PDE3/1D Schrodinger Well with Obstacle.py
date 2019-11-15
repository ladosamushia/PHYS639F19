# -*- coding: utf-8 -*-
"""
Created on Tue Nov 12 13:59:02 2019
Nathan Marshall

1D Schrodinger Equation - Square well with obstacle in the middle
"""

#%%
import numpy as np
import matplotlib.pyplot as plt

L = 1 #width of the well
E = np.arange(0, 300, 0.1)
psi = 0 #starting value of psi, 0 at well edge
dpsi = 1 #arbitrary choice for starting derivative of psi
dx = 0.001
bounds = [] #list to contain values of psi at the boundary
U = 50 #potential value for the obstacle in the middle

def shoot(psi0, dpsi0, E, L, dx):
    '''Shooting method for Schrodinger eqn.'''
    x = 0 #starting value for x
    while x < L:
        if 0.4 < x < 0.6:
            ddpsi = (U-E) * psi0 #2nd deriv. of psi from Schrodinger eqn.
            dpsi0 += ddpsi * dx
            psi0 += dpsi0 * dx
            x += dx
        else:
            ddpsi = -E * psi0 #2nd deriv. of psi from Schrodinger eqn.
            dpsi0 += ddpsi * dx
            psi0 += dpsi0 * dx
            x += dx
    return(psi0)
    
for e in E: #calculate values of psi at the boundary for all E values
    bounds.append(shoot(psi, dpsi, e, L, dx))
    
cross = [] #list to contain zero crossing energies
asdf = []
for i in range(0, len(bounds)-1): #find where energies cross zero
    
    if bounds[i] > 0 and bounds[i+1] < 0: #interpolate to get better estimate
        cross.append((E[i] + E[i+1])/2)
        asdf.append(i)
        
    if bounds[i] < 0 and bounds[i+1] > 0:
        cross.append((E[i] + E[i+1])/2)
        asdf.append(i)
        
for e in cross: #plot psi vs. x for the energy values that worked
    psi = [0] #starting value of psi, 0 at well edge
    dpsi = [1] #arbitary choice for starting derivative of psi
    x = [0]
    dx = 0.001
    while x[-1] < L:
        if 0.4 < x[-1] < 0.6:
            ddpsi = (U-e) * psi[-1] #2nd deriv. of psi from Schrodinger eqn.
            dpsi.append(dpsi[-1] + ddpsi * dx)
            psi.append(psi[-1] + dpsi[-1] * dx)
            x.append(x[-1] + dx)
        else:
            ddpsi = -e * psi[-1] #2nd deriv. of psi from Schrodinger eqn.
            dpsi.append(dpsi[-1] + ddpsi * dx)
            psi.append(psi[-1] + dpsi[-1] * dx)
            x.append(x[-1] + dx)
    plt.plot(x, psi)
plt.title('Infinite Square Well With Obstacle in Center')
plt.xlabel('x')
plt.ylabel(r'$\psi(x)$')