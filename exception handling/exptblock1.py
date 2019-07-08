print("end")
i=input("enter fno")
x=int(i)
j=input("enter sno")
y=int(j)
try:
    z=x/y
    print(z)
except(ZeroDivisionError):
    print("sno can not be zero")
print("end")
