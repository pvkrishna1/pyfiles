i=0
def myfunc():
    global i
    i=i+1
    print("welcome",i)
    while i<=5:
        myfunc()
myfunc()
