# -*- coding: utf-8 -*-
"""
Created on Thu Sep 26 13:17:21 2019
Nathan Marshall

Work in progress!

This program computes the trajectory of a projectile on earth. It accounts for 
air resistance, variation of gravity, and Coriolis force.
"""
#%%
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

m = 1 #mass of the projectile in kg
a = 0 #linear drag coefficient
b = a/m #ratio of drag coefficent to mass for the diff. eq.
M = 5.9722e24 #mass of earth in kg
R = 6.3781e6 #radius of earth at initial launch position in meters
G = 6.67408e-11 #gravitational constant in m^3/(kg*s^2)
#omega = 7.2921159e-5 #angular velocity of earth in rad/sec
omega = 7.2921159e-3
longitude = 0 * np.pi/180
latitude = 0 * np.pi/180
inclination = 45 * np.pi/180 
angle = 0 * np.pi/180
v = 1000
x0 = R * np.cos(longitude) * np.sin(latitude)
y0 = R * np.sin(longitude) * np.sin(latitude)
z0 = R * np.cos(latitude)
#vx0 = v * np.sin(latitude - inclination) * np.cos(longitude - angle)
#vy0 = v * np.sin(latitude - inclination) * np.sin(longitude - angle)
#vz0 = v * np.cos(latitude - inclination)
vx0 = 1000
vy0 = 1000
vz0 = 1000


dt = 0.001 #step size for time in seconds
t0 = 0 #initial condition for time in seconds
tmax = 15 #max value of time in seconds

def dvxdt(x, y, z, vx, vy, vz, g, r):
    '''Differential equation for x velocity.'''
    gravx = -g * x / r
    return -gravx -b * vx * np.sqrt(vx**2 + vy**2 + vz**2)
    
def dvydt(x, y, z, vx, vy, vz, g, r):
    '''Differential equation for y velocity.'''
    y_cor = 2 * m * vz * omega
    gravy = -g * y / r
    return -gravy -b * vy * np.sqrt(vx**2 + vy**2 + vz**2) + y_cor
    
def dvzdt(x, y, z, vx, vy, vz, g, r):
    '''Differential equation for z velocity.'''
    gravz = -g * z / r
    z_cor = -2 * m * vy * omega 
    return -gravz - b * vz * np.sqrt(vx**2 + vy**2 + vz**2) + z_cor
    

t = [t0] #list to contain time values
vx = [vx0] #list to contain x velocity values
vy = [vy0] #list to contain y velocity values
vz = [vz0] #list to contain z velocity values
x = [x0] #list to contain x values
y = [y0] #list to contain y values
z = [z0] #list to contain z values

while x[-1]**2 + y[-1]**2 + z[-1]**2 >= R**2: 
    r = np.sqrt(x[-1]**2 + y[-1]**2 + z[-1]**2)
    g = -G*M/r**2
    x.append(x[-1] + vx[-1] * dt) #calculate and add next x value
    y.append(y[-1] + vy[-1] * dt) #calculate and add next y value
    z.append(z[-1] + vx[-1] * dt)
    vx.append(vx[-1] + dvxdt(x[-1], y[-1], z[-1], vx[-1], vy[-1], vz[-1], g, r)*dt) #add dvx/dt * dt to previous vx
    vy.append(vy[-1] + dvydt(x[-1], y[-1], z[-1], vx[-1], vy[-1], vz[-1], g, r)*dt) #add dvy/dt * dt to previous vy
    vz.append(vz[-1] + dvzdt(x[-1], y[-1], z[-1], vx[-1], vy[-1], vz[-1], g, r)*dt)
    t.append(t[-1] + dt) #add new t value to the list
    

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d') 

ax.plot(x, y, z) #plotting numerical result

#
## Make data
#u = np.linspace(0, 2 * np.pi, 100)
#v2 = np.linspace(0, np.pi, 100)
#x2 = R * np.outer(np.cos(u), np.sin(v2))
#y2 = R * np.outer(np.sin(u), np.sin(v2))
#z2 = R * np.outer(np.ones(np.size(u)), np.cos(v2))
#
## Plot the surface
#ax.plot_surface(x2, y2, z2, rcount = 25, ccount = 25)

