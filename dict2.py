x={"java":80,"python":99,"hadoop":89}
print(x)
x["aws"]=85
print(x)
x["java"]=70
print(x)
print(x["hadoop"])
print(x.get("python"))
print("hadoop" in x)
print(89 in x)
for k in x:
    print(k,x[k])
