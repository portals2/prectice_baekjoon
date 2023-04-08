n = int(input())

a = [1,2]
c = 0
if n == 1:
    print(1)
else:
    for i in range(2, n):
        num = (a[i-1] + a[i-2])
        a.append(num)
    print(a[-1]%10007)

#### 문제 풀이
# 마지막 칸에는 올 수 있는 막대의 경우가 =과 ㅣ가 있다.
# 이때 ㅣ가 온다면 나머지의 칸 즉 2*n-1개의 칸을 채워야하며
# =이면 2*n-2개의 칸을 채워야한다.
# 즉 이것은 피보나치수이다.
####다른 답안
# 한 리스트에 저장하면 overflow가 발생하기 때문에
# 
# n = int(input())
# dp = [0] * 1001
# dp[1] = 1
# dp[2] = 2


# for index in range(3, 1001):
#     dp[index] = dp[index - 1] + dp[index - 2]
# print (dp[n] % 10007)