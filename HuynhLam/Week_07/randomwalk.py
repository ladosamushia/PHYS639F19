# -*- coding: utf-8 -*-
"""
Created on Tue Oct  8 13:18:23 2019

@author: vkonline
"""

#%%
#Random walk in 1D
#

# Import libraries
import numpy as np #math library
import matplotlib.pyplot as plt # Plotting library
from matplotlib.animation import FuncAnimation as animate

#%%
def rwin1D(x0,Nstep):
    t = np.linspace(0,Nstep,Nstep+1)
    x = np.zeros(len(t))
    x[0]=x0
    for i in range(Nstep):
        step = np.random.choice([-1,0,1],p=[0.3,0.3,0.4])
        x[i+1]=x[i]+step
    return t,x

#t1,x1 = rwin1D(x0,Nstep)
#t2,x2 = rwin1D(x0,Nstep)
#t3,x3 = rwin1D(x0,Nstep)
#t4,x4 = rwin1D(x0,Nstep)
#t5,x5 = rwin1D(x0,Nstep)
#plt.plot(t1, x1, label = '1')
#plt.plot(t2, x2, label = '2')
#plt.plot(t3, x3, label = '3')
#plt.plot(t4, x4, label = '4')
#plt.plot(t5, x5, label = '5')

Nstep = 1000
x0 =0

for i in range(10):
    t,y = rwin1D(x0,Nstep)
    plt.plot(t,y)
    
plt.legend()
plt.show()

#%%
def rwin2D(x0,y0,Nstep):
    t = np.linspace(0,Nstep,Nstep+1)
    x = np.zeros(len(t))
    y = np.zeros(len(t))
    x[0]=x0
    y[0]=y0
    for i in range(Nstep):
        step = np.random.choice([1,2,3,4])
        if step == 1:
            x[i+1]=x[i]-1
            y[i+1]=y[i]
        elif step == 2:
            x[i+1]=x[i]+1
            y[i+1]=y[i]
        elif step == 3:
            y[i+1]=y[i]-1
            x[i+1]=x[i]
        else:
            y[i+1]=y[i]+1
            x[i+1]=x[i]
    return t,x,y


Nstep = 100000
x0 =0
y0=0

t1,x1,y1 = rwin2D(x0,y0,Nstep)
t2,x2,y2 = rwin2D(x0,y0,Nstep)
t3,x3,y3 = rwin2D(x0,y0,Nstep)

#initialize animation figure
fig = plt.figure('Trajectory')
ax = plt.subplot()
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_xlim(-100, 100)
ax.set_ylim(-100, 100)
line1, = ax.plot([], [], color='b')
line2, = ax.plot([], [], color='g')
line3, = ax.plot([], [], color='r')
sca1 = ax.scatter([], [], color='b')
sca2 = ax.scatter([], [], color='g')
sca3 = ax.scatter([], [], color='r')

#set number of frames
num_frames = Nstep
step = round(Nstep/num_frames) #step size for the plotted lists

def animation(frame):
    '''Function run to draw each frame of the animation'''
    stop = frame * step #the index at which to stop plotting for current frame
    line1.set_data(x1[0:stop:step], y1[0:stop:step])
    line2.set_data(x2[0:stop:step], y2[0:stop:step])
    line3.set_data(x3[0:stop:step], y3[0:stop:step])
    sca1.set_offsets([x1[stop], y1[stop]])
    sca2.set_offsets([x2[stop], y2[stop]])
    sca3.set_offsets([x3[stop], y3[stop]])
    return(line1, line2, line3, sca1, sca2, sca3)
    
#call the FuncAnimation function
animate(fig, animation, frames=num_frames, interval=20) 