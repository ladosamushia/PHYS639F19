# -*- coding: utf-8 -*-
"""
Created on Fri Oct  4 15:31:48 2019

@author: Nathan
"""
#%%
from scipy.integrate import solve_ivp
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation as animate

m1 = 1 #pendulum 1 mass in kg
m2 = 1 #pendulum 2 mass in kg
l1 = 1 #pendulum 1 length in m
l2 = 1 #pendulum 2 length in m
k = 1.5 #spring constant for coupling spring in N/m
g = 9.81 #acceleration of gravity in m/s^2

phi10 = 40 * np.pi/180 #initial angle pendulum 1 in degrees
phi20 = 0 * np.pi/180 #initial angle pendulum 2 in degrees
omega10 = 0 #initial angular velocity pendulum 1 in rad/sec
omega20 = 0 #initial angular velocity pendulum 2 in rad/sec
t0 = 0 #initial time
tmax = 20 #max time to stop simulation
frame_rate = 30
num_frames = int((tmax - t0) * frame_rate)
interval = 1/frame_rate * 1000
t_out = np.linspace(0, 20, num_frames)

def x1(phi1):
    return l1 * np.sin(phi1)

def y1(phi1):
    return -l1 * np.cos(phi1)
    
def x2(phi2):
    return l2 * np.sin(phi2)

def y2(phi2):
    return -l2 * np.cos(phi2)
    
def func(t, y):
    phi1 = y[0]
    phi2 = y[1]
    omega1 = y[2]
    omega2 = y[3]
    dphi1dt = omega1
    dphi2dt = omega2
    d2phi1dt = (-1/(m1 * l1**2) * m1 * g * l1 * np.sin(phi1) 
                + k*(x2(phi2) - x1(phi1)))
    d2phi2dt = (-1/(m2 * l2**2) * m2 * g * l2 * np.sin(phi2) 
                + k*(x1(phi1) - x2(phi2)))
    
    return(dphi1dt, dphi2dt, d2phi1dt, d2phi2dt)

sol = solve_ivp(func, [t0, tmax], [phi10, omega10, phi20, omega20],
                t_eval=t_out)
phi1 = sol.y[0]
phi2 = sol.y[1]

x_origin1 = -1
y_origin1 = 0
x_origin2 = 1
y_origin2 = 0

fig = plt.figure()
ax = plt.subplot()
line1 = ax.plot([], [], marker = 'o')[0]
line2 = ax.plot([], [], marker = 'o')[0]
line3 = ax.plot([], [], linewidth=0.3)[0]
ax.set_title('Coupled Pendulums')
ax.set_xlim(-2, 2)
ax.set_ylim(-1.5, 0)
ax.set_aspect('equal')

def animation(frame):
    #ax = plt.gca()
    line1, line2, line3 = ax.lines
    line1.set_data([x_origin1, x_origin1 + x1(phi1[frame])], 
                   [y_origin1, y1(phi1[frame])])
    line2.set_data([x_origin2, x_origin2 + x2(phi2[frame])], 
                   [y_origin2, y2(phi2[frame])])
    line3.set_data([x_origin1 + x1(phi1[frame]), x_origin2 + x2(phi2[frame])],
                    [y1(phi1[frame]), y2(phi2[frame])])


    
anim = animate(fig, animation, frames=num_frames, interval=interval)
 
