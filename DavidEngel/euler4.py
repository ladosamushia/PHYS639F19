# -*- coding: utf-8 -*-
"""
Created on Mon Sep 02 21:49:30 2019

@author: Vandi
"""
   
def palindrome(number):
  
    number = str(number)
    
    if number == number[::-1]: 
        
       result = True    
    else:
        result = False
    return(result) 

pals = [] 
for i in range(100**2, 999**2 + 1): 
    if palindrome(i) == True: 
        pals.append(i)
        
pals = pals[::-1] 
found = False 
for i in pals:
    for x in range(999, 99, -1):
        if i % x == 0:
            if len(str(int(i/x))) == 3:
                pal = i
                fac1 = x
                fac2 = int(pal/fac1)
                found = True
                print'The largest palindrome formed by multiplying two three-'                      'digit numbers is', fac1, '*', fac2, '=', pal
                break
    if found == True:
        break