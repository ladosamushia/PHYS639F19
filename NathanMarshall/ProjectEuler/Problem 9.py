# -*- coding: utf-8 -*-
"""
Created on Thu Aug 29 08:21:55 2019
Nathan Marshall

Solution to Project Euler Problem 9
"""
#%%
import numpy as np
sqrs = np.arange(1, 500)**2 #a list of perfect squares to test with
end = False #this will be set to True to break from multiple loops
start = 0 #index to start testing for triples at
for asqr in sqrs: #loop through all values in squares
    for bsqr in sqrs[start:]: #loop through values of squares starting at start
        if asqr + bsqr in sqrs: #if sum of squares is itself a square:
            a, b, c = np.sqrt([asqr, bsqr, asqr+bsqr]) #find the triple
            if a + b + c == 1000: #if the sum of the triple is 1000:
                end = True #break out of all the loops
                break
    if end == True:
        break   
    start += 1 #increment the start index for the bsqr loop
print('The Pythagorean triple whose sum a + b + c is equal to 1000 is',
      int(a), '+', int(b), '+', int(c), '=', int(a + b + c))
