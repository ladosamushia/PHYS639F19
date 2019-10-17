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
#Random walk in 1D
#(T1-T3) A particle starts at the origin and randomly moves either left or right with equal probability at each step. Write a code that simulates this process.
#Plot position vs time and displacement vs time. Experiment with different probabilities (e.g. p_left > p_right).

#Function to make random walk in 1D
def rwin1D(x0,Nstep):
    # Initialize array to save solutions
    t = np.linspace(0,Nstep,Nstep+1)
    x = np.zeros(len(t))
    #Initial consition
    x[0]=x0
    for i in range(Nstep):
        #Choose to move left or right
        step = np.random.choice([-1,1])
        # Add step to current position
        x[i+1]=x[i]+step
    return x

# Input parameters
# Initial position
x0 = 0
# Number of trials
N_trials = 100
# Number of steps per trial
N_steps = 1000
# Array to save data
x_array = np.zeros((N_trials,N_steps+1))
# Array to save average distance vs. time over all trials
x_average = np.zeros(N_steps+1)

# Run random walk for all trials
for i in range(N_trials):
    x_array[i,:] = rwin1D(x0,N_steps)

# Average over all trials
for j in range(N_steps+1):
    x_average[j] = np.mean(np.abs(x_array[:,j]))

# Plot
plt.plot(x_array[0,:],label = 'a sample of position vs. time')
plt.plot(x_average,label='average distance vs. time')    
plt.legend()
plt.show()