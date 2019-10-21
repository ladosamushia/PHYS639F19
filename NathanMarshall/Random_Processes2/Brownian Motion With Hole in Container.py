# -*- coding: utf-8 -*-
"""
Created on Thu Oct 17 13:23:24 2019
Nathan Marshall

2D random walk with a hole in the container.
"""
#%%
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation as animate
from random import gauss

num_particles = 100
num_steps = 400
xmin, xmax = [0, 10]
ymin, ymax = [0, 10]
y_hole1, y_hole2 = [1, 9]

x_all = np.zeros([num_steps, num_particles])
y_all = np.zeros([num_steps, num_particles])
x_all[0] = num_particles * [5]
y_all[0] = num_particles * [5]

def rand_vector():
    vec = [gauss(0, 1) for i in range(2)]
    mag = sum(x**2 for x in vec) ** 0.5
    return [0.3 * x/mag for x in vec]

def step(x_all, y_all, index):
    xprev = x_all[index-1]
    yprev = y_all[index-1]
    x = x_all[index]
    y = y_all[index]
    delete = []
    for i in range(0, num_particles):
        dx, dy = rand_vector()
        x[i] += xprev[i] + dx
        y[i] += yprev[i] + dy
        if x[i] < xmin:
            x[i] = xmax 
        if x[i] > xmax:
            if y[i] < y_hole1 or y[i] > y_hole2:
                x[i] = xmin 
            if y_hole1 < y[i] < y_hole2:
                delete.append(i)
        if y[i] < ymin:
            y[i] = ymax 
        if y[i] > ymax:
            y[i] = ymin 
    return(delete, x, y)
    
xplot, yplot = [], []
for i in range(1, num_steps):
    delete, x, y = step(x_all, y_all, i)
    for col in delete:
        x_all = np.delete(x_all, col, 1)
        y_all = np.delete(y_all, col, 1)
        num_particles -= 1
    xplot.append(x)
    yplot.append(y)
    
   
plt.style.use('default')
fig, (ax, ax2) = plt.subplots(1,2)
ax.set_xlabel('X Displacement (m)')
ax.set_ylabel('Y Displacement (m)')
ax.set_title('2D Diffusion - Hole in Container')
ax.set_xlim([0, 10])
ax.set_ylim([0, 10])
sca = ax.scatter([], [])
ax.set_aspect('equal')
num_frames = num_steps -1
t, num = [], []
line, = ax2.plot(t, num)
ax2.set_xlabel('Time Step')
ax2.set_ylabel('Number of Particles')
ax2.set_title('Number of Particles vs. Time')

def animation(frame):
    ax.collections[0].remove()
    ax.scatter(xplot[frame], yplot[frame], color='r')
    t.append(frame)
    num.append(len(xplot[frame]))
    ax2.lines[0].remove()
    line, = ax2.plot(t, num, color='b')
    
anim = animate(fig, animation, frames=num_frames, interval=50, repeat=False)

        
        