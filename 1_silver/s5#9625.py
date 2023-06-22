# n = int(input())

# s = [(1,0), (0,1), (1,2), (2,3)]

# for i in range(3, n):
#     s.append((s[i][1], sum(s[i])))
# if n < 3:
#     print(s[n][0], s[n][1])
# else:
#     print(s[-2][0], s[-2][1])

# babbabab
# 3 5
# 2 3
# 1 2(1 1이 정답임 // 오답으로 맞췄네)
# 0 1
# 1 0

# a = 전 b의 개수
# b = 전 ab의 개수


#### 모범답안
# DP
K = int(input())
DP = [[0, 0] for _ in range(K+1)]

DP[0] = [1,0]
DP[1] = [0,1]


for i in range(2,K+1):
    DP[i][0] = DP[i-2][0] +DP[i-1][0] # A는 전2번째 전 0과 1전째 0을 합
    DP[i][1] = DP[i-2][1] +DP[i-1][1] # B는 전2번째 전 1과 1전째 1을 합

print(DP[K][0], DP[K][1])