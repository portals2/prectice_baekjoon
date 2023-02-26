# 1 1 1 = 1
# 1 16 16 = 16
# 6 20  1 = 20
# 15 1 10 = 29

a = list(map(int, input().split()))

e, s, m = 1,1,1
c = 1

while (a != [e,s,m]):
    e += 1
    s += 1
    m += 1
    c += 1
    if e == 16:
        e = 1
    if s == 29:
        s = 1
    if m == 20:
        m = 1

print(c)
    
