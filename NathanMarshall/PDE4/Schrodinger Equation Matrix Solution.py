# -*- coding: utf-8 -*-
"""
Created on Fri Nov 22 20:18:13 2019
Nathan Marshall

Solving 1D Schrodinger equation for the Lennard-Jones potential using
the finite differences matrix method.
"""
#%%
import numpy as np
import matplotlib.pyplot as plt

num = 1000 #matrix dimension

t = np.zeros((num, num)) #kinetic energy matrix
v = np.zeros((num, num)) #potential energy matrix
x = np.linspace(0.5, 3, num) #x array
dx = x[1]-x[0] #step size
u = 1/x**12 - 30/x**6 #Lennard Jones potential function

for i in range(0, num): #setting values of kinetic and potential energy
    for j in range(0, num):
        if i == j:
            t[i][j] = -2
            v[i][j] = u[i]
        if i == j - 1:
            t[i][j] = 1
        if j == i - 1:
            t[i][j] = 1

h = -t/(2*dx**2) + v #hamiltonian matrix

eigs, vecs = np.linalg.eig(h) #finding eigenvalues and eigenvectors of h
z = np.argsort(eigs) #z stores the indices required to sort the matrix
z = z[0:2] #look at just the first two solutions

for i in z: #plot the solutions that we found
    y = vecs[:,i] #eigenvectors are stored in columns of vecs matrix
    y = y / np.sqrt(np.trapz(y**2, dx=dx)) #normalize the wavefunction
    plt.plot(x, y) #plot the wavefunction
    
plt.plot(x, u/120, linestyle='dashed', label='Potential')
plt.ylim(-3, 3)
plt.title('Schrödinger Equation Lennard-Jones Potential')
plt.xlabel('x')
plt.ylabel(r'$\psi(x)$')
plt.legend()