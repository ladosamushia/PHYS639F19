# -*- coding: utf-8 -*-
"""
Created on Wed Dec  4 20:00:21 2019
Nathan Marshall

Gas particles in a box with collisions between walls and other particles
"""
#%%
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation as animate

num = 50 #number of particles
num_steps = 100 #number of steps for animation
x = np.random.rand(num) #array for particle x values
y = np.random.rand(num) #array for particle y values
vx = np.random.rand(num) #array for particle x velocity values
vy = np.random.rand(num) #array for particle y velocity values
dt = 0.01 #time step size

fig, ax = plt.subplots(1, 1) #figure and axes plot objects
sca = ax.scatter(x, y, color='b') #initialize scatter plot object
ax.set_xlim(0, 1)
ax.set_ylim(0, 1)
ax.set_aspect('equal')

def animation(frame, x, y):
    ax.collections[0].remove()
    x += vx * dt
    y += vy * dt
    passlist = []
    
    for i in range(num):
        if x[i] <= 0 or x[i] >= 1:
            vx[i] = -vx[i]
            passlist.append(i)
        if y[i] <= 0 or y[i] >= 1:
            vy[i] = -vy[i]
            passlist.append(i)
            
    for i in range(num):
        for j in range(num):
            if j == i:
                continue
            elif i in passlist:
                continue
            c1 = np.asarray([x[i], y[i]])
            c2 = np.asarray([x[j], y[j]])
            r = np.linalg.norm(c1-c2)
            if r < 0.02:
                passlist.append(j)
                v1 = np.asarray([vx[i], vy[i]])
                v2 = np.asarray([vx[j], vy[j]])
                v1 -= np.dot(v1-v2, c1-c2)/np.linalg.norm(c1-c2)**2 * (c1-c2)
                v2 -= np.dot(v2-v1, c2-c1)/np.linalg.norm(c2-c1)**2 * (c2-c1)
                vx[i], vy[i] = v1
                vx[j], vy[j] = v2
                while r < 0.01:
                    x[i] += vx[i] * dt
                    y[i] += vy[i] * dt
                    x[j] += vx[j] * dt
                    y[j] += vy[j] * dt
                    c1 = np.asarray([x[i], y[i]])
                    c2 = np.asarray([x[j], y[j]])
                    r = np.linalg.norm(c1-c2)
                continue
    ax.scatter(x, y, color='b')

frame_rate = int(1/20 * 1000)
anim = animate(fig, animation, frames=num_steps, repeat=True, fargs=[x, y],
               interval=frame_rate)
    