# i-2, i-3

n = int(input())

arr = [1, 1, 1, 2, 2, 3, 4, 5, 7, 9]

for i in range(n):
    num = int(input())
    while len(arr) < num:
        k = len(arr)
        arr.append(arr[k-2]+arr[k-3])
    print(arr[num-1])
