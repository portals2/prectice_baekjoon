import sys
input=sys.stdin.readline

n, m = map(int, input().split(' '))
a = {}

for i in range(n):
    a[i] = input()

b = {v:k for k,v in a.items()}

for i in range(m):
    j = input()
    if 48 <= ord(j[0]) and 57 >= ord(j[0]):
        print(a[int(j)-1],end='')
    else:
        bb = b[j]
        print(1+int(bb))

