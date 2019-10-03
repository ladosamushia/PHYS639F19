# -*- coding: utf-8 -*-
"""
Created on Wed Oct  2 22:39:33 2019

@author: Nathan
"""
#%%
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation as animate

t = np.linspace(0, 2 * np.pi, 100)
sine = np.sin(t)

fig = plt.figure()
ax = plt.subplot()
ax.set_ylim(-1, 1)
ax.set_xlim(0, 7)
line, = ax.plot([], [])

def func(frame):
    line.set_data(t[0:frame], sine[0:frame])
    return line,

animate(fig, func, frames=100, interval=50)


