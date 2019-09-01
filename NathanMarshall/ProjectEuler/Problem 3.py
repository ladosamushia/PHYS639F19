# -*- coding: utf-8 -*-
"""
Created on Tue Aug 27 13:50:31 2019
Nathan Marshall

Solution to Project Euler Problem 3
"""
#%%
import numpy as np

num = 600851475143 #the number of interest
maximum = round(num**(1/2)) #the maximum number to detect factors of num up to

  
def isprime(num):
    '''Brute force algorithm for detecting primes.'''
    prime = True
    for i in range(2, int(num**(1/2))): 
        if num % i == 0: #if the number is divisible, it isn't prime
            prime = False
            break
    return(prime) #if the number isn't divisible up to its sqrt, it is prime
    
factors = []
for i in range(2, maximum+1): #finding factors of num up to its sqrt
    if num % i == 0:
        factors.append(i)
        factors.append(int(num/i))
        
factors = np.sort(factors)[::-1] #sorting factors from greatest to least
for i in factors: #looping through the factors
    if isprime(i) == True: #if a prime is detected, it is the largest 
        print(i, 'is the largest prime factor of', num)
        break   
