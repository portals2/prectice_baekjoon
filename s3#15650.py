# from itertools import permutations

# a,b = map(int, input().split(' '))

# for i in permutations(range(1, a+1), b):
#     for j in i:
#         print(j, end=' ')
#     print()



import sys

n,m = map(int,sys.stdin.readline().split())
result = []

def backTracking(start):
  if len(result) == m:
    for i in range(m):
      print(result[i], end=" ")
    print("")
    return

  for i in range(start,n+1):
    if i not in result:
      result.append(i)
      backTracking(i)
      result.pop()
      
backTracking(1)

# 4 2
# 1 2
# 1 3
# 1 4
# 2 3
# 2 4
# 3 4