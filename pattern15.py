n=int(input("enter number:"))
for i in range(1,n+1):
    for j in range(1,n+1):
        if j==1 :
            print("|",end="")
        
        elif i==j:
            print("\\",end="")
        elif i==n:
                    
            print("_",end="")
        else:
            print(" ",end="")
    print()