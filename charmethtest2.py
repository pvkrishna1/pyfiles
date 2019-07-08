x="python is open soure language"
print(x)
words=x.split()
for w in words:
    print(w)
y="python@is@open@source@language"
print(y)
res=y.split("@")
for p in res:
    print(p.upper(),p.lower(),len(p))
