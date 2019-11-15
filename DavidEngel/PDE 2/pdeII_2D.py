# -*- coding: utf-8 -*-
"""
Created on Thu Nov 07 13:47:07 2019

@author: David Engel
The point of this code is to graph motion of a plane
"""
#importsimport numpy as np
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation as animate
from mpl_toolkits.mplot3d import Axes3D

#length of plane
Lx=10.0
Ly=10.0
lxsteps=100.0
lysteps=100.0
dx=(Lx/lxsteps)
dy=(Ly/lysteps)
#x and y cordinates
x=np.linspace(0,Lx,lxsteps)
y=np.linspace(0,Ly,lysteps)



tsteps=tf
dt=0.1

#inital values of ddf
ddf = np.zeros( (100, 100) )
#inital values of df
df = np.zeros( (100, 100) )
#making f and then filling it with correct vales
f=np.zeros( (100, 100) )
for n in range(100):
    for m in range(100):
        f[n,m]=np.sin(x[n]*np.pi/Lx)*np.sin(y[m]*np.pi/Ly)
#for animating the grah
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
surf = ax.plot_surface(x, y, f, cmap='coolwarm')
ax.set_zlim3d(-1, 1)

#animating
def update(frame):
    #updates ddf    
    for n in range(1,98):
        for m in range(1,98):
            ddf[n,m]=(f[n-1,m]+f[n+1,m]+f[n,m-1]+f[n,m+1])/(4*dx*dy)-f[n,m]/(dx*dy)
    #updates df
    for n in range(1,98):
        for m in range(1,98):
            df[n,m]+=ddf[n,m]*dt
    #updates f
    for n in range(1,98):
        for m in range(1,98):
            f[n,m]+=df[n,m]*dt
       
    ax.collections[0].remove()
    ax.plot_surface(x, y, f, cmap='coolwarm')
#animates the plot    
anim = animate(fig, update, frames=10, interval=1)