import sys
input=sys.stdin.readline
n, m, r = map(int, input().split(' '))

g = [[]for _ in range(n+1)]
q = []
v = [0]*(n+1)

# 무방향 그래프 작성
for i in range(m):
    a,b = map(int, input().split(' '))
    g[a].append(b)
    g[b].append(a)



def bfs(r):
    c = 1 # bfs가 재귀하지 않기 때문에 안에서 한번만 선언 해주면 작동
    q.append(r)
    v[r] = c
    q.append(sorted(g[r]))
    while len(q) != 0:
        q.pop(0)
        if len(q) != 0: # q[0]가 꼭 새로운 요소임을 증명
            for i in q[0]:
                if v[i] == 0:
                    c += 1
                    v[i] = c
                    q.append(sorted(g[i]))
bfs(r)

for i in range(1, n + 1):
    print(v[i])

#### 모범답안
'''
import sys
from collections import deque

n, m, r = map(int, sys.stdin.readline().split())
graph = [[] for _ in range(n+1)]

for _ in range(m):
    a, b = map(int, sys.stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)

for i in range(n+1):
    graph[i].sort()

result = []

def bfs(start):
    count = 1
    visited = [0] * (n+1)
    queue = deque([start]) # 그래프의 인덱스를 저장
    visited[start] = 1
    while queue:
        now = queue.popleft()
        for i in graph[now]:
            if visited[i]:
                continue
            count += 1
            visited[i] = count
            queue.append(i)
    return visited
            
print(*bfs(r)[1:], sep="\n")
'''