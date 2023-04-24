a = {}
for i in range(8):
    n = int(input())
    a[i+1] = n

sorted(a.items())

a = sorted(a.items(), key= lambda x : (x[1]), reverse= True)
c = 0
l = []

for i in range(5):
    c += a[i][1]
    l.append(a[i][0])

print(c)
for i in sorted(l): print(i, end=' ')



