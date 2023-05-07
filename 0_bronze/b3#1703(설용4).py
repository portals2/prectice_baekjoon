
while True:
    l = list(map(int,input().split(' ')))
    if l[0] == 0:
        break
    ls = l[1::2]
    c = l[2::2]
    s = 1
    for i in range(l[0]):
        s = abs((ls[i]* s)-c[i])
    print(s)