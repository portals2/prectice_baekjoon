#1열에 m값 만큼 더하는 식을  계속 하고
# 그 총 합을 더하면 되것
import sys
input=sys.stdin.readline

n, m = map(int, input().split())

a = []

for i in range(n):
    a.append(list(map(int, input().split())))

k = int(input())

for j in range(k):
    num = 0
    z,x,c,v = map(int, input().split())

    if z==c and x==v:
        print(a[z-1][x-1])
    else:
        # for i in range(z, c+1):
        for j in range(z, c+1): 
            # num += a[i-1][j-1]
            num += (sum(a[j-1]) - sum(a[j-1][0:x-1]))
        print(num)

# print(sum(a[0][0:2]))

# 모범답안
n, m = map(int, input().split())
a = []
dp = [[0] * (m + 1) for _ in range(n + 1)]
for _ in range(n):
    a.append(list(map(int, input().split())))
for i in range(1, n + 1):
    for j in range(1, m + 1):
        dp[i][j] = a[i - 1][j - 1] + dp[i][j - 1] + dp[i - 1][j] - dp[i - 1][j - 1]
k = int(input())
for _ in range(k):
    i, j, x, y = map(int, input().split())
    print(dp[x][y] - dp[x][j - 1] - dp[i - 1][y] + dp[i - 1][j - 1])