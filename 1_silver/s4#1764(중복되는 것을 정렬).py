# import sys
# input=sys.stdin.readline

# n, m = map(int, input().split())

# d = []

# for i in range(n):
#     d.append(input())

# d.sort()
# a = []
# c = 0
# for i in range(m):
#     b = input()
#     if b in d:
#         a.append(b)
#         c += 1
# print(c)
# for i in a:
#     print(i,end='')


# 모범답안
n,m = map(int,input().split())
n_name = set(input() for i in range(n))
m_name = set(input() for i in range(m))

sort = sorted(list(n_name & m_name))
print(len(sort))
sort.sort()
for i in sort:
    print(i)

#딕셔너리로 중복 처리
import sys

n,m =map(int, sys.stdin.readline().split())
hp={}
cnt=0
hwp=[]

for _ in range(n):
    hp[input()]=0
for _ in range(m):
    wp = input()
    if wp in hp:
        cnt+=1
        hwp.append(wp)

hwp.sort()
print(cnt)
for i in range(len(hwp)):
    print(hwp[i])