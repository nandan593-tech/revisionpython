n=int(input("enter number:"))
for i in range(1,n+1):
    for j in range(1,n+1):
        if i==1 or i==n or j==(n//2)+1:
            print("\u2764\ufe0f",end="")
        else:
            print(" ",end="")
    for k in range(1,n+1):
        print(" ",end="")
    for l in range(1,n+1):
        if i==n or l==1:
            print("\u2764\ufe0f",end="")
        else:
            print(" ",end="")
    for k in range(1,n+1):
        print(" ",end="")
    for m in range(1,n+1):
        if i==1 or i==n or m==n or m==1:
            print("\u2764\ufe0f",end="")
        else:
            print(" ",end="")
    for k in range(1,n+1):
            print(" ",end="")
    for p in range(1,n+1):
        if i==p:
            print("\u2764\ufe0f",end="")
        else:
            print(" ",end="")
    for k in range(n,0,-1):
        if i==k:
            print("\u2764\ufe0f",end="")
        else:
            print(" ",end="")
    for k in range(1,n+1):
        print(" ",end="")
    for q in range(1,n+1):
        if i==1 or i==n or q==1 or i==n//2+1:
            print("\u2764\ufe0f",end="")
        else:
            print(" ",end="")
    for k in range(1,n+1):
            print(" ",end="")
    for r in range(1,n+1):
        if r==1 or i==n or r==n:
            print("\u2764\ufe0f",end="")
        else:
            print(" ",end="")
    

    print()