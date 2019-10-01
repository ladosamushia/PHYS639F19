# -*- coding: utf-8 -*-
"""
Created on Tue Oct  1 13:46:59 2019
Nathan Marshall

This code simulates the motion of a two body orbital system where both masses
are allowed to move.
"""
#%%
import matplotlib.pyplot as plt

x10 = 1 #initial x small mass
y10 = 0 #initial y small mass
vx10 = 0 #initial x velocity small mass
vy10 = 1 #initial y velocity small mass

x20 = 0 #initial x large mass
y20 = 0 #initial y large mass
vx20 = 0 #initial x velocity large mass
vy20 = -0.1 #initial y velocity large mass

t0 = 0 #start time
tmax = 10 #stop time
dt = 0.001 #time step size

G = 1 #gravitational constant
M = 1 #mass of large object
m = 0.1 #mass of small object

x1 = [x10] #list to contain x values small mass
y1 = [y10] #list to contain y values small mass
vx1 = [vx10] #list to contain x velocities small mass
vy1 = [vy10] #list to contain y velocities small mass

x2 = [x20] #list to contain x values large mass
y2 = [y20] #list to contain y values large mass
vx2 = [vx20] #list to contain x velocities large mass
vy2 = [vy20] #list to contain y velocities large mass
t = [t0] #list to contain time values

def dvxdt(x1, y1, x2, y2, m):
    '''Diff. eq. for x velocity'''
    x = x1 - x2
    y = y1 - y2
    return(- G * m * x / ((x**2 + y**2)**(3/2)))
    
def dvydt(x1, y1, x2, y2, m):
    '''Diff. eq. for y velocity'''
    x = x1 - x2
    y = y1 - y2
    return(-G * m * y / ((x**2 + y**2)**(3/2)))
    

while t[-1] < tmax:
    x1.append(x1[-1] + vx1[-1]*dt)
    y1.append(y1[-1] + vy1[-1]*dt)
    vx1.append(vx1[-1] + dvxdt(x1[-1], y1[-1], x2[-1], y2[-1], M) * dt)
    vy1.append(vy1[-1] + dvydt(x1[-1], y1[-1], x2[-1], y2[-1], M) * dt)
    x2.append(x2[-1] + vx2[-1]*dt)
    y2.append(y2[-1] + vy2[-1]*dt)
    vx2.append(vx2[-1] - dvxdt(x1[-1], y1[-1], x2[-1], y2[-1], m) * dt)
    vy2.append(vy2[-1] - dvydt(x1[-1], y1[-1], x2[-1], y2[-1], m) * dt)
    t.append(t[-1] + dt)
    
fig = plt.figure('Orbital Trajectory')
plt.title('Orbital Trajectory')
plt.xlabel('X (m)')
plt.ylabel('Y (m)')
plt.plot(x1, y1, label='Small Mass')
plt.plot(x2, y2, label='Large Mass')
plt.legend()

