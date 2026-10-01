n= int(input("Enter the number of rows: "))
for i in range(1,n+1):
    for j in range(n,0,-1):
        print(" ",end="")
    for k in range(i):
        if k==n-i:
            print("*",end="")
        else:
            print(" ",end="")
    for l in range(1,n+1):
        print(" ",end="")
    for m in range(n+1,0,-1):
        if m==n-i:
            print("*",end="")
    print()
