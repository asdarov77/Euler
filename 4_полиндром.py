# -*- coding: utf-8 -*-
"""
Created on Wed Jan 22 01:55:42 2020

@author: Admin
"""


def reverse(a):
    b=str(a)
    int(b[::-1])
    return int(b[::-1])
m=[]
for i in range (100,1000):
    
#    print(i)
    for y in range (100,1000):
#        print(y*i)
        m.append(y*i)
m.sort(reverse=True)
max=0
for z in range (0,len(m)):
    if m[z]==reverse(m[z]):
        if m[z] > max:
            max=m[z]
            print(m[z])
            exit
    else:
        z+=1
#    mas=i+reverse(i)    
#    print(i+reverse(i), 'для числа' ,i)
#    reverse(mas)
#    print(mas)
#        if mas==reverse(mas):
#            print('палиндром',mas)
#            exit()
#        else:
#            reverse(mas)
#    m.append(i+reverse(i))
#m.sort()