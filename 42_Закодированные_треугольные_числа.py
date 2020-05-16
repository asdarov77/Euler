# -*- coding: utf-8 -*-
"""
Created on Sun May 17 08:45:36 2020

@author: Admin
"""

def literal_num(symb):
    return int(ord(symb)-ord('A')+1)
    
mas=[int(1/2*n*(n-1)) for n in range(2,26)]
print(mas)

with open('p042_words.txt') as file: 
    words=file.read().replace('"','').split(',') #Читаем в список,удаляем апостроф и указываем разделитель слов   
file.close()

count=0 # Счетчик треугольных слов
for word in words:
    sum=0 # Сумма зашифрованных букв
    split=list(word) # Разделяем слово на символы 
    for i in split:
            sum+=literal_num(i)    
    if sum in mas:
        count+=1
        print(word, 'треугольное слово', sum)
print(count)      

        
