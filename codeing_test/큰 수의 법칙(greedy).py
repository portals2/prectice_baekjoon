n, m, k = map(int, input().split(' '))

num = list(map(int, input().split(' ')))

num.sort(reverse=True)

c = 0

for i in range(1, m+1):
    if i % k == 0:
        c += num[1]
    else:
        c += num[0]

print(c)

#### 수학적인 접근

c = int(m/(k+1))*k
c += m%(k+1)

r = 0
r += c * num[0]
r += (m-c) * num[1]

print(r)