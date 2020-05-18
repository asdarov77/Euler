# -*- coding: utf-8 -*-
"""
Created on Sun May 17 00:22:20 2020

@author: Admin
"""
from sympy import prime 
from itertools import permutations

def delFunction(number): # функция на проверку особенностей условия задачи
    number=str(number)
    lw=1 #левая граница скользящего окна
    rw=0 #правая граница скользящего окна
    while rw<len(number):
        rw=lw+3
        slice=int(number[lw:rw])
#        print(number[lw:rw])
        if slice%prime(lw)==0:  # prime(n) вывод n-ого простого числа
#            print(slice,prime(lw),'делится без остатка')
            lw+=1
            rez=1
        else:
            rez=0
            break
    return rez

sum=0
string='0123456789'
for item in permutations(string):
        numbers=int(''.join(item))
#        print(numbers,'   ',string)
        if delFunction(numbers)==1 and len(str(numbers))==10:
            sum+=numbers
print(sum)