# -*- coding: utf-8 -*-
"""
Created on Tue Mar 24 21:00:02 2020

@author: Admin
"""
sum=0

def delitel(a):
    sum=0
    for i in range(1,a):
        if a%i==0:
            sum+=i
#            print(i)
    return sum
for a in range(1,10000):
    
    if a==delitel(delitel(a))  and a!=delitel(a) :
        sum+=a
        print(a, delitel(a), 'дружественные числа')
print(sum)