from itertools import permutations

n = int(input())

a = list(permutations(range(1, n+1), n))

for i in range(len(a)):
    for j in range(n):
        print(a[i][j], end=' ')
    print('')


def dfs(depth):
    global ans

    if depth == n:
        print(*visited)
    else:
        for i in range(n):
            if i + 1 in visited:
                continue
            visited[depth] = i + 1
            dfs(depth + 1)
            visited[depth] = 0


n = int(input())
visited = [0] * n
dfs(0)
