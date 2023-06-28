n, x = map(int, input().split())

a = list(map(int, input().split()))

c = 100001

for i in range(1, len(a)):
    k = a[i-1] + a[i]
    c = min(c, k)

print(c*x)

