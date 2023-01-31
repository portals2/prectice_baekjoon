import sys
input=sys.stdin.readline
n = int(input())

m = []

for i in range(n):
    t = int(input())
    if t == 0:
        m.pop()
    else:
        m.append(t)
print(sum(m))