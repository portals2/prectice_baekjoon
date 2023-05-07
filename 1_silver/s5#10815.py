n = int(input())
n_c = list(map(int, input().split()))

m = int(input())
m_c = list(map(int, input().split()))

c = {}

for i in m_c:
    if i not in c:
        c[i] = 0
for i in n_c:
    if i in c:
        c[i] = 1

[print(a, end=' ')for a in list(c.values())]