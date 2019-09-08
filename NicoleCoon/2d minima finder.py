# -*- coding: utf-8 -*-
"""
Created on Tue Sep  3 13:38:15 2019

@author: alecc
"""
import numpy as np
#define rectange to find in
xlower = -1
xupper = 1
ylower = -1
yupper = 2
#define start point
x = (xlower+xupper)/2
y = (ylower+yupper)/2
#function to test
def f(x,y):
    return((np.exp(x**2+y**2)))
def grad(x,y): #this is a basic differetnator
    step = .00001
    fprimex = (f(x+step,y)-f(x-step,y))/(2*step) #derivi in x
    fprimey = (f(x,y+step)-f(x,y-step))/(2*step) #deriv in y
    gradient = np.array([fprimex,fprimey]) #create vector of gradient
    return(gradient)
def dubgrad(x,y):
    step = .00001
    fdubx = (f(x+step,y)+f(x-step,y)-2*f(x,y))/step**2 #second in x
    fduby = (f(x,y+step)+f(x,y-step)-2*f(x,y))/step**2#second in y
    dubg = np.array([fdubx,fduby]) #create vector of second
    return(dubg)
i=0
"""
This while loop just increments the step
"""
while i <=100000:
    i=i+1
    grada = grad(x,y)#save comp power by storing gradient
    if grada[0] == 0 and grada[1] == 0: #just in case hits [0,0]
        break    
    stepsize = .0001*np.linalg.norm(dubgrad(x,y))/np.linalg.norm(grada)
    #Stepsize uses f'' over f' as step size
    if xlower <= x <= xupper: #walk in that direction
        x = x+stepsize*(-1*grada[0])
    if ylower <= y <= yupper: 
        y = y+ stepsize*(-1*grada[1])

print(f(x,y))
print(x,y)
