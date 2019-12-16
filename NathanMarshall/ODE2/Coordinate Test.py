# -*- coding: utf-8 -*-
"""
Created on Sat Sep 28 18:31:03 2019
Nathan Marshall

This program tests a set of formulae I came up with to determine the x, y, and
z components of velocity for a projectile launched from the earth's surface.
"""
#%%
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np

longitude = 0 * np.pi/180 #longitude defined as regular longitude
latitude = 45 * np.pi/180 #defined as angle from earth's north pole
inclination = 0 * np.pi/180 #defined as the angle from vertical for an observer
angle = 0 * np.pi/180 #defined as angle north of east for an observer
v = 1 #magnitude of initial velocity
#determine velocity in x, y, and z as well as initial position on earth's sphere
vx = v * np.sin(latitude - inclination) * np.cos(longitude - angle)
vy = v * np.sin(latitude - inclination) * np.sin(longitude - angle)
vz = v * np.cos(latitude - inclination)
x0 = np.cos(longitude) * np.sin(latitude)
y0 = np.sin(longitude) * np.sin(latitude)
z0 = np.cos(latitude)
#display velocity results
print('Vx: ', vx)
print('Vy: ', vy)
print('Vz: ', vz)

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# generate a sphere to plot velocity vector on
u = np.linspace(0, 2 * np.pi, 100)
v = np.linspace(0, np.pi, 100)
x = np.outer(np.cos(u), np.sin(v))
y = np.outer(np.sin(u), np.sin(v))
z = np.outer(np.ones(np.size(u)), np.cos(v))

# Plot the sphere and velocity vector
ax.plot_surface(x, y, z, rcount = 25, ccount = 25)
ax.quiver(x0, y0, z0, vx, vy, vz, color='r')
plt.show()