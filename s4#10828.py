# filo

import sys
input=sys.stdin.readline
l = []

n = int(input())

for i in range(n):
    a = list(input().split())
    if a[0] == 'push':
        l.append(a[1])
    elif a[0] == 'pop':
        if len(l) == 0:
            print(-1)
        else:
            print(int(l.pop()))
    elif a[0] == 'size':
        print(len(l))
    elif a[0] == 'empty':
        if len(l) == 0:
            print(1)
        else:
            print(0)
    elif a[0] == "top":
        if len(l) == 0:
            print(-1)
        else:
            print(l[-1])