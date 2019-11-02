# -*- coding: utf-8 -*-
"""
Created on Tue Oct 29 13:10:53 2019
Nathan Marshall

Partial Differential Equations: Solving Laplace Equation Numerically
"""
#%%
import numpy as np
import matplotlib.pyplot as plt

row = 100 #number of rows
col = 100 #number of columns
num_steps = 1000 #number of averaging steps

V = np.zeros((row, col)) #matrix to hold potential values
bounds = np.zeros((row, col)) #matrix to hold positions of boundaries

#set initial conditions of the matrix
#these first four lines set all edges of matrix to 1
bounds[0] = 1
bounds[row-1] = 1
bounds[:,0] = 1
bounds[:,col-1] = 1
#now set a square 10x10 in the center to 2
for i in range(46, 56):
    V[i][46:56] = 2
    bounds[i][46:56] = 1

def average(V):
    '''Sets each point not on the boundary to the average of its neighbors.'''
    for i in range(0, row):
        for j in range(0, col):
            if bounds[i][j] == 1:
                pass
            else:
                avg = (V[i+1][j] + V[i-1][j] + V[i][j+1] + V[i][j-1])/4
                V[i][j] = avg
                
#run the averaging for the desired number of steps  
Vsum = [] #keeping track of sums of the matrix to test for convergence
for i in range(0, num_steps): 
    Vsum.append(np.sum(V))
    average(V)

#compute difference in neighboring sums to look for convergence
Vdelta = []
for i in range(0, num_steps-1):
    Vdelta.append(Vsum[i+1]-Vsum[i])
    
fig, [ax1, ax2] = plt.subplots(1,2)
ax1.imshow(V) #show the end result matrix
ax1.set_title('Laplace Equation Numeric Solution')
ax2.plot([x for x in range(0, num_steps-1)], Vdelta)
ax2.set_title('Difference in Sum of Adjacent Steps')
ax2.set_xlabel('Step number')
