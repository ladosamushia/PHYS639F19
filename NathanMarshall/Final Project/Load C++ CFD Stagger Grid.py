# -*- coding: utf-8 -*-
"""
Created on Tue Dec 10 14:47:18 2019
Nathan Marshall

"""
#%%
import numpy as np
import matplotlib.pyplot as plt
nx = 128
ny = 128
u = np.zeros(nx*ny) #x velocity
v = np.zeros(nx*ny) #y velocity

data = np.fromfile('CFDstag.bin', dtype='double')
u = data[0:nx*ny]
v = data[nx*ny:nx*ny*2]

u = np.reshape(u, (-1, nx))
v = np.reshape(v, (-1, nx))

#%% plot velocities
stream_points = np.array(zip(np.arange(0,128,1), -np.arange(0,128,1)))
x = np.arange(0, nx, 1)
y = np.arange(0, ny, 1)
fig1, ax = plt.subplots(1, 1)
ax.set_aspect('equal')
ax.streamplot(x, y, v, u, density=4, arrowsize=0, start_points=stream_points)
ax.set_title('Fluid Velocity Streamplot')
im = ax.pcolormesh(x, y, np.sqrt(u**2+v**2))
fig1.colorbar(im)