# -*- coding: utf-8 -*-
"""
Created on Tue Oct  1 13:14:58 2019
Nathan Marshall

This code simulates the orbit of an object around a stationary central mass.
"""
#%%
import matplotlib.pyplot as plt

x0 = 1 #initial x
y0 = 0 #initial y
vx0 = 0 #initial x velocity
vy0 = 0 #initial y velocity
t0 = 0 #start time
tmax = 10 #stop time
dt = 0.001 #time step size

G = 1 #gravitational constant
M = 1 #mass of central object

x = [x0] #list to contain x values
y = [y0] #list to contain y values
vx = [vx0] #list to contain x velocities
vy = [vy0] #list to contain y velocities
t = [t0] #list to contain time values

def dvxdt(x, y):
    '''Diff. eq. for x velocity'''
    return(- G * M * x / ((x**2 + y**2)**(3/2)))
    
def dvydt(x, y):
    '''Diff. eq. for y velocity'''
    return(-G * M * y / ((x**2 + y**2)**(3/2)))
    
while t[-1] < tmax:
    x.append(x[-1] + vx[-1]*dt)
    y.append(y[-1] + vy[-1]*dt)
    vx.append(vx[-1] + dvxdt(x[-1], y[-1]) * dt)
    vy.append(vy[-1] + dvydt(x[-1], y[-1]) * dt)
    t.append(t[-1] + dt)
    
fig = plt.figure('Orbital Trajectory')
plt.title('Orbital Trajectory')
plt.xlabel('X (m)')
plt.ylabel('Y (m)')
plt.plot(x, y)
