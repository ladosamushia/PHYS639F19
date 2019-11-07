# -*- coding: utf-8 -*-
"""
Created on Tue Nov  5 13:08:12 2019
Nathan Marshall

Partial differential equations: waves on a string. 
"""
#%%
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation as animate

#set initial conditions of position and derivative of position
num_points = 100
fi = np.exp(-(np.linspace(-3, 10, num_points))**2)
fi[0], fi[-1] = 0, 0

#fi = np.zeros(num_points)
#for i in range(0, 49):
#    fi[i] = i / 49
#for i in range(0, 49):
#    fi[i + 49] = (49 - i)/49

dfi = np.zeros(num_points)
dt = 0.01
dx = 0.01

#%% animation
        
x = np.arange(0, num_points)
fig, ax = plt.subplots(1,1)
line, = ax.plot(x, fi)
ax.set_ylim(-1, 1)
ax.set_title('Wave Equation 1D Numerical Solution')
def update(frame):
    for i in range(1, num_points-1):
        dfi[i] += (fi[i+1] - 2*fi[i] + fi[i-1])/dx**2 * dt
    for i in range(1, num_points-1):
        fi[i] += dfi[i] * dt
    line.set_data(x, fi)
    return(line,)
    
anim = animate(fig, update, frames=100, interval=50)