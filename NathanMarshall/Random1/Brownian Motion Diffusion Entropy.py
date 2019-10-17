# -*- coding: utf-8 -*-
"""
Created on Tue Oct 15 13:21:35 2019
Nathan Marshall

Random walk in 2D with entropy calculation
"""
#%%
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation as animate
from random import gauss

num_particles = 500
num_steps = 600
x_all = []
y_all = []
x_bounds = [0, 20]
y_bounds = [0, 20]

def rand_vector():
    vec = [gauss(0, 1) for i in range(2)]
    mag = sum(x**2 for x in vec) ** 0.5
    return [x/mag for x in vec]

def random_walk(num_steps):
    dx = 1
    dy = 1
    x0 = 10
    y0 = 10
    x = [x0]
    y = [y0]
    xmin, xmax = x_bounds
    ymin, ymax = y_bounds
    
    for i in range(0, num_steps):
        if x[-1] < xmin:
            x[-1] = xmax 
        if x[-1] > xmax:
            x[-1] = xmin 
        if y[-1] < ymin:
            y[-1] = ymax 
        if y[-1] > ymax:
            y[-1] = ymin 
        dx, dy = rand_vector()
        x.append(x[-1] + dx*0.5)
        y.append(y[-1] + dy*0.5)
        
    return(x, y)

def entropy(x_all, y_all, index):
    num_cells = 21
    p = 1/num_cells
    entropy = 0
    num = np.zeros([num_cells, num_cells])
    for i in range(0, len(x_all)):
        x = x_all[i]
        y = y_all[i]
        thisx = x[index]
        thisy = y[index]
        cellx = int(thisx)
        celly = int(thisy)
        num[celly][cellx] = num[celly][cellx] + 1
    for i in range(num_cells):
        for j in range(num_cells):
            entropy += -p ** num[i][j] * np.log(p ** num[i][j])
    return(entropy)
        
                
                           
    
for i in range(0, num_particles):
    x, y = random_walk(num_steps)
    x_all.append(x)
    y_all.append(y)

s = []
t = np.arange(0, num_steps-1)

for i in range(1, num_steps):
    s.append(entropy(x_all, y_all, i))

plt.style.use('default')
fig, [ax, ax2] = plt.subplots(1,2)
ax.set_xlabel('X Displacement (m)')
ax.set_ylabel('Y Displacement (m)')
ax.set_title('2D Brownian Motion Diffusion')
ax.set_xlim([0, 20])
ax.set_ylim([0, 20])
sca = ax.scatter(np.zeros(num_particles), np.zeros(num_particles))
ax.set_aspect('equal')
ax2.plot([], [], color='b')
ax2.set_xlabel('Time (s)')
ax2.set_ylabel('Entropy')
ax2.set_title('Entropy vs. Time')
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
    ax2.lines[0].remove()
    ax2.plot(t[0:frame], s[0:frame], color='b')
    
    
    
anim = animate(fig, animation, frames=num_frames, interval=50)
