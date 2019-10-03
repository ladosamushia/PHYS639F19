# -*- coding: utf-8 -*-
"""
Created on Thu Oct  3 13:08:03 2019
Nathan Marshall

Simulates two pendulums coupled by a spring. I assumed that the force from
the spring always points in the phi-hat direction of the pendulums.
"""
#%%
import numpy as np
import matplotlib.pyplot as plt

m1 = 1 #pendulum 1 mass in kg
m2 = 1 #pendulum 2 mass in kg
l1 = 1 #pendulum 1 length in m
l2 = 1 #pendulum 2 length in m
k = 1.5 #spring constant for coupling spring in N/m
g = 9.81 #acceleration of gravity in m/s^2

phi10 = 15 * np.pi/180 #initial angle pendulum 1 in degrees
phi20 = 0 * np.pi/180 #initial angle pendulum 2 in degrees
omega10 = 0 #initial angular velocity pendulum 1 in rad/sec
omega20 = 0 #initial angular velocity pendulum 2 in rad/sec
t0 = 0 #initial time
tmax = 20 #max time to stop simulation
dt = 0.001 #time step size

phi1 = [phi10] #list to contain angle 1 values
phi2 = [phi20] #list to contain angle 2 values
omega1 = [omega10] #list to contain angular velocities pendulum 1
omega2 = [omega20] #list to contain angular velocities pendulum 2 
t = [t0] #list to contain time values


def dphi1dt(phi1, phi2):
    '''Differential equation for pendulum 1.'''
    x1 = l1 * np.sin(phi1)
    x2 = l2 * np.sin(phi2)
    return(-1/(m1 * l1**2) * m1 * g * l1 * np.sin(phi1) + k*(x2 - x1))
    
def dphi2dt(phi1, phi2):
    '''Differential equation for pendulum 2.'''
    x1 = l1 * np.sin(phi1)
    x2 = l2 * np.sin(phi2)
    return(-1/(m2 * l2**2) * m2 * g * l2 * np.sin(phi2) + k*(x1 - x2))
    
def energy(phi1, phi2, omega1, omega2):
    '''Calculate total energy of the system. Should be constant with time.'''
    x1 = l1 * np.sin(phi1)
    x2 = l2 * np.sin(phi2)
    return(m1*g*l1*np.cos(phi1) + m2*g*l2*np.cos(phi2) + (1/2*k*(x2 - x1)**2)
            + 1/2*m1*(l1**2)*(omega1**2) + 1/2*m2*(l2**2)*(omega2**2) )
    
energies = [energy(phi10, phi20, omega10, omega20)] #list to contain energies
    
while t[-1] < tmax: #run simulation until the time exceeds maximum time
    phi1.append(phi1[-1] + omega1[-1] * dt)
    phi2.append(phi2[-1] + omega2[-1] * dt)
    
    omega1.append(omega1[-1] + dphi1dt(phi1[-1], phi2[-1]) * dt)
    omega2.append(omega2[-1] + dphi2dt(phi1[-1], phi2[-1]) * dt)
    
    energies.append(energy(phi1[-1], phi2[-1], omega1[-1], omega2[-1]))
    
    t.append(t[-1] + dt)
    

    
fig, [ax1, ax2] = plt.subplots(1, 2) #plot the results
fig.canvas.set_window_title('Coupled Pendulums')
ax1.plot(t, phi1)
ax1.set_xlabel('Time (s)')
ax1.set_ylabel(r'$\phi_1$ (rad)')
ax1.set_title('Pendulum 1 Angle vs. Time')

ax2.plot(t, phi2)
ax2.set_xlabel('Time (s)')
ax2.set_ylabel(r'$\phi_2$ (rad)')   
ax2.set_title('Pendulum 2 Angle vs. Time') 
    
    