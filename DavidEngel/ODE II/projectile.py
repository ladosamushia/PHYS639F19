# -*- coding: utf-8 -*-
"""
Created on Tue Sep 24 13:06:44 2019

@author: David Engel
The point of this program is to solve a projectile
"""
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 24 13:06:44 2019

@author: David Engel
The point of this program is to solve for the position of a ph=rojectile with air resistance

"""
import numpy as np
import matplotlib.pyplot as plt
#all the inital conditions
x0=0.0
y0=0.0
ti=0.0
g=9.81
#final time
tf=100000000
#step in time
dt=.001

#initial speed
v0=1000
#launch angle
theta=30
#degree in radians
rad=np.pi*theta/180
#inital speed in y direction
vy0=np.sin(rad)*v0
#inital speed in x direcrtion
vx0=np.cos(rad)*v0
#differential equatin used for y postion
def d2ydt2 (vyi):
    return (-g)
#differential equatin used for x postion
def d2xdt2 (vxi):
    return (0)
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
#while loop used for formuls
while ti<tf:
    #list of t values modifed by loop
    t.append(ti)
    #eulers method used for x velocity
    vx.append(vx[n-1]+d2xdt2(vx[n-1])*dt)    
    #eulers method for x position
    x.append(x[n-1]+vx[n]*dt)
    #eulers method for y velocity
    vy.append(vy[n-1]+d2ydt2(vy[n-1])*dt)
    #eulers method for y position
    y.append(y[n-1]+vy[n]*dt)
    #counter operation
    n+=1
    #time increasing by a small incrament
    ti+=dt
    #this stops operation when y returning to ground
    if y[n]<.0001:
        ti=tf 
#finding max hieght        
m=max(y)
#finding time of flight
time=n/1000.0
print 'Time of Flight=' 
print time 
print "Max height="
print m
#plot
plt.plot(x, y)
plt.title('Position of Projectile')
plt.xlabel('x')
plt.ylabel('y')