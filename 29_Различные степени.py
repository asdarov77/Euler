# -*- coding: utf-8 -*-
"""
Created on Thu Apr 16 21:58:28 2020

@author: Admin
"""

mas=[]
for a in range(2,101):
    for b in range(2,101):
        if a**b not in mas:
            mas.append(a**b)
mas.sort()

print(len(mas))

r = range(2, 101)
print( "Project Euler 29 Solution =", len({a**b for a in r for b in r}))