# # 1 2 3 4 5 6 7 8 9 10
# # 2 1 3 4 5 6 7 9 10 8

# # 1 2 3 4 5 6 7 8
# # 3 2 7 8 1 4 5 6

# def cercle(start):
#     x=l[start]
#     while True:
#         ll.append((a[start]))
#         start = (a[start])-1
#         if x == l[start]:
#             return 1

# n = int(input())

# for _ in range(n):
#     k = int(input())
#     a = list(map(int, input().split()))
#     l = [i for i in range(1, k+1)]
#     ll =[]
#     c = 0
#     for i in range(k):
#         if l[i] not in ll:
#             c += cercle(i)

#     print(c)


#### 모범답안
import sys
input = sys.stdin.readline

T = int(input())

def dfs(start):
    if visited[start] == True: # 중복체크
        return False
    
    visited[start] = True
    next_node = graph[start] - 1
    dfs(next_node)
    return True # 사이클을 발견하면 True를 return

results = []
for _ in range(T):
    N = int(input())
    graph = list(map(int, input().split()))
    visited = [False] * N

    cnt = 0
    for node in range(0, N):
        if dfs(node) == True:
            cnt += 1
    results.append(cnt)

for result in results:
    print(result)