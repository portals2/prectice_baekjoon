# 0북쪽 1동 2 남 3서
# 왼쪽으로 돌면서 안가본 곳이면 가봄
# 다 가본 곳이면 현재 바라보는 곳에서 뒤로 한칸 이동
# 다시 왼쪽으로 돌면서 반복
# 뒤가 바다면 정지

n,m = map(int, input().split())

# 1 1 0
p = list(map(int, input().split()))
x = p[0]
y = p[1]
look = p[2]

a = []

for i in range(n):
    a.append(list(map(int, input().split())))

# 북쪽이라는 소리는 현재 위치에서 y-1
# 동쪽은 x + 1
# 남쪽은 y + 1
# 서쪽은 x - 1
result = 0
c = 0
while True:
    if c == 4:
    
    if look == 0:
        if a[x][y-1] == 0:
            look += 1
            c += 1
    elif look == 1:
        if a[x+1][y] == 0:
            look += 1
            c += 1
    elif look == 2:
        if a[x][y+1] == 0:
            look += 1
            c += 1
    elif look == 3:
        if a[x-1][y] == 0:
            look = 0
            c += 1