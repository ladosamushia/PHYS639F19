# -*- coding: utf-8 -*-
"""
Created on Mon Sep  2 16:37:27 2019

PHYS 639 >>> Assignments >>> Warmup I
HUYNH LAM

"""
#%%
# 1. Get a GitHub account (see Syllabus).
# 2. Send me your GitHub username and accept my invitation.
# 3. Open a folder in the repo named "FirstnameSecondname"
# 4. Get a working version of python on your device (anaconda, spyder, .... let me know if you need help with this).
# 5. (T1) Finish the python tutorial (see the syllabus).
# 6. (T1) Find a python tutorial that you like online and go through it.
#%%
#######################################################################################
# 7. (T2-T3) Solve at least 5 Project Euler problems (https://projecteuler.net/). #####
#######################################################################################

#%% 
# Project Euler >> Problem 1 >> Multiples of 3 and 5
# Find the sum of all the multiples of 3 or 5 below 1000.

# I just run through all the the numbers using for loop
# Check if they are divisible by 3 or 5 and add to the sum

total = 0
for i in range(1,1000):
    if i%3==0 or i%5==0:
        total = total + i
print("the sum of all the multiples of 3 or 5 below 1000 is ",total)

# The answer is 233168

#%% 
# Project Euler >> Problem 2 >> Even Fibonacci numbers
# By considering the terms in the Fibonacci sequence whose values do not exceed four million,
# find the sum of the even-valued terms.

# We will store all the Fibonacci sequence in an array, start with the first two elements 0 and 1
# And address the number in this sequence by index i

fibonacci_sequence = [0,1]
i = 0

# Initilize the sum and the new Fibonacci number
fibonacci_number = 0
total = 0

# wile the Fibonacci number is smaller than 4 millions, we will keeep generating new number by adding the previous two in the sequence
# And check if the new number is even and less than 4 millions
# If yes, then add it to the sum

while fibonacci_number <= 4000000:
    fibonacci_number = fibonacci_sequence[i] + fibonacci_sequence[i+1]
    fibonacci_sequence.append(fibonacci_number)
    i += 1
    if fibonacci_number%2==0 and fibonacci_number <= 4000000:
        total = total + fibonacci_number

print("the sum of the even-valued terms is ", total)

# The answer is 4613732

#%% 
# Project Euler >> Problem 3 >> Largest prime factor
# What is the largest prime factor of the number 600851475143?

# I first write a function to find the "smallest prime factor" called "spf"
# It receive a number x and return the smallest prime factor of x
# For examples spf(2) = 2, spf(5) = 5, spf(6) = 2, spf(15) = 3
# Basically, it just run through a loop and return the first number that can be divided wholely by the input
# Interestingly, we don't need to check if i is a prime unmber or not since composite number can be decomposed into
# products of prime number through prime factorization

def spf (x):
    flag = "F"
    smallest_prime_factor = 0
    i = 1
    while flag == "F":
        i+=1
        if x%i==0:
            flag = "T"
            smallest_prime_factor = i
    return(smallest_prime_factor)

# Now we will use this function to do factorization and find the "largest prime factor" instead
# Everytime I find a "smallest prime factor", I will divide x with that factor and return the remainder
# Then repeating the loop until the "smallest prime factor" is the same as the "remainder"
# The remainder itself is now the "largest prime factor"
    
x = 600851475143
remainder = x
spf1 = 1
factorization = []

while spf1 != remainder and remainder != 1:
    spf1 = spf(remainder)
    factorization.append(spf1)
    remainder = remainder/spf1

print("Factorization ",factorization)
print("Largest prime factor",spf1)

# The answer is 6857

#%% 
# Project Euler >> Problem 5 >> Smallest multiple
# 2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
# What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

# I will look at multiples of 20 from smallest to largest
# and check whether that is divisible for other numbers from 2 to 19
# The program will stop and print out the smallest multiple of 20 that it found

# I create the counter i to keep track the multiples of 20

i = 0
biggest_number = 20

# And the condition_number to keep track how many numbers are divisible.
# Oviously, multiples of 20 are divisible of 1 and 20 so I start with condition_number = 2

condition_number = 2

# When condition_number is 20, the code will stop and print out the number
# It could be customized for 20 since multiple of 20 are also divisible by 2,4,5,10 to speed up the code few times
# but I want to keep it a bit more general

while condition_number != biggest_number:
    i+=1
    x = i*biggest_number #create multiple of 20
    condition_number = 2 #condition_number is set to 2 as beginning of checking any number
    for j in range(2,biggest_number): #check if x is divisible by 2 through 19
        if x%j==0:
            condition_number += 1 #Everytime x is divisible by j, condition number will be increased by 1
print("the number you are looking for is ",x)

# The answer is 232792560

#%% 
# Project Euler >> Problem 6 >> Sum square difference
# Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.

# I will run through all the number from 1 to 100 using for loop
# At each iteration, I will add the number i to sum_of_number which represents the sum of all number from 1 to 100
# And add i*i to sum_of_squares which represents The sum of the squares

sum_of_squares = 0
sum_of_numbers = 0

for i in range(1,101):
    sum_of_numbers += i
    sum_of_squares += i*i
    
