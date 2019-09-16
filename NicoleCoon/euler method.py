# -*- coding: utf-8 -*-
"""
Created on Tue Sep 10 13:27:39 2019

@author: alecc
"""
import numpy as np
import matplotlib.pyplot as plt
# create basic funcitons
def flinear(x, fx):
    return x

def fcos(x, fx):
    return np.cos(x)

def fnegexp(x, fx):
    return np.exp(-x)

def complicated_function(x, fx):
    return (1 + np.cos(x))/(1 + 2*fx)
#deriv takes 2 inputs, x and function of x
def euler(x0,f0,xi,xf,dx,deriv):    
    #define 2 arrays: store x and y values
    x = np.array([x0])
    y = np.array([f0])
    i = x0-dx
    while i >xi:
        xval = np.array([i]) #incrment x
        x = np.concatenate((x,xval)) #add to arrat
        dfdx = deriv(x[-1],y[-1]) #derv evaluated
        yval = y[-1]-dfdx*dx #incrment y
        yval = np.array([yval])
        y = np.concatenate((y,yval))
        i = i-dx
    i = x0+dx
    #flip to put lowest values first
    x=np.flip(x)
    y=np.flip(y)
    #repeat but forward
    while i<xf:
        xval = np.array([i])
        x = np.concatenate((x,xval))
        dfdx = deriv(x[-1],y[-1])
        yval = y[-1]+dfdx*dx
        yval = np.array([yval])
        y = np.concatenate((y,yval))
        i = i+dx
    return(x,y)
# break down region into peices, and plot along piece of region
NIC = 10
IC = np.linspace(-2, 2, NIC)
for i in range(NIC):
    x,y = euler(0,IC,0,10,.001,complicated_function)    
    plt.plot(x, y)