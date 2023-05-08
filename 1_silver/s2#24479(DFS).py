import sys
sys.setrecursionlimit(10**9)
input = sys.stdin.readline
n,m,r = map(int, input().split(" "))

d = {}
c= [0 for _ in range(n+1)]
cc = 1
for i in range(m):
    a,b = map(int, input().split(" "))
    if (a not in d):
        d[a] = []
    if (b not in d):
        d[b] = []
    d[a].append(b)
    d[b].append(a)

# dfs_l = []
def dfs(r):
    global cc
    # if r not in dfs_l: #한번 더 append하는 과정에서 시간초과
    #     dfs_l.append(r)
    c[r] = cc
    if (r in d):
        for i in sorted(d[r]): #이어진 요소가 없을 경우
            if c[i] == 0:
                cc += 1
                dfs(i)

dfs(r) 

for i in range(1, n + 1):
    print(c[i])


# for i in dfs_l:
#     c[i-1] = c_
#     c_ += 1
# for i in c:
#     print(i)

'''
6 4 1
2 3
1 4
1 5
4 6
'''

         
            
    


# 6 4 1

# 2 3

# 1 4

# 1 5

# 4 6

# 정답 1 4 6 5

# 1 일에 처음 방문
# 0 이에 방문 x
# 0 삼에 방문 x
# 2 4에 두번쨰 방문
# 4 5에 4번째 
# 3 6에 3번째
