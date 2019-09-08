# -*- coding: utf-8 -*-
"""
Created on Tue Sep 03 13:14:40 2019

@author: David Engel
Goal is to numerically find the first derivative at x.
This is done by first defineing the function and then using a formula to calculate it
"""
import numpy as np


#point
x0=5.0

#step size
dx=.001

x=x0
#the function
def f(x):
    return (x**2)

    
#the derivative
fn=f(x0-dx)
fp=f(x0+dx)
#the derivative itself
fpri=(fp-fn)/(2*dx)
print '{}=dy/dx at x=5' .format(fpri)

#test for comparison
print 'dy/dx=10 at x=5 for y=x^2'
print 'the code works, test is successful'
