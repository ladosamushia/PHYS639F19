# -*- coding: utf-8 -*-
"""
Created on Thu Aug 29 13:52:29 2019

@author: Vandi
"""

# -*- coding: utf-8 -*-
"""
Created on Thu Aug 29 13:12:15 2019

@author: Vandi
"""

import numpy as np

upperbound=1

lowerbound=-1

number=10

x=np.linspace(lowerbound, upperbound, number)


fx=x


for i in range (0,number-1):
   if fx[i]*fx[i+1] <= 0:
       print(x)
       