n=int(input("enter Number:"))
for i in range(n+1):
    for j in range(i):
        print(" ",end="")
    for k in range(n-i):
        print("*",end="")
    print()