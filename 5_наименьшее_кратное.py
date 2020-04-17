# -*- coding: utf-8 -*-
"""
Created on Fri Jan 24 01:49:05 2020

@author: Admin
"""

#x=1
#i=1
#while i <=20:
#    print(x)
#    if x % i ==0:
#        print(i)
#        i+=1    
#    else:
#        x+=1
#        i=1
     
#print(x)

def proverka(n):
    
    for i in range(11,21):
        if n % i ==0 and n % 2 ==0 and n % 3 ==0 and n % 5 ==0:
            print(i, 'почему')
#            i=i+1            
            res=1
        else:
            res=0
            break
    return res
        
x=2520

while proverka(x)!=1:
    x=x+1
print(x)

    
        
        
