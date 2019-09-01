# -*- coding: utf-8 -*-
"""
Created on Thu Aug 29 13:33:36 2019
Nathan Marshall

This algorithm searches for the zeros of a discrete function f(x). First, the 
algorithm searches for places where the product of two adjacent points is
negative. This indicates a zero crossing, and then a simple interpolation is 
applied to more accurately approximate for what x f(x) is equal to zero. If no 
zero crossing is detected, the approximate derivative is calculated at each 
point in f(x). When a switch in the sign of the derivative is detected, this 
indicates an extrema of f(x). The extrema values of f(x) and their 
corresponding x values are printed out. This allows zeros of functions that 
just brush the x-axis to still be detected. Here it is shown finding the zeros
of sin(x) from -3*pi/2 to 3*pi/2.
"""
#%%
import numpy as np
num = 100000 #number of x points to be generated
xmin = -3*np.pi/2 #miniumum x value
xmax = 3*np.pi/2 #maximum x value
x = np.linspace(xmin, xmax, num) #array of x values with above properties
fx = np.sin(x) #values of the chosen function f(x) at each x value

zero_idx = [] #list of indices where a zero occurs
for i in range(0, num-1): #searching for where product of adjacent points < 0
    if fx[i] * fx[i+1] < 0 :
        zero_idx.append(i) #saving index i where the zero is detected
    
avg_zero = [] #stores values of x where f(x) = 0
for idx in zero_idx: 
    avg = (x[idx] + x[idx+1])/2 #interpolating x values around the zero
    avg_zero.append(avg)
    
if len(avg_zero) != 0: #display the detected zeros (if any were detected)
    print('The actual zeros of sin(x) occur at:\nx = -pi\nx = 0\nx = pi')
    print('\nThe algorithm found the zeros to occur at:')
    for zero in avg_zero:
        print('x =', zero)

else: #if no zero crossings were detected, instead find the extrema
    def dfdx(x, fx, idx):
        '''Computes the approximate derivative at a given index'''
        return((fx[idx+1]-fx[idx])/(x[idx+1]-x[idx])) 

    deriv = [] #compute the derivative at each point in f(x)
    for i in range(0, len(fx)-1):
        deriv.append(dfdx(x, fx, i))
    
    zero_idx = [] #stores index locations where the derivatve changes sign
    for i in range(0, len(deriv)-1): #find where the derivative changes sign
        if deriv[i] < 0 and deriv[i+1] > 0:
            zero_idx.append(i+1)
        elif deriv[i] > 0 and deriv[i+1] < 0:
            zero_idx.append(i+1)
        
    print('No zero crossing detected. The extrema of this function occur at:')
    for i in zero_idx: #display the detected extrema of the function
        print('x =', x[i], 'f(x) =', fx[i])
