# -*- coding: utf-8 -*-
"""
Created on Wed Mar 25 17:06:32 2020

@author: Admin
"""
import string
scores=0
def alfavit(name):
    sum=0
    for i in range(len(name)):
        sum+=(ord(name[i])-ord('A')+1) # Отнимаем к примеру от буквы А букву А плюс 1 получаем первый в алфавите (1-1=0, и 0+1=1)
    return sum        


handle = open("p022_names.txt", "r") 
data = handle.readline().split(',')
data.sort()
for i in range(len(data)):
#    print(data[i][1:-1])
    name=data[i][1:-1]
    scores+=alfavit(name)*(i+1)
    print(alfavit(name), scores)
print('суммарное кол-во очков', scores)
#print(len(data))
handle.close()
#print(alfavit(data[0][1:-1]))



#try:
#    with open('p022_names.txt') as f:
#        my_lines = str(f)
#        
#except IOError:
#    print("An IOError has occurred!")