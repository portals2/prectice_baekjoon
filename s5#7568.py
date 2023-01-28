import sys
input=sys.stdin.readline
n = int(input())
a = []

for i in range(n):
    x, y = map(int, input().split(' '))
    a.append([x,y,1])

for i in range(len(a)):
    for j in range(len(a)):
        if (a[i][0] < a[j][0]) and (a[i][1] < a[j][1]):
            a[i][2] += 1

for x, y, c in a:
    print(c)