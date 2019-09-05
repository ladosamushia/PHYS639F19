# -*- coding: utf-8 -*-
"""
Created on Tue Sep  3 13:38:15 2019

@author: alecc
"""
import numpy as np
xlower = -1
xupper = 1
ylower = -1
yupper = 2
x = (xlower+xupper)/2
y = (ylower+yupper)/2
def f(x,y):
    return((np.exp(x**2+y**2)))
def grad(x,y): #this is a basic differetnator
    step = .00001
    fprimex = (f(x+step,y)-f(x-step,y))/(2*step)
    fprimey = (f(x,y+step)-f(x,y-step))/(2*step)
    gradient = np.array([fprimex,fprimey])
    return(gradient)
i=0
"""
This while loop just increments the step
"""
while i <=100000:
    i=i+1
    if grad(x,y)[0] != 0 or grad(x,y)[1] != 0: #just in case hits [0,0]
        stepsize = .0001/np.linalg.norm(grad(x,y))
        if xlower <= x <= xupper:
            x = x+stepsize*(-1*grad(x,y)[0])
        if ylower <= y <= yupper:
            y = y+ stepsize*(-1*grad(x,y)[1])
print(f(x,y))
print(x,y)
