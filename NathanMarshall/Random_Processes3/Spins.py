# -*- coding: utf-8 -*-
"""
Created on Tue Oct 22 13:08:25 2019
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

spins = np.random.choice([-1, 1], (numx, numy))

fig, ax = plt.subplots(1,1)
Q = ax.quiver(xx, yy, np.zeros((numx, numy)), spins, scale=25)
ax.scatter(xx, yy)

#%%
def update(frame):
    randrow, randcol = np.random.randint(0, numx, 2)
    spins[randrow][randcol] = np.random.choice([-1, 1])
    Q.set_UVC(np.zeros((numx, numy)), spins)
    return(Q)
    
anim = animate(fig, update, frames=100, interval=50)