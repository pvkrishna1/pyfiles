x=((10,20,30),(40,50,60),(70,80,90))
print(x)
for p in x:
    for q in p:
        print(q,end=" ")
    print()
for a,b,c in x:
    print(a,b,c)
y=((10,20,30),[40,50,60],(70,80,90))
print(y)
y[1][1]=99
print(y)
