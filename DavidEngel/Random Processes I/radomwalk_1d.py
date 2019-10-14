# -*- coding: utf-8 -*-
"""
Created on Tue Oct 08 13:16:43 2019

@author: David Engel
"""
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 08 13:16:43 2019

@author: David Engel
The point of this program is to generate a random set and move in that direction
in 1D and graph the motion and the distance.
"""
#from mpl_toolkits import mplot3d

import numpy as np
import matplotlib.pyplot as plt

# the number of steps
num_steps=100
#list for final x values
finalx=[]

#inital time
t1=0
#final time
tf=100
#list for average distances
dista=[]

#while loop for different paths
while t1<tf:
    #inital x
    x=0
    #list for x values
    xplt=[x]
    #list for y values
    yplt=[y]
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
        #changing x value
        x+=stepx
        #counter
        n+=1
        #list of x values
        xplt.append(x)
        #list for time
        time.append(n)
        #list for distance
        d.append((x**2)**.5) 
    #plot for path
    plt.figure(2)
    plt.plot(time,xplt)
    plt.title('Paths')
    plt.xlabel('Time')
    plt.ylabel('Position X')
    #counter for time
    t1+=1
    #list of final x values
    finalx.append(x)
    #list of distances 
    dista.append(d)
    
#average the distances at each time instance
mean_dist=np.mean(dista, axis=0)
distn=mean_dist
#plot for average distance vers time
plt.figure(1)
plt.plot(time,distn)
plt.title('Average Distance')
plt.xlabel('Time')
plt.ylabel('Position')

#average final position
avex=(sum(finalx)/tf)


print 'Average Final Position'
print avex,avey