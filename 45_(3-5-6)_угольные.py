# -*- coding: utf-8 -*-
"""
Created on Tue May 19 02:35:37 2020

@author: Admin
"""

tri_mas=[int(1/2*n*(n-1)) for n in range(284,56000)]
five_mas=[int(n*(3*n-1)/2) for n in range(164,32000)]
six_mas=[n*(2*n-1) for n in range(143,28000)]


#for i in tri_mas:
for j in five_mas:
    for n in six_mas:
        if j==n:
            print(j,n)
            number=j
if number in tri_mas:
    print(number)
    



