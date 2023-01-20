import sys
input=sys.stdin.readline

n = int(input())

a = list(map(int,input().split(' ')))

y = 0
m = 0
for i in range(n):
    q = ((a[i]//30)+1)*10
    w = ((a[i]//60)+1)*15
    y += q
    m += w
if y>m:
    print('M',m)
elif y<m:
    print('Y',y)
else:
    print('Y M', y)