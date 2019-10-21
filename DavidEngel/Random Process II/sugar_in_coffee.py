# -*- coding: utf-8 -*-
"""
Created on Thu Oct 10 14:16:50 2019

@author: David Engel
The point of this program is to simulate sugar spreading out throughout a solution
and plotting the entropy associated with it. There are 100 particles. The box is
40 by 40.
"""

#from mpl_toolkits import mplot3d


import numpy as np
import matplotlib.pyplot as plt
#from matplotlib import animation

num_sugar=100
#the number of sugar particles



ti=0
#inital time
tf=100
#final time
time=[ti]
#list for time
nt=0
#a counter value for time
y=0
x=0
#inital position of particles
xplt=[]
yplt=[]
#list for paticles position at a specific instant
xpos=[]
ypos=[]
#lists for all postions in time
box_size=20
#bos size
box=21
#the siaze of the box +1
m=0
for i in range(num_sugar):
    xplt.append(0)
    yplt.append(0)
    m+=1
#fills inital values with 0
xpos.append(xplt)
ypos.append(yplt)
#stores inital positions
xps=[]
yps=[]
#lists for entropy for x and y
s=[]
#list for entropy
for i in range(2*box_size):
    xps.append(0)
    yps.append(0)
    s.append(0)
#fills entropy lists
p=1.0/(40*40)
si=-(p)*np.log(p)
st=[si]
while ti<tf:
#loop for time
    n_p=0
    
    for i in range(num_sugar): 
        x=xplt[n_p]
        y=yplt[n_p]
        stepy=np.random.choice([-1,0,1],p=[0.4,0.2,0.4])
        stepx=np.random.choice([-1,0,1],p=[0.4,0.2,0.4])
        #loop that changes each particles position
        x+=stepx
        if x==box or x==-box:
            x-=stepx
        #bounces partlcle of box sides
        y+=stepy
        
        if y==box or y==-box:
            y+=-stepy
        #bounces particles of box
        xplt[n_p]=x
        yplt[n_p]=y
        #updates list for position
        n_p+=1
        #counter
    
    n=0
    while n<=99:
        #loop to count particles in each box
        ls=-box_size
        while ls<box_size:
        
            if ls==xplt[n]:
                xps[ls+20]+=1
            if ls==yplt[n]:
                yps[ls+20]+=1
            ls+=1
        n+=1
    n=0
    #entropy loop
    for i in range(40):
        m=0
        for i in range(40):
            sp=xps[n]*xps[m]*1.0
            s.append((p**sp)*(np.log(1/p)))
            m+=1
        n+=1
    #list for total entropy
    st.append(sum(s,0))       
    xpos.append(xplt)
    ypos.append(yplt)    
    time.append(ti)    
    ti+=1
    
#plot for position
plt.figure(1)
plt.title('Final Position of particles')
plt.xlabel('X')
plt.ylabel('Y')
plt.plot(xplt,yplt, 'o', color='blue') 

#plot for entropy vs time
plt.figure(2)
plt.plot(time,st)
plt.title('Entropy')
plt.xlabel('Time')
plt.ylabel('Etropy')

