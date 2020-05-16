# -*- coding: utf-8 -*-
"""
Created on Sat May 16 14:43:21 2020
'''
Можно воспользоваться функцией sympy.isprime для определения простоты числа,либо использовать написанную ниже
'''
@author: Admin
"""


from itertools import permutations
import sympy


#def isprime(n):
#    if n == 1:
#        return False
#    for x in range(2, n):
#        if n % x == 0:
#            return False
#        else:
#            return True
        

max=0
candidats='123456789'

while  len(candidats)>1:
    for item in permutations(candidats):
        numbers=int(''.join(item))
        if sympy.isprime(numbers)==True: # или используем код функции выше
            if numbers>max:
                max=numbers
    candidats=candidats[:-1]
print(max)
  
    
