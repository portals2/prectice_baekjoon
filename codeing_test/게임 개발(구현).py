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
p = [[0] * m for _ in range(n)]

for i in range(n):
    a.append(list(map(int, input().split())))

# 행렬의 좌표는 유클리드와 다르다. (ex 3x5)
# (0,0) (0,1) (0,2) (0,3) (0,4)
# (1,0) (1,1) (1,2) (1,3) (1,4)
# (2,0) (2,1) (2,2) (2,3) (2,4)

# 북, 동, 남, 서
n = [(-1,0),(0,1),(1,0),(0,-1)]

def turn_left():
    global look
    look -= 1
    if look == -1:
        look = 3

c = 1
t_t = 0
p[x][y] = 1

while True:
    turn_left()
    nx = x + n[look][0]
    ny = y + n[look][1]

    if a[nx][ny] == 0 and p[nx][ny] == 0:
        x = nx
        y = ny
        p[x][y] = 1
        c += 1
        t_t =0
        continue
    else:
        t_t += 1
        

    if t_t == 4:
        nx = x - n[look][0]
        ny = y - n[look][1]
        if a[nx][ny] == 0:
            x = nx
            y = ny
        else:
            break
        t_t = 0

print(c)
