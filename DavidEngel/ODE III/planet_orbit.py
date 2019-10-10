# -*- coding: utf-8 -*-
"""
Created on Tue Oct 01 13:04:59 2019

@author: David Engel
The point od this code is to plot one object orbiting a significatnly more 
massive object
"""
import numpy as np
import matplotlib.pyplot as plt
#initial conditions

x0=149.6*(10**9)

y0=0.0

t0=0.0

tf=365*24*60*60*3

dt=5
#G=1
G=6.674088*(10**-11) #gravitational constant in m**3 kg**-1 s**-2
#M=1
M=1.989*(10**30)#mass of sun in kg

me=1

def d2xdt2(x,y):
    return(-G*M*x/((x**2+y**2)**1.5))
def d2ydt2(x,y):
    return(-G*M*y/((x**2+y**2)**1.5))

#v=1.25
v=30000.0
theta=90
rad=theta*np.pi/180
vx0=v*np.cos(rad)

vy0=v*np.sin(rad)

ti=t0
#list for time
t=[ti]
#List for x position
x=[x0]
#list for y postition
y=[y0]
#list for x velocity
vx=[vx0]
#list for y velocity
vy=[vy0]
#n is used for a counter
n=0
#while loop used for formulas
while ti<tf:
    #list of t values modifed by loop
    t.append(ti)
    #eulers method used for x velocity
    vx.append(vx[n-1]+d2xdt2(x[n],y[n])*dt)    
    #eulers method for x position
    x.append(x[n-1]+vx[n]*dt)
    #eulers method for y velocity
    vy.append(vy[n-1]+d2ydt2(x[n],y[n])*dt)
    #eulers method for y position
    y.append(y[n-1]+vy[n]*dt)
    #counter operation
    n+=1
    #time increasing by a small incrament
    ti+=dt
    
plt.plot(x, y)
plt.title('Position of Planet')
plt.xlabel('x')
plt.ylabel('y')