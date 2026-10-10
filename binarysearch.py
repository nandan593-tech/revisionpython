t = int(input())

arr = []

for i in range(t):
    n = int(input())
    arr.append(n)

target = int(input())

def search(arr, target):
    i = 0
    j = len(arr) - 1

    while i <= j:
        mid = (i + j) // 2

        if arr[mid] == target:
            return mid

        elif arr[mid] < target:
            i = mid + 1

        else:
            j = mid - 1

    return -1

result = search(arr, target)
print(result)