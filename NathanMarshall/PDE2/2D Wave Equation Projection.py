# -*- coding: utf-8 -*-
"""
Created on Thu Nov  7 14:06:58 2019
Nathan Marshall

"""
#%%
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation as animate

#set initial conditions of position and derivative of position
num_points = 100
#standing wave initial conditions
#x = np.linspace(-2*np.pi, 2*np.pi, num_points)
#y = np.linspace(-2*np.pi, 2*np.pi, num_points)
#x, y = np.meshgrid(x, y)
#fi = np.sin(x)*np.sin(y)
#gaussian initial conditions
x = np.linspace(-5, 5, num_points)
y = np.linspace(-5, 5, num_points)
x, y = np.meshgrid(x, y)
fi = np.exp(-(x**2+y**2))
dfi = np.zeros((num_points, num_points))
dt = 0.005
dx = 0.01

#%% animation
        
fig, ax = plt.subplots(1,1)
im = ax.imshow(fi)
ax.set_title('Wave Equation 2D Numerical Solution')

def update(frame):
    for i in range(1, num_points-1):
        for j in range(1, num_points-1):
                dfi[i][j] += ((fi[i+1][j] + fi[i-1][j] + fi[i][j+1] + fi[i][j-1] 
                               - 4*fi[i][j])/dx**2) * dt
    for i in range(1, num_points-1):
        for j in range(1, num_points-1):
            fi[i][j] += dfi[i][j] * dt
    im.set_array(fi)
    return(im)
    
anim = animate(fig, update, frames=100, interval=50)

