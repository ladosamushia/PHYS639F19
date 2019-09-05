# -*- coding: utf-8 -*-
"""
Created on Thu Aug 29 14:12:32 2019
Nathan Marshall

This algorithm finds the global minimum in a discrete function. It does this
by indexing through the list of the values of the function and saving the
minumum number that it finds. It is shown here finding the global minimum 
of x**2-5*x+6. 
"""
#%%
import numpy as np
num = 1000 #number of x points to be generated
xmin = -5 #minimum x value
xmax = 5 #maximum x value
x = np.linspace(xmin, xmax, num) #array of x values with above properties
fx = x**2-5*x+6 #values of the chosen function f(x) at each x value

minimum = fx[0] #initial minimum value set to the first value of f(x)
min_idx = 0 #initial minimum index value set to 0
ctr = 0 #counter variable that increments each time through a loop
for fxi in fx: #index through each value of fx
    if fxi < minimum: #if the current value is the smallest yet, save it
        minimum = fxi #setting new minimum
        min_idx = ctr #setting new minimum index to the counter number
    ctr +=1 #increment the counter
#display the minimum f(x) value that was found
print('The true minimum of x**2-5*x+6 is -1/4 at x = 5/2')
print('\nThe algorithm found the minimum to be', minimum, 'at x =', x[min_idx])
