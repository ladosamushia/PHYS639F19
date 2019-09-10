# -*- coding: utf-8 -*-
"""
Created on Tue Sep  3 13:24:49 2019

PHYS 639 >>> Assignments >>> Warmup II
HUYNH LAM

"""
#%% ######################################################################################################## 
# Week 2 >> Problem 1 >> Find the first and second derivatives of a function f = f(x). #####################
############################################################################################################

# import libraries
import numpy as np
# function that you want to take derivatives
def fx(x):
    func = np.sin(x)
    return func
# Point at which you want to take derivative
x0 = np.pi/2
# Step size
delta = 0.0001

# Calculate derivatives by finite differences
# First derivative
f_dev = (fx(x0+delta)-fx(x0-delta))/(2*delta)
print("The first derivative is",f_dev)
# Second derivative
s_dev = (fx(x0+2*delta)-2*fx(x0)+fx(x0-2*delta))/(4*delta*delta)
print("The second derivative is",s_dev)

##### Some test cases
# f(x) = 3x^2 at x = 2 >>> First derivative is 12.000000000016442 and second derivative is 6.000000007944095
# f(x) = sin(x) at x = pi/2 >>> First derivative is 0.0 and second derivative is -0.999999993922529

#### Cautions
# The accuracy of this approximation depends on how we sample the "true" function
# The closer it can be approximated by a straight line in the vicinity, the better the calculations
# The faster this "true" function varies, the smaller step size needs to be used
# Once need to be careful and check the convergence of their calculation
