# # 시간과 포인트를 비교해서
# # 다음날이 더 커도 이득이라면 다음날을 선택
# # n+1안에 있으면 큰것을 선택


# n = int(input())

# s= []

# for i in range(n):
#     s.append(list(map(int, input().split())))

# for i in range(1, n+1):
#     max = 0
#     d = i
#     p = 0
#     while True:
#         d += s[d-1][0]

#         if d >= n+1: # 이거 체크
#             break

#         p += s[d-1][1]
        
#### 모범답안
# bottom up
import sys
N = int(input())

schedule = [list(map(int, sys.stdin.readline().split())) for i in range(N)]

dp = [0 for i in range(N+1)]

for i in range(N): # i번째 날 부터
    for j in range(i+schedule[i][0], N+1): #i+schedule[i][0]날 까지 했으면
        if dp[j] < dp[i] + schedule[i][1]:
            dp[j] = dp[i] + schedule[i][1]

print(dp[-1])

################################################################
# top down
# N = int(input())
# li = [list(map(int, input().split())) for _ in range(N)]
# dp = [0 for _ in range(N+1)]

# for i in range(N-1, -1, -1):
#     # i일에 상담을 하는 것이 퇴사일을 넘기면 상담을 하지 않는다.
#     if i + li[i][0] > N:
#         dp[i] = dp[i+1]
#     else:
#         # i일에 상담을 하는 것과 상담을 안하는 것 중 큰 것을 선택
#         dp[i] = max(dp[i+1], li[i][1] + dp[i + li[i][0]])

# print(dp[0])