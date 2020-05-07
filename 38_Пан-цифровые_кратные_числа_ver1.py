# -*- coding: utf-8 -*-
"""
Created on Thu May  7 17:09:16 2020

@author: Admin
"""

def panfunction(i):
    number=str(i)
    for j in range(1,10):
        if str(j) in number:
            j+=1
            rez=1
        else:
            rez=0
            break
    return rez

max=0
for num in range(1,9999):
    
#num=192
    number=''
    for i in range (1,10):
        number+=str(num*i)
#        print(number)
#    print(number)
        if panfunction(number)==1 and len(number)<=9 and int(number)>max:
            print(number,'панцифровое число')
            max=int(number)
            
            print(max,'максимальное')
    
    