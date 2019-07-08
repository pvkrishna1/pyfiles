import pickle
data=[["scott",7788,3000.0],["blake",7902,2500.0],["smith",7369,4000.0]]
x=open("picfile.txt","wb")
pickle.dump(data,x)
x.close()
