n = int(input())

a = [0,1,1,2] + [0 for i in range(n-3)] 

if n < 3:
    print(a[n])
else:
    for i in range(3, n+1):
        a[i] = a[i-1] + a[i-2]

    print(a[-1])


