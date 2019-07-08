print("begin")
i=input("enter fno")
j=input("enter sno")
try:
    x=int(i)
    y=int(j)
    z=x/y
    print(z)
except(ZeroDivisionError):
    print("sno can not be zero")
finally:
    print("welcome")
print("end")
