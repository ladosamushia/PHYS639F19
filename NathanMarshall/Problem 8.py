# -*- coding: utf-8 -*-
"""
Created on Wed Aug 28 12:39:03 2019
Nathan Marshall

Solution to Project Euler Problem 8
"""
#%%
num = ('73167176531330624919225119674426574742355349194934'
       '96983520312774506326239578318016984801869478851843'
       '85861560789112949495459501737958331952853208805511'
       '12540698747158523863050715693290963295227443043557'
       '66896648950445244523161731856403098711121722383113'
       '62229893423380308135336276614282806444486645238749'
       '30358907296290491560440772390713810515859307960866'
       '70172427121883998797908792274921901699720888093776'
       '65727333001053367881220235421809751254540594752243'
       '52584907711670556013604839586446706324415722155397'
       '53697817977846174064955149290862569321978468622482'
       '83972241375657056057490261407972968652414535100474'
       '82166370484403199890008895243450658541227588666881'
       '16427171479924442928230863465674813919123162824586'
       '17866458359124566529476545682848912883142607690042'
       '24219022671055626321111109370544217506941658960408'
       '07198403850962455444362981230987879927244284909188'
       '84580156166097919133875499200524063689912560717606'
       '05886116467109405077541002256983155200055935729725'
       '71636269561882670428252483600823257530420752963450')
#representing the large number of interest as a string
start = 0 #index to start slicing at
stop = 13 #index to end slicing at
combos = [] #list to store all 13 digit numbers
products = [] #list to store the products of the 13 digit numbers

while stop <= len(num): #cut number into all consecutive 13 digit numbers
    combos.append(num[start:stop])
    start += 1 #incrementing the start and stop indices
    stop += 1

for string in combos: #compute product of all digits in the 13 digit numbers
    product = 1 #the product is initially set to 1
    for i in string: 
        product = product * int(i) #convert each string digit to int for math
    products.append(product) #add the product to the list

ctr = 0 #counter variable to be incremented each time through loop
for i in products:
    if i == max(products): #searching for index of the maximum value
        break #break from loop when the max is found
    ctr += 1 #increment counter
print('The maximum product formed by 13 consecutive numbers in the 1000'
      '-digit number is', max(products), 'from the numbers', combos[ctr])    
    
        
