n=int(input("Enter the number of rows: "))
for i in range(1,n+1):
    for j in range(i):
        if j==0 or j==i-1 or i==n:
            print("*",end="")
        else:
            print(" ",end="")
    print()