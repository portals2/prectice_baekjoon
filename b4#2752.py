k = []
a, b, c = map(int,input().split(" "))
for i in a, b, c:
    k.append(i)

k.sort()
for i in range(len(k)):
    print(k[i], end=' ')