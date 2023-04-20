n = int(input())

l = {}

for i in range(n):
    a, b = input().split(' ')
    if a not in l:
        l[a] = 0
    if b == 'enter':
        l[a] = 1
    else:
        l[a] = 0

l = dict(sorted(l.items(), reverse=True))

for a,b in l.items():
    if b == 1:
        print(a)
