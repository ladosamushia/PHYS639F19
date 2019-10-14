# -*- coding: utf-8 -*-
"""
Created on Tue Oct 08 13:16:43 2019

@author: David Engel
The point of this program is to generate a random set and move in that direction
in 3D and graph the motion and the distance.
"""
from mpl_toolkits import mplot3d

import numpy as np
import matplotlib.pyplot as plt

# the number of steps
num_steps=100
#list for final x values
finalx=[]
#list for final y values 
finaly=[]
#list for final z values 
finalz=[]
#inital time
t1=0
#final time
tf=100
#list for average distances
dista=[]
#for 3D plot
fig = plt.figure(1)
#code for 3D plot
ax = plt.axes(projection='3d')
#while loop for different paths
while t1<tf:
    #inital y
    y=0 
    #inital x
    x=0
    #inital xz
    z=0
    #list for x values
    xplt=[x]
    #list for y values
    yplt=[y]
    #list for z values
    zplt=[z]    
    #counter
    n=0
    #list for time
    time=[0]
    #list for distance
    d=[0]
    #loop for the calculating each individual path
    for i in range(num_steps): 
        #random step in x
        stepx=np.random.choice([-1,0,1],p=[0.4,0.2,0.4])
        #random step in y        
        stepy=np.random.choice([-1,0,1],p=[0.4,0.2,0.4])
        #random step in z        
        stepz=np.random.choice([-1,0,1],p=[0.4,0.2,0.4]) 
       #changing x value
        x+=stepx
        #changing y values        
        y+=stepy
        #changing z values        
        z+=stepz
        #counter
        n+=1
        #list of y values
        yplt.append(y)
        #list of x values
        xplt.append(x)
        #list for z vaules
        zplt.append(z)
        #list for time
        time.append(n)
        #list for distance
        d.append((x**2+y**2+z**2)**.5) 



    #counter for time
    t1+=1
    #list of final x values
    finalx.append(x)
    #list of final y values
    finaly.append(y)
    #list of distances 
    dista.append(d)
    plt.figure(1)
    #plot for paths
    plt.plot(xplt,yplt,zplt)
distn=[]


#plot for distance
plt.figure(2)
#calculates average distance at each y point
mean_dist=np.mean(dista, axis=0)
distn=mean_dist
plt.plot(time,distn)
plt.title('Random Walk')
plt.xlabel('Time')
plt.ylabel('Position')


avex=(sum(finalx)/tf)
avey=(sum(finaly)/tf)
avez=(sum(finalz)/tf)
print 'Average Final Position'
print avex,avey,avez