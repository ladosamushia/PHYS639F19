# -*- coding: utf-8 -*-
"""
Created on Thu Dec 05 13:14:00 2019

@author: David Engel
"""



#import necessary code
import numpy as np
import matplotlib.pyplot as plt 
import matplotlib.animation as animation

l=.5

xsteps=501

x=np.linspace(0,1,xsteps)

dx=1.0/(xsteps-1)


x0=0.1

sigma=(0.0001)**.5

psiR=np.zeros(xsteps)

psiI=np.zeros(xsteps)

dpsiR=np.zeros(xsteps)

dpsiI=np.zeros(xsteps)

v=np.zeros(xsteps)


psiR=np.exp(-1.0*(x-x0)*(x-x0)*(0.5)*(1.0/(sigma**2)))*1.0*np.cos(500.0*x)
psiI=np.exp(-1.0*(x-x0)*(x-x0)*(0.5)*(1.0/(sigma**2)))*1.0*np.sin(500.0*x)
psiR[0]=0
psiR[xsteps-1]=0
psiI[0]=0
psiI[xsteps-1]=0
#needed for animation
fig, ax = plt.subplots()

ax = plt.axes(xlim=(0, 1), ylim=(-1, 1))
#line for animation
lineR, = ax.plot(x,((psiR)**2+(psiI)**2))
#lineI, = ax.plot(x,psiI)
#function used in animation
dt=.00000005
#plt.plot(x,psiI)
#plt.plot(x,psiR)
#t=0
#tf=dt*100000
#while t<tf:
#    dpsiR[1:-1]=(-(psiI[:-2]+psiI[2:]-2*psiI[1:-1])/(dx**2))-v[1:-1]*psiI[1:-1]
#    dpsiI[1:-1]=((psiR[:-2]+psiR[2:]-2*psiR[1:-1])/(dx**2))-v[1:-1]*psiR[1:-1]
#
#    psiR[1:-1]+=dpsiR[1:-1]*dt
#    psiI[1:-1]+=dpsiI[1:-1]*dt
#    t+=dt
#plt.plot(x,psiR)
#plt.plot(x,psiI)
time=100000
w=50
tl=0.0
def update(t):

    for n in range(1,xsteps-1):
        dpsiR[n]=(-(psiI[n-1]+psiI[n+1]-2.0*psiI[n])/(dx**2))-v[n]*psiI[n]
        dpsiI[n]=((psiR[n-1]+psiR[n+1]-2.0*psiR[n])/(dx**2))-v[n]*psiR[n]
    for m in range(0,xsteps): 
        psiR[m]=psiR[m]+dpsiR[m]*dt
        psiI[m]=psiI[m]+dpsiI[m]*dt
    lineR.set_data(x,((psiR)**2)+((psiI)**2))
    return lineR,
#    lineI.set_data(x,psiI)
#    return lineI,
    
#plt.plot(x,psiR)
#for i in range(2000):
#    update(i)
##    plt.plot(x,(psiI**2)+(psiR**2))
##    plt.plot(x,psiI)
#plt.plot(x,psiR)
    
def graph(t):
    update(t)
    lineR.set_data(x,((psiR)**2)+((psiI)**2))
    return lineR,    
#animates the line
ani = animation.FuncAnimation(fig, graph, frames=time, repeat=False ,interval=0.0000001)
#shows the line
plt.show()
plt.grid()