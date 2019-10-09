# -*- coding: utf-8 -*-
"""
Created on Tue Oct  8 14:08:57 2019
Nathan Marshall

Calculates the average displacement in a 1D random walk for a given number
of trials over a given number of steps.
"""
#%%
import numpy as np
import matplotlib.pyplot as plt
num_steps = 1000
num_trials = 500

t = np.arange(0, num_steps+1)
x_all = []

for trial in range(0, num_trials):
    dx = 1
    x0 = 0
    x = [x0]
    for i in range(0, num_steps):
        x.append(x[-1] + np.random.choice([-dx, dx]))
    x_all.append(x)

summed = np.zeros(num_steps+1)
for i in range(0, num_trials):
    for j in range(0, num_steps+ 1):
        summed[j] += abs(x_all[i][j])
        
avg = summed/num_trials        
fig1 = plt.figure()
plt.plot(t, avg)
plt.xlabel('Number of Steps')
plt.ylabel('Average Displacement (m)')
plt.title('Average Random Walk Displacement - {} Trials'.format(num_trials))
