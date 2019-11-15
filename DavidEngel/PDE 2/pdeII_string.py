# -*- coding: utf-8 -*-
"""
Created on Tue Nov 05 13:19:35 2019

@author: David Engel
The point of this code is to graph motion of a string
"""
#imports
import numpy as np
import matplotlib.pyplot as plt 

#length of string
L=10

lsteps=100

dx=(L/lsteps)
dx=.1
x=np.linspace(0,L,lsteps)

f0=np.sin(x*np.pi/L)

f0[0]=0.0
f0[99]=0.0

ti=0

tf=100
tsteps=tf
dt=0.1



df=np.zeros(lsteps)
ddf = np.zeros(lsteps)

while ti<=tf:
    ddf[1:-1] = (f0[:-2]+f0[2:])/(2*dx) - f0[1:-1]/dx
    df[1:-1] += ddf[1:-1]*dt
    f0[1:-1]+=df[1:-1]*dt
    ti+=dt
    plt.plot(x,f0)