# In the end, The square of the sum by multiplying sum_of_numbers by itself
# And the calculate the difference between the sum of the squares and the square of the sum.

square_of_sum = sum_of_numbers*sum_of_numbers
difference = square_of_sum - sum_of_squares

print("The difference between the sum of the squares and the square of the sum is ",difference)

# The answer is 25164150

#%%
#######################################################################################
# 8. (T1-T3) Write a  code that computes a definite integral. #########################
#######################################################################################

#%%
import numpy as np

# Limits of the integral
low = 0.0
high = np.pi
# Number of steps
num = 10000
# Constant interval array
x = np.linspace(low,high,num+1)  
# Digitized integrand
fx = x
    
# Step size
step = (high-low)/num   
# Approximate the integral by the sum
integral = 0
for i in range(num):
    integral += step*(fx[i]+fx[i+1])*0.5
print("The value of the integral is ",integral)

#### Some test cases
# Integral of sin(x) from 0 to pi with 1000 steps is 1.999998355065662
# The analytical result is 2.
# Integral of x from 0 to 5 with 1000 steps is 12.500000000000005
# The analytical result is 12.5.

#### Cautions
# The accuracy of this approximation depends on how the digitized integrand represents the "true" function
# The faster this "true" function varies, the smaller step needs to be used
# Once need to be careful and check the convergence of their calculation
# For example result from a fast oscilating function like sin(100x)^2 from 0 to pi varies greatly with step size
# With 100 steps: 3.0551484363618595e-28
# With 100 steps: 8.941079227588343e-28
# With 1000 steps: 1.570796326794894
# With 10000 steps: 1.5707963267948677
# >>> There is a huge jump from about 0 to 1.5 when we changed steps from 100 to 1000
# While a slow varying function like f[x] = x on the same range is much more stable
# With 100 steps: 4.934802200544679
# With 100 steps: 4.934802200544683
# With 1000 steps: 4.934802200544679
# With 10000 steps: 4.93480220054468

#%%
###################################################################################################
# 9. (T2-T3) Write a code that finds a global minimum of a function within a given interval. ######
###################################################################################################

#%%
import numpy as np

# Specify the interval
low = -5.0
high = 5.0
# Digitize the function
# Number of steps
num = 1000
# Constant interval array
x = np.linspace(low,high,num)  
# Digitized function
fx = x*x
# Initialize the minimum of this function to be the value at the first point
minimum = fx[0]
# Go through all the elements, if the element is smaller than min then set its value to be the new min
for i in range (num):
    if fx[i] < minimum:
        minimum = fx[i]
print(minimum)

#### Some test cases
# Minimum of sin(x) from 0 to 10 with 1000 steps is -0.9999972954811321
# The exact result is -1.
# Minimum of sin(x)^2 from 0 to 10 with 1000 steps is 0.0
# The exact result is 0.
# Minimum of x^2 from 0 to 10 with 1000 steps is 2.5050075100125133e-05
# The exact result is 0.

#### Cautions
# Same as previous problem. the accuracy of this approximation depends on how we sample the "true" function
# The faster this "true" function varies, the smaller step needs to be used
# Once need to be careful and check the convergence of their calculation


#%%
###################################################################################################
# 10. (T2-T3) Write a code that finds zeros of a function within a given interval. ################
###################################################################################################

#%%

# Specify the interval
low = 0
high = 3/2*np.pi
# Digitize the function
# Number of steps
num = 1000
# Constant interval array
x = np.linspace(low,high,num)  
# Digitized function
fx = np.sin(x)
# Initialize the minimum of this function to be the value at the first point
minimum = fx[0]
# Go through all the elements, if its product with the next element is less than or equal than 0
# The change of sign of two elements indicates zero crossings
# The calculation may produce zero products in both sides of the crossings,
# I use product_old to get rid of one of them since they indicate the same zero
product_old = 1
count = 0
for i in range (num-1):
    product = fx[i]*fx[i+1]
    if product <= 0 and product_old > 0:
        count += 1
        print(count,x[i],fx[i])
    product_old = product

#### Some test cases
# Function x from -5 to 5 with 1000 steps has 1 zero (x,y) = (-0.009999999999999787,-0.009999999999999787)
# The exact result is (x,y) = (0,0).
# Function x^2 from -5 to 5 with 1000 steps has 1 zero (x,y) = (-0.009999999999999787,9.999999999999574e-05)
# The exact result is (x,y) = (0,0).
# Function sin(x) from 0 to Pi/2 with 1000 steps has 2 zeros
# (x,y) = (0.0,0.0) and = (3.141592653589793,1.2246467991473532e-16)
# The exact result are (x,y) = (0,0) and (x,y) = (Pi,0).

#### Cautions
# Same as previous problem. the accuracy of this approximation depends on how we sample the "true" function
# For example,function sin(x) from 0 to Pi with 1000 steps shows only 1 zero (x,y) = (0,0)
# The truth is that it should have another zero at (x,y) = (Pi,0)
# x = Pi is not sample in the degitized function so the zero is missed.
# The faster this "true" function varies, the smaller step needs to be used
# Once need to be clear about their required accuracy, be careful and check the convergence of their calculation

#%%
###################################################################################################
############################################## THE END. ###########################################
###################################################################################################
















