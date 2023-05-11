import sys
sys.setrecursionlimit(10**6) # 재귀 설정
input = sys.stdin.readline

n,m,r = map(int, input().split(' '))

l = [[] for _ in range(n+1)]

for _ in range(m):
    a,b = map(int, input().split(' '))
    l[a].append(b)
    l[b].append(a)

for i in l:
    i.sort(reverse=True)

def bfs(r):
    v = [0 for _ in range(n+1)]
    q = [r]
    v[r] = 1
    c = 1
    while len(q) != 0:
        fq = q.pop(0)
        for i in l[fq]:
            if v[i] == 0:
                c += 1
                v[i] = c
                q.append(i)
    return v
     
for i in bfs(r)[1:]:
    print(i)


# for i in range(1, len(v)):
#     print(v[i])