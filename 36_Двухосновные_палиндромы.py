# -*- coding: utf-8 -*-
"""
Created on Sat May  2 16:45:55 2020

@author: Admin
"""

def isPalindrome(numdec,numbin):
    numdec=str(numdec)
    numbin=str(numbin)
    if numdec==numdec[::-1] and numbin==numbin[::-1]:
        return True

sum=0
for ndec in range(1,1000000):
    nbin=bin(ndec)
    if isPalindrome(ndec,nbin[2:]):
        sum+=ndec
        print(ndec,'двухосновной палиндром')
print(sum)
    