# -*- coding: utf-8 -*-
"""
Created on Tue Sep 10 13:05:52 2019
Nathan Marshall

This program numerically solves a first order ordinary differential equation.
"""
#%%
import numpy as np
import matplotlib.pyplot as plt

def dfdx(x):
    '''Define functional form of the derivative df/dx.'''
    return(x)
    
dx = 0.0001 #step size
x0 = 0 #initial condition for x
f0 = 0 #initial condition for the solution curve f(x)
xmax = 7 #max value of x
x = [x0] #list to contain x values
fx = [f0] #list to contain function values


while x[-1] < xmax: #loop until our increment variable is greater than xmax
    fx.append(fx[-1] + dfdx(x[-1])*dx) #add df/dx * dx to previous f(x)
    x.append(x[-1] + dx) #add new x value to the list


t = np.linspace(x0, xmax, 1000) #test case variable
ft = t**2/2 #test case function

plt.plot(t, ft, label='Analytical Result') #plotting test case
plt.plot(x, fx, label='Numerical Result') #plotting numerical result
plt.grid(True)
plt.legend()