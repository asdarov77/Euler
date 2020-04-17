n=1 # 2,3,4....n-е порядковое треугльное число
x=n*(n+1)/2
int(x)

print(len([_ for _ in range(1,x+1) if not x % _]))
