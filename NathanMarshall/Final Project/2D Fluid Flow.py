# -*- coding: utf-8 -*-
"""
Created on Thu Dec  5 13:08:09 2019
Nathan Marshall

"""
#%% Initialize variables and set boundary conditions
import numpy as np
import matplotlib.pyplot as plt

nx = 25 #number of grid positions in x
ny = 25 #number of grid positions in y

psi = np.zeros((nx, ny)) #matrix to hold stream velocity values
dw = np.zeros((nx, ny))
w =  np.zeros((nx, ny)) #matrix to hold vorticity values
dt = 0.02 #time step value
h = 1/(nx-1) #precision between points
R = 100 #Reynold's number for the fluid
beta = 1.5 #SOR factor
numiter = 100 #number of SOR iterations
numsteps = 60  #number of times to run CFD algorithm

#%% Determine new values for w and psi after a time step

def SOR(psi, w, numiter):
    '''Uses SOR to iteratively determine the stream function psi.'''
    for steps in range(numiter):
        for i in range(1, nx-1):
            for j in range(1, ny-1):
                psi[i][j] = (0.25 * beta * (psi[i+1][j] + psi[i-1][j] + psi[i][j+1] 
                            + psi[i][j-1] + h**2 * w[i][j]) + (1 - beta)*psi[i][j])
def vort_wall(psi, w):
    '''Determine the vorticity boundary values from the stream function psi.'''
    w[:,0] = -2 * psi[:,1]/h**2 #left side
    w[:,nx-1] = -2 * psi[:,nx-2]/h**2 #right side
    w[0] = -2 * psi[1]/h**2 - 2/h #top side
    w[ny-1] = -2 * psi[ny-2]/h**2 + 2/h #bottom side
    
def vort(psi, w, dw):
    '''Determines vorticity at the next time step.'''
    for i in range(1, nx-1):
        for j in range(1, ny-1):
            dw[i][j] = (-0.25*((psi[i][j+1] - psi[i][j-1])*(w[i+1][j] - w[i-1][j])
                        - (psi[i+1][j] - psi[i-1][j])*(w[i][j+1] - w[i][j-1]))/(h**2)
                        + (1/R * (w[i+1][j] + w[i-1][j] + w[i][j+1] + w[i][j-1] - 4*w[i][j])/h**2))
                        
#%% Run the algorithm for desired number of steps
for steps in range(numsteps):
    SOR(psi, w, numiter)
    vort_wall(psi, w)
    vort(psi, w, dw) 
    w[1:ny-1][:,1:ny-1] += dw[1:ny-1][:,1:ny-1] * dt   
    
#%% Extract velocities from stream function
u = np.zeros((nx, ny)) #x velocity
v = np.zeros((nx, ny)) #y velocity
x = np.arange(0, nx, 1)
y = np.arange(0, ny, 1)

for i in range(1, nx-1):
    for j in range(1, ny-1):
        u[i][j] = (psi[i+1][j] - psi[i-1][j])/(2*h)
        v[i][j] = -(psi[i][j+1] - psi[i][j-1])/(2*h)

fig1, ax = plt.subplots(1, 1)
ax.set_aspect('equal')
ax.streamplot(x, y, u, v)
im = ax.pcolormesh(x, y, np.sqrt(u**2+v**2))

#%% Plot Results
fig2, [ax1, ax2] = plt.subplots(1,2) 
im1 = ax1.imshow(w, cmap='inferno')
ax1.set_title('Vorticity')
im2 = ax2.imshow(psi, cmap='inferno')
ax2.set_title('Stream Function')
