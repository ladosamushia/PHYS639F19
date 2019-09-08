# -*- coding: utf-8 -*-
"""
Created on Tue Sep  3 13:21:36 2019

@author: alecc
"""
import numpy as np
def function(x): # test function
    return np.sin(x)
point = 0#point arount to 
step = .000001 #h
fplus = function(point+step)
fminus = function(point-step)
fprime = (fplus-fminus)/(2*step) #finite diference
print(fprime)
fdoubleprime = (fplus+fminus-2*function(point))/step**2 # just use def of finite difference second
print(fdoubleprime)