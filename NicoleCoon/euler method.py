# -*- coding: utf-8 -*-
"""
Created on Tue Sep 10 13:27:39 2019

@author: alecc
"""
import numpy as np
import matplotlib.pyplot as plt
def fprime(x):
    return np.sin(x)
# create given point, and upper and lower bounds
fstart = 0
f0 = -1
xi = -2*np.pi
xf = 2*np.pi
dx = .0001
#define 2 arrays: store x and y values
x = np.array([fstart])
y = np.array([f0])
i = fstart-dx
while i >xi:
    xval = np.array([i]) #incrment x
    x = np.concatenate((x,xval)) #add to arrat
    dfdx = ((1+np.cos(i))/(1+y[-1]+y[-1]))
    yval = y[-1]-dfdx*dx #incrment y
    yval = np.array([yval])
    y = np.concatenate((y,yval))
    i = i-dx
i = fstart+dx
#flip to put lowest values first
x=np.flip(x)
y=np.flip(y)
while i<xf:
    xval = np.array([i])
    x = np.concatenate((x,xval))
    dfdx = (1+np.cos(i))/(1+2*y[-1])
    yval = y[-1]+dfdx*dx
    yval = np.array([yval])
    y = np.concatenate((y,yval))
    i = i+dx

plt.plot(x,y)
    