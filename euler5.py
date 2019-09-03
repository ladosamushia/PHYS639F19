# -*- coding: utf-8 -*-
"""
Created on Mon Sep 02 21:57:06 2019

@author: Vandi
"""

def divis(number):
    
    result = True
    for i in [11, 13, 14, 16, 17, 18, 19]:
        if number % i != 0 :
        
            result = False
            break
    return(result)

number = 20
while divis(number) == False:
    number += 20

print'The smallest number divisible by all the numbers 1 and 20 is', number