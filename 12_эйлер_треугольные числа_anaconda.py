# -*- coding: utf-8 -*-
"""
Created on Thu Feb 20 16:04:12 2020

@author: Admin
"""
import math
x,n,delitel=1,1,1 # 2,3,4....n-е порядковое треугльное число


while delitel <=10:
    x = n * (n + 1) // 2
    delitel = 2+(len([_ for _ in range(2, math.ceil(math.sqrt(x))) if not x % _])*2)
    print('число', x , 'имеет' , delitel, 'делителей', n , 'порядковый номер')
    n+=1
else:

    print('число', x , 'имеет' , delitel, 'делителей')