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
#(T1-T3) This code simulates the random walk process in 2D.
# A particle starts at the origin and randomly moves either up, down, left, or right with equal probability at each step.
# In this code, I use the animation function from Nathan's code.
def rwin2D(x0,y0,Nstep,N_trials):
    # Initialize array to save solutions
    xyt = np.zeros((N_trials, 2, Nstep))
    # Initial consitions
    xyt[:,:,0] = 0
    for i in range(N_trials):
        for j in range(1,Nstep):
            # At each step, choose to move either left (1), right (2), down (3), up (4) with equal probability.
            step = np.random.choice([1,2,3,4])
            # Add step to current positions
            if step == 1:
                xyt[i,0,j] = xyt[i,0,j-1] - 1
                xyt[i,1,j] = xyt[i,1,j-1]
            elif step == 2:
                xyt[i,0,j] = xyt[i,0,j-1] + 1
                xyt[i,1,j] = xyt[i,1,j-1]
            elif step == 3:
                xyt[i,0,j] = xyt[i,0,j-1]
                xyt[i,1,j] = xyt[i,1,j-1] - 1
            else:
                xyt[i,0,j] = xyt[i,0,j-1]
                xyt[i,1,j] = xyt[i,1,j-1] + 1
    return xyt

# Input parameters
# Number of steps
Nstep = 1000
# Number of trials
N_trials = 100
# Initial positions
x0 =0
y0=0

xyt_array = rwin2D(x0,y0,Nstep,N_trials)

# Average over all trials
d_average = np.zeros(Nstep)
for i in range(N_trials):
    for j in range(0,Nstep):
        d_average[j] += np.sqrt((xyt_array[i,0,j])**2+(xyt_array[i,1,j])**2)
d_average = d_average/N_trials

avg_dist = plt.figure('Average distance')
avg_dist.suptitle('Average distance')
plt.xlabel('step')
plt.ylabel('average distance')
plt.plot(d_average, label = 'Average distance')

# Setting up variables for animation
xy1 = xyt_array[0,:,:]
x1 = xy1[0,:]
y1 = xy1[1,:]
xy2 = xyt_array[1,:,:]
x2 = xy2[0,:]
y2 = xy2[1,:]
xy3 = xyt_array[2,:,:]
x3 = xy3[0,:]
y3 = xy3[1,:]

# The animation part from Nathan's code.

#initialize animation figure
fig = plt.figure('Sample Trajectories')
ax = plt.subplot()
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_title('Animation: 2D Random Walk')
ax.set_xlim(-100, 100)
ax.set_ylim(-100, 100)
line1, = ax.plot([], [], color='b')
line2, = ax.plot([], [], color='g')
line3, = ax.plot([], [], color='r')
sca1 = ax.scatter([], [], color='b')
sca2 = ax.scatter([], [], color='g')
sca3 = ax.scatter([], [], color='r')

#set number of frames
num_frames = Nstep
step = round(Nstep/num_frames) #step size for the plotted lists

def animation(frame):
    '''Function run to draw each frame of the animation'''
    stop = frame * step #the index at which to stop plotting for current frame
    line1.set_data(x1[0:stop:step], y1[0:stop:step])
    line2.set_data(x2[0:stop:step], y2[0:stop:step])
    line3.set_data(x3[0:stop:step], y3[0:stop:step])
    sca1.set_offsets([x1[stop], y1[stop]])
    sca2.set_offsets([x2[stop], y2[stop]])
    sca3.set_offsets([x3[stop], y3[stop]])
    return(line1, line2, line3, sca1, sca2, sca3)
    
#call the FuncAnimation function
animate(fig, animation, frames=num_frames, interval=20)