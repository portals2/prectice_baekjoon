n=int(input())
# d=[[0,0]]*(n+1)
d = [[0,0] for _ in range(n+1)]
d[1]=[0,1]
for i in range(2,n+1):
    d[i][0]=d[i-1][0]+d[i-1][1]
    d[i][1]=d[i-1][0]
print(sum(d[n]))
print(d)


#이 문제는 결국 피보나치 수 이다.
n = int(input())

dp = [0] * (n + 1)
dp[1] = 1

for i in range(2, n+1):
    dp[i] = dp[i-2] + dp[i-1]

print(dp[n])