# -*- coding: utf-8 -*-
"""
Created on Tue Dec 03 13:25:58 2019

@author: Vandi
"""


#import necessary code
import numpy as np
import matplotlib.pyplot as plt 
import matplotlib.animation as animation

l=1

xsteps=1000

x=np.linspace(0,l,xsteps)

dx=1.0/xsteps

dt=.0000001

x0=0.5

sigma=0.05

psiR=np.zeros(xsteps)

psiI=np.zeros(xsteps)

dpsiR=np.zeros(xsteps)

dpsiI=np.zeros(xsteps)

v=np.zeros(xsteps)

m=0.0
m2=0
while m<=l:
    
    psiR[m2]=np.exp(-1.0*(m-x0)*(m-x0)*(0.5)*(1.0/(sigma**2)))*np.cos(m)
    psiI[m2]=np.exp(-1.0*(m-x0)*(m-x0)*(0.5)*(1/(sigma**2)))*np.sin(m)
    m+=dx
    m2+=1
#needed for animation
fig, ax = plt.subplots()
#line for animation
lineR, = ax.plot(x,psiR)
#lineI, = ax.plot(x,psiI)
#function used in animation

def update(t):
    
    for n in range(1,xsteps-1):
        dpsiR[n]=(-(psiI[n-1]+psiI[n+1]-2*psiI[n])/(dx**2))-v[n]*psiI[n]
        dpsiI[n]=((psiR[n-1]+psiR[n+1]-2*psiR[n])/(dx**2))-v[n]*psiR[n]
        psiR[n]+=dpsiR[n]*dt
        psiI[n]+=dpsiI[n]*dt
    lineR.set_data(x,psiR)
    return lineR,
#    lineI.set_data(x,psiI)
#    return lineI,
plt.plot(x,psiR)
for i in range(900):
    update(i)
#    plt.plot(x,(psiI**2)+(psiR**2))
#    plt.plot(x,psiI)
plt.plot(x,psiR)
    
    
##animates the line
#ani = animation.FuncAnimation(fig, update, frames=100000 ,interval=10)
##shows the line
#plt.show()