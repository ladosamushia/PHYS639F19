# -*- coding: utf-8 -*-
"""
Created on Mon Sep 16 21:55:37 2019

PHYS 639 >>> Assignments >>> Week 4 >>> ODE I
HUYNH LAM

"""
#%%#============================================================================================================================
#=========== Week 4 >> Radioactive decay                                                                            ============
# Solve the following radioactive decay problems:                                                                   ============
# (T1) Substance A radioactively decays following dN/dt = − N/λ                                                     ============
# (T1-T3) Substance A decays into substance B which also eventually decays into other substances                    ============
# dNA/dt = − N_A/λ_A, dN_B/dt = − N_B/λ_B + N_A/λ_A.                                                                ============
# (T1-T3) Substances A and B decay into each: dN_A/dt = − N_A/λ_A + N_B/λ_B; dN_B/dt = − N_B/λ_B + N_A/λ_A.         ============
#===============================================================================================================================

# Import libraries
import numpy as np #math library
import matplotlib.pyplot as plt # Plotting library

#===============================================================================================================================
# Function to solve first order ODE 
# It takes in the intial conditions (x0,f0), the upper limit of the range you want to solve your ODE (high),
# number of steps (Nsteps) and function that defines the first derivative of the original functions (dfdxA, dfdxB)
# and the decay constants of substances A and B (lmdaA, lmdaB)
# It gives out the numerically estimated function fxA(t), fxB(t) that satisfies the conditions

def solve_first_order_ode(x0, f0, high, Nsteps, dfdxA, dfdxB, lmdaA, lmdaB):
    # Initialize array with discrete values of x
    t = np.linspace(x0,high,Nsteps+1)
    # Initialize array to store the solution of f(x)
    fxA = np.zeros(len(t))
    fxB = np.zeros(len(t))
    # step size
    dt = (high - x0)/Nsteps
    # First value of (x,fx) is the initial condition
    fxA[0] = f0
    fxB[0] = 0
    t[0] = x0
    # Euler's method to estimate the solution f(x)
    # First calculate the derivative then use the derivative
    # and then use this value of derivative and value of function at the previous point to estimate the next point
    for i in range(Nsteps):
        derivativeA = dfdxA(t[i], fxA[i], lmdaA, lmdaB, fxB[i])
        fxA[i+1] = fxA[i] + derivativeA*dt
        derivativeB = dfdxB(t[i], fxB[i], lmdaA, lmdaB, fxA[i])
        fxB[i+1] = fxB[i] + derivativeB*dt
        #print(i,derivativeA,derivativeB,len(x),fxA[i+1])
    #return x, fxA
    return t, fxA, fxB
#===============================================================================================================================
# Decay constants of substances A and B 
lmdaA = 1
lmdaB = 2

#===============================================================================================================================
# Derivative (Decay rate) as a function of x (time) and fx (number of particles)
# Substance A radioactively decays following dN/dt = − N/λ
def dAdt0(x, fxA, lmdaA, lmdaB, fxB):
    return -fxA/lmdaA
def dBdt0(x, fxB, lmdaA, lmdaB, fxA):
    return 0

t0,fxA0, fxB0 = solve_first_order_ode(0, 15, 15, 1000, dAdt0, dBdt0, 0.5*lmdaA, lmdaB)
plt.plot(t0,fxA0,'g', linewidth = 2, label = 'Case I: $N_A$, $\lambda_A$ = %.1f' %(0.5*lmdaA))
plt.legend()
plt.show()

#===============================================================================================================================
# Substance A decays into substance B which also eventually decays into other substances
def dAdt(x, fxA, lmdaA, lmdaB, fxB):
    return -fxA/lmdaA
def dBdt(x, fxB, lmdaA, lmdaB, fxA):
    return -fxB/lmdaB + fxA/lmdaA
    
t,fxA, fxB = solve_first_order_ode(0, 15, 15, 1000, dAdt, dBdt, lmdaA, 0.5*lmdaB)
plt.plot(t,fxA,'k', label = 'Case II: $N_A$, $\lambda_A$ = %.1f, $\lambda_B$ = %.1f' %(lmdaA,lmdaB))
plt.plot(t,fxB,'r', label = 'Case II: $N_B$, $\lambda_A$ = %.1f, $\lambda_B$ = %.1f' %(lmdaA,lmdaB))
plt.legend()
plt.show()

#===============================================================================================================================
# Substances A and B decay into each: dN_A/dt = − N_A/λ_A + N_B/λ_B; dN_B/dt = − N_B/λ_B + N_A/λ_A.
def dAdt2(x, fxA, lmdaA, lmdaB, fxB):
    return -fxA/lmdaA + fxB/lmdaB
def dBdt2(x, fxB, lmdaA, lmdaB, fxA):
    return -fxB/lmdaB + fxA/lmdaA

t2,fxA2, fxB2 = solve_first_order_ode(0, 15, 15, 1000, dAdt2, dBdt2, lmdaA, 0.5*lmdaB)
plt.plot(t2,fxA2,'k', linestyle='dashed', label = 'Case III: $N_A$, $\lambda_A$ = %.1f, $\lambda_B$ = %.1f' %(lmdaA,0.5*lmdaB))
plt.plot(t2,fxB2,'r', linestyle='dotted', label = 'Case III: $N_B$, $\lambda_A$ = %.1f, $\lambda_B$ = %.1f' %(lmdaA,0.5*lmdaB))
plt.legend()
plt.show()

