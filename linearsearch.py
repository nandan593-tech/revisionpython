t=int(input())
arr=[]
for i in range(t):
    n=int(input())
    arr.append(n)
target = int(input())
for j in range(len(arr)):
    if arr[j]==target:
        print("found")
        break
else:
    print("not found")