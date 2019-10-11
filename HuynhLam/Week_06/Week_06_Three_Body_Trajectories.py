# -*- coding: utf-8 -*-
"""
Created on Tue Oct  1 13:05:18 2019

PHYS 639 >>> Assignments >>> Week 6 >>> ODE III
HUYNH LAM

"""
#%%
# Find trajectories of objects that interact with each other via Newtonian gravitational forces.
# Three objects in orbits.

# Import libraries
import numpy as np #math library
import matplotlib.pyplot as plt # Plotting library

# Acceleration of an object due to gravitational forces of the other two
def acc3(G,x1,y1,m2,x2,y2,m3,x3,y3):
    r12 = np.sqrt((x1-x2)**2+(y1-y2)**2)
    r13 = np.sqrt((x1-x3)**2+(y1-y3)**2)
    return -G*m2*(x1-x2)/r12**3-G*m3*(x1-x3)/r13**3, -G*m2*(y1-y2)/r12**3-G*m3*(y1-y3)/r13**3

# Function to calculate trajectories step by step
def orbit3(ti, tf, x10, y10, v1x0, v1y0, x20, y20, v2x0, v2y0, x30, y30, v3x0, v3y0, Nsteps, G, M1, M2, M3):
    # Initialize array with discrete values of time
    t = np.linspace(ti,tf,Nsteps+1)
    # step size
    dt = (tf - ti)/Nsteps
    # Initialize array to store the solutions
    x1 = np.zeros(len(t))
    y1 = np.zeros(len(t))
    x2 = np.zeros(len(t))
    y2 = np.zeros(len(t))
    x3 = np.zeros(len(t))
    y3 = np.zeros(len(t))
    # Initial conditions
    x1[0] = x10
    y1[0] = y10
    x2[0] = x20
    y2[0] = y20
    x3[0] = x30
    y3[0] = y30
    v1x = v1x0
    v1y = v1y0
    v2x = v2x0
    v2y = v2y0
    v3x = v3x0
    v3y = v3y0
    # From acceleration to velocity to trajectory
    for i in range(Nsteps):
            # First object
            a1x, a1y = acc3(G,x1[i],y1[i],M2,x2[i],y2[i],M3,x3[i],y3[i])
            v1x = v1x + a1x*dt
            v1y = v1y + a1y*dt        
            x1[i+1] = x1[i] + v1x*dt
            y1[i+1] = y1[i] + v1y*dt           
            # Second object
            a2x, a2y = acc3(G,x2[i],y2[i],M1,x1[i],y1[i],M3,x3[i],y3[i])
            v2x = v2x + a2x*dt
            v2y = v2y + a2y*dt            
            x2[i+1] = x2[i] + v2x*dt
            y2[i+1] = y2[i] + v2y*dt
            # Third object
            a3x, a3y = acc3(G,x3[i],y3[i],M1,x1[i],y1[i],M2,x2[i],y2[i])
            v3x = v3x + a3x*dt
            v3y = v3y + a3y*dt            
            x3[i+1] = x3[i] + v3x*dt
            y3[i+1] = y3[i] + v3y*dt
            
    return t, x1, y1, x2, y2, x3, y3

#Three body configuration
# Similar to sun-earth-moon configuration.   
t11,x11,y11,x21,y21,x31,y31 = orbit3(0, 2, 0, 0, 0, 0, 1, 0, 0, -2, 1.01, 0, 0, 1.01, 2000, 1, 10, 0.1, 0.001)

# Three body configuration
# Similar to sun-earth-jupiter configuration.
t1,x1,y1,x2,y2,x3,y3 = orbit3(0, 130, 0, 0, 0, 0, 15, 0, 0, 3, 100, 0, 0, 1.2, 13000, 1, 500, 0.01, 1)

# Plots    
fig, (ax0, ax1) = plt.subplots(2, 1)
ax0.plot(x11, y11, label = 'Heavy object')
ax0.legend(loc="center")
ax0.plot(x21, y21, label = 'Small object')
ax0.legend(loc="center")
ax0.plot(x31, y31, label = 'Satellite of small object')
ax0.legend(loc="center")
ax1.plot(x1, y1, label = 'Heavy object')
ax1.legend(loc="center")
ax1.plot(x2, y2, label = 'Smallest object')
ax1.legend(loc="center")
ax1.plot(x3, y3, label = 'Small object')
ax1.legend(loc="center")
plt.legend()
plt.show()