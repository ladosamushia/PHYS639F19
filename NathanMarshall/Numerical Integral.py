# -*- coding: utf-8 -*-
"""
Created on Thu Aug 29 13:12:05 2019
Nathan Marshall

This algorithm numerically evaluates the integral of a function f(x). Here it
is shown evaluating the integral from 0 to pi of sin(x)
"""
#%%
import numpy as np
num = 1000 #number of x points to be generated
xmin = 0 #minimum x value
xmax = np.pi #maximum x value
x = np.linspace(xmin, xmax, num) #array of x values with above properties
dx = (xmax-xmin)/(num-1) #the width (dx) between each x value
fx = np.sin(x) #values of the chosen function f(x) at each x value

integral = 0 #intially the integral is set to 0
for i in range(0, num-1): #loop through i values 0 to 999                       
    integral += (fx[i] + fx[i+1])/2*dx 
    #multiply average height of two adjacent f(x) points by dx to find the 
    #area and add this area to the total integral
print('The analytical value of this integral is 2, and the numerical value found'
      ' was:', integral)