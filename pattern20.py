n=int(input("enter the number of rows:  "))
for i in range(1,n+1):
    for j in range(n-i,0,-1):
        if j==1:
            print("*",end="")
        else:
            print(" ",end="")
    for k in range(1,i):
        print(" ",end="")
    for l in range(0,n-1):
        if l==i-1:
            print("*",end="")
        else:
            print(" ",end="")
    print()
for j in range(1,n+1):
    for k in range(1,j):
        if k==j-1:
            print("*",end="")
        else:
            print(" ",end="")
    print()