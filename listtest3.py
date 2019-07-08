x=[10,20,30,40,50]
print(x)
while True:
    i=int(input("enter the search value"))
    if i in x:
        print("element is found")
        break 
    else:
        print("element is not found")
        
