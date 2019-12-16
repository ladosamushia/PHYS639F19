# -*- coding: utf-8 -*-
"""
Created on Mon Dec 16 10:18:36 2019

@author: David Engel
This is a free particle with a positive well.
"""



#import necessary code
import numpy as np
import matplotlib.pyplot as plt 
import matplotlib.animation as animation

l=.5

xsteps=501

x=np.linspace(0,1,xsteps)

dx=1.0/(xsteps-1)


x0=0.4

sigma=(0.0001)**.5

psiR=np.zeros(xsteps)

psiI=np.zeros(xsteps)

dpsiR=np.zeros(xsteps)

dpsiI=np.zeros(xsteps)

v=np.zeros(xsteps)
for i in range(250,501):
    v[i]=100000

psiR=np.exp(-1.0*(x-x0)*(x-x0)*(0.5)*(1.0/(sigma**2)))*1.0*np.cos(100.0*x)
psiI=np.exp(-1.0*(x-x0)*(x-x0)*(0.5)*(1.0/(sigma**2)))*1.0*np.sin(100.0*x)
psiR[0]=0
psiR[xsteps-1]=0
psiI[0]=0
psiI[xsteps-1]=0
#needed for animation

dt=.00000005
w=500
plt.plot(x,(psiI**2)+(psiR**2))
t=0
tf=dt*10000
t1=tf/4.0
t2=tf/2.0
t3=tf*(3.0/4.0)

while t<t1:
    dpsiR[1:-1]=(-(psiI[:-2]+psiI[2:]-2*psiI[1:-1])/(dx**2))-v[1:-1]*psiI[1:-1]
    dpsiI[1:-1]=((psiR[:-2]+psiR[2:]-2*psiR[1:-1])/(dx**2))+v[1:-1]*psiR[1:-1]

    psiR[1:-1]=psiR[1:-1]+dpsiR[1:-1]*dt
    psiI[1:-1]=psiI[1:-1]+dpsiI[1:-1]*dt

    t+=dt
plt.plot(x,(psiI**2)+(psiR**2))

while t<t2:
    dpsiR[1:-1]=(-(psiI[:-2]+psiI[2:]-2*psiI[1:-1])/(dx**2))-v[1:-1]*psiI[1:-1]
    dpsiI[1:-1]=((psiR[:-2]+psiR[2:]-2*psiR[1:-1])/(dx**2))+v[1:-1]*psiR[1:-1]
    psiR[1:-1]=psiR[1:-1]+dpsiR[1:-1]*dt
    psiI[1:-1]=psiI[1:-1]+dpsiI[1:-1]*dt

    t+=dt
plt.plot(x,(psiI**2)+(psiR**2))

while t<t3:
    dpsiR[1:-1]=(-(psiI[:-2]+psiI[2:]-2*psiI[1:-1])/(dx**2))-v[1:-1]*psiI[1:-1]
    dpsiI[1:-1]=((psiR[:-2]+psiR[2:]-2*psiR[1:-1])/(dx**2))+v[1:-1]*psiR[1:-1]
    psiR[1:-1]=psiR[1:-1]+dpsiR[1:-1]*dt
    psiI[1:-1]=psiI[1:-1]+dpsiI[1:-1]*dt
    t+=dt
plt.plot(x,(psiI**2)+(psiR**2))


while t<tf:
    dpsiR[1:-1]=(-(psiI[:-2]+psiI[2:]-2*psiI[1:-1])/(dx**2))-v[1:-1]*psiI[1:-1]
    dpsiI[1:-1]=((psiR[:-2]+psiR[2:]-2*psiR[1:-1])/(dx**2))+v[1:-1]*psiR[1:-1]
    psiR[1:-1]+=dpsiR[1:-1]*dt
    psiI[1:-1]+=dpsiI[1:-1]*dt

    t+=dt
plt.plot(x,(psiI**2)+(psiR**2))



plt.grid()