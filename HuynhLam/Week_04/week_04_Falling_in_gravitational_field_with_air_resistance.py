# -*- coding: utf-8 -*-
"""
Created on Mon Sep 16 21:55:37 2019

PHYS 639 >>> Assignments >>> Week 4 >>> ODE I
HUYNH LAM

"""
#%%============================================================================================================================
#==============================================================================================================================
#=========== Week 4 >> (T1-T3) Solve a differential equation describing what happens to a velocity of an object   =============
# that's  falling in a gravitational field near earth accounting for air resistance.                              =============
# Make plots demonstrating what happens when you change initial conditions and free parameters.                   =============
# Justify your numeric results (e.g. Do you get the right limits?                                                 =============
# Do the results change in the expected way when you change initial conditions and parameters?)                   =============
#==============================================================================================================================
#==============================================================================================================================

# Import libraries
import numpy as np #math library
import matplotlib.pyplot as plt # Plotting library

#==============================================================================================================================
# Function to solve first order ODE 
# It takes in the intial conditions (x0,f0), the upper limit of the range you want to solve your ODE (high),
# number of steps (Nsteps) and function that defines the first derivative of the original function
# It gives out the numerically estimated function f(x) that satisfies the conditions
#==============================================================================================================================

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
#==============================================================================================================================
# consider gravity to be a constant
g = 9.8
# drag coefficient
a = 2

# Acceleration as a function of velocity (v) and t (no need in this case)
def derivative(t, v):
    return - g - a*v

# Range of initial velocity
NICs = 5
ICs = np.linspace(-10, 10, NICs)

for i in range(NICs):
    x,fx = solve_first_order_ode(0,ICs[i],2,1000,derivative)
    plt.plot(x,fx, label = 'a = %.0f $v_0$ = %.0f' %(a,ICs[i]))
    
a = 0
for i in range(NICs):
    x,fx = solve_first_order_ode(0,ICs[i],2,1000,derivative)
    plt.plot(x,fx, label = 'a = %.0f $v_0$ = %.0f' %(a,ICs[i]))

plt.legend()
plt.show()