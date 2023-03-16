n, k = list(map(int, input().split())) 
c = []

for i in range(n):
    c.append(int(input()))

c.sort(reverse=True)

c_n = 0

for i in c:
    if k != 0:
        c_n += k//i 
        k = k%i

print(c_n)