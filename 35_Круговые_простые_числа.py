# -*- coding: utf-8 -*-
"""
Created on Sat May  2 00:12:06 2020

@author: Admin
"""
from math import sqrt
from itertools import permutations,count, islice

def isPrime(n):
    return n > 1 and all(n%i for i in islice(count(2), int(sqrt(n)-1)))

 
def rotation(num):
    mas=str(num)
    razmer=len(str(num))
    for _ in range(razmer): # Задаст количество круговых перестановок
        mas=mas[-1]+mas[0:razmer-1]
        if isPrime(int(mas)):
#            print(mas)
            rez=1
        else:
            rez=0
            break
        
    return rez

roundcircle=0
for number in range(1000000):
    if rotation(number)==1:
        roundcircle+=1
print(roundcircle)

        