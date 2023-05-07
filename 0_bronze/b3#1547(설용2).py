n = int(input())

a = [1,2,3]

for i in range(n):
    x,y = map(int, input().split(' '))
    if x > y:
        a[a.index(x)], a[a.index(y)] = a[a.index(y)], a[a.index(x)]
    else:
        a[a.index(y)], a[a.index(x)] = a[a.index(x)], a[a.index(y)]
print(a[0]) 

# ############# 왜 인덱스를 따로 저장하면 되는거지??
# li = [1, 2, 3]
# for _ in range(int(input())):
#     X, Y = map(int, input().split())
#     x = li.index(X)
#     y = li.index(Y)
#     li[x], li[y] = li[y], li[x]
# print(li[0])

# # 리스트만을 이용해서(이해하기)
# ball = [0,1,0,0]
# n = int(input())
# for i in range(n):
#     x, y = map(int, input().split())
#     ball[x], ball[y] = ball[y], ball[x]
    
# print(ball.index(1))

# ############# 참신한 발상
# import sys
# input=sys.stdin.readline

# M = int(input())

# pos = 1 # 공이 있는 위치

# for i in range(M) :
#     X, Y = map(int, input().split())

#     if X == pos :
#         pos = Y
#         continue

#     if Y == pos :
#         pos = X
#         continue

# print(pos)