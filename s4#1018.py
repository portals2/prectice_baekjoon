import numpy as np

# a = np.array([[1,2,3],[4,5,6]])
# b = np.array([[1,2,3],[4,7,6]])

# print(a==b)
# #좌표별로 8.8씩 나눠서 비교하기

by = list(map(int, input().split(' ')))
bord = np.array([])
for i in range(by[0]):
    bord = np.append(bord,list(map(str, input())))

bord = bord.reshape(by[0],by[1])
c_bord = np.array([])
c1_bord = [] #첫 번쨰 줄의 8*8

x=0
x1=8
a = 1
a1 = 8
for i in range(by[1]-7):
    for j in range(by[0]):
        c_bord= np.append(c_bord, np.array([bord[j,x:x1]])) # j 첫번째
        # c_bord= np.append(c_bord, np.array([bord[j,x:x1]]))
    x1 += 1
    x += 1
    c_bord = c_bord.reshape(-1,8)
    
    c1_bord.append(c_bord[a:a1])
    print(c_bord[a:a1])
    a = a1
    a1 = a1 + 8
# print(c1_bord[0])
# print(c1_bord[4])

c1 = np.array([]) #bw...
for i in range(4):
    for j in range(4):
        c1= np.append(c1, np.array(['b']))
        c1= np.append(c1, np.array(['w']))
    for j in range(4):
        c1= np.append(c1, np.array(['w']))
        c1= np.append(c1, np.array(['b']))
c1 = c1.reshape(8,8)
# print(c1)

c2 = np.array([]) #wb...
for i in range(4):
    for j in range(4):
        c2= np.append(c2, np.array(['w']))
        c2= np.append(c2, np.array(['b']))
    for j in range(4):
        c2= np.append(c2, np.array(['b']))
        c2= np.append(c2, np.array(['w']))
c2 = c2.reshape(8,8)
# print(c2)




