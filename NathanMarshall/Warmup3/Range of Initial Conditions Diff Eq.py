# -*- coding: utf-8 -*-
"""
Created on Tue Sep 10 14:09:52 2019
Nathan Marshall

Solve the differential equation f' = (1+cos(x))/(1+2f) for a range of initial
conditions with x = 0 and f(x = 0) = -2 to 2. Plot solutions to x_max = 10.
"""
#%%
import numpy as np
import matplotlib.pyplot as plt

dx = 0.0001 #step size
x0 = 0 #initial condition for x
f0_range = np.linspace(-2, 2, 10) #initial conditions for the solution curve
xmax = 10 #max value of x

def diffeq(x0, f0, xmax, dx):
    '''Numerically approximates the given differential equation.'''
    fx = [f0] #list to contain function values
    x = [x0] #list to contain x values
    
    while x[-1] < xmax: #loop until our increment variable is greater than xmax
        dfdx = (1 + np.cos(x[-1]))/(1 + 2 * fx[-1]) #calculate df/dx
        fx.append(fx[-1] + dfdx*dx) #add df/dx * dx to previous f(x)
        x.append(x[-1] + dx) #add new x value to the list
    plt.plot(x, fx) #plot the resulting curve

for f0 in f0_range: #approximate curves for all initial conditions
    diffeq(x0, f0, xmax, dx) #run the differential equation with each I.C.
    
plt.title('Range of Solution Curves to ' 
          r'$\frac{df}{dx} = \frac{1 + cos(x)}{1 + 2f}$')
plt.ylabel('f(x)') 
plt.xlabel('x')
plt.grid(True) 


