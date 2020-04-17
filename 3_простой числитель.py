#import math
n=600851475143
i=1
a=[]
while i*i<=n:
	if n % i ==0:
		if i==n//i:
			a.append(i)
		else:
			a.append(i)
			a.append(n//i)
	i=i+1
a.sort()
print(a)

def isprime(m):
    for ii in range (2,m-1):
        if m % ii == 0:
#            print('делитель на' ,ii , 'составное')
            res=1
            return res
        else:
            ii=ii+1
    res=0    
    return res



for iii in range (0,len(a)):
    m=a[iii]
    isprime(m)
    print(isprime(m))
    if isprime(m)==0:
        print('число простое', m)
    if isprime(m)==1:
        print('число составное', m)
iii=iii+1


        


             
       
        

