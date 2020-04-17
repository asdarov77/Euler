# -*- coding: utf-8 -*-
"""
Created on Tue Apr 14 22:05:07 2020

@author: Admin
Построение циклических чисел согласно алгоритма
https://ru.wikipedia.org/wiki/%D0%A6%D0%B8%D0%BA%D0%BB%D0%B8%D1%87%D0%B5%D1%81%D0%BA%D0%BE%D0%B5_%D1%87%D0%B8%D1%81%D0%BB%D0%BE
Деление столбиком
"""
def cycle_length(number):
    base=10
#    number=7  # number не должен быть делителем основания системы счисления ( то есть не 2,5)
    t=0
    r=1
    n=0
    while r!=1 or t<1 :
        t=t+1
        x=r*base
        d=x//number   #d является числом остатком от деления
        r=x%number    # r на каждом шаге является остатком от деления
        n=n*base+d
    return(t)    # t-длина цикла
max_length_number=0
length=0    
max_length=0    
for number in range(2,1000):
    if number%2!=0 and number%5!=0:
        length=cycle_length(number)
#        print(length)
        if length>max_length:
            max_length=length
            max_length_number=number
print(max_length, max_length_number)
        