# -*- coding: utf-8 -*-
"""
Created on Tue Sep  3 13:06:11 2019
Nathan Marshall

This program contains functions that compute the numerical 1st and 2nd 
derivatives of a function f(x). As an example, f(x) is set to x**3 to test
if the derivative functions are working properly.
"""
#%%
dx = 0.0001 #the step size in x used to compute derivatives
x = 1 #the value of x to compute the derivatives of f(x) at

def fx(x):
    '''Defining the function f(x) to compute derivatives of.'''
    return(x**3) #I chose the function x**3

def dfdx(x, dx, fx):
    '''Computes the approximate derivative of f(x) at a given x value'''
    return((fx(x+dx)-fx(x-dx))/(dx*2))
    #evaluating the difference quotient of f(x) at the given x value using
    #the step size dx gives us an approximation of the derivative

def d2fdx(x, dx, fx, dfdx):
    return((dfdx(x+dx, dx, fx)-dfdx(x-dx, dx, fx))/(dx*2))
    #evaluating the difference quotient of df/dx(x) at the given x value using
    #the step size dx gives us an approximation of the 2nd derivative
    
print('The actual derivative of x**3 at x = 1 is 3')
print('The numerical derivative of x**3 at x = 1 is', dfdx(x,dx,fx))

print('The actual 2nd derivative of x**3 at x = 1 is 6')
print('The numerical 2nd derivative of x**3 at x = 1 is', d2fdx(x,dx,fx, dfdx))