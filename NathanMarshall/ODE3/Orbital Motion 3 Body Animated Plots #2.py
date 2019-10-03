# -*- coding: utf-8 -*-
"""
Created on Wed Oct  2 19:11:11 2019

This code computes the orbital trajectories of a 3 body system and creates an
animation of the result. The different part about this code is that the trails
of the bodies in motion are deleted after they pass a certain length so the
animation doesn't become too cluttered with trails, allowing for longer 
simulations.
"""
#%%
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation as animate

x10 = -1 #initial x mass 1
y10 = 0 #initial y mass 1
vx10 = 0 #initial x velocity mass 1
vy10 = -1.2 #initial y velocity mass 1

x20 = 0.01 #initial x mass 2
y20 = 0 #initial y mass 2
vx20 = 0 #initial x velocity mass 2
vy20 = 0 #initial y velocity mass 2

x30 = 1 #initial x mass 3
y30 = 0 #initial y mass 3
vx30 = 0 #initial x velocity mass 3
vy30 = 1.2 #initial y velocity mass 3

t0 = 0 #start time
tmax = 50 #stop time
dt = 0.001 #time step size

G = 1 #gravitational constant
m1 = 1 #mass 1
m2 = 1 #mass 2
m3 = 1 #mass 3

x1 = [x10] #list to contain x values mass 1
y1 = [y10] #list to contain y values mass 1
vx1 = [vx10] #list to contain x velocities mass 1
vy1 = [vy10] #list to contain y velocities mass 1

x2 = [x20] #list to contain x values mass 2
y2 = [y20] #list to contain y values mass 2
vx2 = [vx20] #list to contain x velocities mass 2
vy2 = [vy20] #list to contain y velocities mass 2

x3 = [x30] #list to contain x values mass 3
y3 = [y30] #list to contain y values mass 3
vx3 = [vx30] #list to contain x velocities mass 3
vy3 = [vy30] #list to contain y velocities mass 3

t = [t0] #list to contain time values

def gravx(x1, y1, x2, y2, m):
    '''Acceleration due to gravitation in x direction.'''
    x = x1 - x2
    y = y1 - y2
    return(- G * m * x / ((x**2 + y**2)**(3/2)))
def gravy(x1, y1, x2, y2, m):
    '''Acceleration due to gravitation in y direction.'''
    x = x1 - x2
    y = y1 - y2
    return(- G * m * y / ((x**2 + y**2)**(3/2)))   
    
while t[-1] < tmax:
    x1.append(x1[-1] + vx1[-1]*dt)
    y1.append(y1[-1] + vy1[-1]*dt)
    vx1.append(vx1[-1] + (gravx(x1[-1], y1[-1], x2[-1], y2[-1], m2) 
               + gravx(x1[-1], y1[-1], x3[-1], y3[-1], m3)) * dt)
    vy1.append(vy1[-1] + (gravy(x1[-1], y1[-1], x2[-1], y2[-1], m2) +
               gravy(x1[-1], y1[-1], x3[-1], y3[-1], m3)) * dt)
    
    x2.append(x2[-1] + vx2[-1]*dt)
    y2.append(y2[-1] + vy2[-1]*dt)
    vx2.append(vx2[-1] + (gravx(x2[-1], y2[-1], x1[-1], y1[-1], m1) 
               + gravx(x2[-1], y2[-1], x3[-1], y3[-1], m3)) * dt)
    vy2.append(vy2[-1] + (gravy(x2[-1], y2[-1], x1[-1], y1[-1], m1) +
               gravy(x2[-1], y2[-1], x3[-1], y3[-1], m3)) * dt)
    
    x3.append(x3[-1] + vx3[-1]*dt)
    y3.append(y3[-1] + vy3[-1]*dt)
    vx3.append(vx3[-1] + (gravx(x3[-1], y3[-1], x1[-1], y1[-1], m1) 
               + gravx(x3[-1], y3[-1], x2[-1], y2[-1], m2)) * dt)
    vy3.append(vy3[-1] + (gravy(x3[-1], y3[-1], x1[-1], y1[-1], m1) +
               gravy(x3[-1], y3[-1], x2[-1], y2[-1], m2)) * dt)
    
    t.append(t[-1] + dt)

#initialize animation figure
fig = plt.figure('Orbital Trajectory')
ax = plt.subplot()
ax.set_xlabel('X (m)')
ax.set_ylabel('Y (m)')
ax.set_xlim(-2.5, 2.5)
ax.set_ylim(-2.5, 2.5)
#set number of frames
num_frames = 800
step = round(len(x1)/num_frames) #step size for the plotted lists

def animation(frame):
    '''Function run to draw each frame of the animation'''
    ax = plt.gca()
    for artist in plt.gca().lines + plt.gca().collections:
        artist.remove() #clear all previous plots each frame
    stop = frame * step #the index at which to stop plotting for current frame
    start = (frame - 20) * step
    if start < 0:
        start = 0
    ax.plot(x1[start:stop:step], y1[start:stop:step], color='b')
    ax.plot(x2[start:stop:step], y2[start:stop:step], color='g')
    ax.plot(x3[start:stop:step], y3[start:stop:step], color='r')
    ax.scatter(x1[stop], y1[stop], color='b')
    ax.scatter(x2[stop], y2[stop], color='g')
    ax.scatter(x3[stop], y3[stop], color='r')
#call the FuncAnimation function
animate(fig, animation, frames=num_frames, interval=20) 
