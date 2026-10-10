t=int(input())
arr=[]
for i in range(t):
    n=int(input())
    arr.append(n)
def selectionSort(arr):
    n=len(arr)
    i=0
    for i in range(n):
        min_index=i
        for j in range(i+1,n):
            if arr[j]<arr[min_index]:
                min_index=j
        temp=arr[i]
        arr[i]=arr[min_index]
        arr[min_index]=temp
    return arr
res=selectionSort(arr)
print(res)

        