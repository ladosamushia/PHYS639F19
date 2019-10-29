# -*- coding: utf-8 -*-
"""
Created on Tue Oct 22 13:04:34 2019

@author: David Engel
This code creates a matirx with spin states and changes them by with a 50/50 
probabiltity for either state
"""
#import necessary code
import numpy as np
import matplotlib.pyplot as plt 
import matplotlib.animation as animation
#size of matic
z=100
#temperature
t=.1
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
   
    #changes values based off of probabilities
    sheet[nc,mc]=np.random.choice([-1, 1],p=[.5,.5])


    #for animation
    matrice.set_array(sheet)
    return[matrice]
    

#animates the matix
ani = animation.FuncAnimation(fig, update, frames=100, interval=5)
#shows the matrix
plt.show()