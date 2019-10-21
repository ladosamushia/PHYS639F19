# -*- coding: utf-8 -*-
"""
Created on Tue Oct  8 13:10:43 2019
Nathan Marshall

Random walk in 1D
"""
#%%
import numpy as np
import matplotlib.pyplot as plt
num_steps = 1000
dx = 1
x0 = 0
t = np.arange(0, num_steps+1)
x = [x0]

for i in range(0, num_steps):
    x.append(x[-1] + np.random.choice([-dx, dx]))

fig1 = plt.figure()
plt.plot(t, x)
plt.xlabel('Time (s)')
plt.ylabel('Displacement (m)')
plt.title('Random Walk 1D')
