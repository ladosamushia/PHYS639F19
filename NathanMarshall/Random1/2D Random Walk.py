# -*- coding: utf-8 -*-
"""
Created on Tue Oct  8 13:42:30 2019
Nathan Marshall

Random walk in 2D
"""
#%%
import numpy as np
import matplotlib.pyplot as plt
num_steps = 10000
dx = 1
dy = 1
x0 = 0
y0 = 0
x = [x0]
y = [y0]

for i in range(0, num_steps):
    x.append(x[-1] + np.random.choice([-dx, dx]))
    y.append(y[-1] + np.random.choice([-dy, dy]))

fig1 = plt.figure()
plt.plot(x, y)
plt.xlabel('X Displacement (m)')
plt.ylabel('Y Displacement (m)')
plt.title('Random Walk 2D')