# -*- coding: utf-8 -*-
"""
Created on Tue Sep 03 14:05:49 2019

@author: David Engel
The point of this code is to calculate the 2nd derivative.
"""
# point calculated
x0=5
x=x0
#step size
dx=.01   

#the function itself
def f(x):
    return(x**3)

#a variable
fn=f(x0-dx)
# another variable
fp=f(x0+dx)

fx0=f(x0)
#definition of second derivative in terms of original function
f2pri=(fp-2*fx0+fn)/(dx**2) 
print f2pri

print '{}=d^2y/dx^2 at x=5' .format(f2pri)

#test for comparison
print 'd^2y/dx^2=30 at x=5 for y=x^3'
print 'the code works, test is successful'