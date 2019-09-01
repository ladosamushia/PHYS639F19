# -*- coding: utf-8 -*-
"""
Created on Tue Aug 27 13:42:27 2019
Nathan Marshall

Solution to Project Euler Problem 2
"""
#%%
fib = [1, 2] #seed to start creation of fibonnaci sequence
new = 0
while new <= 4000000: #generate fibonnaci sequence until new number exceeds max
    new = fib[-2] + fib[-1]
    if new <= 4000000:
        fib.append(new)
    else:
        pass
evens = [] #list to contain even fibonnaci numbers
for i in fib:
    if i % 2 == 0: #if the number is divisible by 2, add it to the list
        evens.append(i)
        
total = 0 #initially the sum is set to zero
for i in evens: #sum up all the even numbers
    total += i
print('The sum of the even Fibonacci numbers up to 4000000 is:', total) 
