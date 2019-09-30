# -*- coding: utf-8 -*-
"""
Created on Tue Sep 24 13:13:37 2019
Nathan Marshall

This program computes the trajectory of an object subject to quadratic air
resistance. It also accounts for the acceleration of gravity changing with 
the object's distance from the earth's surface.
"""
#%%
import numpy as np
import matplotlib.pyplot as plt

m = 1 #mass of the projectile in kg
a = 0.002 #linear drag coefficient
b = a/m #ratio of drag coefficent to mass for the diff. eq.
M = 5.9722e24 #mass of earth in kg
r = 6.3781e6 #radius of earth at initial launch position in meters
G = 6.67408e-11 #gravitational constant in m^3/(kg*s^2)

x0 = 0 #initial x coordinate
y0 = 0 #initial y coordinate
vx0 = 1000 #initial x velocity
vy0 = 1000 #initial y velocity
dt = 0.001 #step size for time in seconds
t0 = 0 #initial condition for time in seconds
tmax = 15 #max value of time in seconds

def dvxdt(vx, vy):
    '''Differential equation for x velocity.'''
    return(-b * vx * np.sqrt(vx**2 + vy**2))
    #The differential equation for the x-velocity is simply the component
    #of quadratic air resistance in the x direction.
    
def dvydt(vx, vy, y):
    '''Differential equation for y velocity.'''
    return(-G*M/(r + y)**2 - b * vy * np.sqrt(vx**2 + vy**2))
    #The first term in the differential equation is the acceleration due to 
    #gravity, which varies with the projectile's height. The second term
    #is the quadratic air resistance in the x direction.
    

t = [t0] #list to contain time values
vx = [vx0] #list to contain x velocity values
vy = [vy0] #list to contain y velocity values
x = [x0] #list to contain x values
y = [y0] #list to contain y values

while y[-1] >= 0: #loop until the projectile comes back to the ground, y = 0
    x.append(x[-1] + vx[-1] * dt) #calculate and add next x value
    y.append(y[-1] + vy[-1] * dt) #calculate and add next y value
    vx.append(vx[-1] + dvxdt(vx[-1], vy[-1])*dt) #add dvx/dt * dt to previous vx
    vy.append(vy[-1] + dvydt(vx[-1], vy[-1], y[-1])*dt) #add dvy/dt * dt to previous vy
    t.append(t[-1] + dt) #add new t value to the list
    
max_range = (x[-1] + x[-2])/2 #interpolate to find the maximum x value
tof = (t[-1] + t[-2])/2 #interpolate to find the time of flight
print('The max range of the projectile is {} meters'.format(max_range))
print('The max height of the projectile is {} meters'.format(np.amax(y)))
print('The time of flight of the projectile is {} seconds'.format(tof))

fig, [ax1, ax2, ax3] = plt.subplots(1,3)   

ax1.plot(x, y, label='Numerical Result') #plot projectile trajectory
ax1.set_title('Projectile Motion')
ax1.set_xlabel('X (m)')
ax1.set_ylabel('Y (m)')
ax1.grid()

ax2.plot(t, vx, label='Numerical Result') #plot x-velocity vs. time
ax2.set_title('X Velocity')
ax2.set_xlabel('Time (s)')
ax2.set_ylabel('X Velocity (m/s)')
ax2.grid()

ax3.plot(t, vy, label='Numerical Result') #plot y-velocity vs. time
ax3.set_title('Y Velocity')
ax3.set_xlabel('Time (s)')
ax3.set_ylabel('Y Velocity (m/s)')
ax3.grid()
    


