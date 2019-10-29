# -*- coding: utf-8 -*-
"""
Created on Thu Oct 24 14:00:43 2019
Nathan Marshall

"""
#%%
import numpy as np
import matplotlib.pyplot as plt

def spin_calc(num_steps, numx, numy, T, B):
    spins = np.random.choice([-1, 1], (numx, numy))
    for i in range(0, num_steps):
        randrow, randcol = np.random.randint(0, numx, 2)
        randspin = spins[randrow][randcol]
        energy = 0
        if randrow == 0:
            energy += -randspin*spins[randrow + 1][randcol]
        if randrow == numx - 1:
            energy += -randspin*spins[randrow - 1][randcol]
        if randcol == 0:
            energy += -randspin*spins[randrow][randcol + 1]
        if randcol == numy - 1:
            energy += -randspin*spins[randrow][randcol - 1]
        if randrow != (numx - 1) and randrow != 0:
            if randcol != (numy - 1) and randcol != 0:
                energy += -randspin*spins[randrow + 1][randcol]
                energy += -randspin*spins[randrow - 1][randcol]
                energy += -randspin*spins[randrow][randcol + 1]
                energy += -randspin*spins[randrow][randcol - 1]
        energy += -B * randspin
        if randspin == -1:
            p_down = np.exp(-energy / T) / (np.exp(-energy / T) + np.exp(energy / T))
            p_up = np.exp(energy / T) / (np.exp(-energy / T) + np.exp(energy / T)) 
        if randspin == 1:
            p_up = np.exp(-energy / T) / (np.exp(-energy / T) + np.exp(energy / T))
            p_down = np.exp(energy / T) / (np.exp(-energy / T) + np.exp(energy / T))
        spins[randrow][randcol] = np.random.choice([-1, 1], p=[p_down, p_up])
        
    return(np.sum(spins)/(numx*numy))
    
B_vals = np.linspace(-10, 10, 50)
T_vals = [0.1, 5, 10]

for T in T_vals:
    sums = []
    for B in B_vals:
        sums.append(spin_calc(1000, 10, 10, T, B))
    plt.plot(B_vals, sums, label='Temp: {}'.format(T))
plt.title('Normalized sum of Spins vs. Magnetic Field Strength')
plt.ylabel('Normalized Sum of Spins')
plt.xlabel('Magnetic Field Strength')
plt.legend()
    
