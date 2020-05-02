# -*- coding: utf-8 -*-
"""
Created on Sat May  2 17:35:21 2020
"""
#Плохое решение. Множественный вызов функции

"""
@author: Admin
"""

def isPrime(n):
    return n > 1 and all(n%i for i in islice(count(2), int(sqrt(n)-1)))


def rezPrime(number): 
    
    nstr=str(number)
    n=len(nstr)
    for m in range(n):
        if isPrime (int(nstr[m:n])) and isPrime (int(nstr[0:n-m])):
#            print(nstr[m:n],nstr[0:n-m])
            rez=1
        else:
            rez=0
            break
    return rez

mas=[]
for num in range(8,999999):
    if rezPrime(num)==1:
        mas.append(num)
print(mas)        
massiv=mas
sum = 0
for i in massiv:
    sum += i
print(sum)