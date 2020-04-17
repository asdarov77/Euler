# -*- coding: utf-8 -*-
"""
Created on Tue Mar 24 19:32:38 2020

@author: Admin
"""
fact=1
n=100
sum=0
while n>=1:
    fact*=n

    n-=1
a=str(fact)    
for i in range(len(a)):
    sum=sum+int(a[i])
print(sum)
    
    