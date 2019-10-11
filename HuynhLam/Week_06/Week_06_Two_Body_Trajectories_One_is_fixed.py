# -*- coding: utf-8 -*-
"""
Created on Tue Oct  1 13:05:18 2019

PHYS 639 >>> Assignments >>> Week 6 >>> ODE III
HUYNH LAM

"""

#%%
# Find trajectories of objects that interact with each other via Newtonian gravitational forces
#(T1-T3) Fix one heavy object at the origin and make a second object orbit around it.

# Import libraries
import numpy as np #math library
import matplotlib.pyplot as plt # Plotting library

#Find trajectories of objects that interact with each other via Newtonian gravitational forces
#(T1-T3) Fix one heavy object at the origin and make a second object orbit around it.

# Acceleration of an object due to gravitational forces of the other two
def acc(G,M,r,x,y):
    return -G*M*x/r**3, -G*M*y/r**3

# Function to calculate trajectories step by step
def orbit(ti, tf, x0, y0, vx0, vy0, Nsteps, G, M):
    # Initialize array with discrete values of time
    t = np.linspace(ti,tf,Nsteps)
    # Initialize array to store the solution
    x = np.zeros(len(t))
    y = np.zeros(len(t))
    # step size
    dt = (tf - ti)/Nsteps
    # Initial conditions
    x[0] = x0
    y[0] = y0
    vx = vx0
    vy = vy0
    for i in range(1,Nsteps):
            r = np.sqrt(x[i-1]**2+y[i-1]**2)
            ax, ay = acc(G,M,r,x[i-1],y[i-1])
            vx = vx + ax*dt
            vy = vy + ay*dt
            x[i] = x[i-1] + vx*dt
            y[i] = y[i-1] + vy*dt
    return t, x, y

# Inital conditions
ti = 0
tf = 4000
x0 = 100
y0 = 0
vx0 = 0.05
vy0 = 0.05
Nsteps = 100000
G = 1
M = 1

# Plot
t1,x1,y1 = orbit(ti, tf, 100, 0, 0, vy0, Nsteps, G, M)
plt.plot(x1, y1, label = 'Trajectory')
plt.legend()
plt.show()