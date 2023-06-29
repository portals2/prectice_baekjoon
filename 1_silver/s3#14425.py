import sys
input = sys.stdin.readline

n,m = map(int, input().split())

a =  {}
c= 0

for i in range(n):
    s = input()
    a[s] = 0

for i in range(m):
    ss = input()
    if ss in a:
        a[ss] += 1

for i in a.values():
    c += i

print(c)
