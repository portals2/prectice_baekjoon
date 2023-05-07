# b1#10989번과 같다.
# 차이점은 메모리 제한이 다르다.
# 256MB 라서 그낭 리슽트에 sort()해도 된다.

import sys
n = int(input())

count={}
for i in range(n):
    a = int(sys.stdin.readline())
    if a not in count:
        count[int(a)]=1
    else:
        count[a] += 1

for i in sorted(count):
    for j in range(count[i]):
        print(i)

