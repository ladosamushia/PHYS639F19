# -*- coding: utf-8 -*-
"""
Created on Thu Oct 03 13:55:39 2019

@author: David Engel
"""
import numpy as np
import matplotlib.pyplot as plt
#inital conditions
t0=0
x0=0
vx0=1
k=1
m=1
tf=20
dt=.01
a=.5
b=.25

#differerntial equation for liner
def d2xdt2linear(x):
    return(-k*x/m)
#differerntial equation for quadratic
def d2xdt2quad(x):
    return((-k*x/m)-a*(x**2))
#differerntial equation for cubic    
def d2xdt2cubic(x):
    return((-k*x/m)-a*(x**2)-b*(x**3))
#lists for plotting
t=[t0]
x=[x0]
vx=[vx0]
ti=t0
#for a counter
n=0
#loop for linear
while ti<=tf:
    t.append(ti)
    vx.append(vx[n-1]+d2xdt2linear(x[n])*dt)
    x.append(x[n-1]+vx[n]*dt)
    n+=1
    ti+=dt
plt.plot(t,x,label='Linear')

t2=[t0]
x2=[x0]
vx2=[vx0]
ti2=t0
n2=0
#loop for quadratic
while ti2<=tf:
    t2.append(ti2)
    vx2.append(vx2[n2-1]+d2xdt2quad(x2[n2])*dt)
    x2.append(x2[n2-1]+vx2[n2]*dt)
    n2+=1
    ti2+=dt

plt.plot(t2,x2,label='Quadratic')

t3=[t0]
x3=[x0]
vx3=[vx0]
ti3=t0
n3=0
#loop for cubic
while ti3<=tf:
    t3.append(ti3)
    vx3.append(vx3[n3-1]+d2xdt2cubic(x3[n3])*dt)
    x3.append(x3[n3-1]+vx3[n3]*dt)
    n3+=1
    ti3+=dt
    
#plot
plt.plot(t3,x3,label='Cubic')
plt.title('Position of Object')
plt.xlabel('t')
plt.ylabel('x')
plt.legend()