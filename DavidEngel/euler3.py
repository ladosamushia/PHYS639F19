# -*- coding: utf-8 -*-
"""
Created on Mon Sep 02 21:21:28 2019

@author: Vandi

this doesn't work
"""
import numpy as np 
number = 600851475143

maximum = round(number**(1/2))


def isprime(number):
    prime = True
    for i in range(2, int(number**(1/2))): 
        if number % i == 0: 
            prime = False
            break
    return(prime) 


factors = []
for i in range(2, maximum+1): 
    if number % i == 0:
        factors.append(i)
        factors.append(int(number/i))
      
factors = np.sort(factors)[::-1] 
for i in factors: 
    if isprime(i) == True:  
        print(i, 'is the largest prime factor of', number)
        break   