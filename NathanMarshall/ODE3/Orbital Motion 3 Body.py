# -*- coding: utf-8 -*-
"""
Created on Tue Oct  1 14:04:26 2019
Nathan Marshall

This code simulates the orbital trajectories of a 3 body system where all 
three masses are allowed to move.
"""
#%%
import matplotlib.pyplot as plt
x10 = 0 #initial x mass 1
y10 = 0 #initial y mass 1
vx10 = 0 #initial x velocity mass 1
vy10 = -0.8 #initial y velocity mass 1

x20 = 1 #initial x mass 2
y20 = 0 #initial y mass 2
vx20 = 0 #initial x velocity mass 2
vy20 = 0.8 #initial y velocity mass 2

x30 = -2 #initial x mass 3
y30 = 0 #initial y mass 3
vx30 = 0 #initial x velocity mass 3
vy30 = -0.8 #initial y velocity mass 3

t0 = 0 #start time
tmax = 10 #stop time
dt = 0.001 #time step size

G = 1 #gravitational constant
m1 = 1 #mass 1
m2 = 1 #mass 2
m3 = 0.0001 #mass 3

x1 = [x10] #list to contain x values mass 1
y1 = [y10] #list to contain y values mass 1
vx1 = [vx10] #list to contain x velocities mass 1
vy1 = [vy10] #list to contain y velocities mass 1

x2 = [x20] #list to contain x values mass 2
y2 = [y20] #list to contain y values mass 2
vx2 = [vx20] #list to contain x velocities mass 2
vy2 = [vy20] #list to contain y velocities mass 2

x3 = [x30] #list to contain x values mass 3
y3 = [y30] #list to contain y values mass 3
vx3 = [vx30] #list to contain x velocities mass 3
vy3 = [vy30] #list to contain y velocities mass 3

t = [t0] #list to contain time values

def gravx(x1, y1, x2, y2, m):
    '''Acceleration due to gravitation in x direction.'''
    x = x1 - x2
    y = y1 - y2
    return(- G * m * x / ((x**2 + y**2)**(3/2)))
def gravy(x1, y1, x2, y2, m):
    '''Acceleration due to gravitation in y direction.'''
    x = x1 - x2
    y = y1 - y2
    return(- G * m * y / ((x**2 + y**2)**(3/2)))   
    
while t[-1] < tmax:
    x1.append(x1[-1] + vx1[-1]*dt)
    y1.append(y1[-1] + vy1[-1]*dt)
    vx1.append(vx1[-1] + (gravx(x1[-1], y1[-1], x2[-1], y2[-1], m2) 
               + gravx(x1[-1], y1[-1], x3[-1], y3[-1], m3)) * dt)
    vy1.append(vy1[-1] + (gravy(x1[-1], y1[-1], x2[-1], y2[-1], m2) +
               gravy(x1[-1], y1[-1], x3[-1], y3[-1], m3)) * dt)
    
    x2.append(x2[-1] + vx2[-1]*dt)
    y2.append(y2[-1] + vy2[-1]*dt)
    vx2.append(vx2[-1] + (gravx(x2[-1], y2[-1], x1[-1], y1[-1], m1) 
               + gravx(x2[-1], y2[-1], x3[-1], y3[-1], m3)) * dt)
    vy2.append(vy2[-1] + (gravy(x2[-1], y2[-1], x1[-1], y1[-1], m1) +
               gravy(x2[-1], y2[-1], x3[-1], y3[-1], m3)) * dt)
    
    x3.append(x3[-1] + vx3[-1]*dt)
    y3.append(y3[-1] + vy3[-1]*dt)
    vx3.append(vx3[-1] + (gravx(x3[-1], y3[-1], x1[-1], y1[-1], m1) 
               + gravx(x3[-1], y3[-1], x2[-1], y2[-1], m2)) * dt)
    vy3.append(vy3[-1] + (gravy(x3[-1], y3[-1], x1[-1], y1[-1], m1) +
               gravy(x3[-1], y3[-1], x2[-1], y2[-1], m2)) * dt)
    
    t.append(t[-1] + dt)

fig = plt.figure('Orbital Trajectory')
plt.title('Orbital Trajectory')
plt.xlabel('X (m)')
plt.ylabel('Y (m)')
plt.plot(x1, y1, label='Mass 1')
plt.plot(x2, y2, label='Mass 2')
plt.plot(x3, y3, label='Mass 3')
plt.legend()