# -*- coding: utf-8 -*-
"""
Created on Wed Jan 29 01:38:00 2020

@author: Admin
"""
n=0
m=0
for i in range (1,101):
    print(i, 'натуральное')
#    i=i*i
    print(i*i, 'квадрат')
    n=n+i*i
    m=m+i
print(n,'сумма квадратов')
print(m*m, 'квадрат суммы')
print (m*m-n, 'разность квадрата суммы и суммы квадратов')
    