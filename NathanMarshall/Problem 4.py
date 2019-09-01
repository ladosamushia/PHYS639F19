# -*- coding: utf-8 -*-
"""
Created on Tue Aug 27 14:39:38 2019
Nathan Marshall

Solution to Project Euler Problem 4
"""
#%%
def palindrome(num):
    '''Detect a palindromic number.'''
    num = str(num) #represent number as a string
    if num == num[::-1]: #if the reverse of the string is the same,
        result = True    #it is a palindrome
    else:
        result = False
    return(result) #result is true if palindrome, false if not

pals = [] #list for containing palindromes
for i in range(100**2, 999**2 + 1): #range of possible numbers
    if palindrome(i) == True: #if the number is palindrome, add it to pals
        pals.append(i)
        
pals = pals[::-1] #put palindromes in descending order
found = False #This will be set to true if the numbers of interest are found
for i in pals:
    for x in range(999, 99, -1): #range of all three digit numbers max to min
        if i % x == 0: #if the palindrome is divisible:
            if len(str(int(i/x))) == 3: #if the result of division is 3-digit:
                pal = i #the palindrome of interest
                fac1 = x #the first 3-digit factor of pal
                fac2 = int(pal/fac1) #the second 3-digit factor of pal
                found = True #set found to True to break out of the loops
                print('The largest palindrome formed by multiplying two three-'
                      'digit numbers is', fac1, '*', fac2, '=', pal)
                break
    if found == True:
        break