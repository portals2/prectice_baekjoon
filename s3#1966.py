# # 중요도를 하나씩 가져와서 비교 연산
# # 중요도(1 1 9 1 1 1)가 있다면 (1,9)만 비교
# # 9를 프린트 후 차례로 1을 프린트
# 1 1 9 1 2 1 >>> 4
from collections import deque

t = int(input())

for i in range(t):
    c = 0
    n, m = map(int, input().split())
    r = deque([[int(i), False] for i in ((input()).split())])
    r[m][1] = True

    while True:
        ss =max(r)
        if ss[0] != r[0][0]:
            r.append(r.popleft())
        elif (ss[0] == r[0][0]) and (r[0][1]==True):
            c += 1
            print(c)
            break
        else:
            c+=1
            r.popleft()
        
