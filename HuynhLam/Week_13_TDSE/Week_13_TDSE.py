# -*- coding: utf-8 -*-
"""
Created on Tue Nov 19 13:11:19 2019

@author: huynhlam
"""
#==================================================================================================================
# TDSE
# This code solve the TDSE equation for putting a gaussian wave-packet in various potential
# such as free particle, square well or barrier potential
#==================================================================================================================

#==================================================================================================================
# Import libraries
#==================================================================================================================
import numpy as np #math library
import matplotlib.pyplot as plt # Plotting library
#==================================================================================================================

#==================================================================================================================
# DEFINITION OF THE INITIAL GAUSSIAN WAVE-PACKET
#==================================================================================================================
# Space width
L = 0.2
# Number of steps in length
Nx = 1000
# Length step
dx = 1
# Number of steps in time
Nt = 80000
# Time step
dt = 0.005
# Temperature of the hot point
T = 1
# Center of the gaussian
xc = L/2.1
# Standard deviation
sigma = xc/100
# Momentum
# If you don't want the particle to move, set p to 0
p = 1000

def initial(xc,sigma):
    x0 = np.linspace(0,L,Nx)
    psiR0 = np.linspace(0,L,Nx)
    psiI0 = np.linspace(0,L,Nx)
    psi20 = np.linspace(0,L,Nx)
    for i in range(Nx):
        psiR0[i] = np.exp(-(x0[i]-xc)**2/(2*sigma**2))*np.cos(p*x0[i])
        psiI0[i] = np.exp(-(x0[i]-xc)**2/(2*sigma**2))*np.sin(p*x0[i])
        psi20[i] = psiR0[i]*psiR0[i] + psiI0[i]*psiI0[i]
    return x0, psiR0, psiI0, psi20
x0, psiR0, psiI0, psi20 = initial(xc,sigma)

plt.figure('Initial gaussian wave-packet')
plt.title('Initial gaussian wave-packet')
plt.plot(x0, psiR0, linestyle='--', marker='o', label = r'Re($\psi$)')
plt.plot(x0, psiI0, linestyle='--', marker='x', label = r'Im($\psi$)')
plt.plot(x0, psi20, linestyle='--', marker='.', label = r'$\psi^2$')
plt.legend()
#==================================================================================================================
# Definition of potential
#==================================================================================================================
# Free particle
def free(L,Nx):
    V = np.zeros(Nx)
    for i in range(Nx):
        V[i] = 0
    return V
# Barrier potential
def barrier(L,Nx):
    V = np.zeros(Nx)
    for i in range(Nx):
        if i/Nx*L > L/1.9 -L/200 and i/Nx*L < L/1.9 + L/200:
            V[i] = 0.1
    return V
# Square well potential
def well(L,Nx):
    V = np.zeros(Nx)
    for i in range(Nx):
        if i/Nx*L > xc + L/35 or i/Nx*L < xc - L/35:
            V[i] = 0.15
    return V
plt.figure('Choices of potential')
plt.title('Choices of potential')
plt.plot(x0, free(L,Nx), linestyle='--', label = 'Free (no potential)')
plt.plot(x0, barrier(L,Nx), linestyle='-', label = 'Barrier potential')
plt.plot(x0, well(L,Nx), linestyle=':', label = 'Square well potential')
plt.legend()

#==================================================================================================================
# SOLVING TDSE
#==================================================================================================================     
def TDSE(L,Nx,Nt,dt,T,xc,potential):
    
    # Potential
    if potential == 'free':
        V = free(L,Nx)
    elif potential == 'well':
        V = well(L,Nx)
    elif potential =='barrier':
        V = barrier(L,Nx)
    plt.plot(x0, V)
        
    # Array to store the time evolution of the wavefunction
    psiRt = np.zeros((Nx,Nt)) # Real part
    psiIt = np.zeros((Nx,Nt)) # Imaginary part
    psi2t = np.zeros((Nx,Nt)) # Psi^2
    dpsiR = np.zeros(Nx) # Derivative of the real part
    dpsiI = np.zeros(Nx) # Derivative of the imaginary part
    
    # Initial conditions
    psiRt[:,0] = psiR0
    psiIt[:,0] = psiI0
    
    print('Start solving TDSE equation')
    print('Progressing...')
    for t in range(1,Nt):
        if np.remainder(t,int(Nt/20)) == 0:
            print(t/Nt*100,'%')
        for i in range(1,Nx-1):
            dpsiR[i] = -(psiIt[i-1,t-1]+psiIt[i+1,t-1]-2*psiIt[i,t-1])/dx**2 + V[i]*psiIt[i,t-1]
            dpsiI[i] = (psiRt[i-1,t-1]+psiRt[i+1,t-1]-2*psiRt[i,t-1])/dx**2 - V[i]*psiRt[i,t-1]   
        psiRt[:,t] = psiRt[:,t-1] + dpsiR*dt
        psiIt[:,t] = psiIt[:,t-1] + dpsiI*dt

    print('Solving TDSE is done!')
    print('Calculating the modulus square of the wave-function...')
    for t in range(Nt):
        for i in range(Nx-1):        
            psi2t[i,t] = psiRt[i,t]**2+psiIt[i,t]**2
    print('Done!')
    
    return psiRt, psiIt, psi2t, V

#==================================================================================================================
# RUNNING AND TESTING THE TDSE CALCULATION
#================================================================================================================== 
# Last input is the potential, which can be 'free', 'barrier' or 'well'
psiRt, psiIt, psi2t, V = TDSE(L,Nx,Nt,dt,T,xc,'barrier')

print('Plot the results')

plt.figure('Modulus square of the wave-function')
plt.title('Modulus square of the wave-function')
plt.imshow((psi2t), aspect=50)

plt.figure('Snap shots of the wave-function at different time')
plt.title('Snap shots of the wave-function at different time')
plt.plot(x0, psi2t[:,0], x0, psi2t[:,int(Nt/2)], x0, psi2t[:,Nt-1], x0, V)
#plt.figure(1)
#plt.title('Modulus square of the wave-function')
#plt.imshow((psi2t)**(1/2), aspect=50)
