# -*- coding: utf-8 -*-
"""
Created on Sat Nov 23 19:12:23 2019
Nathan Marshall

Solving 1D Schrodinger equation for the square barrier using the finite 
differences matrix method.
"""
#%%
import numpy as np
import matplotlib.pyplot as plt

num = 1000 #matrix dimension

t = np.zeros((num, num)) #kinetic energy matrix
v = np.zeros((num, num)) #potential energy matrix
x = np.linspace(-1, 1, num) #x array
dx = x[1]-x[0] #step size
u = np.zeros(num) #potential energy array
u[400:600] = 20 #create a square barrier in the middle

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
z = z[0:2] #look at just the first few solutions

for i in z: #plot the solutions that we found
    y = vecs[:,i] #eigenvectors are stored in columns of vecs matrix
    y = y / np.sqrt(np.trapz(y**2, dx=dx)) #normalize the wavefunction
    plt.plot(x, y) #plot the wavefunction
    
plt.plot(x, u/20, linestyle='dashed', label='Potential') #plot the potential
plt.title('Schrödinger Equation Square Barrier')
plt.xlabel('x')
plt.ylabel(r'$\psi(x)$')
plt.legend()