x={"java":["spring","struts","jef"],"python":["django","flask","bottles"],"hadoop":["hive","pig","sqoop"]}
print(x)
for k,v in x.items():
    print(k)
    print("-------")
    for p in v:
        print(p)
