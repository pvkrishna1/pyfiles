def cube(a,func):
    p=func(a)
    return p*a
x=cube(10,lambda b:b*b)
print(x)
y=cube(20,lambda b:b*b)
print(y)
