# 누적합
import sys
input = sys.stdin.readline

n, m = map(int, input().split())

num = list(map(int, input().split()))
sum = 0
sum_l = [0] # 0을 추가하는 이유는 1일 경우 -1에 대한 인덱스 초과를 방지
for i in num:
    sum += i
    sum_l.append(sum)

for i in range(m):
    a,b = map(int, input().split())
    print(sum_l[b] - sum_l[a-1])

