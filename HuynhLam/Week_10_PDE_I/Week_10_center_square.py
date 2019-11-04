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
#Two parallel plates inside the boundary (not touching the boundary) that have some constant potential on them (LaTeX: \phi_+ϕ +, LaTeX: \phi_-ϕ −).
#Compute the potential everywhere inside the boundary and plot your result.
#%%
# Import libraries
import numpy as np #math library
import matplotlib.pyplot as plt # Plotting library

#%%
def box(x_dim,y_dim,x2_dim,y2_dim,phi_0,phi_i,Niterations):
    # Array to save the time evolution of the solutions
    evolve = np.zeros((x_dim, y_dim,Niterations))
    # Set the values at the boundary
    evolve[0,:,0] = phi_0
    evolve[x_dim-1,:,0] = phi_0
    evolve[:,0,0] = phi_0
    evolve[:,y_dim-1,0] = phi_0
    # Set values of the inside box to be 2
    for i in range(x2_dim):
        for j in range(y2_dim):
            x_index = int(x_dim/2-x2_dim/2+i)
            y_index = int(y_dim/2-y2_dim/2+j)
            evolve[x_index,y_index,0] = phi_i
    # Go to each point in the region defined by the boundary and change the its value to be the average value of its neighbors
    for t in range(1,Niterations):
        print(t/Niterations*100,'%')
        for i in range(1,x_dim-1):
            for j in range(1,y_dim-1):
                #Checking indexes
                if i < int(x_dim/2-x2_dim/2) or i > int(x_dim/2+x2_dim/2-1) or j < int(y_dim/2-y2_dim/2) or j > int(y_dim/2+y2_dim/2-1):
                    for m in range(3):
                        for n in range(3):
                            if m != 1 or n!=1:
                                evolve[i,j,t] = evolve[i,j,t] + evolve[i+m-1,j+n-1,t-1]
                    evolve[i,j,t] = evolve[i,j,t]/8
                else:
                    evolve[i,j,t] = evolve[i,j,t-1]
                #print(i,j,evolve[i,j,t])
#    error = np.zeros(Niterations)                
#    for t in range(1,Niterations):
#        error[t] = sum(sum(evolve[:,:,t]-evolve[:,:,t-1])
    return evolve

# Input parameters
x_dim = 50
y_dim = 50
x2_dim = 5
y2_dim = 5
Niterations = 250
phi_0 = 1
phi_i = 2
# Calculation
evolve = box(x_dim,y_dim,x2_dim,y2_dim,phi_0,phi_i,Niterations)
#Plot
plt.imshow(evolve[:,:,Niterations-1])
#  
