# -*- coding: utf-8 -*-
"""
Created on Tue Oct  8 13:45:25 2019
Nathan Marshall

Random walk in 3D
"""
#%%
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

num_steps = 10000
dx = 1
dy = 1
dz = 1
x0 = 0
y0 = 0
z0 = 0
x = [x0]
y = [y0]
z = [z0]

for i in range(0, num_steps):
    x.append(x[-1] + np.random.choice([-dx, dx]))
    y.append(y[-1] + np.random.choice([-dy, dy]))
    z.append(z[-1] + np.random.choice([-dz, dz]))
    
fig1 = plt.figure()
ax = fig1.add_subplot(111, projection='3d')
ax.plot(x, y, z)
ax.set_xlabel('X Displacement (m)')
ax.set_ylabel('Y Displacement (m)')
ax.set_zlabel('Z Displacement (m)')
ax.set_title('3D Random Walk')
