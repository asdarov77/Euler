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
for num in range(9,99999):
    number=''
    i=1

    while i<=9:
        number+=str(num*i)
        if len(number)>=9:
            break
        else:
            i+=1

    if panfunction(number)==1 and int(number)>max and len(number)==9:
        print(number,'панцифровое число')
        max=int(number)
print(max,'максимальное')
        
    