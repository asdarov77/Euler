# -*- coding: utf-8 -*-
"""
Created on Thu Apr 16 23:24:42 2020

https://euler.jakumo.org/problems/view/30.html

"""
sum=0
    
def function(a):
    mas = 0
    number=a
    while a > 0:
        mas+=(a % 10)**5
        a = a // 10
    if number==mas:
        return 1           



for number in range(100,10000000):
        if function(number)==1:
            print(number)
            sum+=number
print(sum)
        