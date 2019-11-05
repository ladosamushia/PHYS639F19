# -*- coding: utf-8 -*-
"""
Created on Tue Oct 29 14:15:21 2019

@author: David Engel
The point of this code is to caluculate the LaPlace equation for two charged
plates.
"""
#import necessary code
import numpy as np
import matplotlib.pyplot as plt 

#size of matix
z=100
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
#sets edges to zero
sheet[0,:]=0.0
sheet[99,:]=0.0
sheet[:,0]=0.0
sheet[:,99]=0.0
#sets plates to -1 and +1
sheet[15:84,44]=-1.0
sheet[15:84,54]=1.0

#displays inital graph
inital=np.copy(sheet)
plt.figure(1)
plt.imshow(inital) 
#intial time
t=0
#final time
tf=500
#loop to perform the calculations
while t<=tf: 
    nc=0
    mc=0
    #loop to go through cloums
    while nc<=z-1:
        mc=0
        #loop to go through rows
        while mc<=z-1:
            #adjusts for elements not in the matrix
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
            #calculates the values
            sheet[nc,mc]=.25*(sheet[nc,mcu]+sheet[nc,mcd]+sheet[ncu,mc]+sheet[ncd,mc])
            #keeps edge values constant            
            sheet[0,:]=1.0
            sheet[99,:]=1.0
            sheet[:,0]=1.0
            sheet[:,99]=1.0
            sheet[0,:]=0.0
            sheet[99,:]=0.0
            sheet[:,0]=0.0
            sheet[:,99]=0.0
            #keeps plates constant
            sheet[15:84,44]=-1.0
            sheet[15:84,54]=1.0

            #counts for row
            mc+=1
        #counts for column
        nc+=1 
    #counts for interations
    t+=1
#plots final graph
plt.figure(2)
plt.imshow(sheet)   