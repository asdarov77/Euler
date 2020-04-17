# -*- coding: utf-8 -*-
"""
Created on Tue Mar 10 20:28:51 2020

@author: Admin
"""

from num2words import num2words as n2w
i=0
for _ in range(1,1001):
    i+=len(n2w(_).replace('-','').replace(' ',''))
print(i)    
