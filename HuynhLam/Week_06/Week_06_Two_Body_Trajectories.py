# -*- coding: utf-8 -*-
"""
Created on Tue Oct  1 13:05:18 2019

PHYS 639 >>> Assignments >>> Week 6 >>> ODE III
HUYNH LAM

"""
#%%
# Find trajectories of objects that interact with each other via Newtonian gravitational forces
#(T1-T3) Fix one heavy object at the origin and make a second object orbit around it.
#(T3) Same as before but let both objects move.

# Import libraries
import numpy as np #math library
import matplotlib.pyplot as plt # Plotting library

# Acceleration of an object due to gravitational forces of the other two
def acc2(G,x1,y1,m,x2,y2):
    r = np.sqrt((x1-x2)**2+(y1-y2)**2)  
    return -G*m*(x1-x2)/r**3, -G*m*(y1-y2)/r**3

# Function to calculate trajectories step by step
def orbit2(ti, tf, x10, y10, v1x0, v1y0, x20, y20, v2x0, v2y0, Nsteps, G, M1, M2):
    # Initialize array with discrete values of time
    t = np.linspace(ti,tf,Nsteps+1)
    # step size
    dt = (tf - ti)/Nsteps
    # Initialize array to store the solutions
    x1 = np.zeros(len(t))
    y1 = np.zeros(len(t))
    x2 = np.zeros(len(t))
    y2 = np.zeros(len(t))
    # Initial conditions
    x1[0] = x10
    y1[0] = y10
    x2[0] = x20
    y2[0] = y20
    v1x = v1x0
    v1y = v1y0
    v2x = v2x0
    v2y = v2y0
    # From acceleration to velocity to trajectory
    for i in range(Nsteps):
            # Oject 1
            a1x, a1y = acc2(G,x1[i],y1[i],M2,x2[i],y2[i])
            v1x = v1x + a1x*dt
            v1y = v1y + a1y*dt        
            x1[i+1] = x1[i] + v1x*dt
            y1[i+1] = y1[i] + v1y*dt           
            # Object 2
            a2x, a2y = acc2(G,x2[i],y2[i],M1,x1[i],y1[i])   
            v2x = v2x + a2x*dt
            v2y = v2y + a2y*dt            
            x2[i+1] = x2[i] + v2x*dt
            y2[i+1] = y2[i] + v2y*dt            
    return t, x1, y1, x2, y2

# Initial conditions
ti = 0
tf = 10
Nsteps = 1000*tf

x10 = 0
y10 = 0
v1x0 = 0
v1y0 = -0.1

x20 = 1
y20 = 0
v2x0 = 0
v2y0 = 1

G = 1
M_earth = 1
M_moon = 0.1

# Plot
t1,x1,y1,x2,y2 = orbit2(ti, tf, x10, y10, v1x0, v1y0, x20, y20, v2x0, v2y0, Nsteps, G, M_earth, M_moon)
plt.plot(x1, y1, label = 'Heavier object')
plt.plot(x2, y2, label = 'Lighter object')  
plt.legend()
plt.show()