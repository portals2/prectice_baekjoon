# 넘파이로 해결 (백준은 넘파이 지원 안함)
# import numpy as np

# by = list(map(int, input().split(' ')))
# bord = np.array([])
# for i in range(by[0]):
#     bord = np.append(bord,list(map(str, input())))
# bord = bord.reshape(by[0],by[1])

# if (7 < by[0] < 51) and (7 < by[1] < 51):
#     c_bord = []
#     a0 = 0
#     a1 = 0

#     for i in range(by[0]-7):
#         for j in range (by[1]-7):
#             c_bord.append(bord[a0:a0+8,a1:a1+8])
#             a1 += 1
#         a0 += 1
#         a1 = 0


#     c1 = np.array([])
#     for i in range(4):
#         for j in range(4):
#             c1= np.append(c1, np.array(['B']))
#             c1= np.append(c1, np.array(['W']))
#         for j in range(4):
#             c1= np.append(c1, np.array(['W']))
#             c1= np.append(c1, np.array(['B']))
#     c1 = c1.reshape(8,8)

#     c2 = np.array([])
#     for i in range(4):
#         for j in range(4):
#             c2= np.append(c2, np.array(['W']))
#             c2= np.append(c2, np.array(['B']))
#         for j in range(4):
#             c2= np.append(c2, np.array(['B']))
#             c2= np.append(c2, np.array(['W']))
#     c2 = c2.reshape(8,8)
#     # print(c1)
#     # print()
#     # print(c2)

#     count = []
#     for i in range(len(c_bord)):
#         s1 = np.array(c_bord[i] == c1)
#         s2 = np.array(c_bord[i] == c2)
#         s1 = s1.reshape(-1)
#         s2 = s2.reshape(-1)
#         count.append(int(list(s1).count(False)))
#         count.append(int(list(s2).count(False)))
#     print(min(count))
#######################################
# 리스트로 해결
c1 = [['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W'],
    ['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B'],
    ['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W'],
    ['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B'],
    ['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W'],
    ['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B'],
    ['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W'],
    ['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B']]

c2 = [['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B'],
    ['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W'],
    ['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B'],
    ['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W'],
    ['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B'],
    ['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W'],
    ['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B'],
    ['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W']]


n, m = list(map(int, input().split(' ')))
bord = []
for i in range(n):
    bord.append(list(map(str, input())))

c_bord = []
for i in range(n-7):  
    for j in range(m-7):  
        c = [row[j:j+8] for row in bord[i:i+8]]
        c_bord.append(c)

k1 = sum(c1, [])
k2 = sum(c2, [])
k = []
coun = 0

for i in range(len(c_bord)):
    c_1 = sum(c_bord[i], [])
    for j in range(len(k1)):
        if c_1[j] != k1[j]:
            coun += 1
    k.append(coun)
    coun = 0
    for j in range(len(k2)):
        if c_1[j] != k2[j]:
            coun += 1
    k.append(coun)
    coun = 0

print(min(k))
#######################################
#축약 및 sys
# import sys

# a, b = map(int, input().split())

# board = []
# result = []
# for i in range(a):
#     board.append(input())

# for n in range(a-7):
#     for m in range(b-7):
#         white=0
#         black=0
#         for x in range(n, n+8):
#             for y in range(m, m+8):
#                 if((x+y)%2==0):
#                     if board[x][y]!= 'W': 
#                         white+=1         
#                     else:
#                         black+=1

#                 else:
#                     if board[x][y]!= 'W':
#                         black+=1
#                     else:
#                         white+=1

#         result.append(white)
#         result.append(black)

# print(min(result))

