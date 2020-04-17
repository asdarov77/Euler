# -*- coding: utf-8 -*-
"""
Created on Mon Feb  3 22:35:44 2020

@author: Admin
"""
import random as rnd
#i=1
#p=1


#while i < 6:
   
#   a=rnd.randint(1,p)
#   a = [random.randint(1, p) for p in range(0, 10)]
#   if a**p==a%p:
#       print('простое число',p, '  число a', a, '  число i', i )
#       i=i+1
#       p=p+1
#       del(a)
#   else:
#       p=p+1
#       del(a)       
       
def isprime(number):
    a = [rnd.randint(1, number) for i in range(0, 10)]
#    a=rnd.randint(1,number)
    print('случайное число', a , 'которое меньше числа', number)
    if a[i]**number==a[i]%number:
        res=1
        
        
    else:
        res=0
        return res        
    return res
            
            
            
 
        
for i in range (1,6):
    print('для числа',i,'результат', isprime(i))
    