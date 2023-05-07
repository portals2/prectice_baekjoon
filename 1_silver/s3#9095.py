from itertools import product
arr = [1,2,3]


n = int(input())

for i in range(n):
    c =0
    t = int(input())
    for j in range(1, t+1):
        a = list(list(product(arr, repeat=j)))
        for k in range(len(a)):
            if sum(a[k]) == t:
                c += 1

    print(c)


#### 모범답안
t = int(input())

for _ in range(t):
    n = int(input())
    dp = [0] * (n+1)

    if n == 1:
        print(1)
        continue

    if n == 2:
        print(2)
        continue

    if n == 3:
        print(4)
        continue

    dp[1] = 1
    dp[2] = 2
    dp[3] = 4

    for i in range(4, n+1):
        dp[i] = dp[i-1] + dp[i-2] + dp[i-3]

    print(dp[n])