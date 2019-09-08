# -*- coding: utf-8 -*-
"""
Created on Tue Sep  3 13:31:50 2019
Nathan Marshall

This code finds the nearest critical point of a 2D function f(x, y). It 
accomplishes this by first numerically computing the gradient and 2nd 
derivative gradient of f(x, y) at a guess position vector. By subtracting 
the gradient divided by the 2nd derivative gradient from the guess position 
vector, a step towards minimizing the gradient and consequently finding a 
critical point is accomplished. This process is repeated until the the 
magnitude of the gradient is close enough to zero within a user-defined 
precision.
"""
#%%
import numpy as np

def fxy(x, y):
    '''Function of x and y to find critical point of.'''
    return(2*x**4 - x**2 + 2*y**4 - y**2)

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

def grad2(x, y, fxy, step):
    '''Computes 2nd derivative gradient of f(x,y) at the point (x,y)'''
    grad2x = d2fdx(x, step, y, fxy, dfdx)
    grad2y = d2fdy(x, y, step, fxy, dfdy)
    return(np.asarray([grad2x, grad2y]))

def guess_step(r, fxy, step):
    '''
    Takes a step with position vector r in the direction that will minimize
    the gradient of f(x,y). Repeating this many times will eventually find
    a position vector that minimizes the gradient and hence is a critical
    point of f(x,y).
    '''
    dr = -grad(r[0], r[1], fxy, step)/grad2(r[0], r[1], fxy, step)
    return(r + dr) #return improved guess


#%%
step = 1e-8 #small step size used for computing derivatives
prec = 1e-8 #magnitude of the gradient must be less than this value
r = [0.8, 0.8] #guess position vector
while np.linalg.norm(grad(r[0], r[1], fxy, step)) > prec:
    r = guess_step(r, fxy, step) #repeat stepping process until the magnitude
                                 #of the gradient is less than the precision

print('One minimum of the function 2*x**4 - x**2 + 2*y**4 - y**2 occurs at '
      '[0.5, 0.5]. With the guess [0.8, 0.8] the program found the nearest '
      'critical point to occur at', r)
    
    
