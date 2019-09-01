# -*- coding: utf-8 -*-
"""
Created on Tue Aug 27 13:25:59 2019
Nathan Marshall

Solution to Project Euler Problem 1
"""
#%%
import numpy as np

mult3 = [] #lists to contain the multiples of 3 and 5
mult5 = []
for i in range(1, 1000): #loop through i values 1 to 999
    if i % 3 == 0: #if i is divisible by three, add to the proper list
        mult3.append(i)
    if i % 5 == 0: #if i is divisible by five, add to the proper list
        mult5.append(i)
        
both = np.concatenate((mult3, mult5)) #concatenate the lists of multiples
both = np.unique(both) #keep only the unique values in the concatenation

total = 0 #initially set total sum to 0
for i in both: #loop through all the multiples and sum them up
    total += i
print('The sum of the multiples of 3 or 5 up to 1000 is:', total) #display sum
