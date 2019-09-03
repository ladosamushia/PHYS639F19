# -*- coding: utf-8 -*-
"""
Created on Mon Sep 02 21:19:21 2019

@author: Vandi

solution to euler 2
"""

fibonaci = [1, 2] 

new = 0

while new <= 4000000: 
    new = fibonaci[-2] + fib[-1]
    if new <= 4000000:
        fibonaci.append(new)
    else:
        pass

evens = [] 

for i in fibonaci:
    if i % 2 == 0: 
        evens.append(i)
        
total = 0 

for i in evens: 
    total += i

print'The sum of the even Fibonacci numbers up to 4000000 is:', total