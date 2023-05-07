n, k = map(int, input().split(' '))

a = 1
b = 1
c = 1
for i in range(n):
    a *= i+1
for i in range(k):
    b *= i+1
for i in range(n-k):
    c *= i+1

print(int(a/(b*c)))
