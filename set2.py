x={10,20,30,40,50}
print(x)
for p in x:
    print(p)
x.add(80)
print(x)
y=x.copy()
print(y)
x.remove(30)
print(x)
x.discard(200)
print(x)
x.pop()
print(x)
x.clear()
print(x)
p={(10,20,30),(40,50,60),(70,80,90)}
print(p)
for i in p:
    for j in i:
        print(j,end=" ")
    print()
for a,b,c in p:
    print(a,b,c)
    
