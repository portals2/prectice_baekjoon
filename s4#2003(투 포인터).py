import sys
input=sys.stdin.readline

n, m = map(int, input().split(' '))

a = list(map(int, input().split(' ')))
c = 0
s = 0
e = 0
sum = 0

while s < n:
    if sum >= m or e == n:
        sum -= a[s]
        s += 1
    else:
        sum += a[e]
        e += 1
    if sum == m:
        c += 1
        
print(c)

# sum 보다 작거나 같다면, e를 증가 시켜 sum에 더한다.
# 만약 sum이 m보다 크거나 같다면 s를 증가시켜 sum에서 뺀다.
# 여기서 sum이 m과 동일 하다면 하나를 카운트 한다.
# 이렇게 주어진 수열에 대해서 모든 경우를 찾으면서도
# O(N)이라는 시간복잡도를 가질 수있다. 
# 만약 s를 고정하고 e를 계속 바꾸는 이중 for문이면
# 해결하지 못한다.