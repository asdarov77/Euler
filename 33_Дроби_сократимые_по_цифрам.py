# -*- coding: utf-8 -*-
"""
Created on Thu Apr 30 16:27:15 2020
https://euler.jakumo.org/problems/view/33.html
@author: Admin
"""

def solution(i,j):
    istr=str(i)
    jstr=str(j)

    for l in istr:
        if l in jstr and i%10!=0 and j%10!=0:  # Исключаем нетривиальные дроби вида 10/20 , 30/50 и так далее
            istr_num=istr.replace(l,'',1)
            jstr_num=jstr.replace(l,'',1)
            
            if i/j==int(istr_num)/int(jstr_num):

        
                return int(istr_num),int(jstr_num)

    
chislitel=1
znamenatel=1
for i in range (10,100):
    for j in range (10,100):
        if i/j<1 and solution(i,j)!=None:
            print(i,'/',j,'   ',solution(i,j))
            chislitel*=solution(i,j)[0]
            znamenatel*=solution(i,j)[1]
print(chislitel,  znamenatel)
for dividers in range(1,chislitel+1):
    if chislitel%dividers==0 and znamenatel%dividers==0:
        znamenatel=znamenatel/dividers
print(znamenatel)
            
