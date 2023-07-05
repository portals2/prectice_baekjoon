n, m = map(int, input().split())

a = sorted(list(map(int, input().split())))
result = []

def btk(start):
    if len(result) == m:
        for i in range(m):
            print(result[i], end=' ')
        print('')

    for i in range(start, n):
        if a[i] not in result:
            result.append(a[i])
            btk(i)
            result.pop()        

btk(0)