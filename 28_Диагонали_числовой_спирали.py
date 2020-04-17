# -*- coding: utf-8 -*-
"""
Created on Tue Apr 14 23:58:44 2020
https://habr.com/ru/post/227253/
Спираль Улама
@author: Admin
"""



sum_corner=sum(4*n*n-6*n+6 for n in range(3,1002,2))+1
print(sum_corner)