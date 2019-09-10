# -*- coding: utf-8 -*-
"""
Created on Tue Sep  3 13:24:49 2019

PHYS 639 >>> Assignments >>> Warmup II
HUYNH LAM

"""
#%% ################################################################################### 
# Week 2 >> Problem 2 >> Find minimum of a 2D function. ###############################
#######################################################################################
# In this problem, the function is supposed to be smooth and has only one minimum
# We will start from a initial test point and move along the direction of decreasing value based on gradient (first derivative)
# It will converge to the closest minimum
# If the function has more than one minimum, the finder can get trapped in a local minimum and cannot get out

# import libraries
import numpy as np
import matplotlib.pyplot as plt 

# Initial guess
x0 = 2
y0 = 2
# Step size
delta = 0.0001
 
# Define the function fxy = f(x,y)
def fxy(x,y):
     function = np.exp((x+2)**2)*np.exp((y-4)**2);
     #function = (x-2)**2*(y-3)**2-1;
     return function

# Initialize values for the first order derivatives
f_dev_x = 1
f_dev_y = 1

# I created this to trace the path that the function has moved along the surface
x_path = []
y_path = []
z_path = []

while f_dev_x > 0 or f_dev_y > 0 :
    x_path.append(x0)
    y_path.append(y0)
    z_path.append(fxy(x0,y0))

    # First derivative
    f_dev_x = (fxy(x0+delta,y0)-fxy(x0-delta,y0))/(2*delta)
    f_dev_y = (fxy(x0,y0+delta)-fxy(x0,y0-delta))/(2*delta)
    
    # Moving the test point in the direction of decreasing function value based on the calculated gradient
    if f_dev_x < 0:
        x0 = x0 + delta
    elif f_dev_x > 0:
        x0 = x0 - delta
    else:
        x0 = x0
    if f_dev_y < 0:
        y0 = y0 + delta
    elif f_dev_y > 0:
        y0 = y0 - delta
    else:
        y0 = y0
    
print("The minimum appears at:")    
print("x = ",x0,", y = ",y0,", f(x,y) = ",fxy(x0,y0))
plt.plot(x_path, y_path, color='green', linestyle='dashed', linewidth = 1, marker='o', markerfacecolor='blue', markersize=2) 

#ax = plt.axes(projection='3d')
#ax.scatter3D(x_path, y_path, z_path, c=z_path, cmap='Greens');

##### Some test cases
# f(x,y) = e^(x^2)*e^((y-4)^2) >>> Minimum at x =  2.0395168301608202e-13 , y =  4.000000000004221 , f(x,y) =  1.0
# f(x,y) = e^((x+2)^2)*e^((y-4)^2) >>> Minimum at x0 =  -1.999999999999592 , y0 =  4.000000000004221 , f(x,y) =  1.0

##### Cautions
# If the function has more than one minimum, the finder can get trapped in a local minimum and cannot get out
# The step size might not be good enough to sample the given function
# Once need to be careful and check the convergence of their calculation