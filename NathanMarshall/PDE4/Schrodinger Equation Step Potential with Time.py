# -*- coding: utf-8 -*-
"""
Created on Tue Dec  3 13:24:34 2019
Nathan Marshall

Schrodinger Equation - Using Real and Imaginary Components
-Step potential
"""
#%%
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation as animate

num = 400  #number of points for psi arrays
num_steps = 100 #number of time steps
sigma = 0.1
xmin = -4
xmax = 4
psi_r = np.linspace(xmin, xmax, num) #array for real psi values
psi_r = np.exp(-psi_r**2/(2*sigma**2)) * np.cos(10*psi_r)
psi_im = np.linspace(xmin, xmax, num)  #array for imaginary psi values
psi_im = np.exp(-psi_im**2/(2*sigma**2)) * np.sin(10*psi_im)
dpsi_r = np.zeros(num)  #array for real psi derivative
dpsi_im = np.zeros(num) #array for imaginary psi derivative
x = np.linspace(xmin, xmax, num) #x values to plot against
dx = 0.01
dt = 0.0000005


def psi_step():
    for i in range(1, num-1):
        if x[i] < 0.5:
            v = 0
        if x[i] > 0.5:
            v = 2000
        dpsi_r[i] = -(psi_im[i+1] + psi_im[i-1] - 2*psi_im[i]) / dx**2 + v*psi_im[i]
        dpsi_im[i] = (psi_r[i+1] + psi_r[i-1] - 2*psi_r[i]) / dx**2 - v*psi_r[i]
    for i in range(0, num):
        psi_r[i] += dpsi_r[i] * dt
        psi_im[i] += dpsi_im[i] * dt
    
fig, ax = plt.subplots(1,1)
line, = ax.plot(x, psi_r**2 + psi_im**2)

def update(frame):
    psi_step()
    line.set_data(x, psi_r**2 + psi_im**2)

anim = animate(fig, update, frames=num_steps, repeat=True, interval=20)

