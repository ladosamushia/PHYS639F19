# -*- coding: utf-8 -*-
"""
Created on Tue Sep 10 13:23:59 2019

@author: David Engel
Using Euler's Method
"""
import numpy as np
import matplotlib.pyplot as plt

#initial x value
x0=0.0
xf=10.0
number=100
x=np.linspace(x0,xf,number)
#step size
dx=(xf-x0)/number
#initial y value
f0=-1.0
#the ODE
def fpri(x):
    return(np.sin(x))
#lists for plotting
g=[f0]
xall=[x0]
xi=x0
#the process
while xi < xf:
    g.append(g[-1]+fpri(xi)*dx)
    xall.append(xi)
    xi+=dx
#comparison
y=-np.cos(x)
#plotting it
plt.plot(xall,g,label='calculated function')
plt.plot(x,y,label='test')
plt.grid(True)
plt.legend()