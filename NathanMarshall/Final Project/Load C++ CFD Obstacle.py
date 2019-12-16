# -*- coding: utf-8 -*-
"""
Created on Sun Dec  8 09:50:54 2019
Nathan Marshall

Load stream function for CFD computation done in C++ for plotting
"""
#%%
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as patches
nx = 50
ny = 50
h = 1/(nx-1)
sf = np.fromfile('CFD_obstacle2.bin', dtype='double')
sf = np.reshape(sf, (-1, 50))

#%% Extract and plot velocities from stream function
u = np.zeros((nx, ny)) #x velocity
v = np.zeros((nx, ny)) #y velocity
x = np.arange(0, nx-2, 1)
y = np.arange(0, ny-2, 1)

for i in range(1, nx-1):
    for j in range(1, ny-1):
        u[i][j] = (sf[i+1][j] - sf[i-1][j])/(2*h)
        v[i][j] = -(sf[i][j+1] - sf[i][j-1])/(2*h)
        
u = u[1:49][:,1:49] #look at non-boundary values of u
v = v[1:49][:,1:49] #look at non-boundary values of v
fig1, ax = plt.subplots(1, 1)
ax.set_aspect('equal')
ax.streamplot(x, y, u, v, density=5)
obstacle = patches.Rectangle((21, 21), 6, 6)
ax.add_patch(obstacle)
ax.set_title('Fluid Velocity Streamplot')
im = ax.pcolormesh(x, y, np.sqrt(u**2+v**2))
