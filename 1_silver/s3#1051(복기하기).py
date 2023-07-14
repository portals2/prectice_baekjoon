n,m = map(int, input().split())

a = []

for _ in range(n):
    a.append(list(map(int, input())))

area = 1

for i in range(n-1):
    for j in range(m):
        k = j+1
        while k < m:
            try: 
                if a[i][j] == a[i][k]:
                    if a[i][j] == a[(i+k-j)][j] == a[(i+k-j)][k]:
                        area = max(((k-j)+1)**2, area)
            except:
                pass
            k += 1

print(area)

#### try except를 쓰지 않고
n,m = map(int,input().rstrip().split())

data = []
ans = 0
for _ in range(n):
    a = []
    for i in input().rstrip():
        a.append(int(i))
    data.append(a)

for i in range(n):
    for j in range(m):
        temp = data[i][j]
        count = 1
        k = 1
        while True:
            if i+k >= n or j+k >= m:
                break
            if temp == data[i+k][j] and temp == data[i][j+k] and data[i+k][j+k]:
                count = k+1
                k += 1
            else:
                k += 1
        ans = max(ans,count)

print(ans**2)


'''
3 3
123
101
200

3 3
112
221
333


5 10
999999999
999999999
999999999
999999999
999999999
'''