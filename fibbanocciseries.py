n=int(input("enter the number:"))
arr=[0,1]
for i in range(2,n+1):
   f=arr[i-1]+arr[i-2]
   arr.append(f)

print(arr[n])