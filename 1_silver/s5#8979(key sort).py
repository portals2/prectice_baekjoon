# import sys
# input = sys.stdin.readline
# n, k = map(int, input().split(' '))

# l = []

# for i in range(n):
#     l.append(list(map(int, input().split(' '))))

# a = sorted(l, key= lambda x : (x[1], x[2], x[3]), reverse=True)


# r = [[a[0][0],1]]
# c = 1
# c_ = 1

# for i in range(n-1):
#     if a[i][1:] == a[i+1][1:]:
#         r.append([a[i+1][0], c])
#         c_ += 1
#     else:
#         c = c_
#         c += 1
#         r.append([a[i+1][0], c])
#         c_ = c


# for a,b in r:
#     if a == k:
#         print(b)


import sys
input = sys.stdin.readline
n, k = map(int, input().split())
s = []
index = 0
for i in range(n):
    s.append(list(map(int, input().split())))
s.sort(key=lambda x : (-x[1], -x[2], -x[3]))
for i in range(n):
    if s[i][0] == k:
        index = i
for i in range(n):
    if s[index][1:] == s[i][1:]: 
        # 이미 정렬된 list s에서 i번째와 
        # 같다는 소리는 i+1의 순위라는 것이다.
        # 1위와 같다면 0+1
        # 자기 자신이면 해당인덱스+1
        print(i + 1)
        break
