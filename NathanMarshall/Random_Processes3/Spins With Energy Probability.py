# -*- coding: utf-8 -*-
"""
Created on Tue Oct 22 13:51:00 2019
Nathan Marshall

"""
#%%
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation as animate

numx = 10
numy = 10
x = np.arange(0, numx)
y = np.arange(0, numy)
xx, yy = np.meshgrid(x, y)
T = 0.1
spins = np.random.choice([-1, 1], (numx, numy))

fig, ax = plt.subplots(1,1)
Q = ax.quiver(xx, yy, np.zeros((numx, numy)), spins, spins, scale=25, 
              cmap='plasma')
ax.scatter(xx, yy)
ax.set_aspect('equal')
#%%
def update(frame):
    randrow, randcol = np.random.randint(0, numx, 2)
    randspin = spins[randrow][randcol]
    energy = 0
    if randrow == 0:
        energy += -randspin*spins[randrow + 1][randcol]
    if randrow == numx - 1:
        energy += -randspin*spins[randrow - 1][randcol]
    if randcol == 0:
        energy += -randspin*spins[randrow][randcol + 1]
    if randcol == numy - 1:
        energy += -randspin*spins[randrow][randcol - 1]
    if randrow != (numx - 1) and randrow != 0:
        if randcol != (numy - 1) and randcol != 0:
            energy += -randspin*spins[randrow + 1][randcol]
            energy += -randspin*spins[randrow - 1][randcol]
            energy += -randspin*spins[randrow][randcol + 1]
            energy += -randspin*spins[randrow][randcol - 1]
    if randspin == -1:
        p_down = np.exp(-energy / T) / (np.exp(-energy / T) + np.exp(energy / T))
        p_up = np.exp(energy / T) / (np.exp(-energy / T) + np.exp(energy / T)) 
    if randspin == 1:
        p_up = np.exp(-energy / T) / (np.exp(-energy / T) + np.exp(energy / T))
        p_down = np.exp(energy / T) / (np.exp(-energy / T) + np.exp(energy / T))
    spins[randrow][randcol] = np.random.choice([-1, 1], p=[p_down, p_up])
    Q.set_UVC(np.zeros((numx, numy)), spins, spins)
    return(Q)
    
anim = animate(fig, update, frames=1000, interval=10, repeat=False)
