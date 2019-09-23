# -*- coding: utf-8 -*-
"""
Created on Mon Sep 16 21:55:37 2019

PHYS 639 >>> Assignments >>> Week 4 >>> ODE I
HUYNH LAM

"""

#%%============================================================================================================================
#==============================================================================================================================
#========      Week 4 >> Simple Oscillator                                                               ======================
#========      This code numerically solve a simple oscillator with damping force and driving force.     ======================
#==============================================================================================================================
#==============================================================================================================================

# Import libraries
import numpy as np #math library
import matplotlib.pyplot as plt # Plotting library

#==============================================================================================================================
# Function to solve first order ODE 
# It takes in the intial conditions (x0,f0), dfdx0 (the initial value of first order derivative)
# the upper limit of the range you want to solve your ODE (high),
# number of steps (Nsteps) and function that defines the second derivative of the original function (ddfdxx)
# It gives out the numerically estimated function f(x) that satisfies the conditions

def solve_second_order_ode(x0, f0, dfdx0, high, Nsteps, ddfdxx):
    # Initialize array with discrete values of x
    x = np.linspace(x0,high,Nsteps+1)
    # Initialize array to store the solution of f(x)
    fx = np.zeros(len(x))
    # step size
    dx = (high - x0)/Nsteps
    # First value of (x=x0,fx=f0,dfdx=dfdx0) is the initial condition
    dfdx = dfdx0
    fx[0] = f0
    x[0] = x0
    # Euler's method to estimate the solution f(x)
    # First calculate the second derivative then the first derivative
    # and then use this value of the first derivative and value of function at the previous point to estimate the next point
    for i in range(Nsteps):
        dfdx = dfdx + ddfdxx(x[i], fx[i], dfdx)*dx
        fx[i+1] = fx[i] + dfdx*dx
    return x, fx  
#==============================================================================================================================
# Constants
# Gravitational acceleration    
g = 9.8
# Initial amplitude
A = 1*np.pi/180
# Length of the simple oscillator
L = 1
# Initial velocity
v0 = -1
# Angular frequency (in case of simple harmonic oscillator without external force)
w = np.sqrt(g/L)
# Grag coefficient
q = 1
# Amplitude of driving force
Ft0 = 0
# Angular frequency of driving force
Omegat = w

# Derivative (ddtheta/dtt) as a function of t and theta
def derivative(t, theta, dthetadt):
    return -g/L*np.sin(theta) - q*dthetadt + Ft0*np.sin(Omegat*t+np.pi/2)

x,fx = solve_second_order_ode(0,A,v0,15,100000,derivative)
plt.plot(x,v0/w*np.sin(w*x)+A*np.cos(w*x),'k', label = 'analytical, small angle, no external force')
plt.plot(x,fx, linestyle='dashed',color = 'r', label = 'numerical, with damping force')
Ft0 = 1
x1,fx1 = solve_second_order_ode(0,A,v0,15,100000,derivative)
plt.plot(x1,fx1, linestyle='dotted',color = 'g', label = 'numerical, with damping and driving forces')
plt.legend()