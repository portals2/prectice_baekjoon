n, k = map(int, input().split())

a = list(map(int, input().split()))

sum = 0
sum_l = [0]
max_hi = -1e9

for i in a:
    sum += i
    sum_l.append(sum)
for i in range(k, n+1):
    hi = sum_l[i] - sum_l[i-k]
    if hi > max_hi:
        max_hi = hi
print(max_hi)

#누적합의 원리
# n번째 부터 n+i번째의 합을 구하고 싶으면
# 각 자리에 누적합의 index에서
# (n+i) - (n-1)으로 
# n번째 부터 n+i의 합을 구할 수있다.
# n+i는 0부터 모든 합의 수이니까
