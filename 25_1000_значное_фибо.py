# -*- coding: utf-8 -*-
"""
Created on Wed Apr  1 14:51:47 2020

@author: Admin
"""

def fib(n):
    fib1=fib2=1
    i = 2 
    while i < n:
        fib_sum = fib2 + fib1
        fib1 = fib2
        fib2 = fib_sum
        i += 1
    return fib_sum;
i=3
while len(str(fib(i)))<1000:
    i+=1
print('порядковый номер 1000 значного числа Фибоначчи-',i)
    