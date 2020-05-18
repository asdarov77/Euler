# -*- coding: utf-8 -*-
"""
Created on Mon May 18 13:52:21 2020
https://euler.jakumo.org/problems/view/44.html
Перебор. Медленный алгоритм. Не реализован выход после нахождения первой пары ( единственной для этого диапазона)
@author: Admin
"""

mas=[int(n*(3*n-1)/2) for n in range(1,2400)]


razmer=len(mas)
for i in range(0,razmer+1):
    for j in range(i+1,razmer):
        summa=mas[i]+mas[j]
        raznost=mas[j]-mas[i]
        if summa in mas and raznost in mas:
            print(mas[i],mas[j],'нашел')
            print(raznost)
            
       

        





