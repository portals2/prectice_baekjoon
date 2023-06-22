n = int(input())
m = int(input())

# # a = [[]] * m 왜 a[0] = 1을 해도 모든 요소에 추가 되는가?
# a = {1:[2,3]}

def jg(n):
    for i in n:
        if len(a[i]) == 0:
            pass
        else:
            if i in l:
                pass
            else:
                l.append(i)
                jg(a[i])

a = {}
for i in range(101):
    a[i+1] = []
for i in range(m):
    x, y = map(int, input().split(' '))
    a[x] += [y]
    a[y] += [x]

l = []
jg(a[1])

if len(set(l)) == 0:
    print(0)
else:
    print(len(set(l))-1)


####리스트로 푼 문제
# import sys
# input = sys.stdin.readline

# V = int(input())
# E = int(input())

# adj = [[] for _ in range(V + 1)]

# print(adj)

# for _ in range(E):
#     v1, v2 = map(int, input().split())
#     adj[v1].append(v2)
#     adj[v2].append(v1)

# visit = [False] * (V + 1)
# visit[1] = True
# ans = 0


# def dfs(curV):
#     global ans
#     ans += 1

#     for neiV in adj[curV]:
#         if visit[neiV]:
#             continue
#         visit[neiV] = True
#         dfs(neiV)


# dfs(1)
# print(ans - 1)