n,m = map(int, input().split())

a= sorted(list(map(int, input().split())))

l =[]

def btk(start):
    if len(l) == m: #dfs에서 분기를 주어 결과 도출
        for i in l:
            print(i, end=' ')
        print()
        return

    for i in range(n):
        if a[i] not in l:
            l.append(a[i])
            btk(i)
            l.pop()

btk(1)