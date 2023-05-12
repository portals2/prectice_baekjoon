'''
먼저 들어간 숫자 부터 출력 해야함
'''

import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

N, M, R = map(int, input().split())

data = [[] for _ in range(N + 1)]
visited = [0] * (N + 1) 
count = 1

for _ in range(M):
    u, v = map(int, input().split())
    data[u].append(v)
    data[v].append(u)

for i in data:
    i.sort()


def dfs(r):
    global count
    visited[r] = count
    
    for i in data[r]:
        if visited[i] == 0:
            count += 1
            dfs(i)


dfs(R)
for i in range(1, N + 1):
    print(visited[i], end=' ')
print('')
####

def bfs(r):
    v = [0 for _ in range(N+1)]
    q = [r]
    v[r] = 1
    c = 1
    while len(q) != 0:
        fq = q.pop(0)
        for i in data[fq]:
            if v[i] == 0:
                c += 1
                v[i] = c
                q.append(i)
    return v
     
for i in bfs(R)[1:]:
    print(i, end=' ')
