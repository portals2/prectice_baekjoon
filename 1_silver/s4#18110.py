import math
n = int(input())

a = [0 for _ in range(n)]

for i in range(n):
    a[i] = (int(input()))

a.sort()
avg = math.floor(n*(15/100)+0.5)

if n == 0:
    print(0)
elif n < 4:
    print(sum(a)//n)
else:
    print(math.floor((sum(a[avg:-avg])/len(a[avg:-avg])+0.5)))
