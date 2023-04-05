# import sys
# input = sys.stdin.readline

# V = int(input())
# E = int(input())

# adj = [[] for _ in range(V + 1)]

# adj[0].append(3)

# print(adj)


#### 처음 방법
n = int(input())
m = int(input())

a = [[]] * m #왜 a[0] = 1을 해도 모든 요소에 추가 되는가?
a[0].append(1)
print(a)
