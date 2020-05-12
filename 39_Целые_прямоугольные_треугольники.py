# -*- coding: utf-8 -*-
"""
Created on Fri May  8 17:55:43 2020
https://euler.jakumo.org/problems/view/39.html
@author: Admin
"""

 

imax=0 # Максимальное количество вариантов
pmax=0 # Значение периметра pmax при котором будет максимальное количество вариантов

for p in range (1,1001):
    i=0 # Обнуляем при каждом очередном периметре количество вариантов  
    for a in range (1,p):
        for b in range (a,p):
            c=p-a-b
            if c*c==a*a+b*b:
                i+=1
                print(a,b,c,i)
                if i>imax:
                    imax=i
                    pmax=p
print(imax,pmax)                