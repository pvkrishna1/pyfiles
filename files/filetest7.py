import pickle
with open("profile.txt","rb") as x:
    data=pickle.load(x)
    for p in data:
        print(p)
