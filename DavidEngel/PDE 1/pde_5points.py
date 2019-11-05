# -*- coding: utf-8 -*-
"""
Created on Thu Oct 31 13:54:19 2019

@author: David Engel
The point of this code is to calculate the LaPlace equation of 5 points, an 
inner point of -1 surrounded by 4 points of +1
"""

#import necessary code
import numpy as np
import matplotlib.pyplot as plt 
import matplotlib.animation as animation
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
#sets edge values
sheet[0,:]=0.0
sheet[99,:]=0.0
sheet[:,0]=0.0
sheet[:,99]=0.0
#sets point values
sheet[49,49]=-1.0
sheet[49,54]=1.0
sheet[49,44]=1.0
sheet[44,49]=1.0
sheet[54,49]=1.0
#plots initial values
inital=np.copy(sheet)
plt.figure(1)
plt.imshow(inital) 

#intial time
t=0
#final time
tf=1000
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
            #keeps edges constant            
            sheet[0,:]=0.0
            sheet[99,:]=0.0
            sheet[:,0]=0.0
            sheet[:,99]=0.0
            #keeps points constant
            sheet[49,49]=-1.0
            sheet[49,54]=1.0
            sheet[49,44]=1.0
            sheet[44,49]=1.0
            sheet[54,49]=1.0

            #counts for row
            mc+=1
        #counts for column
        nc+=1 
    #counts for interations
    t+=1
    
#list for a plot
zi=0
zl=[]
while zi < z:
    zl.append(zi)
    zi+=1
#plots final plot
plt.figure(2)
plt.imshow(sheet) 
#plot of log of the absolute values
plt.figure(3)
plt.imshow(np.log(np.abs(sheet)))
#one 2D plot of one column
plt.figure(4)
plt.plot(zl,sheet[49,:])