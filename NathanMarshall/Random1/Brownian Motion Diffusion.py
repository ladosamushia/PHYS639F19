# -*- coding: utf-8 -*-
"""
Created on Thu Oct 10 13:17:41 2019
Nathan Marshall

Random walk in 2D, multiple particles
"""
#%%
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation as animate
from random import gauss

num_particles = 100
num_steps = 1000
x_all = []
y_all = []
x_bounds = [-10, 10]
y_bounds = [-10, 10]

def rand_vector():
    vec = [gauss(0, 1) for i in range(2)]
    mag = sum(x**2 for x in vec) ** 0.5
    return [x/mag for x in vec]

def random_walk(num_steps):
    dx = 1
    dy = 1
    x0 = 0
    y0 = 0
    x = [x0]
    y = [y0]
    xmin, xmax = x_bounds
    ymin, ymax = y_bounds
    
    for i in range(0, num_steps):
        if x[-1] < xmin or x[-1] > xmax:
            x[-1] = -x[-1]
        if y[-1] < ymin or y[-1] > ymax:
            y[-1] = -y[-1]
        dx, dy = rand_vector()
        x.append(x[-1] + dx*0.5)
        y.append(y[-1] + dy*0.5)
        
    return(x, y)
    
for i in range(0, num_particles):
    x, y = random_walk(num_steps)
    x_all.append(x)
    y_all.append(y)


plt.style.use('default')
fig, ax = plt.subplots(1,1)
ax.set_xlabel('X Displacement (m)')
ax.set_ylabel('Y Displacement (m)')
ax.set_title('2D Brownian Motion Diffusion')
ax.set_xlim([-11,11])
ax.set_ylim([-11,11])
sca = ax.scatter(np.zeros(num_particles), np.zeros(num_particles))
ax.set_aspect('equal')
num_frames = num_steps

def animation(frame):
    ax.collections[0].remove()
    idx = 0
    thisx = []
    thisy = []
    for i in range(0, num_particles):
        thisx.append(x_all[i][frame])
        thisy.append(y_all[i][frame])
        idx += 1
    ax.scatter(thisx, thisy, color='r')
    
    
    
anim = animate(fig, animation, frames=num_frames, interval=50)

