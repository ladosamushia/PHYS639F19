# -*- coding: utf-8 -*-
"""
Created on Sun Oct 13 17:52:15 2019

PHYS 639 >>> Assignments >>> Week 6 >>> ODE III
HUYNH LAM

"""
#%%
#(T1-T3) A particle starts at the origin and randomly moves either left or right with equal probability at each step. Write a code that simulates this process.
#Plot position vs time and displacement vs time. Experiment with different probabilities (e.g. p_left > p_right).
#(T1-T3) Do the same thing but now in 2D (particle can move either up, down, left, or right).
#(T3) Do the same thing in 3D.
#(T3) Plot average displacement vs time by averaging over many independent instances of this process.
#(T3) In 3D, instead of moving on a lattice make your particle move in a random direction with unit step.

# Import libraries
import numpy as np #math library
import matplotlib.pyplot as plt # Plotting library
from matplotlib.animation import FuncAnimation as animate
from mpl_toolkits.mplot3d import Axes3D
#%%
#(T1-T3) This code simulates the random walk process in 3D.
# A particle starts at the origin and randomly moves a random direction with equal probability (on a unitary sphere) at each step.
# In this code, I use the animation function from Nathan's code.

def rw_in_3D(x0,y0,z0,Nstep):
    t = np.linspace(0,Nstep,Nstep)
    x = np.zeros(len(t))
    y = np.zeros(len(t))
    z = np.zeros(len(t))
    x[0]=x0
    y[0]=y0
    z[0]=z0
    for i in range(1,Nstep):
        r = np.random.random_sample()
        theta = np.pi*np.random.random_sample()
        phi = 2*np.pi*np.random.random_sample()
        x[i] = x[i-1]+r*np.sin(theta)*np.cos(phi)
        y[i] = y[i-1]+r*np.sin(theta)*np.sin(phi)
        z[i] = z[i-1]+r*np.cos(theta)
    return x,y,z

x, y, z = rw_in_3D(0,0,0,10000)

fig1 = plt.figure()
ax = fig1.add_subplot(111, projection='3d')
line, = ax.plot([], [], [])
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
ax.set_title('A sample animation: 3D Random Walk')
ax.set_xlim3d(-20, 20)
ax.set_ylim3d(-20, 20)
ax.set_zlim3d(-20, 20)

Nstep = 1000
frame_rate = 1/24 * 1000
num_frames = Nstep
fstep = round(Nstep/num_frames)

def animation(frame):
    line.set_xdata(x[0:frame*fstep])
    line.set_ydata(y[0:frame*fstep])
    line.set_3d_properties(z[0:frame*fstep])
    return(line,)
    
anim = animate(fig1, animation, frames=num_frames, interval=frame_rate)

N_trials = 100
d_average = np.zeros(Nstep)
for i in range(N_trials):
    x,y,z = rw_in_3D(0,0,0,10000)
    for j in range(Nstep):
        d_average[j] += np.sqrt(x[j]**2+y[j]**2+z[j]**2)
d_average = d_average/N_trials
t = np.linspace(0,Nstep,Nstep)
fig = plt.figure('Average distance')
fig.suptitle('Average distance')
plt.xlabel('step')
plt.ylabel('average distance')
plt.plot(t,d_average)