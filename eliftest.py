print("begin")
i=input("enter a positive num")
x=int(i)
if x<10:
    print("given number is single digit number")
elif x<100:
    print("given number is 2 digit number")
elif x<1000:
    print("given number is 3 digit number")
else:
    print("given number is 3< digit number")
print("end")
