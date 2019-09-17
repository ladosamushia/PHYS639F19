# -*- coding: utf-8 -*-
"""
Created on Tue Sep  3 13:24:49 2019

PHYS 639 >>> Assignments >>> Week 3 >>> Warmup III
HUYNH LAM

"""

#%%==================================================================================================
#=========== Week 3 >> Warmup III >> First order ODEs.                               ================
#=========== Write a code that solves a differential equation f'=(1+cos(x))/(1+2f)   ================
#=========== between x = 0 and 10 for a range of initial conditions f(0) = -2 to 2.  ================
#====================================================================================================

# Import libraries
import numpy as np #math library
import matplotlib.pyplot as plt # Plotting library

# Function to solve first order ODE 
# It takes in the intial conditions (x0,f0), the upper limit of the range you want to solve your ODE (high),
# number of steps (Nsteps) and function that defines the first derivative of the original function
# It gives out the numerically estimated function f(x) that satisfies the conditions

def solve_first_order_ode(x0, f0, high, Nsteps, dfdx):
    # Initialize array with discrete values of x
    x = np.linspace(x0,high,Nsteps+1)
    # Initialize array to store the solution of f(x)
    fx = np.zeros(len(x))
    # step size
    dx = (high - x0)/Nsteps
    # First value of (x,fx) is the initial condition
    fx[0] = f0
    x[0] = x0
    # Euler's method to estimate the solution f(x)
    # First calculate the derivative then use the derivative
    # and then use this value of derivative and value of function at the previous point to estimate the next point
    for i in range(Nsteps):
        derivative = dfdx(x[i], fx[i])
        fx[i+1] = fx[i] + derivative*dx
    return x, fx  

# Derivative as a function of x and fx
def derivative(x, fx):
    return (1 + np.cos(x))/(1 + 2*fx)

# solve dfdx = (1 + cos(x))/(1 + 2*x) for a range of Initial Conditions
# Number of initial consitions
NICs = 25
# Initial conditions
ICs = np.linspace(-2, 2, NICs)

for i in range(NICs):
    x,fx = solve_first_order_ode(-10,ICs[i],10,1000,derivative)
    plt.plot(x,fx,'k')