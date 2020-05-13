# -*- coding: utf-8 -*-
"""
Created on Wed May 13 02:09:27 2020

https://euler.jakumo.org/problems/view/40.html

@author: Admin
"""
const='0'
rez=1

y=[x for x in range(1,1000001)] # генерируем нашу дробь
for i in y:
    const+=str(i)

#print(const[1],' ',const[10],' ',const[100],' ',const[1000],' ',const[10000],' ',const[100000],' ',const[1000000])
'''
Первый вариант,через возведение в степень. Должен быть медленным
'''

for j in range(7):
    rez*=int(const[10**j])
print(rez)
'''
Второй вариант,дабы избежать возведения в степень
'''
rezultat=1
position=1
for _ in range(6):
    position*=10
    rezultat*=int(const[position])
    print(int(const[position]))
print(rezultat)

    