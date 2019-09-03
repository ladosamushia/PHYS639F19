# -*- coding: utf-8 -*-
"""
Created on Thu Aug 29 13:12:15 2019

@author: Vandi
"""

import numpy as np

upperbound=np.pi

lowerbound=0

number=1000

x=np.linspace(lowerbound, upperbound, number)

dx=(upperbound-lowerbound)/number

fx=np.sin(x)

integral = 0

for i in range (0,number-1):
    avg=(fx[i]+fx[i+1])/2
    integral += avg*dx
print (integral)