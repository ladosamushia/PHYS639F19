# -*- coding: utf-8 -*-
"""
Created on Thu Sep 12 13:15:34 2019

@author: Vandi
The purpose of the program is to plot solutions to f'=(1+cos(x))/(1+2*f) for -2<f(0)<2
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

def fpri(x,f):
    return((1+np.cos(x))/(1+(2*f)))
#lists for plotting

xall=[x0]
yi=-2.0
yf=2.0
#this allows for and cycles through the possible y-intercept postions
while yi < yf :
    
    f0=yi
    f=f0
    g=[f0]
    xi=x0
    #eulers method is used to solve based off of the initial conditions
    while xi < xf:
        
        g.append(g[-1]+fpri(xi,f0)*dx)
        f0=g[1]
        xall.append(xi)
        xi+=dx
    #plots each graph    
    plt.plot(xall,g)
    plt.grid(True)
    plt.legend()
    xall=[x0]
    yi+=.1
plt.xlim(-.1,10.1)
plt.ylim(-5,5)