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

#def isprime(number):
#    a = [rnd.randint(1, number) for i in range(0, 10)]
#    a=rnd.randint(1,number)
#    print('случайное число', a , 'которое меньше числа', number)
#    if a[i]**number==a[i]%number:
#        res=1
#
#
#    else:
#        res=0
#        break
#    return res
def isprime(number):
    if number == 2:
        res=1
        return res
    if number % 2 ==0:
        res=0
        return res
    if number > 3 and number % 3 ==0:
        res=0
        return res
    if number > 5 and number % 5 ==0:
        res=0
        return res
    if number > 7 and number % 7 ==0:
        res=0
        return res
    if number > 11 and number % 11 ==0:
        res=0
        return res
    if number > 13 and number % 13 ==0:
        res=0
        return res
    if number > 17 and number % 17 ==0:
        res=0
        return res
    if number > 19 and number % 19 ==0:
        res=0
        return res
    if number > 23 and number % 23 ==0:
        res=0
        return res
    if number > 29 and number % 29 ==0:
        res=0
        return res
    
    
    a = [rnd.randint(1, number-1) for i in range(0, 20)]
#    print(a, 'массив случайных')
    for i in a:
        if i**(number-1) % number == 1:
#            print (number, 'простое число', i , 'случайное меньше')
            res=1
            
        else:
            res=0
#            print (number, 'составное число', i , 'случайное меньше')
            break
    return res


#if isprime(5)==1:
#        print (5, 'простое число')

x=1
n=2

while x <=10001:
    if isprime(n)==1:
        print (n, 'простое число', '  которое по счету' ,  x)
        x=x+1
        n=n+1
    else:
        n=n+1

