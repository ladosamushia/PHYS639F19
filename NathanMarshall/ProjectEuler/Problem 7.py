# -*- coding: utf-8 -*-
"""
Created on Tue Aug 27 15:30:14 2019
Nathan Marshall

Solution to Project Euler Problem 7
"""
#%%
def primefind(num, primes):
    '''
    Updated prime number finder. Checks divisibility of a number by a list
    of prime numbers up to its square root. If it is not divisible by any
    of the prime numbers, True is returned. If it is divisible by one of the
    numbers, False is returned.
    '''
    prime = True
    sqrtmax = round((num)**(1/2))
    for i in primes:
        if i > sqrtmax:
            break
        if num % i == 0:
            prime = False
            break
    return(prime)

primes = [2] #list for storing primes, starting with two
num = 3 #number to check, starting with 3

while len(primes) != 10001: #generate primes up to the 10001st
    if primefind(num, primes) == True:
        primes.append(num)
    num += 2 #incrementing by two to avoid testing any even number
print('The 10001st prime number is', primes[-1]) #display the 10001st