# -*- coding: utf-8 -*-
"""
Created on Tue Nov 12 13:19:48 2019

@author: David Engel
"""
import numpy as np
import matplotlib.pyplot as plt 

l=1
xsteps=100
x=np.linspace(0,l,xsteps)
dx=1.0/xsteps

psi=[]
dpsi=[]
ddpsi=[]
for i in range(xsteps):
    psi.append(0)
    dpsi.append(0)
    ddpsi.append(0)
E=0
dE=.01
psi[xsteps-1]=.0001
dpsi[0]=1

while psi[xsteps-1]>0:
    for i in range(xsteps):
        ddpsi[i]=-E*psi[i]
    n=0
    while n<=xsteps-2:
        dpsi[n+1]=dpsi[n]+ddpsi[n]*dx
        psi[n+1]=psi[n]+dpsi[n]*dx
        n+=1
    E+=dE
E1=np.copy(psi)
plt.figure(1)
plt.plot(x,E1)
print E

E+=dE
while psi[xsteps-1]<0:
    for i in range(xsteps):
        ddpsi[i]=-E*psi[i]
    n=0
    while n<=xsteps-2:
        dpsi[n+1]=dpsi[n]+ddpsi[n]*dx
        psi[n+1]=psi[n]+dpsi[n]*dx
        n+=1
    E+=dE
E2=np.copy(psi)
plt.figure(2)
plt.plot(x,E2)
print E

E+=dE
while psi[xsteps-1]>0:
    for i in range(xsteps):
        ddpsi[i]=-E*psi[i]
    n=0
    while n<=xsteps-2:
        dpsi[n+1]=dpsi[n]+ddpsi[n]*dx
        psi[n+1]=psi[n]+dpsi[n]*dx
        n+=1
    E+=dE
E3=np.copy(psi)
plt.figure(3)
plt.plot(x,E3)
print E 
E+=dE

while psi[xsteps-1]<0.01:
    for i in range(xsteps):
        ddpsi[i]=-E*psi[i]
    n=0
    while n<=xsteps-2:
        dpsi[n+1]=dpsi[n]+ddpsi[n]*dx
        psi[n+1]=psi[n]+dpsi[n]*dx
        n+=1
    E+=dE
    
E4=np.copy(psi)
plt.figure(4)
plt.plot(x,E4)
print E

#E+=dE
#while psi[99]>0:
#    for i in range(xsteps):
#        ddpsi[i]=-E*psi[i]
#    n=0
#    while n<=xsteps-2:
#        dpsi[n+1]=dpsi[n]+ddpsi[n]*dx
#        psi[n+1]=psi[n]+dpsi[n]*dx
#        n+=1
#    E+=dE
#E5=np.copy(psi)
#plt.figure(5)
#plt.plot(x,E5)
#print E
#    
#    
    
    
    
    
    