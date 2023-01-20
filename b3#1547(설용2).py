n = int(input())

a = [1,2,3]

for i in range(n):
    x,y = map(int, input().split(' '))
    if x > y:
        a[a.index(x)], a[a.index(y)] = a[a.index(y)], a[a.index(x)]
    else:
        a[a.index(y)], a[a.index(x)] = a[a.index(x)], a[a.index(y)]
print(a[0]) 


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