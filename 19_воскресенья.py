# -*- coding: utf-8 -*-
"""
Редактор Spyder

Это временный скриптовый файл.
"""

from datetime import datetime, date
print(date.today())
now=date(2000,12,31)
then = date(1901, 1 ,1)
then.weekday()

year=1901
month=1
day=1
voskres=0
#
while year<2001:
    for j in range(12):
        if j==3 or j==5 or j==8 or j==10:
            for i in range(30):
                print(date(year, month+j ,day+i))
                if (date(year, month+j ,day+i)).weekday()==6 and i==0:
                    voskres+=1
        elif j==1 and year%4==0:    
            for i in range(29):    
                print(date(year, month+j ,day+i))
                if (date(year, month+j ,day+i)).weekday()==6  and i==0:
                    voskres+=1
        elif j==1 and year:    
            for i in range(28):    
                print(date(year, month+j ,day+i))
                if (date(year, month+j ,day+i)).weekday()==6  and i==0:
                    voskres+=1
        else:    
            for i in range(31):    
                print(date(year, month+j ,day+i), (date(year, month+j ,day+i)).weekday())
                if (date(year, month+j ,day+i)).weekday()==6  and i==0:
                    voskres+=1
    year+=1    
print('количество воскресений', voskres)    