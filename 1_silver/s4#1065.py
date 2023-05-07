n = int(input())
c = 0

if n < 100:
    print(n) #99
else:
    for i in range(100, n+1):
        a = list(str(i))
        ck = int(a[0]) - int(a[1])
        for j in range(2, len(a)):
            if ck == (int(a[j-1]) - int(a[j])):
                c += 1
    print(c+99)
