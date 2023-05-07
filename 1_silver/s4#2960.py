n, k = map(int, input().split(' '))
con=0


a = [False] + [True]*(n)
l = []

for i in range(2,n+1):
  if a[i]:
    for j in range(i, n+1, i):
        if j in l:
           pass
        else:
            a[j] = False
            l.append(j)
            if len(l) == k:
               print(j)

