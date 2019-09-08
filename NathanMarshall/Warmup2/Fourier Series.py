# -*- coding: utf-8 -*-
"""
Created on Thu Sep  5 13:21:36 2019
Nathan Marshall

This code computes Fourier coefficients for an arbitrary function on the 
interval -pi to pi. As an example it is shown computing Fourier coefficients
for a step function that is 0 for t < 0 and 1 for t >= 0. The actual function
and Fourier approximation are displayed in a graph for comparison.
"""
#%%
import numpy as np
from matplotlib import pyplot as plt
num = 1000 #number of t points to be generated
num_terms = 100 #number of Fourier series terms to be computed
tmin = -np.pi #minimum t value
tmax = np.pi #maximum t value
t = np.linspace(tmin, tmax, num) #array of t values with above properties
dt = (tmax-tmin)/(num-1) #the width (dt) between each t value

def ft(t): 
    '''This function defines a step function.'''
    if t < 0: #if t < 0, return a 0
        return(int(0))
    if t >= 0: #if t >= 0, return a 1
        return(int(1))
    
def find_a(ft, dt, n):
    '''Computes A_n terms of the Fourier series.'''
    integral = 0 #intially the integral is set to 0
    for i in range(0, num): #loop through values of t                       
        integral += ft(t[i])*np.sin(n*t[i])*dt #add up each piece of integral
    return(integral*(1/np.pi)) #return the integral divided by pi
          
def find_b(ft, dt, n):
    '''Computes B_n terms of the Fourier series.'''
    integral = 0 #intially the integral is set to 0
    for i in range(0, num): #loop through values of t                       
        integral += ft(t[i])*np.cos(n*t[i])*dt
    return(integral*(1/np.pi))
    
an = [] #list for containing A_n coefficients
bn = [] #list for containing B_n coefficients

for i in range(0, num_terms): #finding coefficients up to the declared number
    an.append(find_a(ft, dt, i)) #add each coefficent to the proper list
    bn.append(find_b(ft, dt, i))

bn[0] = bn[0]/2 #satisfying the exception case for B_0

fourier = [] #list for containing the Fourier approximation of the function
for ti in t: #loop through every t value
    y = 0 #start with the value of the function at 0
    for n in range(0, num_terms): #add contribution from each Fourier term
        y += bn[n]*np.cos(n * ti) + an[n]*np.sin(n * ti)
    fourier.append(y) #add the Fourier approximation value to the list
    
ft_plot = [ft(ti) for ti in t] #create a list of actual function values to plot
plt.plot(t, fourier, label='Fourier Series') #plot the Fourier approximation
plt.plot(t, ft_plot, label='Step Function') #plot the actual function
plt.title('Fourier Approximation of a Step Function')
plt.xlabel('t') #x-axis label
plt.ylabel('f(t)') #y-axis label
plt.grid(True) #add grid to plot
plt.legend() #add legend to plot
plt.show() #make sure the plot is displayed

