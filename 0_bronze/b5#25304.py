p = int(input())
n = int(input())
all = 0

for i in range(n):
    a, b = map(int, input().split(' '))
    all += a*b

if all == p:
    print('Yes')
else:
    print('No')