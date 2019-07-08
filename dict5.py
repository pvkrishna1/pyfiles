x={"java":{"spring":90,"struts":78,"jef":67},"python":{"django":99,"flask":70,"bottles":65},"hadoop":{"hive":90,"pig":90,"sqoop":89}}
print(x)
for k,v in x.items():
    print(k)
    print("---------")
    for i,j in v.items():
        print(i,j)
