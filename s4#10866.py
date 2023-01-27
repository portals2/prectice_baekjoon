from collections import deque
import sys
input=sys.stdin.readline

n = int(input())
l = deque([])

for i in range(n):
    a = list(input().split())
    if a[0] == 'push_front':
        l.appendleft(a[1])
    elif a[0] == 'push_back':
        l.append(a[1])
    elif a[0] == 'pop_front':
        if len(l) == 0:
            print(-1)
        else:
            print(l.popleft())
    elif a[0] == 'pop_back':
        if len(l) == 0:
            print(-1)
        else:
            print(l.pop())
    elif a[0] == 'size':
        print(len(l))
    elif a[0] == 'empty':
        if len(l) == 0:
            print(1)
        else:
            print(0)    
    elif a[0] == 'front':
        if len(l) == 0:
            print(-1)
        else:
            print(l[0])
    elif a[0] == 'back':
        if len(l) == 0:
            print(-1)
        else:
            print(l[-1])