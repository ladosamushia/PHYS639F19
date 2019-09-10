# -*- coding: utf-8 -*-
"""
Created on Tue Sep  3 13:24:49 2019

PHYS 639 >>> Assignments >>> Warmup II
HUYNH LAM

"""
#%% ######################################################################################### 
####### Week 2 >> Problem 3 >> Compute Fourier series coefficients. #########################
####### Write a code that will compute coefficients of Fourier series #######################
####### for an arbitrary function f(t) defined in -pi<t<pi interval. ########################
#############################################################################################

# Import library
import numpy as np
import matplotlib.pyplot as plt

# Function to decompose into series expansion
def func(x):
     fx = np.exp(0.25*x**2)*(np.sin(5*x))**2+x**2;
     #fx = x**2;
     return fx

# Number of steps for calculating the integrals
num = 10000

# Constant interval arrays
x = np.linspace(-np.pi, np.pi, num)

# Step size
step = 2*np.pi/num

# Initialize arrays to store value of coefficients
# We will not look at it in very details here, though.
A = []
B = []

# Create an array to keep track of the expansion series so that we can compare with the initial function in the end
# Start with the first element of 0.5*a0 = 0.5*1/pi*integrate(fxdx) from -pi to pi
# Here, the integral is approximated by the sum
expansion = 0.5*sum(func(x))*step/np.pi

# Run through the loops and calculating all the expansion coefficients
for n in range(1,100):
    a = sum(func(x)*np.sin(n*x))*step/np.pi
    b = sum(func(x)*np.cos(n*x))*step/np.pi
    A.append(a)
    B.append(b)
    expansion += a*np.sin(n*x) + b*np.cos(n*x)

# Make plot to compare the result from Fourier series with the initial function
plt.plot(x, func(x), color='green', linewidth = 3, label = 'Initial function')
plt.plot(x, expansion, color='red', linestyle='dashed', linewidth = 2, label = 'Fourier series expansion')
plt.legend()
plt.show()

##### Some test cases
# I have tested the code for few cases
# It is good for even order polynomials like x^2, x^4, x^6, etc.
# but is not good near the borders for odd order polynomials like x, x^3, etc.

##### Cautions
# The step size might not be good enough to sample the given function
# The number of coefficients may not be sufficient to describe the function
# Once need to be careful and check the convergence of their calculation