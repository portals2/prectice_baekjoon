import sys

n,m = map(int,sys.stdin.readline().split())
result = []
 # DFS에서 if문으로 제약을 두어\
 # 모든 경우를 확인하지 않는 것이 백트레킹
def backTracking(start):
  if len(result) == m:
    for i in range(m):
      print(result[i], end=" ")
    print("")
    return

    # dfs 부분
  for i in range(start,n+1): 
      result.append(i) 
      backTracking(i)
      # 분기를 만나 부모노드로 올라오면
      # 자식노드를 삭제한다.
      result.pop() 

      
backTracking(1)

# 깊이 우선 탐색
# root 1
# 2 3 4