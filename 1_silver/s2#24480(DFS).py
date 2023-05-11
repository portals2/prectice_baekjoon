'''
내림차순
리스트로 풀기
[[], [4, 2], [4, 3, 1], [4, 2], [3, 2, 1], []]
'''

import sys
sys.setrecursionlimit(10**6) # 재귀 설정
input = sys.stdin.readline

n,m,r = map(int, input().split(' '))

l = [[] for _ in range(n+1)]
v = [0 for _ in range(n+1)]
c = 1

for _ in range(m):
    a,b = map(int, input().split(' '))
    l[a].append(b)
    l[b].append(a)

for i in l:
    i.sort(reverse=True)

def dfs(r):
    global c
    v[r] = c
    for i in l[r]:
        if v[i] == 0:
            c += 1
            dfs(i)
            
dfs(r)

for i in range(1, len(v)):
    print(v[i])
    