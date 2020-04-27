# -*- coding: utf-8 -*-
"""
Created on Sat Apr 25 01:10:27 2020
https://euler.jakumo.org/problems/view/32.html
@author: Admin
"""

        
def panfunction(i):
    number=str(i)
    for j in range(1,10):
        if str(j) in number:
            j+=1
            rez=1
        else:
            rez=0
            break
    return rez

mas=[]

for i in range(1,1000):
    for j in range(i,10000):
        temp=str(i)+str(j)+str(i*j)
        if len(temp)==9:
            if panfunction(temp)!=0:
                if (i*j) not in mas:
                    mas.append(i*j)
print(mas)
print(sum(mas))