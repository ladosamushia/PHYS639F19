# -*- coding: utf-8 -*-
"""
Created on Tue Oct  8 12:40:44 2019
Nathan Marshall

This is a stable sun-earth-moon 3-body orbital system. I used actual numbers
for orbital radius, orbital velocity, and body masses for our sun-earth-moon
system. The result is displayed in animations relative to the sun and the earth
so that the orbital motion of the earth around the sun and the moon around the
earth can be seen.
"""
#%%
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation as animate

x10 = 0 #initial x mass 1
y10 = 0 #initial y mass 1
vx10 = 0 #initial x velocity mass 1
vy10 = 0 #initial y velocity mass 1

x20 = 149.6e9 #initial x mass 2
y20 = 0 #initial y mass 2
vx20 = 0 #initial x velocity mass 2
vy20 = 30000 #initial y velocity mass 2

x30 = x20 + 384.4e6 #initial x mass 3
y30 = 0 #initial y mass 3
vx30 = 0 #initial x velocity mass 3
vy30 = vy20 + 1000 #initial y velocity mass 3

t0 = 0 #start time
tmax = 31536000 #stop time, 1 year in seconds
dt = 1000#time step size

G = 6.67408e-11 #gravitational constant
m1 = 1.989e30 #mass 1
m2 = 5.972e24 #mass 2
m3 = 7.348e22 #mass 3

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
plt.style.use('dark_background')
fig, [ax, ax2] = plt.subplots(1, 2)
ax.set_xlabel('X (m)')
ax.set_ylabel('Y (m)')
ax.set_xlim(-x30 - 2e10, x30 + 2e10)
ax.set_ylim(-x30 - 2e10, x30 + 2e10)
sca1 = ax.scatter([], [], color='y', s=50)
sca2 = ax.scatter([], [], color='b', s=5)
sca3 = ax.scatter([], [], color='0.5', s=3)
line2, = ax.plot([], [], color='b')
ax.set_aspect('equal')
ax.set_xlabel('X (m)')
ax.set_ylabel('Y (m)')
ax.set_title('Relative to Sun')

sca4 = ax2.scatter([], [], color='0.5')
sca5 = ax2.scatter(0, 0, color='b', s=70)
ax2.set_xlim(-500e6, 500e6)
ax2.set_ylim(-500e6, 500e6)
ax2.set_aspect('equal')
ax2.set_xlabel('X (m)')
ax2.set_ylabel('Y (m)')
ax2.set_title('Relative to Earth')

fig.suptitle('Sun-Earth-Moon Orbital Motion')

#set number of frames
num_frames = 400
step = round(len(x1)/num_frames) #step size for the plotted lists

def animation(frame):
    '''Function run to draw each frame of the animation'''
    stop = frame * step #the index at which to stop plotting for current frame
    start = (frame - 20) * step
    if start < 0:
        start = 0
    line2.set_data(x2[:stop:step], y2[:stop:step])
    sca1.set_offsets([x1[stop], y1[stop]])
    sca2.set_offsets([x2[stop], y2[stop]])
    sca3.set_offsets([x3[stop], y3[stop]])
    sca4.set_offsets([x3[stop]-x2[stop], y3[stop]-y2[stop]])
    return(sca1, sca2, sca3, sca4)
 
#call the FuncAnimation function
anim = animate(fig, animation, frames=num_frames, interval=50)

