# -*- coding: utf-8 -*-
"""
Created on Tue Sep 17 13:09:44 2019
Nathan Marshall

This code numerically solves the differential equation for free fall under
gravitational acceleration accounting for linear drag. The equation is solved
for a range of initial velocity conditions. As we would expect, the velocities
all asymptotically approach a terminal velocity. According to the equation, 
the terminal velocity should be -g/a where g is gravitational acceleration and
'a' is the linear drag coefficent. With g = 9.81 m/s^2 and a = 0.5 s^-1, the
terminal velocities in the graph all converged to -19.62 m/s exactly as the
equation predicts. This prediction held when 'a' was varied.
"""
#%%
import numpy as np
import matplotlib.pyplot as plt

g = 9.81 # gravitational acceleration in m/s^2
a = 0.5 #linear drag coefficient
v0 = np.linspace(0, -30, 10) #range of initial conditions for velocity in m/s
dt = 0.0001 #step size for time in seconds
t0 = 0 #initial condition for time in seconds
tmax = 20 #max value of time in seconds

def dvdt(v):
    '''
    This function defines the functional form of the acceleration for free 
    fall under gravitational acceleration with linear drag as a function of
    velocity.
    '''
    return(-g - a*v )

def integrate(v0):
    '''
    Numerically integrates the differential equation dv/dt defined above given
    an initial condition for velocity.
    '''
    t = [t0] #list to contain time values
    v = [v0] #list to contain velocity values
    
    while t[-1] < tmax: #loop until time is greater than tmax
        v.append(v[-1] + dvdt(v[-1])*dt) #add dv/dt * dt to previous v
        t.append(t[-1] + dt) #add new t value to the list
    plt.plot(t, v, label='Numerical Result') #plotting numerical result

for v0_i in v0: #find a numerical solution for each initial velocity condition
    integrate(v0_i)
    
plt.title('Free Fall Velocity with Linear Drag')
plt.xlabel('Time (s)')
plt.ylabel('Velocity (m/s)')
plt.grid()
