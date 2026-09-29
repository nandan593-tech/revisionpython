n=int(input("enter number:"))
for i in range(1,n+1):
    for j in range(n,i,-1):
        print("*",end="")
    for k in range(1,i):
        print(" ",end="")
    for l in range(1,i):
        print(" ",end="")
    for m in range(n,i,-1):
        print("*",end="")
    print()