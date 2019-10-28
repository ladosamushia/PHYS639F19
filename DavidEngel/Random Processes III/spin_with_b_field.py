# -*- coding: utf-8 -*-
"""
Created on Mon Oct 28 13:03:25 2019


@author: David Engel
The point of this code is to simulate particles with spins flipping up or down 
based off of the spin of nearby particles and magnetic field.
"""
#import necessary code
import numpy as np
import matplotlib.pyplot as plt 
import matplotlib.animation as animation
#size of matic
z=100
#temperature
t=.1
#magnetic field
b=100
#creates the matrix with zeros
sheet=np.zeros((z,z))
#this fills the matrix with random values of 1 or -1
#counter for row
n=0
for i in range(z):
    #counter for columns
   m=0
   #loop to fill specific element 
   for i in range(z):
       sheet[n,m]=np.random.choice([-1,1],p=[0.5,0.5])
       m+=1
   n+=1    
#list for row and cloumn selection
length=[]
#makes a list based off of size z
for i in range(z):
        length.append(i)
#list for each row element probability
plength=[]
#makes a list of probability 1/z
for i in range(z):
    plength.append(1/(z*1.0))
#e
e=2.71
#needed for animation
fig, ax = plt.subplots()
#matrix for animation
matrice = ax.imshow(sheet, cmap='viridis',interpolation='none')
#function used in animation
def update(i):
    #selects a specific element to update
    nc=np.random.choice(length,p=plength)
    mc=np.random.choice(length,p=plength)
    #this deals with edges treats outside as same values as element    
    ncd=nc-1    
    if ncd==-1 :
        ncd=0
    ncu=nc+1    
    if ncu==z:
        ncu=z-1
    mcd=mc-1   
    if mcd==-1 :
        mcd=0
    mcu=mc+1  
    if mcu==z:
        mcu=z-1
    #this is to crate values campoaring each neighbor to selected element    
    #energy vales for each pair is calculated
    eu=sheet[nc,mc]*sheet[ncd,mc]
    
    ed=sheet[nc,mc]*sheet[ncu,mc]
    
    el=sheet[nc,mc]*sheet[nc,mcd]
    
    er=sheet[nc,mc]*sheet[nc,mcu]
    #magnetic componet
    bef=b*sheet[nc,mc]
    #total energy
    et=eu+ed+el+er+bef
    
    #exponates for probability calculation
    nprob=(e**(et/t))
    pprob=(e**(-et/t))
    #probablilites is element is =1
    if sheet[nc,mc]==1:
        pu=nprob/(nprob+pprob)
        pd=pprob/(nprob+pprob)
    #probabilities if element is -1
    if sheet[nc,mc]==-1:
        pu=pprob/(nprob+pprob)
        pd=nprob/(nprob+pprob)    
    #changes values based off of probabilities
    sheet[nc,mc]=np.random.choice([-1, 1],p=[pd,pu])


    #for animation
    matrice.set_array(sheet)
    return[matrice]
    

#animates the matix
ani = animation.FuncAnimation(fig, update, frames=100, interval=5)
#shows the matrix
plt.show()