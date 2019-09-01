# -*- coding: utf-8 -*-
"""
Created on Tue Aug 27 15:21:30 2019
Nathan Marshall

Solution to Project Euler Problem 6
"""
#%%
sumsqr = 0
for i in range(1, 101): #for numbers 1-100, sum up their squares
    sumsqr += i**2

summed = 0
for i in range(1, 101): #sum all the numbers 1-100
    summed += i
sqrsum = summed**2 #square the sum of numbers 1-100
print('The difference in the squared sum and the sum of the squares of the'
      ' natural numbers 1-100 is', sqrsum, '-', sumsqr, '=', sqrsum-sumsqr)
#display the difference