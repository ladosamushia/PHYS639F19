# -*- coding: utf-8 -*-
"""
Created on Thu Aug 29 14:01:24 2019

@author: Vandi
"""

import numpy as np

xmin=-10

xmax=10

num=10

x=np.linspace(xmin, xmax , num)

fx=x**2


maxfx=max(fx)
minfx=min(fx)
for i in range (0, num-1):
    if fx[i]==minfx:
        minx =x
         
    if fx[i]==maxfx:
        maxx =x
print(minx)
print(maxx)