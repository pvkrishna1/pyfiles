def cube(a,func):
    p=func(a)
    return p*a
def square(b):
    return b*b
x=cube(10,square)
print(x)
