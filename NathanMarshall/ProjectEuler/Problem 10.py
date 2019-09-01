# -*- coding: utf-8 -*-
"""
Created on Thu Aug 29 08:53:10 2019
Nathan Marshall

Solution to Project Euler Problem 10
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

primes = [2] #list to contain primes
num = 3 #current number to check if prime

while num < 2000000: #finding prime numbers up to 2000000
    if primefind(num, primes) == True:
        primes.append(num)
    num += 2 #incrementing number to be checked by two to avoid all evens
#printing the sum of all the prime numbers in the list
print('The sum of the prime numbers below two million is', sum(primes))
