# -*- coding: utf-8 -*-
"""
Created on Tue Nov 19 13:10:58 2019
Nathan Marshall

1D Heat Equation - Metal Rod with Fixed Endpoints
"""
#%%
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation as animate

L = 1 #length of rod
num = 100 #number of points
num_steps = 100 #number of time steps
a = 0.001 #thermal conductivity
u = np.zeros(num) #array to hold temperature values for each position
u[49] = 1 #set the middle temperature to 1
du = np.zeros(num) #array to contain derivative values
x = np.linspace(0, L, num) #array of x values for plotting
dx = 0.01 #length step
dt = 0.01 #time step

def heat_eqn(u):
    '''Numerical Heat Equation using Finite Differences.'''
    for i in range(1, num-1):
        du[i] = a * (u[i+1] + u[i-1] - 2*u[i])/dx**2 
    for i in range(1, num-1):
        u[i] += du[i] * dt
        
fig, ax = plt.subplots(1,1) #create a figure, line, and axes object
line, = ax.plot([], []) 
ax.set_title('1D Heat Equation with Fixed Boundaries')   
ax.set_ylabel('Temperature')
ax.set_xlabel('Position along Rod')
def update(step): #animation update function
    line.set_data(x, u)
    heat_eqn(u)
    return(line,)
    
anim = animate(fig, update, frames=num_steps, interval=20)
plt.show()