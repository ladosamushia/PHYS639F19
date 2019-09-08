# -*- coding: utf-8 -*-
"""
Created on Thu Sep  5 13:39:59 2019

@author: alecc
"""

import numpy as np

# this defines the function to be transformed
def f(x):
    return x
def inter(lower,upper,function):
    step = .0001 #this is the incremnt size
    i = lower # i is dummy variable
    height = 0 #height is the y value that is summed up 
    while i < upper-step:
        height = height + function(i)
        i = i + step
    return(step*height)
def intercos(function,n):
    step = .0001 #this is the incremnt size
    i = -np.pi # i is dummy variable
    height = 0 #height is the y value that is summed up 
    while i < np.pi-step:
        height = height + np.cos(n*i)*function(i)
        i = i + step
    return(step*height)
def intersin(function,n):
    step = .0001 #this is the incremnt size
    i = -np.pi # i is dummy variable
    height = 0 #height is the y value that is summed up 
    while i < np.pi-step:
        height = height + np.sin(n*i)*function(i)
        i = i + step
    return(step*height)
a = 1
atotal = np.array([0])
while a <10:
    aterm = intersin(f,a)/np.pi #establish each a term, and then assign to array
    anext = np.array([aterm])
    atotal = np.concatenate((atotal,anext)) #expands fib
    a = a+1
    
btotal = np.array([inter(-1*np.pi,np.pi,f)/(2*np.pi)])
b=1
while b < 10:
    bterm = intercos(f,a)/np.pi
    bnext = np.array([bterm])
    btotal = np.concatenate((btotal,bnext)) #expands b array
    b = b+1
def forier(x,aval,bval):
    i = 1
    b1 =np.array([aval[0]])#estabish storage array for values
    a1 =np.array([0])
    while i<10:
        aterm = np.array([aval[i]*np.sin(i*x)])
        bterm = np.array([bval[i]*np.cos(i*x)])
        b1 = np.concatenate((b1,bterm))
        a1 = np.concatenate((a1,aterm))
        total = np.concatenate((a1,b1))
        return(np.sum(total))
print(forier(1,atotal,btotal),f(1))
print(atotal)
print(btotal)        
import matplotlib as plot

        
    