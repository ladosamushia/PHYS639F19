# -*- coding: utf-8 -*-
"""
Created on Tue Nov 19 13:58:44 2019
Nathan Marshall

2D Heat Equation
"""
#%%
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation as animate

L = 1 #length of rod
num = 100 #number of points
num_steps = 100 #number of time steps
a = 0.002 #thermal conductivity
u = np.zeros((num, num)) #array to hold temperature values for each position
for i in range(45, 55): #set a central square with an initial temperature
    for j in range(45, 55):
        u[i][j] = 1
du = np.zeros((num, num)) #array to contain derivative values
dx = 0.01 #length step
dt = 0.01 #time step

def heat_eqn(u):
    '''Numerical Heat Equation using Finite Differences.'''
    for i in range(1, num-1):
        for j in range(1, num-1):
            du[i][j] = (a * (u[i+1][j] + u[i-1][j] + u[i][j+1] + u[i][j-1]  
                        - 4*u[i][j])/dx**2 )
    for i in range(1, num-1):
        for j in range(1, num-1):
            u[i][j] += du[i][j] * dt
            
fig, ax = plt.subplots(1,1) #create a figure, line, and image object
im = ax.imshow(u) 
ax.set_title('2D Heat Equation')   

def update(step): #animation update function
    heat_eqn(u)
    im.set_array(u)
    return(im)
    
anim = animate(fig, update, frames=num_steps, interval=20)
plt.show()