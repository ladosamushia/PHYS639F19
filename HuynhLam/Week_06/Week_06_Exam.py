# -*- coding: utf-8 -*-
"""
Created on Thu Oct  3 13:14:53 2019

@author: Huynh Lam
"""

#%%======================================================================================================================================
#========================================================================================================================================
#========      Week 06 >> Modified harmonic potential                                                              =========================
#========      This code numerically solve for equation of motion of an object in amodified harmonic potential     =========================
#========      with cubic and quarubic terms V(x) = 1/2*k*x^2 + 1/3!*alpha*x^3 + 1/4!*beta*x^4.                    =========================
#===========================================================================================================================================
#===========================================================================================================================================

# Import libraries
import numpy as np #math library
import matplotlib.pyplot as plt # Plotting library

#===========================================================================================================================================
# Function to solve second order ODE 
# It takes in the intial conditions
##### Initial time ti        ##### Initial position xi              ##### Initial velocity vi     ##### Stiff constant "k"
##### Final time tf          ##### Number of steps Nsteps           ##### Constant to moify potential "alpha" (cubic), "beta" (quadrubic)
# It gives out the position as function of time (t,x)
#===========================================================================================================================================

def solve_second_order_ode(ti, tf, xi, vi, Nsteps, k, m, alpha, beta, acceleration):
    # Initialize array with discrete values of time
    t = np.linspace(ti,tf,Nsteps+1)
    # Initialize array to store the solution of x=x(t)
    x = np.zeros(len(t))
    # step size
    dt = (tf - ti)/Nsteps
    # First value of (t=ti,x=xi,v=vi) is the initial condition
    t[0] = ti
    x[0] = xi
    v = vi
    # Euler's method to estimate the solution f(x)
    # First calculate the second derivative then the first derivative
    # and then use this value of the first derivative and value of function at the previous point to estimate the next point
    for i in range(Nsteps):
        v = v + acceleration(k, m, alpha, beta,x[i])*dt
        x[i+1] = x[i] + v*dt
    return t, x , alpha, beta
#============================================================================================================================================
# Acceleration as a function of k, m, alpha and beta
def acceleration(k, m, alpha, beta,x):
    return -k/m*x - 1/2*alpha*x**2 - 1/6*beta*x**3
#============================================================================================================================================
# Constants and Coefficients
k = 1
m = 1
ti = 0
tf = 20
Nsteps = 1000
# Initial amplitude
xi = 1
# Initial velocity
vi = 2
# Angular frequency (in case of simple harmonic oscillator without external force)
w = np.sqrt(k/m)
#============================================================================================================================================
t1, x1, alpha1, beta1 = solve_second_order_ode(ti, tf, xi, vi, Nsteps, k, m, 0, 0, acceleration)
t2, x2, alpha2, beta2 = solve_second_order_ode(ti, tf, xi, vi, Nsteps, k, m, 0.1, 0, acceleration)
t3, x3, alpha3, beta3 = solve_second_order_ode(ti, tf, xi, vi, Nsteps, k, m, 0, 0.4, acceleration)
t4, x4, alpha4, beta4 = solve_second_order_ode(ti, tf, xi, vi, Nsteps, k, m, 0.1, 0.4, acceleration)
plt.plot(t1,x1, color = 'r', label = r'Case 1: k = %.1f m = %.1f $\alpha$ = %.1f $\beta$ = %.1f $x_i$ = %.1f $v_i$ = %.1f' %(k,m,alpha1,beta1,xi,vi))
plt.plot(t2,x2, color = 'g', label = r'Case 2: k = %.1f m = %.1f $\alpha$ = %.1f $\beta$ = %.1f $x_i$ = %.1f $v_i$ = %.1f' %(k,m,alpha2,beta2,xi,vi))
plt.plot(t3,x3, color = 'b', label = r'Case 3: k = %.1f m = %.1f $\alpha$ = %.1f $\beta$ = %.1f $x_i$ = %.1f $v_i$ = %.1f' %(k,m,alpha3,beta3,xi,vi))
plt.plot(t4,x4, color = 'k', label = r'Case 4: k = %.1f m = %.1f $\alpha$ = %.1f $\beta$ = %.1f $x_i$ = %.1f $v_i$ = %.1f' %(k,m,alpha4,beta4,xi,vi))
plt.legend()