# -*- coding: utf-8 -*-
"""
Created on Sun Dec 15 16:33:51 2019
Nathan Marshall

"""
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation as animate

num = 30 #number of particles
num_steps = 100 #number of steps for animation
r = np.random.rand(num, 2) #random initial position vector
v = np.random.normal(size=(num, 2)) #random gaussian initial velocity vector
dt = 0.005 #time step size

fig, [ax, ax2] = plt.subplots(1, 2) #figure and axes plot objects
sca = ax.scatter(r[:,0], r[:,1], color='b') #initialize scatter plot object
ax.set_xlim(0, 1)
ax.set_ylim(0, 1)
hist = ax2.hist(np.linalg.norm(v, axis=1))
ax.set_aspect('equal')

def animation(frame, r):
    ax.collections[0].remove()
    r += v * dt #increment each particle position
    coll = [] #array to hold the second index of collision
    xbound = np.where(((r[:,0] < 0) | (r[:,0] > 1))) #check for wall collision
    ybound = np.where(((r[:,1] < 0) | (r[:,1] > 1)))
    v[:,0][xbound] = -v[:,0][xbound] #elastic collisions with walls
    v[:,1][ybound] = -v[:,1][ybound]
    coll.append(xbound)
    coll.append(ybound)
    for i in range(num):
        for j in range(num):
            if i == j:
                continue
            if i in coll:
                continue
            sep = np.linalg.norm(r[i] - r[j])
            if sep < 0.01:
                print('hit')
                print(i, j)
                v[i] -= np.dot(v[i]-v[j], r[i]-r[j])/np.linalg.norm(r[i]-r[j])**2 * (r[i]-r[j])
                v[j] -= np.dot(v[j]-v[i], r[j]-r[i])/np.linalg.norm(r[j]-r[i])**2 * (r[j]-r[i])
                coll.append(j)
                while sep < 0.01:
                    r[i] += v[i] * 0.001
                    r[j] += v[j] * 0.001
                    sep = np.linalg.norm(r[i] - r[j])
    
    ax.scatter(r[:,0], r[:,1], color='b')

frame_rate = int(1/30 * 1000)
anim = animate(fig, animation, frames=num_steps, repeat=True, fargs=[r],
               interval=frame_rate)
