# n = int(input())

# a = [0 for i in range(n)]

# for i in range(n):
#     a[i] = int(input())

# c1 = 0
# # c2 = a[1]
# c1_ = 0
# # c2_ = 2
# # 이분법으로 더한다
# # 만약 리스트의 끝의 선택지가 나오면 그걸 더한다.
# # 아래 두개에서 위에 하나를 더한다.
# for i in range(n):
#     if (c1_ == n-1) or (c1_+1 == n-1):
#         c1 += a[n-1]
#         break
#     c1 += max(a[c1_]+a[c1_+2] , a[c1_+1]+a[c1_+2])
#     c1_+=2
# for i in range(n):
#     if (c2_ == n-1) or (c2_+1 == n-1):
#         c2 += a[n-1]
#         break
#     c2 += max(a[c2_], a[c2_+1])
#     if a[c2_] > a[c2_+1]:
#         c2_ += 1
#     else: c2_ += 2

# print(c1)

#### 모범답안
# 종이로 해보기 arr 그려서
N = int(input())
stair = [0]*301
for i in range(N):
    stair[i]=int(input())

DP = [0]*301
DP[0] = stair[0]
DP[1] = stair[0]+stair[1]
DP[2] = max(stair[0]+stair[2], stair[1]+stair[2])

for i in range(3, N):
    DP[i] = max(DP[i-3] + stair[i-1] + stair[i], DP[i-2]+stair[i])
# DP는 stair[i]를 선택 했을 때의 최대값
# 연속으로 선택하면 뒤에 숫자는 무조건 한칸 뛰어야 하니까 i-3
# 바로 뛰어 버린느 선택이면 i-2    
print(DP[N-1])