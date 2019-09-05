# -*- coding: utf-8 -*-
"""
Created on Tue Sep  3 13:31:50 2019
Nathan Marshall

This code finds the extrema of a 2D function f(x, y). It accomplishes this
by first numerically computing the gradient and laplacian of f(x, y) at a
guess point
"""
#%%
import numpy as np

def fxy(x, y):
    '''Function of x and y to find minimum of.'''
    return(x**4-x**2+y**4-y**2)

def dfdx(x, dx, y, fxy):
    '''Computes the approximate partial derivative in x of f(x, y) at (x, y)'''
    return((fxy(x+dx, y)-fxy(x-dx, y))/(2*dx))
    #evaluating the difference quotient of f(x, y) at the given point using
    #the step size dx gives us an approximation of the derivative
    
def dfdy(x, y, dy, fxy):
    '''Computes the approximate partial derivative in y of f(x, y) at (x, y)'''
    return((fxy(x, y+dy)-fxy(x, y-dy))/(2*dy))
    #evaluating the difference quotient of f(x, y) at the given point using
    #the step size dy gives us an approximation of the derivative
    
def d2fdx(x, dx, y, fxy, dfdx):
    '''Computes the approx. 2nd partial derivative in x of f(x, y) at (x, y)'''
    return((dfdx(x+dx, dx, y, fxy)-dfdx(x-dx, dx, y, fxy))/(2*dx))

def d2fdy(x, y, dy, fxy, dfdy):
    '''Computes the approx. 2nd partial derivative in y of f(x, y) at (x, y)'''
    return((dfdy(x, y+dy, dy, fxy)-dfdy(x, y-dy, dy, fxy))/(2*dy))

def grad(x, y, fxy, step):
    '''Compute the gradient of f(x,y) at the point (x,y)'''
    gradx = dfdx(x, step, y, fxy) 
    grady = dfdy(x, y, step, fxy)
    return(np.asarray([gradx, grady]))

def laplace(x, y, fxy, step):
    '''Computes numerical laplacian of f(x,y) at the point (x,y)'''
    lapx = d2fdx(x, step, y, fxy, dfdx)
    lapy = d2fdy(x, y, step, fxy, dfdy)
    return(np.asarray([lapx, lapy]))

def guess_step(r, fxy, step):
    '''
    Takes a step with position vector r in the direction that will minimize
    the gradient of f(x,y). Repeating this many times will eventually find
    a position vector that minimizes the gradient and hence is a critical
    point of f(x,y).
    '''
    dr = -grad(r[0], r[1], fxy, step)/laplace(r[0], r[1], fxy, step)
    return(r + dr)


#%%
step = 1e-8
prec = 1e-8
r = [0.8, 0.8]
while np.linalg.norm(grad(r[0], r[1], fxy, step)) > prec:
    r = guess_step(r, fxy, step)
print(r)

    
    
