# -*- coding: utf-8 -*-
"""
Created on Tue Mar 31 19:30:07 2020

@author: Admin
"""

import math
x=14060

sum=0
#for i in range(1,int(math.sqrt(x)+1)):

for i in range(1,x):
    if x%i==0:
        sum+=i
        print(i, 'делитель')
print(sum, 'сумма')    
if x==sum:
    print(x, '-число идеальное')
elif sum>x:
    print(x, '-число избыточное')
else:
    print(x, '-число недостаточное')
    