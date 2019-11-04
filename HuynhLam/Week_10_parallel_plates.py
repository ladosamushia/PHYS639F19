# -*- coding: utf-8 -*-
"""
Created on Tue Oct 29 13:40:29 2019

@author: huynhlam
"""
#%%
# Solve Laplace equation (△ ϕ = 0) in 2D.
# Assume that the boundary is square with some constant boundary condition on it (ϕ = ϕ_0).
# Consider following setups:
# A smaller square inside the boundary that has a constant potential on its surface (ϕ = ϕ_i).
# Two parallel plates inside the boundary (not touching the boundary) that have some constant potential on them (ϕ_+, ϕ_−).
# Compute the potential everywhere inside the boundary and plot your result.
#%%
# Import libraries
import numpy as np #math library
import matplotlib.pyplot as plt # Plotting library

#%%
def box(x_dim,y_dim,plate1_x,plate2_x,phi_p,phi_m,Niterations):
    # Array to save the time evolution of the solutions
    evolve = np.zeros((x_dim, y_dim,Niterations))
    # Set the values at the boundary
    evolve[0,:,0] = 0
    evolve[x_dim-1,:,0] = 0
    evolve[:,0,0] = 0
    evolve[:,y_dim-1,0] = 0
    # Set potentials of the plates
    for i in range(int(y_dim/4)):
        evolve[plate1_x,int(y_dim/2)-int(y_dim/8)+i,0] = phi_p
        evolve[plate2_x,int(y_dim/2)-int(y_dim/8)+i,0] = phi_m
    # Go to each point in the region defined by the boundary and change the its value to be the average value of its neighbors
    for t in range(1,Niterations):
        print(t/Niterations*100,'%')
        for i in range(1,x_dim-1):
            for j in range(1,y_dim-1):
                #Checking indexes
                if (i == plate1_x or i == plate2_x) and j > int(y_dim/2)-int(y_dim/8)-1 and j < int(y_dim/2)-int(y_dim/8)+int(y_dim/4):
#                    print(i,j)
                    evolve[i,j,t] = evolve[i,j,t-1]
                else:
                    for m in range(3):
                        for n in range(3):
                            if m != 1 or n!=1:
                                evolve[i,j,t] = evolve[i,j,t] + evolve[i+m-1,j+n-1,t-1]
#                                if i==5:
#                                    print(i,j,m,n,evolve[i,j,t])
                    evolve[i,j,t] = evolve[i,j,t]/8
#                if (i!= plate1_x and i != plate2_x) or j < int(y_dim/2)-int(y_dim/8) or j > int(y_dim/2)-int(y_dim/8)+int(y_dim/4):
#                    for m in range(3):
#                        for n in range(3):
#                            if m != 1 or n!=1:
#                                evolve[i,j,t] = evolve[i,j,t] + evolve[i+m-1,j+n-1,t-1]
#                    evolve[i,j,t] = evolve[i,j,t]/8
#                else:
#                    evolve[i,j,t] = evolve[i,j,t-1]
#    error = np.zeros(Niterations)                
#    for t in range(1,Niterations):
#        error[t] = sum(sum(evolve[:,:,t]-evolve[:,:,t-1])
    return evolve

# Input parameters
x_dim = 50
y_dim = 50
plate1_x = 20
plate2_x = 30
phi_p = 1
phi_m = -1
Niterations = 250
# Calculation
evolve = box(x_dim, y_dim, plate1_x, plate2_x, phi_p, phi_m,Niterations)
#Plot
plt.imshow(evolve[:,:,Niterations-1])
#  