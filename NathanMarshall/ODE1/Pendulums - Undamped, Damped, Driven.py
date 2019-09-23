# -*- coding: utf-8 -*-
"""
Created on Thu Sep 19 13:21:53 2019
Nathan Marshall

This code numerically solves the differential equations for undamed, damped,
and damped-driven pendula. It also generates a plot of the frequency of an 
undamped pendulum as a function of the initial angle that it starts swinging
from.
""" 
#%% Integrate the Differential Equations to Find Pendulum Motion
import numpy as np
import matplotlib.pyplot as plt

g = 9.81 #acceleration in m/s^2
l = 5 #pendulum length in meters
k = np.sqrt(g/l)
dt = 0.001 #step size
t0 = 0 #initial condition for t
phi0 = 0.1 #initial condition for the solution curve f(x)
dfdt0 = 0 #initial condition for the derivative of phi
tmax = 10 #max value of t

def df2dt(phi):
    '''Define functional form of 2nd derivative df2/dt'''
    return(-k**2*np.sin(phi))

def integrate(phi0):
    '''Integrates differential equation from t0 to tmax.'''
    t = [t0] #list to contain t values
    phi = [phi0] #list to contain phi values
    dfdt = [dfdt0] #list to contain derivative values
    while t[-1] < tmax: #loop until our increment variable is greater than xmax
        phi.append(phi[-1] + dfdt[-1]*dt) #add df/dt * dt to previous phi
        dfdt.append(dfdt[-1] + df2dt(phi[-1]) * dt) #add df2/dt * dt to prev. df/dt
        t.append(t[-1] + dt) #add new t value to the list
    return(t, phi)
        
t, phi = integrate(phi0)
t_test = np.linspace(t0, tmax, 1000) #creating test case with analytical soln.
phi_test = dfdt0 / k * np.sin(k * t_test) + phi0 * np.cos(k * t_test)

plt.figure(1)
plt.plot(t, phi, label='Numerical Result') #plotting numerical result
plt.plot(t_test, phi_test, label='Analytical Result') #plotting test case
plt.title('Numerical vs. Analytical Pendulum Motion')
plt.xlabel('Time (s)')
plt.ylabel('Pendulum Angle (radians)')
plt.grid(True)
plt.legend()
#%% Find pendulum frequency as a function of initial angle
from scipy.signal import find_peaks #we will use this to find peaks
phi0s = np.linspace(0.01, 3, 25) #a range of initial angles
freqs = [] #list to contain frequencies
tmax = 30 #maximum time for integration

for phi0 in phi0s: #loop through every initial angle
    t, phi = integrate(phi0) #integrate the diff. eq. for each angle
    peaks = find_peaks(phi) #find the peaks of the solution curve
    period = t[peaks[0][1]] - t[peaks[0][0]] #subtract adjacent peaks to find period
    freq = 1/period #calculate frequency from period
    freqs.append(freq) #add frequency to list
    
plt.figure(2) #plot frequency vs. initial angle
plt.plot(phi0s, freqs)
plt.title('Frequency of Pendulum vs. Initial Angle')
plt.xlabel('Initial angle (radians)')
plt.ylabel(r'Frequency $(s^{-1})$')
#%% Damped pendulum motion

dt = 0.001 #step size
t0 = 0 #initial condition for t
phi0 = 0.1 #initial condition for the solution curve f(x)
dfdt0 = 0 #initial condition for the derivative of phi
tmax = 10 #max value of t
b = np.linspace(0, 0.8, 3) #range of damping constants

def damped(phi, dfdt, b):
    '''Define functional form of 2nd derivative df2/dt'''
    return -k**2*np.sin(phi) - b * dfdt

def integrate(phi0, b):
    '''Integrates differential equation from t0 to tmax.'''
    t = [t0] #list to contain t values
    phi = [phi0] #list to contain phi values
    dfdt = [dfdt0] #list to contain derivative values
    while t[-1] < tmax: #loop until our increment variable is greater than xmax
        phi.append(phi[-1] + dfdt[-1]*dt) #add df/dt * dt to previous phi
        dfdt.append(dfdt[-1] + damped(phi[-1], dfdt[-1], b) * dt) #add df2/dt * dt to prev. df/dt
        t.append(t[-1] + dt) #add new t value to the list
    return(t, phi)
        

plt.figure(3)

for bi in b:
    t, phi = integrate(phi0, bi)
    plt.plot(t, phi, label='Damping Constant = {}'.format(bi)) #plotting numerical result
plt.title('Damped Pendulum Motion')
plt.xlabel('Time (s)')
plt.ylabel('Pendulum Angle (radians)')
plt.grid(True)
plt.legend()
#%% Damped driven pendulum motion

dt = 0.001 #step size
t0 = 0 #initial condition for t
phi0 = 0.1 #initial condition for the solution curve f(x)
dfdt0 = 0 #initial condition for the derivative of phi
tmax = 20 #max value of t
b = 0.3

def damped_driven(phi, dfdt, F):
    '''Define functional form of 2nd derivative df2/dt'''
    return -k**2*np.sin(phi) - b * dfdt + F

def Ft(t):
    '''Driving force as a function of time'''
    return -np.cos(k*t)

def integrate(phi0):
    '''Integrates differential equation from t0 to tmax.'''
    t = [t0] #list to contain t values
    phi = [phi0] #list to contain phi values
    dfdt = [dfdt0] #list to contain derivative values
    while t[-1] < tmax: #loop until our increment variable is greater than xmax
        phi.append(phi[-1] + dfdt[-1]*dt) #add df/dt * dt to previous phi
        dfdt.append(dfdt[-1] + damped_driven(phi[-1], dfdt[-1], Ft(t[-1])) * dt) #add df2/dt * dt to prev. df/dt
        t.append(t[-1] + dt) #add new t value to the list
    return(t, phi)
        
t, phi = integrate(phi0)

plt.figure(4)
plt.plot(t, phi) #plotting numerical result
plt.title('Damped-Driven Pendulum Motion')
plt.xlabel('Time (s)')
plt.ylabel('Pendulum Angle (radians)')
plt.grid(True)