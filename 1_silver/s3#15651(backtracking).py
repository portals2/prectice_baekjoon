import sys

n,m = map(int,sys.stdin.readline().split())
result = []

def backTracking(start):
  if len(result) == m:
    for i in range(m):
      print(result[i], end=" ")
    print("")
    return

  for i in range(start,n+1): # 1부터 시작해야함
      result.append(i) # 중복 숫자 제거 if문 삭제
      backTracking(i)
      result.pop()
      
backTracking(1)