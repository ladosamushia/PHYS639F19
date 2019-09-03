# -*- coding: utf-8 -*-
"""
Created on Thu Aug 29 13:12:15 2019

@author: Vandi
solution to Euler Problem 1
"""

sum=0
for x in range(1, 1000):
        if x % 3==0 or x % 5==0: 
            sum += x
            
print(sum)
            