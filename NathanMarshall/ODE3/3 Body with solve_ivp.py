# -*- coding: utf-8 -*-
"""
Created on Tue Dec  3 15:53:40 2019
Nathan Marshall

"""
#%%
from scipy.integrate import solve_ivp
import numpy as np
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

num_frames = 800 #number of frames to get from solve_ivp
t0 = 0 #start time
tmax = 50 #stop time
t_out = np.linspace(t0, tmax, num_frames)

G = 1 #gravitational constant
m1 = 1 #mass 1
m2 = 1 #mass 2
m3 = 1 #mass 3

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

def func(t, z):
    x1 = z[0]
    x2 = z[1]
    x3 = z[2]
    y1 = z[3]
    y2 = z[4]
    y3 = z[5]
    vx1 = z[6]
    vx2 = z[7]
    vx3 = z[8] 
    vy1 = z[9]
    vy2 = z[10]
    vy3 = z[11]
    dvx1 = gravx(x1, y1, x2, y2, m2) + gravx(x1, y1, x3, y3, m3)
    dvx2 = gravx(x2, y2, x1, y1, m1) + gravx(x2, y2, x3, y3, m3)
    dvx3 = gravx(x3, y3, x1, y1, m1) + gravx(x3, y3, x2, y2, m2)
    dvy1 = gravy(x1, y1, x2, y2, m2) + gravy(x1, y1, x3, y3, m3)
    dvy2 = gravy(x2, y2, x1, y1, m1) + gravy(x2, y2, x3, y3, m3)
    dvy3 = gravy(x3, y3, x1, y1, m1) + gravy(x3, y3, x2, y2, m2)
    return(vx1, vx2, vx3, vy1, vy2, vy3, dvx1, dvx2, dvx3, dvy1, dvy2, dvy3)
    
ivs = [x10, x20, x30, y10, y20, y30, vx10, vx20, vx30, vy10, vy20, vy30]
sol = solve_ivp(func, [t0, tmax], ivs, t_eval=t_out)

x1 = sol.y[0]
x2 = sol.y[1]
x3 = sol.y[2]
y1 = sol.y[3]
y2 = sol.y[4]
y3 = sol.y[5]

#%% initialize animation figure

fig = plt.figure('Orbital Trajectory')
ax = plt.subplot()
ax.set_xlabel('X (m)')
ax.set_ylabel('Y (m)')
ax.set_xlim(-2.5, 2.5)
ax.set_ylim(-2.5, 2.5)
line1, = ax.plot([], [], color='b')
line2, = ax.plot([], [], color='g')
line3, = ax.plot([], [], color='r')
sca1 = ax.scatter([], [], color='b')
sca2 = ax.scatter([], [], color='g')
sca3 = ax.scatter([], [], color='r')
ax.set_aspect('equal')
step = round(len(x1)/num_frames) #step size for the plotted lists

def animation(frame):
    '''Function run to draw each frame of the animation'''
    stop = frame * step #the index at which to stop plotting for current frame
    start = (frame - 20) * step
    if start < 0:
        start = 0
    line1.set_data(x1[start:stop:step], y1[start:stop:step])
    line2.set_data(x2[start:stop:step], y2[start:stop:step])
    line3.set_data(x3[start:stop:step], y3[start:stop:step])
    sca1.set_offsets([x1[stop], y1[stop]])
    sca2.set_offsets([x2[stop], y2[stop]])
    sca3.set_offsets([x3[stop], y3[stop]])
    return(line1, line2, line3, sca1, sca2, sca3)
 
#call the FuncAnimation function
anim = animate(fig, animation, frames=num_frames, interval=30)