# -*- coding: utf-8 -*-
"""
Created on Tue Nov 19 13:20:06 2019

@author: David Engel
"""
#import necessary code
import numpy as np
import matplotlib.pyplot as plt 
import matplotlib.animation as animation

l=1

xsteps=1000

x=np.linspace(0,l,xsteps)

dx=1.0/xsteps

dt=.0001

f=np.zeros(xsteps)
f[499]=1

#needed for animation
fig, ax = plt.subplots()
#line for animation
line, = ax.plot(x,f)
#function used in animation

def update(t):
    
    for n in range(1,xsteps-2):
        f[n]+=(((f[n+1]+f[n-1])-2*f[n])/(dx*2))*dt    
    
    
    line.set_data(x,f)
    return line,
    

#for i in range(1000):
#    update(i)
#    
#    plt.plot(x,f)
#animates the line
ani = animation.FuncAnimation(fig, update, frames=100 ,interval=100)
#shows the line
plt.show()