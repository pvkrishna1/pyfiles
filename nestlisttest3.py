msg="python is a opensource language"
print(msg)
words=msg.split()
x=([w.upper(),w.lower(),len(w)]for w in words)
for p in x:
    print(p)
