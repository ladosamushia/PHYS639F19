# -*- coding: utf-8 -*-
"""
Created on Tue Sep  3 13:24:49 2019

PHYS 639 >>> Assignments >>> Week 3 >>> Warmup III
HUYNH LAM

"""
#%% ######################################################################################### 
############ Week 3 >> Warmup III >> First order ODEs.       ################################
############ Write a code that will solve a first order ODE  ################################
############ with an arbitrary initial condition.            ################################
#############################################################################################

# Import libraries
import numpy as np
import matplotlib.pyplot as plt 

# First derivative of the function
def dfdx(x):
     # return np.exp(0.25*x**2)*(np.sin(2*x))**2+x**2;
     return x**3
     # return x

# Number of steps for estimating the function
num = 1000

# Initial condition
x0 = -5*np.pi
f0 = (5*np.pi)**4/4

# Up to what range in which you want to estimate the function
high =5* np.pi

# Constant interval arrays
x = np.linspace(x0, high, num)

# Step size
step = (high-x0)/num

# Derivative
derivative = dfdx(x)

# Initialize arrays to store value of the estimated function
estimated_function = np.zeros(num)
estimated_function[0] = f0


# Run through the loops and estimate the function using Euler method
# Basically just take the previous value and add the change estimated by derivation (gradient)
for i in range(0,num-1):
    estimated_function[i+1] = estimated_function[i]+derivative[i]*step

# Make plot to compare the result from Fourier series with the initial function
plt.plot(x, estimated_function, color='green', linewidth = 3, label = 'Estimated function')
plt.plot(x, x**4/4, color='red', linestyle='dashed', linewidth = 2, label = 'True function')
plt.legend()
plt.show()

##### Some test cases
# I have tested the code for few cases like x, x^2, etc. and some combinations with sine and cosine functions as well
# It performed well

##### Cautions
# The step size might not be good enough to sample the given function
# And this will makes the estimated function worse and worse as it moves far from the initial conditions
# Once need to be careful and check the convergence of their calculation