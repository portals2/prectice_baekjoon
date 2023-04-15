import sys
input=sys.stdin.readline
a, b = map(int, input().split(" "))

s = []

for i in range(2):
    s += list(map(int, input().split(" ")))

s.sort()
for i in s:
    print(i, end=' ')