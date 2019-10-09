# -*- coding: utf-8 -*-
"""
Created on Tue Oct  8 19:56:04 2019
Nathan Marshall

An animated random walk where each step of the particle is in the direction of 
a random unit vector.
"""
#%%
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from random import gauss
from matplotlib.animation import FuncAnimation as animate

def rand_vector():
    vec = [gauss(0, 1) for i in range(3)]
    mag = sum(x**2 for x in vec) ** 0.5
    return [x/mag for x in vec]

num_steps = 1000
dx = 1
dy = 1
dz = 1
x0 = 0
y0 = 0
z0 = 0
x = [x0]
y = [y0]
z = [z0]

for i in range(0, num_steps):
    dx, dy, dz = rand_vector()
    x.append(x[-1] + dx)
    y.append(y[-1] + dy)
    z.append(z[-1] + dz)
    
fig1 = plt.figure()
ax = fig1.add_subplot(111, projection='3d')
line, = ax.plot([], [], [])
ax.set_xlabel('X Displacement (m)')
ax.set_ylabel('Y Displacement (m)')
ax.set_zlabel('Z Displacement (m)')
ax.set_title('3D Random Walk')
ax.set_xlim3d(-20, 20)
ax.set_ylim3d(-20, 20)
ax.set_zlim3d(-20, 20)

frame_rate = 1/24 * 1000
num_frames = 1000
fstep = round(num_steps/num_frames)

def animation(frame):
    line.set_xdata(x[0:frame*fstep])
    line.set_ydata(y[0:frame*fstep])
    line.set_3d_properties(z[0:frame*fstep])
    return(line,)
    
anim = animate(fig1, animation, frames=num_frames, interval=frame_rate)

