"""
Created on Sun Oct 20 17:52:15 2019

PHYS 639 >>> Assignments >>> Week 8 >>> Random Processes II
HUYNH LAM

"""
#%%
#(T2-T3) This code simulates diffusion of particles in a box ("Sugar cube in a coffee cup" problem).
# Start with 100 particles at the origin.
# The particles can randomly move in any direction in 2D.
# When particles reach the boundaries of the box they either stop
# or reenter from the opposite direction (periodic boundary conditions).
#(T2-T3) Compute entropy of the particle distribution as a function of time using: S=-p_i*ln[p_i]
#(T3) Make a hole in one of the walls. If particle exits trough a hole it does not reenter the box.
# Make a plot of particle number as a function of time and see how it changes with the size of the hole.

#%%
# Import libraries
import numpy as np #math library
import matplotlib.pyplot as plt # Plotting library

#%%
def teacup(x_bound,y_bound,Nstep,N_particles,y2_hole,y1_hole):
    
    # Initialize array to save solutions
    # First index is the number of particles
    # Second index is coordinates x and y
    # Third index is number of step
    solutions = np.zeros((N_particles, 2, Nstep))
    
    # Variable for tracking number of particles going through the hole
    # It will be used later to neglect all particles went out through the hole
    # when calculating entropy and number of particles over time
    boundary_tracking = np.zeros((Nstep,N_particles))
    
    # Loop through all steps and all particles
    for i in range(1,Nstep):
        for j in range(N_particles):
            
            # At each step, the particles can randomly move in any direction in 2D.
            r = np.random.random_sample()
            phi = 2*np.pi*np.random.random_sample()
            dx = r*np.cos(phi)
            dy = r*np.sin(phi)
            # Add step to current positions
            solutions[j,0,i] = solutions[j,0,i-1] + dx
            solutions[j,1,i] = solutions[j,1,i-1] + dy
                
            # Checking particles going into the hole on the left side of the wall (from y1_hole to y2_hole)
            if solutions[j,0,i] < -x_bound and solutions[j,1,i] > y1_hole and solutions[j,1,i] < y2_hole:
                boundary_tracking[i:,j] = boundary_tracking[i,j] + 1
                
            # Periodic boundary conditions
            if solutions[j,0,i] > x_bound:
                solutions[j,0,i] = solutions[j,0,i] - 2*x_bound
            if solutions[j,0,i] < -x_bound:
                solutions[j,0,i] = solutions[j,0,i] + 2*x_bound
            if solutions[j,1,i] > y_bound:
                solutions[j,1,i] = solutions[j,1,i] - 2*y_bound
            if solutions[j,1,i] < -y_bound:
                solutions[j,1,i] = solutions[j,1,i] + 2*y_bound
    
    # Snap shots of the tea cup surface over time (distribution of particles over time)
    xyt = np.zeros((2*x_bound+1, 2*y_bound+1, Nstep))
    # Initial conditions: Start with all particles at the origin.
    xyt[x_bound,y_bound,0] = N_particles    
    # Positions of particles is rounding off to put on a grid
    for i in range(1,Nstep):
        for j in range(N_particles):
            if boundary_tracking[i,j] == 0:
                xyt[int(solutions[j,0,i]+x_bound),int(solutions[j,1,i])+y_bound,i] = xyt[int(solutions[j,0,i]+x_bound),int(solutions[j,1,i])+y_bound,i] + 1                  
    return xyt

# Input parameters
# Number of steps
Nstep = 1000
# Number of particles
N_particles = 100
# Boundary
x_bound = 10
y_bound = 10
#Postitions of hole on the wall (left side)
y2_hole = y_bound/10
y1_hole = -y_bound/10

# Run the simulation
xyt = teacup(x_bound,y_bound,Nstep,N_particles,y2_hole,y1_hole)

# Calculating entropy and number of particles over time
# Entropy over time
entropy_t = np.zeros(Nstep)
# Number of particles over time
nptc_vs_time = np.zeros(Nstep)
# Probability of particle is on a cell of the grid
p = 1/((2*x_bound+1)*(2*y_bound+1))
# Snap shots of tea cup surface
xy = np.zeros((2*x_bound+1, 0))

for i in range(Nstep):
    # Snap shot of tea cup surface at one step
    xyt_slice = xyt[:,:,i]
    # Number of particles over time
    nptc_vs_time[i] = sum(sum(xyt_slice))
    for j in range(2*x_bound+1):
        for k in range(2*y_bound+1):
            # Entropy over time
            entropy_t[i] = entropy_t[i] - p**xyt_slice[j,k]*xyt_slice[j,k]*np.log(p)
    # Snap shots of tea cup surface
    xy = np.concatenate((xy, xyt_slice), axis=1)

#Plots
plt.figure('Entropy vs. time')
plt.plot(entropy_t)
plt.xlabel('step')
plt.ylabel('Entropy')
plt.figure('Number of particles vs. time')
plt.plot(nptc_vs_time)
plt.xlabel('step')
plt.ylabel('Number of particles')


