n=1000
n_max=1
while n%2==0:
    n=n/2
    n_max+=1
print(n_max, n)
print(str((2**n_max)**int(n)))
#print(sum([_ for _ in range(1,2**n+1)]))
arr=str((2**n_max)**int(n))
#print(sum(str((2**n))[i]) for i in range(0, len(str(2**n))))
print(sum((int(arr[_]) for _ in range(0, int(len(arr))))))
# 2**n = (2**1)**n
# максимальная степень двойки
# (2**n_max)**(n/n_max)