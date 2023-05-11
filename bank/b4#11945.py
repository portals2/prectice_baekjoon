n,m = map(int, input().split(' '))

a = []

for i in range(n):
    a.append(str(input()))


for i in range(n):
    aa = list(a[i])
    for j in range(m-1,-1,-1):
        print(aa[j], end='')
    print('')