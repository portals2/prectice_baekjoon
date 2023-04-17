a = []
for i in range(4):
    a.append(int(input()))
b = []
for i in range(2):
    b.append(int(input()))

a.sort(reverse=True)
b.sort(reverse=True)

print(a[0]+a[1]+a[2]+b[0])