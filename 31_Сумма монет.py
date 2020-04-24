# -*- coding: utf-8 -*-
"""
Created on Sat Apr 18 19:19:09 2020
Условие
https://euler.jakumo.org/problems/view/31.html

https://python-scripts.com/question/7869
https://dp.acmp.ru/index_files/m3_z4.pdf
@author: Admin
"""

#def solution():
#    target = 10
#    coins = (1, 2, 5, 10)
#    ways = [1] + [0]*target
#    print(ways)       
#    for coin in coins:
#        for i in range(coin, target+1):
#            ways[i] += ways[i-coin]
#            print(coin ,  ways[i-coin])           
#    return ways[target]
  
#if __name__ == '__main__':
#    print(solution())

#def function(coin,target):
    






w=200
coins=[1,2,5,10,20,50,100,200]
table=[1]+[1]*w
#print(table)

for i in range(1,len(coins)):    # монеты порядковый номер. Строка
    for j in range(1,w+1):  # сдача w
        if j<coins[i]:
            table[j]=table[j]
#            print(j ,   table[j] , 'coin', coins[i])
        else:
            table[j]=table[j]+table[j-coins[i]]
#            print(j, table[j]   , 'coin', coins[i] )
print(table[-1])



