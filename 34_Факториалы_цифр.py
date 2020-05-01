# -*- coding: utf-8 -*-
"""
Created on Fri May  1 14:34:13 2020

@author: Admin
"""



def factorial(number):
    fnum=1
    for i in range(1,number+1):
        fnum*=i
    return fnum
    
mas=0
for i in range(3,100000):
    m=0
    for l in str(i):
        m+=factorial(int(l))
#    print(i,m)
    if i==m:
            
        print('число', i ,'=', m ,'факториал')
        mas+=m
print(mas)
        
        
        
    