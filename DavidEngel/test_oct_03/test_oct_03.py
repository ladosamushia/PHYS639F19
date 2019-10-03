# -*- coding: utf-8 -*-
"""
Created on Thu Oct 03 13:08:15 2019

@author: David Engel
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
#air resistance constant
a=0
af=2
da=0.5
while a<=af:
    
    #radious of earth
    Re=6738100.0
    #differential equation for changing gravity and y position velocity 
    def d2ydt2 (vyi,yi):
        return (-(g*(Re**2)/((Re+yi)**2))-a*vyi)
    #differential equatin used for x postion
    def d2xdt2 (vxi):
        return (-a*vxi)
    #initail speed
    v0=10
    #final speed
    vf=1000
    #change in speed
    dv=10
    dist=[]
    v0l=[]
    while v0<=vf:
        v0l.append(v0)
        #launch angle
        theta=45
        #degree in radians
        rad=np.pi*theta/180
        #inital speed in y direction
        vy0=np.sin(rad)*v0
        #inital speed in x direcrtion
        vx0=np.cos(rad)*v0
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
        ti=0.0
        while ti<tf:
            #list of t values modifed by loop
            t.append(ti)
            #eulers method used for x velocity
            vx.append(vx[n-1]+d2xdt2(vx[n-1])*dt)    
            #eulers method for x position
            x.append(x[n-1]+vx[n]*dt)
            #eulers method for y velocity
            vy.append(vy[n-1]+d2ydt2((vy[n-1])*dt,y[n-1]))
            #eulers method for y position
            y.append(y[n-1]+vy[n]*dt)
            #counter operation
            n+=1
            #time increasing by a small incrament
            ti+=dt
            #this stops operation when y returning to ground
            if y[n]<.0001:
                ti=tf 
        #finding max distance        
        m=max(x)
        #finding time of flight
        time=n/1000.0
        v0+=dv
        dist.append(m)
    

        #plot
        plt.plot(v0l, dist)
        plt.title('Inital speed V range')
        plt.xlabel('Initial Velocity(m/s)')
        plt.ylabel('Distance X(m)')
        
    a+=da
plt.savefig('test.png')
print 'Launch angle is 45 degrees'