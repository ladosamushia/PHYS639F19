# -*- coding: utf-8 -*-
"""
Created on Tue Aug 27 15:03:09 2019
Nathan Marshall

Solution to Project Euler Problem 5
"""
#%% 
def divis(num):
    '''Check for the given divisibilty requirement'''
    result = True
    for i in [11, 13, 14, 16, 17, 18, 19]: #a carefully chosen list of factors
        if num % i != 0 : #if the number isn't divisble by i, return False
            result = False
            break
    return(result) #return true if it is divisible by all numbers in the list

num = 20 #The number to be tested
while divis(num) == False: #testing numbers at intervals of 20
    num += 20

print('The smallest number divisible by all the numbers 1-20 is', num)