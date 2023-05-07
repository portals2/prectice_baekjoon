# t = int(input())

# a = []
# m = 0
# for i in range(t):
#     user = map(str, input().split(' '))
#     y, n = user
#     a.append((int(y), n, m))
#     m+=1
# a.sort(key= lambda x : (x[0], x[2])) 
# for i in range(t):
#     k,y =a[i][0:2]
#     print(k, y)


import sys
t = int(input())
a = []
input=sys.stdin.readline

for i in range(t):
    user = list(map(str, input().split()))
    print(user)
    y, n = user
    a.append((int(y), n))
# x[0]번 만 정렬하면서 다른 위치는 건드리지 않는다.
a.sort(key= lambda x : (x[0])) 
for k, y in a:
    print(k,y)

## 모범 답안 
# x=open(0)
# N = int(x.readline())

# members = [list(x.readline().split()) for i in range(N)]
# members.sort(key=lambda x:int(x[0]))

# for res in members:
#     print(res[0], res[1])