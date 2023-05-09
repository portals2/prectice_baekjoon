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

'''
#### 모범답안
import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

N, M, R = map(int, input().split())

# index 1부터 요소를 저장하기 때문에 n+1을 한다.
data = [[] for _ in range(N + 1)]
# visited 저장을 1부터 하기 때문에 n+1을 한다.
visited = [0] * (N + 1) 
# fleg라고 해도 무관 // vitied을 판단하기 위해
count = 1

for _ in range(M):
    u, v = map(int, input().split())
    # 무방향성이기 때문에 어디서든 접근이 가능해야한다.
    data[u].append(v)
    data[v].append(u)

# 오름차순 정렬이기 때문에 각 요소를 정렬한다.
for i in data:
    i.sort()


def dfs(r):
    global count
    # r index를 0에서 1로 visited 했다는 것을 표시
    visited[r] = count
    
    for i in data[r]:
        if visited[i] == 0:
            count += 1
            dfs(i)


dfs(R)
for i in range(1, N + 1):
    print(visited[i])
'''