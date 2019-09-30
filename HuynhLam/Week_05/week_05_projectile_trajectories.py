# -*- coding: utf-8 -*-
"""
Created on Mon Sep 16 21:55:37 2019

PHYS 639 >>> Assignments >>> Week 5 >>> ODE II
HUYNH LAM

"""
#%%===================================================================================================================================================
#=====================================================================================================================================================
#=========== Week 5 >> Solve a differential equation describing motion of a projectile launched with some initial velocity and angle. ================
#=========== You have to find x(t), y(t), and plot the trajectories.                                                                  ================
#=========== (T1) Solve a simple projectile motion without air resistance and constant g.                                             ================
#=========== (T1-T3) Add air resistance term that's proportional to the velocity squared.                                             ================
#=========== (T1-T3) Account for the fact that g changes with the elevation (1/R2).                                                   ================
#=========== Do the results change in the expected way when you change initial conditions and parameters?)                            ================
#=====================================================================================================================================================
#=====================================================================================================================================================

# Import libraries
import numpy as np #math library
import matplotlib.pyplot as plt # Plotting library

#==============================================================================================================================
# Function to solve second order ODE 
# It takes in the intial conditions
##### (x0,f0), the upper limit of the range you want to solve your ODE (high),
##### Initial time t0        ##### Initial positions x0, y0         ##### Initial velocity v     ##### Launch angle in degrees "angle"
##### Final time tf          ##### Number of steps Nsteps           ##### Base line (landscape) "y_base"
# It gives out the positions as function of time (t,x,y)
#==============================================================================================================================
def projectile_trajectories(t0, x0, y0, v, angle, tf, Nsteps, ax, ay, y_base):
    # Initialize array with discrete values of time
    t = np.linspace(t0,tf,Nsteps)
    # Initialize array to store the solution of f(x,y)
    x = np.zeros(len(t))
    y = np.zeros(len(t))
    # step size
    dt = (tf - t0)/Nsteps
    # First value of (x,y,vx,vy) is the initial condition
    x[0] = x0
    y[0] = y0
    # Angle from degrees to radiants
    angle = angle/180*np.pi
    vx = v*np.cos(angle)
    vy = v*np.sin(angle)
    # Loop to calculate velocity from acceleration
    # and from acceleration to location
    for i in range(1,Nsteps):
        if y[i-1] >= y_base:
            vx = vx + ax(x[i-1], v, vx)*dt
            vy = vy + ay(y[i-1], v, vy)*dt
            v = np.sqrt(vx**2+vy**2)
            x[i] = x[i-1] + vx*dt
            y[i] = y[i-1] + vy*dt
        else:
            x[i] = x[i-1]
            y[i] = y[i-1]
    return t, x, y  
#==============================================================================================================================
# Initial conditions
# consider gravity to be a constant
g = 9.8
# drag coefficient
a = 0.5
# Initial time
t0 = 0
# Final time
tf = 25
# Initial positions
x0 = 0
y0 = 0
# Initial velocity
v = 5
# Launch angle
angle = 45
# Number of steps
Nsteps = 10000
# Base line (landscape)
base = 0
# Earth's radius
R = 10
#==============================================================================================================================
# Acceleration as a function of velocity (v) and y
# Case 1: Simple projectile motion without air resistance and constant g
def ay1(y,v,vy):
    return -g
def ax1(x,v,vx):
    return 0
# Case 2: Add air resistance term that's proportional to the velocity squared.
def ay2(y,v,vy):
    return - g - a*v*vy
def ax2(x,v,vx):
    return - a*v*vx
# Case 3: Account for the fact that g changes with the elevation (1/R^2).
def ay3(y,v,vy):
    return - g*R**2/(R+y)**2 - a*v*vy
def ax3(x,v,vx):
    return - a*v*vx
#==============================================================================================================================
t1,x1,y1 = projectile_trajectories(t0, x0, y0, v, angle, tf, Nsteps, ax1, ay1, base)
plt.plot(x1, y1, label = 'Case 1: v = %.1f angle = %.1f degrees g = %.1f $a$ = %.1f $R$ = %.1f' %(v,angle,g,0,R))

t2,x2,y2 = projectile_trajectories(t0, x0, y0, v, angle, tf, Nsteps, ax2, ay2,base)
plt.plot(x2, y2, label = 'Case 2: v = %.1f angle = %.1f degrees g = %.1f $a$ = %.1f $R$ = %.1f' %(v,angle,g,a,R))

t3,x3,y3 = projectile_trajectories(t0, x0, y0, v, angle, tf, Nsteps, ax3, ay3,base)
plt.plot(x3, y3, label = 'Case 3: v = %.1f angle = %.1f degrees g = g(y) $a$ = %.1f $R$ = %.1f' %(v,angle,a,R))
    
plt.legend()
plt.show()